# 我的 Codex Skills

这个仓库用于维护我自己的 Codex 自定义 skills。

仓库范围只包含我个人编写和长期维护的 skills，不并入第三方 skill 仓库。

## 当前包含的 Skills

目前共有 4 个 personal skills：

- `writing-master`
- `purple-periodic`
- `purple-action-board`
- `purple-meeting-record`

## 最近更新要点

- `writing-master` 现在采用两份平级的权威样文作为最高优先级风格依据：
  - `references/style-samples.md`
  - `references/style-samples-simulation.md`
- `purple-action-board` 已拆分出候选审阅契约与正式面板契约：
  - `references/review-contract.md`
  - `references/board-contract.md`
- `purple-meeting-record` 已形成更稳定的四阶段整理流程，并显式区分 `全细节 / 详细 / 标准 / 极简` 四档压缩强度。
- `purple-periodic` 继续强调分层来源、低扫描范围和 periodic 工作流边界，避免与行动判断层混用。

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

核心特点：

- 把 daily note 视为原始输入层
- 把 project log 视为项目长期事实层
- 把分类 idea logs 视为 ideas 的长期沉淀层
- 把 weekly 视为第一层汇总
- 把 monthly 视为第二层汇总
- 汇总时强调综合归纳，而不是把来源笔记逐条重写

### `purple-action-board`

面向 Purple Sys 的行动判断层 skill，主要用于：

- 基于 daily、weekly、project logs、student logs 和 meeting/material notes 生成或更新 AI 行动面板
- 判断当前更该推进什么、哪些线程处于等待条件、哪些事项可能已经完成
- 在必要时回捞“曾被记录、后来沉下去、但可能仍值得重新判断”的事项
- 将结果写入固定页面 `00 Dashboard/AI 行动面板.md`

核心特点：

- 它不是主动提醒系统，也不替代 `purple-periodic`
- 面板按“线程”而不是单条 bullet 组织
- 默认先做候选审阅，再由用户确认，最后整体重算覆盖面板
- 固定状态为 `推进中`、`等待条件`、`待确认完成`、`可忽略`
- 旧条目处置和正式页面结构分别由两份 contract 文件约束

### `purple-meeting-record`

面向 Purple Sys 的沟通记录整理 skill，主要用于：

- 把会议、电话、师生沟通和多人讨论的 transcript 文本整理成 Purple Sys 风格的正式 meeting note
- 在正式落稿前，先生成可筛选的候选要点清单
- 在 speaker 标签缺失、错误或一人账号代表多人时，先做归属判断，再把高风险归属交给用户确认
- 为 daily、student log、project log 生成可直接回填的高密度短条目，并在用户明确允许后自动写入对应位置

核心特点：

- 默认采用四阶段流程，而不是一步到位改写 transcript
- 先清洗、归属判断和候选提取，再生成完整稿包，最后才在明确授权后落库
- 档位显式区分为 `全细节`、`详细`、`标准`、`极简`
- 默认不自动新建 student log 或 project log

## Purple Sys 三个 Skills 的边界

- `purple-periodic`
  - 负责 periodic 总结、daily 归档、weekly / monthly 汇总和 project 候选判断
- `purple-action-board`
  - 负责行动线程提取、状态判断、沉底事项回捞和下一步排序
- `purple-meeting-record`
  - 负责 transcript 到 meeting note / daily / log 回填草稿的整理与落库工作流

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
│       └── review-contract.md
├── purple-meeting-record/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       └── output-contract.md
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
- 在保持 skill 清晰分工的前提下，持续扩展更多自定义 skills
