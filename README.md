# 我的 Codex Skills

这个仓库用于维护我自己的 Codex 自定义 skills。

仓库范围只包含我个人编写和长期维护的 skills，不并入第三方 skill 仓库。

## 当前包含的 Skills

目前共有 5 个 personal skills：

- `writing-master`
- `purple-periodic`
- `purple-action-board`
- `purple-meeting-record`
- `meeting-press-release`

## 最近更新要点

- `writing-master` 现在采用两份平级的权威样文作为最高优先级风格依据：
  - `references/style-samples.md`
  - `references/style-samples-simulation.md`
- `purple-action-board` 已拆分出候选审阅契约与正式面板契约：
  - `references/review-contract.md`
  - `references/board-contract.md`
- `purple-action-board` 现在把 `AI 行动面板` 的旧小事项区替换成 `未来7天承诺与待闭合小事`，并支持项目块级 `人工修正 / 交互输入`
- `purple-action-board` 现在除 `AI 行动面板` 外，还维护 `学生沟通面板`，并新增学生沟通候选审阅与页面契约。
- `purple-meeting-record` 已形成更稳定的四阶段整理流程，并显式区分 `全细节 / 详细 / 标准 / 极简` 四档压缩强度；学生沟通场景下会额外输出稳定的 `沟通形式 / 本次主要汇报 / 沟通建议 / 触发原因` 信号。
- `purple-periodic` 继续强调分层来源、低扫描范围和 periodic 工作流边界，避免与行动判断层混用；当前会显式区分 daily 里的事实输入与未来 `7` 天短期承诺层。
- 新增 `meeting-press-release`，用于根据会议日程、会议手册、会务资料、会后事实或已有初稿生成中文会议会后通稿，并在关键信息不足时先输出待补信息清单。

## Skills 总览

### `writing-master`

面向以下研究方向的学术英语写作 skill：

- 流化床
- 多相流
- 颗粒技术
- CFD
- DEM
- CFD-DEM
- 相关建模与数值模拟研究

支持的典型任务：

- 中译英
- 英文润色
- 中英混合草稿重写
- 在保持科学含义不变的前提下重组逻辑
- 术语统一
- 依据用户提供的权威样文进行风格控制

当前特点：

- 以两份平级的 expert-revised exemplars 作为最高优先级风格标准
- 一份样文偏 preface / 学科定位 / 应用铺陈
- 一份样文偏 simulation chapter / 方法介绍 / 技术解释 / 章节推进
- 配套 `terminology.md` 用于跨论文、proposal 和章节草稿的术语一致性控制

### `purple-periodic`

面向 Purple Sys 的 periodic 工作流 skill，主要用于：

- 维护和总结 daily、weekly、monthly 周期笔记
- 把 daily 内容按规则归档到 project logs 或分类 idea logs
- 基于分层来源完成 weekly 和 monthly 汇总，而不是扫描整个 vault
- 在 weekly 或 monthly 过程中识别 project 候选，但不未经确认直接创建项目
- 正确读取 daily 里的 `今日杂项 / 触发事项` 与 `未来几天需要做的事情`，但不把短期承诺误当成已发生事实

核心特点：

- 把 daily note 视为原始输入层
- 区分 daily 里的事实输入和未来 `7` 天短期承诺层
- 把 project log 视为项目长期事实层
- 把分类 idea logs 视为 ideas 的长期沉淀层
- 把 weekly 视为第一层汇总
- 把 monthly 视为第二层汇总
- 汇总时强调综合归纳，而不是把来源笔记逐条重写

### `purple-action-board`

面向 Purple Sys 的行动判断层 skill，主要用于：

- 基于 daily、weekly、project logs、student logs 和 meeting/material notes 生成或更新 AI 行动面板
- 读取 recent daily 的 `未来几天需要做的事情` 与 `今日杂项 / 触发事项`，维护短期承诺区
- 维护独立的 `学生沟通面板`，跟踪 `ongoing` 学生的月度覆盖与沟通分流
- 判断当前更该推进什么、哪些线程处于等待条件、哪些事项可能已经完成
- 判断哪些学生欠月度汇报、哪些学生更适合单独细节讨论、哪些学生更适合 `long meeting`
- 在必要时回捞“曾被记录、后来沉下去、但可能仍值得重新判断”的事项
- 将结果写入固定页面 `00 Dashboard/AI 行动面板.md` 与 `00 Dashboard/学生沟通面板.md`

核心特点：

- 它不是主动提醒系统，也不替代 `purple-periodic`
- `AI 行动面板` 按“线程”而不是单条 bullet 组织
- `AI 行动面板` 用 `未来7天承诺与待闭合小事` 取代旧小事项区，并支持项目块级 `人工修正 / 交互输入`
- `学生沟通面板` 负责全体 `ongoing` 学生的月度欠账、单独讨论、`long meeting` 与全员台账
- 默认先做候选审阅，再由用户确认，最后整体重算覆盖面板
- 固定状态为 `推进中`、`等待条件`、`待确认完成`、`可忽略`
- 全局主板与学生沟通页分别由各自 contract 文件约束

### `purple-meeting-record`

面向 Purple Sys 的沟通记录整理 skill，主要用于：

- 把会议、电话、师生沟通和多人讨论的 transcript 文本整理成 Purple Sys 风格的正式 meeting note
- 在正式落稿前，先生成可筛选的候选要点清单
- 在 speaker 标签缺失、错误或一人账号代表多人时，先做归属判断，再把高风险归属交给用户确认
- 为 daily、student log、project log 生成可直接回填的高密度短条目，并在用户明确允许后自动写入对应位置
- 在学生沟通场景中，把稳定的沟通信号写回 meeting note 与 student log，供 `purple-action-board` 继续判断

核心特点：

- 默认采用四阶段流程，而不是一步到位改写 transcript
- 先清洗、归属判断和候选提取，再生成完整稿包，最后才在明确授权后落库
- 档位显式区分为 `全细节`、`详细`、`标准`、`极简`
- 默认不自动新建 student log 或 project log
- student log 回填在学生沟通场景下固定写成：`来源 / 本次主要汇报 / 沟通建议 / 触发原因`

### `meeting-press-release`

面向中文会议新闻通稿写作的 skill，主要用于：

- 根据会议日程、会议手册、会务资料、参会与发言信息生成会后新闻稿
- 根据会后事实、现场亮点、结果信息或关键引语组织官网新闻、公众号通稿或媒体报道
- 对已有会议新闻初稿做事实校对和结构重写
- 在会后事实不足时先列出待补信息，而不是编造完整稿

核心特点：

- 默认把任务视为 `会后通稿`，不把计划、议程或期待写成既成事实
- 先做材料识别、事实抽取和缺口检查，再进入提纲或完整稿包
- 支持 `机构新闻` 与 `媒体报道` 两种风格模式
- 完整稿包固定包含 `标题候选`、`导语`、`正文` 和 `发布摘要`
- 配套 `missing-info-checklist.md`、`style-modes.md`、`style-guide.md`、`output-contract.md` 和真实样稿目录

## Purple Sys 三个 Skills 的边界

- `purple-periodic`
  - 负责 periodic 总结、daily 归档、weekly / monthly 汇总和 project 候选判断
  - 区分 `今日杂项 / 触发事项` 的事实输入与 `未来几天需要做的事情` 的短期承诺
- `purple-action-board`
  - 负责行动线程提取、状态判断、沉底事项回捞、学生沟通分流、短期承诺追踪和人工纠偏吸收
- `purple-meeting-record`
  - 负责 transcript 到 meeting note / daily / log 回填草稿的整理与落库工作流，并把学生沟通信号稳定写回记录层

接口关系：

- `purple-meeting-record` 负责把单次沟通沉成 `meeting note + student log`
- `purple-action-board` 负责读取这些稳定信号，重算 `学生沟通面板`
- 两者分工固定，不互相替代

它们共享同一套 Purple Sys 背景，但职责不同，不应混成一个“大而全”的 skill。

## 目录结构

```text
my-skills/
├── writing-master/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       ├── style-samples.md
│       ├── style-samples-simulation.md
│       └── terminology.md
├── purple-periodic/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       └── prompt-templates.md
├── purple-action-board/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       ├── board-contract.md
│       ├── review-contract.md
│       ├── student-board-contract.md
│       └── student-review-contract.md
├── purple-meeting-record/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       └── output-contract.md
├── meeting-press-release/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       ├── missing-info-checklist.md
│       ├── output-contract.md
│       ├── style-guide.md
│       ├── style-modes.md
│       └── examples/
│           ├── README.md
│           ├── institutional-sample-01.md
│           ├── institutional-sample-02.md
│           └── media-sample-01.md
├── .gitignore
└── README.md
```

## 维护约束

- 这个仓库只维护自定义 skills。
- 第三方 skills 仓库保持独立，不合并到这里。
- 每个 skill 的主说明放在各自的 `SKILL.md` 中。
- 较长的样文、模板、术语表、输出契约等内容放在 `references/` 中，避免把 `SKILL.md` 写得过长。
- `agents/openai.yaml` 应与对应 skill 的定位、触发方式和默认输出保持一致。
- Purple Sys 相关 skills 应尽量明确各自边界，避免 periodic 汇总、行动判断和会议整理相互越界。

## 使用与迭代方向

当前优先迭代方向：

- 继续完善 `writing-master` 的权威样文体系和术语控制
- 继续压实 Purple Sys 三个 skills 的边界、入口 prompt 和 references 契约
- 继续补齐 `meeting-press-release` 的真实样稿基准和机构 / 媒体风格差异
- 在保持 skill 清晰分工的前提下，持续扩展更多自定义 skills
