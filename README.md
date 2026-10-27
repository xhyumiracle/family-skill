# family

> "I don't have friends. I got family." — Dominic Toretto

<img src="assets/banner.jpg" alt="" width="100%">

Get the family together before the job. A Claude Code skill that researches one question with a crew of independent seats, then sends a fact-checker to open every source they leaned on.

English · [中文](README.zh-CN.md)

```
/family  What in this skill's own design has evidence behind it, and what is folklore?
```

```mermaid
flowchart LR
  Q([your question]) --> B["brief<br/>facts and constraints,<br/>none of your opinions"]
  B --> C["cast 3-5 seats<br/>each owns one<br/>evidence territory"]
  subgraph crew ["crew: parallel, blind to each other"]
    direction TB
    S1["practitioner"]
    S2["researcher"]
    S3["outsider from<br/>an unrelated trade"]
    S4["skeptic: hunts<br/>published dissent"]
  end
  C --> S1 & S2 & S3 & S4
  S1 & S2 & S3 & S4 --> G{"gaps?<br/>send a seat<br/>back out"}
  G --> V["verifier<br/>opens every cited source,<br/>4 verdicts"]
  V --> R["report<br/>bottom line · 7 key judgments<br/>cruxes · blind spots"]
```

## Install

```bash
git clone https://github.com/xhyumiracle/family-skill && ./family-skill/install.sh
```

Claude Code with subagents and web search. Start a new session after installing. No model is named anywhere; seats run on your subagent default.

## Use

```
/family <question>          3-5 seats + verifier · ~25 min · ~700K tokens
/family quick <question>    no crew: the orchestrator searches alone, a small verifier checks it
/family deep <question>     6 seats · bigger verifier · evidence rounds until the cruxes stop moving (max 3)
```

Or just ask: "what am I missing about X", "从0到1了解 X". Output lands in `family/<slug>/report.md`.

## What you get

First screen for a ten-minute reader, appendix for audit.

| | |
|---|---|
| Bottom line | what to do · how likely, on a seven-level scale with a range · the assumption that would break it |
| Key judgments | at most seven, each with its strongest confirmed source and what would change it |
| Cruxes | where seats disagree, both sides sourced, what would settle it |
| Blind spots | what nobody looked at |
| Source summary | what the evidence is made of, and the rows the verifier downgraded |

## Highlights

- **A fact-checker opens every source the conclusion rests on.** Four verdicts, two flags, and a quote inverted by truncation counts as misquoted. The best-evidenced part of the pipeline.
- **One seat comes from an unrelated trade.** Cast by structural analogy (CI engineers for bots and humans on one repo; intelligence tradecraft for independent estimators). Marked experimental, kept because it keeps finding the blind spot.
- **The skeptic is the only seat that knows what you believe**, and it goes looking for published dissent, not for objections of its own.
- **Seats work blind and never argue.** Agreement between seats of one model is conformity, not evidence.
- **The orchestrator's own bottom line is checked word by word** against the verification table before you see it.
- **First screen in ten minutes, audit below the fold.** Three-slot bottom line on a seven-level likelihood scale, at most seven key judgments, cruxes with what would settle them.
- **It audited itself twice**, and v0.3 is what the audits produced.

Design rationale and the evidence behind each choice: [docs/DESIGN.md](docs/DESIGN.md).

## It audited itself

[`examples/family-skill-v03/`](examples/family-skill-v03/): five seats (a benchmark author, a ten-minute reader, a GRADE methodologist, a researcher, a skeptic) read v0.2.0 and the literature; the verifier opened 20 sources. They found structure that had never run, seat metrics with a selection bias, and a stitched number in the orchestrator's own bottom line. v0.3.0 is the result.

## Not for

Picking A or B for you (it lays out the evidence; the choice is yours) · single facts · long articles · cheap research.

## References

The ones the design leans on most; the full list with page-level notes is in [docs/DESIGN.md](docs/DESIGN.md).

- Shao et al. *Assisting in Writing Wikipedia-like Articles From Scratch with LLMs* (STORM). NAACL 2024. [arxiv.org/abs/2402.14207](https://arxiv.org/abs/2402.14207)
- Jiang et al. *Into the Unknown Unknowns* (Co-STORM). EMNLP 2024. [arxiv.org/abs/2408.15232](https://arxiv.org/abs/2408.15232)
- Choi, Zhu, Li. *Debate or Vote: Which Yields Better Decisions in Multi-Agent LLMs?* NeurIPS 2025. [arxiv.org/abs/2508.17536](https://arxiv.org/abs/2508.17536)
- Zheng et al. *When "A Helpful Assistant" Is Not Really Helpful.* EMNLP Findings 2024. [arxiv.org/abs/2311.10054](https://arxiv.org/abs/2311.10054)
- Venkit et al. *DeepTRACE.* ICLR 2026. [arxiv.org/abs/2509.04499](https://arxiv.org/abs/2509.04499)
- Kim et al. *Towards a Science of Scaling Agent Systems.* 2025. [arxiv.org/abs/2512.08296](https://arxiv.org/abs/2512.08296)
- *Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research.* 2026. [arxiv.org/abs/2608.24306](https://arxiv.org/abs/2608.24306)
- Sharma et al. *Towards Understanding Sycophancy in Language Models.* ICLR 2024. [arxiv.org/abs/2310.13548](https://arxiv.org/abs/2310.13548)
- Nemeth, Brown, Rogers. *Devil's advocate versus authentic dissent.* Eur. J. Soc. Psychol. 2001.
- Lee et al. *"Fact-checking" fact checkers.* HKS Misinformation Review 2023.
- Mandel, Karvetski, Dhami. *Boosting intelligence analysts' judgment accuracy.* Judgment and Decision Making 2018.
- Intelligence Community Directive 203, *Analytic Standards.* 2015, rev. 2023.
- Rosenbaum, Glenton, Oxman. *Summary-of-findings tables in Cochrane reviews improved understanding and rapid retrieval of key information.* J Clin Epidemiol 2010.
- Miller. *Adding Error Bars to Evals.* 2024. [arxiv.org/abs/2411.00640](https://arxiv.org/abs/2411.00640)
- Anthropic. *How we built our multi-agent research system.* 2025. [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system)

MIT · prior art read first: claude-storm, storm-research, panel-skill, perspectives-skill, dotclaude · stills from *Fast Five*, Universal Pictures
