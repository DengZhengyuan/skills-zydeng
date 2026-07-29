# LibVault RC Contract

本文件是 `lib-rc` 的唯一 schema、body 和索引契约。其他 skills 不复制这些 schema，只引用本文件。

## 目录

- [共同规则](#共同规则)
- [Paper](#paper)
- [Thesis](#thesis)
- [Manual](#manual)
- [Book](#book)
- [Proposal](#proposal)
- [Other](#other)
- [Body 契约](#body-契约)
- [索引契约](#索引契约)
- [更新与验证](#更新与验证)

## 共同规则

- RC 文件名使用 `RC - <doc-key>.md`。
- frontmatter 必须包含 `type: reference_card` 和 `doc_type`。
- 正文、PDF、DOCX 和 note 链接只放在 RC body。
- `index` 的统一语义是 project/use-case，即 source 被用于哪里。
- `index` 是 YAML list；没有明确项目时使用 `[]`。
- 旧 manual/book/proposal RC 缺少 `index` 时，在该 RC 下次被更新时补为 `[]`；不要未经要求批量迁移整个 vault。
- `created` 保留首次创建日期；除 other 外不默认增加 `updated`。
- 不把无法确认的 metadata 写成确定事实。

## Paper

```yaml
---
type: reference_card
doc_type: paper
title: ""
first_author: []
corresponding_authors: []
other_authors: []
year:
venue: ""
status: "未读"
ai_topics: []
labels: []
index: []
created:
---
```

- `status` 只允许 `未读`、`在读`、`已读`。
- 根据明确作者标记拆分共同第一作者和通讯作者；无法确认时保留待核对。
- `ai_topics` 由 AI 根据 title、abstract、keywords 和正文填写。
- `labels` 和 `index` 由用户指示或当前 vault 的明确证据维护。

## Thesis

```yaml
---
type: reference_card
doc_type: thesis
title: ""
author: []
supervisor: []
year:
institution: ""
status: "未读"
ai_topics: []
labels: []
index: []
created:
---
```

- 从封面、摘要、目录或前言提取 author、supervisor 和 institution。
- `status`、`ai_topics`、`labels`、`index` 与 paper 使用相同语义。

## Manual

```yaml
---
type: reference_card
doc_type: manual
title: ""
target_type:
target_name: ""
vendor: ""
version: ""
year:
index: []
created:
---
```

- `target_type` 根据实际对象填写，例如 `software` 或 `hardware`。
- 不写 reading status、topics 或 labels。

## Book

```yaml
---
type: reference_card
doc_type: book
title: ""
creators: []
year:
publisher: ""
edition: ""
index: []
created:
---
```

- `creators` 使用 YAML list。
- 不写 reading status、topics 或 labels。

## Proposal

```yaml
---
type: reference_card
doc_type: proposal
title: ""
author: ""
year:
index: []
created:
---
```

- 从标题页或正文明确字段提取 author 和 year；无法确认时留空。
- 不写 reading status、topics 或 labels。

## Other

Other 使用最小通用 schema，并允许按证据补充作者、年份等 metadata：

```yaml
---
type: reference_card
doc_type: other
title: ""
read_status: "未读"
topics: []
index: []
created:
updated:
---
```

- `read_status` 只允许 `未读`、`在读`、`已读`。
- `topics` 是通用主题，不等同于 paper/thesis 的 `ai_topics`。
- 不在 frontmatter 中保存 source_note、source_pdf 或 source_docx。

## Body 契约

- `paper`：中文卡片、`点评`、`Paper link`、`PDF link`、`Keywords`、`Affiliations`。
- `thesis`：约 200 字中文介绍、`点评`、`MD link`、`PDF link`、`Keywords`。
- `manual/book`：约 200 字中文摘要、`Source note`、`PDF link`。
- `proposal`：约 200 字中文摘要、`Source note`、`PDF link/PDF links` 或 `DOCX link`。
- `other`：文档用途、关键事项、适用场景、待核对、`Source note`、源文件链接、`Keywords`。

已有 `note - ...` 时可加入 `Notes`；不要为此强行创建 note。

## 索引契约

- paper/thesis `ai_topics` → `02 Index/Topics/`
- paper/thesis `labels` → `02 Index/Labels/`
- 所有 doc type 的 `index` → `02 Index/Projects/`
- paper/thesis `status` 与 other `read_status` → `02 Index/Reading Status/`
- `doc_type` → `02 Index/Doc Types/`

`02 Index/Projects/` 至少保留：

- `Projects Index.md`
- `Needs Project Assignment.md`
- 每个实际非空 `index` 值的 project 页面

Topics 和 People 可使用 DataviewJS；Labels、Manual、Reading Status、Doc Types 和 Projects 使用普通 Dataview。所有索引目标都是 RC。

## 更新与验证

- 保留用户已有的 `点评`、正文卡片和人工链接。
- 不向严格 schema 添加旧字段，例如 `source_note`、`source_pdf`、`collections` 或错误的 reading-status 字段。
- 校验所有 list 字段、reading status、body 链接和 Dataview 可见性。
- 校验 source/chap Markdown 不含 frontmatter。
