# LibVault 入库契约

本文件记录 `lib-import` 的可调整规则。后续修改 LibVault 目录、字段、索引、正文链接或拆分策略时，优先改这里。

## 目录层

LibVault 至少包含以下目录层：

```text
01 PDF Library/
02 Paper Markdown/
03 Index/
  Projects/
  People/
  Software/
  Topics/
  Reading Status/
```

日期分组规则：

- PDF 原件按入库日期分组。
- Markdown 与图片按 MinerU 处理日期或整理日期分组。

推荐结构：

```text
01 PDF Library/YYYY/YYYY-MM/YYYY-MM-DD/<pdf-file>.pdf

02 Paper Markdown/YYYY/YYYY-MM/YYYY-MM-DD/<doc-key>/
  <doc-key>.md
  images/
```

guide/manual/book 拆分后：

```text
02 Paper Markdown/YYYY/YYYY-MM/YYYY-MM-DD/<doc-key>/
  <doc-key>.md
  <doc-key> - 000 Front Matter.md
  <doc-key> - 001 <chapter-title>.md
  <doc-key> - 002 <chapter-title>.md
  images/
```

## Paper frontmatter

论文条目必须以轻量 frontmatter 开头：

```yaml
---
type: paper
authors: []
corresponding_author: []
publish_year:
read_status: "未读"
topics: []
---
```

字段规则：

- `authors` 使用作者列表；不确定时留空。
- `corresponding_author` 使用列表；只有明确识别到通讯作者时填写。
- `publish_year` 使用论文发表年份；不确定时留空。
- `read_status` 新入库默认 `未读`。
- `topics` 只放稳定主题词，不放 DOI、venue、项目、软件或长摘要。

不要把 `title`、`doi`、`url`、`source_pdf`、`abstract`、`venue`、`mineru_method`、`processed_date`、`ingest_date`、`projects`、`people`、`software`、`tags` 写入 paper frontmatter。

## Paper 正文链接

Paper 正文开头固定为：

```markdown
# <paper title>

- DOI: [10.xxxx](https://doi.org/10.xxxx)
- URL: <https://...>
- Source PDF: [[01 PDF Library/.../<file>.pdf|PDF]]
```

规则：

- DOI、URL、Source PDF 放在 H1 title 下方。
- DOI 使用普通 Markdown 链接。
- URL 使用裸链接尖括号。
- Source PDF 使用 Obsidian wikilink，并使用 `PDF` 作为显示名。
- 如果 DOI、URL 或 PDF 路径无法可靠识别，写 `待核对`，不要编造。
- 若 MinerU 输出在 H1 前放了首页图片，导入时把首页图片移动到上述链接块之后。

## Paper citation 后处理

MinerU 可能把括号内 citation 错误拆成跨段落文本。导入 paper 时做保守修复：

- 只处理普通正文段落。
- 不处理 headings、tables、images、math blocks、code blocks。
- 当上一行仍处于括号 citation 内，且下一非空行以年份开头时，合并为同一段。
- 清理 citation 内多余空格，但不改写作者名、年份或引用内容。

典型修复：

```markdown
(Deen et al.

2007)
```

改为：

```markdown
(Deen et al. 2007)
```

```markdown
(Schneiderbauer 2020,

2022)
```

改为：

```markdown
(Schneiderbauer 2020, 2022)
```

## Guide/manual frontmatter

guide、manual、book 的父级 note 使用：

```yaml
---
type: guide
title: ""
source_pdf: ""
processed_date:
ingest_date:
read_status: "未读"
software: []
topics: []
tags:
  - guide
---
```

章节 note 使用相同基础信息，并增加章节字段：

```yaml
---
type: guide_chapter
parent: ""
title: ""
chapter: ""
source_pdf: ""
processed_date:
ingest_date:
read_status: "未读"
software: []
topics: []
tags:
  - guide
---
```

父级 note 负责目录和章节 wikilink，章节 note 负责正文内容。

## Other frontmatter

无法稳定归类的资料使用：

```yaml
---
type: other
title: ""
source_pdf: ""
processed_date:
ingest_date:
read_status: "未读"
topics:
  - 待分类
tags:
  - imported
---
```

正文顶部保留简短提示，说明该条目需要后续分类。

## 阅读状态

`read_status` 只允许三个值：

- `未读`
- `正在读`
- `已读`

新入库默认 `未读`。阅读状态索引放在：

```text
03 Index/Reading Status/
```

## 图片规则

- 每个文档一个文件夹。
- 每个文档文件夹内最多一个共享 `images/` 文件夹。
- paper 的主 Markdown 与 `images/` 同级。
- guide/manual/book 的父级 note、章节 note 与 `images/` 同级。
- 保留 MinerU 原生相对引用：

```markdown
![](images/<file>)
```

不把图片移动到全局 attachments，不按章节复制图片。

## 索引规则

索引目录：

```text
03 Index/Projects/
03 Index/People/
03 Index/Software/
03 Index/Topics/
03 Index/Reading Status/
```

索引 note 只做引用和短上下文：

```markdown
- [[Paper or Guide Title]] - 简短说明
```

不要在多个索引中复制完整 metadata。无法可靠判断项目、人员、软件或主题时，先不写对应索引。

## MinerU 正式导入范围

正式 LibVault 只保留：

- PDF 原件
- 整理后的 Markdown
- 当前文档自己的 `images/`
- 索引 note

不得作为正式条目导入：

- `_content_list.json`
- `_middle.json`
- `_model.json`
- `_layout.pdf`
- `_span.pdf`
- layout PDF
- span PDF
- 其他只服务于 MinerU 处理过程的中间产物

## MinerU 临时输出清理

如果 MinerU 输出由本次任务创建：

- 导入和验证成功后清理。
- 失败时保留并报告路径和失败原因。

如果 MinerU 输出由用户提供：

- 默认不清理。
- 只读提取正式产物。
- 只有用户明确要求时才删除或归档。

## 验收标准

入库完成应满足：

- Markdown frontmatter 合法并位于正文最前。
- Paper frontmatter 只包含 `type`、`authors`、`corresponding_author`、`publish_year`、`read_status`、`topics`。
- Paper H1 title 下方有 DOI、URL 和 Source PDF。
- Source PDF wikilink 可在 vault 中找到。
- 所有 `images/` 引用无断链。
- 阅读状态索引已更新。
- guide/manual/book 已拆分为父级 note 和章节 note。
- 正式库中没有 MinerU 中间文件。
