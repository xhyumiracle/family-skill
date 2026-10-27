<p align="center"><a href="README.md">English</a> · <b>简体中文</b></p>

<div align="center">

# family

<sub>「我没有朋友，我只有家人。」· 唐老大，《速度与激情》</sub>

<img src="assets/hero-zh.gif" alt="family：五个不同行当的人各查各的，再由核查员点开他们引用的每个链接" width="100%">

**一个问题，叫五个不同行当的人各查各的，<br>再派个核查员，把他们引用的链接挨个点开看。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-standard-green)](https://agentskills.io)
[![Version](https://img.shields.io/badge/version-0.5.0-blue)](CHANGELOG.md)
[![Tested on](https://img.shields.io/badge/tested%20on-Claude%20Code-f97316)](#安装)

[看效果](#看效果) · [安装](#安装) · [怎么运作](#怎么运作) · [设计依据](docs/DESIGN.md)

</div>

## 为什么要这么折腾

- **只从一个角度查，来源只找得到一半。** STORM 做过消融：从多个视角提问，每个主题平均找到 99.83 个不同来源；去掉多视角，只剩 54.36 个。
- **AI 调研给的引用，只有 40% 到 80% 站得住。** 这是 DeepTRACE（ICLR 2026）测各家 deep research 得出的数。
- **family 自己也记账。** 四次真实运行，核查员一共点开 78 条引用，有 17 条原文并没有完全说过那句话，进报告之前就被降了权。

## 看效果

### 它会叫来谁

问「没有糖尿病，戴动态血糖仪有用吗？」，选角这一步的原样输出：

| | 家人 | 为什么找这个人 |
|---|---|---|
| 用它的 | 戴过三个月 Stelo 或 Lingo 的健康用户 | 固定席 |
| 做它的 | 做代谢健康门诊的内分泌科医生 | 固定席 |
| 赌它的 | 投消费级医疗器械的 VC | 固定席 |
| 挑刺儿的 | 写 [JAMA Internal Medicine 那篇「无证据」综述](https://doi.org/10.1001/jamainternmed.2026.2772)的那类循证医学研究者 | 固定席，找的是真发表过的反方 |
| 外援 | 研究筛查过度诊断的流行病学家 | 跟 PSA 筛查是一个结构：把医疗传感器卖给健康人，噪声读数被当成诊断 |

### 核查员抓到过什么

一次真实运行里的一条（[verification.md](examples/family-skill-design/verification.md) 第 14 行）：

> **家人写的：**「两个模型都答错时，约 60% 会给出同一个错误答案。」
>
> **原文**（[arxiv.org/abs/2506.07962](https://arxiv.org/abs/2506.07962)）："*on one leaderboard dataset*, models agree 60% of the time when both models err."
>
> **PARTIAL ↓** 原文说的是「在一个排行榜数据集上」，不是普遍规律。进报告之前就被降了权。

### 拿它审它自己

[`examples/family-skill-v03/`](examples/family-skill-v03/) 是拿这个 skill 去查它自己的设计。核查员点开了 20 个来源，查出三件事：上一版新加的结构压根没跑过；每个家人贡献多少的计数有选择偏差；编排者自己写的结论里，有个数字是从两个不同实验里拼出来的。v0.3 就是这么改出来的。

## 安装

**直接跟你的 agent 说**，哪个 runtime 都行：

```text
帮我安装这个 skill：https://github.com/xhyumiracle/family-skill
```

**或者用 Agent Skills 通用安装器：**

```bash
npx skills add xhyumiracle/family-skill -g
```

**或者在 Claude Code 里完整安装：**

```bash
git clone https://github.com/xhyumiracle/family-skill && ./family-skill/install.sh
```

完整安装会多装两个 agent 定义，`family-member` 和 `family-verifier`。它们手里没有开子代理的工具，所以你批准了几个人，就只花几个人的钱。装完开个新会话。（替人安装的 agent：Claude Code 上用完整安装，其他环境用 `npx` 那行。）

需要能开子代理、能联网搜索。在 Claude Code 上测过。Codex、Cursor、Gemini CLI、OpenCode 都有子代理，按理能跑，但还没测。没有子代理的环境只能跑 `quick`。文件里没写任何模型名，每个家人都用你的默认模型。

## 用法

```
/family <问题>          5 个家人 + 核查员 · 约 30 分钟 · 约 65 万 token
/family quick <问题>    不叫家人，自己查一遍，再让小核查员核一遍
/family deep <问题>     还是这五个人 · 多核几条 · 证据轮一直跑到分歧不再变（最多 3 轮）
```

不想记命令就直接说：「从 0 到 1 了解一下 X」「X 的 hype 是真的吗」「关于 X 我还漏了什么」。报告在 `family/<slug>/report.md`。

## 怎么运作

```mermaid
flowchart LR
  Q([你的问题]) --> B["brief<br/>事实和约束，<br/>不带你的观点"]
  B --> C["叫齐家人"]
  subgraph crew ["家人各查各的，互相看不到"]
    direction TB
    S1["用它的"]
    S2["做它的"]
    S3["赌它的"]
    S4["挑刺儿的<br/>（唯一知道你怎么想的人）"]
  end
  O["从八竿子打不着的行业<br/>拉来的一个人"]:::far
  C --> S1 & S2 & S3 & S4
  C -. "谁解决过同样结构的问题？" .-> O
  S1 & S2 & S3 & S4 & O --> V["核查员<br/>逐个打开引用来源"]
  V --> E{"证据轮<br/>直到分歧不再动"}
  E --> R["报告<br/>结论 · 关键判断 · 分歧 · 盲区"]
  classDef far fill:#fff3cd,stroke:#d4a017,stroke-width:2px
```

- **干活的时候谁也不跟谁说话。** 同一个模型扮的几个人意见一致，那叫从众，不叫证据，所以每个家人都是闷头自己查。
- **只有挑刺儿的知道你怎么想。** 它的活是去找已经发表的反方，不是自己编反驳。
- **外援看问题的结构去找。** 机器人和人往同一个 repo 提交，就去找 CI 工程师；一群人各自估计再汇总，就去找情报分析员。这一条标了「实验性」。
- **「再深入讨论一下」是证据轮，不是吵架。** 分歧双方匿名拿到对方核实过的证据，只能三选一：拿新来源坚持、点名哪条证据说服了自己而让步、或者指出其实是定义不同。证据不再变就停，不是等大家意见一致。
- **编排者自己写的结论，要逐字对着核查表过一遍**，然后才给你看。

每条设计背后是哪篇论文：[docs/DESIGN.md](docs/DESIGN.md)。

## 报告长什么样

第一屏给只有十分钟的人看，审计材料都在后面。

| | |
|---|---|
| 结论 | 该做什么 · 有多大可能（七级刻度，带数字区间）· 哪个假设一倒结论就倒 |
| 关键判断 | 最多七条，每条附最硬的来源，以及什么情况下它会变 |
| 分歧 | 哪几个家人在哪儿不一致，两边都有出处，什么能解决 |
| 盲区 | 没人查过的地方 |
| 来源总评 | 证据是什么成色，核查员降了哪几条 |

## 它不干什么

替你选 A 还是 B（证据摆给你，选是你的事）· 查一个事实 · 写长文 · 省钱。

## 参考文献

设计上最依赖的几篇，完整清单和逐页说明见 [docs/DESIGN.md](docs/DESIGN.md)。

- Shao et al. *Assisting in Writing Wikipedia-like Articles From Scratch with LLMs*（STORM）. NAACL 2024. [arxiv.org/abs/2402.14207](https://arxiv.org/abs/2402.14207)
- Jiang et al. *Into the Unknown Unknowns*（Co-STORM）. EMNLP 2024. [arxiv.org/abs/2408.15232](https://arxiv.org/abs/2408.15232)
- Choi, Zhu, Li. *Debate or Vote: Which Yields Better Decisions in Multi-Agent LLMs?* NeurIPS 2025. [arxiv.org/abs/2508.17536](https://arxiv.org/abs/2508.17536)
- Zheng et al. *When "A Helpful Assistant" Is Not Really Helpful.* EMNLP Findings 2024. [arxiv.org/abs/2311.10054](https://arxiv.org/abs/2311.10054)
- Venkit et al. *DeepTRACE.* ICLR 2026. [arxiv.org/abs/2509.04499](https://arxiv.org/abs/2509.04499)
- Kim et al. *Towards a Science of Scaling Agent Systems.* 2025. [arxiv.org/abs/2512.08296](https://arxiv.org/abs/2512.08296)
- *Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research.* 2026. [arxiv.org/abs/2608.24306](https://arxiv.org/abs/2608.24306)
- Sharma et al. *Towards Understanding Sycophancy in Language Models.* ICLR 2024. [arxiv.org/abs/2310.13548](https://arxiv.org/abs/2310.13548)
- Nemeth, Brown, Rogers. *Devil's advocate versus authentic dissent.* Eur. J. Soc. Psychol. 2001.
- Lee et al. *"Fact-checking" fact checkers.* HKS Misinformation Review 2023.
- Mandel, Karvetski, Dhami. *Boosting intelligence analysts' judgment accuracy.* Judgment and Decision Making 2018.
- Intelligence Community Directive 203, *Analytic Standards.* 2015，2023 修订.
- Rosenbaum, Glenton, Oxman. *Summary-of-findings tables in Cochrane reviews improved understanding and rapid retrieval of key information.* J Clin Epidemiol 2010.
- Miller. *Adding Error Bars to Evals.* 2024. [arxiv.org/abs/2411.00640](https://arxiv.org/abs/2411.00640)
- Anthropic. *How we built our multi-agent research system.* 2025. [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system)

<sub>MIT · 动手前读过：claude-storm、storm-research、panel-skill、perspectives-skill、dotclaude · 剧照来自《速度与激情5》，Universal Pictures</sub>
