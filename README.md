# family

**Assemble the crew before the job.** A Claude Code skill that researches one question with a crew of independent seats, each sent to a different part of the evidence, then sends a fact-checker to open every source the crew leaned on.

The name is the one rule of the *Fast & Furious* franchise: you do not do the job alone, you get the family together first. That is the whole reference. We promise.

```
/family:family  How do the realistic sync options for an Obsidian vault behave when an AI agent
                writes to it on a server while a human edits from a laptop and a phone?
```

Twenty minutes later you get `report.md`: a bottom line where every sentence maps to a checked claim, what every seat agreed on, the cruxes with both sides' evidence, the blind spots nobody looked at, and an evidence ledger with verdicts. Two real runs are in [`examples/`](examples/), including the one where we pointed the skill at itself.

## What it does

1. **Frame.** One question, its constraints, the known facts, the starting sources. Your own opinion is kept out of the shared brief.
2. **Cast.** Three moves, in order: discover the evidence territories the field already has (its issue tracker, its filings, its one conference); pull one outsider from an unrelated trade that solved the same structure of problem; fill the rest from five archetypes (practitioner, researcher, market, historian, skeptic). The skeptic is always cast and is the only seat told what you believe, with orders to find the strongest *published* dissent.
3. **Fieldwork.** Each seat is a subagent with its own context, a search budget, and a fixed note schema. Seats never see each other's notes. They cannot spawn helpers; the agent definitions have no Agent tool.
4. **Verify.** One fact-checker gets the load-bearing claims (not the notes), opens every cited page, traces secondary sources to the primary, looks for an independent second origin, and labels each claim on two axes.
5. **Synthesize.** One writer, after all fieldwork. Bottom line, consensus, cruxes, blind spots, ledger, seat metrics, cost.

Three depth tiers: `quick` (one inline pass plus a small verifier), `standard` (3 to 5 seats plus verifier, about 500K tokens, about 20 minutes), `deep` (up to 6 seats, a bigger verifier, and one anonymised feedback round).

## Install

Claude Code with subagents and web search. Pick one:

**As a plugin** (skill is `/family:family`, agents come along):

```
/plugin marketplace add xhyumiracle/family-skill
/plugin install family@family-skill
```

**Copied into `~/.claude`** (skill is `/family`):

```bash
git clone https://github.com/xhyumiracle/family-skill && ./family-skill/install.sh
```

Start a new session afterwards. Agent definitions are read at session start.

The skill never names a model. Seats and the verifier run on whatever your subagent default is (`CLAUDE_CODE_SUBAGENT_MODEL` in settings, otherwise the session model). Our two runs used Sonnet seats and Opus seats respectively; the Opus run had a lower verifier downgrade rate, but that is one run each on different topics.

## Use

Say what you want to understand and the skill triggers on its own: "research X from zero", "what am I missing about X", "is the hype about X real", "组个队", "从0到1了解". Or call it: `/family:family <question>`. Add `quick` or `deep` to pick a tier; `standard` is the default. The roster and the agent count are printed before anything is spawned.

Everything lands in `family/<slug>/` under your working directory: `brief.md`, `roster.md`, `cards/`, `seats/`, `claims.md`, `verification.md`, `report.md`. Each run appends a line to `family/runs.log`.

## Why it is built this way

Most multi-persona skills are folklore. We tried to keep only what has evidence, and we say which is which. The short version (full ledger with sources in [`docs/DESIGN.md`](docs/DESIGN.md)):

| Design choice | Evidence | What we did |
|---|---|---|
| Independent seats, one writer after fieldwork | Debate between agents adds little beyond voting over their independent answers (Choi et al., NeurIPS 2025); parallel section-writing produced disjoint reports at LangChain | Seats write blind; the orchestrator writes the report |
| A separate verification pass | Deep-research systems cite correctly 40-80% of the time (DeepTRACE, ICLR 2026); parallel agents without a central check amplified errors 17x in a 260-configuration study | One batched verifier, two-axis verdicts, hard rule that a misquoted claim never reaches the bottom line |
| Seats as search territories, not personas | STORM's own ablation: perspectives barely moved outline quality but doubled the distinct sources found; persona detail adds nothing over a name (SPP); personas in system prompts do not improve accuracy (Zheng et al., EMNLP Findings 2024) | Cards spend their words on where to search and what to leave to others |
| Keep the user's belief out of the shared brief | A belief in the prompt pulls answers toward it (Sharma et al., up to 27% on 2023 models) | Only the skeptic sees it |
| Skeptic finds published dissent | Authentic dissent beat every form of assigned devil's advocate (Nemeth et al. 2001) | The skeptic's first job is to find who has argued the other side, with sources |
| Searches per seat over seat count | Token budget explains 80% of the variance in Anthropic's research system; averaging three independent estimates captures most of the gain of averaging (Mandel et al. 2018) | Default four seats; raise searches before adding seats |
| The outsider seat, the discovered seat, the feedback round | No controlled study either way | On by default, labelled experimental, measured per run via seat metrics |

## What it is not

Not a decision tool (it maps a field; use a decision framework for A-vs-B). Not a single-fact lookup. Not an article writer. Not cheap: a standard run is roughly fifteen times a chat turn. Not an oracle: five seats on one model share that model's priors, and the verification pass is where most of the measured value lives.

## Examples

- [`examples/obsidian-agent-vault-sync/`](examples/obsidian-agent-vault-sync/): the first real run (5 seats, 15 claims checked, 5 downgraded, two of them meaning-inverting).
- [`examples/family-skill-design/`](examples/family-skill-design/): the skill run on itself. Five seats, including an intelligence-analysis methodologist as the outsider, read the skill files and the literature; 20 claims checked, 17 confirmed at the primary source. Version 0.2.0 is what came out.

## Credits

STORM is Shao et al., *Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models*, NAACL 2024. The crew idea came from a 小红书 post describing the five-role prompt and the film analogy. Prior art we read before building: hadufer/claude-storm, mediagato/storm-research, zrabin/panel-skill, Kanorin-chan/perspectives-skill, fradser/dotclaude.

MIT.
