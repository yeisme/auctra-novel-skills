# 角色智能方法来源说明

访问日期：2026-07-31。

本项目进行有界、问题导向的来源扫描，不追求任意数量，也不把 marketplace 搜索结果直接当成人物知识。外部来源用于界定机制、发现工作流空白和建立安全边界；人物本体、知识卡、模板与 skills 均使用原创组织和表述，不复制外部 skill 正文。

社会科学、文化、阶层、群体、权力与意识形态来源已经拆分到 `social-research-source-ledger.md`，避免心理与社会证据混成一个来源层。当前 canonical 方法结构见 `character-intelligence-ontology.md`；`character-intelligence-matrix.md` 只是历史兼容种子目录。

## 权威知识来源

| ID | 来源 | 用途 | 使用限制 |
| --- | --- | --- | --- |
| `INT-01` | [Dan P. McAdams, Northwestern University](https://psychology.northwestern.edu/people/faculty/core/profiles/dan-mcadams.html) | 叙事身份、人生故事、连续性与意义的研究入口 | 不把单一叙事框架当全部自我，也不复制量表或受限文本 |
| `INT-02` | [Self-Determination Theory 官方理论页](https://selfdeterminationtheory.org/theory/) | 自主、胜任、关系需要；内在与外在动机 | 理论概念转译为创作问题，不据此诊断现实人物 |
| `INT-03` | [APA: Self-Determination Theory](https://www.apa.org/research-practice/conduct-research/self-determination-theory) | SDT 的研究概览与应用边界 | 只做概念核验，不用概要替代原始研究 |
| `INT-04` | [James Gross, Stanford University](https://psychology.stanford.edu/people/james-gross) | 情绪生成、调节策略与研究入口 | 知识卡是创作转译，不宣称某策略在所有情境都最好 |
| `INT-05` | [OpenStax Psychology 2e: Thinking and Intelligence](https://openstax.org/books/psychology-2e/pages/7-introduction) | 认知、概念、问题解决、判断、偏误和智力概览 | 不把教材分类变成封闭人物类型或能力排名 |
| `INT-06` | [OpenStax Psychology 2e: Emotion and Motivation](https://openstax.org/books/psychology-2e/pages/10-introduction) | 动机、情绪、需要和生理—认知机制概览 | 不用单章概览支持临床或确定性结论 |
| `INT-07` | [OpenStax Psychology 2e: Personality](https://openstax.org/books/psychology-2e/pages/11-introduction) | 人格理论、自我与个体差异的概览 | 多理论并置，不选择单一流派作为人物真相 |
| `INT-08` | [Stanford Encyclopedia of Philosophy: Embodied Cognition](https://plato.stanford.edu/entries/embodied-cognition/) | 身体、行动与环境参与认知的理论边界 | 哲学争论保持为开放背景，不写成统一实证结论 |
| `INT-09` | [Stanford Encyclopedia of Philosophy: Pragmatics](https://plato.stanford.edu/entries/pragmatics/) | 语境、说话者意图、听者推断与交流行动 | 不把一个语用理论当所有文化交流的通则 |
| `INT-10` | [Stanford Encyclopedia of Philosophy: Speech Acts](https://plato.stanford.edu/entries/speech-acts/) | 陈述、请求、承诺、威胁、宣告等言语行为 | 用于对白功能分析，不复制长篇原文 |
| `INT-11` | [Stanford Encyclopedia of Philosophy: Implicature](https://plato.stanford.edu/entries/implicature/) | 会话含意、共同知识和未明说内容 | 潜台词必须由具体语境支持，不能只靠作者解释 |
| `INT-12` | [International Personality Item Pool](https://ipip.ori.org/index.htm) | 开放人格项目与公共领域条目池的研究入口 | 当前不导入条目、不建立量表、不用分数代替人物机制 |
| `INT-13` | [OpenStax Psychology 2e: Stress, Lifestyle, and Health](https://openstax.org/books/psychology-2e/pages/14-introduction) | 压力、应对、身体状态和社会支持概览 | 文学压力测试不等于健康或临床风险评估 |

## 外部 Skill 扫描与缺口判断

通过 SkillsMP API 与站内搜索测试了 `character voice`、`character motivation`、`narrative identity`、`dialogue subtext`、`character arc`、`embodied character`、`emotion regulation` 和 `decision analysis` 等查询。检索结果的主要问题是：

| 结果类型 | 可借鉴 | 未采用原因 | Yeisme 决策 |
| --- | --- | --- | --- |
| AI persona forge | 人设约束、声音一致性、可复用 persona 结构 | 主要服务 Agent persona，不拥有小说场景证据、关系代价和人物弧线验证 | 不导入；只保留“约束必须可执行”的抽象原则 |
| 品牌身份 discovery | 结构化访谈、身份叙事与价值提问 | 面向品牌定位，不处理记忆、角色冲突、身份威胁与人物表演 | 自建 `character-identity-narrative-modeler` |
| 通用 character arc | want/need、阻力、阈值选择 | 与现有人物设计和压力测试已有能力重叠 | 当前不新增人物弧线 specialist |
| 对白或写作工具 | 语气、重写、风格提示 | 多数缺少言语行为、含意、关系位置和沉默的独立交付物 | 自建 `character-voice-pragmatics-designer` |
| embodied character 检索 | “embodied” 关键词 | 结果多为机器人具身、控制和仿真，不适合文学表演 | 自建身体、感官、空间与习惯知识卡 |
| 心理/医疗分析工具 | person-situation、层级化观察 | 临床目标、风险边界和人物创作交付物不一致 | 只保留非临床的证据与情境原则 |

结论：外部 marketplace 适合发现通用 workflow，但当前没有一组可直接、低风险导入且能覆盖六个内在机制独立交付物的 fiction skills。自建内容仍必须通过来源账本、原创实现和 skill 校验。

| 来源 | 采用的抽象启发 | 未采用内容 | 备注 |
| --- | --- | --- | --- |
| [SkillsMP 心理学家职业页](https://skillsmp.com/zh/occupations/psychologists) | 认知画像、心理分析、研究与测量类 skill 的候选入口 | 不把职业页条目直接变成人物创作清单 | 页面混合研究、临床、神经科学等不同目标 |
| [SkillsMP API 文档](https://skillsmp.com/zh/docs/api) | 通过关键词进行来源发现和筛选 | 不在技能中绑定 SkillsMP API | 匿名 API 有速率限制 |
| [dhdna-profiler](https://skillsmp.com/zh/creators/k-dense-ai/scientific-agent-skills/skills-dhdna-profiler) | 文本证据、认知维度、张力对、置信度、比较模式 | 不采用其专有框架命名或完整 12 维定义 | 自建矩阵重新分类并原创表述 |
| [character-arc](https://skillsmp.com/creators/jwynia/agent-skills/skills-creative-fiction-character-character-arc) | lie/want/need、正向/负向/平坦弧、阻力与阈值选择 | 不复制示例、诊断文本或完整结构 | 用于弧线领域的抽象启发 |
| [novel-character-design](https://skillsmp.com/creators/uu201/character-arc/resources-skills-distilled-novel-toolbox-novel-character-design) | 主角、配角功能、反派、关系和群像需要不同设计入口 | 不复制标签库、反派模板或网文专属措辞 | Yeisme 不采用标签堆积作为主模型 |
| [writer-memory](https://skillsmp.com/creators/yeachan-heo/oh-my-claudecode/skills-writer-memory) | 人物声音、情绪基线、触发点、关系事件、场景前后状态 | 不采用其 JSON 持久化和 slash command 设计 | Yeisme 结构化状态仍由 Auctra CLI 管理 |
| [psychologist-analyst](https://skillsmp.com/zh/creators/freedomintelligence/openclaw-medical-skills/skills-psychologist-analyst) | person-situation、多个分析层级、个体差异与上下文 | 不复制临床/医学长文或诊断流程 | 角色智能明确保持非临床边界 |
| [ljg-relationship](https://skillsmp.com/creators/lijigang/ljg-skills/skills-ljg-relationship) | 关系可从交换、权力、边界、阶段和叙事结构观察 | 不复制对话流程、精神分析结论或文件写入行为 | 转化为人物关系动力维度 |

## 许可证与复制边界

SkillsMP 页面可能展示某个 skill 的许可证，但 GitHub 仓库级许可证识别不一定一致。除非后续对具体路径和许可证完成独立确认，本项目默认：

- 不导入外部 skill 目录。
- 不复制外部 SKILL.md、reference、模板或示例库。
- 只保留来源 URL、抽象启发和原创实现。
- 若未来确需导入，必须使用固定 Git ref、放入 `.skills/imported/` 并走独立 canary 与许可证审查。
