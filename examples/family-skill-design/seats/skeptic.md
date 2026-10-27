# Seat: skeptic（怀疑论者：一个模型戴五顶帽子，账单是 15 倍 token）

## Core position
有硬证据的只有两件事。第一，让 seat 去不同地方找来源：STORM 去掉 perspective 后，收集到的独立来源数从 99.83 降到 54.36；给 seat 换人设则没有用，Zheng 2024 测得 persona 不提升准确率。第二，独立核验：深度研究系统的引用准确率只有 40–80%，首跑 15 条里 5 条被降为 PARTIAL。其余设计都没有在开放式研究上测过，包括 5 个 seat、强制 outsider、deep 档交叉质询、每个 seat 用最强模型。能找到的近邻证据要么是零增益（debate 约等于投票），要么随基座模型变强而缩小，要么在等 token 预算下消失。拿到九成价值的最便宜管线是：一个强模型做发现和提纲，2–3 个按证据来源划分的中档检索 seat，再加一个 claim 预算翻倍的 verifier。置信度：中。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) |
|---|---|---|---|---|---|---|
| 1 | Anthropic 的 +90.2% 来自 Opus 主控加 **Sonnet** 子 agent，即它自己没有让子 agent 用最强模型。这与业主信念 (2) 相冲突。 | "Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2%" ; "on our internal research eval" | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06 | primary | H |
| 2 | 多 agent 的增益主要是"花了更多 token"，不能算作"视角"本身的功劳；该对比也不是等 token 对比。 | "token usage by itself explains 80% of the variance" ; "three factors explained 95% of the performance variance" ; "agents typically use about 4× more tokens than chat interactions" ; "multi-agent systems use about 15× more tokens than chats"（80% 这个数只针对 BrowseComp） | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06 | primary | H |
| 3 | 反向证据（部分支持信念 2）：换更强的模型比把 token 翻倍更有效。 | "upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7" | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06 | primary | H |
| 4 | 子 agent 的产出质量取决于任务边界写得多清楚，与人设无关；没有边界时子 agent 会重复劳动、留空白，数量也会失控。 | "Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information." ; "Early agents made errors like spawning 50 subagents for simple queries" | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06 | primary | H |
| 5 | STORM 自己的消融里，perspective 对提纲质量的贡献很小，而且在 GPT-4 上比在 GPT-3.5 上更小（只看 soft recall）。消融本身没有做显著性检验。真正起作用的是有检索支撑的多轮提问（conversation）。 | Table 3，Heading Soft Recall / Entity Recall：GPT-3.5 下 STORM 86.26/40.52，w/o Perspective 84.49/40.12，w/o Conversation 77.97/31.98；GPT-4 下 STORM 92.73†/45.91，w/o Perspective 92.39/42.70，w/o Conversation 88.75/39.30；GPT-4 RAG-expand 91.36/43.53。† 只标在"STORM vs 最佳 baseline"上，GPT-4 的 entity recall 45.91 没有 †。 | https://arxiv.org/pdf/2402.14207 | 2024-02（NAACL 2024） | primary | H |
| 6 | 反向证据（支持多视角）：perspective 的可测增益在"找到的独立来源"这一项，接近翻倍。这是"覆盖面"论点能拿到的最好数据。 | Table 5，平均独立参考数 \|R\|：STORM 99.83，w/o Perspective 54.36，w/o Conversation 39.56 | https://arxiv.org/pdf/2402.14207 | 2024-02 | primary | H |
| 7 | brief 引用的"+10% coverage"在人评中不显著，样本只有 20 对，标注者间一致性低。可核验性没有提升，信息越多反而越容易出现无法核验的推断。 | Table 6：Coverage oRAG 3.58 vs STORM 4.00，p=0.084；Organization 3.25 vs 4.00，p=0.005；Verifiability 3.85 vs 3.80，p=0.843；"20 pairs"；Krippendorff's Alpha 0.221–0.388。"editors assign lower Verifiability scores to articles from our approach in over 50% of the cases" ; "low Verifiability scores stem from red herring fallacy or over-speculation issues" | https://arxiv.org/pdf/2402.14207 | 2024-02 | primary | H |
| 8 | STORM 的 perspective 是单一管线里的提问条件，提问这一步用的是较弱的 gpt-3.5-turbo。所以"STORM 以并行子 agent 运行、每个 seat 用最强模型"这种形态并没有被测过。 | "We use the chat model gpt-3.5-turbo for question asking and use gpt-3.5-turbo-instruct for other parts of STORM. We also experiment with using gpt-4 for drafting and refining the outline" | https://arxiv.org/pdf/2402.14207 | 2024-02 | primary | H |
| 9 | 在 system prompt 里加人设不提升表现；自动挑出"最佳人设"的效果不比随机好。按"职业身份"选 seat 本身不产生价值。（事实问答，模型为 2023–24 年代，可能过时） | "adding personas in system prompts does not improve model performance" ; "compared to the control setting where no persona is added" ; "automatically identifying the best persona is challenging" ; "predictions often performing no better than random selection" ; "4 popular families of LLMs and 2,410 factual questions" | https://arxiv.org/abs/2311.10054v2 | 2023-11（v2 2024-10，EMNLP Findings 2024） | primary | H |
| 10 | 多智能体辩论的增益大多来自多数投票；辩论本身不提高期望正确率（martingale）。这对 deep 档的交叉质询轮不利。（7 个 NLP 基准，有标准答案的任务） | snippet: "Majority Voting alone accounts for most of the performance gains typically attributed to MAD"；摘要第 6 句（抓取摘要转述）：debate 形成关于信念的 martingale，"debate alone does not improve expected correctness" | https://arxiv.org/abs/2508.17536 | 2025-08（v2 2025-10，NeurIPS 2025） | primary | H |
| 11 | 基座模型越强，多 agent 相对单 agent 的优势越小。用最强模型跑 5 个 seat，等于在优势最小的区间叠加成本。 | "We find that the benefits of MAS over SAS diminish as LLM capabilities improve" ; "the design and deployment of MAS incur higher complexity and runtime cost compared to single-agent systems (SAS)." | https://arxiv.org/abs/2505.18286v1 | 2025-05 | primary | M |
| 12 | 把思考 token 预算拉平后，单 agent 在多跳推理上持平或胜过多 agent；不少报告出来的 MAS 增益其实来自没算进去的额外计算。（多跳 QA，不是开放式研究） | "SAS consistently match or outperform MAS on multi-hop reasoning tasks when reasoning tokens are held constant." ; MAS 增益 "confounded by increased test-time computation" | https://arxiv.org/abs/2604.02460v1 | 2026-04 | primary | M |
| 13 | 260 种配置的受控研究：单 agent 基线较强时，协调的回报递减甚至为负；工具密集型任务会带来多 agent 开销；没有集中核验的架构传播错误更多。这条既支持"保留 verifier"，也支持"少放 seat"。注意 v1 与 v3 的数字不同。 | v3 摘要："tool-heavy tasks appear to incur multi-agent overhead" ; "architectures without centralized verification tend to propagate errors more than those with centralized coordination"；相对单 agent 的表现从 +80.8% 到 -70.0%。v1 snippet："coordination yields diminishing or negative returns (beta=-0.408, p<0.001) once single-agent baselines exceed ~45%" | https://arxiv.org/abs/2512.08296 | 2025-12（v3 2026-04） | primary | M |
| 14 | 质量比多样性重要：只用最强的单一模型做集成，胜过混合多个模型。这对信念 2 是部分支持（如果要多个 seat，宁可都用强模型），对 casting.md 里"换模型族才能打破先验"的说法不利。（单答案集成，不是研究任务） | snippet: "Self-MoA achieves 6.6% improvement over MoA on the AlpacaEval 2.0 benchmark" ; "mixing different LLMs often lowers the average quality of the models" | https://arxiv.org/abs/2502.00674 | 2025-02（TMLR 2026） | primary | M |
| 15 | 开放式生成里，同一模型内部高度重复，不同模型之间也高度同质。"五个 seat 一个模型"给出的是相关样本，不是独立视角；换模型族也不能保证多样性。（论文没有测 persona 提示） | "intra-model repetition, where a single model consistently generates similar responses" ; "inter-model homogeneity, where different models produce strikingly similar outputs" | https://arxiv.org/abs/2510.22954 | 2025-10（v2 2026-10，NeurIPS 2025） | primary | H |
| 16 | 核验这一步有外部测量支撑：主流深度研究系统的引用准确率只有 40–80%，有大量无支撑陈述，在有争议的问题上明显一边倒。 | "with citation accuracy ranging from 40--80% across systems" ; "still exhibit large fractions of unsupported statements" ; "remain highly one-sided on debate queries" | https://arxiv.org/abs/2509.04499v1 | 2025-09（ICLR 2026） | primary | H |
| 17 | 跨行业类比（outsider）的近邻证据来自人类设计创意研究，而且对"远类比"不利：受控实验和大样本文本分析都发现，近源启发的创意质量更高。没有找到任何在 LLM 开放式研究上测过类比 seat 的研究。 | snippet（搜索工具转述，不是原文）：84 名机械工程研究生的实验中，near-field 类比得到的创意 "higher novelty and quality than far-field ones"；平台文本分析：较近的启发源比远的更有帮助，且距离与创造力的反向关系 "robust across design problems" | https://re.public.polimi.it/handle/11311/1121826 ; https://link.springer.com/10.1007/978-3-319-91134-2_12 | 年份未核（Springer 章节 ISBN 显示约 2018）；snippet | primary（只看到 snippet） | L |
| 18 | 与第 17 行冲突：较早的研究发现远类比能提高新颖性，但质量波动更大、产出概念更少。所以 outsider 最多能被当成新颖性发生器，不能当覆盖面工具。 | snippet（转述）：一项高年级学生实验发现 "positive effects of far-field examples on novelty"；另一早期研究报告远类比新颖性更高，但 "more variable quality and fewer concepts" | https://www.lrdc.pitt.edu/Schunn/papers/Chanetal2011.pdf ; https://asiachapter.designsociety.org/download-publication/39849/Investigating+effects+of+stimuli+on+ideation+outcomes | 2011 及更早；snippet | primary（只看到 snippet） | L |

## My edge
- 我把"覆盖面"和"决策质量"拆开看。STORM 的 perspective 能测到的增益在"找到更多独立来源"（+84%，第 6 行），提纲质量在 GPT-4 上只多 0.34 个点（第 5 行），人评的覆盖面不显著（第 7 行）。多出来的来源同时带来更多无法核验的推断（第 7 行）。所以多视角买到的是更多原料，原料能不能变成可靠结论，要看核验。
- 我回到 STORM 的原表去读。"STORM 以并行子 agent 运行"其实是外推：原文的 perspective 是一个管线里的提问提示，跑在 gpt-3.5-turbo 上（第 8 行）。被引用最多的 "+25%/+10%" 是完整 STORM 对 oRAG 的比较，不是 perspective 的消融。
- Anthropic 自己的架构直接反驳信念 2：主控用 Opus，干活的子 agent 用 Sonnet（第 1 行）。"模型比 token 更重要"（第 3 行）说的是要把强模型放在综合和判断的环节，不是说要乘以 seat 数。
- brief 里的首跑记录：seat 消耗约 412K/482K token（85%），verifier 只用 70K（15%）。可是两条改变了结论含义的修正（被截断后意思反转的维护者引语；"atomic writes" 实为 "MCP server"）都来自 verifier。这是本 skill 唯一一次内部测量，测出来的价值落在最便宜的那一环。
- 本 skill 现在不测量自己：没有记录每个 seat 的边际贡献，也没有单 agent 基线。我的改动建议核心是让每次运行都产出这份数据，而不是凭直觉在 3、5、6 个 seat 之间争论。

## What the other seats will get wrong
- researcher seat 会把 STORM 的 "+25% organization / +10% coverage" 当作"多视角有效"的证据。这两个数是完整 STORM 对 oRAG 的比较，coverage 的 p=0.084、n=20、alpha 约 0.35。perspective 自己的消融在 GPT-4 上 soft recall 只多 0.34 个点，也没有显著性检验（第 5、7 行）。
- 引用 Anthropic 90.2% 的 seat 会拿它支持"多视角 seat"和"每个 seat 用最强模型"。按我对原文的理解，它的子 agent 是对任务做拆分（不同子问题），不是对同一问题换视角；用的是 Sonnet；80% 的方差由 token 量解释；对比也不是等 token 的（第 1、2 行）。
- outsider 或 historian 类 seat 会引用创造力文献（远类比、跨界启发）来给 outsider seat 背书。受控设计研究对质量的结论偏向近源（第 17 行），远源最多提高新颖性（第 18 行），而且没有一项研究是在 LLM 研究任务上测的。
- 会有 seat 把首跑"4 个 crux、没有一致意见"读成"多样性起作用了"。同一个模型被分配了对立角色（比如 skeptic 被要求反对），本来就会制造分歧（第 15 行）。分歧只有在两边由不同来源支撑时才算数。

## What would change my mind
- 一个开放式研究任务上的正面对比：在等 token 预算下比较 N 个 seat 与"单 agent + 发现的提纲"，用"经核验的独有 claim 数"或"结论是否改变"来衡量，且多 seat 胜出 20% 以上。
- 本 skill 自己 3 次以上运行的数据：outsider seat 贡献的已核验 claim 至少一次进入了 bottom line 并改变了它。或者反过来，删掉 seat 4、5 后结论在多次运行中都改变了。
- 同一 verifier 下 Sonnet 级与 Opus 级 seat 的 A/B：如果 Opus seat 的降级率明显更低，或者独有已核验 claim 明显更多，信念 2 对 seat 层也成立。

## Positions I hold without evidence
- 首跑真正影响决策的内容来自 verifier 的修正和 1–2 个 crux，砍到 3 个 seat 大概率不会改变用户的行动。我没有数据支持这一点，因为本 skill 没有记录"删掉某 seat 后结论是否变化"。
- outsider seat 在最强模型上更危险：它产出的是流畅、生动、难以核验的类比。合成者容易被文笔打动，verifier 的规则又只碰有来源的 claim，类比因此会漏网。
- 同模型 seat 之间的不少分歧是角色指令制造的，不是来自证据。
- 对我立场不利的一点：业主似乎用的是订阅额度，token 的成本是额度和速率，不是现金。seat 又是并行的，砍 seat 节省的墙钟时间不多（首跑约 20 分钟由最慢的 seat 决定）。所以"15 倍 token"在这个用户身上的真实代价比通常算法要低。对从零进入一个领域的人来说，多出来的近一倍来源（第 6 行）可能值这个价。
- verifier 应该用最强模型：发现"截断引语导致含义反转"需要仔细阅读。我没有找到这方面的 A/B。

## Deliberately not examined
- ChatEval 的"3–4 个角色时效果最好"和 SPP 的"只给人设名称与详细档案效果相同"：brief 通过 zrabin/panel-skill 的 README 转引，我没有核对原文。casting.md 的 "peak around three to four" 依赖前者。
- Co-STORM 的评测，以及 Anthropic 文中按问题复杂度调整子 agent 数量的具体规则（没有拿到原文措辞）。
- Vals AI 和 Cohere 的"团队 vs 单人、等预算"数据：只在一篇标注为 100% AI 生成的二手文章里看到（yage.ai，2026-10-21），而且是编程任务，属于范围外，没有使用。
- SAFE（Wei et al. 2024）等自动事实核查与人工一致率的研究。
- 在 LLM 开放式研究上测"跨领域类比提示"的研究：搜了一次，没找到，所以第 17、18 行都是人类设计研究的近邻证据。
- Reddit 或从业者对多 agent 研究工具的使用反馈。
- Claude Code 子 agent 的默认模型（inherit 还是配置值）：`~/.claude/agents/family-*.md` 没有 model 字段，我是从这一点推断"seat 会继承主模型"，没有查官方文档。

## Proposed changes to the skill
| file | keep/change/add/remove | what | evidence row # or "judgment" |
|---|---|---|---|
| SKILL.md | change | 第 10 行 "Practically this is STORM ... run as parallel subagents" 和 "you will not have missed the obvious"：改成如实陈述。STORM 的 perspective 是单管线内的提问条件（gpt-3.5）；它的可测增益是"独立来源接近翻倍"和"组织性"（p=0.005）；人评覆盖面不显著（p=0.084，n=20）；并行 seat 这种形态没有被测过。 | 5, 6, 7, 8 |
| SKILL.md | keep | 规则 2 "Seats are evidence standards, not voices"：这是全套设计里证据最硬的一条。把它升级为 casting 的唯一硬约束：每个 seat 必须有不重叠的检索领地（站点、文献类型、数据源）。 | 6, 9, 15 |
| SKILL.md | change | 规则 6 "Unanimity is a casting failure"：改为"同模型 seat 的一致和分歧都不能直接当信号；只有两边各有不同来源支撑的分歧才算 crux，由角色指令产生的分歧不算"。 | 15 + judgment |
| SKILL.md | change | Depth tiers：standard 默认改为 3 个检索 seat 加 1 个 verifier（claims 25–30），4–6 个 seat 移到 deep。理由：等 token 时单 agent 不输于多 agent；多 agent 的增益随模型变强而递减；首跑 85% 的 token 花在 seat 上，而改变结论的修正来自 verifier。 | 2, 11, 12, 13；brief 首跑记录 |
| SKILL.md | change | quick 档：从"orchestrator 内联扮演 3 个 seat、不做核验"改为"1 个 agent 按发现的提纲检索，加 1 个 verifier 核 8–10 条"。内联扮演 3 个 persona 就是一个模型戴三顶帽子，同时还丢掉了唯一有测量支撑的环节。 | 9, 15, 16 |
| SKILL.md | change | "Do not pass a model override"：改为显式分层。orchestrator（综合）和 verifier 用最强模型，检索 seat 用中档（Sonnet 级），cost footer 记录每个 seat 用的模型。在 A/B 结果出来之前，不要默认 5 个 seat 都用最强模型。 | 1, 3, 14 + judgment |
| SKILL.md | add | `--baseline` 开关：同一问题再跑一遍"单 agent + 发现的提纲 + 同一 verifier"，比较"经核验的独有 claim 数"和"bottom line 是否改变"。积累 3 次运行后再定默认 seat 数。 | judgment（开放式研究上没有正面对比） |
| casting.md | change | Move 2 outsider：从 "Mandatory" 改为可选，standard 档默认关闭。启用时，类比必须同时引用 (a) 源行业那条规则的文献，(b) 目标领域缺这条规则的证据，否则只能写进 "Positions I hold without evidence"。 | 17, 18 + judgment |
| casting.md | change | Move 1 Discover：保留，但产出从"topic-native 人设"改为"检索领地"（例如 issue tracker、维护者的 release notes、某个会议的论文集）。要发现的是去哪里搜，不是谁在说话。 | 6, 9 |
| casting.md | change | "Five is the default" 改为 "Three is the default; add a seat only if its 'trusts' column names a source type no other seat touches"。 | 11, 12, 13；ChatEval 3–4 角色（brief 转引，未核） |
| casting.md | remove | 交叉质询轮（deep 档）：删掉，换成"verifier 对每个 crux 的两侧各做一次反证搜索"。辩论的增益主要来自投票，辩论本身不提高期望正确率。 | 10 |
| casting.md | change | Second-model seat 里的 "this is the only cheap way to break that"：删掉这句断言。不同模型族在开放式生成上同样高度同质，混入较弱的模型还会拉低平均质量。功能保留，价值用"独有已核验 claim"来衡量。 | 14, 15 |
| seat-protocol.md | change | 卡片细节：把 "Who you are" 人设压到一行，篇幅留给"检索领地、明确不搜什么、与其他 seat 的边界"。 | 4, 9 |
| seat-protocol.md | add | claims 表加一列 "novel?"：seat 自评这条是否预期别的 seat 也会找到。合成时可以据此估算每个 seat 的边际贡献。 | judgment |
| verifier-protocol.md | change | claim 预算从 15 提到 25–30（standard 档）。反证搜索从"前 1/3"改为覆盖每个 crux 的两侧。依据是首跑 15 条里 5 条 PARTIAL、其中 2 条含义反转，以及行业引用准确率 40–80%。 | 16, 7；brief 首跑记录 |
| verifier-protocol.md | add | 输出中增加按 seat 汇总的降级率（PARTIAL 和 MISQUOTED 的占比），作为跨运行判断"这类 seat 值不值得保留"的数据。 | 13 + judgment |
| report-template.md | add | 新增 "Decision delta" 小节：bottom line 的每条结论列出由哪些 seat 支撑，删掉某个 seat 后结论是否会变。cost footer 增加"每个 seat 的独有已核验 claim 数"。 | judgment |
| report-template.md | keep | "A MISQUOTED or single-origin CIRCULAR claim cannot appear in it"：保留。这是唯一有测量支撑的价值来源在报告里的落地点。 | 16；brief 首跑记录 |

## Sources
1. https://www.anthropic.com/engineering/multi-agent-research-system — Anthropic 工程博文：Opus 主控 + Sonnet 子 agent 比单 agent 高 90.2%；token 解释 80% 方差；15×/4× token；换模型胜过 token 翻倍；任务描述与重复劳动。2025-06
2. https://arxiv.org/pdf/2402.14207 — STORM (Shao et al., NAACL 2024)：Table 3 perspective 消融、Table 5 独立来源数、Table 6 人评 p 值与 IAA、verifiability/red herring、gpt-3.5-turbo 用于提问。2024-02
3. https://arxiv.org/abs/2311.10054v2 — Zheng et al.，system prompt 中的 persona 不提升表现（EMNLP Findings 2024）。2023-11 / v2 2024-10
4. https://arxiv.org/abs/2508.17536 — Choi, Zhu, Li，Debate or Vote（NeurIPS 2025）：多数投票解释了大部分 MAD 增益，辩论是 martingale。2025-08
5. https://arxiv.org/abs/2505.18286v1 — Gao et al.，Single-agent or Multi-agent Systems? Why Not Both：MAS 相对 SAS 的增益随模型能力提升而递减。2025-05
6. https://arxiv.org/abs/2604.02460v1 — Tran & Kiela，等思考 token 预算下单 agent 持平或胜过多 agent（多跳推理）。2026-04
7. https://arxiv.org/abs/2512.08296 — Kim et al.，Towards a Science of Scaling Agent Systems：协调回报随单 agent 基线变强而递减；缺乏集中核验时错误传播更多。v1 2025-12，v3 2026-04
8. https://arxiv.org/abs/2502.00674 — Li et al.，Rethinking Mixture-of-Agents（Self-MoA）：单一最强模型集成胜过混合多模型。2025-02
9. https://arxiv.org/abs/2510.22954 — Jiang et al.，Artificial Hivemind：模型内重复与模型间同质（NeurIPS 2025）。2025-10 / v2 2026-10
10. https://arxiv.org/abs/2509.04499v1 — Venkit et al.，DeepTRACE：深度研究系统引用准确率 40–80%（ICLR 2026）。2025-09
11. https://re.public.polimi.it/handle/11311/1121826 — 近类比与远类比的受控实验（84 名机械工程研究生），只看到 snippet。年份未核
12. https://link.springer.com/10.1007/978-3-319-91134-2_12 — 启发源概念距离与创造力的文本分析，只看到 snippet（抓取时被登录重定向）。约 2018
13. https://www.lrdc.pitt.edu/Schunn/papers/Chanetal2011.pdf — Chan et al. 2011，远类比例子对新颖性有正面作用，只看到 snippet。2011
14. https://asiachapter.designsociety.org/download-publication/39849/Investigating+effects+of+stimuli+on+ideation+outcomes — 远类比新颖性更高但质量波动更大，只看到 snippet。年份未核
15. https://yage.ai/share/multi-agent-what-it-buys-en-20261021.html — 二手文章（页面自标 100% AI 生成），转述 Vals AI 和 Cohere 的团队 vs 单人数据。看过但没有进 claims 表。2026-10-21
16. /home/xhyumiracle/projects/xhyu/family/family-skill-design/brief.md — 首跑记录（482K token，verifier 15 条中 5 条 PARTIAL）。2026-10-27

## Budget used
searches: 10 / 10 · fetches: 12（其中 2 次失败：Chanetal PDF 404，Springer 登录重定向）；STORM PDF 因 WebFetch 无法解析，改用本地 Read 读取页面图像（不计入搜索预算）
