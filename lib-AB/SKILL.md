---
name: lib-AB
description: 中文 LibVault annotated bibliography skill。用于为 LibVault 中已入库的 paper 生成、更新和归档 AB sidecar note，维护 `AB - <paper-key>.md`、04 Annotated Bibliography Inbox/Collections，以及基于用户点评和 collections 的交叉归档；不处理 guide/manual/book，不运行 MinerU。
---

# lib-AB

## 概述

`lib-AB` 负责 LibVault 中 paper 的 annotated bibliography 工作流。它不负责 PDF/MinerU 入库，也不移动 PDF 或原文 Markdown；这些仍由 `lib-import` 处理。paper 入库完成后，`lib-AB` 为同一 paper 文件夹生成或更新 `AB - <paper-key>.md`，并维护 `04 Annotated Bibliography/` 中的嵌入页。

使用前先确认当前可访问的 vault 是 LibVault，并读取 vault 内的 `README.md` 和 `SYSTEM-CONVENTIONS.md`。如两者与本 skill 冲突，以用户最新指示和 vault 当前实际 AB 样例为准。

## 触发场景

以下请求应触发本 skill：

- `给这篇 paper 生成 AB`
- `生成 annotated bibliography`
- `更新 AB`
- `把 AB 放进 Inbox`
- `按 collections 归档 AB`
- `整理 AB 格式`
- `为刚导入的 paper 自动生成 AB`

## 固定边界

- 只处理 `type: paper` 的论文条目；guide/manual/book/other 暂不进入 AB 流程。
- 不运行 MinerU，不移动 PDF，不改写 paper 原文 Markdown。
- 不强制创建 `note - <paper title>.md`；note 是后续逐步写或生成的可选材料。
- 不在 collection 页面复制 AB 正文；只用 Obsidian embed 嵌入 AB。
- 更新已有 AB 时保留用户写入的 `点评` 和 `collections`，除非用户明确要求覆盖。

## 文件位置

每篇 paper 一个文件夹：

```text
02 Paper Markdown/YYYY/YYYY-MM/YYYY-MM-DD/<paper-key>/
  <paper-key>.md
  AB - <paper-key>.md
  images/
  note - <paper title>.md   # 可选
```

AB 汇总层：

```text
04 Annotated Bibliography/
  Inbox.md
  Collections/
```

## AB 模板

AB 文件名固定为：

```text
AB - <paper-key>.md
```

Frontmatter 固定保持轻量：

```yaml
---
type: annotated_bibliography
authors: []
venue: ""
publish_year:
status: "待粗读"
collections: []
created:
updated:
---
```

不要把 `title`、`paper_key`、`paper_note`、`keywords`、`affiliations`、`notes`、PDF link 写入 AB frontmatter。

正文格式：

```markdown
### <paper title>

<中文 AB 正文，约 200 字，写这篇文章对用户可能有用的地方、方法、结论、可借鉴点或与已有工作的关系。>

- 点评：

- Paper link: [[<paper-key>|<paper title>]]
- PDF link: [[<pdf-file>.pdf]]
- Keywords:
	-
- Affiliations:
	-
```

如果同一 paper 文件夹中已经存在 `note - <paper title>.md`，在 `PDF link` 后加入可选块：

```markdown
- Notes:
	- [[note - <paper title>]]
```

## 状态

AB status 只允许：

- `待粗读`
- `已粗读`
- `已归档`

默认写 `待粗读`。这里的 `待粗读` 表示 AB 已生成但仍等待用户确认、点评或归档，不表示 AB 尚未写。

当用户明确完成确认或要求标记时，才改为 `已粗读`。当 AB 已嵌入对应 collection 页面并不再只停留在 Inbox 时，才改为 `已归档`。

## 工作流

### 生成或更新单篇 AB

1. 找到 paper 文件夹、主 Markdown、PDF link 和可选 `note - ...` 文件。
2. 从 paper frontmatter 和正文开头提取作者、期刊/来源、年份、关键词、单位和 PDF 文件名；无法可靠识别时留空或写 `待核对`。
3. 读 paper 摘要、引言、结论和必要的方法/结果段，生成中文约 200 字 AB。
4. 新建或更新 `AB - <paper-key>.md`。若 AB 已存在，保留用户 `点评` 和已有 `collections`。
5. 将 AB embed 加入 `04 Annotated Bibliography/Inbox.md`，避免重复嵌入。

### 归档到 collections

1. 读取 AB frontmatter 的 `collections` 和用户 `点评`。
2. 在 `04 Annotated Bibliography/Collections/` 下找到或创建对应 collection 页面。
3. 用 `![[AB - <paper-key>]]` 嵌入 AB，不复制 AB 正文。
4. 归档完成后可将 `status` 改为 `已归档`。

## 验证

完成前检查：

- AB 文件存在于 paper 文件夹内，文件名为 `AB - <paper-key>.md`。
- AB frontmatter 不包含 `title`、`paper_key`、`paper_note`、`keywords`、`affiliations`、`notes`。
- `status` 是 `待粗读`、`已粗读`、`已归档` 之一，默认新 AB 为 `待粗读`。
- 正文包含标题、中文 AB、`点评`、`Paper link`、`PDF link`、`Keywords`、`Affiliations`。
- 只有实际存在 `note - <paper title>.md` 时才包含 `Notes` 块。
- `04 Annotated Bibliography/Inbox.md` 或 collection 页面使用 embed，不复制 AB 正文。
