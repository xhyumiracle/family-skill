# 多视角研究管线（STORM 式）的六个设计选择，哪些有证据、哪些是 folklore，以及 `family` skill 该怎么改

standard 档（核查预算加到 20）· 5 席 + 1 名核查员 · 2026-10-27 · 本次运行目录：`projects/xhyu/family/family-skill-design/`

## Bottom line

六个设计选择里，有对照或生产级测量支撑的是三个：席位之间独立、盲写，研究结束后由一个人综合（#7、#8、#20）；一个单独的来源核查步骤（#8、#10、#16，加上本 skill 两次运行的降级记录）；以及「预算是主变量」，每席的搜索次数比席位数更决定质量（#9）。角色生成方式、席位数、卡片详略、deep 档的交叉质询，没有任何在开放式研究上的同预算对照（#1、#5、#6 都是别的任务上的窄结果）。STORM 自己的消融说明「视角」对大纲质量几乎没贡献（92.73 vs 92.39，无显著性检验），它可测的作用是让独立来源数接近翻倍（99.83 vs 54.36），承重的是「读完再追问」的检索循环（#1、#2）；人评的 +10% 覆盖度在 20 对样本上 p=0.084（#3）。人设本身不让单个 agent 更准（#4、#5），所以席位的意义是「去不同地方搜」而不是「扮演谁」。情报界的教训与此一致：被实测的结构化技术（ACH）没提高准确度，有效的是独立估计后的聚合和带理由的匿名反馈（#11、#18），指派的 devil's advocate 不如真实异见（#12），把 owner 的信念写进所有席位共读的 brief 是锚定通道（#19）。最大 caveat：以上证据几乎都来自 2023-2025 年的模型和封闭答案任务，迁移到今天的开放式研究属推断；而这个 skill 到目前为止没有自己的 eval，两条 owner 信念都还没被它自己检验过。

## Belief vs. finding

- **信念 1（跨行业 outsider + 发现席优于固定五原型）**：文献里没有对照实验，正反都没有（#5 的「动态优于固定」基线太弱，不能算支持）。本次运行的席位指标偏向 outsider：核查通过的 20 条 claim 里，仅由一席产出的有 10 条，其中 6 条来自 tradecraft（outsider）席，且这一席带来了报告里三条最不显而易见的改法（信念不进 brief、核查分两轴、加聚合步）。n=1，而且这个题目恰好离情报分析很近，不能外推。
- **信念 2（每席最强模型值得）**：Anthropic 实测的配置是 Opus 主控 + Sonnet 子代理，不是每席最强（#9）；「换代际比翻倍 token 收益大」是跨代际的比较，不是同代 Opus vs Sonnet（#9）；越强的模型错误越相关（#14，单数据集）。本 skill 的两次运行：sonnet 席位那次 15 条里 5 条降级、2 条翻转；opus 席位这次 20 条里 3 条降级、0 条翻转。方向支持信念 2，但题目不同、n=1，只是提示。最有支撑的是「最强模型放在综合和核查上」。

## 五席都同意的

- **独立盲写 + 一人综合**。Debate or Vote（NeurIPS 2025）：多智能体辩论的收益大部分来自多数投票，辩论本身不提高期望正确率（#7，PRIMARY-CONFIRMED，四席独立引用同一篇）；Kim et al.：无中心核查的独立并行 agent 把错误放大 17.2 倍，中心化 4.4 倍（#8）；LangChain 拆掉了并行写章节，Anthropic 的 lead prompt 禁止子代理写最终报告（未占核查预算，两席逐字一致）。
- **核查步骤是证据最硬的部件**。生产级 deep-research 系统引用准确率 40-80%、争议问题一边倒（#10，四席引用）；MAST 1600+ 条轨迹里验证缺失或错误占 17%，加任务目标级验证 +15.6%（#16）。本 skill 自己两次运行的降级率 5/15 和 3/20。
- **席位是搜索领地，不是人设**。SPP 里详细人设档案不加分、名字就够（#5）；Zheng v3：system prompt 里的人设不提升，自动挑人设不比随机好（#4）；STORM 视角的实测效果是独立来源翻倍（#2）；Anthropic：子代理需要的是「目标、输出格式、工具与来源指引、边界」（#9），2026 年的复盘说按角色切分的流水线在交接处丢上下文，应按上下文边界切分（#20）。五席来源独立，是收敛不是回声。
- **搜索预算是质量旋钮，席位数只是花预算的方式**。BrowseComp 上 token 用量单独解释 80% 方差（#9）。
- **skill 里的两处引文错了**：规则 2 写的「Zheng et al. 2023」在 2023 年的 v1 结论相反（v1 原话 "consistently improves"），负面结论出自 2024-10 的 v3（#4）；ChatEval 的 agent 不检索，不能用来支持「角色让模型搜不同地方」（#6）。
- **上一轮核查的硬规则没触发**：截断翻转原意的引文被标成 PARTIAL 而不是 MISQUOTED，「MISQUOTED 不进结论」这条保险靠综合者手工兜底（practitioner 读了上一轮的 verification.md）。
- **skill 不测量自己**。五席都提出了同一组指标：每席独立 URL 数、席位间重叠、仅由一席产出且核查通过的 claim 数、单 agent 基线。

## Seat estimates

| 子问题 | builder | tradecraft | researcher | practitioner | skeptic | 分布 |
|---|---|---|---|---|---|---|
| (a) 角色生成：模板 / 发现 / 跨行业 | 未测，outsider 作实验臂 | 异质专家优先，outsider 保留但只带规则不估数 | 发现有近邻证据，outsider 未测 | 模板是社区谱系，outsider 仅当有可搜语料 | 领地不是人设，outsider 可选 | 5/5「未测」；4/5 保留 outsider 带约束 |
| (b) 席位数 | 由 eval 定，4×15 vs 6×10 | 3-11 无差别，别凑数 | 4-6，经验判断 | 4 | 3 | 中位 4，总预算固定 |
| (c) 卡片详略 | 来源指引承重，人设一行 | 卡片保持短 | 名字够，细节写去哪搜 | Who you are 一句 | 人设一行 | 5/5 一致 |
| (d) 盲写 vs 辩论 | 盲写；交叉质询改定向再检索 | 盲写；匿名带理由，一轮 | 盲写；交叉质询移到核查后、让步须引证据 | 盲写；只重起顶层 crux 两席 | 盲写；删交叉质询 | 5/5 盲写；4/5 改造而非删除 |
| (e) 独立核查 | 保留 + 高层检查 | 保留，拆两轴 | 保留，CoVe 式因子化 | 保留，收紧 MISQUOTED | 保留，预算 25-30 | 5/5 保留并加强 |
| (f) 模型与预算 | 预算主变量；席位 Sonnet 档 | 每席最强会加剧错误相关 | 最强给编排与综合 | 显式分层，核查员最强 | 最强给核查员 | 5/5「最强模型先给核查/综合」；席位层 3/5 倾向次一档 |

## 分歧（cruxes）

### Crux 1：模型放哪里，以及 skill 该不该写
- **A 面**（builder、practitioner）：在 agent 文件里显式写模型：席位 Sonnet 档、核查员和编排最强；否则席位模型取决于环境变量，信念 2「从来没生效过」。
- **B 面**（owner 的规则；tradecraft、researcher 部分支持）：skill 不提模型；席位全上最强会加剧错误相关（#14），应把最强给综合与核查。
- **证据**：#9（Anthropic 用 Sonnet 子代理，PRIMARY）、#15（Claude Code 文档「Use Sonnet for teammates」，PRIMARY；7x 只在 plan mode，PARTIAL）、#14（错误相关 60%，单数据集，PARTIAL）。注意 #9、#15、#20 都出自 Anthropic，不互相独立。
- **什么能解决它**：同一题目、同一核查员下 Sonnet 席 vs Opus 席的 A/B，看降级率和独有核查通过 claim 数。
- **当前倾向**：skill 文本保持不提模型（owner 的决定，且与 B 面一致）；模型用 settings 控制。核查员发现 `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` 可以让该环境变量压过一切，这让「skill 不提模型」和「席位用 opus」可以同时成立。

### Crux 2：outsider 席强制、可选，还是实验
- **A 面**（当前 casting.md：Mandatory）。
- **B 面**（skeptic、builder、practitioner）：无任何对照证据，设计类比研究对远类比的质量结论偏负（skeptic 的两条只见 snippet，L），改为可选或实验臂。
- **C 面**（tradecraft、researcher）：异质专家优先是 Delphi 的原则性建议（#18：核查员指出这是推理出的原则，不是实证），保留但约束：只带本行规则，不估目标领域数量，其 claim 同样核查，并用席位指标追踪。
- **证据**：本次 tradecraft 席 6 条独有核查通过 claim（n=1）。
- **当前倾向**：C 面：默认开启、roster 标「experimental」、只有类比指向可搜语料时才选、报告记录它的独有贡献。

### Crux 3：默认席位数
- 3（skeptic）/ 4（practitioner）/ 4-6（researcher）/ eval 定（builder）/ 3-11 无差别（tradecraft，#18 PRIMARY 的那部分）。
- **当前倾向**：standard 档 3-5、默认 4，总搜索预算固定；6 只在 deep。ChatEval 的「3-4 最佳」是 ChatGPT 在一个评测基准上 60→62.5（#6），不能当依据。

### Crux 4：deep 档的交叉质询，删还是改
- **删**（skeptic：#7 辩论不提高期望正确率）vs **改**（researcher、builder、tradecraft：移到核查之后、匿名、让步必须引新证据）。
- **证据**：核查员补充 #7 的同一篇论文还报告「把信念更新偏向纠错的干预能提升辩论效果」，这支持改造而不是删除；Delphi 的「带理由」反馈条件提升最大（#18）。
- **当前倾向**：改。

## 盲区

- **Co-STORM 的主持人消融**：核查员在搜索摘要里看到「去掉主持人比砍专家更伤」，没人打开。这直接关系到编排者（综合者）的角色比席位更重要这一假设。
- **RAPID**：有第三方在人评里胜过 STORM，没人看。
- **2024 年后模型上的 persona / 辩论 / 谄媚结果**：#4、#5、#6、#19 全是 2023 年代模型；SPP 自己说人设效应依赖模型能力。
- **本 skill 没有 eval**：五席都指出；没有单 agent 基线，没有席位边际贡献记录。本次是第一次算席位指标。
- **owner 的成本模型**：订阅额度而非现金，席位并行所以砍席位省不了墙钟时间；skeptic 自己承认这削弱了「15 倍 token」的论点。
- **第二模型席**：没有任何证据；#14 说跨厂商错误相关。
- **非 Anthropic 的生产系统消融**（OpenAI/Perplexity/Google deep research）：预算内没找到公开数字。
- 以上盲区中，Co-STORM 主持人消融若成立，会把改进重点从席位转向编排者；其余不改变 bottom line。

## 证据账本

| # | Claim（短） | 判定 | 权重 | 原始来源 |
|---|---|---|---|---|
| 1 | STORM Table 3：去视角 92.73→92.39，去对话→88.75 | PRIMARY-CONFIRMED | = | arxiv.org/html/2402.14207 |
| 2 | STORM Table 5：独立来源 99.83 / 54.36 / 39.56 | PRIMARY-CONFIRMED | = | 同上 |
| 3 | STORM 人评：coverage p=0.084，organization p=0.005，20 对 | PRIMARY-CONFIRMED | = +10% 是「≥4 分比例」之差 | 同上 |
| 4 | Zheng et al. v1 与 v3 结论反转 | PRIMARY-CONFIRMED | = v1 原话 "consistently improves" | arxiv.org/abs/2311.10054 |
| 5 | SPP：动态人设优于固定；详细档案不加分 | PRIMARY-CONFIRMED | = | arxiv.org/html/2307.05300v3 |
| 6 | ChatEval：同角色=单 agent 53.8，多样 60，3-4 角色 62.5；不检索 | PRIMARY-CONFIRMED | = | arxiv.org/pdf/2308.07201 |
| 7 | Debate or Vote：投票占大部分增益，辩论不提高期望正确率 | PRIMARY-CONFIRMED | = 同篇还说纠错偏向的更新有效 | arxiv.org/abs/2508.17536 |
| 8 | Kim et al. 17.2x vs 4.4x；+80.8% / -70% | PRIMARY-CONFIRMED | = 版本间数字略异 | research.google 博客；arxiv 2512.08296 |
| 9 | Anthropic：Opus 主控 + Sonnet 子代理 90.2%；token 解释 80% 方差；换代 > 翻倍预算 | PRIMARY-CONFIRMED | = | anthropic.com/engineering/multi-agent-research-system |
| 10 | DeepTRACE：引用准确率 40-80% | PRIMARY-CONFIRMED | = | arxiv.org/abs/2509.04499v1 |
| 11 | Mandel 2018：ACH 无效（0.21 vs 0.26）；3 人平均拿到大部分收益 | PRIMARY-CONFIRMED | = | cambridge.org JDM 13(6) |
| 12 | Nemeth 2001：真实异见优于三种 devil's advocate | PRIMARY-CONFIRMED | = 「bolstering」一句属其早期研究 | DOI 10.1002/ejsp.58 |
| 13 | Kelly 2025：可信赖度评分更取决于来源可靠性而非信息可信度 | PRIMARY-CONFIRMED | = | cambridge.org JDM 20 e36 |
| 14 | Kim ICML 2025：两模型同错时 60% 同一错答案 | PARTIAL | ↓ 仅一个排行榜数据集 | arxiv.org/abs/2506.07962v1 |
| 15 | Claude Code 文档：Sonnet for teammates；7x；嵌套三层；模型优先级 | PARTIAL | ↓ 7x 仅 plan mode；FORCE=1 可强制 | code.claude.com/docs |
| 16 | MAST：验证类失败 17%；任务目标验证 +15.6% | PRIMARY-CONFIRMED | = | arxiv.org/html/2503.13657v3 |
| 17 | Tran & Kiela 2026：等 token 下单 agent 不输多 agent（多跳推理） | PRIMARY-CONFIRMED | = | arxiv.org/abs/2604.02460v1 |
| 18 | Rowe & Wright：Delphi 5:1（两平）；带理由反馈最有效；3-11 人无差别 | PARTIAL | ↓ 平局数；「异质专家优先」是原则非实证 | gwern.net/doc/.../2001-rowe.pdf |
| 19 | Sharma 2023：用户暗示错误答案使准确率最多降 27% | PRIMARY-CONFIRMED | = 2023 模型、QA 任务 | arxiv.org/pdf/2310.13548 |
| 20 | Anthropic 2026：多 agent 3-10x token；按上下文边界切分 | PRIMARY-CONFIRMED | = 与 #9、#15 同源不独立 | claude.com/resources/articles/... |

未进入核查预算：LangChain 并行写作割裂；Gao 2025 增益递减；Self-MoA；Artificial Hivemind；BrowseComp 64 采样 +15-25%；Opus 4.6 BrowseComp 84.0 vs 86.8（snippet）；GJP 2014 / 2025 重分析；Dhami 2019 ACH；近远类比设计研究（snippet）；各 skill README；Anthropic cookbook lead prompt；上一轮运行的本地产物。

## 五席一句话

- **builder**（discovered）：只有预算、模型代际、「独立并行 + 中心核查」有生产级测量；skill 没有 eval 所以什么都证伪不了；席位搜同一个问题是把 Anthropic 的「重复劳动」当成了设计。核查：#8、#9、#16 全部成立。
- **tradecraft**（outsider）：ACH 实测无效、聚合有效；指派异见不如真实异见；信念进 brief 是锚定；核查员混淆了来源可靠性与 claim 可信度。核查：#11-#14、#18-#19 成立，两处措辞修正。独有核查通过 claim 6 条，全席最多。
- **researcher**：STORM 承重的是对话不是视角；skill 两处引文错；盲写有 2025 年从众研究支持；交叉质询应移到核查后。核查：#1-#7、#10 成立。
- **practitioner**：三条有「踩坑后改」支撑；上一轮核查的 MISQUOTED 规则没触发；上一轮根本没跑过 outsider 和发现席，信念 1 没被检验。核查：#15 PARTIAL（7x 限 plan mode）、#20 成立。
- **skeptic**：只有「分派到不同来源」和「核查」有硬证据；+10% coverage 不显著；最便宜的管线是一强 agent + 2-3 中档席 + 双倍核查预算。核查：#3、#17 成立；它对 outsider 的两条设计研究只有 snippet。

## 下一步

- 已按共识改写 skill（见 SKILL.md v2）：规则 2 引文修正、信念只给 skeptic、席位卡改为「领地 + 边界」、默认 4 席、核查两轴 + MISQUOTED 收紧 + 预算 20、交叉质询改为核查后的匿名反馈、quick 档改为「一次研究 + 小核查」、报告加 Estimates 表和席位指标、runs.log。
- 模型：settings 里用 `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` 强制 opus（owner 决定），skill 不提模型。
- 等 10-20 次运行的 runs.log 积累后，再回头定席位数和 outsider 的去留；在那之前这两条都标「实验」。
- 值得补读：Co-STORM 主持人消融（arXiv 2408.15232）。

## Cost

seats: 5（opus，本会话显式传参）· searches: 50 / 50（seats）+ 10（verifier）· fetches: 71（seats）+ 38（verifier）· claims checked: 20 / 20 listed · agents spawned: 6 · tokens: 606,291 subagent（seats 487,431：builder 107K / practitioner 106K / researcher 94K / tradecraft 93K / skeptic 88K；verifier 118,860）· wall time: 约 30 分钟
Seat metrics: unique URLs：builder 15 · practitioner 15 · researcher 13 · skeptic 16 · tradecraft 12；shared across ≥2 seats：Anthropic 博文（5 席）、Debate or Vote（4）、DeepTRACE（4）、Kim scaling（3）、STORM（2）、Claude Code 文档（2）；verified claims only one seat produced：tradecraft 6 · researcher 2 · builder 1 · practitioner 1 · skeptic 1
Not verified: 「未进入核查预算」清单 11 项；盲区全部。
