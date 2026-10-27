# Seat: researcher（只读消融表、不读摘要的多智能体 LLM 研究者）

## Core position
六项设计里，有对照证据支撑的是两项：盲写独立（从众与辩论研究：辩论本身不提升期望正确率，多数压力压制纠错）和单独核验（深度研究系统引用准确率 40-80%）。STORM 消融里，"视角"对提纲质量的贡献很小，主要作用是让独立来源数翻倍；真正承重的是"读完再问"的迭代检索。人设细节无用（SPP、Zheng v3）。"3-4 席最佳"来自 ChatEval 单一评测基准上 2.5 个点的差，不能外推到开放式研究。"跨行类比外援优于模板"和"每席都用最强模型"在文献里没有对照实验：它们是未测量的信念，而不是被证伪的结论。对前两项判断置信度高；对后两项"无证据"这一判断置信度也高。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) |
|---|---|---|---|---|---|---|
| 1 | STORM 消融：去掉"视角"对提纲召回几乎无影响；去掉"对话"（读后再问的迭代检索）影响最大。基线是同一管线去掉组件，问题总数固定 | Table 3, GPT-4: STORM 92.73 / 45.91（heading soft recall / entity recall）；w/o Perspective 92.39 / 42.70；w/o Conversation 88.75 / 39.30。GPT-3.5: 86.26/40.52 vs 84.49/40.12 vs 77.97/31.98。原文："STORM w/o Conversation" gives much worse results（WebFetch 摘要转述，表中数字为原表） | https://arxiv.org/html/2402.14207 | 2024-02（NAACL 2024） | primary | H |
| 2 | STORM 中"视角"的可测作用是扩大检索面：独立参考来源数接近翻倍 | Table 5 平均独立参考数：STORM 99.83，w/o Perspective 54.36，w/o Conversation 39.56；"the full pipeline discovers more different sources"（我抓取的内容未标明该表对应哪个模型） | https://arxiv.org/html/2402.14207 | 2024-02 | primary | H |
| 3 | STORM 的人评规模很小，比较对象是 oRAG 全管线而非消融；+25%/+10% 是"评分≥4 的文章比例"之差 | "25% more articles produced by STORM are considered organized (Organization rating ≥4)"; "10% more are deemed to have good coverage"；10 位编辑、20 个主题、每对文章 2 位编辑评；N=M=5 | https://arxiv.org/html/2402.14207 | 2024-02 | primary | H |
| 4 | SPP：按任务动态生成的细粒度人设，优于固定通用人设（"AI Assistant"+"Expert"）。注意这个固定基线远弱于 family 的五个证据标准原型 | SPP vs SPP-Fixed-Persona：Trivia N=5 79.9 vs 72.9；N=10 84.7 vs 75.9；Codenames 79.0 vs 38.1；Logic Grid 68.3 vs 64.3；"SPP consistently outperforms SPP-Fixed-Persona across all tasks"；"cognitive synergy only emerges in GPT-4 and does not appear in less capable models" | https://arxiv.org/html/2307.05300v3 | 2023-07（v3 2024） | primary | H |
| 5 | SPP：给人设加详细档案不提升，反而略降；名字就够 | SPP-Profile 79.1 / 83.0 / 76.7 / 64.8，SPP 79.9 / 84.7 / 79.0 / 68.3；"a fine-grained persona name without a detailed description may already be sufficient" | https://arxiv.org/html/2307.05300v3 | 2023-07 | primary | H |
| 6 | Zheng et al. 的结论在版本间反转：v1（2023-11）称人际角色"generally improved"；v3（2024-10，EMNLP Findings）称人设不提升，且自动挑选最佳人设"little better than random" | v3 摘要："adding personas in system prompts does not improve model performance"（162 角色、4 个模型家族、2,410 道事实题）；v1：162 角色、3 个模型、2,457 题，加角色后性能普遍提升（WebFetch 转述） | https://arxiv.org/abs/2311.10054 ; https://arxiv.org/abs/2311.10054v1 | 2023-11 / 2024-10 | primary | H |
| 7 | ChatEval：多个智能体用同一个角色提示时等于单智能体，换成多样角色后才有增益。这些角色只是角色描述，智能体不检索，任务是评判两段回答 | Table 3（ChatGPT, FairEval）：Single-Agent 53.8 / κ0.27；Multi-Agent (Same Role Prompt) 53.8 / 0.25；Multi-Agent (Diverse Role Prompt) 60 / 0.33 | https://arxiv.org/pdf/2308.07201 | 2023-08（ICLR 2024） | primary | H |
| 8 | ChatEval 的"3-4 个角色最佳"：ChatGPT、单一评测基准，效应约 2.5 个点；增加讨论轮数无显著提升 | "reaches an apex with an Acc. of 62.5% at role numbers 3 and 4 before declining at role number 5"（2 个角色的默认配置为 60.0）；"no significant upward trend is detected with respect to the increase in discussion turns" | https://arxiv.org/pdf/2308.07201 | 2023-08 | primary | H |
| 9 | 在开放式发散任务里，名人人设只让多样性提升一点点；流程（CoT 分步）提升更多。这是我找到的最接近"覆盖面"的人设测量 | 余弦相似度（越低越多样）：Steve Jobs 人设 0.368 vs 基线 0.377；人类组 0.243 vs GPT-4 0.255-0.432；CoT 使独立创意 "from around 3700 for the base prompt to 4700"；共 35 种提示 | https://arxiv.org/pdf/2402.01727 | 2024-01 | primary | H |
| 10 | 辩论 vs 投票：多智能体辩论的收益大部分来自多数投票（集成）；辩论本身不提升期望正确率；把信念更新偏向纠错的干预有效 | "Majority Voting alone accounts for most of the performance gains typically attributed to MAD"; "debate alone does not improve expected correctness"; "biasing the belief update toward correction, can meaningfully enhance debate effectiveness"（7 个 NLP 基准） | https://arxiv.org/abs/2508.17536 | 2025-08（NeurIPS 2025 Spotlight） | primary | H |
| 11 | 从众：所有受测 LLM 都会跟从群体意见；在 Doubt 协议下平均从众率接近一半 | "Finding I: All the evaluated LLMs show a tendency to conform."；5 个代表模型的平均从众率 23.5%（Wrong Guidance）/ 31.3%（Trust）/ 47.2%（Doubt）；GPT-4o 在 Trust 协议下准确率降 22.6%（数字经 WebFetch 摘要；论文 Table 1 与 Table 2 的 Llama3.1-405B 数值不一致） | https://arxiv.org/html/2501.13381v2 | 2025-01（ICLR 2025） | primary | M |
| 12 | 受控辩论研究：多数压力压制独立纠错；群体多样性和个体推理强度是辩论成败的主要因素 | "majority pressure suppresses independent correction"; "intrinsic reasoning strength and group diversity are the dominant drivers of debate success"（Knight-Knave-Spy 逻辑谜题） | https://arxiv.org/abs/2511.07784v1 | 2025-11 | primary | H |
| 13 | 180 种配置的受控研究：独立并行智能体放大错误 17.2 倍，有中心协调时控制在 4.4 倍；可并行任务 +80.8%，顺序推理任务 -39% 至 -70%；单智能体基线超过约 45% 后协调收益递减或转负 | 摘要（WebFetch 转述，数字原样）："independent agents amplify errors 17.2x, while centralized coordination contains this to 4.4x"；"+80.8% on parallelizable tasks"；"degraded performance by 39-70%"；"~45%"；在 GPT-5.2 上做样本外验证 | https://arxiv.org/abs/2512.08296v2 | 2025-12（v3 2026-04） | primary | H（数字）/ M（"Independent" 拓扑是否等同 family 的写法，我未核对定义） |
| 14 | 深度研究系统的引用经常不支持其陈述，单独的来源核验有必要 | Deep-research 配置 "still exhibit large fractions of unsupported statements"，引用准确率 "ranging from 40--80% across systems"（受测系统包括 GPT-4.5/5、Perplexity、Gemini 等） | https://arxiv.org/abs/2509.04499v1 | 2025-09（ICLR 2026） | primary | H |
| 15 | CoVe 的关键设计是因子化核验：核验问题要在不看初稿的情况下独立回答。注意 CoVe 是闭卷自检，不重新打开来源 | "(iii) answers those questions independently so the answers are not biased by other responses"（摘要不含数字，我没有看到它的结果表） | https://arxiv.org/abs/2309.11495 | 2023-09 | primary | H（设计）/ 数字未看 |
| 16 | Anthropic：多智能体系统在内部研究评测上比单智能体 Opus 4 高 90.2%；token 用量约为对话的 15 倍。该配置的子智能体并非最强模型（Opus 主控 + Sonnet 子智能体） | "outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval"; "multi-agent systems use about 15× more tokens than chats"；"Opus 主控 + Sonnet 子智能体"这一点我拿到的引文只是句子片段，二手来源（aktagon）也这样写，需要核验员确认 | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H（数字）/ M（配置） |
| 17 | Anthropic：在 BrowseComp 上，token 用量单独解释 80% 的性能方差；换更强的模型比把 token 预算翻倍收益更大。BrowseComp 是找难找事实的基准，不是综合研究任务 | "three factors explained 95% of the performance variance in the BrowseComp evaluation"; "token usage by itself explains 80% of the variance"; "upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7" | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H |
| 18 | Anthropic 的 CitationAgent 负责给结论标注出处位置，不是对抗式事实核验。他们的评测从约 20 个查询起步；规模规则是写在提示里的启发式，不是测出来的最优值 | "to identify specific locations for citations"; "We started with a set of about 20 queries representing real usage patterns."; "Simple fact-finding requires just 1 agent with 3-10 tool calls"; "complex research might use more than 10 subagents" | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H |

## My edge
- 我能把"多样角色有帮助"拆成两种机制。第一种是让单个智能体更聪明：证据为负（Zheng v3 #6，SPP 详细档案无益 #5）。第二种是让多个智能体去看不同的东西、犯不相关的错：证据为正（ChatEval 同角色等于单智能体 #7，STORM 独立来源翻倍 #2，Debate-or-Vote 的增益来自集成 #10）。family 的 SKILL.md 规则 2 把这两种混在一起了。
- STORM 消融里承重的组件是"对话"（读后再问的迭代检索），不是"视角"（#1）。在 family 里，"对话"对应每个席位自己的搜索、阅读、再追问循环，该保护的是这个循环，而不是选角流程。
- 每个常被引用的数字都有很窄的适用范围：3-4 角色的峰值是 ChatGPT 在一个评测基准上 60→62.5（#8）；90.2% 是内部评测，配置用的是 Sonnet 子智能体（#16）；80% 方差来自 BrowseComp（#17）；STORM 人评只有 20 个主题（#3）。这些都不是开放式研究综合任务。
- 文献里找不到"跨行类比外援"或"发现式选角 vs 精心设计的模板"的对照实验。SPP 的固定基线只是"AI Assistant + Expert"（#4），比 family 的五个证据标准原型弱得多，不能拿来反驳模板。
- 2025-2026 年对辩论的研究（#10-#12）一致支持保持盲写。这也意味着 deep 档的交叉质询轮次有引入从众的风险，除非像 #10 那样把更新偏向纠错。

## What the other seats will get wrong
- 引用"Zheng et al. 2023 证明人设无用"：2023 年的 v1 结论正好相反，负面结论出自 2024 年 10 月的 v3（EMNLP Findings 2024）。SKILL.md 规则 2 现在写的就是"Zheng et al. 2023"（#6）。
- 把 ChatEval 当作"检索不同来源的角色更好"的证据：ChatEval 的智能体不检索，它测的是评判任务上的角色描述多样性。SKILL.md 规则 2 用"STORM; ChatEval"支持"roles that search different places"，属于错误归因（#7）。
- 拿 Anthropic 的 90.2% 支持"每席都用最强模型"：该配置的子智能体是 Sonnet，而且"模型升级强于预算翻倍"是在 BrowseComp 上测的（#16、#17）。也会有人把 CitationAgent 读成核验步骤，它其实只做出处标注（#18）。
- 怀疑论席位可能拿 Kim et al. 的"独立智能体放大错误 17.2 倍"攻击盲写。但 family 是盲写之后接中心综合和核验员，更接近有校验点的中心化拓扑。论文对 "Independent" 的定义我没有核对，这一点仍有疑问（#13）。

## What would change my mind
- 一项在同一组问题、同样预算下比较"五原型模板"与"发现式席位+外援"选角的实验，用独立来源数和专家评的覆盖度做指标。如果外援席位在多次运行中贡献的独有来源和独有关键论断显著更多，我会把信念 1 从"未测量"改为"有支持"。
- 在固定搜索次数下比较 Opus 席位和 Sonnet 席位：如果更强的模型找到明显更多的一手来源，或核验降级率明显更低，信念 2 成立。
- 一项研究显示：在独立研究之后加入交叉质询，研究报告的事实性（核验后）比"只做核验"更高。

## Positions I hold without evidence
- 我推断 FairEval 大约有 80 道题（ChatEval 的准确率都是 1.25% 的整数倍）。如果属实，ChatEval 的角色效应只相当于 2-5 道题。我没有打开 FairEval 原文确认。
- 我记得 STORM 除了发现的视角外，还默认加入一个"basic fact writer"视角，本次没有核实。
- 我记得 Anthropic 那篇文章强调要给子智能体详细的任务描述（目标、输出格式、工具和来源指引、边界），否则会重复劳动，但本次抓取没有拿到原句。如果属实，那么卡片细节有用的是"任务指令"部分，而不是"人物传记"部分。
- 外援席位如果有价值，价值应当体现在它提的第一批问题不同，从而搜索不同的地方；独立来源数应能测到这一点。
- 2023 年的结果（SPP、ChatEval、STORM 的 GPT-3.5/4）可能不适用于 Claude 4 级别的模型。SPP 本身就显示人设效应依赖模型能力（#4）。
- 我记得 CoVe 的 FactScore 从约 55.9 升到 71.4，但没有看到原表，所以不列入表格。
- family 首次运行的数据（来自 brief：15 条中 5 条 PARTIAL，其中 2 条改变了原意）只是 n=15 的内部数据，但方向与 DeepTRACE（#14）一致。

## Deliberately not examined
- Co-STORM（2408.15232）里主持人和思维导图的消融。
- Du et al.（2305.14325）和 Liang et al.（2305.19118）原文：我只经由 ChatEval 对它们的引用看到"轮数增加不提升"。
- Smit et al. "Should we be going MAD?"；异构模型多样性研究（例如 Hegazy 2024），这类研究关系到 `--second-model`。
- 多智能体系统在生产中的失败模式分类（例如 MAST），以及成本、延迟等工程现实。这是我这个席位的盲区。
- Tran et al. 2501.06322 和 2502.14321 两篇综述；GitHub 上的同类仓库。
- Kim et al. 对 "Independent / Centralized" 拓扑的精确定义，以及各基准的分项数字。
- CoVe 的结果表。

## Proposed changes to the skill
| file | keep/change/add/remove | what | evidence row # or "judgment" |
|---|---|---|---|
| SKILL.md（规则 2） | change | 把 "Zheng et al. 2023" 改为 "Zheng et al., EMNLP Findings 2024 (v3)"，并注明 2023 年 v1 的结论相反。删除 ChatEval 作为"检索不同来源的角色有用"的证据，改写为：人设不会让单个智能体更准（#6、#5）；多个智能体之间的差异有用，因为它让它们看不同的东西、犯不相关的错（#7、#2、#10） | #5 #6 #7 #2 #10 |
| SKILL.md（开头的 STORM 段） | change | 保留"增益在广度和组织，不在准确率"，并补一句：STORM 消融中承重的是基于检索的迭代追问（对话），视角的主要可测作用是让独立来源数接近翻倍（99.83 vs 54.36）；人评只有 20 个主题 | #1 #2 #3 |
| seat-protocol.md（§2） | add | 加一条：至少一半的搜索应当是由刚读到的内容派生出的追问（STORM 的"对话"），而不是一开始就把查询全部列好 | #1 |
| casting.md（Diversity test） | change | 多样性测试改为比较各席位计划的头 3 个查询和目标来源类型；如果两个席位会跑相同的头几个查询，就是同一个席位。"trusts / asks / paid by"的标签保留，作为生成查询的手段 | #2 #7 #9 |
| casting.md（Headcount 末句） | change | "Debate-style setups peak around three to four distinct roles" 改为如实表述："ChatEval（ChatGPT，一个评测基准，2023）在 3-4 个角色时达到 62.5%，2 个角色时为 60%"；删除没有来源的 "past six you are paying for repetition"；4-6 席标注为经验判断 | #8 |
| casting.md（Move 2 外援） | change | 把 "Mandatory" 改为"默认启用、需要实测"。文献中没有类比选角的对照实验；Zheng v3 显示自动挑人设约等于随机，说明编排者的直觉选择不可靠。保留外援，但把它贡献的独有来源占比写进报告，用 5-10 次运行检验主人的信念 1 | #6 #4 + judgment |
| casting.md（Move 1 发现） | keep | 这是与 STORM 原法一致的做法，也是 SPP 中"动态优于通用"的最近证据。但要在文中写明：它从未与精心设计的模板做过对照 | #4 #2 |
| seat-protocol.md（卡片模板） | keep | 卡片保持短，人物只写一句；细节写在"去哪搜、信什么证据"上，不写人物背景 | #5 + judgment |
| report-template.md（Cost 或新增小节） | add | 加一行来源重叠统计：每个席位的独立 URL 数、席位两两之间的 URL 重叠、最终报告结论各来自哪个席位。这是 STORM 用过的指标，也是测试信念 1 的唯一廉价办法，不需要额外的智能体 | #2 + judgment |
| SKILL.md（规则 6 一致即选角失败） | change | 改为：如果各席位一致，而且来源高度重叠，说明选角失败；如果一致但来源基本不重叠，说明证据收敛，是强信号 | #12 + judgment |
| SKILL.md（规则 3 盲写） | keep | 盲写独立有 2025 年的从众与辩论研究支持 | #10 #11 #12 |
| casting.md（Cross-examination round） | change | 把交叉质询移到核验之后，并把 verification.md 发给各席位。"concede" 也必须写明是哪条证据改变了判断，否则默认 "hold"；不得向被标为 PARTIAL 或 MISQUOTED 的论断让步。这样把信念更新偏向纠错，而不是偏向多数 | #10 #11 #12 |
| verifier-protocol.md | keep | 核验员只拿 claims.md、看不到席位笔记，这与 CoVe 的因子化核验一致；单独核验是六项中证据最强的一项 | #14 #15 #13 |
| SKILL.md（Keeping the bill honest，model 一行） | change | 席位继续不传 model 覆盖。新增说明：没有证据表明每席用最强模型划算，Anthropic 拿到 90.2% 的配置用的是 Sonnet 子智能体；最强模型应优先给编排者和综合步骤 | #16 #17 |
| SKILL.md（Depth tiers，deep 档） | change | deep 档优先增加每席的搜索次数（token 用量解释了 80% 的方差），而不是先加席位和辩论轮。席位数在 3-4 个以后收益很小，单智能体已经较强时协调收益会递减 | #17 #13 #8 |
| SKILL.md（新增） | add | 每次运行在 `family/runs.log` 追加一行：tier、席位数、tokens、每席独立来源数、核验降级率。积累约 20 次运行后，就能检验两条主人信念（Anthropic 的评测也是从约 20 个查询起步的） | #18 + judgment |

## Sources
1. https://arxiv.org/html/2402.14207 : STORM（Shao et al.），Table 3 提纲消融、Table 5 独立来源数、§6 人评；2024-02，NAACL 2024
2. https://arxiv.org/html/2307.05300v3 : Solo Performance Prompting（Wang et al.），SPP / Fixed-Persona / Profile 对比；2023-07，v3 2024
3. https://arxiv.org/pdf/2308.07201 : ChatEval（Chan et al.），Table 1、Table 3（同角色 vs 多样角色）、§4.3 角色数与轮数；2023-08，ICLR 2024
4. https://arxiv.org/abs/2311.10054 : Zheng et al. v3 摘要与版本历史（人设不提升）；2024-10，EMNLP Findings 2024
5. https://arxiv.org/abs/2311.10054v1 : Zheng et al. v1 摘要（结论相反）；2023-11
6. https://arxiv.org/pdf/2402.01727 : Meincke, Mollick, Terwiesch, Prompting Diverse Ideas（人设与 CoT 对创意多样性的影响）；2024-01
7. https://arxiv.org/abs/2508.17536 : Choi, Zhu, Li, Debate or Vote（投票占辩论增益的大部分，辩论构成鞅）；2025-08，NeurIPS 2025 Spotlight
8. https://arxiv.org/html/2501.13381v2 : BenchForm, Do as We Do, Not as You Think（多智能体从众）；2025-01，ICLR 2025
9. https://arxiv.org/abs/2511.07784v1 : Wu, Li, Li, Can LLM Agents Really Debate?（受控辩论研究）；2025-11
10. https://arxiv.org/abs/2512.08296v2 : Kim et al., Towards a Science of Scaling Agent Systems（180 种配置，误差放大）；2025-12
11. https://arxiv.org/abs/2509.04499v1 : DeepTRACE（深度研究系统引用准确率 40-80%）；2025-09，ICLR 2026
12. https://arxiv.org/abs/2309.11495 : Chain-of-Verification（Dhuliawala et al.）摘要；2023-09
13. https://www.anthropic.com/engineering/multi-agent-research-system : Anthropic，How we built our multi-agent research system；2025-06-13

## Budget used
searches: 10 / 10 · fetches: 13（其中 2 个 PDF 先抓取到本地，再读取页面图像：ChatEval 第 5-9 页、Meincke 第 1-6 页）
