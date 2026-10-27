# Changelog

## 0.3.5 — 2026-10-28

- Four fixed seats instead of three: uses it, builds it, bets on it, picks it apart. Users and builders read different material, so they are two territories, not one. Plus the outsider, plus a discovered seat when Move 1 finds one: five or six.

## 0.3.4 — 2026-10-28

- The three fixed seats are defined by evidence territory (practice, money, dissent) with the job as the per-topic instantiation (engineer or operator; buyer, budget-holding manager or VC; skeptic). Rationale and its limits written into casting.md and docs/DESIGN.md: no fixed list has experimental support; runs.log plus leave-one-seat-out is how it gets tested.

## 0.3.3 — 2026-10-28

- The crew is three fixed seats (someone who does this for a living, someone who pays for it or bets on it, the skeptic) plus two dynamic ones (discovered territory, outsider). Fixed seats keep rosters comparable across runs; the dynamic two are where the unique findings came from in every run so far.
- A gap round may also fire after verification, from the verifier's "Found but not cited"; the verifier is then resumed for the new claims. Came from a run where the verifier surfaced a product that changed the bottom line.
- Tier costs updated from a run with the 0.3 cards: seats 65-110K tokens each, verifier 135K, gap round 26K.

## 0.3.2 — 2026-10-28

- Seats are named after real jobs ("an industry VC", "a procurement security officer who writes the RFPs"), not archetype categories with qualifiers; the archetypes are an incentive checklist. The bench is a list of jobs. Invented colour beyond the job title is banned: persona detail does not change what a seat finds, the territory does.
- The roster table shows job title plus one clause; territory lines stay on the cards.

## 0.3.1 — 2026-10-28

- Gap rounds can repeat in `deep` (max 3) with an evidence-based stop rule: another round only if the last one moved a crux. Never a convergence-of-opinion rule.
- "Pick A or B" requests are reframed as a comparison on the decision's dimensions and researched; the pick stays with the user. The README's "not for" line says so instead of refusing.
- README: `quick` described plainly (no crew; the orchestrator searches alone).

## 0.3.0 — 2026-10-28

Rewritten after a second self-review run (5 seats on the v0.2.0 files, 20 claims checked; see `examples/family-skill-v03/`). The theme: v0.2.0 added structure that no run had validated, and the orchestrator was the least-checked part of the pipeline.

- Verifier verdicts collapsed from eleven labels on two axes to four verdicts (CONFIRMED primary/secondary, PARTIAL, MISQUOTED inverted/stitched/absent, NOT-VERIFIED), two evidence-backed flags (CIRCULAR, CONTRADICTED), a direct/indirect mark with a reason, and a mechanically derived "eligible" column. Weight arrows removed. Every PARTIAL or MISQUOTED quotes the original and the adjacent sentence verbatim.
- Post-synthesis check: every number and quoted phrase in the bottom line and key judgments must appear verbatim in the verification table; a six-item lint is scored in the appendix.
- Report split into a reader layer (three-slot bottom line on a seven-level likelihood scale with confidence stated separately, a key-judgments table of at most seven rows, belief vs. finding, cruxes, blind spots, source summary, next step) and a maintainer appendix. The seat-estimates table and the full ledger left the reader's path.
- Gap round: after fieldwork and before verification, the orchestrator may resume one or two finished seats with at most two questions drawn from what seats read but did not cite. Rule-triggered, logged, no findings passed along. Replaces the never-run deep-tier feedback round. Messaging a seat during fieldwork is now an explicit rule violation.
- Seat notes gained "Read but not cited"; lost the confidence column (the verifier's verdict is the confidence). Estimates use the likelihood scale.
- claims.md uses stable IDs and seat codes; selection floors per sub-question, per crux side and per seat come before diagnosticity ranking. `scripts/metrics.py` computes seat metrics; hand counts are banned (round 1's were wrong).
- `references/eval.md`: how to evaluate a configuration change (arms from subsets of one blind run, paired statistics, binary rubrics, pre-registered stop rules). runs.log is a cost log, not an eval.
- Brief now states the decision, the deadline, and what result would make the reader act; sub-questions say what "yes" means.
- Agent turn caps raised to 60 (a seat hit 40 while reading files plus twelve searches).
- Evidence refreshed to 2025-26 models for personas (still no gain) and sycophancy (23.8% right-to-wrong on a 2026 frontier model). Of the 20 claims this version rests on, the verifier confirmed 14 at the primary source, marked 5 partial and 1 contradicted (in a direction that strengthens the change); details in `examples/family-skill-v03/verification.md`.

## 0.2.0 — 2026-10-27

Unvalidated by any run at the time of release: the credibility axis, the seat-estimates table, the seat metrics, the feedback round. 0.3.0 removed or reshaped all four.

Rewritten after running the skill on itself (5 seats + verifier, 20 claims checked; see `examples/family-skill-design/`).

- Seats are search territories, not personas. Cards spend their words on where to search and what to leave to others; the biography is one line.
- Casting is three moves: discover territories from how the field sections itself, one outsider from an unrelated trade (on by default, marked experimental), then the archetypes.
- The user's current belief goes only to the skeptic's card, never into the shared brief.
- The skeptic looks for published dissent instead of inventing objections.
- Verifier verdicts split into two axes (fidelity/provenance and credibility); a quote inverted by truncation or stitching is MISQUOTED, not PARTIAL; standard budget 20 claims.
- Deep tier's cross-examination became an anonymised, post-verification, new-evidence-required feedback round.
- Quick tier is one inline research pass plus a small verifier.
- Report gained a seat-estimates table, a belief-vs-finding line, and per-seat metrics; runs append to `family/runs.log`.
- Fixed two citations in the rules (Zheng et al. version; ChatEval misattribution).
- Removed the Codex "second model" seat: untested, harness-specific, and frontier models' errors are correlated across providers anyway.

## 0.1.0 — 2026-10-27

First version: five renamed archetypes, independent seats, batched verifier, three depth tiers, agents without the Agent tool. First real run: `examples/obsidian-agent-vault-sync/`.
