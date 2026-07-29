---
name: lib-rc
description: 中文 LibVault Reference Card skill。用于为已入库的 paper、thesis、manual、book、proposal 和 other document 生成、更新、校验或归档 `RC - ...` metadata 主表，维护阅读状态、ai_topics、labels、index、作者或目标对象 metadata，以及 Dataview 索引；不运行 MinerU、不移动 source 文件，也不改写正文。
---

# lib-rc

## 开始前

1. 确认当前可访问的 vault 是用户指定或当前打开的 LibVault，不根据旧路径猜测。
2. 读取 vault 中的 `README.md`、`SYSTEM-CONVENTIONS.md` 和同类型现有 RC 样例。
3. 必须读取 [references/rc-contract.md](references/rc-contract.md)，以其中的 schema、body 和索引规则为唯一 RC contract。
4. 如果用户最新指示、vault 当前规范与 contract 冲突，先以用户指示和当前 vault 为准，并报告差异。

## 固定边界

- 把 `RC - ...` 作为 document 唯一 metadata/index 主表。
- 不给 `MD - ...` 或 `chap.xx - ...` 添加 frontmatter。
- 不运行 MinerU，不移动 PDF，不重写 source Markdown。
- 把正文、PDF、DOCX 和 note 入口放在 RC body，不放入 frontmatter。
- 更新已有 RC 时保留用户写入的 `点评`、正文卡片和已有正文链接，除非用户明确要求覆盖。
- 不维护静态 RC 列表或 collection 空壳页；索引由 Dataview/DataviewJS 从 RC 动态生成。

## 工作流

1. 根据同文件夹 source 和用户说明确认 `doc_type`。
2. 从 title、abstract、keywords、作者区、目录或正文提取可确认 metadata。
3. 无法可靠确认的字段留空或列为 `待核对`，不猜测作者、年份、单位、主题或项目归属。
4. 按 `rc-contract.md` 生成或更新 frontmatter。
5. 按文档类型维护 RC body 链接、中文介绍、关键词和点评区。
6. 当 `index` 出现新值时，确保对应 Projects Dataview 页面存在；不要把 `ai_topics` 或 `labels` 混入 Projects。
7. 完成后校验 RC、source、索引和链接。

## Metadata 分工

- `paper/thesis`
  - 使用 `status` 维护 `未读 / 在读 / 已读`。
  - 使用 `ai_topics` 表示 AI 语义主题。
  - 使用 `labels` 表示用户维护的 source 属性。
  - 使用 `index` 表示 project/use-case，即 source 被用于哪里。
- `manual/book/proposal`
  - 不维护 reading status。
  - 使用各自专用 metadata。
  - 可使用 `index` 进入 Projects。
- `other`
  - 使用 `read_status`、`topics` 和 `index`。
  - 只在证据明确时增加作者、年份等可选 metadata。

## 索引规则

- `ai_topics` → `02 Index/Topics/`
- `labels` → `02 Index/Labels/`
- `index` → `02 Index/Projects/`
- paper/thesis `status` 与 other `read_status` → `02 Index/Reading Status/`
- doc type → `02 Index/Doc Types/`

索引目标必须是 RC，不是正文 MD。具体页面使用 Dataview 或 DataviewJS，不手写 RC 条目。

## 验证

完成前至少检查：

- frontmatter 与 `doc_type` 对应 schema 一致。
- list 字段保持 YAML list。
- reading status 只使用允许值。
- `MD - ...` 与 `chap.xx - ...` 不含 frontmatter。
- RC body 的 source/PDF/DOCX 链接能解析。
- 新 `index` 值有对应 Projects 页面。
- `02 Index/Doc Types/Reference Cards.md` 能动态查询该 RC。

若同一任务由 `$lib-import` 发起，在其文件、图片和 PDF 验证完成后再执行本工作流。
