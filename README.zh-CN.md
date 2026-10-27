# family

**先组队，再干活。** 一个 Claude Code skill：对一个问题派出一组互相独立的席位，每席去证据的不同角落搜，最后派一名核查员把结论依赖的每个来源逐个打开核对。

名字来自《速度与激情》唯一的规矩：活不能一个人干，先把 family 叫齐。梗到此为止。

```
/family:family  Obsidian 库在「VM 上 agent 直接写文件、人在笔记本和手机上编辑」时，
                各种同步方案到底会怎么坏？
```

二十分钟后得到 `report.md`：每句话都对应一条核查过的 claim 的 bottom line、全席共识、带双方证据的分歧、没人查的盲区、带判定标签的证据账本。[`examples/`](examples/) 里有两次真实运行，其中一次是把这个 skill 对准它自己。

## 它做什么

1. **Frame**：一句话问题、约束、已知事实、起始来源。你自己的观点不进共读的 brief。
2. **Cast**：三步选角。先从这个领域已有的综述里发现证据领地（它的 issue tracker、它的监管文书、它的那个会议）；再从一个解决过同构问题的无关行业拉一个 outsider；剩下的从五个原型里补（从业者、研究员、市场、历史学家、怀疑论者）。怀疑论者必选，是唯一知道你信什么的席位，任务是找已发表的最强反方。
3. **Fieldwork**：每席一个子代理，独立上下文、固定搜索预算、固定笔记格式，互相看不到。它们不能再派人：agent 定义里没有 Agent 工具。
4. **Verify**：一名核查员拿到承重 claim 清单（不是笔记），逐个打开引用页，追到一手来源，找独立的第二来源，两轴判定。
5. **Synthesize**：等所有席位结束，一个人写报告。

三档：`quick`（一次行内调研 + 小核查）、`standard`（3-5 席 + 核查员，约 50 万 token、20 分钟）、`deep`（最多 6 席、更大的核查预算、一轮匿名反馈）。

## 安装

需要带子代理和联网搜索的 Claude Code。二选一：

**作为 plugin**（skill 是 `/family:family`，agent 一起装上）：

```
/plugin marketplace add xhyumiracle/family-skill
/plugin install family@family-skill
```

**复制进 `~/.claude`**（skill 是 `/family`）：

```bash
git clone https://github.com/xhyumiracle/family-skill && ./family-skill/install.sh
```

装完开新会话；agent 定义在会话启动时读取。

skill 里不写模型。席位和核查员用你的子代理默认模型（settings 里的 `CLAUDE_CODE_SUBAGENT_MODEL`，没有就是会话模型）。

## 用法

直接说你想搞清楚什么就会触发：「从0到1了解 X」「组个队研究一下」「X 的 hype 是真的吗」。或者 `/family:family <问题>`。加 `quick` 或 `deep` 选档，默认 `standard`。派人之前会先打印席位表和代理数。

产物都在工作目录的 `family/<slug>/`：`brief.md`、`roster.md`、`cards/`、`seats/`、`claims.md`、`verification.md`、`report.md`。每次运行在 `family/runs.log` 追加一行。

## 为什么这么设计

多角色 skill 大多是 folklore。我们只保留有证据的部分，并且说清楚哪些是、哪些不是。完整账本在 [`docs/DESIGN.md`](docs/DESIGN.md)，概要：

| 设计选择 | 证据 | 做法 |
|---|---|---|
| 席位独立、一人写报告 | agent 之间辩论的收益主要来自对独立答案投票（NeurIPS 2025）；并行写章节在 LangChain 产出割裂的报告 | 盲写；编排者写报告 |
| 单独的核查步骤 | deep-research 系统引用准确率 40-80%（DeepTRACE）；无中心核查的并行 agent 把错误放大 17 倍 | 一名批量核查员、两轴判定、「MISQUOTED 不进结论」硬规则 |
| 席位是搜索领地不是人设 | STORM 自己的消融：视角对大纲质量几乎没贡献，但让独立来源翻倍；人设细节不如一个名字（SPP）；system prompt 里的人设不提升准确率（Zheng et al. 2024） | 卡片写去哪搜、留什么给别人，人物只一句 |
| 用户信念不进 brief | 提示里的信念把答案拉过去（Sharma et al.） | 只给怀疑论者看 |
| 怀疑论者找已发表的异见 | 真实异见胜过所有形式的指派 devil's advocate（Nemeth 2001） | 第一任务是找谁带证据反对过 |
| 每席搜索次数优先于席位数 | Anthropic 的研究系统里 token 预算解释 80% 的方差；三个独立估计取平均已拿到大部分收益（Mandel 2018） | 默认 4 席，先加搜索再加席位 |
| outsider 席、发现席、反馈轮 | 没有对照研究 | 默认开启、标注实验、每次运行记录席位指标 |

## 它不是什么

不是决策工具（它画地图，A 还是 B 请用决策框架）。不是查单个事实的。不写长文。不便宜：一次 standard 大约是一轮对话的十五倍 token。不是神谕：一个模型的五个席位共享同一套先验，测得出的价值大半在核查那一步。

## 例子

- [`examples/obsidian-agent-vault-sync/`](examples/obsidian-agent-vault-sync/)：第一次真实运行（5 席，15 条核查，5 条降级，其中 2 条含义翻转）。
- [`examples/family-skill-design/`](examples/family-skill-design/)：用这个 skill 审它自己。五席（outsider 是情报分析方法论者）读 skill 文件和文献，20 条核查，17 条一手来源确认。0.2.0 就是这么来的。

## 致谢

STORM：Shao et al., NAACL 2024。组队的想法来自一篇小红书帖子里的五角色 prompt 和电影比喻。动手前读过的同类项目：hadufer/claude-storm、mediagato/storm-research、zrabin/panel-skill、Kanorin-chan/perspectives-skill、fradser/dotclaude。

MIT。
