# 我的 Codex Skills

这个仓库用于维护我自己的 Codex 自定义 skills。

仓库范围只包含自定义 skills，不并入第三方 skill 仓库。

## 当前包含的 Skills

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
- 在保持克制的前提下重组逻辑
- 术语统一
- 依据用户提供样文进行风格控制

## Purple Sys Skills

### `purple-periodic`

面向 Purple Sys 的 periodic 工作流 skill，主要用于：

- 维护和总结 daily、weekly、monthly 周期笔记
- 把 daily 内容按规则归档到 project logs 或分类 idea logs
- 基于分层来源完成 weekly 和 monthly 汇总，而不是扫描整个 vault
- 在 weekly 或 monthly 过程中识别 project 候选，但不未经确认直接创建项目

这个 skill 的核心特点是控制来源范围和 token 消耗，并保持信息分层：

- daily note 作为原始输入层
- project log 作为项目长期事实层
- idea logs 作为 ideas 的长期沉淀层
- weekly 作为第一层汇总
- monthly 作为第二层汇总

适用前提：

- Purple Sys 中已经存在 daily、project log、idea log、weekly、monthly 等分层结构
- 汇总工作默认依赖模板、既有命名约定和 `inbox` / `linked` 等状态约定

### `purple-action-board`

面向 Purple Sys 的行动判断层 skill，主要用于：

- 基于 daily、weekly、project logs、student logs 和 meeting/material notes 生成或更新 AI 行动面板
- 判断当前更该推进什么、哪些线程处于等待条件、哪些事项可能已经完成
- 在必要时回捞“曾被记录、后来沉下去、但可能仍值得重新判断”的事项
- 将结果写入固定页面 `00 Dashboard/AI 行动面板.md`

这个 skill 不替代 `purple-periodic`，而是在 periodic 工作流之上增加“被动 / 半被动”的行动判断层：

- `purple-periodic` 负责 periodic 总结、daily 归档和 project 候选判断
- `purple-action-board` 负责线程提取、状态判断、沉底事项回捞和下一步行动排序

核心特点：

- 面板按“线程”而不是单条 bullet 组织
- 默认不扫描整个 vault，而是分层读取旧面板、近期增量、短期背景和中期背景
- 默认整页重算覆盖，不做局部拼补
- 固定状态为 `推进中`、`等待条件`、`待确认完成`、`可忽略`
- 用户的判断默认写回行动面板本身，便于后续持续更新
- 常规更新只围绕少量高不确定线程提问，不把更新过程变成大问卷

行为边界：

- 不接 TickTick
- 不做主动提醒或定时催办
- 不把 daily 中每个 bullet 直接转成待办
- 不把行动面板写成待办清单或 daily 摘要

适用前提：

- Purple Sys 中已经存在 project、student、admin 等长期 log 结构
- 行动判断以既有 periodic notes 和 logs 为事实来源，而不是额外维护一套任务系统
- 面板更新默认遵循 `references/board-contract.md` 的结构契约

## 目录结构

```text
my-skills/
├── writing-master/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       ├── style-samples.md
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
│       └── board-contract.md
├── .gitignore
└── README.md
```

## 维护约束

- 这个仓库只维护自定义 skills。
- 第三方 skills 仓库保持独立，不合并到这里。
- skill 的主说明放在各自的 `SKILL.md` 中。
- 较长的模板、术语表、样例等内容放在 `references/` 中，避免把 `SKILL.md` 写得过长。
- `agents/openai.yaml` 应与对应 skill 的定位保持一致。
- Purple Sys 相关 skills 应尽量明确各自边界，避免 periodic 汇总和行动判断混在同一个 skill 中。

## 使用与迭代方向

当前优先迭代的方向包括：

- 继续完善 `writing-master`
- 继续扩展更多自定义 skills
- 持续优化 Purple Sys skills 的边界、入口 prompt 和 README
