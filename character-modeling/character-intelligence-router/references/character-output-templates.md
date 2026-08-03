# 角色智能输出模板

## 目录

1. 路由结果
2. 证据式人物画像
3. 人物设计包
4. 戏剧压力测试
5. Auctra handoff

## 1. 路由结果

```markdown
任务类型：analyze | design | stress_test | social_research | draft_handoff
主 skill：
facet specialist（可选，最多一个）：
目标交付物：
已有输入：
缺失输入：
媒介：novel | screenplay | short_drama | audio | game
下一步 owner：
Auctra：phase / artifact / gate（如适用）
```

## 2. 证据式人物画像

```markdown
# 人物画像：<name>

## 材料覆盖
- 范围：
- source refs：
- 证据限制：

## 一句话核心机制
<欲望 + 恐惧 + 信念 + 保护策略>

## 承重 facet
| domain/facet | 状态 | 结论 | 证据 | 置信度 | 替代解释 |
| --- | --- | --- | --- | --- | --- |

## 思维与决策
- 注意焦点：
- 推理方式：
- 归因方式：
- 决策指纹：

## 情绪与关系
- 情绪基线/触发/恢复：
- 信任、边界和权力：
- 关键关系差异：

## 声音与外显
- 句长/词汇/称谓：
- 回避方式：
- 身体或仪式线索：

## 矛盾与未知
- 冲突证据：
- unknown：
- 验证场景：
```

## 3. 人物设计包

```markdown
# 人物设计包：<name>

## 故事功能
- 角色功能：
- 不可替代价值：
- 主题承载：

## 核心引擎
- surface_want：
- deep_need：
- dominant_fear：
- core_belief：
- protection_strategy：

## 承重 facet
| domain/facet | author_decision | 平时表现 | 压力表现 | 关系代价 |
| --- | --- | --- | --- | --- |

## 身份与声音
- public_mask：
- private_self：
- role_identity：
- voice_rules：
- embodied_tells：

## 关系动力
| 对象 | 我想要 | 对方想要 | 筹码/亏欠 | 权力 | 背叛风险 |
| --- | --- | --- | --- | --- | --- |

## 阴影与边界
- self_deception：
- internal_contradiction：
- moral_boundary：
- temptation_path：

## 人物弧线
- ghost/wound：
- false_story：
- resistance：
- threshold_choice：
- direction_and_cost：

## 验证场景
1. 诱惑：
2. 失去：
3. 亲密暴露：
4. 道德边界：
```

## 4. 戏剧压力测试

```markdown
# 人物压力测试：<character> / <scene>

## 基准状态
- 当前欲望/恐惧/信念：
- 已知信息：
- 关系状态：
- 弧线阶段：

## 测试矩阵
| 压力 | 触发 facet | 预测第一反应 | 主选择 | 不会选什么及原因 | 代价 | 后果 | 结果 |
| --- | --- | --- | --- | --- | --- | --- | --- |

结果：pass | needs_setup | contradiction | arc_break | insufficient_evidence

## 最小修复
| 问题 | 最小动作 | owner skill | 验证方式 |
| --- | --- | --- | --- |
```

## 5. Auctra handoff

```markdown
phase=character
artifact=character_profile | character_design_pack | character_stress_report
canonical_owner=cli/auctra
review_state=candidate
display_path=<建议的人类可见路径>
source_refs=<来源>
open_hypotheses=<待确认>
next_command=<真实 auctra 命令或明确产品缺口>
```

可用命令示例：

```bash
auctra gate check --before chapter_write --json
auctra material add --from 人物/角色设计包.md --json
```

只有文件真实存在且符合当前项目布局时才运行 `material add`。不得手写 `.auctra/**`。
