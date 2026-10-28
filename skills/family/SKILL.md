---
name: family
description: "Assemble five independent researchers on one question, one per kind of evidence: first-hand experience, expert knowledge of how and why, the people with stakes in the answer, the strongest published dissent, and the outside view from a field that has handled the same kind of problem. Each searches its own territory in its own context and writes a sourced note; then map consensus, cruxes and blind spots, and send a fact-checker to check the load-bearing sources. STORM-style multi-perspective research for going from 0 to 1 on an unfamiliar or contested question. Use when the user wants to 'understand X properly', '从0到1了解', '全面调研', '多角度看看', '帮我研究一下这个领域', 'what am I missing about X', 'is the hype about X real', mentions STORM, a crew, a panel, '组个队', 'family' or '/family', even if they only say 'research X' and X is contested or unfamiliar. Not for: picking between named options, single fact lookups, uncontested topic overviews, code questions, long articles."
license: MIT
compatibility: "Needs parallel subagents, web search and file writes. Built and tested on Claude Code; other runtimes with subagents follow the Fallbacks section. Without subagents or web search it cannot run."
---

# family.skill: assemble the crew before the job

Before the job, pull in people who read different sources, give them the same briefing, let each work alone, put the findings in one room, and send one person to open every door they say is open.

This is STORM's pre-writing stage (Shao et al., NAACL 2024) run as parallel subagents, with a verification pass that STORM does not have. Be exact about what STORM measured: in its ablation the component that carried outline quality was the *conversation* (reading retrieved material, then asking follow-up questions); removing perspectives barely moved outline recall but roughly halved the number of distinct sources found (99.83 vs 54.36). Human raters found STORM articles better organised (p=0.005) and only suggestively broader (p=0.084, 20 pairs). So the promise here is: more distinct sources, a map of where informed people disagree, and claims that have been checked. Not accuracy by itself, and no edge by itself.

## Why each rule exists

1. **Same brief to every seat, minus the user's opinion.** A seat that has to invent the facts argues with a fiction, so `brief.md` carries the question, constraints, known facts and starting sources. It does not carry what the user currently believes: a stated belief pulls answers toward it (up to 27% on 2023 models, Sharma et al.; still 23.8% of objective questions flipped right-to-wrong on a 2026 frontier model). The belief goes only to the dissent seat's card.
2. **Seats are search territories.** Personas as costumes leave a single agent's accuracy unchanged (Zheng et al., EMNLP Findings 2024; the 2023 preprint of the same paper claimed roles "consistently improve" performance, so cite the final version; a 2025 retest on six models found the same null), and detailed persona profiles add nothing over a name (Wang et al., SPP). What does measure is several agents reading *different material*: STORM's perspectives doubled distinct sources; Anthropic's production notes say a worker needs "guidance on the tools and sources to use" and a boundary, and that work should be split by context. So a seat card spends its words on where to search, what evidence it trusts, and what to leave to others; the biography is one line.
3. **Independent contexts, no contact during fieldwork.** Debate between agents mostly adds nothing beyond voting over their independent answers (Choi et al., NeurIPS 2025); a unanimous wrong majority overturned 23-71% of correct answers across 23 open models, and the harness lets you message a running seat, so the rule has to be explicit: nobody messages a seat while it works. Seats write blind; one synthesizer writes the report after all fieldwork (parallel section-writing produced disjoint reports at LangChain; Anthropic's lead prompt forbids delegating the final report). Blind seats also give a free ablation: any subset of one run approximates a smaller crew (see `references/eval.md`), and mid-run contact would destroy that.
4. **A claim without a source is an opinion.** Seats separate the two in their notes. The verifier only touches sourced claims.
5. **Independent work pays only when something checks it, including the synthesis.** Parallel agents without a central check amplified errors 17x in a 260-configuration study; with a central check, 4x (Kim et al. 2025/26). Production deep-research systems cite correctly only 40-80% of the time (DeepTRACE), and in one 2026 error-localisation study 84.7% of final-report errors originated at the orchestrator. So the verifier checks the seats' claims, and the orchestrator's own bottom line is checked sentence by sentence against the verification table before delivery. In this skill's own runs the verifier downgraded 5 of 15 and 3 of 20 load-bearing claims, and the synthesizer once stitched two numbers from different tests into one sentence. Do not trade verifier budget for more seats.
6. **Disagreement is the product, if it is sourced.** Do not average into beige. A crux counts only when each side rests on different sources; a disagreement manufactured by role instructions on one model is not a finding. Unanimity with heavily overlapping sources is a casting failure; unanimity with independent sources is convergence.
7. **Fixed headcount, nobody hires.** The crew is cast once, the agent count is announced before spawning, and no seat may spawn helpers. In Claude Code this is structural: `family-member` and `family-verifier` (shipped in `agents/`) have no Agent tool. Elsewhere it is a prompt guard (see Fallbacks). Budget per seat (searches) is the main quality knob; headcount is one way of spending that budget, and single runs cannot tune it.

## Protocol

Work in `family/<slug>/` under the current directory (slug: short, lowercase, hyphenated, from the question). All paths given to seats are absolute. `<skill dir>` below means the base directory this SKILL.md was loaded from (Claude Code prints it when the skill loads; elsewhere, the directory you read this file from); build the protocol paths on cards from it.

### 0. Frame (inline, no agents)

Write `brief.md`:

- The question in one line.
- What it is for, as three facts: the decision the reader has to make, when, and what result would make them act. The bottom line is written against these.
- Sub-questions, each with what a "yes" would mean (a threshold, a range, or a named outcome), so that seats can give leans the synthesizer can line up.
- Constraints: time window, geography, language, exclusions.
- Known facts, and the starting sources from the casting step so no seat rediscovers them.
- The output language.

If the request is "pick A or B", reframe it as "how do A and B behave on the dimensions the decision turns on", research that, and leave the pick to the user; the report's key judgments are the input to their choice. Record the user's current belief, if any, in `cards/dissent.md` only (step 1), and keep a private copy for the report's "belief vs. finding" line. Only ask the user a question if the answer changes who you would cast.

### 1. Cast (inline, at most two searches)

Read `references/casting.md`. Two moves, in order:

1. **Discover the territories.** One or two searches for overview or "state of" pieces on the topic or a sibling topic. From how they are sectioned and whom they quote, write down the evidence territories that exist and the two or three canonical primary pages you found. The pages go into `brief.md` as "Starting sources". A territory none of the five perspectives would reach becomes a seat by replacing the perspective whose material overlaps most.
2. **Fill the five perspectives, named as real jobs or sources for this question.** Each is one kind of evidence from a published method, so the set fits any question: **first-hand** (the people closest to the evidence; argument from position to know), **expert** (the people who explain how and why), **stakes** (who decides, pays, benefits or bears the consequences; the roles of Critical Systems Heuristics), **dissent** (the strongest published case against the prevailing answer, named after the real dissenting group, so it works on questions with no stance; Nemeth, Brown and Rogers 2001: authentic dissent beat every form of assigned devil's advocate), and the **outside view** (a field that has handled the same structure, bringing how comparable cases turned out; reference-class forecasting). Write one or two candidates per perspective from the question and keep, per perspective, the one most relevant to the question and least like the others (AgentInit: query-generated teams chosen for relevance and diversity together beat predefined roles). When nobody real holds stakes (a pure science or history question), fill that seat with a second method that reads different evidence; a perspective with no relevant candidate is dropped, so a crew may have fewer than five. Cast the outside view only if that field has a searchable corpus, and mark it "experimental". Never invent a holder. Jobs someone actually holds, two to five words, no invented colour: persona detail beyond the job title does not change what a seat finds.

Five seats in `standard` and `deep`, three in `mini` (dissent plus the two perspectives most relevant to the question); never a sixth. Three independent inputs capture most of the aggregation gain, Delphi panels of 3 to 11 show no accuracy difference, and each seat costs 70-110K tokens. Run the diversity test (first three planned queries and source types must differ). Print the roster as one table (seat code S1..Sn, job title plus at most one clause, perspective), the tier, and the agent count, then continue; the territory lines belong on the cards. Wait for approval only if the user asked to approve casts, or if the tier is `deep`.

### 2. Fieldwork (parallel agents)

Write one card per seat to `cards/<seat>.md` (template in `references/seat-protocol.md`), then spawn one `family-member` per seat, all in a single turn, each with the two-line spawn prompt that names only the card path. Long spawn prompts have stalled permission checks, and the card on disk is the audit trail. Members return a short summary; read their files. A seat that stops at its turn cap is resumed with "stop searching, write the note now", never re-run. Nobody messages a seat before it has finished.

### 2.5 Evidence rounds (at most 1 in `standard`, rule-triggered; up to 3 in `deep`, by default)

This is the only form of "discuss it further" the evidence supports, and it is not a debate. Free debate between agents adds little beyond voting over their independent answers, and exposure to peers flips right answers; what did improve accuracy in human panels was anonymous, reasons-carrying feedback over a few rounds (Delphi), and in LLM debate, updates that are allowed only in the direction of correction. So a round is built as a Delphi round over verified evidence.

After verification, write `cruxes.md`: each crux as "Side A claims X (verified evidence, verdicts) / Side B claims Y (verified evidence, verdicts)", with no seat names, plus at most two gap questions drawn from the seats' "Read but not cited" and "Deliberately not examined" sections and the verifier's "Found but not cited". Resume the seats that are party to a crux or own a gap's territory (budget 4 searches each, message template in `references/seat-protocol.md`). Each may do three things only: hold with a new source (URL required), concede by naming the verified claim that changed its mind, or reframe (the disagreement is definitional). A reply with no new source is recorded as "hold, no new evidence". Resumed seats append "## Post-round N" to their notes; the new claims are added to `claims.md` and the verifier is resumed for them. Record the trigger, the cruxes sent and the seats in `amendments.md`.

In `standard` the round fires only on the rule in the brief: a sub-question with no direct evidence, a crux with one side unsourced, or a gap that would change the bottom line. In `deep` it runs by default and repeats while the evidence is still moving: another round only if the last one changed a crux's lean, filled an empty side, or produced a concession; stop when a round changes nothing, or after three (Delphi practice is two or three rounds, Rowe and Wright 2001). The stopping rule is about evidence, never agreement: convergence between seats of one model is what conformity produces.

### 3. Verify (one agent)

From the seat notes write `claims.md` with stable IDs (C01, C02, ...) and seat codes in the "Seats" column (S1, S3), never seat names, so the verifier cannot tell a seat's role. Include every load-bearing claim: each claim a key judgment or the bottom line could rest on, both sides of every crux, and at least two per sub-question and two per seat. There is no fixed count; order the list by diagnosticity (a claim that, if false, flips a crux), then contested, single-source, surprising, quantitative. Mark each crux's two sides so the verifier searches both. If the synthesis later needs a claim that was not verified, resume the verifier for it before using it. Spawn one `family-verifier` with `references/verifier-protocol.md`, `claims.md`, and the output path `verification.md`.

### 4. Synthesize (inline)

Read all seat files and `verification.md`. Write `report.md` per `references/report-template.md`: a three-slot bottom line, a key-judgments table of at most seven rows, belief vs. finding, cruxes, blind spots, a source summary, next step, and a maintainer appendix. Then the post-synthesis check, before anything is delivered:

- Every number and every quoted phrase in the bottom line and the key-judgments table must appear verbatim in `verification.md` (or in the brief's known facts). If it does not, rewrite the sentence or tag it [UNVERIFIED]. Two numbers from different tests never share a sentence.
- A claim with verdict MISQUOTED, or flagged CIRCULAR without a second origin, cannot support a key judgment.
- Run the six-item lint in the template and write the score in the appendix. Run `<skill dir>/scripts/metrics.py <run dir>` on `claims.md` and `verification.md` for the seat metrics; do not count by hand.

### 5. Deliver

Reply with the three bottom-line slots copied from the report, at most three cruxes, one blind spot, the path to `report.md`, and the cost line. Append one line to `family/runs.log` (date, slug, tier, seats, tokens, claims checked, downgraded, lint score, evidence rounds run). The log is a cost and health record; it is not an eval. How to evaluate the skill is in `references/eval.md`.

## Depth tiers

| Tier | Seats | Searches / seat | Evidence rounds | Agents spawned | Rough cost |
|---|---|---|---|---|---|
| `mini` | 3: dissent plus the two perspectives most relevant to the question | 12 | no | seats + 1 | ~350-450K tokens |
| `standard` (default) | 5 (four perspectives + outside view; a discovered territory replaces an overlapping one) | 12 | at most 1, rule-triggered | seats + 1 | ~600-800K tokens, ~30 min wall (measured: seats 65-110K each with the stop rule, verifier about 7K per claim, one round 26K + re-verification) |
| `deep` | the same five | 12 | up to 3, until the evidence stops moving | seats + 1 | ~1M tokens; confirm with the user first |

Pick `standard` unless the user names a tier. `deep` is the same family taken through evidence rounds until the cruxes stop moving; it never adds seats.

## Keeping the bill honest

- The agent count for the tier is the agent count. No helper agents, no "let me spawn an Explore to find sources", no re-running the whole crew because one seat was weak.
- Seats stop at their search budget, or earlier when two searches in a row find no new primary source, and say what they did not cover. The budget of 12 sits inside the 10 to 15 tool calls per subagent Anthropic writes into its prompts for comparison-type research, because agents judge their own effort poorly; the stop rule does the real work.
- The verifier gets `claims.md`, never the seat notes.
- Member summaries are capped (250 words).
- Print the cost line from real numbers.
- Do not pass a `model` override when spawning seats or the verifier unless the user asked for one in this run.

## Fallbacks

- No `family-member` or `family-verifier` agent (a runtime other than Claude Code, or the skill installed without `agents/`): spawn the runtime's general-purpose subagent with the same two-line prompt, prefixed with "You have no permission to spawn subagents; do the work in this context." This guard is only a prompt, so say so in the cost line.
- The runtime cannot message a finished subagent: wherever this skill says "resume" (turn cap, evidence rounds, re-verification), spawn a fresh subagent on the same card and add one line pointing at its existing note. Everything it needs is on disk.
- No subagents or no web search: the family cannot run. Say so and stop.

## Files this skill reads

- `references/casting.md`: the two casting moves, the five perspective cards, the bench, the diversity test, the evidence round
- `references/seat-protocol.md`: what a seat does, its note schema, the seat card file, the spawn prompt, the evidence-round message
- `references/verifier-protocol.md`: verdicts, flags, directness, the spawn prompt
- `references/report-template.md`: report structure, the likelihood scale, the lint
- `references/eval.md`: how to evaluate a configuration change without fooling yourself
- `scripts/metrics.py`: seat metrics from `claims.md` and `verification.md`
