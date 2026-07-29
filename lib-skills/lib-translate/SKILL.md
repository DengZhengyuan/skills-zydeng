---
name: lib-translate
description: >
  中文 LibVault paper 双语正文 skill。用于对 LibVault 中 `01 Sources` 内已入库 paper 的 `MD - ...`
  主 Markdown 逐段插入中文译文：保留英文正文，在每个普通英文叙述段落下方新增 `译文：...`；通过同文件夹
  `RC - ...` 的 `doc_type: paper` 确认目标，跳过 RC、章节、索引、日志、模板、公式、表格、图片、details OCR、references 和 PDF。
---

# lib-translate

## 概述

`lib-translate` 用于把 LibVault 中已入库 paper 的英文主 Markdown 改成中英双语阅读版。默认直接在原 paper 主 Markdown 中插入中文译文，不另建副本。

核心格式固定为：保留英文段落，在其下一段新增：

```markdown
译文：<中文译文>
```

## 触发场景

以下请求应触发本 skill：

- `用 lib-translate 翻译这篇 paper`
- `给这个 paper 加中文译文`
- `把正文翻译成中文放每段下面`
- `将这篇文章做成中英双语`
- 显式调用 `$lib-translate`

## 固定边界

- 只处理 LibVault `01 Sources/**/MD - <doc-key>.md` 中已入库 paper 的主 Markdown。
- 必须通过同文件夹 `RC - <doc-key>.md` frontmatter 中的 `type: reference_card` 和 `doc_type: paper` 确认目标类型。
- 不处理 `RC - ...md`、`chap.*.md`、`02 Index/`、`98 Logs/`、`99 Templates/`、PDF 或图片文件。
- 如果输入是 PDF、MinerU 输出目录或尚未入库材料，先提示用户使用 `lib-import` 入库。
- 不改 RC frontmatter、DOI、URL、Source PDF、图片链接或原英文正文。
- 不翻译或不改写公式、表格、代码块、`<details>...</details>` OCR 内容、references。
- 不为了翻译统一 LaTeX 风格或修公式；如果发现明显格式/公式问题，只报告或建议先按 `lib-import` 的正文/公式体检规则修复。

## 输入定位

用户可能提供：

- paper 主 Markdown 路径。
- paper 文件夹路径。
- Obsidian wikilink 或文章标题。

处理前先确认目标是 paper 主 Markdown：

- 文件名必须匹配 `MD - <doc-key>.md`，并位于 `01 Sources` 下的 source folder。
- 同级必须存在 `RC - <doc-key>.md`；同级通常有 `images/` 和 `PDF - <doc-key>.pdf`。
- 以 RC frontmatter 判断：`type: reference_card` 且 `doc_type: paper`。如果无法确认，不要根据正文猜测执行。

## 翻译范围

翻译普通英文叙述正文，包括：

- `ABSTRACT`
- `INTRODUCTION`
- 方法、模型、结果、讨论、结论等正文段落
- 必要的短说明段落

默认不翻译：

- headings
- DOI / URL / Source PDF 元数据行
- `Keywords:` 行
- 图表 caption
- Acknowledgement
- Appendix
- `# REFERENCES` 及其后文

如果用户明确要求翻译 caption、Keywords 或 Acknowledgement，可以处理这些普通文本行，但仍跳过公式、表格、图片和 details。

## 块级解析规则

按块解析 Markdown，再决定是否翻译。至少识别并跳过：

- Markdown headings。
- `$$...$$` 公式块。
- fenced code blocks。
- `![](images/...)` 图片引用。
- HTML 表格和 Markdown 表格。
- `<details>...</details>` 块。
- `# REFERENCES` 及其后所有内容。
- 已有 `译文：` 段落。

只翻译普通英文段落。一个普通段落可以跨多行；插入译文时放在该英文段落后的独立段落中。

## 插入规则

- 若英文段落下一段已经以 `译文：` 开头，则跳过，保证重复执行不会重复添加译文。
- 译文必须紧跟对应英文段落，中间不插入额外标题或说明。
- 保留英文段落中的公式、变量、单位、引用、缩写和专有名词。
- 技术术语优先准确稳定，可采用“中文 + 原术语”方式，例如 `parcel`、`DEM`、`BGK`、`MP-PIC`、`granular temperature`。
- 不改写英文原文；如果英文有明显 OCR 错误且影响翻译，在最终回复中列为可疑位置，不擅自重写。

## 验证

完成前至少检查：

- 目标 `MD - ...` 仍不含 YAML frontmatter。
- 同文件夹 `RC - ...` 仍存在，且 `doc_type: paper`。
- Source PDF 行仍存在。
- 所有 `![](images/...)` 引用仍能在同级 `images/` 中找到。
- `译文：` 没有出现在 `<details>...</details>` 或 `# REFERENCES` 后。
- 没有连续重复的 `译文：` 段落。
- 抽查摘要、引言、结论各 1-2 段，确认译文紧跟英文段落。
- 如果当前目录是 Git 工作树，运行 `git diff --check`；否则做文件级结构检查并说明。

## 输出给用户

最终回复应简短说明：

- 处理的 paper 主 Markdown。
- 新增译文段落数。
- 跳过的已有译文段落数。
- 未翻译块类型，例如公式、表格、图片、details、references。
- 是否发现疑似 OCR、格式或公式问题。
