# Seat: researcher

## Core position
Co-STORM 的主持人结果不能直接搬到盲写的并行席位上。它的主持人在共享对话里工作，输入是"已检索、未被引用"的材料，输出是一个新问题（#3）。它的消融差距没有做显著性检验，打分是 LLM 评审在 1-5 分上给的（#1、#2）；第三方复跑里，Co-STORM 的信息多样性在 5 个骨干模型上全部低于 STORM（#5、#6）。能迁移的是这个机制，不是"运行中插手"这个时机：田野工作结束后、核查之前，加一轮缺口轮，问题从未用材料里出，只带问题，不带结论。运行中给席位发消息有代价，而且有数字：同伴或权威信号会把正确答案翻错（#10-#12）；它还会毁掉盲写的副产品，也就是免费的子集消融，而这正是区分 3/4/5 席、outsider 开或关时最便宜的 eval（#19）。信心中等。

## Estimates
- (a) 编排者是否运行中 steer：**运行中不发；田野后加一轮缺口轮：是**。编排者在运行中看不到席位读过但没引用的材料，它发的消息对席位来说是权威信号（#10、#11）；运行中 steer 还会破坏子集消融（#19）。缺口轮复用的是主持人"从未用信息出问题"的机制（#3），以及 Anthropic"两波之间追加"的做法（#8）。harness 支持续跑（#9）。信心中等，因为主持人效应本身没有过显著性检验，第三方复跑的结果也不稳（#2、#5、#6）。
- (b) eval 与区分指标：**主指标是盲席子集上的留一法边际贡献**，即某席独有且核查通过的 claim 数和独立一手来源数。一次 5 席运行可以免费得到 10 个三席子集和 5 个四席子集，outsider 关闭就是去掉它的那个四席子集。模型档位没法用子集法，要在同一批题上配对重跑，看 claim 级降级率。10-20 题只能检出约 0.6-0.7 个"每题配对差标准差"量级的效应（按 #17 的公式自算：n=15 时 δ≈0.72σ，n=20 时 δ≈0.63σ）。所以 rubric 总分不是好的主指标：它与人评的相关只有 0.31-0.58（#7），小样本下 CLT 误差棒又会偏窄（#18）。
- (c) 两轴核查与 20 条预算：**核查员是净收益；20 条预算保留，但要按席保底分层；第二轴在论文型 claim 上倾向是噪音**。round 1 的反证搜索对论文 claim 多数是"未找到独立复现"（#20），第二轴在这类 claim 上几乎总会给 SINGLE-ORIGIN。另外，预算按诊断性排序时，"每席独有核查通过 claim"有一部分是选择造成的。
- (d) 报告模板对十分钟读者是否承重：**不确定，倾向部分承重**。Bottom line、Cruxes、Next step 承重；Seat estimates 和 seat metrics 是给维护者的数据。本地观察：round 1 的 bottom line 有 6 个长句，超过模板的 3-5 句，而 SKILL.md 交付步骤写的是"三句"，两处自相矛盾。读者体验交给 reader 席。
- (e) 该砍的过度设计：**砍掉 deep 档的匿名反馈轮（至今零次运行），并入缺口轮这一种机制；第二轴不再全量跑**。核查员和盲写不砍。顺带一条：runs.log 里 round 0（sonnet，5/15 降级）对 round 1（opus，3/20 降级）的 Fisher 双侧 p≈0.25（据 runs.log 自算），而且题目和协议也不同，不能当作模型档位的方向证据。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) | Novel? |
|---|---|---|---|---|---|---|---|
| 1 | Co-STORM 表 3 消融：去掉主持人后，Relevance 3.78→3.56、Breadth 3.79→3.69、Depth 3.77→3.41、Novelty 3.05→2.89、信息多样性 0.602→0.577、独立 URL 6.04→5.67。只留一个专家（w/o Multi-Expert）时，Depth 不变（3.77），Novelty 降到 2.93，URL 降到 5.91 | "Notably, removing the moderator has a greater negative impact than reducing the number of experts."；表值经 WebFetch 转录，非逐字 | https://arxiv.org/html/2408.15232 | 2024-08（EMNLP 2024） | primary | H | no |
| 2 | 上面这些消融差距没有做显著性检验。评分由 Prometheus 评审在 1-5 分上打出，系统和模拟用户都是 gpt-4o-2024-05-13，数据集是 WildSeek（100 个主题，24 个领域） | † 只标在 Co-STORM 对两个基线的配对 t 检验上（WebFetch 转述，非逐字）；表题 "Report scoring rubrics on a 1-5 scale for the Prometheus model"；"We simulate the user with an LM (gpt-4o-2024-05-13)" | https://arxiv.org/html/2408.15232 | 2024-08 | primary | M（显著性一项来自摘要模型的转述） | yes |
| 3 | 主持人的具体做法：用上次主持人发言之后检索到、但没有被引用的来源生成问题；来源按"与主题相似、与当前问题不相似"重排，并对照思维导图里的概念去重；连续 L=2 轮专家回答后触发；主持人发言时同时更新专家名单 | "generate informed questions based on the uncited sources retrieved since the last moderator turn"；"The simulated moderator is prompted with unused information and the mind map."；"upon observing L consecutive turns of expert responses" | https://arxiv.org/html/2408.15232 | 2024-08 | primary | H | yes |
| 4 | 按作者自己的说法，一个专家加一个主持人已经拿到大部分收益，专家数量的边际贡献小 | "Having just one expert and one moderator can already provide most of the benefits." | https://arxiv.org/html/2408.15232 | 2024-08 | primary | H | no |
| 5 | 第三方复跑之一（RAPID，ACL Findings 2025）：以非交互方式运行 Co-STORM，三个骨干模型上的信息多样性都低于 STORM（Qwen-Max 0.580 vs 0.618；DeepSeek-v3 0.591 vs 0.607；GPT-4o 0.584 vs 0.626）。在 DeepSeek-v3 上，组织性 3.89 vs 4.58，实体召回 5.87 vs 11.81 | Table 1 表值（WebFetch 转录） | https://arxiv.org/html/2503.00751 | 2025-03 | primary（第三方） | M | yes |
| 6 | 第三方复跑之二（OmniThink，EMNLP 2025）：去掉模拟用户的 Co-STORM 在 GPT-4o 上 Breadth 4.66、Depth 4.65，都高于 STORM 的 4.21，但信息多样性仍然更低（0.6285 vs 0.6342；Qwen-Plus 上 0.5332 vs 0.6417）。**与 #5 在评分项上冲突，在多样性上一致**：5 个骨干模型里，Co-STORM 的多样性 5 次都低于 STORM | Table 2 表值（WebFetch 转录）；表注说明 Co-STORM* 运行时没有模拟用户（转述） | https://arxiv.org/html/2501.09751 | 2025-01（v5 2025-11） | primary（第三方） | M | yes |
| 7 | 20 个主题的规模下，LLM 评审分与人评只是弱相关：Pearson 相关 Interest 0.58、Organization 0.51、Relevance 0.31、Coverage 0.47（n=20）；人评偏好 STORM 13 票、RAPID 27 票 | RAPID Table 5 和 Table 4 表值（WebFetch 转录） | https://arxiv.org/html/2503.00751 | 2025-03 | primary | M | yes |
| 8 | Anthropic 的生产系统不在运行中 steer：子代理同步执行，"lead 不能 steer 子代理"被列为当前设计的瓶颈。它的调整发生在两波之间，由 lead 决定是否追加子代理。约 20 题的评测之所以够用，前提是效应很大 | "the lead agent can't steer subagents, subagents can't coordinate"；"decides whether more research is needed—if so, it can create additional subagents or refine its strategy."；"With effect sizes this large, you can spot changes with just a few test cases." | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H | no（起始来源，具体句子可能是新的） |
| 9 | 当前的 Claude Code harness 在机制上允许运行中 steer：SendMessage 可以按 agent ID 发给仍在运行的子代理，子代理会把它当作任务中途的修正去执行；给已完成的子代理发消息就是续跑，完整历史保留 | "To reach the earlier agent while it's still running, Claude addresses it by the agent ID"；"A subagent treats messages from the agent that launched it as normal task direction, including mid-task course corrections"；"Resumed subagents retain their full conversation history" | https://code.claude.com/docs/en/sub-agents | 2026-10-27 读取（活文档） | primary | H | yes |
| 10 | 同伴压力的量级（23 个开源模型，超过 100 万条判分）：一致而错误的多数让模型放弃了 22.8%（MMLU）、54.8%（GPQA）、71.0%（SimpleQA）的正确答案，84-89% 的翻转落在同伴给的答案上。所有缓解方法都在"顶住压力"和"接受正确纠正"之间此消彼长 | 摘要数字（WebFetch 转述，非逐字）；只测了开源模型 | https://arxiv.org/abs/2608.11247 | 2026-08 | primary（预印本） | M | yes |
| 11 | 权威标签会让模型选被背书的答案，不论对错；同伴一致把对的带错，比把错的纠对容易得多；作者的结论是多智能体系统应该核查同伴答案，而不是简单聚合 | "Authority labels make models more likely to choose the endorsed answer, regardless of whether it is correct."；"peer agreement makes it much easier to mislead initially correct models than to correct initially wrong ones." | https://arxiv.org/abs/2606.01637 | 2026-06 | primary（预印本，4 个开源模型） | M | yes |
| 12 | 谄媚在 2026 年的前沿模型上依然存在：9 个前沿模型里表现最好的 GPT-5.4，也在 23.8% 的客观题场景中为了迎合用户把对的改成错的；用户语气的强度是影响最大的因素之一。这条把 round 1 的 #19（Sharma 2023，LLaMA 2 上最多 27%）更新到了当前模型 | "changes answers from right to wrong to please users in 23.8% of OBJ scenarios"（摘要；其余几句是 WebFetch 转述） | https://neurips.cc/virtual/2026/poster/148794 | 2026（NeurIPS 2026 poster） | primary（摘要页） | M | yes |
| 13 | "人设不提升准确率"在 2025 年的模型上复测成立：6 个模型、GPQA Diamond 和 MMLU-Pro 上，领域内专家人设没有显著影响（Gemini 2.0 Flash 例外），低知识人设普遍有害。这条更新了 round 1 #4、#5 的"2023 年模型"caveat | "had no significant impact on performance (with the exception of the Gemini 2.0 Flash model)"；"generally harmful to benchmark accuracy" | https://arxiv.org/abs/2512.05858 | 2025-12-05 | primary | H | maybe |
| 14 | 无交互基线（NI）的论点多样性最高：NI 0.717，三种辩论协议分别为 0.663、0.640、0.639，差值全部 p_HB<0.001。但测的是 3B-20B 的开源模型，20 个事件 × 5 个种子，单作者 | "Relative to NI, all three debate protocols show significantly lower AD"；表值经 WebFetch 转录 | https://arxiv.org/html/2603.28813v1 | 2026-03 | primary（预印本） | L | yes |
| 15 | 在 Claude 4.5 上，"核查后重规划"唯一的数字被预算混在一起：VMAO 完整度 4.2 vs 静态流水线 3.5，来源质量 4.1 vs 3.2，但 token 用量是 850K vs 350K，只有 25 题，作者也承认没有做组件消融 | 主结果表值；"tests verification and replanning jointly without a component-level ablation" | https://arxiv.org/html/2603.11445v2 | 2026-03（ICLR 2026 workshop） | primary | M | yes |
| 16 | 反方证据：Anemoi 在运行中让 agent 之间直接通信，在 GAIA 上得到 52.73%，OWL 是 43.63%。但它的规划者是弱模型，没有去掉通信的消融，作者来自推广该协议的公司 | "achieved 52.73% accuracy with a small LLM (GPT-4.1-mini) as the planner"；"surpassing the strongest open-source baseline OWL (43.63%) by +9.09%"；"would be more pronounced when the planner agent is powered by a weaker LLM" | https://arxiv.org/html/2508.17068v3 | 2025-08（v3 2025-10） | primary（厂商自报） | L | yes |
| 17 | 小样本 eval 能检出多大的差：配对设计下所需题数为 n=(z_{α/2}+z_β)²(ω²+σ²_A/K_A+σ²_B/K_B)/δ²；文中例子是检出 0.03 的差需要约 969 题；作者建议尽量用配对标准误 | 公式 (9)；"n = (z0.025 + z0.20)²(1/9)/(0.03)² ≈ 969"；"We therefore recommend using the paired version of the standard error estimate wherever practicable." | https://arxiv.org/abs/2411.00640 | 2024-11 | primary | H | maybe |
| 18 | 数据点只有几百条以下时，基于 CLT 的误差棒会严重低估不确定性 | "CLT-based methods perform very poorly, usually dramatically underestimating uncertainty" | https://arxiv.org/abs/2503.01747 | 2025-03（ICML 2025 position spotlight） | primary | H | maybe |
| 19 | 评估单个 agent 的贡献时，留一法（LOO）找瓶颈 agent 的效果与组合法相当，成本低得多；让 LLM 在上下文里"内省地"判断去掉某个 agent 会怎样，并不可靠。同一作者组的 ICLR 2026 版本说，在层级系统里 LOO 可以可靠地代替 Shapley/Banzhaf（同源，不算独立佐证） | "Leave-One-Out (LOO) identifies bottleneck agents as effectively as combinatorial methods"；"introspective LLM judges fail to faithfully approximate this behavior"；ICLR 版："Leave-One-Out (LOO) attribution serves as a reliable proxy" | https://arxiv.org/abs/2605.27621 ；https://www.iclr.cc/virtual/2026/10016292 | 2026-05（v2 2026-09）；ICLR 2026 | primary（预印本） | M | yes |
| 20 | 本 skill round 1 的核查员用的是单轴协议，没有可信度列。20 条里 3 条 PARTIAL；另有 3 条（#4、#8、#12）判了 PRIMARY-CONFIRMED，但措辞或归属需要改。对 #1-#7 做的反证搜索，多数结果是"没有独立复现"，也就是说在论文型 claim 上第二轴大概率给 SINGLE-ORIGIN | "反证搜索：未找到独立复现或反驳。"（#1、#5）；"未找到复现"（#2）；"未找到独立复现"（#6）；Corrections 一节修正了 #4、#8、#12 | /home/xhyumiracle/projects/xhyu/family/family-skill-design/verification.md | 2026-10-27 | primary（本地运行记录） | H | maybe |

## My edge
- 我打开的是 Co-STORM 表 3 本身，以及两份第三方复跑的表（RAPID、OmniThink），没有停在摘要那句"去掉主持人更伤"上。看下来：消融行没有显著性检验，评审是 Prometheus，最大的差是 Depth 掉了 0.36 分（1-5 分制）；第三方复跑中 Co-STORM 的信息多样性 5 次都低于 STORM。
- 我区分"共享对话里的主持人"和"给独立席位发消息"这两件事。主持人的输入是未被引用的已检索材料；在 family 里，这些材料只存在于各席自己的上下文里，席位结束之前编排者拿不到。所以可迁移的是"从未用信息出问题"这个机制，要换到田野工作之后执行，并且需要席位把"读过但没引用"的材料交出来。
- 盲写有一个副产品：一次运行里任意几个席位的组合，都可以近似当作一个更小 crew 的样本。所以 3/4/5 席、outsider 开或关，都能离线做留一法消融，不需要重跑（#19 支持用 LOO 代替组合法）。运行中 steer 会把这个性质毁掉。
- round 1 的盲区"2023 年模型上的结论"，我用 2025-26 年的复测更新了：人设复测仍然无效（#13），谄媚在前沿模型上仍有 23.8%（#12）。
- 用 Miller 的公式算出 10-20 题 eval 能检出的下限；runs.log 里 sonnet 对 opus 的降级率差异，Fisher p≈0.25。

## What the other seats will get wrong
- 他们会把"去掉主持人比砍专家更伤"当作定论，从而主张编排者必须运行中介入。他们看不到两件事：消融行没做显著性检验、是 LLM 评审在 1-5 分上打的分（#2）；第三方复跑中这个系统的多样性优势不存在（#5、#6）。
- 他们会提议用 SendMessage 在运行中 steer，因为 harness 支持（#9），但不会给它定价：这样做会让 crux 不再独立，让同伴和权威信号进入席位（#10-#12），还会毁掉免费的子集消融。
- evaluator 可能会设计一个 10-20 题的 rubric eval 来区分 3/4/5 席。在这个题数下，只有很大的效应才检得出来（#17、#18），而且 rubric 评审分与人评的相关只有 0.31-0.58（#7）。区分席位配置要靠子集上的留一法，比较模型档位要靠 claim 级降级率；后者每题有 20 个观测，统计功效高得多（按两比例检验粗算，15% 对 30% 的降级率每臂约需 120 条 claim，即约 6 题以上；按题聚类的话还要更多）。
- 有人会把 round 0 的 5/15 和 round 1 的 3/20 当作"opus 席位更好"的方向证据。实际上 p≈0.25，而且题目和协议都不一样。

## What would change my mind
- 一个预算匹配的消融：给并行研究 agent 在运行中发编排者消息，提升了核查通过的 claim 覆盖，同时没有降低来源多样性。
- Co-STORM 的消融行补上了显著性检验，或者有第三方复跑在信息多样性或核查通过 claim 数上复现了主持人的优势。
- 有证据表明 Claude 4.x 或 GPT-5.x 在研究任务里不会随编排者或同伴消息改动已有来源支撑的结论，翻转率接近 0。

## Positions I hold without evidence
- 编排者在运行中看不到席位读过但没有引用的材料，所以运行中 steer 只能依据还没产生的摘要，近乎盲目。
- 子集近似是有偏的：卡片上 "Leave to other seats" 那一行在选角时就把席位耦合在了一起，真正的三席 crew 会分到更宽的领地。因此子集指标是对小 crew 表现的下界估计，比较配置时方向可用，绝对值不能直接用。
- 缺口轮的价值集中在"会改变 bottom line 的盲区"上。round 1 恰好有一例：Co-STORM 主持人那个盲区被标为可能改变结论，却留给了整整一轮新运行，其实 1 个席位 × 3-4 次搜索就能关掉。
- 第二轴（可信度）对论文型题目基本是噪音，对厂商、市场、单一数据源的题目有用。
- 闭源前沿模型对编排者消息的从众率应该低于开源模型，但不会是 0。#12 支持这个方向，但它测的是用户，不是编排者。

## Deliberately not examined
- WebWeaver、ScaffoldAgent 的动态大纲消融（单 agent 长文写作，brief 已排除；搜索摘要提到 ScaffoldAgent 去掉修订动作后 RACE 48.27→43.09，我没打开）。
- FlashResearch 的实时编排数字（摘要说"最高 5 倍加速、质量相当"）；MACU 的重规划预算消融（computer-use 任务，仅见 EmergentMind 摘要）。
- rubric 设计和 DeepResearch Bench 等基准（evaluator）；GRADE（grade）；报告可读性（reader）。
- 缺口轮的墙钟时间和 token 成本：没有数据，只给了预算建议。
- 前沿推理模型上的辩论复测，以及 Artificial Hivemind 的同质性结果。
- Reddit 和实践者关于用 SendMessage 中途 steer 的经验（没有用 site:reddit.com 搜）。
- PARROT（arXiv 2511.17220）：PDF 读不出来，没有使用。

## Proposed changes to the skill
| file | keep/change/add/remove | what | evidence |
|---|---|---|---|
| SKILL.md | add | 新增步骤 "3a. Gap round"（缺口轮），在 Fieldwork 之后、Verify 之前；standard 档可选，deep 档默认，最多一轮。编排者从各席的 "Read but not cited" 清单、"Deliberately not examined" 段，以及可能改变结论的盲区里，写出不超过 3 个缺口问题；用 SendMessage 续跑领地对口的 1-2 个席位（保留上下文），每席 3-4 次搜索。消息里只放问题、领地和预算，不放任何席位的发现，也不放编排者的倾向。续跑产出在笔记里单列为 "post-steer" 段，不计入独立性指标和子集指标 | #3 #8 #9；搜索数为 judgment |
| SKILL.md | change | 规则 3 补一句：田野工作期间不给席位发消息。harness 允许这样做（#9），但同伴和权威信号会翻转正确答案（#10 #11 #12），无交互时论点多样性最高（#14），并且会破坏盲写带来的子集消融（#19）。唯一允许的接触是席位完成后的续跑 | #9 #10 #11 #12 #14 #19 |
| SKILL.md | add | 加一句 Co-STORM 的准确表述：主持人消融的差距（例如 Depth 3.77→3.41）没有做显著性检验，由 LLM 评审打分；第三方复跑中它的信息多样性 5/5 低于 STORM；本 skill 借用的是"从未用信息出问题"这个机制，不是"运行中干预" | #1 #2 #3 #5 #6 |
| SKILL.md | change | 规则 1 的谄媚证据补上 2026 年前沿模型的数字（GPT-5.4 为 23.8%）；规则 2 的人设证据补上 2025 年 6 个模型的复测 | #12 #13 |
| SKILL.md | change | Step 5 的 runs.log 每行补两项：每席的 claim 编号及核查结论，每席 URL 集合所在的文件路径，以便离线计算子集指标（3/4/5 席、outsider 关）。积累到 10 次运行后再算一次 | #17 #18 #19 |
| SKILL.md | change | Deliver 步骤写"bottom line 最多三句"，模板写"三到五句"，统一成一个数（round 1 实际写了 6 个长句） | judgment（本地 report.md） |
| casting.md | remove | 删掉 "Feedback round (deep tier only)" 整节，由缺口轮替代：两者机制相同（续跑席位、少量搜索、只带问题）。crux 的处理改为在缺口轮里问"什么证据能解决 crux N"，不再让席位读匿名化的对方论点 | #11 #14；round 1 #7；runs.log 显示零次运行 |
| casting.md | keep | 席位是领地，不是人设；outsider 继续标 experimental | #13 |
| seat-protocol.md | add | 笔记新增一节 "## Read but not cited"：最多 5 个读过、和问题相关、但没有进 claims 表的 URL，每个附一行说明。这就是 Co-STORM 主持人的输入（"uncited sources"），没有它编排者无法出缺口问题。需要同步更新合成器解析的标题列表 | #3 |
| seat-protocol.md | add | 加缺口轮的续跑消息模板：问题 + 领地 + 搜索数，明文禁止带入其他席位的发现 | #10 #11 |
| verifier-protocol.md | change | claims.md 的选法：先给每席保底 2 条（各取该席最具诊断性的），剩余预算再按诊断性排序。否则"每席独有核查通过 claim"有一部分是选择偏差，留一法指标也就不可信 | #19；judgment |
| verifier-protocol.md | change | 第二轴（可信度）只对标注为 single-source、厂商自报或单源定量的 claim 运行；论文型 claim 默认 SINGLE-ORIGIN，不做反证搜索，省下的预算用于打开来源 | #20；judgment |
| verifier-protocol.md | keep | MISQUOTED-INVERTED 规则、一名核查员、20 条预算 | #11（"verify rather than aggregate"）；round 1 |
| report-template.md | change | 把 "Seat estimates" 和 Cost 段里的 seat metrics 移到末尾的 "For the maintainer" 附录。十分钟阅读路径为 Bottom line → Belief vs finding → Cruxes → Blind spots → Next step | judgment（reader 席的领地） |
| report-template.md | add | Cost 段加子集指标：每席的留一法 Δ，即去掉该席后独有核查通过 claim 和独立一手来源各减少多少。这个数由计数得出，不让综合者去"评估"哪一席重要 | #19 |
| report-template.md | add | 加一行 "Gap round"：问了什么，续跑了谁，带回了什么，标注 post-steer | #3 |
| references/eval.md（新文件） | add | 一个 10-20 题 eval 的骨架。每题跑一次 5 席，用子集法得到 3/4/5 席和 outsider 开关的对比；模型档位在同一批题上配对重跑。主指标是 claim 级降级率（按题聚类的标准误）和留一法独有核查通过 claim 数；rubric 分只作次要指标。报告配对差及其置信区间，不用 CLT 误差棒。rubric 本身交给 evaluator 席 | #7 #17 #18 #19 |

## Sources
1. https://arxiv.org/html/2408.15232 : Co-STORM（Jiang et al., EMNLP 2024），表 3 消融、主持人机制、附录 B 思维导图、模型与评审；2024-08
2. https://arxiv.org/html/2503.00751 : RAPID（ACL Findings 2025），Table 1 复跑 STORM/Co-STORM（三个骨干），Table 4 人评，Table 5 人评与 LLM 评审的相关，Table 7 成本；2025-03
3. https://arxiv.org/html/2501.09751 : OmniThink（EMNLP 2025），Table 2 复跑 STORM/Co-STORM*；2025-01，v5 2025-11
4. https://www.anthropic.com/engineering/multi-agent-research-system : Anthropic 多智能体研究系统，同步执行、"can't steer subagents"、两波之间追加、约 20 题评测；2025-06-13
5. https://code.claude.com/docs/en/sub-agents : Claude Code 子代理文档，SendMessage 发给运行中的子代理、续跑保留历史；2026-10-27 读取
6. https://arxiv.org/abs/2608.11247 : Hussain & Nielbo，从众缓解方法落在同一条"抗压/接受纠正"前沿上，23 个开源模型；2026-08
7. https://arxiv.org/abs/2606.01637 : Qu, Fu & Hu，"Easier to Mislead Than to Correct"，权威标签与同伴一致的影响；2026-06
8. https://neurips.cc/virtual/2026/poster/148794 : SuperSycophantic，9 个前沿模型，GPT-5.4 改对为错 23.8%；NeurIPS 2026
9. https://arxiv.org/abs/2512.05858 : Basil et al.，Prompting Science Report 4，专家人设不提升准确率，6 个模型；2025-12-05
10. https://arxiv.org/html/2603.28813v1 : Zargari Marandi，辩论协议对比，无交互时论点多样性最高（小型开源模型）；2026-03
11. https://arxiv.org/html/2603.11445v2 : VMAO，核查后重规划，Claude Sonnet/Opus 4.5，没有组件消融；2026-03
12. https://arxiv.org/html/2508.17068v3 : Anemoi，agent 之间直接通信，GAIA 52.73 vs 43.63，厂商自报；2025-08/10
13. https://arxiv.org/abs/2411.00640 : Miller，"Adding Error Bars to Evals"，配对标准误与样本量公式（PDF 第 6-9 页）；2024-11
14. https://arxiv.org/abs/2503.01747 : Bowyer, Aitchison & Ivanova，小样本 eval 不要用 CLT（ICML 2025 position spotlight）；2025-03
15. https://arxiv.org/abs/2605.27621 : Lu et al.，"Agents that Matter"，LOO 与组合法效果相当，内省式 LLM 评审不可靠；2026-05，v2 2026-09
16. https://www.iclr.cc/virtual/2026/10016292 : 同一作者组的 ICLR 2026 版本，LOO 可以代替 Shapley/Banzhaf；2026
17. /home/xhyumiracle/projects/xhyu/family/family-skill-design/verification.md : 本 skill round 1 的核查表（单轴）；2026-10-27
18. /home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md 与 /home/xhyumiracle/projects/xhyu/family/runs.log : round 1 报告与两次运行的指标；2026-10-27

## Budget used
searches: 12 / 12 · fetches: 21（其中 5 次没有挂在搜索下：Co-STORM 起始来源 3 次、Anthropic 起始来源 1 次、Claude Code 文档 1 次；Miller 的 PDF 落盘后在本地读了 4 页；PARROT 的 PDF 读不出，没有使用）· stopped because: budget spent
