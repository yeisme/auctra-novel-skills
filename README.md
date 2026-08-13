# Auctra Novel Skills

Auctra 与中文长篇小说生产的独立开源 Skills 仓库。它把 Auctra 运行指导、小说创作矩阵、人物建模和视觉交接从通用 Yeisme Skills 集合中分离出来。

## 模块

- [`auctra-runtime/`](auctra-runtime/README.md)：Auctra CLI/runtime、项目启动、工作区路由、市场研究、审稿编排和优化。
- [`novel-writing/`](novel-writing/README.md)：从写前简报、分卷、大纲、场景卡到章节写作、审稿、连续性、修订和连载运营。
- [`character-modeling/`](character-modeling/README.md)：人物认知、动机、身份、关系、具身、社会知识、群体组织和戏剧压力建模。
- [`auctra-visual/`](auctra-visual/README.md)：Auctra 专属 Eikona 视觉路由、引用约束和资产交接。

每个 Skill 使用统一目录结构：

```text
<module>/<skill-name>/
  SKILL.md
  agents/openai.yaml
```

## 验证

```bash
python3 scripts/validate_skills.py
```

## 作为 Yeisme 源模块安装

主 `yeisme-agent` 工作区将本仓库作为 `.skills/yeisme/auctra-novel/` 源模块挂载。现有 Skill 名称保持稳定，`.agents/skills` 与 `.claude/skills` 的消费者无需改名。

独立使用时可直接读取目标 `SKILL.md`，或将仓库接入宿主 Agent 的渐进式 Skill profile。

## 边界

本仓库不包含 Auctra CLI 实现、小说正文、项目正典或运行状态。这些内容由对应项目持有：

- Auctra CLI: `https://github.com/yeisme/auctra`
- Novel project: `https://github.com/yeisme/chichao-beian`

## License

本仓库采用 [MIT License](LICENSE)。
