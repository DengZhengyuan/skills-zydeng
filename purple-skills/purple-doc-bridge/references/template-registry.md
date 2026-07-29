# Template Registry

## Default Word Template

- Purpose: gas-solid fluidization group / department-style Word output.
- Bundled asset: `assets/templates/gas-solid-fluidization-template.docx`
- Original source at creation time: `/Users/zydeng/Downloads/气固流态化课题组文件模板.docx`
- Added to this skill as a stable default so export tasks do not depend on `Downloads`.

## When To Use

Use the bundled template by default when the user asks for:

- `课题组模板`
- `气固流态化课题组文件模板`
- `按照之前那个 Word 模板`
- generic Purple Sys Markdown -> Word export with no stronger template instruction

Ask before using another template when:

- the user mentions a specific project, school, proposal, contract, journal, or externally supplied template
- the target document has strict institutional formatting
- the user says the bundled template is stale or wants to update the style

## Update Procedure

To update the bundled default:

1. Confirm the new reference `.docx` path with the user.
2. Replace `assets/templates/gas-solid-fluidization-template.docx` with that file.
3. Run a small Markdown -> DOCX export using `scripts/export_md_to_docx.py`.
4. Verify the generated DOCX by render check if available, otherwise by `pandoc -t plain`.
5. Update this registry if the source path, purpose, or naming convention changes.

Do not overwrite the bundled template from a transient output document unless the user explicitly says it is the new template.
