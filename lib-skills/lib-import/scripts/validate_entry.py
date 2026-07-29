#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required. Run this script with the aiday environment or install PyYAML.") from exc


READING_STATES = {"未读", "在读", "已读"}
SCHEMAS: dict[str, dict[str, set[str]]] = {
    "paper": {
        "required": {
            "type",
            "doc_type",
            "title",
            "first_author",
            "corresponding_authors",
            "other_authors",
            "year",
            "venue",
            "status",
            "ai_topics",
            "labels",
            "index",
            "created",
        },
        "lists": {"first_author", "corresponding_authors", "other_authors", "ai_topics", "labels", "index"},
    },
    "thesis": {
        "required": {
            "type",
            "doc_type",
            "title",
            "author",
            "supervisor",
            "year",
            "institution",
            "status",
            "ai_topics",
            "labels",
            "index",
            "created",
        },
        "lists": {"author", "supervisor", "ai_topics", "labels", "index"},
    },
    "manual": {
        "required": {
            "type",
            "doc_type",
            "title",
            "target_type",
            "target_name",
            "vendor",
            "version",
            "year",
            "index",
            "created",
        },
        "lists": {"index"},
    },
    "book": {
        "required": {
            "type",
            "doc_type",
            "title",
            "creators",
            "year",
            "publisher",
            "edition",
            "index",
            "created",
        },
        "lists": {"creators", "index"},
    },
    "proposal": {
        "required": {"type", "doc_type", "title", "author", "year", "index", "created"},
        "lists": {"index"},
    },
    "other": {
        "required": {"type", "doc_type", "title", "read_status", "topics", "index", "created", "updated"},
        "lists": {"topics", "index"},
    },
}
FORBIDDEN_FRONTMATTER_LINK_FIELDS = {"source_note", "source_pdf", "source_docx"}
INTERMEDIATE_PATTERN = re.compile(
    r"(?:^|[_-])(middle|model|layout|span)(?:[_-]|\.|$)|(?:middle|model)_?list\.json$",
    re.IGNORECASE,
)
IMAGE_PATTERN = re.compile(r"!\[[^\]]*\]\((images/[^)\s]+)(?:\s+[^)]*)?\)")
WIKILINK_PATTERN = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


@dataclass
class Report:
    source_dir: str
    doc_type: str | None = None
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checks: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def as_dict(self) -> dict[str, object]:
        return {
            "ok": self.ok,
            "source_dir": self.source_dir,
            "doc_type": self.doc_type,
            "errors": self.errors,
            "warnings": self.warnings,
            "checks": self.checks,
        }


def parse_frontmatter(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.DOTALL)
    if not match:
        raise ValueError("missing or malformed YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return data, text[match.end() :]


def has_frontmatter(path: Path) -> bool:
    return path.read_text(encoding="utf-8").startswith("---")


def resolve_wikilink(source_dir: Path, target: str) -> bool:
    candidate = source_dir / unquote(target)
    if candidate.exists():
        return True
    if candidate.suffix:
        return False
    return any(path.stem == candidate.name for path in source_dir.iterdir() if path.is_file())


def find_vault_root(source_dir: Path) -> Path | None:
    for candidate in (source_dir, *source_dir.parents):
        if (candidate / "01 Sources").exists() and (candidate / "02 Index").exists():
            return candidate
    return None


def validate(source_dir: Path) -> Report:
    source_dir = source_dir.expanduser().resolve()
    report = Report(source_dir=str(source_dir))
    if not source_dir.is_dir():
        report.errors.append(f"source directory does not exist: {source_dir}")
        return report

    rc_files = sorted(source_dir.glob("RC - *.md"))
    main_files = sorted(source_dir.glob("MD - *.md"))
    chapter_files = sorted(source_dir.glob("chap.*.md"))
    if len(rc_files) != 1:
        report.errors.append(f"expected exactly one RC file, found {len(rc_files)}")
    if len(main_files) != 1:
        report.errors.append(f"expected exactly one main Markdown file, found {len(main_files)}")
    if not rc_files:
        return report

    rc_path = rc_files[0]
    try:
        frontmatter, rc_body = parse_frontmatter(rc_path)
    except (ValueError, yaml.YAMLError) as exc:
        report.errors.append(f"{rc_path.name}: {exc}")
        return report

    doc_type = frontmatter.get("doc_type")
    report.doc_type = doc_type if isinstance(doc_type, str) else None
    if frontmatter.get("type") != "reference_card":
        report.errors.append("RC type must be reference_card")
    if report.doc_type not in SCHEMAS:
        report.errors.append(f"unsupported or missing doc_type: {doc_type!r}")
    else:
        schema = SCHEMAS[report.doc_type]
        keys = set(frontmatter)
        missing = sorted(schema["required"] - keys)
        if missing:
            report.errors.append(f"missing required frontmatter fields: {', '.join(missing)}")
        if report.doc_type != "other":
            unexpected = sorted(keys - schema["required"])
            if unexpected:
                report.errors.append(f"unexpected fields for strict {report.doc_type} schema: {', '.join(unexpected)}")
        for key in sorted(schema["lists"]):
            if key in frontmatter and not isinstance(frontmatter[key], list):
                report.errors.append(f"{key} must be a YAML list")

    legacy_links = sorted(FORBIDDEN_FRONTMATTER_LINK_FIELDS & set(frontmatter))
    if legacy_links:
        report.errors.append(f"source links must be in RC body, not frontmatter: {', '.join(legacy_links)}")

    if report.doc_type in {"paper", "thesis"}:
        if frontmatter.get("status") not in READING_STATES:
            report.errors.append("status must be 未读, 在读, or 已读")
    if report.doc_type == "other":
        if frontmatter.get("read_status") not in READING_STATES:
            report.errors.append("read_status must be 未读, 在读, or 已读")
    if report.doc_type in {"manual", "book", "proposal"} and (
        "status" in frontmatter or "read_status" in frontmatter
    ):
        report.errors.append(f"{report.doc_type} must not contain reading status")

    for path in [*main_files, *chapter_files]:
        if has_frontmatter(path):
            report.errors.append(f"source Markdown must not contain frontmatter: {path.name}")

    markdown_files = [*main_files, *chapter_files]
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for target in IMAGE_PATTERN.findall(text):
            image_path = source_dir / unquote(target)
            if not image_path.exists():
                report.errors.append(f"missing image referenced by {path.name}: {target}")

    intermediate_files = [
        path.name for path in source_dir.rglob("*") if path.is_file() and INTERMEDIATE_PATTERN.search(path.name)
    ]
    if intermediate_files:
        report.errors.append(f"MinerU intermediate files found: {', '.join(sorted(intermediate_files))}")

    links = WIKILINK_PATTERN.findall(rc_body)
    broken_links = [target for target in links if not resolve_wikilink(source_dir, target)]
    if broken_links:
        report.errors.append(f"broken RC body links: {', '.join(sorted(set(broken_links)))}")
    if main_files and not any(
        main_files[0].name in target or main_files[0].stem == Path(target).stem for target in links
    ):
        report.warnings.append("RC body does not appear to link the main Markdown file")

    source_files = [
        path for path in source_dir.iterdir() if path.is_file() and path.suffix.lower() in {".pdf", ".docx"}
    ]
    if not source_files:
        report.warnings.append("no PDF or DOCX source file found")
    elif not any(
        source.name in target or source.stem == Path(target).stem for source in source_files for target in links
    ):
        report.warnings.append("RC body does not appear to link a PDF or DOCX source file")

    vault_root = find_vault_root(source_dir)
    if vault_root is None:
        report.warnings.append("could not locate LibVault root; Import log and index pages were not checked")
    else:
        if not (vault_root / "98 Logs" / "Import.md").exists():
            report.warnings.append("98 Logs/Import.md does not exist")
        if not (vault_root / "02 Index" / "Doc Types" / "Reference Cards.md").exists():
            report.warnings.append("Reference Cards Dataview page does not exist")

    report.checks.extend(
        [
            f"RC: {rc_path.name}",
            f"main Markdown files: {len(main_files)}",
            f"chapter files: {len(chapter_files)}",
            f"source files: {len(source_files)}",
            f"RC body wikilinks: {len(links)}",
        ]
    )
    return report


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read-only validation for one LibVault source folder.")
    parser.add_argument("--source-dir", required=True, help="Path to one LibVault document source folder.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a text report.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    report = validate(Path(args.source_dir))
    if args.json:
        print(json.dumps(report.as_dict(), ensure_ascii=False, indent=2, default=str))
    else:
        print("OK" if report.ok else "FAILED")
        print(f"source_dir: {report.source_dir}")
        print(f"doc_type: {report.doc_type or 'unknown'}")
        for label, items in (("errors", report.errors), ("warnings", report.warnings), ("checks", report.checks)):
            if items:
                print(f"{label}:")
                for item in items:
                    print(f"- {item}")
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
