# 剧本样本研究合同

## 语义层

| 层 | 事实 | 禁止项 |
| --- | --- | --- |
| Source | 原文、换行、marker、media ref、digest、permission | 自动修文、插图标、猜缺字 |
| Overlay | source span、kind、attributes、confidence、review、repair | 无来源结论、自动接受 |
| Presentation | Lucide icon、短标签、tooltip、aria、状态 | icon-only、颜色唯一语义、写回 source |

## 规范块类型

`episode_heading`、`scene_heading`、`location`、`time_of_day`、`int_ext`、`cast_list`、`prop_list`、`action`、`character_cue`、`dialogue`、`parenthetical`、`voice_over`、`off_screen`、`transition`、`flashback`、`sound_music`、`subtitle`、`vfx_sfx`、`reference_image`、`unsupported`。

Fountain 兼容投影只使用既有 `scene_heading/action/character/dialogue/parenthetical/transition/note/unsupported`；episode 与扩展类型保留在上层 boundary、attributes 或 metadata。

## 便携符号

| 类型 | 工作稿标识 | Studio icon |
| --- | --- | --- |
| 集 | `§ 集` | `ListVideo` |
| 场 | `🎬 场` | `Clapperboard` |
| 地点/时间 | `⌖ 地` / `◷ 时` | `MapPin` / `Clock3` |
| 内外景 | `INT / EXT` | `Building2` / `Trees` |
| 人物/道具 | `👥 人` / `□ 道` | `UsersRound` / `Package` |
| 动作 | 原始 `△/▲` | `Activity` |
| 角色/对白 | `@ 角` / `💬 话` | `UserRound` / `MessageSquareText` |
| VO/OS | `VO` / `OS` | `Mic2` / `Radio` |
| 转场/闪回 | `→` / `↶` | `ArrowRightLeft` / `History` |
| 声音/字幕/特效 | `♪` / `CC` / `✦` | `Music2` / `Captions` / `Sparkles` |
| 参考图/未知 | `▧` / `?` | `Image` / `CircleHelp` |

工作稿标识用于图例和展示；canonical screenplay 不应无条件插入 emoji。原稿已有 `△/▲` 时保留。

## Pattern Lens

1. Promise：受众体验承诺。
2. Hook：首段未知、危险、羞辱、欲望或反常。
3. Conflict Ladder：阻碍与代价升级。
4. Information Gap：观众、主角、对手的知识差。
5. Reversal：身份、证据、关系、目标或局势反转。
6. Emotional Payoff：爽、虐、暖、悔、燃的兑现。
7. Character Function：阻碍、见证、误导、支持和改变功能。
8. Scene Rhythm：进入点、目标、转折、退出点和 cliffhanger。
9. Dialogue Strategy：信息、冲突、潜台词、口吻与动作比例。
10. Production Shape：场景、角色、资产、动作、VFX 与复用成本。

## 数据用途

| Split | 可做 | 不可做 |
| --- | --- | --- |
| calibration | parser/符号/gold set 校准 | 独立证明泛化 |
| holdout | 冻结后的盲测 | 调参、recipe、生成上下文 |
| exploratory | 权限/格式/续作/新模式压力 | 稳定 benchmark |

## Recipe 晋级

- exploratory：观察或假设。
- candidate：至少两个独立来源、人工抽象审核。
- production_ready：至少三个独立来源、权限允许、holdout/原创性/生产性通过。

任何阶段都不得携带可拼贴的专名、长台词或独特桥段。

## Owner 链

```text
Anatomia reviewed video observations (可选)
  -> Auctra source/overlay/pattern/recipe/project candidate/review/canon
  -> Auctra ProductionHandoff
  -> Scaena ProductionGraph/ShotIntent/ShotGenerationSpec/production review
```

Studio 只消费 Auctra typed contract 和提交 review/link/eval 命令；不拥有 source、recipe 或 canon。
