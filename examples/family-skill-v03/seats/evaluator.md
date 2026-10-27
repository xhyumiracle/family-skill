# Seat: evaluator

## Core position
v0.3 最该改的是测量，编排排在后面。runs.log 和「每席独有核查通过 claim」都当不了 eval：这个数取决于编排者挑哪些 claim 去核查；round 1 把 PARTIAL 也算作通过，各席加起来是 11，报告正文却写 10；同一配置重跑，findings 大半会变。按 Miller 的功效计算，要分辨 3 分的差距大约需要 1000 题。一个预注册的 12-20 题 eval 只能看出大效应：模型档位大概率分得出（指标用席位盲抽样的引文忠实率），outsider 开关也许分得出，3/4/5 席基本分不出来，所以不该再调席位数。Co-STORM 去掉主持人后的差值很小，消融也没做显著性检验，因此只值得加一个轻量的补缺口步骤，放在核查之后、综合之前，并作为实验臂。核查预算 20 条保留。双轴判定从没在任何一次运行里用过，先记日志再说。模板里只有能机检的规则在起作用，而两份样例报告都违反了。置信度中等。

## Estimates
- (a) 编排者中途转向：部分赞成。fieldwork 期间不插话，席位继续盲写（round 1 已定）。核查之后、综合之前加一个「补缺口」步骤：最多 2 条，续跑一个席位，最多 4 次搜索，标为实验。依据：Co-STORM 主持人的机制是拿「没被引用的检索结果」去提问（#10），可它的消融差值不超过 0.36/5，也没有检验。
- (b) eval：用 12 题。8 题借 ResearchRubrics 的专家二值 rubric，4 题用 owner 自己的问题，跑之前写好 crux key。席位数的各臂从同一次 5 席盲笔记里取嵌套子集。分得开的指标有两个：席位盲随机抽样的引文忠实率，管模型档位；二值 rubric 加 crux 召回，管 outsider。3/4/5 席在 n≤20 时需要配对效应 d≳0.8 才看得出，预期分不开。
- (c) 20 条核查预算：净收益为正。round 1 的 3 条降级全落在第 14-18 位，预算砍到 12 条一条都抓不到（#16）。双轴：不确定，从未实际跑过（#16）。保留轴 1，另加一列二值的「能否进 bottom line」门槛；轴 2 的反证搜索只给厂商来源、数量和 crux 两侧的 claim。
- (d) 模板：部分承重。真正起作用的是能机检的几条：bottom line 对应 claim 号、crux 两侧各有来源并附 settle 行、盲区、未核查清单。两份样例按这些条目 lint 只得 6/9 和 5/10，规则写了但没人执行（#17）。「五席一句话」和席位指标是写给维护者看的，应移到附录。
- (e) 过度工程：删掉「runs.log 攒够 10-20 次就是 eval」这句话（#5 #8），也不再用「独有核查 claim 数」评 outsider（#15）。席位指标改成脚本计算的 leave-one-out（#14）。Seat estimates 表只在有 3 个以上可投票子问题、单元格能写成 yes/no/数字时才保留。

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Confidence (H/M/L) | Novel? |
|---|---|---|---|---|---|---|---|
| 1 | DeepResearch Bench 的 RACE 和人类的一致性来自「对照参考报告的相对评分」；维度权重、准则权重几乎不起作用；裸提示直接打分最差 | Table 2：RACE Full PAR 71.33，人类专家之间 68.44（"surpasses the inter-agreement rate observed among human experts"）；Vanilla Prompt 58.89；No Reference 66.56；No Weights 71.11；judge 每次查询约 $0.13（Gemini 2.5 Pro） | https://arxiv.org/html/2506.11763 | 2025-06（ICLR 2026） | primary | M（表格数字经 fetch 摘要转述） | yes |
| 2 | ResearchRubrics：二值判分比三值判分的人机一致性高约 20 个百分点；用 LLM 改写专家 rubric 会严重拉低一致性；报告越长得分越高 | "binary grading achieves substantial agreement (0.72–0.76 Macro F1"；"The shift from ternary to binary evaluation increases agreement by approximately 20 percentage points."；改写 rubric "catastrophically degrades alignment by 15-20%"；"longer responses generally achieve higher scores"（r≈0.24-0.28）；最好的系统 0.677（三值）/0.615（二值） | https://arxiv.org/html/2511.07685 | 2025-11（ICLR 2026） | primary | H | yes |
| 3 | LiveResearchBench：直接打 0-10 分和人类的一致性不到 60%，所以改用 checklist、逐条判分和配对；Claude 4 Sonnet 做 judge 一致性低，没进最终的 judge 组合；各系统差距最大的维度是引文关联（30.9-81.4） | "yielding less than 60% agreement with human judgments even when using SoTA LLM judges"；"Claude 4 Sonnet exhibited inconsistent and low agreement with human experts"；"multi-agent deep research systems (69.5) outperform both single-agent web (62.8)..." | https://arxiv.org/html/2510.14240v1 | 2025-10（ICLR 2026） | primary | H（各维度差距是 fetch 从 Table 1 算出来的，M） | yes |
| 4 | 和 #1、#3 冲突：配对判断比绝对分更容易被风格类干扰项带偏 | "Pairwise preferences flip in about 35% of the cases, compared to only 9% for absolute scores." | https://arxiv.org/abs/2504.14716v2 | 2025-04/08（COLM 2025） | primary | H | yes |
| 5 | 题量少的 eval 只能检出大效应：3 分的差距需要约 969 题；配对标准误和每题重采样都能降方差；几百个数据点以下 CLT 区间会严重低估不确定性 | "We therefore recommend using the paired version of the standard error estimate wherever practicable."；"new evals should contain at least 1,000 questions in order to have good signaling ability."；K=1→2 "the total variance is reduced by 1/3"；Bowyer 等："CLT-based methods perform very poorly, usually dramatically underestimating uncertainty" | https://arxiv.org/html/2411.00640 ; https://arxiv.org/abs/2503.01747 | 2024-11；2025-03（ICML 2025） | primary | H | yes |
| 6 | Anthropic 的研究系统一开始只用约 20 条查询做 eval，前提是早期效应很大；单次 LLM 调用、单个 prompt 的 judge 最一致；人工测试能抓到自动 eval 漏掉的问题 | "We started with a set of about 20 queries representing real usage patterns."；"A prompt tweak might boost success rates from 30% to 80%."；"...was the most consistent and aligned with human judgements."；"consistently chose SEO-optimized content farms over authoritative but less highly-ranked sources" | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | H | no（起始来源；但「20 题只够看大效应」这层读法是新的） |
| 7 | 同一个 lead 在两轮之间判断要不要补研究，但不在子代理跑的过程中插手：生产系统是同步分批的 | lead "decides whether more research is needed—if so, it can create additional subagents or refine its strategy"；"Currently, our lead agents execute subagents synchronously, waiting for each set of subagents to complete before proceeding." | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | primary | M（第一句是 fetch 摘要里带引号的片段） | no |
| 8 | 同一个 deep-research agent 重跑同一查询，findings 大半不同，引文也有近一半不同：单次运行之间的比较主要反映噪声 | Table 3 平均 total variance：findings 0.76，citations 0.44；"Findings (𝐁) exhibit substantially larger total variance than citations (𝐂)."；设置：20 题 × 10 次，Qwen3 backbone | https://arxiv.org/html/2602.23271v1 | 2026-02 | primary | M（系统和任务都和 family 不同） | yes |
| 9 | judge 重跑或换 judge 会让绝对分大幅漂移，排名却不变；合成质量和事实性的排名会互相错开；陈述越多，精确率越低 | "re-running the primary GPT judge three times ... yields Overall standard deviations of only 0.3 to 0.6 across systems, with identical rankings in every run"；"substituting Gemini ... inflates absolute scores by 13 to 17 points on Overall, yet the system ranking is perfectly preserved (Kendall's τ = 1.0)"；"rankings shift substantially across evaluation dimensions across systems"；图 5 注："a negative correlation between statement volume and precision" | https://arxiv.org/pdf/2603.28407 | 2026-03 | primary（作者评的是自家 MiroThinker，有利益关系） | M | yes |
| 10 | Co-STORM「去主持人比去多专家更伤」的差值小，消融行也没有显著性检验；主持人的机制是拿没被引用的检索结果去提问 | Table 3（1-5 分 autorater）：完整版、去多专家、去主持人三者 Depth 3.77/3.77/3.41，Relevance 3.78/3.73/3.56，Novelty 3.05/2.93/2.89，Unique URLs 6.04/5.91/5.67；† 只标 Co-STORM 对两个基线的比较；主持人从 "uncited sources retrieved since the last moderator turn" 生成问题 | https://arxiv.org/html/2408.15232 | 2024-08（EMNLP 2024） | primary | M（经 fetch 读表，请 researcher 席核对） | 部分 |
| 11 | DeepResearch Bench II 把 rubric 从专家文章里抽出来写成二值准则，judge 对人类的准确率约 92%；作者批评 LLM 自定准则 | "Each rubric is a binary criterion, typically phrased as a concrete factual or inferential requirement"；Table 5：Gemini-2.5-Pro accuracy 91.75 / F1 89.57（10 份报告的消融）；"even the strongest models satisfy fewer than 50% of the rubrics"；LLM 定义的准则 "can introduce systematic misalignment with human expert judgments" | https://arxiv.org/html/2601.08536 | 2026-01 | primary | H（92% 只来自 10 份报告） | yes |
| 12 | ResearchRubrics 的数据和评分代码公开，可以直接借来做 family 的外部 rubric：MIT 许可，HF 上需接受条款，实现的是二值判分，评一次很便宜 | "This project is licensed under the MIT License"；"Binary Grading (Current Implementation)"；"Place markdown reports in agent_responses/ directory."；"Approximately $0.01-$0.05 per rubric evaluation (Gemini 2.5 Pro pricing)" | https://github.com/scaleapi/researchrubrics ; https://huggingface.co/datasets/ScaleAI/researchrubrics | 2025-11 起（README 读于 2026-10） | primary | H | yes |
| 13 | LLM 搜索式事实核查和人工标注的一致度够当测量工具，成本低一个数量级以上 | "SAFE agrees with crowdsourced human annotators 72% of the time"；"on a random subset of 100 disagreement cases, SAFE wins 76% of the time"；"more than 20 times cheaper than human annotators" | https://arxiv.org/abs/2403.18802v2 | 2024-03 | primary | H（2024 年的 gpt-3.5 实现） | yes |
| 14 | 逐一移除某个 agent 的 leave-one-out 归因可以代替 Shapley 估计，也确实能找出几乎不贡献的 agent | "Leave-One-Out (LOO) attribution serves as a reliable proxy for more complex axiomatic estimators"（like Shapley and Banzhaf）；"while the QA Engineer exhibits negligible or negative marginal impact" | https://www.iclr.cc/virtual/2026/10016292 | 2026（ICLR 2026） | primary（只读到摘要） | M（任务是 MetaGPT 代码生成，层级式 MAS） | yes |
| 15 | round 1 的「outsider 独有核查通过 6 条」只反映编排者挑了哪些 claim，算法也不一致：tradecraft 是 #11-14、#18、#19 唯一的 Relied on by，其中 #14、#18 是 PARTIAL 也被计为通过；各席之和是 11，报告正文写 10；排序规则本身就偏向单一来源、出人意料的 claim | claims.md：#11-14、#18、#19 "Relied on by: tradecraft"；verification.md：#14、#18 PARTIAL；report.md："仅由一席产出的有 10 条，其中 6 条来自 tradecraft" 对比 "tradecraft 6 · researcher 2 · builder 1 · practitioner 1 · skeptic 1"；SKILL.md："Rank by diagnosticity first ..., then contested-between-seats, single-source, surprising, quantitative" | /home/xhyumiracle/projects/xhyu/family/family-skill-design/claims.md ; .../verification.md ; .../report.md ; /home/xhyumiracle/projects/xhyu/family-skill/skills/family/SKILL.md | 2026-10-27 | primary（本地产物） | H | yes |
| 16 | 核查员数据：靠后的预算仍能抓到降级；核查约占 15-20% 的 token；双轴判定从未执行过；round 1 的 7 次反证搜索一条反驳也没找到 | round 1：PARTIAL 在第 #14、#15、#18 位（共 20 条）；round 0：在第 #2、#3、#5、#6、#13 位（共 15 条）；核查员 118,860/606,291（19.6%），70,560/482,031（14.6%）；round 1 的 verification.md 只有一列 "Verdict"；#1-#7 的备注里是「未找到独立复现或反驳」一类 | /home/xhyumiracle/projects/xhyu/family/family-skill-design/verification.md ; /home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/report.md ; /home/xhyumiracle/projects/xhyu/family/runs.log | 2026-10-27 | primary（本地产物） | H | yes |
| 17 | 拿 10 条二值 lint 去评两份样例报告：Obsidian 6/9，round 1 只有 5/10。两份的 bottom line 都超过 5 句（7 句、6 句）；round 1 最后一句 caveat 没有 claim 号；round 1 四个 crux 只有 1 个有 settle 行；Obsidian 的 Crux 4 自己写着「双方都没有一手来源」 | Obsidian report.md Crux 4："双方都没有一手来源；B 面是推理"；round 1 report.md 只有 Crux 1 有「什么能解决它」；template："three to five sentences"、"a crux counts only when each side rests on different sources" | /home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/report.md ; /home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md ; /home/xhyumiracle/projects/xhyu/family-skill/skills/family/references/report-template.md | 2026-10-27 | primary（本地产物；打分是我做的） | H | yes |

## My edge
- 把两次运行的产物当数据读，没把它们当成故事：降级落在第几位、席位指标的加法、模板合规 lint。这几项都能从磁盘直接复核（#15 #16 #17）。
- 功效算术：12、15、20 题做配对符号检验，分别要赢 10/12、12/15、15/20 才达到 p<0.05（双侧，我自己算的）；配对 t 检验在 80% 功效下能检出的标准化效应大约是 0.9、0.8、0.7。所以 12-20 题只够回答「模型档位」这种大效应问题（#5 #6）。
- 席位盲写本来是质量规则，它还带来一个白送的实验设计：3/4/5 席、outsider 开关都可以从同一次 5 席运行的笔记里取子集，再重跑综合就行；claim 的判定只取决于 claim 和来源，各臂可以共用同一份核查（相当于共同随机数，去掉了核查员这一份方差）。和每臂单独跑相比，token 约降到 35-40%。
- judge 协议的取舍：二值判分比三值好（#2），绝对 0-10 分最差（#3），配对判断容易被风格带偏（#4）。family 各臂的报告都由同一个编排者写，风格干扰已经被控制住，所以配对加交换位置可以作为次要指标。

## What the other seats will get wrong
- 拿 runs.log 里的「tradecraft 6 条」当 outsider 有用的证据。这个数主要来自编排者挑了哪些 claim、算法前后不一致，题目又恰好贴近情报分析（#15）。
- 把 Co-STORM「去主持人更伤」当已经确立的结论，进而主张重写编排。表里的差值不超过 0.36/5，消融行没做显著性检验，而且是对话式系统，和 family 的并行盲写结构不同（#10）。
- 设计 eval 时用 LLM 生成 rubric、1-10 打分，或拿独立 URL 数比配置。前两种和人类一致性差（#2 #3 #11）。独立 URL 数会在质量不变时翻倍：round 1 的 #1/#2 里，STORM 去掉视角后大纲分 92.73→92.39，独立来源却是 99.83→54.36。
- 提议 3/4/5 席各跑一遍新的完整运行，花三倍预算，结果在 n≤20 时照样分不开（#5 #8）。

## What would change my mind
- 在 4 道题上把同一 5 席配置重跑一次，如果二值 rubric 合规率的运行间差异 <3 分、crux 召回几乎不变，那么席位数也许能分辨，可以把 3 vs 5 加进主 eval。
- owner 先标 20 条，拿 Claude 当 judge 做二值判分，如果 Macro F1 ≥0.75，就可以全用订阅、不接外部 API；如果低于 0.65（LiveResearchBench 的 Claude 4 Sonnet 结果指向这一边，#3），judge 必须换成 Gemini。
- 若出现带显著性检验的 Co-STORM 消融复现，或者 family 的 eval 显示补缺口步骤让 crux 召回或盲区关闭提升 ≥2 个/题，就把补缺口从实验升为默认。
- 如果前 5 次 v0.3 运行里轴 2 至少有一次给出 CONTRADICTED 或 CORROBORATED，并因此改动了 bottom line，就保留轴 2 的全部预算。

## Positions I hold without evidence
- outsider 那 6 条更多来自「题目贴近情报分析」，和「跨行业选角」关系不大。换一个远离情报分析的题目，这个数会掉。
- 在 family 里，题目之间的方差远大于 3/4/5 席之间的差异。
- 十分钟读者实际只读 bottom line、cruxes 和下一步；证据账本和五席一句话几乎没人读。
- 补缺口步骤通常花不到 100K token，多数时候能关掉排第一的盲区。round 1 漏掉的 Co-STORM 是一个现成例子：它在 verification.md 的 "Found but not cited" 里出现过，最后要专门跑一整轮去补。
- 在 Max 订阅上，22M 左右的 token 分两三周跑完，不会挤占 owner 的日常工作。官方额度没有一手来源，只能靠 /usage 百分比实测。
- MiroEval 里 Claude-Opus-4.6 是「Breadth 79.1 最高、Depth 58.8」，说明 Claude 子代理广而不深。这和 family 席位的表现一致，但只是一个厂商基准上的一个点。

## Deliberately not examined
- Co-STORM 内部机制和它的人评细节，归 researcher 席。我只读了消融表，用来判断效应大小。
- 双轴判定该怎么分级、Admiralty 式评级的文献，归 grade 席。我只从测量信度的角度表态（二值门槛）。
- 十分钟读者的阅读行为和报告写作规范，归 reader 席。我只评模板里哪些规则能机检。
- 订阅额度：官方没有公开数字，搜到的都是第三方汇总，所以没有进 claims 表。
- 跨语言判分：ResearchRubrics 的题是英文，family 默认输出中文。我建议 eval 运行设成英文输出，但没查过中文报告对英文 rubric 判分的一致性。
- DeepResearch Bench 的 50 道中文题能不能直接拿来用：RACE 要用参考报告，又偏好长文，和 family 刻意不写长文的定位冲突（#1 #2 的长度相关），所以只记下没深挖。
- 迭代式补检索的其他文献（TTD-DR、WebWeaver 等），以及 Claude judge 的自我偏好。

## Proposed changes to the skill
| file | keep/change/add/remove | what | evidence row # or "judgment" |
|---|---|---|---|
| SKILL.md | remove | 删掉 step 5 的 "After ten or twenty runs that log is the eval this skill does not otherwise have." runs.log 降级为成本和健康日志，另加一行指向 `references/eval.md` | #5 #8 #15 |
| SKILL.md | change | step 4 的席位指标先给 "verified" 下定义：轴 1 为 PRIMARY 或 SECONDARY-CONFIRMED，PARTIAL 单独计数。指标由编排者跑一个小脚本，从 claims.md 和 verification.md 算出，不再手算。去掉 "they are the only cheap evidence of whether a seat earned its budget" 这句 | #15 |
| SKILL.md | add | 新增 step 3.5「补缺口」（实验，quick 档关闭）：核查完成后，编排者从各席的 "Deliberately not examined" 和核查员的 "Found but not cited" 里挑最多 2 条，标准是「若成立会改 bottom line」；续跑其中一席，最多 4 次搜索，补到的 claim 在报告里标 [UNVERIFIED]，或者在预算允许时交给核查员复核。席位在 fieldwork 期间不受干预 | #7 #10，judgment |
| SKILL.md | change | step 3 写 claims.md 时，"Relied on by" 列用席位代号（S1..S5），不写席位名和 outsider 标记，让核查员看不出 claim 出自哪一席。在优先级清单之外，每席再随机抽 1 条 claim 进核查，用来无偏估计各席的忠实率 | #15，judgment |
| SKILL.md | change | step 4 的 bottom-line check 改成一张 6 条二值 lint，结果打在 Cost 行（"lint 6/6"）：≤5 句；每句有 claim 号或 [UNVERIFIED]；没有 MISQUOTED/CIRCULAR；每个 crux 两侧都有来源；每个 crux 都有 settle 行；盲区非空 | #17 #2 |
| SKILL.md | keep | standard 档核查 20 条，以及「不拿核查预算换席位」 | #16 #13 |
| verifier-protocol.md | keep | 轴 1 的标签，以及 MISQUOTED（INVERTED/STITCHED）硬规则 | #16（round 0 有两条翻转原意被标成 PARTIAL） |
| verifier-protocol.md | change | 输出表加一列二值的 "Bottom-line eligible (Y/N)"，由两个轴推出。eval 测核查员重跑一致性时只看这一列，不比细标签 | #2，judgment |
| verifier-protocol.md | change | 轴 2 的反证搜索默认只做三类：厂商或利益相关来源、数量型 claim、crux 两侧。每次运行把 CORROBORATED、CONTRADICTED、CANNOT-JUDGE 的计数写进 runs.log；5 次运行后若轴 2 从没改动过 bottom line，就把它降为备注列 | #16 |
| verifier-protocol.md | change | "Downgrades by seat" 改为按代号统计，由编排者映射回席位名 | #15 |
| report-template.md | keep | Bottom line → claim 号、Crux（两侧来源 + settle + lean）、Blind spots、Evidence ledger 精简版、Not verified | #17 |
| report-template.md | change | "The seats, one line each" 和 Seat metrics 移出正文，放到 Cost 之后的附录（或者只写进 runs.log）；这些是给维护者看的 | judgment，#15 |
| report-template.md | change | Seat estimates 的单元格只能写 yes/no/unsure 或数字；可投票的子问题少于 3 个时省略整张表 | #17（round 1 表里的单元格是散文） |
| casting.md | change | outsider 的去留不再看 runs.log 里的「独有核查 claim」，改看 eval 里 outsider 开关这一臂，以及从笔记子集做的 LOO 结果 | #14 #15 |
| casting.md | keep | standard 默认 4 席、上限 5。补一句：在 ≤20 题的 eval 上分不出 4 和 5，别拿单次运行去调席位数 | #5 #8 |
| seat-protocol.md | change | claims 表每行加一个稳定 ID（如 S2-04），一路带进 claims.md 和 verification.md，脚本算指标和 LOO 才有可能 | judgment |
| references/eval.md（新增） | add | 预注册 eval，规格见下方列表 | #1-#6 #8 #9 #11-#14 |

eval.md 规格要点（所有 rubric 和 crux key 都在第一次运行之前写好，冻结后不再改）：
- 题目共 12 道。8 道取自 ResearchRubrics：专家写的二值 rubric，MIT 许可，判分代码现成（#12），挑有争议、有两方文献的题。4 道用 owner 的真实问题，每题写 15-25 条二值 rubric，另写 2-4 条 crux key（「报告指出分歧 X，并且两侧各有来源」）。不用 LLM 改写 rubric（#2 #11）。eval 运行统一用英文输出。
- 各臂怎么构造。每题按每个模型档位跑一次 5 席 fieldwork（opus 一次，sonnet 一次），各臂从这份盲写笔记里取子集：5 席；去掉 outsider 的 4 席；LOO（每次去掉一个非 skeptic 席位）；3 席。各档位把全部 claim 的并集只核查一次，各臂共用判定；每个臂只重跑综合。总量约为每题 1.0M（fieldwork）+ 0.24M（核查）+ 8×0.07M（综合）≈ 1.8M，12 题约 22M token。每臂单独跑完整运行约 58M。成本按 runs.log 的实测数推算。
- 主指标及其用途。模型档位看 M1：席位盲随机抽样的 claim 忠实率，即「能进 bottom line」的比例（#13 #16）。席位数和 outsider 看 M2：二值 rubric 合规率，以及 crux key 召回。次要指标：同一编排者写出的两份报告做配对偏好，交换位置后取平均（#1 #4）。不要用 0-10 绝对分、三值判分、独立 URL 数（#2 #3）。
- 统计方法。全部做配对比较，用精确或 Bayesian 区间，不用 CLT（#5）。12 题时某一臂要赢 ≥10 题才算分出差异。另抽 4 道题，把整套流程原样重跑一次，估计同一配置的运行间方差（#8）。只报排名和配对差，跨 judge 的绝对分不能比（#9）。
- judge。正式开跑前，owner 手标 20 条 rubric 判定。Claude（订阅）的二值 Macro F1 ≥0.75 就用 Claude；否则改用 Gemini 2.5 Pro，每条 $0.01-0.05（#3 #12）。
- 停止规则（预先写好）。若 3 席对 5 席在 M2 上分不出差异，standard 档固定为 4 席，以后不再调。若 outsider 开关在 M2 和 crux 召回上都分不出，outsider 从默认开启改为可选。

## Sources
1. https://arxiv.org/html/2506.11763 ：DeepResearch Bench（RACE/FACT，Table 2 消融，judge 成本），2025-06，ICLR 2026
2. https://arxiv.org/html/2511.07685 ：ResearchRubrics 论文（二值和三值判分的一致性、rubric 改写、长度相关），2025-11，ICLR 2026
3. https://github.com/scaleapi/researchrubrics ：ResearchRubrics 评分代码 README（MIT、二值判分、单价），读于 2026-10
4. https://huggingface.co/datasets/ScaleAI/researchrubrics ：ResearchRubrics 数据集（需接受条款），2025-11
5. https://arxiv.org/html/2510.14240v1 ：LiveResearchBench（DeepEval 各协议的人机一致性，Claude judge 一致性低），2025-10，ICLR 2026
6. https://arxiv.org/abs/2504.14716v2 ：Tripathi 等，Pairwise or Pointwise（35% vs 9% 翻转），COLM 2025
7. https://arxiv.org/html/2411.00640 ：Miller，Adding Error Bars to Evals（配对标准误、969 题、重采样），2024-11
8. https://arxiv.org/abs/2503.01747 ：Bowyer 等，Don't Use the CLT with fewer than a few hundred datapoints，ICML 2025
9. https://www.anthropic.com/engineering/multi-agent-research-system ：Anthropic 多智能体研究系统（约 20 题起步、judge、同步执行、lead 决定是否补研究），2025-06-13
10. https://arxiv.org/html/2602.23271v1 ：Evaluating Stochasticity in Deep Research Agents（findings TV 0.76、citations TV 0.44），2026-02
11. https://arxiv.org/pdf/2603.28407 ：MiroEval（judge 重跑和换 judge 的稳定性、维度间排名错位、陈述量与精确率负相关），2026-03
12. https://arxiv.org/html/2408.15232 ：Co-STORM（Table 3 消融、主持人机制），EMNLP 2024
13. https://arxiv.org/html/2601.08536 ：DeepResearch Bench II（专家文章派生的二值 rubric、judge 准确率），2026-01
14. https://arxiv.org/abs/2403.18802v2 ：SAFE，Long-form factuality（72% 一致、76% 胜、便宜 20 倍以上），2024-03
15. https://www.iclr.cc/virtual/2026/10016292 ：Lu、Huang、Lee，Agent That Matters（LOO 可代替 Shapley），ICLR 2026
16. https://arxiv.org/abs/2510.02190 ：Dr. Bench 摘要（看过，没有人机一致性数据，未进入 claims 表），2025-10/2026-01
17. 本地：/home/xhyumiracle/projects/xhyu/family/family-skill-design/{report.md, claims.md, verification.md}，round 1 产物，2026-10-27
18. 本地：/home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/report.md，round 0 报告，2026-10-27
19. 本地：/home/xhyumiracle/projects/xhyu/family/runs.log，两次运行的指标，2026-10-27
20. 本地：/home/xhyumiracle/projects/xhyu/family-skill/skills/family/{SKILL.md, references/*.md}，v0.2.0，2026-10-27

## Budget used
searches: 10 / 12 · fetches: 17（其中 5 次是起始来源，不挂在搜索下；MiroEval PDF 落盘后在本地读了 11 页）· stopped because: done（证据已够回答 (a)-(e)；订阅额度那次搜索没有一手来源）
