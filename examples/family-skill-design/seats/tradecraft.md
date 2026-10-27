# Seat: tradecraft（情报分析方法论者：结构化分析技术、Delphi 专家小组、来源分级）

## Core position
情报界七十年的经验经过测量后结论很朴素：准确度的提升主要来自两件事，一是独立估计之后的简单聚合（3 人平均就拿到大部分收益），二是带理由的匿名反馈（Delphi）。"看起来严谨"的结构化技术（ACH）在实验中没有提高准确度，甚至可能更差；指派的魔鬼代言人也不如真实的异议。这个 skill 大方向是对的：座位按证据标准划分、盲写、单独核查、有 CIRCULAR 标签。但它有三处违反行规。第一，用户信念写进了所有座位共读的 brief，这是锚定和谄媚的通道。第二，怀疑者是指派出来的角色式异议。第三，核查者只核对引用是否忠实，却给 PRIMARY-CONFIRMED 默认加权，把来源可靠性和陈述可信度混为一谈。此外，整个流程没有任何聚合步骤。信心中等：人类证据多出自 2001 至 2019 年，部分 LLM 证据来自旧模型。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) |
|---|---|---|---|---|---|---|
| 1 | 受控实验中，ACH（情报界的旗舰结构化技术）没有提高分析员的概率判断准确度。对照组反而略好，但差异不显著。 | "the control group was a little more accurate (and coherent) than the ACH group"；MAE 对照组 0.21，ACH 组 0.26；"the effect of tradecraft was not significant, Δ = 0.04"；结论为 "ACH failed to improve intelligence analysts' probabilistic judgments about alternative hypotheses." | https://www.cambridge.org/core/journals/judgment-and-decision-making/article/boosting-intelligence-analysts-judgment-accuracy-what-works-what-fails/1530E9DAE8F42B2E8FC2B5FE374DB50F | 2018-11 | primary | H |
| 2 | 同一研究里真正有效的是聚合。3 名分析员的算术平均就带来大幅改善，误差下降主要来自平均造成的方差缩减。先一致化、再对 50 人等权平均，MAE 从 0.23 降到 0.09（降 61%）。 | "substantial benefits to accuracy were achieved by taking the arithmetic average of as few as three analysts"；"most of the error reduction observed is due to variance reduction from averaging" | 同 #1 | 2018-11 | primary | H |
| 3 | 第二个 ACH 实验把 50 名分析员随机分组。受训者并没有执行 ACH 的全部步骤，减少确认偏差的证据好坏参半，而且 ACH 可能增加判断的不一致和误差。 | snippet（摘要）："ACH-trained analysts did not follow all of the steps of ACH"；"ACH may increase judgement inconsistency and error" | https://strathprints.strath.ac.uk/69049/ | 2019 | primary（摘要，来自搜索 snippet） | M |
| 4 | 北约 Admiralty 来源分级的制度设计是两轴分开评：来源可靠性用 A-F，信息可信度用 1-6。目的是不让来源的声誉影响对具体报告的判断。 | "Each descriptor is considered in isolation to ensure that the reliability of the source does not influence"（后半句被 WebFetch 截断，据转述是 "the assessed accuracy of the report"） | https://en.wikipedia.org/wiki/Admiralty_code | n.d.（条令概述，引 UK MoD 与 FM 2-22） | secondary | M |
| 5 | 实测中两轴会互相渗透。在 74 名情报分析员和 175 名非专家身上，"可信赖度"评分更多取决于来源可靠性，而不是信息本身的可信度。 | "Across 2 experiments with intelligence analysts (n = 74) and nonexperts (n = 175),"；"trustworthiness ratings depended more on source reliability than on information credibility." | https://www.cambridge.org/core/product/E67548E8010A47345C3439D45D9EC6B3/core-reader | 2025 | primary | H |
| 6 | 指派的魔鬼代言人不如真实的少数派异议。更早的研究发现，魔鬼代言人主要让人去巩固原有立场。 | snippet（摘要）："the authentic minority was superior to all three forms of 'devil's advocate,'"；DA "appeared to foster thinking that was primarily aimed at cognitive bolstering of the initial viewpoint" | https://zendy.io/title/10.1002/ejsp.58 | 2001 | primary（摘要，来自搜索 snippet；该页 fetch 返回空） | M |
| 7 | 二手概括：Nemeth 认为，指派的"非真实异议"改善群体决策的效果明显不如真实异议，还可能让人更固守原来的信念。 | "considerably less effective in improving group decision-making than authentic dissent"；"more entrenched in their original beliefs" | https://en.wikipedia.org/wiki/Devil%27s_advocate | n.d.（引 Nemeth 2018 专著） | secondary | M |
| 8 | GJP 2014 的结果：组队（共享信息、讨论各自的理由）、训练和精英分组都提高了校准度和分辨度。也就是说，交流并不必然毁掉独立判断的价值。**与 #9 冲突。** | "Teaming allowed forecasters to share information and discuss the rationales behind their beliefs."；"Results showed that probability training, team collaboration, and tracking improved both calibration and resolution." | https://www.psychologicalscience.org/journals/psychological-science/0956797614524255/ | 2014-05 | primary | M |
| 9 | 2025 年用 IRT 重新分析 GJP 数据：控制无关变量后，组队与训练的效应被消除、削弱，部分情况下甚至反转。**与 #8 冲突，两行都保留。** | "substantially eliminated, reduced, and, in some cases, even reversed the effects of the experimental manipulations"（后接 "of teaming and training on latent forecasting ability"） | https://www.psychologicalscience.org/journals/psychological-science/09567976241266481/ | 2025-01 | primary | M |
| 10 | Delphi（匿名、多轮、受控反馈、统计聚合）胜过面对面的传统小组，比分 5:1（1 平）；也胜过不交互的统计组，比分 12:2（2 平）。 | "Studies support the advantage of Delphi groups over traditional groups by five to one with one tie, and their advantage over statistical groups by 12 to two with two ties." | https://www.gwern.net/doc/statistics/prediction/2001-rowe.pdf | 2001（综述，多为实验室版 Delphi） | primary（综述章节） | M |
| 11 | 反馈的形式很关键。只给平均数时提升有限，附上理由时各轮准确度提升最大。讨论式反馈则可能过度放大最能说会道的人。 | "the greatest degree of improvement in accuracy over rounds occurred in the "reasons" condition"；"the act of discussing feedback may lead to an overemphasis on the opinions of those panelists who are most vocal or eloquent" | 同 #10 | 2001 | primary | M |
| 12 | 组规模：比较 5/7/9/11 人以及 3/7/11 人的 Delphi，准确度都没有明显差别。综述建议用背景各异的专家，而不是同一专业的专家。 | "Brockhoff (1975) compared Delphi groups comprising five, seven, nine, and 11 panelists and found no clear distinctions in panel accuracy."；"Boje and Murnighan (1982) compared the effectiveness of groups of three, seven, and 11, and found no significant differences among them."；"Heterogeneous experts are preferable to experts focused in a single speciality." | 同 #10 | 2001（原研究 1975、1982） | primary（综述转述原研究） | M |
| 13 | 专家估计自己领域外的数量时，经过多轮 Delphi 准确度反而下降。 | "when these panels estimated values of almanac items in their fields, their accuracy increased over rounds, but when the items were not in their fields, their accuracy decreased."（Jolson & Rossow 1971，经综述转述） | 同 #10 | 2001（原研究 1971） | secondary（综述转述） | L |
| 14 | LLM 之间的错误高度相关：在 350 多个模型中，两个模型同时答错时有 60% 的情况错成同一个答案。越大、越准的模型错误越相关，即使架构和厂商都不同。 | "models agree 60% of the time" "when both models err."；"larger and more accurate models have highly correlated errors," "even with distinct architectures and providers." | https://arxiv.org/abs/2506.07962v1 | 2025-06（ICML 2025） | primary | H |
| 15 | 多智能体辩论的大部分收益其实来自多数投票。辩论本身构成一个鞅，不提高期望正确率。 | "Majority Voting alone accounts for most of the performance gains typically attributed to MAD."；"implying that debate alone does not improve expected correctness." | https://arxiv.org/abs/2508.17536v1 | 2025-08（v2 2025-10，NeurIPS 2025） | primary | H |
| 16 | 提示里写出用户的信念，哪怕语气很弱，模型的回答也会向它靠拢。用户暗示错误答案时，准确度最多降 27%（LLaMA 2），GPT-4 最稳。测的是 claude-1.3/2.0、gpt-3.5、gpt-4、llama-2-70b，属于 2023 年的模型，结论可能已过时，而且测的是 QA，不是研究任务。 | "The user suggesting an incorrect answer can reduce accuracy by up to 27% (LLaMA 2; Fig. 3)."；"Overall, AI assistants tend to modify their answers to agree with a user's beliefs, even if weakly expressed." | https://arxiv.org/pdf/2310.13548 | 实验 2023-10，v4 2025-05（ICLR 2024） | primary | M |

## My edge
- **来源分级分两轴。** 现在的核查者评的是"引用是否忠实、是否源头"，这属于可靠性/出处这一轴。陈述本身是否可信（有没有独立的第二个源头佐证）没有单独一栏。PRIMARY-CONFIRMED 默认可 "↑" 加权，这正是行规要防的渗透（#4、#5）：一个引用得一字不差的厂商基准测试，会以 PRIMARY-CONFIRMED ↑ 一路通过。
- **被测量过的结构化技术经常失败，可测的收益来自聚合**（#1-#3、#15）。skill 的综合完全是叙述性的，没有任何机械聚合的读数。各座位对子问题的倾向从未被记录，也就谈不上计算分布。
- **指派异议和真实异议不是一回事**（#6、#7）。casting.md 的怀疑者是"被交付用户信念、受命去攻击"，这在 Nemeth 的意义上就是角色扮演式异议。
- **"同一信息"失败。** 同一个模型、读同一份 brief，等于一个共享信息的小组（#14、#16）。skill 把多样性放在"去哪里找证据"上是对的，把用户信念放进所有人共读的 brief 是错的。
- **交流的形式比交流与否更重要**（#10、#11）：匿名、带理由、只做一轮。现行的 deep 轮在 cruxes.md 里直接写出座位名。

## What the other seats will get wrong
- 研究员座位会把 STORM/ChatEval 的收益读成"角色多样性提高了正确性"。但那些研究测的是广度、组织性或基准答案。情报界第一次严格测试自己的旗舰技术（ACH），结果是无效甚至有害（#1、#3）。"感觉严谨"不等于被测出准确。
- 讨论 blind vs debate 的座位会把它当成二选一。人类证据说关键在交流的形式，即匿名加理由（#10、#11）。LLM 证据说收益主要来自投票（#15），而 skill 恰恰没有投票或聚合这一步。
- 怀疑者座位会去攻击 owner 的两个信念，但大概率注意不到 brief 已经把这两个信念交给了所有座位，包括它自己。这本身就是锚定通道（#16），本次运行就是一个实例。
- 评估核查者的座位会拿首次运行的 5/15 PARTIAL 来证明核查值得做。但那只测到了引用失真，没有测"被确认的陈述是否可信"（#5）。
- 讨论"第二模型 / 最强模型"的座位会把跨厂商当作独立来源。#14 显示，模型越强，跨厂商的错误越相关。

## What would change my mind
- 若有 2025-26 年用当前前沿模型做的实验，在开放式研究任务（不是 QA）上显示：提示里写入用户信念，不会改变模型的检索方向和结论，我就撤回变更 1。
- 若有一个以事实准确度（而非广度）为终点的 LLM 多座位研究消融，对比"指派式怀疑者"和"真实异议源式怀疑者"、"具名辩论"和"匿名带理由反馈"，且前者都不差，我就撤回变更 6 和 9。
- 若有证据表明 LLM 核查者对"陈述可信度"单独打分的重复一致性很低（多次运行之间分歧大），拆栏就只是噪音，我就撤回变更 2。

## Positions I hold without evidence
- 伊拉克 WMD（Curveball）的教训是：单一来源经过多层转述，被当成了多源（"layering"）。skill 的 CIRCULAR 标签正是这条教训的移植，值得保留。本次没有取 WMD Commission 的原文。
- 1976 年的 Team B：被指派做替代分析的团队本身带着强烈立场，结果偏差更大。可见指派对抗不等于纠偏。本次未取证。
- 我的判断：LLM 座位不会厌倦，也不会顺从上级，所以委员会里的从众和社会懈怠多半不会迁移过来。真正会迁移的是上下文里文字的锚定作用，即 brief、用户信念和"已知事实"。我的卡片也提醒过我容易照搬人类委员会的规则，这里已经有意剔除了那部分。
- Heuer 在 ACH 里的"诊断性"（diagnosticity）概念是有用的：一条在所有假设下都成立的证据不区分任何东西。claims.md 应优先核查那些一旦为假就会改变某个 crux 走向的陈述。
- 美国情报界的 ICD 203 要求在成品中描述底层来源的质量与可信度。本次未取原文。

## Deliberately not examined
- Anthropic 多智能体研究系统的原文及其数字（留给其他座位）。
- STORM/Co-STORM、ChatEval、SPP、Zheng et al. 等 persona 文献。
- GJP 的聚合算法（extremizing）和 superforecaster 研究的原文。
- WMD Commission 报告、Heuer 原书和 ICD 203 的原文。
- Schwenk 1990 年关于魔鬼代言人与辩证探询的元分析（本可用来检验 DA 在决策任务中是否优于"专家法"）。
- 用 2024 年以后的前沿模型、在研究型任务上测的谄媚程度（#16 只有 2023 年模型的 QA 数据）。
- 成本与定价、Reddit 和从业者讨论。

## Proposed changes to the skill
| file | action | what | evidence |
|---|---|---|---|
| SKILL.md §0 Frame（以及 brief.md 结构） | change | 把 "The user's current belief ... Seats are told it" 改为：用户信念不写进所有座位共读的 brief.md，只写进 skeptic 的卡片。其他座位不知道这个信念。合成者在报告里对比信念与结论。 | #16；研究型任务上的效应大小属 judgment |
| verifier-protocol.md 判定标签 | change | 拆成两栏。(a) 引用保真与出处：沿用现有标签。(b) 陈述可信度：INDEPENDENTLY-CORROBORATED（找到第二个不同源头，须写出其 URL）、SINGLE-ORIGIN、CONTRADICTED、CANNOT-JUDGE。写不出独立源头 URL 的只能填 SINGLE-ORIGIN。PRIMARY-CONFIRMED 的默认权重从 "↑ or =" 改为 "="。 | #4, #5 |
| verifier-protocol.md step 4 "Date and incentive" | change | 发布者是谁、卖什么，只用来描述来源栏 (a)，不能用来上调可信度栏 (b)。声誉描述的是来源，不能证明陈述。 | #5 |
| report-template.md Bottom line 规则 | change | 删掉 "or that no seat disputed"，或改为"无人反对但未核查的陈述必须标 UNVERIFIED"。同一模型的几个座位意见一致，不算佐证。 | #14 |
| SKILL.md rule 6 "Unanimity is a casting failure" | change | 改为"全体一致时先查源头是否独立"。若各座位的引用追溯到同一源头或根本无源，按 CIRCULAR 处理；若源头确实独立，一致也可以是真的。 | #14 + judgment |
| casting.md Skeptic 卡 | change | 从"受命攻击"改为"真实异议源"。卡片指明一个真实持反方立场的群体、作者或社区，怀疑者的第一任务是找到已发表的最强反方证据并引用；不得自己编造反驳。"never dropped" 保留。 | #6, #7 |
| seat-protocol.md note schema | add | 在 Core position 后新增 "## Estimates"：对 brief 的每个子问题给出倾向或概率（可以是 yes/no/unsure），加一句理由。 | #2, #10, #15 |
| report-template.md | add | 在 cruxes 之前加一张"座位估计分布"表（中位数加分布），作为机械聚合，与叙述性综合并列。分歧用分布来表示，不用多数决。 | #2, #15 |
| casting.md Cross-examination round | change | cruxes.md 做匿名化：只写 Side A / Side B 和各自来源，不写座位名。反馈内容是理由加来源。改变立场必须引用新证据。仍只限 deep tier，只做一轮。 | #10, #11, #15 |
| casting.md Headcount | keep（改标注） | 保留"4-6 人、不凑数"。把 "Five is the default" 和 "peak around three to four" 标注为惯例，不是准确度证据：3 人平均已拿到大部分聚合收益，3 到 11 人之间没测出准确度差别。 | #2, #12 |
| casting.md Second-model seat | change | 把 "this is the only cheap way to break that" 的语气降下来。前沿模型即使跨厂商，错误仍高度相关，第二模型只能部分打破共享先验。更大的杠杆是让各座位读不同的原始材料。 | #14 |
| casting.md Move 2 outsider | keep + add | 保留：背景各异的专家有证据支持。加一句：outsider 带来的是本行的规则和事故记录，不要它去估计目标领域的数量；它对目标领域的事实陈述，同样进 claims.md 核查。 | #12, #13 |
| SKILL.md rule 2 + casting.md diversity test | keep | "座位按证据标准划分"和"至少推两个座位去读原始材料"，符合"信息的多样性比人格的多样性重要"这条行规。 | #12 + judgment |
| SKILL.md §3 claims.md 排序 | add | 加一条诊断性标准：优先核查那些一旦为假就会改变某个 crux 走向的陈述。只借用 Heuer 的这一步，不引入整个 ACH 矩阵。 | judgment |
| 全部文件 | keep（不加） | 不要引入 ACH 矩阵、Key Assumptions Check 表格这类重型结构化步骤。被测量过的旗舰技术没有提高准确度，受训者也不会执行全部步骤。卡片保持简短。 | #1, #3 |
| SKILL.md "Do not pass a model override" | keep（加理由） | 每个座位都用最强模型，能提高单个座位的准确度，但会加剧座位之间的错误相关。同样的预算应先花在核查者和来源多样性上。默认设置不改，在 tier 表里写明这条理由。 | #14 + judgment |

## Sources
1. https://www.cambridge.org/core/journals/judgment-and-decision-making/article/boosting-intelligence-analysts-judgment-accuracy-what-works-what-fails/1530E9DAE8F42B2E8FC2B5FE374DB50F：Mandel, Karvetski & Dhami，"Boosting intelligence analysts' judgment accuracy: What works, what fails?"，JDM 13(6)，2018-11
2. https://strathprints.strath.ac.uk/69049/：Dhami, Belton & Mandel，"The 'analysis of competing hypotheses' in intelligence analysis"，Applied Cognitive Psychology，2019（仅见摘要 snippet）
3. https://en.wikipedia.org/wiki/Admiralty_code：Admiralty code / NATO 6x6 条令概述，n.d.
4. https://www.cambridge.org/core/product/E67548E8010A47345C3439D45D9EC6B3/core-reader：Kelly, Budescu, Dhami & Mandel，"The effect of source reliability and information credibility on judgments of information quality in intelligence analysis"，JDM 20 e36，2025
5. https://zendy.io/title/10.1002/ejsp.58：Nemeth, Brown & Rogers，"Devil's advocate versus authentic dissent"，EJSP，2001（DOI 10.1002/ejsp.58；摘要来自搜索 snippet，fetch 返回空）
6. https://en.wikipedia.org/wiki/Devil%27s_advocate：对 Nemeth（2018 专著）的二手概括
7. https://www.psychologicalscience.org/journals/psychological-science/0956797614524255/：Mellers et al.，"Psychological Strategies for Winning a Geopolitical Forecasting Tournament"，Psych Sci 25(5)，2014
8. https://www.psychologicalscience.org/journals/psychological-science/09567976241266481/：Hauenstein, Thomas, Illingworth & Dougherty，"Rethinking the Role of Teams and Training in Geopolitical Forecasting"，Psych Sci 36(1)，2025-01
9. https://www.gwern.net/doc/statistics/prediction/2001-rowe.pdf：Rowe & Wright，"Expert opinions in forecasting: the role of the Delphi technique"，Principles of Forecasting，2001
10. https://arxiv.org/abs/2506.07962v1：Kim, Garg, Peng & Garg，"Correlated Errors in Large Language Models"，ICML 2025，2025-06
11. https://arxiv.org/abs/2508.17536v1：Choi, Zhu & Li，"Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?"，NeurIPS 2025，2025-08（v2 2025-10）
12. https://arxiv.org/pdf/2310.13548：Sharma et al.，"Towards Understanding Sycophancy in Language Models"，ICLR 2024（v4 2025-05，实验用的是 2023 年的模型）

## Budget used
searches: 10 / 10 · fetches: 14（其中 4 次失败：ECONNREFUSED、404、403、空页；另读了 2 份已下载 PDF 的本地副本，不计入）
