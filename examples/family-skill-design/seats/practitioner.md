# Seat: practitioner（2026 年做过并用过 STORM 式 / council 式 Claude Code skill，细读过别人交付后的复盘）

## Core position
六个设计选择里，有"先踩坑再改"式实测支撑的只有三条：独立上下文的并行席位 + 研究结束后由一个综合者单独写报告；一个批量核查员，而不是每条发现一个核查员；预算（token 与模型）决定质量。默认 5 席、卡片里的人物细节、deep 档全员交叉质询、强制外行席，都没有任何已交付项目的测量。owner 首跑实际用的是 sonnet 上改了名的五原型模板，没有外行席也没有发现席，所以 owner 的两条信念都没被自己的运行检验过。首跑真正产生价值的是核查员。前三条结论置信度中高；"其余属于 folklore"置信度中。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) |
|---|---|---|---|---|---|---|
| 1 | Anthropic 唯一公开的多智能体实测配置是"最强模型做 lead、次强模型做 subagent"，并且是在约 15 倍 chat token 的代价下取得的；它没有测"每个 subagent 都用最强模型" | "outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval."（配置为 Opus 4 lead + Sonnet 4 subagents）；"multi-agent systems use about 15× more tokens than chats." | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H |
| 2 | 在 BrowseComp 上，花多少 token 是质量的主导变量；但模型代际升级比加倍预算更值 | "token usage by itself explains 80% of the variance"；"upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7." | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H |
| 3 | Anthropic 早期系统的浪费正是"席位太多 + 重复搜索"，修法是更详细的任务描述和按复杂度写死的规模规则 | "Early agents made errors like spawning 50 subagents for simple queries"；"subagents misinterpreted the task or performed the exact same searches as other agents."；"Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information."；"we embedded scaling rules in the prompts." | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H |
| 4 | Anthropic 开源的 lead prompt：默认 3 个 subagent，中等复杂度 3-5 个；最终报告禁止交给 subagent 写；要求在任务里写明可靠来源与起始来源 | "default to using 3 subagents for most queries."；"Medium complexity queries: 3-5 subagents"；"NEVER create a subagent to generate the final report"；"Suggested starting points and sources to use; define what constitutes reliable information"；"Prioritize original sources over news aggregators." | https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/patterns/agents/prompts/research_lead_agent.md | 无日期（2026-10-27 抓取；经 WebFetch 摘要模型，引文可能有出入） | primary | M |
| 5 | Anthropic 2026 年的复盘：按"角色"拆分的流水线在交接处丢上下文、协调成本高于干活成本；应按上下文边界拆分；多智能体通常是单智能体 token 的 3-10 倍 | "multi-agent implementations typically use 3-10x more tokens than single-agent approaches"；"they suffered from lost context at each handoff and spent more tokens coordinating than executing."；"Dividing by context boundaries means an agent handling a feature should also handle its tests." | https://claude.com/resources/articles/building-multi-agent-systems-when-and-how-to-use-them | 2026-01-23 | primary | H |
| 6 | LangChain 把"子代理并行写章节"拆掉了，因为报告前后不接；改成多代理只做研究、研究完再一次性写作 | "Earlier versions of our research agent wrote sections of the final report in parallel with sub-agents."；"the reports were disjoint because the section-writing agents were not well coordinated."；"We resolved this by using multi-agent for only the research task itself, performing writing after all research was done." | https://www.langchain.com/blog/open-deep-research | 2025-07-16 | primary | H |
| 7 | panel-skill 的成本史：第一次真跑约 25 个 subagent、数百万 token；最大的历史成本是"每条发现一个怀疑者"的扇出，后改为批量核查，light 档约 200K 成为默认 | "the first real run spun up ~25 subagents and ~millions of tokens"；"The dominant historical cost was a per-finding skeptic fan-out"；表格行 "\| `light` (default) \| ~6–8 \| ~200K \|" | https://raw.githubusercontent.com/zrabin/panel-skill/main/README.md | 无日期（仓库 5 commits，2026-10-27 抓取） | primary（作者自述，未见运行日志） | M |
| 8 | panel-skill 作者自认：短材料上单个前沿 agent 已经找全，面板的可测优势在核查与严重度校准；"一致则回炉"的机制实跑中很难触发；镜头是"批评模式"而非"专家人设" | "A frontier single agent saturates small and medium documents"；"on short inputs it finds essentially everything"；"The unanimity loop-back is hard to trigger live"；"Lenses are modes of critique, not subject-matter experts" | https://raw.githubusercontent.com/zrabin/panel-skill/main/README.md | 无日期（2026-10-27 抓取） | primary（作者自述；评审任务，不是联网研究） | M |
| 9 | 与之相反的做法（具体详细的人设、全员一致就重选）没有任何测量，只有示意数字 | "casts a small council of **specific, detailed people**"；"If every persona agrees, the cast was wrong and it re-casts."；仅有示意数字 "~60-140 tool calls, ~2-5 minutes"；"1 star"，"7 Commits" | https://github.com/Kanorin-chan/perspectives-skill | 无日期（2026-10-27 抓取） | primary（README，无运行数据） | M |
| 10 | 五原型模板是社区流行模板的谱系，不是测出来的：一个流传很广的免费 STORM skill 用的正是 practitioner / academic / skeptic / economist / historian，加"核查每个来源" | "spins up a practitioner, academic, skeptic, economist, and historian,"；"maps where they disagree, then verifies every source before handing you a clean HTML briefing." | https://www.skool.com/ai-automation-society/new-video-stanfords-method-turns-claude-into-a-phd-level-research-team | "Jun 29"（页面未显示年份） | primary（作者帖子；无测量） | M |
| 11 | 采用量最大的 Claude Code STORM 实现做的是"发现人设"，但同样没有公布测量 | 研究阶段 "Discovers research personas"；"596" stars；完成条件 "`research/sources.json` exists and has ≥1 entry" | https://www.skills.sh/fradser/dotclaude/storm-research | First Seen 2026-07-07（页面所示） | primary（registry 页） | M |
| 12 | Karpathy 的 llm-council 是"各自作答 + 匿名互评 + 主席汇总"，作者明说是周六玩具、不维护、不声称任何结果 | "the LLM identities are anonymized so that the LLM can't play favorites when judging their outputs."；"This project was 99% vibe coded as a fun Saturday hack"；"I'm not going to support it in any way" | https://github.com/karpathy/llm-council | 无日期（5 commits，2026-10-27 抓取） | primary | H |
| 13 | LLM 互评的排名与人的判断会分叉，互评不能当质量裁判 | "The models consistently praise GPT 5.1 as the best and most insightful model, and consistently select Claude as the worst model."；"the peer-generated rankings sometimes diverge from his own human assessment" | https://www.cxodigitalpulse.com/karpathys-llm-council-experiment-shows-gpt-5-1-leading-peer-based-ai-evaluations/ | 2025-11-24 | secondary（新闻转述 Karpathy 的推文，未追到原推） | M |
| 14 | 在 Claude Code 里，subagent 用哪个模型由优先级链决定；family 的两个 agent 定义没有 `model` 字段、SKILL.md 又禁止传 override，所以席位模型取决于环境变量或主会话，是偶然结果；嵌套默认开启，family 去掉 Agent 工具是必要的；撞到 maxTurns 的 subagent 可以续跑 | "1. The per-invocation `model` parameter. 2. The subagent definition's `model` frontmatter… 3. The `CLAUDE_CODE_SUBAGENT_MODEL` environment variable… 4. The main conversation's model."；"By default, a subagent can spawn subagents of its own, up to three layers below the main conversation."；"Claude Code returns its output marked as partial, and Claude can resume it to continue." | https://code.claude.com/docs/en/subagents | 2026-10-27 抓取（文档提到 v2.1.251） | primary | H |
| 15 | 已交付的 deep research 系统仍有大量"引用不支持的陈述"，引用准确率 40-80%，在有争议的问题上高度一边倒；这正是单独核查环节和强制怀疑席要解决的事 | "still exhibit large fractions of unsupported statements"；"with citation accuracy ranging from 40--80% across systems."；"remain highly one-sided on debate queries" | https://arxiv.org/abs/2509.04499v1 | 2025-09-02（ICLR 2026） | primary | H |
| 16 | owner 首跑：核查员 15/15 全查，5 条 PARTIAL、0 条 MISQUOTED；但其中两条按协议本该是 MISQUOTED（一条截断引文含义相反，一条引文"拼接自多句"），所以"MISQUOTED 不进 bottom line"这条硬规则一次都没触发，纠错全靠综合者手工照做 | verification.md #2 判定 "PARTIAL"，备注 "**lishid 引文被截断并改变了含义**"；#3 判定 "PARTIAL"，备注 "在页面中没有逐字对应(拼接自多句)"；协议原文 "Different is MISQUOTED. Absent is MISQUOTED." | /home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/verification.md | 2026-10-27 | primary（本地运行产物，n=1） | H |
| 17 | owner 首跑的阵容是 sonnet 上改了名的五原型（operator、sync-researcher、pricing-analyst、historian、skeptic），没有外行席也没有发现席；casting.md 里那份 Obsidian 示例阵容（CI 工程师外行 + LiveSync 维护者发现席）并没有真跑过 | report.md："standard 档 · 5 席（sonnet）+ 1 名核查员"；五席一句话只列这五席；seats 411,471 token（70K/73K/80K/81K/107K），verifier 70,560 | /home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/report.md | 2026-10-27 | primary（本地运行产物，n=1） | H |
| 18 | owner 首跑的席位在基础来源上重复劳动：同一份官方文档被五席都引用，obsidian-git 的 README 警告也是五席都引 | claims.md #1 "Relied on by": "operator, sync-researcher, pricing-analyst, historian, skeptic"；"obsidian-git README mobile warning (5 seats, verbatim)"；#8 被 4 席引用 | /home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/claims.md | 2026-10-27 | primary（本地运行产物，n=1） | H |

## My edge
- 我把首跑当运维事故来看，而不是当成功案例：核查员确实抓到了含义反转，但给它贴的是 PARTIAL 而不是 MISQUOTED（#16）。skill 里唯一的硬安全阀"MISQUOTED 不进 bottom line"因此没起作用，这次是综合者自己细心才没出事。下一次换一个不那么细心的 orchestrator，反转的引文就会进 bottom line。
- 模型选择这件事 skill 根本没有在控制（#14、#17）。"不传 model override"加上 agent 定义里没有 `model` 字段，意味着席位模型取决于 `CLAUDE_CODE_SUBAGENT_MODEL` 或主会话。owner 相信"最强模型值得"，可首跑是 sonnet，这条信念从来没生效过。
- token 浪费在哪里，交付过的人说法一致：每条发现一个核查员（#7）、子代理太多和重复搜索（#3）、重跑整组人。family 的 deep 档交叉质询要把 6-7 个席位全部再起一遍，正是第三种；首跑里五席都去找同一份官方文档，是第二种（#18）。
- 五原型的来路是社区流行模板（#10），不是证据；"按上下文边界拆分，而不是按角色拆分"（#5）才是 family 第 2 条规则"席位是证据标准而不是声音"的真正依据。这个依据写进 skill，比引 Zheng 2023 有用。
- 写报告的环节：Anthropic 禁止 subagent 写最终报告（#4），LangChain 把并行写章节拆掉了（#6）。family 的"研究和写作分开、一个人写"做对了，这一点不要在改版里丢掉。

## What the other seats will get wrong
- researcher 席会把 ChatEval 的"3-4 个角色最好"和 SPP 的"光有名字就够"直接搬来定席位数和卡片细节。那些是 2023 年 GPT-3.5/4 上不联网的辩论或评测任务；在联网研究流水线里，主导变量是 token（#2）。任何席位数对比如果不把总搜索预算固定住，测到的是预算，不是视角。
- skeptic 席会拿 Anthropic 的"Sonnet 做 subagent"去攻击"最强模型"这条信念，但多半不会注意到首跑本来就是 sonnet，而且 skill 没有固定模型（#14、#17）。真正该攻击的是"skill 没有实现这条信念，所以它从来没被检验过"。
- 几乎所有席位都会把首跑当作"发现席 + 外行席"有效的证据。首跑里这两种席位一个都没有（#17）；casting.md 的 Obsidian 示例是事后写的假想阵容。
- 引用 90.2% 的席位会把它读成"多智能体在同等成本下胜过单智能体"。那是 Anthropic 自己的内部评测，代价约 15 倍 token（#1），预算并不对等。

## What would change my mind
- 用 owner 自己的 skill 在 3 个以上问题上做预算对等的 A/B：模板阵容 vs 发现席 + 外行席阵容，总搜索数相同，按"只有一个席位找到且经核查成立的承重 claim 数"和 owner 标注的"我会据此行动"打分。如果外行席在多数运行里贡献至少一条这样的 claim，我会支持它保持强制。
- 同一问题，席位分别跑 Opus 和 Sonnet：如果核查员的降级率明显下降（比如 5/15 降到 1/15 以下），或者经核查的独有 claim 增加 30% 以上而成本不到两倍，那么"每席最强模型"值得。
- 一次 deep 档交叉质询的记录：如果它以"拿出新证据后让步"的方式（而不是改措辞）缩短了 crux 清单，且额外 token 不超过 30%，我会收回"应换成定向追问"的建议。

## Positions I hold without evidence
- 首跑的截断引文错误主要是"读"的错误而不是"搜"的错误，所以把最强模型放在核查员上，比放在每个席位上更划算。
- 外行席产出的 claim 来源离题更远，核查更难，会推高核查员负担；它带来的价值更可能落在"盲区"一节，而不是证据账本。
- 报告模板把"全体同意"放在"分歧"前面，会诱导综合者先写共识、往中间靠（发灰）。我没有数据。
- 在 roster 上加一个审批步骤（mediagato 的做法）能让用户发现漏掉的席位；没有测量。
- 250 词的返回上限大致合适，能让 orchestrator 的上下文保持足够小。

## Deliberately not examined
- hadufer/claude-storm、HirogaKatageri 的研究插件、mediagato/storm-research：两次搜索都没找到，预算内也没去直接抓 GitHub API，所以它们的 commit 历史（"拆掉了什么"）我没看。
- 卡片里提到的"Anthropic 在 Claude Code skills 仓库里的 deep-research skill"：没找到，我不能确认它存在。
- Cognition 的 "Don't build multi-agents" 原文：只看到 LangChain 一句转述。
- Reddit / HN 上这些 skill 的用户反馈：没有做 site:reddit.com 搜索。
- panel-skill 所引论文（ChatEval、SPP、Zheng）的原文：没有复核，留给 researcher 席。
- 第二模型席位（Codex）：没有任何证据。
- 首跑的五份席位笔记逐份阅读：只读了 brief、一张卡、claims、verification、report。
- Karpathy 的原推：只看到新闻转述。

## Proposed changes to the skill
| file | keep/change/add/remove | what | evidence |
|---|---|---|---|
| SKILL.md（Depth tiers，`quick`） | change | 把"3 席由 orchestrator 内联扮演、无核查"改成"内联做一次研究 + 1 个核查员只查前 5-8 条承重 claim"。有测量价值的是核查，不是多个内联人设。 | #8、#15、#16 |
| SKILL.md（Depth tiers，`standard`）与 casting.md（Headcount） | change | 默认席位数从"typically 5"改成 4（standard 区间 3-5，6 只给 deep）；总搜索预算保持不变（例如 4×12）。顺带修掉 casting.md 自己说"peak around three to four"却默认五席的矛盾。 | #2、#3、#4、#18；ChatEval 一点经 panel-skill 转引，未复核 |
| SKILL.md（Keeping the bill honest，最后一条） | change | "不要传 model override"改成显式固定：核查员用最强模型；席位默认 Sonnet 级（Anthropic 唯一实测过的配置）；把 owner 的"每席最强模型"当作一次对照实验来跑，而不是默认值。 | #1、#2、#14、#16、#17；分配方式本身是 judgment |
| ~/.claude/agents/family-verifier.md、family-member.md | add | 加 `model:` frontmatter，让模型不再取决于会话或环境变量。 | #14 |
| report-template.md（Cost） | change | cost 行写明每类 agent 的实际模型以及它是怎么定下来的（frontmatter / 环境变量 / 主会话）。 | #14、#17 |
| verifier-protocol.md（Per claim 第 2 步与标签表） | add | 写明：如果被引句子在同一条评论或同一段里紧接着被限定或反转，或者引文由多句拼接而成，判 MISQUOTED，不判 PARTIAL。可加子标签 MISQUOTED-INVERTED，让 bottom line 的硬规则真正生效。 | #16 |
| verifier-protocol.md（整体） | keep | 每次运行一个批量核查员；不要每条 claim 一个核查员。 | #7、#15 |
| casting.md（Move 2 外行席） | change | 从 "Mandatory" 改成"只有当类比能指出一个可以去搜的独立语料（某行业的复盘报告、验证统计）时才选，否则不选"；在上面的 A/B 跑出结果之前，标注为实验性。 | #5、#17；其余是 judgment |
| casting.md（Fitting the cast，Obsidian 示例） | change | 要么换成真正跑过的阵容，要么标注"假想阵容，并非实际运行"。 | #17 |
| casting.md（Cross-examination round，deep） | change | 不再把每个席位全部重起一遍；改成把前 3 条有争议的 claim 交给核查员的反证搜索，或者只重起顶层 crux 涉及的两个席位，每个最多 5 次搜索。 | #3、#5、#7、#8；判断成分较重 |
| SKILL.md（第 0 步 Frame）与 brief.md 模板 | add | brief 里加一节"Starting sources"：把选角那 1-2 次搜索找到的标准一手页面列进去，告诉席位不要重复去找，把预算花在 brief 里没有的东西上。 | #4、#18 |
| seat-protocol.md（Seat card file） | change | 保留 "Evidence you trust" 和 "first question"（任务细节是有证据支撑的那种细节）；"Who you are" 压缩成一句。理由引 #5（按上下文边界拆，不按角色拆）。 | #3、#4、#5、#8、#9 |
| SKILL.md（第 2 步，撞到上限的席位） | change | 撞到 maxTurns 的席位用 resume 续跑，不要从头重跑。 | #14 |
| SKILL.md（第 7 条规则）与 agents 的 tools 白名单 | keep | 不给 Agent 工具；Claude Code 默认允许三层嵌套。 | #7、#14 |
| SKILL.md（第 4 步 Synthesize） | keep | 所有实地研究结束后由一个综合者写报告，不让任何席位写报告章节。 | #4、#6 |
| SKILL.md（第 6 条规则，一致即选角失败） | keep | 只在报告里记一笔，不做自动重选循环。 | #8、#9 |
| report-template.md（cruxes 不按多数票裁决；Blind spots 永不为空） | keep | 已交付的研究 agent 在有争议的问题上一边倒。 | #15 |
| casting.md（Move 1 发现席） | keep（限 1 次搜索） | 成本低，采用量最大的 STORM skill 也这么做，但没有测量。它的主要产出应当是填进 brief 的 Starting sources。 | #11；judgment |

## Sources
1. https://www.anthropic.com/engineering/multi-agent-research-system — Anthropic, "How we built our multi-agent research system"：90.2%、15×、80% 方差、早期失败模式，2025-06-13
2. https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/patterns/agents/prompts/research_lead_agent.md — Anthropic 开源的 research lead prompt：subagent 数量规则、lead 自己写报告，无日期
3. https://claude.com/resources/articles/building-multi-agent-systems-when-and-how-to-use-them — Anthropic, "Building multi-agent systems: When and how to use them"：3-10x token、角色流水线失败、按上下文拆分，2026-01-23
4. https://www.langchain.com/blog/open-deep-research — LangChain, Open Deep Research：拆掉并行写章节，2025-07-16
5. https://raw.githubusercontent.com/zrabin/panel-skill/main/README.md — panel-skill README：成本史、局限、镜头设计，无日期（同时看了 https://github.com/zrabin/panel-skill）
6. https://github.com/Kanorin-chan/perspectives-skill — perspectives-skill README：详细人设、一致即重选、无测量，无日期
7. https://www.skool.com/ai-automation-society/new-video-stanfords-method-turns-claude-into-a-phd-level-research-team — 社区免费 STORM skill 的五原型帖子，"Jun 29"（年份不详）
8. https://www.skills.sh/fradser/dotclaude/storm-research — fradser/dotclaude 的 STORM skill registry 页：发现人设、596 stars，first seen 2026-07-07
9. https://github.com/karpathy/llm-council — Karpathy 的 llm-council README：三阶段、匿名互评、vibe-code 声明，无日期
10. https://www.cxodigitalpulse.com/karpathys-llm-council-experiment-shows-gpt-5-1-leading-peer-based-ai-evaluations/ — 新闻转述 Karpathy 的互评结果，2025-11-24
11. https://code.claude.com/docs/en/subagents — Claude Code subagents 文档：模型优先级、嵌套深度、maxTurns 部分输出与续跑，2026-10-27 抓取
12. https://arxiv.org/abs/2509.04499v1 — DeepTRACE（Venkit et al.，ICLR 2026）：deep research 引用准确率 40-80%、争议问题一边倒，2025-09-02
13. /home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/verification.md — owner 首跑的核查表，2026-10-27
14. /home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/report.md — owner 首跑的报告：阵容、模型、token，2026-10-27
15. /home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/claims.md — owner 首跑的 claims："Relied on by" 重复情况，2026-10-27

## Budget used
searches: 10 / 10 · fetches: 14
