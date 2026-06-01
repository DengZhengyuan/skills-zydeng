---
name: lib-import
description: 中文 LibVault 文献入库 skill。用于把 PDF、MinerU 输出、论文、guide/manual/book 等资料整理进当前通过 Obsidian Skill 可访问的 LibVault；负责类型判断、MinerU 接入、章节拆分、论文元数据、阅读状态、图片引用、PDF 回链和索引维护，并在 paper 入库后引用 lib-AB 生成 AB sidecar。
---

# lib-import

## 概述

`lib-import` 用于把 PDF 或 MinerU 输出整理进当前可访问的 LibVault。这个 skill 只定义入库规则和执行流程，不记录固定 vault 路径，不处理 Mac/Ubuntu 同步。

使用时默认通过 Obsidian 相关 skill 或当前任务上下文接入 LibVault。只要当前环境能访问 LibVault，就按本 skill 执行；如果无法确认当前 vault 是 LibVault，先确认 vault 接入，不要硬猜路径。

详细目录、frontmatter、正文链接、图片、索引和清理规则见 [references/libvault-contract.md](references/libvault-contract.md)。执行正式入库前必须读取该文件。

对 `paper`，正式入库完成后默认进入 `lib-AB` 工作流：在 paper 文件夹内生成或更新 `AB - <paper-key>.md`，并嵌入 `04 Annotated Bibliography/Inbox.md`。guide/manual/book 不进入 AB 流程。

## 触发场景

以下请求应触发本 skill：

- `把这个 PDF 入库`
- `把这个 MinerU 输出放进 LibVault`
- `整理这篇论文`
- `导入 guide/manual`
- `按章节拆分入库`
- `用 MinerU 处理后放进论文库`

## 固定边界

- 不写死 LibVault 绝对路径。
- 不处理 Mac/Ubuntu 同步机制。
- 不把 MinerU JSON、layout、span、middle、model 等中间文件作为正式 LibVault 条目导入。
- 不使用全局 attachments；图片保留在每个文档自己的 `images/` 文件夹中。
- Paper frontmatter 保持轻量；DOI、URL、Source PDF 放在正文 H1 标题下方。
- Paper 入库后默认引用 `lib-AB` 生成 AB sidecar；AB 不写入 paper frontmatter，不处理 guide/manual/book。
- 不编造论文元数据。无法可靠识别的作者、通讯作者、发表年份、主题、DOI 或链接留空或写 `待核对`。
- 不对用户已有的 MinerU 输出目录做删除操作，除非该目录明确是本次任务创建的临时工作区。

## 输入识别

先判断用户给的是什么：

- `PDF`：需要先经过 MinerU，再入库。
- `MinerU 输出目录`：直接整理其中的 `.md`、`images/` 和可用 PDF 信息。
- `vault 中已有 Markdown`：检查并补齐 frontmatter、正文链接、图片规则和索引。

如果输入是 PDF：

1. 先粗判文档类型。
2. 检查当前环境是否有 MinerU 命令入口或用户指定的 MinerU 处理方式。
3. 若可运行 MinerU，把完整输出写入 vault 外的临时工作区。
4. 若不可运行 MinerU，停止转换步骤，说明需要用户提供 MinerU 输出目录；不要处理同步问题。

如果输入是 MinerU 输出目录：

1. 识别目录中的主 Markdown、`images/` 和原始 PDF。
2. 忽略 MinerU 中间文件。
3. 按类型整理进 LibVault。
4. 用户提供的原始输出目录默认不清理。

## 类型判断

默认分类为 `paper`、`guide`、`manual`、`book`、`other`。

- `paper`：期刊论文、会议论文、预印本、学位论文中的单篇研究文档。默认不拆分。
- `guide` / `manual` / `book`：软件手册、用户指南、理论指南、命令参考、API 文档、长教程、书籍。默认按章节拆分。
- `other`：无法稳定归类的 PDF 或资料。先作为待分类文档入库，不强套论文元数据。

判断依据优先级：

1. 用户明确说明。
2. PDF 或 Markdown 标题、封面、目录、文件名。
3. 文档结构：是否有 DOI、作者列表、摘要、参考文献；是否有长目录、章节编号、命令/API 列表。
4. 页数和 Markdown 规模。很长的 guide/manual/book 不应作为单个巨型 note 入库。

如果 `paper` 与 `guide/manual/book` 无法区分，先保守问一句；不要一边猜测一边执行破坏性整理。

## 入库流程

### 1. 准备

1. 读取 [references/libvault-contract.md](references/libvault-contract.md)。
2. 确认当前可访问的 Obsidian vault 是 LibVault。
3. 确认入库日期和处理日期。
4. 生成稳定的 `doc-key`，优先使用清理后的标题；标题不可用时用文件名。

### 2. PDF 原件

把原始 PDF 放入 PDF 原始文件库。对 `paper`，PDF 链接写在正文 H1 标题下的 `Source PDF` 行；不要写入 paper frontmatter。若 PDF 已在库中，优先复用已有文件，不制造重复副本。

### 3. Markdown 与图片

只把正式可读内容导入 Markdown 层：

- 整理后的 `.md`
- 当前文档自己的 `images/`

保留 MinerU 图片引用形式：

```markdown
![](images/<file>)
```

对 `paper`，若 MinerU 输出在 H1 前放了首页图片，导入时调整为：

1. frontmatter
2. H1 title
3. DOI / URL / Source PDF 链接
4. MinerU 原正文内容和图片

### 4. 元数据

- `paper` 使用轻量 frontmatter，只保留 `type`、`authors`、`corresponding_author`、`publish_year`、`read_status`、`topics`。
- `guide/manual/book` 使用 guide frontmatter。
- `other` 使用待分类 frontmatter。
- 新条目 `read_status` 默认 `未读`。

### 5. 论文正文后处理

MinerU 可能把括号内 citation 错误拆成跨段落文本。对 `paper` 做轻量后处理：

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

### 6. 拆分规则

`paper` 默认不拆分；只有用户要求或单篇 Markdown 明显过大时才拆。

`guide/manual/book` 默认拆分：

- 每个文档一个文件夹。
- 父级 note 作为目录索引。
- 章节 note 与该文档的 `images/` 同级。
- 所有章节共享同一个 `images/` 文件夹。
- 章节 wikilink 写入父级 note。

### 7. 索引

至少更新阅读状态索引。能可靠识别项目、人员、软件或主题时，再更新对应索引；不能可靠识别时不要编造分类。

索引 note 是引用面，不是重复数据库。优先写 wikilink 和短上下文，不复制大段 metadata。

### 8. Paper AB

对 `paper`，入库、图片检查和 PDF 回链完成后，按 `lib-AB` 规则生成或更新同文件夹的 `AB - <paper-key>.md`，默认 `status: "待粗读"`。若同文件夹已有 `note - <paper title>.md`，AB 中可以加入 `Notes` 块；否则不要强行创建或链接 note。

guide/manual/book/other 不执行本步骤。

## MinerU 临时文件策略

如果本次任务从 PDF 运行 MinerU：

1. MinerU 完整原始输出先放在 vault 外的临时工作区。
2. 导入和验证成功后，清理该临时输出。
3. 如果导入、拆分、图片检查、PDF 回链或 Obsidian 验证失败，保留临时输出目录，并报告路径和失败原因。

如果用户提供的是已经存在的 MinerU 输出目录：

- 默认只读使用，不删除。
- 只把正式产物复制或整理进 LibVault。
- 需要清理原始输出时必须由用户明确要求。

## 验证

完成前至少检查：

- 目标 Markdown 存在，frontmatter 在正文最前。
- Paper frontmatter 只包含 `type`、`authors`、`corresponding_author`、`publish_year`、`read_status`、`topics`。
- `read_status` 是 `未读`、`正在读`、`已读` 之一。
- 对 `paper`，DOI、URL、Source PDF 出现在 H1 标题下方，且 Source PDF wikilink 指向 vault 中的 PDF 原件。
- 对 `paper`，已按 `lib-AB` 生成或更新 `AB - <paper-key>.md`，并嵌入 `04 Annotated Bibliography/Inbox.md`。
- 所有 `![](images/...)` 引用能在当前文档文件夹的 `images/` 中找到。
- 正式库中没有 MinerU 中间文件。
- 对 guide/manual/book，父级 note 能链接到章节 note。
- 阅读状态索引已更新。

## 输出给用户

最终回复应简短说明：

- 入库类型：`paper`、`guide/manual/book` 或 `other`。
- 生成或更新了哪些主要条目。
- 对 `paper`，是否已生成或更新 AB sidecar。
- 是否拆分章节。
- 图片放置规则。
- MinerU 临时输出是否已清理；若失败则给出保留位置和原因。
- 哪些元数据或正文链接仍为 `待核对`。
