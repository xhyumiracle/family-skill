# Seat: skeptic

## Core position
v0.2.0 新增的结构里，同时有机制和证据的只有两项：MISQUOTED-INVERTED 规则（round-0 那条截断后意思反转的引文）和 20 条核查预算（round-1 第 16 至 20 条里抓到一处承重修正，核查员只占约 20% 的 token）。其余几项是 credibility 轴、Estimates 表、seat metrics 和 deep 档反馈轮，它们要么运行次数为 0，要么在 round-1 没产出任何可聚合的东西。外部证据显示，细粒度判定标签无论交给人还是交给 LLM 都难以复现；情报界的双轴评级，87% 的打分落在对角线上。"v0.2.0 优于 v0.1.0" 目前没有任何 v0.2.0 运行可以作证。最小的 v0.3：核查改为单轴（5 个标签加 2 个旗标）；报告删掉 Estimates 表和席位指标，指标移入 runs.log 并写清定义；评测用配对设计加计数指标，不用 rubric 总分。置信度：中。

## Estimates
- (a) 编排者中途引导：no（standard 档不加新阶段）。理由：盲写独立是 round-1 定论；Co-STORM 主持人的输入是"未使用的信息"，这一点 family 已经在核查员的 "Found but not cited" 里事后产出，缺的是有人去跟进，而不是缺一个实时阶段。deep 档：把从未运行过的反馈轮改成一次事后 "gap round"。
- (b) 评测：10 至 20 题只能检出大效应。以 Miller 的例子外推，n=20、每题单次采样时，最小可检测效应约 41 个百分点（按 1/√n 换算，是我的计算，不是论文数字）。所以要用配对设计（同题、同一核查员、两种配置），配计数指标：不同 primary URL 数、独有 CONFIRMED claim 数、抓到的降级数、删掉某席后 bottom line 是否改变。rubric 总分在这个样本量下分不出 3、4、5 席。
- (c) 两轴判定：no，净噪声。第二轴对"某论文某表的某个数字"这类 claim 几乎恒为 SINGLE-ORIGIN。20 条预算：yes，保留，便宜而且抓到过东西。
- (d) 报告模板：部分承重。Bottom line、Cruxes、Blind spots、Evidence ledger、Next step 承重；Seat estimates 表、Cost 里的 seat metrics、"五席一句话"对十分钟读者是杂物。
- (e) 该砍的过度设计：credibility 轴及其 4 个标签、报告里的 Estimates 表和 seat metrics、seat 笔记里的 H/M/L 置信度列（judgment）。从未运行过的 deep 反馈轮不删，改作 gap round。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) | Novel? |
|---|---|---|---|---|---|---|---|
| 1 | v0.2.0 的两轴核查从未运行过。"v0.2.0 优于 v0.1.0" 没有一次 v0.2.0 运行作证。两次运行的降级率之差同时混入了模型、题目和核查预算三个变量。git 里也没有 v0.1 到 v0.2 的 diff。 | round-1 verification.md 表头只有一个判定列 `Verdict`，后面紧跟 `Primary URL (if traced)`，没有 credibility 列。runs.log 只有两行，都是 2026-10-27："5 seats (sonnet, v1 archetype cast, no outsider/discovered) ... 5 PARTIAL (2 meaning-inverting, mislabelled PARTIAL)" 对 "5 seats (opus; 1 discovered, 1 outsider, 3 archetypes) ... 3 PARTIAL, 0 MISQUOTED"。.git/logs/HEAD 只有一行："commit (initial): family 0.2.0" | file:///home/xhyumiracle/projects/xhyu/family/family-skill-design/verification.md ; file:///home/xhyumiracle/projects/xhyu/family/runs.log ; file:///home/xhyumiracle/projects/xhyu/family-skill/.git/logs/HEAD | 2026-10-27 | primary（本 skill 产物） | H | yes |
| 2 | 本 skill 的典型 claim 是"某论文某表的某个数字"，对这类 claim，credibility 轴几乎恒为 SINGLE-ORIGIN，不携带信息。round-1 核查员对 #1 至 #7 做了反证或复现搜索，7 条里 0 条找到独立的第二来源。 | #1 "反证搜索：未找到独立复现或反驳"；#2 "反证搜索：未找到复现"；#3 "反证搜索：未发现反驳"；#5 "反证搜索：未找到独立复现或反驳"；#6 "反证搜索：未找到独立复现"；#7 "反证搜索：未找到反驳论文"；#4 只找到一篇不同任务的论文 (Kong et al.)。round-0 #3："反证搜索：未找到相反报告(也未找到佐证)" | file:///home/xhyumiracle/projects/xhyu/family/family-skill-design/verification.md | 2026-10-27 | primary（产物） | H（计数）/ M（推论） | yes |
| 3 | 情报界 Admiralty 双轴（来源可靠性 × 信息可信度）正是 v0.2 两轴的原型。实际使用中，评级员把两轴塌成一条对角线，标签集中在一个众数上；对同一材料，可信度一轴与标准答案的分歧高达 49%。"文件上分两轴"不等于"打分时两轴独立"。 | "[3] observed that 87% of the scores (N = 608 out of 695) fell stricly along the diagonal of the scale"；"Moreover, score B2 alone comprised 75% of all the ratings (N = 518)"；"[3] showed that collected ratings differed from the instructor's solution about 49% of the time for credibility, and 15% of the time for reliability"；[3] 即 "In 1968, Baker, McKendry & Mace analyzed 695 joint ratings obtained from two US intelligence corps during field exercises" | https://arxiv.org/abs/2405.19968 | 数据 1968；综述 2024-05-30 | secondary（Icard 综述 1968 年的一手研究；一手报告未打开） | M | yes |
| 4 | 职业事实核查机构对同一条 claim 的细粒度判定常常不一致，分歧主要出在等级粒度上；按粗粒度（方向）比较时几乎完全一致。也就是说，粗标签可复现，细标签不可复现。 | "749 were matching claims, of which 521 (69.6%) received identical ratings, while the remaining 228 (30.4%) had diverging ratings."；"Rating discrepancies are attributed to various systematic factors: 1) differences in the granularity of verdict ratings, ..."；"After adjusting these systematic discrepancies, we found only one case out of 749 matching claims with conflicting verdict ratings."；Lee 对 Lim (2018) 的转述："the fact checkers agreed on obvious truths and falsehoods but had lower agreement rates for statements in the ambiguous rating range"。Lim 原文 κ=0.52 只见于搜索结果摘要，不是逐字引文（DOAJ 返回 403） | https://misinforeview.hks.harvard.edu/wp-content/uploads/2023/10/lee_fact-checking_fact_checkers_20231026.pdf （DOI 10.37016/mr-2020-126）；Lim: https://doaj.org/article/1bbf739b92544595b33db6f907f8a1ba | 2023-10-26；Lim 2018-07 | primary（Lee）；Lim 部分为 snippet | H（Lee）/ L（κ） | yes |
| 5 | 经过培训的人类标注员做三档引用支持判断（full / partial / no），一致率是全部判断里最低的。作者在算 Likert 一致率之前，还得先把 5 档粗化成 3 档。 | Table 4 两两一致率："Citation Supports 82.0"，"Verifiability 94.6"，"Statement Supported 82.2"；"When calculating agreement on fluency and perceived utility judgments, we coarsen the 5-point Likert judgments into three options" | https://arxiv.org/abs/2304.09848 | 2023-04（EMNLP Findings 2023） | primary | M（并非粒度的对照实验） | yes |
| 6 | 对 LLM 核查员来说，最难的类别恰恰是"来源与陈述相反"。这正是 MISQUOTED-INVERTED 要抓的东西：规则的机制成立，但它到底触发了多少次无人测量。 | "Models struggle most notably with contradictory errors."；AttrEval-GenSearch 上 GPT-4 zero-shot 的 F1：Attributable 87.3，Contradictory 45.0，Extrapolatory 89.6（表格数字经 WebFetch 转录） | https://arxiv.org/abs/2305.06311 | 2023-05（EMNLP Findings 2023） | primary | M（2023 年模型） | yes |
| 7 | 同一个 LLM 评审用同样的设置跑 3 次，连二值事实一致性标签都复现不稳；多次运行取多数投票能提高与人工判断的一致性。一次核查产出的一组标签只是一个样本。 | Table 1 "Self-reliability of different LLM judges on the SummaC benchmark across 3 runs"：Llama 3.1 0.3263，Deepseek-R1 0.6278，Qwen-3 0.7883；"Qwen 3 gave the same judgment on all 3 runs for only 61.3% of cases"（MT-Bench）；"for Deepseek-R1 and Qwen 3, taking the majority vote gives a higher balanced accuracy than the maximum accuracy achieved by a single run" | https://arxiv.org/abs/2510.27106 | 2025-10-31（Findings EMNLP 2025） | primary | M（开源中型模型，不是 Claude） | yes |
| 8 | 20 条预算的边际收益在 round-1 可见且成本低。前 13 条全部 PRIMARY-CONFIRMED；3 处降级 (#14、#15、#18) 里，只有 #18 落在 15 条预算之外；#18 的修正改动了 Crux 2 所依赖的"异质专家"一句。核查员占全部子代理 token 不到 20%。 | ledger：#14 PARTIAL、#15 PARTIAL、#18 PARTIAL，其余 PRIMARY-CONFIRMED；#18 的 Note："p.128 "Heterogeneous experts are preferable to experts focused in a single speciality." 是作者推理出的原则，不是实证结果"；Cost："verifier 118,860"，"606,291 subagent" | file:///home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md ; file:///home/xhyumiracle/projects/xhyu/family/family-skill-design/verification.md | 2026-10-27 | primary（产物） | H | yes |
| 9 | seat metric "仅由一席产出的已核验 claim" 在同一份报告里自相矛盾，还把 PARTIAL 算成了已核验。分子由编排者挑哪些 claim 进 claims.md 决定，所以这个指标量到的是编排者的选择，不是席位的价值。 | Belief 段："仅由一席产出的有 10 条，其中 6 条来自 tradecraft"；Cost 行："tradecraft 6 · researcher 2 · builder 1 · practitioner 1 · skeptic 1"（合计 11）；tradecraft 的 6 条是 "#11-#14、#18-#19"，其中 #14、#18 在 ledger 里是 PARTIAL；SKILL.md 第 3 步："From the seat notes write claims.md ... Rank by diagnosticity first" | file:///home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md ; file:///home/xhyumiracle/projects/xhyu/family-skill/skills/family/SKILL.md | 2026-10-27 | primary（产物） | H | yes |
| 10 | round-1 的 Seat estimates 表是编排者从散文里拼出来的，格子里几乎没有可聚合的倾向，只有 (b) 一行有数字。round-1 的 seat 笔记里没有 Estimates 段，所以 v0.2 在 seat 一侧补上的 Estimates 段，本轮是第一次测试。 | 表格单元格如 "未测，outsider 作实验臂"、"异质专家优先，outsider 保留但只带规则不估数"；"分布"列为 "5/5「未测」；4/5 保留 outsider 带约束"；只有 (b) 一行写着 "中位 4"。round-1 skeptic 笔记的标题依次是 Core position、Claims and evidence、My edge 等，没有 Estimates | file:///home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md ; file:///home/xhyumiracle/projects/xhyu/family/family-skill-design/seats/skeptic.md | 2026-10-27 | primary（产物） | H | yes |
| 11 | 小样本 eval 检不出中小效应。要检出 3 个百分点的差异，大约需要 969 道独立题目；每题多采样、做配对比较，是"免费"的方差缩减手段。 | WebFetch 对论文算例的转述（非逐字）："with a 3-point minimum detectable difference, 80% power, and a 5% false-positive rate ... about 969 independent questions"；逐字："reduces the Minimum Detectable Effect from 13.2% to 7.5%"（n=198，每题采样从 1 次增到 10 次）；"paired differences represent a "free" reduction in estimator variance when comparing two models"；"We therefore recommend using the paired version of the standard error estimate wherever practicable." | https://arxiv.org/abs/2411.00640 | 2024-11 | primary | H | partly |
| 12 | 在公认的 deep-research 基准上，头部系统之间 rubric 总分只差约 2 分，计数指标却差约 2.7 倍。基准自己的引用核查也只用二值判定。 | RACE Overall：Gemini-2.5-Pro Deep Research 48.88，OpenAI Deep Research 46.98；FACT E. Cit.：111.21 对 40.79（表格经 WebFetch 解析，列头有歧义；二手来源给出 49.71/46.45 和 48.92）；"This results in a binary judgment ('support' or 'not support') for each pair." | https://arxiv.org/abs/2506.11763 | 2025-06（ICLR 2026） | primary | M | partly（基准已在 brief 中，这个角度是新的） |
| 13 | 读者对回答的偏好主要由长度驱动；标题、加粗、列表这些格式元素只是二阶效应。模板的标题本身几乎不影响观感，但每多一节，就多耗读者的时间。 | "All in all, when analyzing the style coefficients, we found that length was the dominant style factor."；"All other markdown effects are second order."；Control Both 系数：Length 0.249，List 0.031，Header 0.024，Bold 0.019 | https://www.lmsys.org/blog/2024-08-28-style-control | 2024-08-29 | primary | H（对 Arena 聊天偏好）/ M（迁移到报告） | yes |
| 14 | 与第 13 行冲突：一个 deep-research 报告基准报告说，评审分数与报告长度几乎不相关。 | snippet："The Pearson correlation is nearly zero (r = -0.02, p = 0.67), and the Spearman correlation is also very small (ρ = 0.10, p < 0.01)"，800 份报告（附录 N；抓取被截断，未见原文） | https://arxiv.org/abs/2512.17776 | v5 2026-07-13 | primary（只见 snippet） | L | yes |
| 15 | 给判断者更多信息，提升的是信心而不是准确度。"更多标签、更多小节显得更可信"正是这个机制：它让人更相信，却不让结论更准。 | "We report three studies that show when judges receive more information, their confidence increases more than their accuracy, producing substantial confidence-accuracy discrepancies." | https://ideas.repec.org/a/eee/jobhdp/v107y2008i2p97-105.html | 2008-11（OBHDP 107(2)） | primary（摘要） | H（人类判断）/ M（迁移） | yes |
| 16 | 一个把 agent 大幅简化的工程报告：18 个工具砍到 1 个，效果反而更好、更便宜。但它的证据只有 5 道题，和"复杂更好"的证据一样薄。两边的教训一致：没有测量就无法判断。 | "100% success rate instead of 80%."；"We benchmarked the old architecture against the new file system approach across 5 representative queries."；"Addition by subtraction is real."；表格（经 fetch 转述）：274.8s 降到 77.4s，约 102k 降到约 61k tokens | https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools | 2025-12-22 | primary（工程博文） | M（text-to-SQL agent，接近范围外） | yes |
| 17 | 反方证据，支持模板：固定结构在简化材料上更易检索，但在真实文献上没有显示出检索速度优势。结构对"找得到"可能有用，对"读得快"未证实。 | "it is perhaps not surprising that they are easier to search (study 14)"；更复杂的真实 MEDLINE 摘要的研究 "have not shown an advantage for search speed."；读者主观评分 7.92 对 6.10 只见于搜索摘要 | https://informationr.net/ir/hartley1.html | 2004（JMLA 92(3)） | secondary（作者综述，含其本人的研究） | M | yes |

## My edge
- 我把 v0.2.0 的产物本身当证据来读，而不是只读它引用的文献。读出三件事：两轴核查一次都没跑过（第 1 行）；round-1 核查员事实上的 credibility 搜索 7 次里 0 次找到独立来源（第 2 行）；seat metric 在同一份报告里是 10 也是 11，还把 PARTIAL 算成"已核验"（第 9 行）。这三条都不需要外部文献。
- 我区分"标签更多"和"标签更可靠"。人和 LLM 在粗粒度方向上一致率高，细分等级上一致率低（第 4、5、7 行）。双轴在情报界实际是一条对角线（第 3 行）。对 LLM 核查员来说，"相反"恰恰是最难判的类别（第 6 行）。
- 我对 (b) 做了功效估算：10 至 20 题的 rubric 总分只能检出约 40 分级别的差异，而头部系统之间只差约 2 分；计数指标的差距在倍数级（第 11、12 行）。所以能区分席位配置的只有计数指标加配对设计。
- 我也承认自己的盲点：作为开源 skill，固定标题对其他用户有可读性价值，对合成器有可解析价值，这部分结构不应按"效果未测"砍掉。我砍的是声称自己代表严谨度的标签，不是文档骨架。

## What the other seats will get wrong
- evaluator 会把 rubric 总分（RACE 式或 ResearchRubrics 式）当作区分 3、4、5 席的指标。在 10 至 20 题时这个指标没有功效：头部商用系统之间只差约 2 个 RACE 分（第 11、12 行），席位数之间的差只会更小。
- researcher 会把 Co-STORM 的主持人消融读成"加一个实时引导阶段"。Co-STORM 主持人的原料是"已检索但未使用的信息"；round-1 核查员的 "Found but not cited" 恰好列出了 Co-STORM 本身，结果无人跟进，直到又跑了一整轮。缺口在于没人去执行，不在于少了一个阶段。
- grade 席可能建议引入 GRADE 的四级确定性作为又一个标签轴。这是在第 3 至 7 行描述的问题上叠加新的细粒度标签；如果采用，应当折叠进现有的单列判定，不要新开一轴。
- 有人会拿 round-0 的 5/15 和 round-1 的 3/20 降级率，证明 v0.2、opus 或新 casting 更好。这两次运行的模型、题目类型（GitHub issue 对论文表格）和核查预算全都不同（第 1 行）。

## What would change my mind
- 用两个独立的核查员实例，各自按 v0.2 协议检查同一份 claims.md：如果两轴标签的 Krippendorff α 都不低于 0.8，并且 credibility 轴不是近乎常数（SINGLE-ORIGIN 占比低于 70%），我会保留两轴。
- 任意一次运行里，credibility 轴的判定（CONTRADICTED 或 INDEPENDENTLY-CORROBORATED）改变了 bottom line 中的一句话，而单列判定做不到这一点。
- 一个小型读者实验：同一份运行，生成带 Estimates 表和不带的两版报告，让读者在 10 分钟内回答 5 个关于结论和 crux 的问题；带表版本的正确率明显更高。

## Positions I hold without evidence
- 席位指标一旦写进报告，下一轮编排者挑 claim 时就会倾向于"让 outsider 有分"（Goodhart），使这个指标更加失真。
- 实时中途引导会把编排者正在形成的看法泄露给本应盲写的 seat。在只能"读文件、单层派生"的 harness 里，它还意味着第二波派生，成本接近再跑一轮。
- seat 笔记中 H/M/L 置信度列在下游没有任何用途，而且是不可复现的口头标签；核查员的判定才是置信度。
- 对开源用户而言，可见的结构本身有文档价值，即便效果没有测过。这一点削弱了我"越小越好"的立场，所以我只砍标签和报告里的派生表，保留协议标题。
- 每条降级判定附上相邻句原文，让读者能复判，比提高标签的可复现性更划算。

## Deliberately not examined
- Co-STORM 主持人消融表（researcher 的领地）；GRADE 规则（grade 席）；新 rubric 设计（evaluator）。
- Baker, McKendry & Mace (1968) 的一手报告：只通过 Icard 2024 的综述读到。
- Lim 2018 全文（DOAJ 403）：κ=0.52 只见搜索摘要。
- DEER 附录 N 的原文：抓取被截断，第 14 行只有 snippet。
- Claude 级别核查员的自一致性：没有找到对应数据，第 7 行是开源中型模型的结果。
- 评分刻度研究 arXiv 2601.03444（0-5 分刻度时人机一致性最高）读了首页，没有列为 claim：它比较的是数值刻度，不是分类标签。
- arXiv 2606.01629（LLM 评审长篇报告，rubric 引导下与人工的准确率 DR-Bench 0.5479 到 0.7075，RealDR 0.4179 到 0.4787）读了，没有列为 claim，因为准确率的定义没有核实。
- Reddit 和从业者对 skill 复杂度的反馈；该 skill 仓库的 issue 和用户数：没有查。
- Kapoor et al. "AI Agents That Matter" 一类的成本控制评测：属于编程任务，在范围外，没有用。

## Proposed changes to the skill
| file | keep/change/add/remove | what | evidence row # or "judgment" |
|---|---|---|---|
| verifier-protocol.md | change | 两轴合并为单列判定：CONFIRMED（注明 primary 或 secondary）/ PARTIAL / MISQUOTED（INVERTED、STITCHED、ABSENT）/ UNREACHABLE / UNCHECKED。CIRCULAR 和 CONTRADICTED 降为附加旗标，只在找到具体 URL 时填写。删除 INDEPENDENTLY-CORROBORATED、SINGLE-ORIGIN、CANNOT-JUDGE 三个默认标签。 | 1, 2, 3, 4, 5 |
| verifier-protocol.md | keep | MISQUOTED-INVERTED / STITCHED 规则，以及"要求逐字句子"的取证指令。这是唯一有本 skill 自身事故（round-0 #2 的 lishid 引文）支撑的标签细分，而"相反"正是 LLM 最难判的类别。 | 6；round-0 verification.md #2 |
| verifier-protocol.md | change | 每条 PARTIAL 和 MISQUOTED 必须附上原句和相邻句的逐字原文（round-1 核查员已自发这么做），让读者能复判，而不是依赖标签本身可复现。 | 7 + judgment |
| verifier-protocol.md | remove | "Weight" 列（↑ = ↓ ↓↓）：它完全由判定标签推出，是重复信息。 | judgment |
| SKILL.md | keep | standard 档 20 条核查预算，以及规则 5 "Do not trade verifier budget for more seats"。 | 8 |
| SKILL.md | change | 第 4 步 seat metrics 从报告移出，只写进 runs.log，并给出操作定义：独有已核验 claim 指 claims.md 中 "Relied on by" 恰好只有一席、判定为 CONFIRMED 的 claim；PARTIAL 另计；同时记录该席进入 claims.md 的条数作为分母。 | 9 |
| SKILL.md | add | 一段简短的 Eval 说明：比较配置时用配对设计（同题、同一核查员、两种配置）；主指标用计数，即不同 primary URL 数、独有 CONFIRMED claim 数、被抓到的降级数、删掉某席后 bottom line 是否改变；n 小于 100 时不以 LLM rubric 总分作决策；积累 10 次配对运行之前不改默认席位数。 | 11, 12, 13, 14 |
| CHANGELOG.md | change | 0.2.0 条目加一行："unvalidated by any run: credibility axis, seat estimates, seat metrics, feedback round"，不要暗示 v0.2 已被证明更好。 | 1 |
| report-template.md | remove | "Seat estimates" 表。子问题的倾向在 Bottom line 里用一句话写分布（如"5 席中 4 席倾向 X"），完整倾向留在 seat notes。 | 10, 15 |
| report-template.md | remove | "The seats, one line each" 小节，以及 Cost 里的 "Seat metrics" 行。Cost 只留总量（席位数、搜索数、token、核查条数）。 | 9, 13, 15 |
| report-template.md | change | 给 Evidence ledger 以上部分加长度上限（judgment：英文 ≤ 1,000 词，中文 ≤ 2,000 字），超出就删，不压缩字体或格式。 | 13, 15 + judgment |
| report-template.md | keep | Bottom line（受 ledger 约束）、Belief vs. finding、Cruxes（含 What would settle it）、Blind spots、Evidence ledger、Next step。round-0 报告没有 Estimates 表和 seat metrics，同样给出了可以直接执行的下一步（两周受控实验）。 | 17 + judgment；round-0 report.md |
| casting.md | change | deep 档反馈轮（运行 0 次）改为 "gap round"：合成之前，编排者从核查员的 "Found but not cited" 和各席的 "Deliberately not examined" 里挑出至多 2 个未用信息点，派至多 2 个 seat，每个 5 次搜索去追。这相当于 Co-STORM 主持人"从未用信息里提问"的事后版本；seat 看不到彼此的结论，盲写保持不变。 | judgment；round-1 verification.md 的 "Found but not cited" 列出了 Co-STORM 却无人跟进 |
| seat-protocol.md | remove | claims 表的 Confidence (H/M/L) 列：下游没有人使用，且是不可复现的口头标签；保留 Type 和 Novel? 两列。 | judgment（第 3、4 行为类比） |
| seat-protocol.md | keep | Estimates 段，要求写 yes / no / unsure 或数字。round-1 的表之所以是散文，是因为当时 seat 没被要求写倾向；本轮是第一次测试，跑过 3 次以上再决定去留。 | 10 |

## Sources
1. file:///home/xhyumiracle/projects/xhyu/family/family-skill-design/verification.md：round-1 核查表（单一 Verdict 列；#1 至 #7 的反证搜索记录）。2026-10-27
2. file:///home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md：round-1 报告（Seat estimates 表、seat metrics、ledger、Cost）。2026-10-27
3. file:///home/xhyumiracle/projects/xhyu/family/family-skill-design/seats/skeptic.md：round-1 skeptic 笔记（没有 Estimates 段、没有 Novel? 列）。2026-10-27
4. file:///home/xhyumiracle/projects/xhyu/family/runs.log：两次运行的记录。2026-10-27
5. file:///home/xhyumiracle/projects/xhyu/family-skill/.git/logs/HEAD 与 /home/xhyumiracle/projects/xhyu/family-skill/CHANGELOG.md：只有一个初始提交，CHANGELOG 是 v0.1 到 v0.2 的唯一变更记录。2026-10-27
6. file:///home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/report.md 与 verification.md：round-0 报告与核查。2026-10-27
7. https://arxiv.org/abs/2405.19968：Icard，A Dynamic Logic for Information Evaluation in Intelligence，综述 Admiralty 评级实验（含 Baker, McKendry & Mace 1968）。2024-05-30
8. https://misinforeview.hks.harvard.edu/wp-content/uploads/2023/10/lee_fact-checking_fact_checkers_20231026.pdf：Lee, Xiong, Seo, Lee，"Fact-checking" fact checkers，HKS Misinformation Review 4(5)。2023-10-26
9. https://doaj.org/article/1bbf739b92544595b33db6f907f8a1ba：Lim，Checking how fact-checkers check，Research & Politics（403，只见搜索摘要）。2018-07
10. https://arxiv.org/abs/2304.09848：Liu, Zhang, Liang，Evaluating Verifiability in Generative Search Engines（附录 E 一致率表）。2023-04
11. https://arxiv.org/abs/2305.06311：Yue et al.，Automatic Evaluation of Attribution by Large Language Models（AttrScore）。2023-05
12. https://arxiv.org/abs/2510.27106：Haldar & Hockenmaier，Rating Roulette: Self-Inconsistency in LLM-As-A-Judge Frameworks。2025-10-31
13. https://arxiv.org/abs/2411.00640：Miller，Adding Error Bars to Evals。2024-11
14. https://arxiv.org/abs/2506.11763：DeepResearch Bench（RACE / FACT 主表）。2025-06
15. https://www.lmsys.org/blog/2024-08-28-style-control：LMSYS，Does style matter? 风格控制回归系数。2024-08-29
16. https://arxiv.org/abs/2512.17776：DEER benchmark（长度偏差分析只见 snippet）。v5 2026-07-13
17. https://ideas.repec.org/a/eee/jobhdp/v107y2008i2p97-105.html：Tsai, Klayman, Hastie，Effects of amount of information on judgment accuracy and confidence，OBHDP 107(2)。2008-11
18. https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools：Vercel 工程博文，d0 agent 从 18 个工具砍到 1 个。2025-12-22
19. https://informationr.net/ir/hartley1.html：Hartley，Current findings from research on structured abstracts（JMLA 92(3)）。2004
20. https://arxiv.org/abs/2601.03444：Li et al.，Grading Scale Impact on LLM-as-a-Judge（只读了首页，未列为 claim）。2026-01-06
21. https://arxiv.org/abs/2606.01629：Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation（读了，未列为 claim）。v4 2026-08-28

## Budget used
searches: 12 / 12 · fetches: 17（2 次 403：DOAJ、cogprints；5 份 PDF 经 WebFetch 无法解析，改为本地读取已保存的副本；DEER 抓取被截断，未见附录 N） · stopped because: budget spent
