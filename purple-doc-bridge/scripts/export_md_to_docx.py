#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = SKILL_DIR / "assets" / "templates" / "gas-solid-fluidization-template.docx"
TEMP_ROOT = Path("/private/tmp/purple-doc-bridge")


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    lines = text.splitlines()
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "\n".join(lines[index + 1 :]).lstrip() + "\n"
    return text


def normalize_wikilinks(text: str) -> str:
    text = re.sub(r"!\[\[([^\]]+)\]\]", lambda m: f"[attachment: {m.group(1).strip()}]", text)

    def replace_link(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        if "|" in target:
            return target.split("|", 1)[1].strip()
        return target

    return re.sub(r"\[\[([^\]]+)\]\]", replace_link, text)


def flatten_callouts(text: str) -> str:
    output: list[str] = []
    callout_marker = re.compile(r"^>\s*\[![A-Za-z0-9_-]+\][+-]?\s*(.*)$")
    for line in text.splitlines():
        marker = callout_marker.match(line)
        if marker:
            title = marker.group(1).strip()
            if title:
                output.append(f"> {title}")
            continue
        if line.startswith("> "):
            output.append(line[2:])
        elif line == ">":
            output.append("")
        else:
            output.append(line)
    return "\n".join(output).rstrip() + "\n"


def read_sources(paths: list[Path]) -> str:
    chunks: list[str] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        text = flatten_callouts(normalize_wikilinks(strip_frontmatter(text)))
        chunks.append(text.strip())
    return "\n\n".join(chunk for chunk in chunks if chunk) + "\n"


def run(cmd: list[str], *, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
    )


def verify_docx(path: Path, title: str | None) -> str:
    result = run(["pandoc", str(path), "-t", "plain"], capture=True)
    plain = result.stdout.strip()
    if not plain:
        raise RuntimeError("pandoc plain-text verification returned empty output")
    if title and title not in plain[:2000]:
        raise RuntimeError(f"title not found in DOCX plain-text verification: {title}")
    return plain


def build_docx(
    sources: list[Path],
    output: Path,
    *,
    title: str | None,
    template: Path | None,
    toc: bool,
    verify: bool,
) -> Path:
    if shutil.which("pandoc") is None:
        raise RuntimeError("pandoc is required but was not found on PATH")

    for source in sources:
        if not source.exists():
            raise FileNotFoundError(source)

    if template is not None and not template.exists():
        raise FileNotFoundError(template)

    output = output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    TEMP_ROOT.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="export-", dir=TEMP_ROOT) as raw_tmp:
        tmp = Path(raw_tmp)
        clean_md = tmp / "cleaned-source.md"
        temp_docx = tmp / output.name
        clean_md.write_text(read_sources(sources), encoding="utf-8")

        cmd = ["pandoc", str(clean_md), "-o", str(temp_docx)]
        if template is not None:
            cmd.extend(["--reference-doc", str(template)])
        if title:
            cmd.extend(["--metadata", f"title={title}"])
        if toc:
            cmd.extend(["--toc", "--toc-depth=2"])

        run(cmd)

        if verify:
            verify_docx(temp_docx, title)

        shutil.copy2(temp_docx, output)

    return output


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export Purple Sys Markdown to a templated DOCX.")
    parser.add_argument("--source", action="append", required=True, help="Markdown source path. Repeat for multiple files.")
    parser.add_argument("--output", required=True, help="Final DOCX output path.")
    parser.add_argument("--title", help="Document title for metadata and verification.")
    parser.add_argument("--template", default=str(DEFAULT_TEMPLATE), help="DOCX reference template path.")
    parser.add_argument("--no-template", action="store_true", help="Do not pass a pandoc reference-doc.")
    parser.add_argument("--toc", action="store_true", help="Include a table of contents.")
    parser.add_argument("--no-verify", action="store_true", help="Skip pandoc plain-text round-trip verification.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    template = None if args.no_template else Path(args.template).expanduser()
    try:
        output = build_docx(
            [Path(p).expanduser() for p in args.source],
            Path(args.output).expanduser(),
            title=args.title,
            template=template,
            toc=args.toc,
            verify=not args.no_verify,
        )
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
