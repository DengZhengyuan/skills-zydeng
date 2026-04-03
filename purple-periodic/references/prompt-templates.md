# Prompt 模板

## Weekly 汇总 Prompt

用于汇总 weekly review note。

```text
请只使用以下来源来总结本周：
- 本周的 daily notes
- 相关的 project logs
- 本周新增的 project / material / record notes

来源优先级如下：
- 项目进展：project logs 优先
- 沟通、学习、ideas、触发事项：daily notes 优先
- 新增 notes：只用于补漏

另外，请额外检查：
- 本周仍然处于 `inbox` 的 material / meeting
- 本周 daily 中反复出现但尚未稳定归属的主题

如果发现已经形成稳定主题簇，请单独给出“project 候选建议”：
- 说明候选 project 名称
- 说明它将统筹哪些 inbox 内容
- 不要直接创建 project，先等用户确认

不要扫描整个 vault。
不要把 daily 里的每条 bullet 原样复述。
请进行归纳总结，但也不要漏掉细节。
把结果写入以下章节：
- 本周推进的项目
- 本周关键沟通 / 决策
- 本周学习 / 系统建设
- 本周形成的想法 / 线索
- 本周阻塞 / 待跟进事项
- 下周重点方向

在最后进行本周点评。
```

## Monthly 汇总 Prompt

用于汇总 monthly review note。

```text
请按以下方式总结本月：
- 以本月的 weekly reviews 作为主要来源
- 以关键更新过的 project logs 作为校验层
- 以本月新增的 project / material / record notes 作为轻量补漏层

另外，请额外检查：
- 本月仍然处于 `inbox` 的 material / meeting
- 跨多个 weekly 反复出现但尚未稳定归属的主题

如果发现已经形成稳定主题簇，请单独给出“project 候选建议”：
- 说明候选 project 名称
- 说明它将统筹哪些 inbox 内容
- 不要直接创建 project，先等用户确认

只有在 weekly 缺失或明显不完整时，才回退去读原始 daily notes。
不要扫描整个 vault。
先写 3-5 条 `本月核心结论`。
不要按周顺序复述 weekly，要按月度主题重组。
请进行归纳总结，但也不要漏掉细节。
把结果写入以下章节：
- 本月核心结论
- 本月产出 / 节点成果
- 本月推进的项目
- 本月学生与课题推进
- 本月关键沟通 / 决策
- 本月学习 / 系统建设
- 本月形成的想法 / 线索
- 本月反复出现的问题 / 阻塞
- 下月重点方向

额外要求：
- `本月产出 / 节点成果` 只列关键成果、结果和节点，不做文件清单
- `本月学生与课题推进` 独立组织，不并入项目板块
- `下月重点方向` 必须由前文内容自然推导
```

## Daily 归档 Prompt

用于把 daily 内容转移到 project logs 和分类 idea logs。

```text
请按以下规则整理今天的 daily note：
- 只有在已存在对应 project 和 project log 时，才把 `今日项目推进` 中的 bullets 移到对应的 project log
- 把 `[Research]` 的 idea bullets 移到 `log Research idea`
- 把 `[Skill]` 的 idea bullets 移到 `log Skill idea`
- 把 `[Unsorted]` 的 idea bullets 暂时保留在 daily note 中，或放入待分类区
- 只有在某个项目下的 ideas 已经持续积累时，才考虑建立项目专属 idea log
- 对尚未形成稳定项目线的推进，不自动创建 project 或 log
- 保留 daily note 作为当天原始痕迹，而不是完整项目历史
```
