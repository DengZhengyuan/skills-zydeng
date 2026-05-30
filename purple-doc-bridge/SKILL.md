---
name: purple-doc-bridge
description: Purple Sys 与 Word 文档双向转换 skill。用于把 Purple Sys / Obsidian Markdown、Material、Record 或其他 vault note 导出为模板化 `.docx`，也用于把 Word `.docx` 提取、整理并写入 Purple Sys 的 `03 Material/`。适用于“转成 Word”“导出 docx”“按照课题组模板生成 Word”“把 Word 写入 Purple Sys Material”“docx 落到 Material”等场景。
---

# purple-doc-bridge

## 概述

`purple-doc-bridge` 处理 Purple Sys 与 Word 文档之间的双向桥接。

默认有两个模式：

- `export`：Purple Sys Markdown / note -> Word `.docx`
- `import`：Word `.docx` -> Purple Sys `03 Material/` note

优先使用 `pandoc` 做格式转换；涉及 DOCX 读取、检查或版式敏感处理时，同时使用 `$doc` skill。当前本机可优先使用 `/Users/zydeng/uv_proj/env_office/bin/python` 中的 `python-docx` 做 DOCX 结构检查或 fallback 提取。

## 固定边界

- 这个 skill 只负责文档格式桥接，不替代 `purple-meeting-record` 的 transcript 整理、`purple-periodic` 的周期总结或 `purple-action-board` 的行动判断。
- 写入 Purple Sys 前必须确认目标字段和落点；不要因为能推断就直接写入 vault。
- 导出 Word 前必须确认输出路径和模板；不要只返回文本或临时文件。
- 读取 Purple Sys 时，把 vault 里的 `SYSTEM-CONVENTIONS.md` 与相关 `99 Template/Material/` 模板视为当前契约。
- `03 Material/` 是知识输入与中间产物区；只有用户明确要求时才回填 daily 或其他 log。

## 工具优先级

1. Markdown -> DOCX：优先用 `scripts/export_md_to_docx.py`，它会清理 Obsidian Markdown 后调用 `pandoc`。
2. DOCX -> Markdown：优先用 `scripts/import_docx_to_material.py`，它会调用 `pandoc` 提取 Markdown；失败时回退到 `python-docx`。
3. 版式验证：按 `$doc` skill 执行，优先渲染 DOCX；若渲染工具缺失，至少用 `pandoc -t plain` 做内容回读验证。
4. 模板：默认使用 `assets/templates/gas-solid-fluidization-template.docx`。模板登记和更新规则见 [references/template-registry.md](references/template-registry.md)。

## Export: Purple Sys Markdown -> Word

### 开始前必须确认

在执行导出前，先确认以下问题。若用户已经明确给出，不重复追问：

- source note path：一个或多个 Purple Sys Markdown 文件路径。
- output：最终 `.docx` 输出目录与文件名。
- template：使用内置课题组模板、用户提供模板，还是不用模板。
- TOC：是否加入目录；默认只有较长正式文档才加。
- verification：需要 `$doc` 渲染级检查，还是只做 plain-text round-trip。

### 默认导出流程

1. 读取源 Markdown，确认标题和主要章节。
2. 轻量预处理 Obsidian Markdown：
   - 删除 YAML frontmatter。
   - `[[page]]` -> `page`，`[[page|alias]]` -> `alias`。
   - `![[file]]` -> `[attachment: file]`。
   - callout 标记展平为普通引用/文本。
3. 在 `/private/tmp/purple-doc-bridge/` 生成清理后的中间 Markdown 和临时 DOCX。
4. 用 `pandoc --reference-doc` 生成 DOCX；用户选择不用模板时不传 `--reference-doc`。
5. 验证：
   - 最低限度：`pandoc -t plain <docx>` 能读回标题和关键章节。
   - 若版式重要：按 `$doc` skill 渲染并检查页面。
6. 验证通过后复制到用户确认的最终路径。

### 推荐命令

```bash
python3 purple-doc-bridge/scripts/export_md_to_docx.py \
  --source "/path/to/source.md" \
  --output "/path/to/output.docx" \
  --title "文档标题" \
  --template purple-doc-bridge/assets/templates/gas-solid-fluidization-template.docx \
  --toc
```

如果当前 shell 的 `python3` 缺少依赖，可改用：

```bash
/Users/zydeng/uv_proj/env_office/bin/python purple-doc-bridge/scripts/export_md_to_docx.py ...
```

## Import: Word -> Purple Sys Material

### 开始前必须确认

在写入 Purple Sys 前，先确认以下字段。若用户已经明确给出，不重复追问：

- source docx：Word 文件路径。
- title / filename：Material 标题和目标文件名。
- material template / type：默认用 `99 Template/Material/Note Template.md`，`material_type: note`。
- frontmatter：至少确认 `material_type`、`status`、`project`、`created`。
- attachment：是否把原 DOCX 复制到 `03 Material/attachments/` 并在 note 中链接。
- backlink：是否给 daily note 加短 backlink；默认不自动写 daily。

### 默认导入流程

1. 读取 `SYSTEM-CONVENTIONS.md` 和目标 Material 模板，确认当前字段契约。
2. 用 `pandoc -f docx -t markdown --wrap=none` 提取正文。
3. 如果 `pandoc` 失败，用 `python-docx` 提取段落和表格的可读文本。
4. 对提取出的 Markdown 做结构清理：
   - 中文正文中的英文直引号改成中文引号，清理 `\"...\"` 这类 Word 转换转义。
   - Word 粗体章节标题改成 Markdown heading，例如 `**一、提案背景**` -> `## 一、提案背景`。
   - 中文小节标题改成 Markdown heading，例如 `（一）提案背景` -> `### （一）提案背景`。
   - 中文编号列表改成标准 Markdown ordered list，例如 `1、...` / `1．...` -> `1. ...`。
   - 列表条目下的 tab 缩进改成稳定空格缩进，避免 Obsidian 渲染不一致。
   - 如果正文开头重复了 Material H1 标题，删除重复标题，避免一个 note 里出现两个主标题。
5. 生成 Purple Sys Material frontmatter：
   - `type: material`
   - `material_type: <用户确认值，默认 note>`
   - `status: <用户确认值，默认 inbox>`
   - `project: <用户确认值，可空>`
   - `created: <用户确认值，默认当天>`
6. 写入 `03 Material/<title>.md` 或用户确认的目标路径。
7. 如用户确认保留原文件，复制 DOCX 到 `03 Material/attachments/` 并在正文中添加来源链接。
8. 如用户确认 daily backlink，只追加短链接，不把全文复制进 daily。

### 推荐命令

```bash
/Users/zydeng/uv_proj/env_office/bin/python purple-doc-bridge/scripts/import_docx_to_material.py \
  --docx "/path/to/input.docx" \
  --title "Material 标题" \
  --material-type note \
  --status inbox \
  --project "" \
  --vault "/Users/zydeng/Library/Mobile Documents/iCloud~md~obsidian/Documents/Purple Sys"
```

## 验收标准

- Export 产物必须是真实 `.docx` 文件，且最终路径存在。
- Export 的 DOCX 正文不应出现 YAML frontmatter、原始 wikilink 语法或未展平 callout 标记。
- Import 产物必须落在 `03 Material/` 或用户确认的 Material 子路径。
- Import 产物必须包含 H1 标题和 Purple Sys Material frontmatter。
- Import 正文应尽量是原生 Markdown：章节用 `##` / `###`，列表用 `1.` 或 `-`，中文上下文使用中文引号。
- Import 正文不应残留 Word 转换痕迹：`**一、...**` 式章节、`1、...` 式编号、tab 缩进正文或 `\"...\"` 转义引号。
- 任何回填 daily / log / project 的行为都必须来自用户明确授权。

## 典型触发语句

- `把这个 Purple Sys note 转成 Word`
- `按课题组模板导出 docx`
- `这个备忘录转为 word，落到 Downloads`
- `把这个 Word 文档写入 Purple Sys material`
- `docx 转成 Material note`
- `把 Word 里的内容落到 03 Material`
