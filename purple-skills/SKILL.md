---
name: purple-skills
description: Purple Sys 的 periodic 工作流 skill。用于维护和总结 daily、weekly、monthly 周期笔记，处理 daily 到 project log 的归档、idea 的采集与转移，以及按分层来源而不是扫描整个 vault 的方式完成 weekly 和 monthly 汇总。
---

# purple-skills

## 概述

`purple-skills` 用来维护 Purple Sys 的 periodic 工作流，控制 token 消耗，并把信息按层次组织起来。它把 daily note 视为原始输入，把 project log 视为项目长期主线，把分类 idea logs 视为 ideas 的长期沉淀层，把 weekly 视为第一层汇总，把 monthly 视为第二层汇总。

## 核心规则

- 控制来源范围。除非用户明确要求做全量回溯，否则不要扫描整个 vault。
- 把 daily note 作为沟通、学习、idea 和触发事项的主要来源。
- 把 project log 作为 daily 内容归档后的项目进展事实来源。
- 把 `Idea Collection` 下的分类 idea logs 作为 ideas 的长期沉淀来源。
- 把新增文档视为轻量补漏层，而不是主要叙事来源。
- 汇总时保持“综合归纳”，不要把来源笔记中的每个 bullet 原样重写一遍。
- `Project` 是稀缺容器，不因为一次短期主题就自动创建。
- `inbox` 允许长期存在；它表示“暂未决定归属”，不等于系统错误。
- 不要因为 daily 里出现一条推进，就自动新建 project 或 log。

## Weekly 复盘流程

当需要创建或更新 weekly note 时：

1. 先读取目标 weekly note 或 weekly template。
2. 读取该周所有 daily notes。
3. 读取同一周相关的 project logs。
只读取该周明显有更新的 log，或在这一周 daily 中被链接到的 log。
4. 读取该周新增的 project、material、record notes。
5. 额外检查该周仍处于 `inbox` 的 material / meeting，以及 daily 中反复出现但尚未稳定归属的主题。
6. 按章节综合整理。

使用以下来源优先级：

- `本周推进的项目`：优先看 project logs，再用 daily 补上下文。
- `本周关键沟通 / 决策`：优先看 daily notes。
- `本周学习 / 系统建设`：优先看 daily notes。
- `本周形成的想法 / 线索`：优先看 daily notes，尤其是 idea 栏。
- `本周阻塞 / 待跟进事项`：由 daily 中的触发事项和 project log 中尚未闭合的状态综合判断。
- `下周重点方向`：从本周的阻塞、未闭合线程和项目动量中推导。
- `是否需要新建 project`：只做候选判断，不直接创建。优先看反复出现的 inbox 主题簇。

## Monthly 复盘流程

当需要创建或更新 monthly note 时：

1. 先读取目标 monthly note 或 monthly template。
2. 读取该月所有 weekly reviews。
3. 用该月新增文档和关键更新过的 project logs 作为校验层。
4. 额外检查本月仍处于 `inbox` 的 material / meeting，以及跨多个 weekly 反复出现的未归属主题。
5. 只有在 weekly 缺失或明显不完整时，才回退去读原始 daily notes。
6. 按章节综合整理。

使用以下来源优先级：

- `本月推进的项目`：优先看 weekly reviews，再用关键 project logs 校验。
- `本月关键沟通 / 决策`：优先看 weekly reviews。
- `本月学习 / 系统建设`：优先看 weekly reviews。
- `本月形成的想法 / 线索`：优先看 weekly reviews，必要时再查看 daily 中的 idea。
- `本月反复出现的问题 / 阻塞`：从 weekly 中重复出现的阻塞和 recurring friction 推断。
- `下月重点方向`：从月内尚未解决的问题和最强的活跃项目线程中推导。
- `是否需要新建 project`：只做候选判断，不直接创建。优先看跨周重复出现的 inbox 主题簇。

## Daily 归档规则

当用户要求归档或重组 daily 内容时：

- 只有在已存在对应 project 和 project log 时，才把 `今日项目推进` 中的 bullets 移入对应的 project log。
- 当 daily 中出现学生相关沟通、进展或安排，但当前没有对应学生 log 时，先询问用户是否新建该学生 log，不要直接创建。
- 如果用户同意新建学生 log，则必须从模板中的 student profile / `99 Template/Record/Student Log Template.md` 创建，再把当天对应内容归入新建的学生 log。
- 把 `[Research]` ideas 移入 `log Research idea`。
- 把 `[Skill]` ideas 移入 `log Skill idea`。
- 把 `[Unsorted]` ideas 暂时留在 daily note 中，或转入待分类区。
- 只有在某个项目下的 ideas 已经持续积累时，才考虑建立项目专属 idea log。
- 对尚未形成稳定项目线的推进，不自动创建 project 或 log；必要时保留在 daily，或建议相关 material / meeting 继续保持 `inbox`。
- 保留 daily note 作为当天原始痕迹，不要把它变成长期项目记录。

## Project 候选建议与创建规则

当 weekly 或 monthly 中出现一批相关 inbox 内容时：

- 可以提出“是否新建 project”的候选建议。
- 建议时要说明候选 project 将统筹哪些 material、meeting、daily 主题。
- 只有在用户明确同意后，才创建新的 project 和 project log。
- 创建后，再把相关 inbox material / meeting 链接到该 project，并把 `status` 改成 `linked`。
- 创建后，可以用相关 daily 和 material 回填一版初始 project log。

## Obsidian 执行方式

当用户在 live vault 中工作时，优先使用 `obsidian-cli` 读取内容。把 vault 里的模板视为章节名称和输出形状的契约。

典型动作：

- 在提出结构修改前，先读取目标 periodic template。
- 只读取目标时间段所需的 daily、weekly、log 和新增 notes。
- 编辑笔记时优先保留现有标题，除非用户明确要求改结构。
- 汇总时按行为和结果分组，不要按文件清单罗列。
- 如果要建议新建 project，先给候选方案，不要直接落文件。

## 参考资料

当你需要可直接复用的 weekly 或 monthly 汇总 prompt，或想快速查看精简版来源选择规则时，读取 `references/prompt-templates.md`。
