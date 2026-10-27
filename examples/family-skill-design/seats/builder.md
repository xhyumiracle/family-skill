# Seat: builder（交付过生产级 deep-research 系统、写过"到底是什么推动了 eval"复盘的工程师）

## Core position
六个设计选项里，有生产级测量支撑的只有三类：预算（BrowseComp 上 token 用量单独解释 80% 方差）、模型代际（升级到 Sonnet 4 的收益大于给 Sonnet 3.7 翻倍 token）、"独立并行 + 中心化校验/聚合"（独立 agent 错误放大 17.2x，中心化 4.4x；并行采样后做选择 +15-25%；生产 DR 系统引用准确率只有 40-80%）。透视生成方式、卡片细节、席位数、辩论轮在生产中没有同预算 A/B，属于"感觉有原则"。多 agent 溢价随单 agent 变强而收缩（2025 内部 eval +90.2%，2026 BrowseComp 约 +2.8 点）。"每席最强模型"没有公开证据，Anthropic 自己的生产配置和文档都是强 lead 配 Sonnet 工人。最大缺口：skill 没有自己的 eval，六个选项都无法被它自己证伪。置信度：中。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) |
|---|---|---|---|---|---|---|
| 1 | Anthropic 的 90.2% 是"多 agent vs 单 agent"，配置是 Opus 4 lead + Sonnet 4 工人，在内部 eval 上测得；它不是"每席最强模型"的证据，反而是强 lead + 次一档工人的证据。题集未公开。 | "a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents" ... "outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval" | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H |
| 2 | 预算是主变量：BrowseComp 上三因素解释 95% 方差，token 用量单独解释 80%；多 agent 约为 chat 的 15 倍 token，单 agent 约 4 倍。 | "three factors explained 95% of the performance variance in the BrowseComp evaluation"; "token usage by itself explains 80% of the variance"; "agents typically use about 4× more tokens than chat interactions"; "multi-agent systems use about 15× more tokens than chats" | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H |
| 3 | 模型代际升级的收益大于翻倍 token。注意这是跨代（3.7 到 4），不是同代 Opus vs Sonnet 的工人对比。 | "upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7" | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H |
| 4 | 生产中破的地方是任务边界和停止条件，不是人设：工人需要目标、输出格式、工具与来源指引、清晰边界；否则重复劳动、留空白；早期出现简单问题开 50 个 subagent。努力分级是提示里的经验规则，不是测出的最优值。定性经验，无 ablation 数字。 | "Each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries."; "Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information."; "Early agents made errors like spawning 50 subagents for simple queries"; "direct comparisons might need 2-4 subagents with 10-15 calls each"; "These changes cut research time by up to 90% for complex queries." | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | M |
| 5 | 早期开发阶段效应量很大，约 20 道题的 eval 就能看出差异；Anthropic 的 judge 维度里有"引用准确"和"来源质量"两项，且早期 agent 偏爱 SEO 内容农场。 | "We started with a set of about 20 queries representing real usage patterns."; "A prompt tweak might boost success rates from 30% to 80%."; "citation accuracy (do the cited sources match the claims?)"; "our early agents consistently chose SEO-optimized content farms over authoritative but less highly-ranked sources" | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H |
| 6 | 多 agent 适用面：广度优先、可并行、任务价值足以覆盖成本；需要共享上下文或强依赖的任务不适合。 | "multi-agent research systems excel especially for breadth-first queries"; poor fit when tasks "require all agents to share the same context or involve many dependencies between agents"; "multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance" | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H |
| 7 | 到 2026 年前沿模型上，多 agent 相对单 agent 的溢价在 BrowseComp 上只剩约 2.8 个百分点：单 agent（50k 触发压缩、总计最多 10M token）84.0%，多 agent harness 86.8%；系统卡 2026-03 修订为 83.73% / 86.57%。单 agent 的 84.0% 和修订值只来自搜索摘要。 | 新闻页脚注片段："context compaction triggered at 50k tokens up to 10M total tokens"；多 agent 86.8%（fetch 转述的脚注）。系统卡（snippet）："Updated highest single-agent BrowseComp score (83.97% -> 83.73%)"; "Updated multi-agent BrowseComp (86.81% -> 86.57%)" | https://www.anthropic.com/news/claude-opus-4-6 ; https://www-cdn.anthropic.com/6a5fa276ac68b9aeb0c8b6af5fa36326e0e166dd.pdf | 2026-02-05（修订 2026-03） | primary（部分为 snippet） | M |
| 8 | 受控对比（Google Research/DeepMind/MIT）：没有中心化校验的独立并行 agent 把错误放大 17.2 倍，中心化 4.4 倍；单 agent 基线已经强时，协调的收益递减；相对单 agent 的变化从 +80.8%（可分解任务）到 -70.0%（序列规划）。数字随版本漂移：v1 为 180 配置、4 基准，v3 为 260 配置、6 基准，R² 0.373。 | 博客原文："We found that independent multi-agent systems (agents working in parallel without talking) amplified errors by 17.2x." 中心化 "contained this amplification to just 4.4x"；"This model correctly identifies the optimal coordination strategy for 87% of unseen task configurations." v3 摘要的数字（+80.8%、-70.0%、260、R² 0.373、强基线下收益递减）来自 fetch 摘要，不是原文引用 | https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/ ; https://arxiv.org/abs/2512.08296 | 博客 2026-01-28；arXiv v1 2025-12-09，v3 2026-04-08 | primary | H（17.2x/4.4x），M（其余） |
| 9 | 同一论文中，BrowseComp-Plus（网页检索）上去中心化 +9.2%，中心化只有 +0.2%：编排式多 agent 在网页检索类任务上几乎没有收益。 | snippet："Decentralized coordination excels on dynamic web navigation (+9.2% vs. +0.2%)"（未在页面上核实，可能为 v1 数字） | https://arxiv.org/abs/2512.08296v1 | 2025-12 | primary（snippet） | L |
| 10 | 独立并行再加一步选择是有测量的配方：Deep Research 每题 64 次并行采样，投票或 best-of-N 比单次高 15-25%，原因是"验证比找到容易"；收益集中在前 4-8 份（Figure 4 目测：best-of-N 1 份约 0.52，4 份约 0.67，8 份约 0.71，64 份约 0.78；多数投票 4 份约 0.58，64 份约 0.67）。带浏览的模型校准差（Deep Research 校准误差 91%）。注意这是同一 prompt 的重复采样、短答案任务。 | "As shown in Figure 4, the three methods improve performance by 15% to 25% compared to just using a single attempt."; "BrowseComp is a benchmark that is easier to verify than to find the answer"; Table 3: Deep Research accuracy 51.5, calibration error 91 | https://arxiv.org/pdf/2504.12516 | 2025-04 | primary | H（引文），M（曲线读数） |
| 11 | 生产级 DR 系统即使引用很全，仍有大量无支撑陈述，引用准确率 40-80%，在争议问题上高度一边倒。独立核查一遍有必要；多视角（含怀疑者）针对的正是一边倒。 | deep research configurations "remain highly one-sided on debate queries and still exhibit large fractions of unsupported statements, with citation accuracy ranging from 40--80% across systems" | https://arxiv.org/abs/2509.04499v1 | 2025-09-02（ICLR 2026） | primary | H |
| 12 | 多 agent 辩论的收益大多来自投票（集成），而不是辩论本身；理论上辩论不提高期望正确率。在 7 个封闭答案 NLP 基准上测得，迁移到开放式研究属推断。 | "we find that Majority Voting alone accounts for most of the performance gains typically attributed to MAD"; "across seven NLP benchmarks"; "We prove that it induces a martingale over agents' belief trajectories" | https://arxiv.org/abs/2508.17536v1 | 2025-08-24（v2 2025-10-23，NeurIPS 2025） | primary | H（发现），M（迁移） |
| 13 | 1600+ 条 MAS 轨迹中，排前面的失败模式是重复步骤、不知道何时停、不遵守任务规格、验证缺失或错误；补一个高层"任务目标"验证 +15.6%，改角色规格 +9.4%；只靠末端低层检查的验证器不够。框架以编程类为主。 | FM-1.3 step repetition 15.7%, FM-1.5 unaware of termination conditions 12.4%, FM-1.1 disobey task specification 11.8%, FM-3.3 incorrect verification 9.10%, FM-3.2 no or incomplete verification 8.20%; ChatDev role-spec +9.4%, task-objective verification +15.6%; "Current verifier implementations are often insufficient; sole reliance on final-stage, low-level checks is inadequate." | https://arxiv.org/html/2503.13657v3 | 2025-10-26（v3） | primary | M |
| 14 | 并行"写"会散，并行"查"可以：LangChain 先让子 agent 并行写章节，结果报告割裂，改为多 agent 只做研究、写作单独一步。同一 repo 的成本表显示：研究模型从 gpt-4.1 换成 claude-sonnet-4，RACE 只从 0.4309 到 0.4401，成本从 $45.98 到 $187.09（约 4 倍）；换 GPT-5 到 0.4943，用 204.6M token（约 3.5 倍）。 | "the reports were disjoint because the section-writing agents were not well coordinated"; "We resolved this by using multi-agent for only the research task itself, performing writing after all research was done."; table: Defaults 0.4309 / $45.98 / 58,015,332 tokens; Claude Sonnet 4 0.4401 / $187.09 / 138,917,050; GPT-5 0.4943 / 204,640,896 | https://www.langchain.com/blog/open-deep-research ; https://github.com/langchain-ai/open_deep_research | 2025-07-16；表约 2025-08-07 | primary（厂商工程） | M |
| 15 | Claude Code 官方给多实例协作的成本建议是队员用 Sonnet、队伍要小、spawn prompt 要短；agent teams 约为普通会话 7 倍 token；session 切 Opus 时继承模型的 subagent 也跟着变 Opus。这是厂商建议，不是 eval。 | "Use Sonnet for teammates. It balances capability and cost for coordination tasks."; "Keep spawn prompts focused. Teammates load CLAUDE.md, MCP servers, and skills automatically, but everything in the spawn prompt adds to their context from the start."; "Agent teams use approximately 7x more tokens than standard sessions when teammates run in plan mode"; "A switch to Opus also applies to the subagents that inherit your session's model" | https://code.claude.com/docs/en/costs | as-of 2026-10-27 | primary（厂商文档） | H |
| 16 | 当前 Claude Code 默认允许 subagent 嵌套派生到三层，并发上限 20。skill 的 `general-purpose` 回退只靠 prompt 里一句"不许派生"，不是结构性约束。 | "By default, a subagent can spawn subagents of its own, up to three layers below the main conversation."; "when 20 subagents are running in a session, spawning another with the Agent tool fails with `Concurrent subagent limit reached`" | https://code.claude.com/docs/en/sub-agents.md | as-of 2026-10-27 | primary（厂商文档） | H |

## My edge
- **90.2% 一直被拿来当"多 agent + 强模型"的证据，其实两头都不对。** 那个配置的工人是 Sonnet（#1）。在 Anthropic 自己的分析里，主要解释量是 token（#2）。到 2026 年，单 agent 有了压缩、最多可用 10M token，差距只剩约 2.8 点（#7）。多 agent 的大部分溢价，买的是"多开几个上下文窗口的 token"，不是"多几个视角"。
- **family 的设计让每个席位研究同一个问题，Anthropic 列为失败模式的"重复劳动"在这里是有意为之。** 这和 best-of-N 是同一种机制（#10）：独立重复本身不值钱，值钱的是后面的选择和验证。所以 family 真正有证据撑腰的部件是 verifier 和合成步（#8、#10、#11、#13），不是 casting。
- **搜索预算才是质量旋钮，席位数只是花预算的方式。** skill 的分级表把每席搜索数固定为 10，同时围绕席位数做文章。按 #2，同样总预算下"4 席 × 15 次"和"6 席 × 10 次"哪个好，是一个可以测的问题；它们不是两个不同的哲学。
- **skill 一次运行都没测过自己。** Anthropic 从约 20 道题起步，因为早期改动的效应量有 30% 到 80% 那么大（#5）。没有 eval，所有者的两个信念（outsider 席、每席最强模型）都没法证伪，只能靠争论。首次运行的数据（brief：482K token、5/15 条被降级、其中 2 条意思反了）就是一份现成的 eval 种子。
- **生产里先坏的是停止条件和边界，不是人设。** 最常见的失败是重复步骤 15.7%、不知何时停 12.4%（#13），以及开 50 个 subagent、在网上没完没了地搜（#4）。family 的搜索预算和"不许雇人"规则恰好管住了这两个，应当保留，并且在回退路径上也要做成结构性约束（#16）。

## What the other seats will get wrong
- 研究员席会引用 STORM、ChatEval、多 agent 辩论在 2023-2024 年模型和封闭答案基准上的数字，当作席位数和辩论轮的依据。#12 显示辩论收益大多是投票；#8 显示单 agent 基线强时协调收益递减。这些老数字高估了今天的溢价。
- 怀疑者席会拿人设文献（Zheng 2023、SPP）来攻击 outsider 席。family 的席位卡本质上是"去哪里搜、信什么证据"的路由指令，接近 Anthropic 所说的 "guidance on the tools and sources to use"（#4），不是人设。人设的零结果不能直接套过来。不过反方向同样没有证据（见下）。
- 有人会把 90.2% 当作"每席都用最强模型值得"的依据。它测的是 Sonnet 工人（#1）；官方文档的建议也是队员用 Sonnet（#15）。
- 实践者或历史学家席可能把 verifier 当成锦上添花。在六个选项里，它是跨来源证据最一致的一个（#10、#11、#13，加上首次运行的 5/15 降级）。

## What would change my mind
- 一个公开的同预算 A/B：在开放式研究 eval 上，"透视条件化的席位"在覆盖率或准确率上明显胜过"N 个同 prompt 的席位"（2025 年以后的模型）。如果有，casting 就从"感觉有原则"升级为有证据。
- Anthropic 或其他厂商公布研究类任务的"Opus 工人 vs Sonnet 工人"消融，并且差距大于成本比。如果有，我会收回"席位默认降一档"。
- family 自己的 10-20 题 eval 显示：席位间来源重叠低于约 20%，且每多一席，经 verifier 确认的独有 claim 数大致线性增加。如果是这样，席位数就值它的钱。

## Positions I hold without evidence
- 同一问题上视角席位的价值，主要来自检索的去相关（不同的搜索词、不同的站点），也就是让 best-of-N 起作用的那种样本差异。人设的口吻贡献接近零。
- outsider 席方差很大：偶尔挖到最好的盲点，多数时候是离题的 token 消耗。我没有找到任何生产 eval 支持或否定"强制 outsider 席"。
- 按"每 token 移除的错误"算，verifier 比任何追加的席位都便宜。首次运行中 verifier 约 70K token，抓到 2 条意思被颠倒的引用，而单个席位要 70-107K token。
- 如果问题只有一个核心争点，一个强单 agent 用同样的总搜索预算，加上同一个 verifier，能拿到大部分结果。crew 真正值钱的场合是多社群、有争议的话题。
- deep 档的交叉质询轮，如果写成"必须带新证据，否则让步"，更像有针对性的再检索，而不是辩论，#12 不完全适用。是否值得付钱，仍需 eval。

## Deliberately not examined
- STORM / Co-STORM 消融、人设文献（Zheng、SPP、ChatEval）留给研究员席；我的卡写明这是我的盲区。
- 前 LLM 时代的方法（Delphi、红队、ACH 竞争性假设分析、情报界多源核查），完全没看。
- OpenAI / Perplexity / Google deep research 的内部多 agent 消融：在预算内没有找到公开数字。
- Opus 5 系统卡的多 agent BrowseComp（10-agent team 93.6% 只见于二手聚合站 benchmarklist.com，系统卡 PDF 超过 10MB 无法抓取）；单 agent 对照数字没拿到。Opus 4.6 系统卡 PDF 同样无法抓取，修订值只来自 snippet。
- 2026-10 当前的按 token 计价，所以没有给"Sonnet 席位省多少钱"的具体数字。
- 首次运行的目录在磁盘上没找到（无法列目录），所以没测席位间的来源重叠。
- Reddit 和从业者论坛，没有查。

## Proposed changes to the skill
| file | keep/change/add/remove | what | evidence row # or "judgment" |
|---|---|---|---|
| SKILL.md | add | 新增一节"Eval"：把 10-20 个历史问题（从首次 Obsidian 运行开始）各配一份金标准 claim 列表，存在 `family/_eval/`。之后任何改动（档位、席位数、模型、casting 步骤）都先在这套题上做 A/B，记录 token、墙钟时间、verifier 确认的独有 claim 数和降级率。 | #5, #1 |
| report-template.md | change | Cost 一节加四个实测量：每席 token、每席不同 URL 数、席位间 URL 重叠率、每席"经核实且只有它有"的 claim 数。这是判断第 N+1 个席位值不值的唯一生产信号。 | #4, #8；judgment |
| SKILL.md（Depth tiers） | change | 写明"每席搜索数是主要质量旋钮，席位数只是花预算的方式"。standard 档给两个同预算变体（4 × 15 与 6 × 10），由 eval 决定默认值；扩容时先加每席搜索预算，再加席位。 | #2, #7 |
| SKILL.md（Keeping the bill honest，"Do not pass a model override"） | change | 默认席位用 Sonnet 档（在 `family-member` agent 的 frontmatter 写 `model: sonnet`），orchestrator 的 casting 和合成留在最强模型。"每席最强"改为可选 flag `--strong-seats`，并作为 eval 的一个实验臂。注意：#3 说明代际差距大于预算，所以不能用上一代模型。 | #1, #15, #14；judgment（没有同代工人消融） |
| verifier-protocol.md | keep | 保留独立 verifier、逐条打开原文、只拿 `claims.md`。这是六个选项里证据最一致的一项。 | #10, #11, #13 |
| verifier-protocol.md | add | 在逐条核查之外加一步高层检查：拿到报告的 bottom line 草稿后，逐句对应到已确认的 claim 编号；对应不上的句子标出来。MAST 显示只做末端低层检查不够，任务目标级验证 +15.6%。 | #13 |
| SKILL.md（第 4 步 Synthesize） | change | 顺序改为：合成草稿，交给 verifier 做上一行的高层检查，再定稿。仍然只有一个 verifier agent，只是多一次调用，不新增 agent。 | #13；judgment |
| casting.md（Cross-examination round） | change | 把 deep 档的交叉质询从"辩论"改为"定向再检索"：每个争点上，席位只能带新的一手证据维持立场，否则让步；没有新证据的反驳不计入。或者直接删掉这一轮，把预算转给 verifier 的 claim 数。 | #12；judgment |
| casting.md（Headcount："Debate-style setups peak around three to four distinct roles; past six you are paying for repetition."） | change | 这句话来自 2023 年模型上的 ChatEval。补上更新、更直接的依据：并行采样的收益集中在前 4-8 份；单 agent 基线强时协调收益递减。同时注明这两条都是同质样本或封闭任务上的结果。 | #10, #8 |
| casting.md（Move 2，outsider 席 "Mandatory"） | change | 把"强制"改为"默认开启，eval 实验臂"：没有任何生产 eval 支持或否定它。eval 跑出结果前保留，但在 roster 里标为实验。 | judgment |
| seat-protocol.md（Seat card file） | keep | 保留 "Evidence you trust" 这一行，并把它视为卡片里最承重的一行。它对应 Anthropic 所说的 "guidance on the tools and sources"，也直接对付 SEO 内容农场问题。 | #4, #5 |
| seat-protocol.md（Seat card file） | add | 卡片加一行 "Stop when"（预算用完，或连续 2 次搜索没有新的一手来源），再加一行 "Leave to other seats"，按证据域划界，不按子问题划界，这样问题仍是同一个，但检索被去相关。 | #4, #13 |
| SKILL.md（Fallbacks，general-purpose） | change | 在当前 Claude Code 中，`general-purpose` 可以嵌套派生三层，回退时那句 "no permission to spawn" 只是 prompt。改为：`family-member` 不可解析时，先尝试在 `~/.claude/agents/` 安装它（不带 Agent 工具）；只有装不上才回退，并在 cost 一节里用 `/usage` 的 subagent 归因核对实际派生数。 | #16；judgment |
| SKILL.md（spawn prompt 保持两行、卡片落盘） | keep | 官方文档同样建议 spawn prompt 保持简短，因为 CLAUDE.md、MCP 和 skills 都会自动加载进每个队员的上下文。 | #15 |
| SKILL.md（第 4 步：单写手合成） | keep | 席位只做研究，由 orchestrator 一个人写报告，不让席位并行写章节。 | #14 |
| SKILL.md（Depth tiers） | add | 新增 `solo` 基线臂（只给 eval 用）：一个强 agent 拿全部席位的总搜索预算，加同一个 verifier。没有这个基线，crew 的溢价就无从测量。 | #7, #8, #10 |

## Sources
1. https://www.anthropic.com/engineering/multi-agent-research-system — Anthropic, "How we built our multi-agent research system"：90.2%、token 方差、15x、任务说明、评估方法；2025-06-13
2. https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/ — Google Research 博客：17.2x / 4.4x 错误放大、87% 架构预测；2026-01-28
3. https://arxiv.org/abs/2512.08296 — Kim et al., "Towards a Science of Scaling Agent Systems"：v1 2025-12-09，v3 2026-04-08（260 配置，6 基准）
4. https://arxiv.org/abs/2512.08296v1 — 同上 v1；BrowseComp-Plus 数字只来自 snippet；2025-12
5. https://www.anthropic.com/news/claude-opus-4-6 — Opus 4.6 发布页，BrowseComp 脚注（压缩、10M token、多 agent 86.8%）；2026-02-05
6. https://www-cdn.anthropic.com/6a5fa276ac68b9aeb0c8b6af5fa36326e0e166dd.pdf — Opus 4.6 系统卡（PDF 过大无法抓取，修订值来自搜索 snippet）；2026-02，修订 2026-03
7. https://benchmarklist.com/benchmarks/browsecomp_multi_agent/ — 二手聚合站：Opus 5 的 10-agent team 93.6%（未进入 claims 表）；采样于 2026-07-24
8. https://arxiv.org/pdf/2504.12516 — Wei et al.（OpenAI），BrowseComp：64 份采样聚合 +15-25%、Figure 4、校准误差；2025-04
9. https://arxiv.org/abs/2509.04499v1 — Venkit et al., DeepTRACE：DR 系统引用准确率 40-80%、一边倒；2025-09-02
10. https://arxiv.org/abs/2508.17536v1 — Choi, Zhu, Li, "Debate or Vote"：多数投票解释了 MAD 的大部分收益；2025-08-24
11. https://arxiv.org/html/2503.13657v3 — Cemri et al., MAST "Why Do Multi-Agent LLM Systems Fail?" v3：失败模式比例与干预结果；2025-10-26
12. https://www.langchain.com/blog/open-deep-research — LangChain Open Deep Research：并行写作割裂，改为单独写作；2025-07-16
13. https://github.com/langchain-ai/open_deep_research — 同项目 README 成本/RACE 表；约 2025-08-07
14. https://code.claude.com/docs/en/costs — Claude Code 成本文档：队员用 Sonnet、agent teams 约 7x token、spawn prompt 要短；as-of 2026-10-27
15. https://code.claude.com/docs/en/sub-agents.md — Claude Code subagents 文档：可嵌套三层、并发上限 20、model 字段；as-of 2026-10-27

## Budget used
searches: 10 / 10 · fetches: 18（其中 2 次因 PDF 超过 10MB 失败，1 次为重定向；BrowseComp PDF 由 fetch 存盘后用 Read 读取第 5-8 页）
