# Evaluating a configuration change

Read this before changing a default (headcount, the outsider seat, model tier, a verifier rule) on the strength of a run or two. The skill's own runs are a cost and health log, not an eval: which claims get verified is the orchestrator's choice, so per-seat counts from one run measure the orchestrator, and a deep-research agent re-run on the same query changes most of its findings (total variance 0.76 on findings vs 0.44 on citations in one 2026 study). Twenty questions detect only large effects: a 3-point difference on a rubric score needs about a thousand questions, and CLT error bars below a few hundred points are badly over-confident.

## What can be measured cheaply, and what cannot

| Question | Can a 12-20 question eval answer it? | Metric |
|---|---|---|
| Model tier for seats | Probably | M1: fidelity rate on a seat-blind random sample of claims (share eligible Y / Y*), paired by question |
| Outsider seat on vs off | Maybe | M2: binary rubric compliance and crux-key recall, from subsets of one run |
| 3 vs 4 vs 5 seats | No | Do not tune headcount from evals this size; default stays at four |
| Report template versions | Yes, differently | Reader test: first 300 words only; four questions (what is recommended, how likely, what would change it, which load-bearing claim is weakest); correctness and time |
| Verifier label reliability | Yes | Run the verifier twice on the same claims.md; report raw agreement and kappa on the Eligible column only |

## Design

- **Pre-register.** Write the question set, the rubrics, the crux keys, the primary metric and the one primary comparison before the first run, and freeze them. Everything else is exploratory and is labelled so.
- **Questions.** Twelve: eight from ResearchRubrics (expert-written binary rubrics, MIT-licensed grading code, pick contested questions with literature on both sides) and four of the owner's own, each with 15-25 binary rubric items and 2-4 crux keys ("the report names disagreement X with sources on both sides"). Do not let an LLM rewrite rubrics (that degrades agreement by 15-20 points). Run the eval in English so the rubrics apply.
- **Arms from subsets.** Blind seats make subsets valid: run one 5-seat fieldwork per question per model tier, verify the union of claims once, and build the arms by re-running only the synthesis on subsets: all five; four without the outsider; leave-one-out for each non-skeptic seat; three. Verdicts are shared across arms (common random numbers). This costs about a third of running each arm in full.
- **Paired statistics.** Compare arms within question, report paired differences with exact or Bayesian intervals, never a CLT bar. Re-run four questions end to end once to estimate run-to-run variance before reading any difference as real.
- **Judge.** Before the first scored run, the owner hand-labels 20 rubric items. If a Claude judge reaches Macro F1 ≥ 0.75 against those labels, use it; otherwise use a judge that does (LiveResearchBench excluded Claude 4 Sonnet from its judge ensemble for low agreement). Binary grading only; no 0-10 scores, no ternary scales.
- **Stop rules, written first.** If three seats and five seats do not separate on M2, the default stays at four and headcount is closed. If the outsider arm does not separate on M2 and crux recall, the outsider becomes optional.

## Cost

Per question: one 5-seat fieldwork per tier (about 0.7-0.9M tokens on current pricing of attention), one verification of the union (about 0.25M), eight syntheses (about 0.07M each). Twelve questions and two tiers come to roughly 25-30M tokens. Full separate runs per arm would be about three times that.
