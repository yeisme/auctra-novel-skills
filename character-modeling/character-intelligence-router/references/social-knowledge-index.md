# 人物社会知识索引

本索引用于把社会背景问题路由到最小合适的知识域和 skill。它不是社会科学百科，也不允许从群体标签直接推断个体人格。

## 目录

- [三层知识结构](#三层知识结构)
- [六个技能域](#六个技能域)
- [五个跨域事实包](#五个跨域事实包)
- [路由决策树](#路由决策树)
- [组合规则](#组合规则)
- [社会情境最小字段](#社会情境最小字段)
- [反刻板化检查](#反刻板化检查)
- [RAG 升级门槛](#rag-升级门槛)

## 三层知识结构

| 层 | 回答的问题 | 允许内容 | 禁止混入 |
| --- | --- | --- | --- |
| 事实层 | 某种社会机制在什么条件下存在？ | 定义、时空范围、来源、争议、反例 | 作者偏好、剧情结论 |
| 创作解释层 | 该机制可能怎样改变角色？ | 机会、代价、语言、声誉、关系和选择 | 把可能性写成必然人格 |
| 创作规则层 | 如何把机制写进故事并验证？ | 提问、场景触发、反证、连续性检查 | 冒充实证研究结论 |

## 六个技能域

| 域 | 核心对象 | 典型问题 | Skill | Reference |
| --- | --- | --- | --- | --- |
| 社会知识研究 | 时代、地域、制度、职业、习俗与资料证据 | “这个背景是真的吗？”“当时普通人如何生活？” | `character-social-knowledge-researcher` | 本索引、来源账本 |
| 关系与亲属 | 信任、互惠、依赖、边界、债务、照料、背叛与修复 | “他们为什么离不开又互相伤害？” | `character-relationship-dynamics-modeler` | `relationships-and-kinship.md` |
| 权力与地位 | 资源、权威、制裁、声誉、赞助、守门与正当性 | “谁职位不高却能让所有人服从？” | `character-power-status-analyst` | `power-status-and-institutions.md` |
| 文化与阶层 | 社会化、规范、语言、教育、资源、流动、污名与身份切换 | “角色进入新阶层后哪里会露怯？” | `character-culture-class-context-modeler` | `culture-class-and-socialization.md` |
| 群体与组织 | 角色、规范、联盟、派系、领导、网络、官僚与集体行动 | “团队为什么集体沉默或突然分裂？” | `character-group-organization-modeler` | `groups-organizations-and-networks.md` |
| 道德与意识形态 | 价值、世界解释、身份、正当性、框架、宣传、异议与极化 | “双方为什么都认为自己在保护正义？” | `character-moral-ideology-conflict-designer` | `morality-ideology-and-legitimacy.md` |

## 五个跨域事实包

这五类内容通常先由 `character-social-knowledge-researcher` 建立有来源 context pack，再交给一个现有 specialist 解释人物机制；它们暂不创建独立 skill，因为没有证据表明需要新的 owner 或独立交付格式。

| 事实包 | 典型问题 | 可能 handoff | Reference |
| --- | --- | --- | --- |
| 工作、经济与物质生活 | 人物如何谋生、负债、花时间、使用基础设施和承受经济冲击？ | 权力、阶层、关系 | `work-economy-and-material-life.md` |
| 法律、官僚与公民身份 | 规则怎样被分类、记录、执行、协商和申诉？ | 权力、组织、文化阶层 | `law-bureaucracy-and-citizenship.md` |
| 宗教、仪式与象征秩序 | 神圣、仪式、机构、意义与共同体怎样限制或支持人物？ | 道德意识形态、文化、群体 | `religion-ritual-and-symbolic-order.md` |
| 媒介、技术与公众 | 信息怎样传播、排序、保存、监控并形成公众？ | 权力、群体、文化 | `media-technology-and-publics.md` |
| 迁移、地方与离散 | 移动、身份、家乡、多地家庭和回返怎样改变机会与关系？ | 文化阶层、关系、权力 | `migration-place-and-diaspora.md` |

## 路由决策树

1. 用户主要想拿到带来源的背景资料吗？
   - 是：主 skill 选择社会知识研究员。
   - 否：先由人物分析、人物设计或压力测试 skill 主导。
2. 哪个社会机制最直接改变角色当前选择？
   - 关系能否继续、双方欠什么：关系动力。
   - 谁能奖惩、排除或定义规则：权力地位。
   - 角色掌握哪些隐性规则与资格：文化阶层。
   - 群体如何形成角色、联盟和沉默：群体组织。
   - 什么价值与正当性使行动变得“应该”：道德意识形态。
3. 如果两个域都重要，选择最接近当前决策点的一个；另一个写入后续 handoff。
4. 工作、法律、宗教、媒介或迁移问题先由社会研究员提供事实包；不要仅因事实类别增加新的 specialist。

## 组合规则

- 每次只有一个主 skill。
- 每次最多追加一个社会 specialist。
- 社会研究员可以是主 skill，也可以在 specialist 之前提供 context pack，但不与五个 specialist 争夺人物结论 owner。
- writer 只在人物/社会机制已形成后负责成稿，不反向发明未经确认的社会事实。
- Auctra accepted canon 仍由项目 review 与 CLI/application service 管理。

## 社会情境最小字段

```text
time_scope:
place_scope:
institution_scope:
character_position:
formal_rules:
informal_norms:
resources_and_access:
rewards_and_sanctions:
public_script:
private_practice:
exceptions_and_dissent:
uncertainties:
source_refs:
```

## 反刻板化检查

- 是否把国家、族群、阶层、性别、职业或组织当成统一人格？
- 是否写明时代、地域、代际、城乡、教育和制度差异？
- 是否区分“规范要求”“统计倾向”“个体认同”“实际行为”？
- 角色是否拥有顺从、协商、伪装、逃离、反抗和重新解释的选择？
- 是否只描写精英制度文本，遗漏普通人的非正式实践？
- 是否至少存在一个反例或边界人物来测试规则？

## RAG 升级门槛

当前阶段使用 Markdown 正本与语义路由。只有下列三项至少满足两项时，才新建立项评估 RAG：

- 原创社会知识卡超过 300 条或来源文档超过 30 份。
- 至少 30 个代表性查询的 top-5 有效命中率低于 80%。
- 至少三个独立产品或子项目需要共享版本、权限和同步。

即使升级，来源账本和 Markdown 正本仍是 source of truth，向量索引只是可重建的派生层。
