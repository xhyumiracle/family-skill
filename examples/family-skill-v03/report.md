# family v0.3 该改什么：编排者要不要中途介入、怎么评估、两轴核查值不值、报告模板对读者是否承重、哪些是过度设计

standard 档（核查 20 条）· 5 席（evaluator、reader、grade、researcher、skeptic）+ 1 名核查员 · 2026-10-27 · 本次运行目录：`projects/xhyu/family/family-skill-v03/`

## Bottom line
① v0.3 做四件事：核查判定收成四种加两个旗标和一个「直接/间接」标记；综合之后把 bottom line 逐字对照核查表；报告分成读者层（三格结论、最多七条关键判断）和审计层；fieldwork 结束后允许一轮按规则触发的 gap round。运行中不给席位发消息，席位数不再调。
② 这些改动让首屏少出错：很可能（80-95%）。置信度中：LLM 侧的证据多来自开源或中档模型、别的任务（间接），本 skill 自己只有两次运行。
③ 承重假设：最终报告的错误主要出在编排者（一个系统、一项研究）。若接下来两次 v0.3 运行的逐字核对都是零不匹配且 lint 6/6，这条假设就该下调，综合后核对保留为廉价保险。
（claims: #1 #3 #9 #10 #12 #17 #18）

## Key judgments
| # | 判断 | 可能性（区间）/ 置信度 | 最强的核查通过来源 | 什么会改变它 | Claims |
|---|---|---|---|---|---|
| 1 | 运行中给席位发消息会让它们放弃已有来源支撑的答案 | 很可能（80-95%）/ 中：数字来自 23 个开源模型，不是 Claude | 2608.11247：一致的错误多数翻掉 22.8%-71.0% 的正确答案 | 前沿模型上对「编排者消息」的翻转率接近 0 的研究 | #19 |
| 2 | Co-STORM 的主持人结果不支持「运行中介入」，只支持「从未引用的材料里出题」这个机制 | 可能（55-80%）/ 中：消融无显著性检验、LLM 评审打分；第三方运行没有复现主持人效应，但也没有消融它 | Co-STORM 表 3：去主持人 Depth 3.77→3.41，无显著性检验 | 带显著性检验的主持人消融，或第三方复现 | #1 #2 |
| 3 | 细粒度判定标签不可复现；四种判定加旗标比两轴十一标签可靠 | 很可能（80-95%）/ 中：人类核查员和开源模型的数据，Claude 级核查员未测 | Lee 2023：749 条里 30.4% 不一致，粒度是最大单一原因；Admiralty 两轴 87% 落在对角线；GRADE 在真实综述里 κ 仅 0.18-0.44 | 用 v0.2 两轴协议把同一份 claims.md 核查两遍，Eligible 列一致率 ≥0.8 | #7 #8 #9 #10 |
| 4 | 编排者的综合需要单独核对 | 可能（55-80%）/ 中：84.7% 只来自一个系统；本 skill 第一轮的拼接是实例 | 2608.24306："84.7% of final-report errors in AI-Q originate at the orchestrator"；本地：round-1 bottom line 把「+10% 覆盖度」与「p=0.084」拼成一句 | 两次 v0.3 运行逐字核对零不匹配 | #3 #18 |
| 5 | 首屏按「主信息先行 + 固定可能性刻度 + ≤7 条关键判断」写，读者更快拿到结论 | 很可能（80-95%）/ 中：标准是一手文本，但随机试验很小且是医学读者 | ICD 203、Cochrane 第 14 章；Rosenbaum 2010 RCT II（18 vs 15）：正确率 93% vs 44%，找到关键信息 90 秒 vs 4 分钟 | 用本 skill 的报告做读者测验（前 300 字、四个问题）看不出差别 | #4 #5 #6 |
| 6 | 10-20 题的 eval 分不出 3/4/5 席；席位配置要用一次盲写运行的子集做留一法，配对比较计数指标 | 可能（55-80%）/ 中：969 是 Miller 的算例参数，LOO 结论来自 workshop 海报且限定层级系统 | Miller 2024 算例；Bowyer 2025：几百条以下 CLT 区间严重低估；Lu et al.：LOO 与组合法等效 | 同一配置重跑 4 题，运行间方差很小 | #11 #14 #15 |
| 7 | 单次运行的席位指标是选择偏差：第一轮「outsider 6 条独有」不能当证据 | 几乎确定（95-99%）/ 高：本地产物逐条可查 | round-1 report.md 写 10 条、Cost 行合计 11；6 条里 2 条是 PARTIAL 却计为通过 | 无 | #18 |

## Belief vs. finding
owner 的信念「v0.2.0 优于 v0.1.0，核查和报告里的结构越多越可信」被削弱：没有任何 v0.2.0 的运行存在（本轮是第一次，且用的还是 v0.2 协议的单轴核查表，两轴一次都没跑过，#17）；新加的四项结构里两项（Estimates 表、席位指标）在第一轮报告里就出了错（#18）。被证据留下的只有 MISQUOTED-INVERTED 规则和 20 条核查预算（第一轮的三处降级在第 14、15、18 位，#17）。

## Cruxes
### Crux 1：gap round 放在核查之前还是之后
- **Side A**（researcher、grade）：之前。补回来的 claim 也要过核查员；触发规则预先写进 brief，记录为 amendment。
- **Side B**（evaluator、skeptic）：之后。核查员的「Found but not cited」是最好的缺口来源；补回来的标 [UNVERIFIED]。
- **What would settle it：** 两种时机各跑两次，比较补回 claim 的核查通过率和是否改变 bottom line。
- **Current lean：** 可能（55-80%）偏 A。核查只跑一次最省；席位自己的「Read but not cited」已经提供了缺口来源（researcher #3 的机制）。

### Crux 2：两轴核查是立刻收掉，还是留在审计层先记日志
- **Side A**（skeptic、grade）：收掉。第二轴对论文型 claim 恒为 SINGLE-ORIGIN（第一轮 7 次反证搜索 0 次找到独立来源）；两轴制在情报界实际塌成一轴（#8）；标签越多越不可复现（#9、#10、#7）。
- **Side B**（reader、evaluator）：留在审计层，先跑 5 次看它有没有改过 bottom line。
- **What would settle it：** 同一份 claims.md 用两轴协议核查两遍，看第二轴的一致率和 SINGLE-ORIGIN 占比。
- **Current lean：** 很可能（80-95%）偏 A。本轮核查员自发用了第二轴：20 条里 16 条 SINGLE-ORIGIN，4 条 CORROBORATED，1 条 CONTRADICTED（#7，方向反而支持 A）。保留 CIRCULAR 和 CONTRADICTED 为旗标。

### Crux 3：席位的 Estimates 还要不要
- **Side A**（grade、skeptic）：要，给综合者用，按子问题写倾向；grade 要的是按子问题的四级确定度加脚注。
- **Side B**（reader）：报告里的 Seat estimates 表是假精度（第一轮的「中位 4」从散文格子里算出来），五席不是五个独立估计者。
- **What would settle it：** 读者测验比较有无该表的两版报告。
- **Current lean：** 可能（55-80%）偏「笔记里保留、报告里不放」：席位用七级刻度写倾向，综合者在关键判断里给区间，不算中位数。

## Blind spots
- Co-STORM 附录 B 的思维导图消融和 OmniThink 的表 2：核查员打开了后者（4 个 backbone 里 3 个低于 STORM），没有席位读过前者。
- 没有任何关于「人怎么读 LLM 长报告」的一手研究；reader 席的标准全部来自情报和医学。
- Claude 级核查员的重跑一致率没有数据，只有开源中型模型的（#10）。
- gap round 的 token 成本和触发频率未测。

## Source summary
证据底子三块：2024-2026 的 LLM 论文（多为 ICLR 2026 / NeurIPS 2025，不少是预印本或 workshop）、方法学手册和标准（Cochrane、GRADE、ICD 203，稳定但面向人类读者，属间接）、本 skill 自己的产物（一手，可逐条复核）。弱处：LLM 侧的数字大多测在开源或中档模型、别的任务上；一条关键的编排者错误比例只来自一个系统。承重的是 #18、#17（本地）、#19、#4、#10。
- #2 PARTIAL：RAPID 没有消融 moderator，不是复现；Co-STORM 自己的表显示 diversity 0.602 vs 0.592，方向与 RAPID 相反
- #7 CONTRADICTED：Hartling 2012 在真实综述里 GRADE κ 仅 0.18-0.44（方向支持判断 3）
- #8 SECONDARY：Baker 1968 只剩目录条目，经 Icard 2024 转述
- #9 PARTIAL：粒度是四类系统性因素里最大的一类（98/228），合并为两档一致率只从 69.6% 升到 74.2%
- #11 PARTIAL：969 是算例参数下的数字
- #14 PARTIAL：「reliable proxy」出自 ICLR 2026 workshop 海报，限定层级系统
- #15 PARTIAL：0.76/0.44 是受控温度扰动下的均值，不是默认设置的重跑噪声
- #13：论文正文 69.5/62.8 与其表 1 不一致，只引方向
完整表：verification.md

## Next step
- 在一个无关题目上跑一次 v0.3，测 gap round 的触发和 lint。
- 用 v0.2 两轴协议把本轮 claims.md 再核查一遍，算 Eligible 列一致率（判断 3 的最便宜检验）。
- 写 eval 的 12 道题和 rubric，冻结后再跑任何配置比较。
- 读 Co-STORM 附录 B。

---

## Appendix (for the maintainer)
Seats: S1 evaluator（discovered）· 先改测量再改编排；LOO 子集法 · 核查降级 3 ｜ S2 reader（discovered）· 首屏承重、下半部是审计材料、综合者拼接过数字 · 降级 0 ｜ S3 grade（outsider）· 标签收窄、加间接性、按子问题给确定度、敏感性分析 · 降级 1 ｜ S4 researcher · 主持人机制可迁移、时机不可、盲写自带消融 · 降级 3 ｜ S5 skeptic · 只有 INVERTED 规则和 20 条预算有证据、两轴塌成一轴 · 降级 2（撞 40 轮上限后续跑）
Gap round: 无（本轮按 v0.2 协议运行）
Cost: seats 5 · searches 58 / 60（seats）+ 7（verifier）· fetches 94（seats）+ 56（verifier）· claims checked 20 / 20 listed · agents spawned 6 · tokens 899,772 subagent（seats 723,129：evaluator 153K / skeptic 186K / researcher 134K / reader 130K / grade 119K；verifier 176,643）· wall time 约 45 分钟
Seat metrics（ad hoc 脚本，v0.2 格式）: evaluator 2/8 · reader 3/6 · grade 2/5 · researcher 2/6 · skeptic 2/6（CONFIRMED only this seat / contributed；PARTIAL：3 · 0 · 1 · 3 · 2）
Lint: 6/6
Not verified: 「未进入核查预算」清单 20 项；盲区全部。
