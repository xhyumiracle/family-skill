<p align="center"><b>English</b> · <a href="README.zh-CN.md">简体中文</a></p>

<div align="center">

# family

**Got a question? Get the family first.**

A multi-perspective research skill based on Stanford's STORM. Five members research your question<br>independently from five perspectives, every claim is checked against its source, and you get a sourced report.

<img src="assets/hero-en.gif" alt="family demo: ask one question, five members research it, every source is checked, you get a conclusion" width="100%">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-standard-green)](https://agentskills.io)
[![Version](https://img.shields.io/badge/version-0.6.1-blue)](CHANGELOG.md)
[![Tested on](https://img.shields.io/badge/tested%20on-Claude%20Code-f97316)](#install)

[Install](#install) · [Usage](#usage) · [How it works](#how-it-works)

<sub><i>"I don't have friends. I got family."</i><br>Dominic Toretto</sub>

</div>

## When to use it

- You're new to a field and want the full picture fast.
- You want to know whether a claim, or a wave of hype, holds up.
- You're about to make a call and want to know what you've missed.

For single facts, long-form writing, or picking between A and B for you, other tools fit better.

## Install

**Tell your agent:**

```text
Install this skill: https://github.com/xhyumiracle/family-skill
```

**Or use the Agent Skills installer:**

```bash
npx skills add xhyumiracle/family-skill -g
```

**Or, on Claude Code, the full install:**

```bash
git clone https://github.com/xhyumiracle/family-skill && ./family-skill/install.sh
```

The full install adds two agent definitions that cannot spawn subagents, so the family stays the size you see. Start a new session afterwards.

Needs an agent with subagents and web search. Tested on Claude Code; Codex, Cursor, Gemini CLI and OpenCode support subagents too and should work.

<!-- Agents installing this for someone: on Claude Code use the full install (install.sh); on any other runtime use the npx line. -->

## Usage

```
/family <question>          five members + a fact-checker · ~30 min · ~650K tokens
/family quick <question>    one fast pass, still fact-checked · ~80K tokens
/family deep <question>     the same five, more claims checked, extra rounds on disagreements (up to 3)
```

Or just say it: "help me understand X from scratch", "is the hype about X real", "what am I missing about X".

You get `family/<short-name>/report.md`. It opens with three lines: what to do, how confident to be, and which assumption would change the answer. Below that: key findings, where the members disagree, and what nobody looked into, each with its source.

## How it works

```mermaid
flowchart LR
  Q([your question]) --> B["background brief<br/>facts and constraints only"]
  subgraph crew ["five members, each searching alone"]
    direction TB
    S1["first-hand"]
    S2["expert"]
    S3["stakes"]
    S4["dissent<br/>(the only one told your view)"]
    S5["outside view"]
  end
  B --> S1 & S2 & S3 & S4 & S5
  S1 & S2 & S3 & S4 & S5 --> V["check every cited source"]
  V --> E{"disagreement?<br/>one more round"}
  E --> R["report<br/>with all sources"]
```

The five members split the work by where the evidence comes from, so the set fits any question: a product, a policy, history, science, a personal decision.

| Perspective | Who | Basis |
|---|---|---|
| First-hand | the people closest to the evidence: users, participants, the team that ran the experiment; for history, the contemporary sources | argument from position to know (Walton et al., 2008) |
| Expert | people who can explain how and why | argument from expert opinion; the "expert" role in Critical Systems Heuristics (Ulrich, 1983) |
| Stakes | people who decide, pay, benefit, or bear the consequences; when a question has no stakeholders, a second research method takes this seat | the beneficiary, decision-maker and affected roles in Critical Systems Heuristics (Ulrich, 1983) |
| Dissent | the strongest published case against the prevailing answer in the field; works on questions with no stance | minority dissent widens a group's thinking (Nemeth, 1986); real dissent corrects better than an assigned devil's advocate (Nemeth et al., 2001); one dissenting answer reduces LLM conformity to a majority (Zhu et al., ACL 2025) |
| Outside view | someone from another field that has handled the same kind of problem, bringing how comparable cases usually turned out | the outside view and reference-class forecasting (Kahneman & Lovallo, 1993; Flyvbjerg, 2006); untested in AI research, so marked experimental |

- **Complementary views.** Together the five triangulate in the qualitative-research sense: different data sources, different lenses, independent investigators (Denzin, 1978). In STORM's experiments, asking from several perspectives nearly doubled the distinct sources found (99.83 vs 54.36).
- **Five is enough.** Averaging three analysts' independent judgments already captures most of the gain of averaging fifty (Mandel et al., 2018), and Delphi panels of 3 to 11 show no difference in accuracy (Rowe & Wright, 2001). Multi-agent research shows the same: identical agents saturate quickly, and two diverse agents matched sixteen identical ones (Yang et al., 2026). Each extra person only adds cost, about 70–110K tokens.
- **Members are picked per question.** Each perspective gets one or two candidates written for your question, and the one most relevant and least like the others is kept. Teams generated from the query and chosen for relevance and diversity together beat predefined roles, and either criterion alone did worse (AgentInit, EMNLP 2025).
- **Independent work, one merge.** The gains from AI agents debating are almost entirely explained by voting (Choi et al., NeurIPS 2025), and working alone avoids conformity.
- **Your view goes only to the dissent member.** Everyone else gets facts only, so nobody bends toward you (Sharma et al., ICLR 2024).
- **Faithful citations.** Deep-research tools cite correctly 40–80% of the time (DeepTRACE, ICLR 2026). The fact-checker opens every key source and downgrades claims the source doesn't support. Numbers and quotes in the conclusion are then matched word for word against the fact-checker's table, since a 2026 study traced 84.7% of report errors to the orchestrating agent that writes the final report.
- **One more round on disagreements.** Each side sees the other's checked evidence anonymously and can hold with a new source, concede, or show the two define a term differently. It stops when the evidence stops changing (the Delphi method).
- **Cost counts alongside quality.** Steps that cost more without doing better were cut, such as multi-round debate and a sixth member (the cost–accuracy Pareto view of Kapoor et al., 2024).

A full run, every intermediate file included: [`examples/family-skill-design/`](examples/family-skill-design/), family reviewing its own design. The evidence behind each choice: [docs/DESIGN.md](docs/DESIGN.md).

## References

- Shao et al. *Assisting in Writing Wikipedia-like Articles From Scratch with LLMs* (STORM). NAACL 2024. [arxiv.org/abs/2402.14207](https://arxiv.org/abs/2402.14207)
- Jiang et al. *Into the Unknown Unknowns* (Co-STORM). EMNLP 2024. [arxiv.org/abs/2408.15232](https://arxiv.org/abs/2408.15232)
- Choi, Zhu, Li. *Debate or Vote: Which Yields Better Decisions in Multi-Agent LLMs?* NeurIPS 2025. [arxiv.org/abs/2508.17536](https://arxiv.org/abs/2508.17536)
- Zheng et al. *When "A Helpful Assistant" Is Not Really Helpful.* EMNLP Findings 2024. [arxiv.org/abs/2311.10054](https://arxiv.org/abs/2311.10054)
- Venkit et al. *DeepTRACE.* ICLR 2026. [arxiv.org/abs/2509.04499](https://arxiv.org/abs/2509.04499)
- Kim et al. *Towards a Science of Scaling Agent Systems.* 2025. [arxiv.org/abs/2512.08296](https://arxiv.org/abs/2512.08296)
- *Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research.* 2026. [arxiv.org/abs/2608.24306](https://arxiv.org/abs/2608.24306)
- Sharma et al. *Towards Understanding Sycophancy in Language Models.* ICLR 2024. [arxiv.org/abs/2310.13548](https://arxiv.org/abs/2310.13548)
- Nemeth, Brown, Rogers. *Devil's advocate versus authentic dissent.* Eur. J. Soc. Psychol. 2001.
- Tian et al. *AgentInit: Initializing LLM-based Multi-Agent Systems via Diversity and Expertise Orchestration.* EMNLP 2025 Findings. [arxiv.org/abs/2509.19236](https://arxiv.org/abs/2509.19236)
- Yang et al. *Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity.* 2026. [arxiv.org/abs/2602.03794](https://arxiv.org/abs/2602.03794)
- Zhu et al. *Conformity in Large Language Models.* ACL 2025. [aclanthology.org/2025.acl-long.195](https://aclanthology.org/2025.acl-long.195)
- Nemeth. *Differential contributions of majority and minority influence.* Psychological Review 1986.
- Walton, Reed, Macagno. *Argumentation Schemes.* Cambridge University Press 2008.
- Ulrich. *Critical Heuristics of Social Planning.* 1983. [summary by the author](https://i2insights.org/2022/05/24/critical-systems-heuristics/)
- Kahneman, Lovallo. *Timid choices and bold forecasts.* Management Science 1993.
- Flyvbjerg. *From Nobel Prize to project management: getting risks right.* Project Management Journal 2006.
- Schwenk. *Effects of devil's advocacy and dialectical inquiry on decision making: a meta-analysis.* OBHDP 1990.
- Denzin. *The Research Act.* 1978.
- Kapoor et al. *AI Agents That Matter.* TMLR 2025. [arxiv.org/abs/2407.01502](https://arxiv.org/abs/2407.01502)
- Lee et al. *"Fact-checking" fact checkers.* HKS Misinformation Review 2023.
- Rowe, Wright. *Expert opinions in forecasting: the role of the Delphi technique.* 2001.
- Mandel, Karvetski, Dhami. *Boosting intelligence analysts' judgment accuracy.* Judgment and Decision Making 2018.
- Intelligence Community Directive 203, *Analytic Standards.* 2015, rev. 2023.
- Rosenbaum, Glenton, Oxman. *Summary-of-findings tables in Cochrane reviews improved understanding and rapid retrieval of key information.* J Clin Epidemiol 2010.
- Miller. *Adding Error Bars to Evals.* 2024. [arxiv.org/abs/2411.00640](https://arxiv.org/abs/2411.00640)
- Anthropic. *How we built our multi-agent research system.* 2025. [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system)

<sub>MIT · similar projects read first: claude-storm, storm-research, panel-skill, perspectives-skill, dotclaude · stills from *Fast Five*, Universal Pictures</sub>
