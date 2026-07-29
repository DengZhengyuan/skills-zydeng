---
name: lib-import
description: 中文 LibVault 文献入库 skill。用于把 PDF、MinerU 输出、论文、thesis、manual、book、proposal 和 other 资料整理进当前可访问的 LibVault；负责类型判断、MinerU 接入、source 目录、章节拆分、正文与公式轻量体检、图片、PDF 回链、Import log 和 Dataview 索引接入，并调用 lib-rc 生成或更新 RC metadata 主表。
---

# lib-import

## 开始前

1. 确认当前可访问的是用户指定或当前打开的 LibVault，不根据旧路径猜测。
2. 必须读取 [references/libvault-contract.md](references/libvault-contract.md)。
3. 确认 `$lib-rc` 及 `../lib-rc/references/rc-contract.md` 可用。
4. 读取 vault 的 `README.md`、`SYSTEM-CONVENTIONS.md` 和同类型近期 source 样例。

## 固定边界

- 不写死 LibVault 绝对路径，不处理 Mac/Ubuntu 同步。
- 不把 MinerU JSON、middle、model、layout、span PDF 等中间文件导入正式库。
- 每个 document 使用自己的 source folder 和 `images/`。
- `MD - ...` 与 `chap.xx - ...` 不写 frontmatter；metadata 只写入 RC。
- 不编造作者、年份、DOI、主题、标签或项目归属。
- 只清理本次任务创建的临时目录；用户提供的既有 MinerU 输出默认只读。
- PDF、DOCX、图片、正文和 RC 验证完成后才记录成功。

## 输入与类型

先识别输入：

- `PDF`：先经过 MinerU，再入库。
- `MinerU 输出目录`：整理主 Markdown、images 和原始 source。
- `vault 中已有 Markdown`：补齐 source folder、RC、链接、图片和索引兼容性。

支持的 `doc_type`：

- `paper`：期刊、会议或预印本单篇研究文档，默认不拆分。
- `thesis`：学位论文，使用 thesis RC。
- `manual`：产品、软件、硬件、命令或 API 手册，默认按章节拆分。
- `book`：正式书籍或教材，默认按章节拆分。
- `proposal`：基金、科研计划、人才项目或开放基金申请书，默认保持单个 source note。
- `other`：无法稳定归类的正式资料。

分类优先级为用户说明、封面/标题/目录/文件名、文档结构、最后才是页数和 Markdown 规模。无法区分 paper 与 manual/book 且选择会导致不同整理时，先确认类型。

## 入库流程

### 1. 准备

- 确认入库日期和 source 日期。
- 生成稳定 `doc-key`，优先使用清理后的标题。
- 目标目录使用 `01 Sources/YYYY/YYYY-MM/YYYY-MM-DD/<doc-key>/`。

### 2. MinerU

输入为 PDF 时：

1. 检查当前环境的 MinerU 命令或用户指定入口。
2. 把完整输出写入 vault 外的任务临时目录。
3. 无法运行 MinerU 时停止转换，请用户提供 MinerU 输出；不要改用未经确认的在线服务。

输入为既有 MinerU 目录时，只读使用，不删除原目录。

### 3. Source、Markdown 与图片

- 原始 PDF 命名为 `PDF - <doc-key>.pdf`；多 PDF 增加描述后缀。
- 主正文命名为 `MD - <doc-key>.md`。
- 章节命名为 `chap.00 - <doc-key>.md`、`chap.01 - <doc-key>.md`。
- 图片保留为 `![](images/<file>)`，并验证每个引用存在。
- Paper 正文顺序保持为 H1、DOI/URL/Source PDF、MinerU 正文。
- 已有同一 source 时复用，不制造重复副本。

### 4. Paper 轻量体检

只对正式 paper 主 Markdown 做保守后处理：

- 合并高置信度的跨段 citation，例如 `(Deen et al.` 与下一段 `2007)`。
- 检查破损数学分隔符、连续公式块、明显拆开的变量/上下标/token。
- 必要时对照 PDF 确认公式附近的 OCR 错误。
- 不处理 frontmatter、链接、图片、表格、details OCR、references 或纯风格 LaTeX 重排。
- 无法确认的复杂公式不猜，列为 `待核对`。

最终记录为：未发现明显问题、已修复 N 处，或仍有待核对位置。

### 5. 拆分

- Paper 和 proposal 默认不拆分。
- Manual/book 默认拆分，主 Markdown 作为目录入口。
- 章节共享同级 `images/`，并由主 Markdown 链接。

### 6. RC 与索引

文件、图片和 PDF 验证完成后：

1. 调用 `$lib-rc`。
2. 读取其唯一 `rc-contract.md`。
3. 生成或更新同文件夹 `RC - <doc-key>.md`。
4. 让 Dataview 从 RC 动态维护 Topics、Labels、Projects、Reading Status 和 Doc Types。

Project/use-case 写入 `index`；paper/thesis 的 source 属性写入 `labels`，不要混用。

### 7. 日志与临时目录

- 成功完成全部验证后，向 `98 Logs/Import.md` 追加日期、doc key、doc type、source folder 和待核对事项。
- 成功后清理本次创建的 MinerU 临时目录。
- 失败时保留临时目录并报告位置和原因。

## 确定性验证

优先运行：

```bash
python scripts/validate_entry.py --source-dir "/path/to/source-folder"
```

该脚本只读检查结构，不自动修复或写入 vault。脚本通过后仍需抽查正文、公式和 metadata 语义。

## 完成检查

- 主 Markdown、RC 和原始 source 存在。
- source/chap Markdown 不含 frontmatter。
- RC 符合 `$lib-rc` contract。
- Paper DOI/URL/Source PDF 位于 H1 后并能解析。
- 所有图片引用存在。
- manual/book 主 Markdown 能链接章节。
- 正式库没有 MinerU 中间文件。
- RC 能由 Reference Cards Dataview 查询。
- `98 Logs/Import.md` 已追加记录。

## 输出给用户

简短说明：

- doc type、source folder 和主要产物
- 是否拆分章节
- RC 和索引是否完成
- paper 正文/公式扫描结果
- 图片、PDF 和日志验证结果
- 临时输出是否清理
- 仍需核对的 metadata 或正文位置
