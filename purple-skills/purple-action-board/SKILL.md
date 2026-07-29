---
name: purple-action-board
description: Purple Sys 行动判断 skill。用于回答“接下来该做什么”“哪些线程卡住、沉底或可能完成”，并通过候选审阅更新 `AI 行动面板`；读取 recent daily 的短期承诺、weekly、project/student logs、meeting/material notes 和面板人工修正。默认只处理主行动面板；只有用户明确要求学生板面、月度欠账、单独讨论或 long meeting 时才维护学生沟通面板。不用于普通 periodic 总结或 daily 归档。
---

# purple-action-board

## 定位与边界

- 把本 skill 作为 Purple Sys 的行动判断层，不创建正式 task 库。
- 基于 vault 中的事实和用户纠偏判断线程，不把每条 daily bullet 转成待办。
- 默认只更新 `00 Dashboard/AI 行动面板.md`。
- 只有用户明确把学生沟通纳入本次范围时，才更新 `00 Dashboard/学生沟通面板.md`。
- 普通 daily/weekly/monthly 总结和归档交给 `$purple-periodic`。
- 不扫描整个 vault；按时间层和明确关联控制来源。
- 不把讨论、追问、critique 或 AI 推测自动升级为行动。

## 必读 contracts

更新主行动面板时必须读取：

- [references/review-contract.md](references/review-contract.md)：候选审阅输出。
- [references/board-contract.md](references/board-contract.md)：正式面板结构与状态。

本次明确包含学生沟通时再读取：

- [references/student-review-contract.md](references/student-review-contract.md)
- [references/student-board-contract.md](references/student-board-contract.md)

固定格式、字段、编号和示例只以这些 contracts 为准，不在本文件重复定义。

## 来源范围

按以下层次读取：

1. `变化层`
   - 上次面板后新增或更新的 record、material、project log、student log。
   - 同时间段 daily/weekly 只用于补上下文。
2. `短期背景层`
   - 最近 14 天 periodic notes。
   - 与候选明确相关的 logs。
3. `中期背景层`
   - 最近 1 个月 weekly 和关键 logs。
4. `长周期回溯层`
   - 默认不读。
   - 用户明确要求回捞时扩展到最近 3 个月。

更新主板时额外读取：

- recent daily 的 `未来几天需要做的事情`
- recent daily 的 `今日杂项 / 触发事项`
- 旧面板每个线程的 `人工修正 / 交互输入`

学生板面纳入范围时额外读取：

- 所有 `record_type=log-student` 且 `status=ongoing` 的 student logs
- 最近 4–8 周学生 meeting notes 和 student log 条目
- `月度故事汇报 / 单独细节讨论 / long meeting` 信号

## 判断规则

### 线程与短期动作

- 把反复出现、有明确下一步或牵动主线的主题归并为线程。
- 把未来 7 天承诺、短 follow-up 和待闭合小事放入 `眼前动作`。
- 同一即时动作不在主线程正文重复展开。
- 重要但暂时不能推进的事项进入 `等待条件`，不能因没有新证据直接消失。
- 只有明确完成、失效或被后续线程吸收时才建议放掉。
- 旧记录中可能仍有价值的沉底事项只进入候选，不直接落板。

### 状态

状态字段严格使用 `board-contract.md`：

- `近期重点`
- `近期有变化`
- `等待条件`
- `待确认完成`
- `可忽略`

区块位置和状态使用同一套语义，不再使用旧状态 `推进中`。

### 下一步证据

只有以下来源可写成具体动作：

- 用户明确承诺
- 明确未闭合事项
- 真实阻塞
- 高置信度延续线程

其他内容使用“可考虑 / 待确认 / 保持观察”，没有明确动作时写“暂无明确下一步”。

## 主行动面板流程

1. 读取旧面板和各线程 `人工修正 / 交互输入`。
2. 读取增量事实和限定范围内的背景。
3. 按 `review-contract.md` 输出连续编号候选：
   - 旧条目处置
   - 新线程
   - 新短期事项
4. 等用户逐条确认状态、位置或去留。
5. 只把确认纳入的内容按 `board-contract.md` 整体重写正式面板。
6. 验证结构、状态、短期动作和人工输入处理结果。

首次生成时省略旧条目处置，但仍先候选、后确认、再写入。

## 人工修正

- 重算前优先读取每个线程的 `人工修正 / 交互输入`。
- 输入只影响所属线程，不能串到同 section 其他项目。
- 已吸收输入默认清空。
- 只有带 `#留摘要` 的输入才在本次确认摘要保留一句处理结果。
- 未吸收输入继续保留。
- 有未处理输入时不要随意改线程标题；确需合并或改名时先保留其意图。

## 学生沟通流程

仅在用户明确要求时执行：

1. 读取所有 ongoing student logs 和现有学生沟通面板。
2. 按 `student-review-contract.md` 生成候选。
3. 等用户确认。
4. 按 `student-board-contract.md` 整体重写学生沟通面板。

月度覆盖只由 `月度故事汇报` 或 `long meeting` 抵扣；`单独细节讨论` 不抵扣。超过 28 天没有有效覆盖的 ongoing 学生进入月度欠账候选。系统只能建议 `paused/closed`，不能未经授权修改 student log 状态。

## 验收

- 正式面板明显比候选清单收敛。
- 没有把短期承诺误写成已发生事实。
- 没有把推测性改进写成已安排动作。
- 旧条目不会仅因缺少新证据被直接放掉。
- 主板不包含全员学生台账。
- 未明确要求学生板面时没有修改学生沟通面板。
- 人工修正按 contract 被吸收、保留或清理。
