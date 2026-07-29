# LibVault Import Contract

本文件只规定入库目录、source、图片、MinerU、拆分、索引接入和清理规则。RC schema 的唯一来源是 `$lib-rc` 的 `references/rc-contract.md`。

## 目录

- [目录结构](#目录结构)
- [正式导入范围](#正式导入范围)
- [PDF 与 source](#pdf-与-source)
- [Markdown 与图片](#markdown-与图片)
- [拆分规则](#拆分规则)
- [索引接入](#索引接入)
- [临时文件与日志](#临时文件与日志)
- [验收标准](#验收标准)

## 目录结构

```text
01 Sources/YYYY/YYYY-MM/YYYY-MM-DD/<doc-key>/
  MD - <doc-key>.md
  RC - <doc-key>.md
  PDF - <doc-key>.pdf
  chap.00 - <doc-key>.md
  images/
```

Vault 支撑层：

```text
02 Index/
03 Notes/
98 Logs/
99 Templates/
```

- `MD - ...` 和 `chap.xx - ...` 只承载正文，不写 frontmatter。
- `RC - ...` 是唯一 metadata/index 主表。
- `note - ...` 是人工后续笔记，不属于自动 metadata 主表。

## 正式导入范围

正式 LibVault 只保留：

- 原始 `PDF - ...`、`DOCX - ...` 等 source 文件
- 主 Markdown 和必要的章节 Markdown
- 当前 document 自己的 `images/`
- 当前 document 的 RC
- 必要的 Dataview 索引页面
- `98 Logs/Import.md` 中的简短导入记录

不要导入 MinerU JSON、middle/model/layout/span PDF 或其他中间产物。

## PDF 与 source

- 把原始 PDF 放在 source folder 根目录，命名为 `PDF - <doc-key>.pdf`。
- 多 PDF 使用 `PDF - <doc-key> - <desc>.pdf`。
- 已有同一 source 时优先复用，不制造重复副本。
- Paper 在正文 H1 下保留 DOI、URL 和 `Source PDF` 可见链接。
- RC body 同时保留对应 source/PDF/DOCX 入口。
- 无法确认 DOI、URL 或 metadata 时留空或标为待核对。

## Markdown 与图片

- 保留可读的 MinerU Markdown，不导入中间 JSON。
- 保持图片引用为 `![](images/<file>)`。
- 图片必须位于当前 source folder 的 `images/`。
- Paper 正文顺序优先为 H1、DOI/URL/Source PDF、MinerU 正文。
- 只修复高置信度的 citation、OCR 和 Markdown 问题。
- 不猜测复杂公式；无法从 PDF 或上下文确认时列为 `待核对`。

Paper 轻量体检至少检查：

- 跨段 citation
- 破损数学分隔符和连续公式块
- 明显拆开的变量、上下标和 token
- 公式附近影响阅读或渲染的 OCR 错误

不要自动重排纯风格 LaTeX，也不要改写 references、HTML 表格、details OCR 或无法确认的复杂公式。

## 拆分规则

- `paper` 默认不拆分。
- `proposal` 默认保持单个 source note。
- `manual/book` 默认按章节拆分。
- 主 Markdown 作为目录入口，章节使用 `chap.00 - ...`、`chap.01 - ...`。
- 所有章节共享同级 `images/`。
- 章节链接写入主 Markdown。

## 索引接入

文件、图片和 PDF 验证完成后，进入 `$lib-rc` 工作流：

1. 读取 `../lib-rc/references/rc-contract.md`。
2. 生成或更新同文件夹 RC。
3. 让 Dataview 从 RC 动态生成 Topics、Labels、Projects、Reading Status 和 Doc Types。
4. 不手写 RC 列表，不直接索引正文 MD。

项目/use-case 只写入 `index`；paper/thesis source 属性只写入 `labels`，不要混用。

## 临时文件与日志

本次从 PDF 运行 MinerU 时：

1. 把完整输出放在 vault 外的任务临时目录。
2. 导入并验证成功后，只清理本次任务创建的临时目录。
3. 失败时保留临时目录并报告位置和原因。

用户提供的既有 MinerU 输出默认只读，不删除。

成功入库并完成 RC/链接验证后，向 `98 Logs/Import.md` 追加一条简短记录，包括日期、doc key、doc type、source folder 和待核对事项。不要改写旧日志。

## 验收标准

- source folder、主 Markdown、RC 和原始 source 文件存在。
- source/chap Markdown 不含 frontmatter。
- RC 通过 `$lib-rc` contract 校验。
- Paper 的 DOI/URL/Source PDF 位于 H1 后，链接可解析。
- 所有 `images/...` 引用存在。
- manual/book 主 Markdown 能链接章节。
- 正式库没有 MinerU 中间文件。
- RC 可由 `02 Index/Doc Types/Reference Cards.md` 查询。
- `98 Logs/Import.md` 已追加简短记录。

优先运行 `scripts/validate_entry.py` 做只读结构检查，再进行人工抽查。
