# Auctra Novel Skills 工作区说明

本仓库只维护 Auctra 与中文长篇小说 Skills，不维护 Auctra CLI 源码、小说正文、项目正典或运行数据库。

Auctra 产品实现归 `cli/auctra` CLI/API owner；本 Skills 源仓库不创建独立 GUI、浏览器客户端或新的产品入口。需要继续实现 Auctra runtime 时，先阅读 `cli/auctra/docs/claude-next-goal.md` 与对应 OpenSpec。

## 目录边界

- `auctra-runtime/`：Auctra 产品运行、项目启动、路由、市场研究与审稿优化。
- `novel-writing/`：中文小说从写前简报到分卷、场景、章节、审稿与修订的工作流。
- `character-modeling/`：人物认知、动机、关系、身份、群体与行为模型。
- `auctra-visual/`：Auctra 专用视觉路由与交接。
- `docs/`：仓库级说明与分类文档。
- `openspec/`：本仓库结构或 Skills 契约变更记录。

## 修改规则

- 每个 Skill 必须保留 `SKILL.md` 与 `agents/openai.yaml`。
- `SKILL.md` 的 `name` 必须与 Skill 目录名一致。
- 不在运行副本中维护源文件；运行副本由宿主项目的 profile 同步生成。
- 不把小说项目正文、正典台账、Auctra `.auctra` 数据库或 CLI 实现放入本仓库。
- 破坏 Skill 名称、frontmatter 或 profile 兼容性的变更必须先记录迁移、兼容窗口与回滚方式。

## 验证

本仓库先运行独立结构校验：

```bash
python3 scripts/validate_skills.py
```

宿主工作区的 profile、同步和 runtime 校验属于宿主适配层，不应写死在本仓库 Skill 的可移植工作流中。
