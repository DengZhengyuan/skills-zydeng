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

### `purple-skills`

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
├── purple-skills/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       └── prompt-templates.md
├── .gitignore
└── README.md
```

## 维护约束

- 这个仓库只维护自定义 skills。
- 第三方 skills 仓库保持独立，不合并到这里。
- skill 的主说明放在各自的 `SKILL.md` 中。
- 较长的模板、术语表、样例等内容放在 `references/` 中，避免把 `SKILL.md` 写得过长。
- `agents/openai.yaml` 应与对应 skill 的定位保持一致。

## 使用与迭代方向

当前优先迭代的方向包括：

- 继续完善 `writing-master`
- 继续扩展更多自定义 skills
- 持续优化 README、examples 和 terminology
