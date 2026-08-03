# 开放人物智能本体

这是角色智能 suite 的 canonical reference。它用于选择人物问题、知识域、facet specialist 和验证场景，不规定维度总数，也不要求把人物“填满”。旧 `character-intelligence-matrix.md` 仅作为兼容种子目录。

## 目录

- [本体结构](#本体结构)
- [十八个开放领域](#十八个开放领域)
- [六个内在机制 specialist](#六个内在机制-specialist)
- [选择最小充分 facet](#选择最小充分-facet)
- [扩展门槛](#扩展门槛)
- [旧矩阵映射](#旧矩阵映射)
- [知识与证据状态](#知识与证据状态)
- [禁止用法](#禁止用法)

## 本体结构

```text
domain
  -> facet
    -> dimension
      -> core_question
      -> observable_signals
      -> state_context_modifiers
      -> dramatic_consequences
      -> falsification_scene
      -> evidence_source_status
```

- `domain`：稳定的检索与所有权边界，不是人格类型。
- `facet`：一组能回答相近创作问题的机制，可随知识增长扩展。
- `dimension`：具体观察坐标，不要求分数化。
- `observable_signals`：动作、语言、注意、选择、关系或身体表现。
- `state_context_modifiers`：时间、资源、身份、对象、疲劳、风险和社会情境造成的变化。
- `dramatic_consequences`：该机制如何改变场景目标、代价、关系、节奏或弧线。
- `falsification_scene`：什么场景能证明当前解释不够好。
- `evidence_source_status`：文本证据、创作推断、作者决定、开放假设及知识来源层级。

## 十八个开放领域

领域没有配额。表内 facet 是当前优先入口，不是封闭清单。

| domain | 主要回答 | 当前 facet 入口 | 主要 owner |
| --- | --- | --- | --- |
| 证据与认知状态 | 我们知道什么、如何知道、哪里可能错？ | 证据覆盖、置信度、替代解释、未知、叙事偏差 | `character-evidence-profiler` |
| 感知与注意 | 人物先看到、听到、忽略和误读什么？ | 注意选择、威胁扫描、社会线索、感官显著性、专业注意 | evidence / cognition / embodiment |
| 认知与决策 | 人物怎样建模、比较、预测并选择？ | 心智模型、启发式、归因、概率、时间折扣、决策阈值 | `character-cognition-decision-modeler` |
| 知识、信念与不确定性 | 人物相信什么，愿意因何修正？ | 核心信念、世界假设、证据标准、认知失调、秘密与未知 | cognition / psychology designer |
| 动机、需要与目标 | 什么在推动人物，哪些目标互相争夺？ | 表层目标、基本需要、趋近回避、奖励结构、承诺、优先级 | `character-motivation-value-architect` |
| 价值、道德与意义 | 什么值得保护、牺牲或赋予正当性？ | 价值排序、神圣价值、道德推理、意义、意识形态、底线 | motivation / moral ideology |
| 情绪、评估与调节 | 事件为何触发某种情绪，人物怎样处理？ | 事件评估、基线、触发、表达、调节、恢复、情绪粒度 | `character-emotion-regulation-modeler` |
| 自我、身份与叙事 | 人物把自己讲成谁，怎样维护连续性？ | 自我图式、角色身份、面具、记忆选择、人生章节、身份威胁 | `character-identity-narrative-modeler` |
| 身体、感官与习惯 | 身体和环境怎样参与人物决策与表演？ | 感觉、动作准备、姿势、空间、物件、日常、疲劳、疼痛 | `character-embodiment-habit-designer` |
| 能动性、行动与策略 | 人物怎样把意图变成行动？ | 决断、风险、计划、适应、坚持、退出、执行能力、资源使用 | psychology / cognition / power |
| 关系、依恋与亲属 | 人物怎样连接、交换、依赖、背叛与修复？ | 信任、互惠、边界、照料、退出、亲属义务、关系阶段 | `character-relationship-dynamics-modeler` |
| 权力、地位与资源 | 谁能设议程、奖惩、排除和定义现实？ | 正式权威、非正式影响、资源、声誉、守门、赞助、继承 | `character-power-status-analyst` |
| 文化、阶层与社会化 | 人物学会了哪些隐性规则和资格？ | 规范、语言、品味、教育、阶层资源、污名、流动、语码切换 | `character-culture-class-context-modeler` |
| 群体、组织与制度 | 群体如何赋予角色、规范和集体压力？ | 角色、联盟、派系、网络、官僚、沉默、集体行动、退出成本 | `character-group-organization-modeler` |
| 沟通、声音与语用 | 人物通过说、暗示、沉默和称谓做什么？ | 声音指纹、言语行为、会话含意、礼貌、潜台词、语码转换 | `character-voice-pragmatics-designer` |
| 冲突、防御与应对 | 人物怎样保护自己并制造代价？ | 防御、自欺、回避、控制、讨好、攻击、解离式隔离、修复策略 | psychology / emotion / stress tester |
| 学习、适应与转变 | 哪种反馈能使人物改变或拒绝改变？ | 学习规则、旧策略收益、阈值选择、复发、成长、堕落、代价 | psychology / stress tester |
| 戏剧功能、媒介与类型 | 机制如何变成可写、可拍、可演的故事功能？ | 角色功能、类型期待、场景发动机、表演性、视角、节奏、余波 | router / writer |

社会机制的事实层和 specialist 路由见 `social-knowledge-index.md`。内在机制的知识卡分别见：

- `cognition-decision-and-uncertainty.md`
- `motivation-needs-and-values.md`
- `emotion-appraisal-and-regulation.md`
- `identity-memory-and-self-narrative.md`
- `voice-pragmatics-and-subtext.md`
- `embodiment-sensation-and-habit.md`

## 六个内在机制 specialist

| 当承重问题是…… | 选择 | 独立交付物 | 不负责 |
| --- | --- | --- | --- |
| 人物为什么以这种方式推理、误判和下注 | `character-cognition-decision-modeler` | 认知模型 + 决策指纹 | 诊断智力、替作者决定剧情 |
| 多个目标、需要、价值和奖励怎样竞争 | `character-motivation-value-architect` | 动机价值层级 + 冲突图 | 把一切动机归因童年创伤 |
| 情绪怎样从评估发展到表达、调节与恢复 | `character-emotion-regulation-modeler` | 情绪调节回路 | 临床判断、把压抑写成无情绪 |
| 人物怎样讲述自己、扮演角色并应对身份威胁 | `character-identity-narrative-modeler` | 身份叙事图 | 宣称存在唯一“真实自我” |
| 人物怎样用语言完成请求、拒绝、威胁、亲近和遮蔽 | `character-voice-pragmatics-designer` | 声音语用与潜台词规则 | 直接写完整章节或剧本场景 |
| 感官、身体、空间、物件、日常和疲劳怎样塑造行为 | `character-embodiment-habit-designer` | 身体习惯表演图 | 用怪癖替代人物机制 |

## 选择最小充分 facet

1. 写出当前需要解释或设计的一个人物选择。
2. 找出最直接改变该选择的机制 domain。
3. 选择能形成“信号 → 解释 → 代价 → 验证”的最小 facet 集。
4. 若通用 worker 已能回答，不追加 specialist。
5. 若需要 specialist，只选独立交付物最接近当前选择的一项。
6. 其余问题写入 handoff，不在同一轮加载。

“完整人物”不是覆盖所有 domain，而是在当前故事压力下拥有足够明确的欲望、解释、选择、关系、声音和代价，并且未知处被诚实保留。

## 扩展门槛

新增 dimension 前必须回答：

```text
candidate_name:
domain/facet:
unique_question:
nearest_existing_dimensions:
observable_signals:
state_context_modifiers:
dramatic_consequences:
falsification_scene:
source_fact_or_original_rule:
why_merge_is_insufficient:
```

拒绝或合并以下候选：

- 只是另一个性格形容词或善恶评价。
- 只能通过自我陈述观察，没有行动或关系信号。
- 不会改变人物选择、语言、关系、代价或弧线。
- 与现有维度只存在措辞差异。
- 来自群体刻板印象、临床标签滥用或无法追溯的流行说法。

## 旧矩阵映射

旧矩阵保持冻结，不承担新本体配额。粗略映射如下：

| 旧领域 | 新本体主要落点 |
| --- | --- |
| 感知 | 感知与注意；身体、感官与习惯 |
| 认知 | 认知与决策；知识、信念与不确定性 |
| 信念 | 知识、信念与不确定性；价值、道德与意义；自我、身份与叙事 |
| 动机 | 动机、需要与目标；价值、道德与意义 |
| 情绪 | 情绪、评估与调节；冲突、防御与应对 |
| 行动 | 能动性、行动与策略；身体、感官与习惯 |
| 关系 | 关系、依恋与亲属；权力、地位与资源 |
| 身份表达 | 自我、身份与叙事；沟通、声音与语用；身体、感官与习惯 |
| 阴影冲突 | 冲突、防御与应对；价值、道德与意义 |
| 人物弧线 | 学习、适应与转变；戏剧功能、媒介与类型 |

历史维度 id 仍可作为 alias 使用，但新工作必须解释它在当前 domain/facet 中的含义，不能假设旧编号代表优先级或完整性。

## 知识与证据状态

### 人物材料状态

- `observed_evidence`
- `creative_inference`
- `author_decision`
- `open_hypothesis`

### 方法知识层

- `source_fact`：权威资料或原始来源支持的概念摘要。
- `creative_interpretation`：将概念转译为人物观察问题。
- `creative_rule`：Yeisme 的戏剧设计规则，不冒充科学定律。

详细协议见 `character-evidence-protocol.md`，来源见 `source-ledger.md` 与 `social-research-source-ledger.md`。

## 禁止用法

- 不用本体覆盖率、维度数量或分数排名人物质量。
- 不把维度当成稳定终身本质；必须考虑对象、场景、资源和弧线阶段。
- 不从文化、阶层、性别、族群、职业、疾病或组织标签直接推断个体。
- 不用文学人物方法诊断现实人物、判断说谎或预测暴力。
- 不把理论术语替代可观察动作、语言和代价。
- 不让 skill reference、Pinax、RAG 或向量索引取代 Auctra accepted canon。
