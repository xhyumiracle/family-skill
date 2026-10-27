# Seat: reader

## Core position
报告模板的上半部分承重，下半部分是给审计者和维护者看的，却放在了读者的阅读路径上。两份样例报告的 bottom line 都超过模板规定的 3-5 句（分别为 6 句和 7 句）。真正决定下一步的那句话埋在中间，或者在最后一节；设计报告的 bottom line 引了 16 个 claim 编号，却没说 skill 该改什么。情报产品（ICD 203/208）和系统综述（Cochrane/GRADE）面对的是同一类读者，收敛出的结构也相同：结论先行；可能性用固定刻度表达，并与置信度分开；一张最多 7 行的关键判断表；一段来源总评；完整证据表放在审计文件里。v0.3 应把报告改成这个形状：删掉报告里的 Seat estimates 表、Weight 列和完整账本，再加一道综合之后的逐句核对，因为 2026 年的测量显示编排者是主要出错点。置信度：中高。这些标准都有一手出处，但它们对本 skill 读者的效果没有测过。

## Estimates
- (a) 编排者中途 steering：倾向否（standard 档）。读者能测到的风险在综合阶段，不在田野阶段（#11、#16）。应先加综合后核对，中途干预等这个做完再说；Co-STORM 的消融表留给 researcher 席。
- (b) eval 与区分指标：模板版本用 Rosenbaum 式读者测验来区分，指标是只读前两屏时的理解正确率和找到关键信息的用时（#7）。席位配置的区分指标交给 evaluator 席；我倾向用"只由一席产出、核查通过、且进入关键判断表的 claim 数"，比单纯的独有 claim 数更接近读者价值。
- (c) 两轴核查与 20 条预算：在审计层算净收益，倾向是（两轴一次都还没真正跑过，现在没有数据支持删掉）；在报告层是噪音，倾向否。两列判定加 Weight 列不改变读者的行动：两次运行共 35 行，27 行是 "="，"↑" 一次没出现过（#15）。20 条预算应与报告行数脱钩，报告最多展示 7 条（#5）。
- (d) 模板对十分钟读者是否承重：是，但只有前两屏承重，即 BLUF、Belief vs finding 和 cruxes。Seat estimates、20 行账本、五席一句话、Cost 都是给维护者的。读者最需要、模板却没有的是：开头一句明确的建议，一个固定的可能性刻度，以及承重假设加上会推翻它的指标（#1、#2、#4）。
- (e) 过度工程：删掉报告内的 Seat estimates 表（席位笔记里保留 Estimates 节给综合者用）、Weight 列、报告内的完整账本，以及 bottom line 里逐句插入的 claim 编号；"五席一句话"和 Cost 移到附录和 runs.log。不删的：核查员和 bottom-line 检查，后者还应加强。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) | Novel? |
|---|---|---|---|---|---|---|---|
| 1 | 情报分析标准要求结论先行。多个判断时，要有一句从全部判断里提炼出的主信息，而不是逐条罗列判断 | "Analytic products should present a clear main analytic message up front. Products containing multiple judgments should have a main analytic message that is drawn collectively from those judgments."（ICD 203 D.6.e.(6)，PDF 第 6 页） | https://www.dni.gov/files/documents/ICD/ICD-203.pdf （301 跳转到 archive.dni.gov，PDF 下载后读第 4-6 页） | 2015-01-02 签署；2022-01-21、2023-06-12 技术修订 | primary | H | yes |
| 2 | 同一标准把"事件的可能性"和"对判断依据的置信度"拆开，可能性必须用一套固定的七级词（附数字区间），并且禁止在同一句里混用两者。本 skill 模板里的 "how confident"、"Current lean" 和席位的 H/M/L 都没有锚定 | "specifically the likelihood of occurrence of an event or development, and the analyst's confidence in the basis for this judgment."；表格："almost no chance … 01-05%"、"roughly even chance … 45-55%"、"almost certain(ly) … 95-99%"；"must not combine a confidence level and a degree of likelihood, which refers to an event or development, in the same sentence."；"products should identify indicators that would alter the levels of uncertainty for major analytic judgments." | https://www.dni.gov/files/documents/ICD/ICD-203.pdf （第 5 页） | 2015-01（含 2023 修订） | primary | H | yes |
| 3 | 给读者的来源处理应是一段总评，说明来源底子的强弱，以及哪些来源支撑关键判断；完整清单不进读者产品。ICD 208 还要求先弄清读者需要什么信息 | ICD 203："Source summary statements … should be used to provide a holistic assessment of the strengths or weaknesses in the source base and explain which sources are most important to key analytic judgments."；ICD 208："Sourcing information in each analytic product should enable readers to discover and retrieve sources … while avoiding exhaustive source listings"；"Know Your Customers: … including what information the customer needs, timeliness" | https://www.dni.gov/files/documents/ICD/ICD-203.pdf （第 4-5 页）；https://www.dni.gov/files/documents/ICD/ICD-208-Maximizing-the-Utility-of-Analytic-Products-2017-01-09.pdf （第 1-2 页） | ICD 203 2015；ICD 208 2017-01-09 | primary | H | yes |
| 4 | ICD 203 还有三条要求，模板只部分做到：写明承重假设以及假设错了会怎样；写明本次判断与上一份分析相比是一致还是改变；不回避难下的判断。"Belief vs. finding" 只覆盖了第二条的一半 | "Products should state assumptions explicitly when they serve as the linchpin of an argument … Products should explain the implications for judgments if assumptions prove to be incorrect."；"Analytic products should state how their major judgments on a topic are consistent with or represent a change from those in previously published analysis"；"should not avoid difficult judgments in order to minimize the risk of being wrong." | https://www.dni.gov/files/documents/ICD/ICD-203.pdf （第 5-6 页） | 2015-01 | primary | H | yes |
| 5 | 系统综述给决策者的结论表最多 7 行，次要结局直接省略。报告里放 20 行账本超出这个规格将近三倍 | "'Summary of findings' tables include a row for each important outcome (up to a maximum of seven)."；"review authors will need to omit the less important outcomes from the table." | https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14 | 2023-08（Handbook v6.5，2024） | primary | H | no（grade 席可能也会找到） |
| 6 | GRADE 把审计用的表和读者用的表分开：Evidence profile 写各维度的判定细节，给作者和质疑者看；SoF 表只给一个质量等级，不展开判定细节，给终端读者看。本 skill 的两轴判定属于前者 | evidence profile "is intended for review authors, those preparing SoF tables and anyone who questions a quality assessment"；SoF 面向 "a broader audience, including end users of systematic reviews and guidelines"，给出质量等级 "without details of the judgements about the quality of evidence" | https://gdt.gradepro.org/app/handbook/handbook.html | 2013 年更新版（活文档） | primary | H | no |
| 7 | 一张紧凑的结论表确实承重，有随机试验证据：读者理解显著更好，找到关键信息快得多。所以应该缩小表，而不是删表；这个设计本身也可以直接拿来当读者 eval | "93% vs. 44% ( P = 0.003) and 87% vs. 11% ( P < 0.001)"；"Participants with the SoF table spent an average of 90 seconds to find key information compared with 4 minutes … ( P = 0.002)"；"In two small trials"（RCT II n=18 vs 15） | https://designresearch.no/publications/summary-of-findings-tables-in-cochrane-reviews-improved-understanding-and-rapid-retrieval-of-key-information （J Clin Epidemiol 63，DOI 10.1016/j.jclinepi.2009.12.014） | 2010 | primary | M（样本小） | yes |
| 8 | 只用文字表达可能性时，读者会把它往 50% 拉；加上数字区间后与原意的一致性提高。lean 或"很可能"这类词应附数字 | "As predicted, laypeople interpret IPCC statements as conveying probabilities closer to 50% than intended by the IPCC authors."；替代格式为 "supplementing the verbal terms with numerical ranges"，摘要称其提高了与指南的一致性、更好地区分了各词（这半句是 WebFetch 的转述） | https://ideas.repec.org/a/nat/natcli/v4y2014i6d10.1038_nclimate2194.html （Nature Climate Change 4(6):508-512） | 2014-06 | primary（摘要） | H（方向）/ M（幅度未见） | yes |
| 9 | 引用的存在本身就会提高读者对 AI 输出的信任，随机引用也一样；读者真去核对时信任反而下降。所以一张很长的账本即使没人读，也会制造"严谨感"；真正该推到读者面前的是那些核对后改变结论的行 | "We found a significant increase in trust when citations were present,"；"a result that held true even when the citations were random;"；"we also found a significant decrease in trust when participants checked the citations." | https://arxiv.org/abs/2501.01303 | 2025-01-02（AAAI 2025） | primary | M（场景是聊天问答，不是长报告） | yes |
| 10 | 反证：一项政策简报的随机试验发现，简报几乎改变不了强先验读者的信念，而且效果与简报的具体形式无关。说明模板形式对"改变信念"的作用可能有限，Belief vs. finding 必须正面回应先验 | "the policy brief had little effect on changing the beliefs of readers who held strong prior beliefs"；"the impact of the policy brief seems to be independent of the specific form"（snippet；ALNAP 全文 403，3ie 页只有导语） | https://3ieimpact.org/evidence-hub/publications/working-papers/what-difference-does-policy-brief-make （3ie Working Paper 70，DOI 10.23846/WP0070） | 2012 | primary（只见 snippet） | L | yes |
| 11 | 2026 年对开源 deep-research 系统的错误溯源发现，最终报告的错误绝大多数出在编排者，而不在搜索子代理。本 skill 的核查员只看 claims.md，综合者写报告这一步没有人核 | "84.7% of final-report errors in AI-Q originate at the orchestrator"（摘要；据 WebFetch，其中约 31% 是幻觉，其余是引用错误，这一半为转述）；"Almost every agent makes a lot of mistakes with the exception being those that summarize a single document." | https://arxiv.org/abs/2608.24306 | 2026-08-25（v1） | primary | M（84.7% 只针对一个系统） | yes |
| 12 | LLM 口头报告的置信度系统性偏高；对多次回答做一致性检验和聚合能缓解。所以席位自报的 H/M/L 和 lean 不能当作校准过的数字直接展示；聚合可以做，但要在数字化的 lean 上做 | "LLMs, when verbalizing their confidence, tend to be overconfident"；"consistency among multiple responses, and better aggregation strategies can help mitigate this overconfidence" | https://arxiv.org/abs/2306.13063 | 2023-06 v1 / 2024-03 v2（ICLR 2024；2023 年代模型） | primary | M | no |
| 13 | 本 skill 的两份报告都超出了模板对 bottom line 的长度限制，而且把可执行的那句话埋了。设计报告：6 句，引用 16/20 个 claim 编号，没说要改什么（改动写在"下一步"第 1 条）。Obsidian 报告：7 句，"决定故障率的杠杆与选哪个产品无关"是第 5 句；"先回答一个事实：agent 是离散任务还是常驻进程"放在倒数第二节 | 模板："<three to five sentences …>"；设计报告 bottom line 引用的编号：#1-#12、#16、#18、#19、#20；Obsidian 报告"开放问题与下一步"第 1 条 | /home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md ；/home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/report.md ；/home/xhyumiracle/projects/xhyu/family-skill/skills/family/references/report-template.md | 2026-10-27 | primary（本地产物，本席计数） | H | no（其他席可能也会读到，但大概不会计数） |
| 14 | Seat estimates 表是假精度：(b) 行的"中位 4"是从五个格子里算出来的，其中两格根本不是数字。另外五席是同一个模型，不是独立估计者（round-1 #14：错误相关） | 五格原文："由 eval 定，4×15 vs 6×10"、"3-11 无差别，别凑数"、"4-6，经验判断"、"4"、"3"；分布列："中位 4，总预算固定" | /home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md （Seat estimates 表） | 2026-10-27 | primary（本地产物） | H | yes |
| 15 | 账本的 Weight 列几乎不带信息，两轴判定也从来没在实际运行里用过：round-1 的 verification.md 只有一列 "Verdict"。v0.2.0 的两轴目前是零次运行、零数据 | 设计报告：20 行中 17 行 "="、3 行 "↓"、0 行 "↑"；Obsidian 报告：15 行中 10 行 "="、5 行 "↓"、0 行 "↑"；verification.md 表头："| # | Claim (short) | Cited URL | Verdict | Primary URL (if traced) | …" | /home/xhyumiracle/projects/xhyu/family/family-skill-design/verification.md ；两份 report.md 的证据账本 | 2026-10-27 | primary（本地产物） | H | yes |
| 16 | 本 skill 自己的综合者在 bottom line 里拼接出了错误：把"≥4 分比例之差 +10%"和"均值差的 p=0.084"接在一起。按 verifier-protocol 自己的定义，这属于 STITCHED，却通过了 bottom-line 检查，因为检查按 claim 判定把关，不按句子把关 | 报告 bottom line："人评的 +10% 覆盖度在 20 对样本上 p=0.084（#3）"；verification #3："是 ≥4 分比例之差（70.0-45.0；67.5-57.5），不是均值差；Coverage 均值差 p=0.084"；verifier-protocol："the 'quote' is assembled from several sentences, the claim is MISQUOTED (sub-label … STITCHED)" | /home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md ；/home/xhyumiracle/projects/xhyu/family/family-skill-design/verification.md | 2026-10-27 | primary（本地产物） | H | yes |

## My edge
- 我把报告当作"十分钟内要据此行动"的读者来读，不当作管线输出来读：数了 bottom line 的句数、里面引用的编号数、Weight 列的分布、Seat estimates 的中位数是怎么算出来的（#13-#16）。
- 带来两个行业为同一类读者写下的硬规格：情报产品（主信息先行、七级可能性刻度、置信度单列、来源总评、不列穷尽清单）和系统综述（结论表最多 7 行、证据档案与读者表分开、有随机试验支持的结论表）（#1-#7）。
- 区分审计层和阅读层。大部分臃肿不是信息多余，而是放错了层：两轴判定和 20 行账本属于审计层，GRADE 的 evidence profile 也是这个位置（#6）。
- 在本 skill 自己的产物里找到一个综合者拼接错误（#16），并有 2026 年的外部测量说明编排者是主要出错点（#11）。这让"综合后核对"比"中途 steering"更值得先做。

## What the other seats will get wrong
- grade 席会把核查标签做得更细（更多子标签、更多列）。这在审计层是对的，但如果直接搬进 report.md，读者路径会更长。层必须分开，报告里只显示一个推导出来的等级（#6）。
- evaluator 席会倾向 DeepResearch Bench / ResearchRubrics 那类 rubric，奖励全面性和引用准确率。但引用本身就会抬高信任，随机引用也一样（#9）；按报告完整度或引用数打分，奖励的是"看起来严谨"。至少要加一项只读前两屏的读者理解测验（#7）。
- researcher 席会根据 Co-STORM 主张加一个中途 moderator。2026 年测得的主要出错点恰恰是编排者（#11），本 skill 的编排者也已经在综合时出过错（#16）。不加核对就增加编排者的输出，等于扩大了没人核查的面。
- 多数席位会把 Seat estimates 当作 round-1 已经定下的"聚合步"保留。给综合者用的聚合没问题（round-1 #11 的 Mandel 证据针对的是独立分析员的数字概率），但把文字 lean 算成中位数展示给读者是假精度（#12、#14）。

## What would change my mind
- 在 2-3 份已有报告上做 Rosenbaum 式读者测验：如果现行模板和"BLUF + ≤7 行关键判断表"版本的理解正确率和找信息用时没有差别，那么模板重排就不值得做。
- owner 实际据报告行动时用过账本行（比如回头查过某个 # 的 URL）。那样账本就不是审计层，而是阅读层，应该留在报告里。
- 2608.24306 的 84.7% 如果在"编排者只负责综合、不管引用"的系统上不成立，那么综合后核对的优先级要往后排。

## Positions I hold without evidence
- 这个 skill 的实际读者（owner 本人，技术背景、单人决策）读完 bottom line、cruxes 和下一步就会行动，不读账本。NN/g 2008 年的网页数据说读者最多读 28% 的字、更可能是 20%，但那是网页、旧数据，没有放进 claims 表。
- 对 LLM 综合者来说，"3-5 句"这种自由约束会被突破（2/2 次运行都超了），带固定槽位的模板（①建议 ②可能性/置信度 ③承重假设与指标）更容易被遵守。
- 中文报告里，七级刻度应该有固定的中文词，例如：几乎不可能 1-5%、很不可能 5-20%、不太可能 20-45%、大致五五开 45-55%、可能 55-80%、很可能 80-95%、几乎确定 95-99%。这个译法是我的判断。
- 两份报告里最有决策价值的内容都是"owner 才能回答的事实"，比如 agent 是离散任务还是常驻进程。这类内容应该在报告第二行就出现，而不是放在最后。

## Deliberately not examined
- Co-STORM 的消融表（researcher 席）、自动评测的 rubric 设计（evaluator 席）、证据分级方法论（grade 席），都按卡片分工没有碰。
- AR 25-50（陆军公文 BLUF 规定）的原文：只看到 Wikipedia 的二手转述，没打开一手 PDF；BLUF 的论证改用 ICD 203 (6)。
- Beynon 等 2012 的全文和效应量：ALNAP 返回 403，只有 snippet。
- 2024-2026 年针对"读者如何阅读 LLM 长报告或 deep-research 报告"的用户研究：两次搜索都没找到一手研究，这是本席最大的证据空白。读者行为证据大多比 brief 要求的 2024-2026 窗口更早（ICD 2015/2017、Cochrane 2023、Rosenbaum 2010、Budescu 2014）；标准类文件本来就稳定，但需要说明。
- 用 LLM 充当"读者"做理解测验时的效度：没有查。
- Reddit 或从业者论坛上关于 deep-research 报告怎么用的讨论：没有搜。

## Proposed changes to the skill
| file | keep/change/add/remove | what | evidence row # or "judgment" |
|---|---|---|---|
| references/report-template.md | change | Bottom line 改为三个固定槽位：① 一句结论或建议（读者下一步做什么、该信什么）；② 可能性用七级刻度加数字区间，置信度（高/中/低）另起一句并给原因，两者不放同一句；③ 一句承重假设，加上会推翻它的指标。总长 ≤150 字，claim 编号集中放在句末一个括号里 | #1 #2 #4 #8 #13 |
| references/report-template.md | add | 紧跟 bottom line 加 "Key judgments" 表，≤7 行，列为：判断 · 可能性/置信度 · 最强的核查通过来源（一个 URL）· 什么会改变它。在读者路径上取代 "What every seat agreed on" | #5 #6 #7 |
| references/report-template.md | change | "Evidence ledger" 改为 "Source summary"：先写 3-5 行总评（来源底子是什么、弱在哪、哪几条承重），再列触及关键判断的 PARTIAL / MISQUOTED / CONTRADICTED / UNCHECKED 行；完整表留在 verification.md，报告里只给路径 | #3 #6 #9 |
| references/report-template.md | remove | 报告里的 "Seat estimates" 表。席位笔记的 Estimates 节保留，给综合者用；如果席位给的是数字区间，就在 Key judgments 行里写区间（最小到最大），不算中位数；分歧只在 cruxes 里按"哪些来源"表达 | #12 #14 |
| references/report-template.md | change | "Belief vs. finding" 扩为 "Belief / previous judgment vs. finding"，紧跟 Key judgments：先正面回应 owner 的先验；重跑或已有旧报告时，写明哪条判断变了、是哪条新证据改变的 | #4 #10 |
| references/report-template.md | change | "The seats, one line each"、"Cost" 和 seat metrics 移到分隔线之后的 "Appendix (for the maintainer)"，同样内容写入 runs.log | #13，主要是 judgment |
| references/report-template.md | keep | Cruxes 里的 "What would settle it" 和 "Current lean" 保留；lean 改用同一刻度表达，写 "open" 时必须同时写出指标 | #2 #4 |
| references/report-template.md | keep | Blind spots 永不为空；但最多 3 条，先写会改变 bottom line 的那条 | judgment |
| SKILL.md（步骤 4） | add | 综合后逐句核对：bottom line 和 Key judgments 表里的每个数字、每个引号内短语，必须能在 verification.md 对应行里找到原样字符串；找不到就改写，或标 [UNVERIFIED]；不匹配的数量写进 runs.log。只读文件，不增加 agent | #11 #16 |
| SKILL.md（步骤 0） | change | brief.md 的 "What it is for" 改为必填三项：读者要做的决定、期限、什么结果会让他行动。这就是 bottom line 第①格的锚 | #3（ICD 208 Know Your Customers）#1 |
| SKILL.md（步骤 5） | change | 回复里的 bottom line 直接复制报告的三个槽位，不另写一版；cruxes 列表最多 3 条 | judgment |
| SKILL.md（eval / runs.log） | add | 读者测验作为 eval 的一项：只给报告前 300 字（约前两屏），问四个问题：建议是什么、多确定、什么会改变它、最弱的承重 claim 是哪条；答案键从 verification.md 生成；记录正确率和用时。用它比较模板版本，不用来比较席位配置 | #7 |
| references/verifier-protocol.md | remove | "Weight" 列（= / ↓ / ↑）：两次运行共 35 行中 27 行是 "="，"↑" 从未出现，信息已经包含在判定列里 | #15 |
| references/verifier-protocol.md | add | 加一列由两轴机械推出的 "Grade"：A＝一手确认且有独立佐证；B＝确认但只有单一来源；C＝PARTIAL / CIRCULAR / UNREACHABLE；X＝MISQUOTED / CONTRADICTED。报告只显示 Grade，两轴细节留在审计文件 | #6 #15 |
| references/verifier-protocol.md | keep | 两轴本身留在审计层。它还没有在任何一次运行中真正跑过，没有数据就删掉为时过早 | #15 |
| references/seat-protocol.md | change | Estimates 每行改为：lean 用七级刻度词加数字区间，置信度单独写，不写"中位数"之类的聚合 | #2 #8 #12 |
| SKILL.md（步骤 3） | keep | 核查 20 条的预算保留（这是审计用的），但与报告行数脱钩：报告最多展示 7 条关键判断 | #5，加上 judgment |

## Sources
1. https://www.dni.gov/files/documents/ICD/ICD-203.pdf （301 跳转到 archive.dni.gov）：ICD 203 Analytic Standards，含 2022 和 2023 技术修订；读的是 PDF 第 1-6 页的原文图像；签署于 2015-01-02
2. https://www.dni.gov/files/documents/ICD/ICD-208-Maximizing-the-Utility-of-Analytic-Products-2017-01-09.pdf ：ICD 208 Maximizing the Utility of Analytic Products，读了第 1-3 页；签署于 2017-01-09
3. https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14 ：Cochrane Handbook 第 14 章，SoF 表最多 7 个结局；2023-08 更新
4. https://gdt.gradepro.org/app/handbook/handbook.html ：GRADE Handbook，evidence profile 与 SoF 表的受众区分；2013 版，活文档
5. https://designresearch.no/publications/summary-of-findings-tables-in-cochrane-reviews-improved-understanding-and-rapid-retrieval-of-key-information ：Rosenbaum, Glenton, Oxman，J Clin Epidemiol 63，两项 SoF 表随机试验；2010
6. https://ideas.repec.org/a/nat/natcli/v4y2014i6d10.1038_nclimate2194.html ：Budescu, Por, Broomell, Smithson，Nature Climate Change 4:508-512，跨国研究读者如何理解 IPCC 的可能性用词；2014
7. https://arxiv.org/abs/2501.01303 ：Ding et al., Citations and Trust in LLM Generated Responses，AAAI 2025；2025-01
8. https://3ieimpact.org/evidence-hub/publications/working-papers/what-difference-does-policy-brief-make ：Beynon, Chapoy, Gaarder, Masset，3ie WP 70，政策简报随机试验；2012；只见 snippet
9. https://arxiv.org/abs/2608.24306 ：Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research；2026-08-25
10. https://arxiv.org/abs/2306.13063 ：Xiong et al., Can LLMs Express Their Uncertainty?，ICLR 2024；2023-06 / 2024-03
11. /home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md 和 verification.md ：round-1 报告与核查表（本席计数）；2026-10-27
12. /home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/report.md ：round-0 报告（本席计数）；2026-10-27
13. 打开过但没进 claims 表：https://en.wikipedia.org/wiki/BLUF_(communication) （AR 25-50 的二手转述，2013 版）；https://www.nngroup.com/articles/how-little-do-users-read/ （Nielsen，2008-05-05，网页阅读比例）

## Budget used
searches: 12 / 12 · fetches: 19 次 WebFetch 调用，其中 4 次是 301 跳转提示，实际打开 15 个页面（第 1、2 次搜索各超出 2 次，原因是同一文档的跳转；1 次 404，1 次 403，1 个 PDF 抽不出文字）· 另有 2 个 PDF 下载到本地后用 Read 读取 · stopped because: budget spent
