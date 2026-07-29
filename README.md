# 我的 Codex Skills

这个仓库只维护当前仍在使用的个人 Codex skills。第三方和插件自带 skills 保持独立。

## 当前 Skills

目前共有 8 个：

### LibVault

- `lib-import`：把 PDF、MinerU 输出和其他资料整理进 LibVault。
- `lib-rc`：生成、更新和归档 Reference Card metadata 主表。
- `lib-translate`：为已入库 paper 主 Markdown 逐段插入中文译文。

### Purple Sys

- `purple-periodic`：维护 daily、weekly、monthly 和 daily 归档。
- `purple-action-board`：生成行动判断面板，并在明确要求时维护学生沟通面板。
- `purple-meeting-record`：把 transcript 整理为 meeting note 和 daily/log 回填稿。
- `purple-doc-bridge`：在 Purple Sys Markdown 与 Word DOCX 之间双向转换。

### Academic writing

- `writing-master`：处理流态化、多相流和模拟研究中的学术英语翻译、润色与重写。

## 分工边界

- `purple-periodic` 负责周期汇总和事实归档。
- `purple-action-board` 负责行动判断，不代替 periodic 汇总。
- `purple-meeting-record` 负责单次沟通记录，未获写入许可时只生成草稿。
- `purple-doc-bridge` 只负责 Markdown/DOCX 格式桥接。
- `lib-import` 负责入库；`lib-rc` 负责 RC；`lib-translate` 只处理已入库 paper 正文。

## 目录结构

```text
my-skills/
├── lib-skills/
│   ├── lib-import/
│   ├── lib-rc/
│   └── lib-translate/
├── purple-skills/
│   ├── purple-action-board/
│   ├── purple-doc-bridge/
│   ├── purple-meeting-record/
│   └── purple-periodic/
├── writing-master/
├── .gitignore
└── README.md
```

## 维护约束

- 每个 skill 的触发范围写入 `SKILL.md` frontmatter 的 `description`。
- `SKILL.md` 只保留核心流程、边界和资源导航。
- 固定 schema、输出格式、长样文和详细契约放入 `references/`。
- 重复且需要确定性执行的处理放入 `scripts/`，并在修改后实际测试。
- `agents/openai.yaml` 与对应 skill 的名称、定位和默认入口保持一致。
- 修改后使用最新 `skill-creator/scripts/quick_validate.py` 校验每个 skill。
