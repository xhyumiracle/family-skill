# Seat: grade

## Core position
v0.2.0 的核查员做对了评级行业在最省事的快速综述里也不肯砍的那一步：第二个人逐条核对抽取（保真轴）。这一步保留。它缺的是评级行业真正交付的东西：每个子问题一个第二评审能复现的确定度。两轴判定从未跑过（第一轮 verification.md 只有单栏 Verdict）。第二轴规定"有佐证就上调"，GRADE 的上调条件比这严得多。第一轮真正的不确定性来自 GRADE 叫"间接性"的那类问题（2023 年的模型、单一数据集、别的任务）：17 条 PRIMARY-CONFIRMED 里至少 6 条带这类注释，权重却没动。v0.3 应收窄标签，加间接性列，由综合者按子问题给四级确定度，用 GRADE 的固定措辞写结论，报告以 SoF 表为核心。编排者可以中途纠偏，前提是由预先写定的规则触发并记录为 protocol amendment。信心：中。

## Estimates
- (a) 编排者中途纠偏：有条件的 yes。只做一次，时点在 fieldwork 结束后、核查之前，触发规则预先写进 brief（例如某子问题没有任何直接证据），并记入 amendments.md。不在 fieldwork 进行中改题，也不按"哪边更有意思"选方向（#12、#13；Co-STORM 消融留给 researcher 席）。
- (b) eval：任何配置开跑之前先写定 eval protocol。主指标用"留一席敏感性分析"：去掉某一席后重新综合，看各子问题的结论或确定度变不变。辅助指标两个：每个子问题"直接且核查通过"的 claim 数；核查员重测一致率。10-20 题只够做一个预设的主比较（建议 outsider 开/关），其余比较都算探索（#1、#12、#13、#14）。
- (c) 两轴判定 + 20 条预算：保真轴是净收益，保留。第二轴目前是没检验过的复杂度，而且"佐证即上调"不合 GRADE 的上调规则，应改为子问题确定度的下调理由之一，不再单独给权重。20 条预算保留，但按子问题分配，每个子问题至少 2 条（#4、#6、#7、#11）。
- (d) 报告模板：部分承重。承重的是 bottom line 加一张按子问题排的 SoF 表（结论、确定度、理由脚注、claim 号）。"五席都同意的"、"每席一行"和正文里的全量证据账本是杂物，移到附录（#9、#10、#16）。
- (e) 该砍的过度设计：11 个判定标签和逐条权重箭头（没有起点，无法复现）；CIRCULAR、UNREACHABLE、UNCHECKED 三者合并；按席位分列的 Estimates 表移出正文。真正缺的是间接性和确定度，不是更多标签（#1、#3、#5、#6）。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) | Novel? |
|---|---|---|---|---|---|---|---|
| 1 | 证据确定度用操作化的结构规则来评，评级者间一致性从约 0.3 升到约 0.7；评级者越多一致性越高；配对讨论出的共识评级不提高一致性。与 #2 冲突，见 #2 | "The IRR without using the GRADE approach for two individual raters was 0.31"；"0.27 (95% CI = 0.19-0.37) among the GRADE working group members (n = 15)"；用 GRADE 后 0.66 和 0.72；三名评级者 0.80/0.74，四名 0.84/0.79；摘要另述共识评级未提高信度（WebFetch 转述，非逐字） | https://www.rti.org/publication/the-grade-approach-is-reproducible-in-assessing-the-quality-of-evidence-of-quantitative-evidence-syntheses | 2013（J Clin Epidemiol 66(7)） | primary（摘要） | H | yes |
| 2 | 证据体不能做 meta 分析时，有经验的评审对同一证据的强度评级可以差得很远。family 处理的证据几乎都属于这一类。与 #1 冲突：#1 用的是训练过的评级者和定量合成好的证据 | snippet："the conclusions reached by experienced reviewers based on the same evidence can differ greatly, particularly when they are faced with bodies of evidence that do not lend themselves to meta-analysis" | https://ncbi.nlm.nih.gov/books/NBK98221 | 2012-05（AHRQ Pub. No. 12-EHC067-EF） | primary（只见搜索摘要；NCBI 页面被浏览器验证挡住） | M | yes |
| 3 | 层级多、标签细的偏倚风险工具（RoB 2），即便由方法学者使用，一致性也只有 fair，部分领域只有 slight，而且耗时 | "The agreement was fair for the overall risk of bias (0.27, standard deviation 0.06)"；"the agreement was slight for domains 2 and 3"；"The mean time to complete RoB 2 was 34 minutes (standard deviation 17)"；"The application appears to be complex and requires a sound background in the methodology"（4 名评级者，事先未校准，70 项试验中前 30 项的初步结果） | https://abstracts.cochrane.org/2019-santiago/reliability-and-applicability-revised-cochrane-risk-bias-tool-randomized-trials-rob-2 | 2019（Cochrane Colloquium 摘要，初步结果） | primary | M | yes |
| 4 | Core GRADE（2025）把单项研究的偏倚风险简化成二分；起点由研究设计决定；上调只在效应量大或很大时考虑。佐证数量本身不是上调理由（后一句是我据此推出的，不是原文） | "Core GRADE users first classify individual studies as low or high risk of bias."；"randomised controlled trials begin as high certainty evidence"；"can consider rating up certainty of evidence when risk ratios from pooled estimates suggest large or very large effects." | https://researchportal.plymouth.ac.uk/en/publications/core-grade-4-rating-certainty-of-evidencerisk-of-bias-publication/ | 2025-05（BMJ 389） | primary（摘要） | H | yes |
| 5 | 间接性是 GRADE 单独命名的下调领域：研究的人群、干预、结局、场景与目标问题差别越可能改变效应大小，越应下调 | "When target and study PICOs differ substantially, studies provide indirect evidence."；"The greater the likelihood of substantial differences the more advisable rating down for indirectness." | https://archive-ouverte.unige.ch/unige:185846 | 2025-05-20（BMJ 389:e083865） | primary（摘要） | H | yes |
| 6 | 第一轮里，17 条 PRIMARY-CONFIRMED 至少有 6 条在注释里带适用范围或间接性限制，权重仍是"="；报告只能把间接性写成一句全局 caveat。核查标签没有放间接性的位置 | verification.md：#5 "cognitive synergy only emerges in GPT-4"；#9 "90.2% 出自 Anthropic 未公开的内部研究评测"；#11 "单一研究，共 50 名分析员"；#16 "+15.6% 只针对 ChatDev 在 ProgramDev 上的结果"；#17 "范围仅限多跳推理、三个模型家族"；#19 "27% 是 \"up to\"，为单一模型的最大值"。六条的 Weight 列都是 "="。report.md："最大 caveat：以上证据几乎都来自 2023-2025 年的模型和封闭答案任务，迁移到今天的开放式研究属推断" | /home/xhyumiracle/projects/xhyu/family/family-skill-design/verification.md ；/home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md | 2026-10-27 | primary（本 skill 的运行产物） | H | yes |
| 7 | v0.2.0 的两轴判定没有任何一次运行：第一轮核查表只有一栏 Verdict。第一轮核查员最有价值的产出是 Corrections 段，其中三条改了 claim，判定标签却没动 | 表头："\| # \| Claim (short) \| Cited URL \| Verdict \| Primary URL (if traced) \| Evidence date \| Publisher / incentive \| Weight \| Note \|"（没有 credibility 列）；Corrections："#8（措辞精度，判定不变）"、"#12（归属，判定不变）"；#4 权重 "=（引语须改）" | /home/xhyumiracle/projects/xhyu/family/family-skill-design/verification.md | 2026-10-27 | primary（本 skill 的运行产物） | H | partly |
| 8 | 确定度是"真值落在某个阈值哪一侧"的把握，不是对点估计的把握；评审应写明自己用的阈值或范围。同一批证据换了语境，确定度可以从高变低 | "Certainty of evidence is best considered as the certainty that a true effect lies on one side of a specified threshold"（后接 "or within a chosen range"）；"It is desirable for systematic review authors, guideline panelists, and health technology assessors ... to specify the threshold or ranges they are using when rating the certainty in evidence."；"the certainty of the evidence can vary depending upon the context" | https://eprints.gla.ac.uk/140632 ；https://pmc.ncbi.nlm.nih.gov/articles/PMC6542664 | 2017-05（J Clin Epidemiol 87:4-13） | primary | H | yes |
| 9 | GRADE 对结论措辞有固定写法：确定度和效应大小共同决定动词，高为直述，中为 "likely"，低为 "may"；这套写法在系统综述的生产者和使用者中接受度超过 60% | "x results in a large reduction…"；"x likely results in a large reduction…"；"x may result in a large reduction…"；"Statements for low, moderate and high certainty evidence were acceptable to >60%"；方法上对 "unacceptable to ≥40% of participants" 的措辞做了修改 | https://experts.mcmaster.ca/display/publication1676921 | 2020（J Clin Epidemiol，GRADE guidelines 26） | primary（摘要） | H | yes |
| 10 | 在随机试验中，读者用新版 Summary-of-findings 表格对"疗效对应的证据质量"答对的比例明显更高。人群是医学综述使用者，用到 LLM 报告读者身上属间接证据 | "63% (95% confidence interval {CI}: 55, 71) and 62% (95% CI: 52, 71) more correct answers, respectively"（分别对应 risk difference 和 "quality of the evidence associated with a treatment effect"）；随机化 290 人 | https://research.lstmed.ac.uk/en/publications/improving-grade-evidence-tables-part-1-a-randomized-trial-shows-i-5/ | 2016（J Clin Epidemiol 74:7-18） | primary（摘要） | H（数字）/ M（迁移） | partly（reader 席可能找到） |
| 11 | Cochrane 快速综述在时间受限时的砍法：确定度评级从"两人独立"降为"一人评、一人核对"，但核对这一步不砍；结局数控制在 7 个以内；每次上调或下调都要写理由脚注 | "GRADE guidance recommends that two reviewers independently assess the COE of each relevant outcome."；"For RRs subjected to time constraints, we recommend that a single reviewer conducts COE ratings."；"To accelerate the process, consider rating fewer than seven outcomes."；"Explanatory footnotes summarise reasons for downrating or uprating the COE."；"The first reviewer needs to provide a clear rationale for each decision to up- or downrate the COE." | https://pmc.ncbi.nlm.nih.gov/articles/PMC10850678 | 2023-04（BMJ EBM 29(1):50-54，Cochrane Rapid Reviews Methods Group） | primary | H | yes |
| 12 | 即便事先注册了 protocol，系统综述也常常中途改主要结局，或者从未写明主要结局。没有记录的中途变更是常态，不是例外 | "A discrepancy in the primary outcome occurred in 32% of the included reviews."；"39% of the reviews did not explicitly specify a primary outcome(s)."（96 篇 PROSPERO 注册综述；结果是否有利与改结局之间无显著关联） | https://research-information.bris.ac.uk/en/publications/a-third-of-systematic-reviews-changed-or-did-not-specify-the-prim/ | 2016-04（J Clin Epidemiol） | primary（摘要） | H | yes |
| 13 | Cochrane 的敏感性分析是把那些武断或不明确的决定换成替代选项，重做一遍分析；要做哪些分析，应在 protocol 阶段预先写定。"留一席重新综合"正是这一工具 | "A sensitivity analysis is a repeat of a meta-analysis in which alternative decisions are substituted"（后接 "for decisions that were arbitrary or unclear"，见检索摘要）；"As an author, you should predefine at the protocol stage which study characteristics you plan to investigate" | https://documentation.cochrane.org/revman-kb/sensitivity-analyses-260702328.html | as-of 2026-10（活文档） | primary（官方文档） | H | yes |
| 14 | 在系统综述的数据抽取任务上，LLM 与人类的一致性（κ 0.28-0.48）低于人类之间（κ 0.65）。未测 Claude，任务是抽取不是核查，对本 skill 属间接证据 | human "substantial (Cohen's κ=0.65)"；对第一审者 ChatGPT 0.36、DeepSeek 0.48、Qwen 0.48、Mistral 0.44、Grok 0.41；"their agreement with human reviewers remains limited and their performance is insufficient to replace human judgment." | https://conferences.publisso.de/en/conferences/gmds2025/25gmds060 | 2025-09（GMDS 年会；2025-11-03 发表） | primary（会议摘要） | M | yes |
| 15 | 做偏倚风险判断时，LLM 比人类更保守，即使证据就在文中，也倾向给"高风险"或"No Information"。由此推测：LLM 核查员可能偏向 CANNOT-JUDGE 或 UNREACHABLE 这类回避性标签（推论） | "finding that LLMs remain overly conservative compared to human reviewers, frequently opting for high-risk or \"No Information\" judgments even when evidence is present."（Llama-3.3-70B、GPT-3.5-Turbo、GPT-4o、Claude 3.5 Sonnet；245 份人工评估） | https://arxiv.org/abs/2511.03048 | 2025-11-04（arXiv v1） | primary（从 PDF 第 1 页读出） | M | yes |
| 16 | 第一轮的 Seat estimates 表格单元格是散文，不是 yes/no/数字；"分布"列也是散文。brief 没给子问题定义"yes"的阈值，聚合就无从复现 | 例："(a) 角色生成 … \| 未测，outsider 作实验臂 \| 异质专家优先，outsider 保留但只带规则不估数 \| …"；"(b) 席位数 \| 由 eval 定，4×15 vs 6×10 \| 3-11 无差别，别凑数 \| 4-6，经验判断 \| 4 \| 3 \| 中位 4，总预算固定" | /home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md | 2026-10-27 | primary（本 skill 的运行产物） | H | partly |

## My edge
- 我知道评级一致性的实际数字。结构化、操作化的规则能把一致性从约 0.3 拉到约 0.7（#1）；但证据不能合并（#2）或工具层级太细（#3）时，有经验的人也评不一致。family 的证据正是不能合并的那一类。所以标签要少、定义要硬、每次下调要写理由，不要再加标签。
- 间接性是 GRADE 单独命名的领域（#5），也是第一轮真正的不确定性来源（#6）。v0.2.0 只问"页面是否这么说"和"有没有第二来源"，没问"这条证据说的是不是我们的问题"。2023 年的模型、QA 任务，搬到 2026 年的开放研究上，就属于这一类。
- 对照评级行业三条规矩，v0.2.0 的情况：遵循了"先写 protocol 再搜"（brief 先于 fieldwork，子问题事先给定，核查优先级有规则）和"第二人核对"（#11）；违背了"上调有严格条件"（第二轴"佐证即上调"，#4）；忽略了"每个结局给确定度，并写明阈值"（#8）、"间接性"（#5）和"变更要记录"（#12）。
- 快速综述是现成的"二十分钟版 GRADE"：砍掉双人独立评级，保留一人评、一人核，结局数不超过 7，每次升降写脚注（#11）。family 的形状与此几乎一致，所以该补的是"按子问题给确定度 + 脚注"，而不是更多核查预算。
- 评估席位的贡献，Cochrane 已有现成工具：敏感性分析（#13）。在已有的笔记上去掉一席重新综合，不需要新的搜索，就能直接测出这一席是否改变了结论。

## What the other seats will get wrong
- 有人会把 17/20 PRIMARY-CONFIRMED 当成质量分。它量的是引用忠实度，不是确定度；第一轮的不确定性藏在注释里的间接性限制中（#6），标签上看不到。
- evaluator 席多半会提议用 LLM judge 按 rubric 打分作主指标，却不测 judge 自身的重测一致性。没有操作化定义时，人类评级者之间约 0.3（#1），RoB 2 这种复杂工具只有 0.27（#3）。一个不能复现的指标分辨不出 3 席和 5 席的差别。
- researcher 席可能把 Co-STORM 的 moderator 结果当成"允许中途随意改方向"的依据。在综述行业，没有记录的中途变更正是结局切换的通道（#12）。纠偏可以做，但规则要预先写好，并且记录在案。
- reader 席可能把确定度信息当成杂物砍掉。SoF 的随机试验显示，把证据质量放在每个结论旁边，正是读者理解"这条有多可靠"的关键（#10）。真正该砍的是按席位分列的表和正文里的全量账本。

## What would change my mind
- 把第一轮的 claims.md 交给 v0.2.0 两轴核查员跑两遍：如果第二轴原始一致率不低于 0.8，并且至少改变了一句 bottom line 的措辞或确定度，第二轴就值得原样保留。
- 如果核查员的间接性标注在重测中一致率很低（比如原始一致率低于 0.6），间接性就只该留在注释里，不进结构化列，确定度由综合者一人判断。
- 如果在第一轮上做留一席敏感性分析，去掉任何一席都不改变任何子问题的结论或确定度，说明 5 席在这个题目上冗余，我对"默认 4 席"的支持会转向 3 席。

## Positions I hold without evidence
- 当某个标签占绝大多数时（第一轮 17/20 是 PRIMARY-CONFIRMED），κ 会被压低（kappa paradox），所以重测必须同时报原始一致率。检索摘要里有一篇方法博客提到这一点，我没有打开，也没有找一手文献。
- 适应性设计的原则是"调整规则事先写定就不算作弊"。我把这条迁到编排者纠偏上，但这轮没有为它找来源（例如 FDA 的 adaptive design guidance）。
- 编排者读完席位笔记后自己挑 claims.md，又自己写综合，这是一条选择偏倚通道：可能下意识地优先核查支持正在成形的结论的 claim。"每个子问题、每个 crux 两侧都至少入选一条"的规则能部分堵住这条通道。
- 四级确定度（高/中/低/极低）是对读者还有用的最粗分法；再细，LLM 评级者之间无法复现。
- family 引用的大量证据是工程博客和定性材料，GRADE-CERQual（方法局限、一致性、充分性、相关性）可能比 GRADE 更贴合。这轮没有查。

## Deliberately not examined
- Co-STORM moderator 消融表本身（researcher 的领地），LLM 基准和 rubric 的设计细节（evaluator），GRADE 的 SoF 研究之外的人类报告阅读研究（reader）。
- deep 档的匿名反馈轮：我的领地里没有新证据，不评价。
- GRADE 的发表偏倚领域在网页检索上对应什么（搜索引擎排序偏倚、厂商内容的 SEO），没查。
- PRISMA 2020 第 24 条（注册与修订）原文没有取到逐字引语；protocol 变更的论点靠 #12 和 #13 支撑。
- 成本：每条提议的 token 成本只做了粗估（见下表），没有实测。按我这一席的偏向，可能把完整综述的严格程度带进了二十分钟的流程。因此所有新增项都放在综合者的内联步骤，或只在 eval 运行时做，不增加每次运行的 agent 数。
- Minozzi 2020 正式论文的最终 κ 值（只拿到 2019 年的初步摘要）；BMC Med Res Methodol 2025 那篇 LLM 研究（跳转到登录页，没打开）。

## Proposed changes to the skill
| File | Keep / change / add / remove | What | Evidence row # or "judgment" |
|---|---|---|---|
| verifier-protocol.md | keep | 要求逐字取证；MISQUOTED-INVERTED/STITCHED 规则；只设一名核查员，只核对，不综合 | #7、#11 |
| verifier-protocol.md | change | 第一轴 7 个标签收成 4 个：CONFIRMED（另标 primary/secondary）、PARTIAL、MISQUOTED（INVERTED/STITCHED/ABSENT）、NOT-VERIFIED（合并原 UNREACHABLE 和 UNCHECKED，写明原因）。CIRCULAR 移到第二轴，作为 SINGLE-ORIGIN 的一种原因 | #1、#3、#15 |
| verifier-protocol.md | add | 新增一列"是否直接适用于本问题"：direct 或 indirect。若为 indirect，写一个原因（模型代际、任务类型、人群或场景、单一数据集）。只做标记，不评分 | #5、#6 |
| verifier-protocol.md | remove | 删掉逐条 Weight 箭头和 "Only axis 2 can raise a claim's weight"。两轴结果加上间接性列，一起作为子问题确定度的下调理由输入 | #4、#7、judgment |
| verifier-protocol.md | change | "Publisher / incentive"列改为"来源风险 low/high"并写一句理由。high = 厂商自述、未公开的内部评测、作者评自家系统 | #4 |
| SKILL.md（步骤 0，brief） | add | 每个子问题写明"yes"指什么（阈值或范围），以及它服务于哪个决定 | #8、#16 |
| SKILL.md（步骤 3） | change | claims.md 选择规则：每个子问题至少 2 条，每个 crux 两侧各至少 1 条；20 条总预算不变 | #11、judgment |
| SKILL.md（步骤 4） | add | 综合者给每个子问题一个四级确定度（高/中/低/极低）；每次下调写一条脚注，理由从这几项里选：保真问题、单一来源或矛盾、间接、来源风险、席位间不一致 | #8、#11、#2 |
| SKILL.md（新步骤 2.5） | add | 缺口轮：standard 档可选，deep 档默认。fieldwork 结束后，若某子问题没有任何直接证据，resume 1-2 个相关席位，每席 4 次搜索，卡片上只写缺口。触发规则、时间和原因记入 amendments.md。fieldwork 进行中不干预 | #12、#13、judgment |
| report-template.md | change | Bottom line 按确定度用固定措辞：高"X 会…"，中"X 很可能…"，低"X 可能…"，极低"证据非常不确定"。每句仍带 claim 号 | #9 |
| report-template.md | change | 把"Seat estimates"改成 Summary-of-findings 表，列为：子问题、结论、确定度、下调理由（脚注）、claim 号、席位分布（例如 4/5 yes） | #10、#16 |
| report-template.md | remove | "What every seat agreed on"并入 SoF 表各行；"The seats, one line each"和全量 Evidence ledger 移到 Cost 之后的附录，正文只留 bottom line 用到的账本行 | #10、judgment |
| 新增 references/eval.md（或并入 SKILL.md 步骤 5） | add | 任何配置开跑之前写定 eval protocol：题目、rubric、唯一主指标、唯一主比较；其余比较一律标为探索 | #12、#13 |
| 新增 references/eval.md | add | 两个低成本测量。① 留一席重新综合（不新增搜索），看子问题的结论或确定度是否改变。② 用同一份 claims.md 重跑一次核查员，报原始一致率和 κ。两者只在 eval 运行中做，不进日常运行 | #13、#1、#14、#15 |
| runs.log 格式（SKILL.md 步骤 5） | change | 每次运行追加：各子问题的确定度、indirect claim 占比、NOT-VERIFIED 条数 | #6、#15、judgment |

## Sources
1. https://www.rti.org/publication/the-grade-approach-is-reproducible-in-assessing-the-quality-of-evidence-of-quantitative-evidence-syntheses ：Mustafa et al.，GRADE 评级者间信度（摘要），2013
2. https://ncbi.nlm.nih.gov/books/NBK98221 ：Berkman et al.，AHRQ EPC 证据强度评级信度测试（只见检索摘要），2012-05
3. https://abstracts.cochrane.org/2019-santiago/reliability-and-applicability-revised-cochrane-risk-bias-tool-randomized-trials-rob-2 ：Minozzi et al.，RoB 2 一致性与耗时（初步结果），2019
4. https://researchportal.plymouth.ac.uk/en/publications/core-grade-4-rating-certainty-of-evidencerisk-of-bias-publication/ ：Core GRADE 4，偏倚风险二分、起点与上调，BMJ 2025
5. https://archive-ouverte.unige.ch/unige:185846 ：Core GRADE 5，间接性，BMJ 2025-05-20
6. /home/xhyumiracle/projects/xhyu/family/family-skill-design/verification.md ：本 skill 第一轮核查表，2026-10-27
7. /home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md ：本 skill 第一轮报告，2026-10-27
8. https://eprints.gla.ac.uk/140632 和 https://pmc.ncbi.nlm.nih.gov/articles/PMC6542664 ：Hultcrantz et al.，确定度的阈值定义，J Clin Epidemiol 2017
9. https://experts.mcmaster.ca/display/publication1676921 ：Santesso et al.，GRADE guidelines 26 结论措辞，J Clin Epidemiol 2020
10. https://research.lstmed.ac.uk/en/publications/improving-grade-evidence-tables-part-1-a-randomized-trial-shows-i-5/ ：Carrasco-Labra et al.，SoF 表格随机试验，J Clin Epidemiol 2016
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC10850678 ：Gartlehner et al.，Cochrane 快速综述的确定度评级指南，BMJ EBM 2023
12. https://research-information.bris.ac.uk/en/publications/a-third-of-systematic-reviews-changed-or-did-not-specify-the-prim/ ：Tricco et al.，PROSPERO 注册综述的主要结局变更，J Clin Epidemiol 2016
13. https://documentation.cochrane.org/revman-kb/sensitivity-analyses-260702328.html ：Cochrane RevMan 知识库，敏感性分析定义与预先写定，as-of 2026-10
14. https://conferences.publisso.de/en/conferences/gmds2025/25gmds060 ：Stenzel et al.，LLM 做系统综述数据抽取的一致性，GMDS 2025
15. https://arxiv.org/abs/2511.03048 ：Hevia et al.，ROBoto2，LLM 辅助 RoB 2，2025-11-04

## Budget used
searches: 12 / 12 · fetches: 23（第 5 次搜索多跟了一次跳转，抓回的是登录页，超出每次搜索 2 次的上限 1 次）；另从磁盘本地读取已下载的 PDF 1 次 · stopped because: budget spent
