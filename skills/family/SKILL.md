---
name: family
description: "Assemble a crew of 3-6 independent research seats, each sent to a different evidence territory on the SAME framed question (its own context, web search, fixed-schema note), then map consensus, cruxes and blind spots, and send a fact-checker to open every load-bearing source and up/down-weight it. STORM-style multi-perspective research, built for going from 0 to 1 on a field you do not know yet. Use whenever the user wants to 'understand X properly', '从0到1了解', '全面调研', '多角度看看', '帮我研究一下这个领域', 'what am I missing about X', 'is the hype about X real', mentions STORM, a crew, a panel, '组个队', 'family', or '/family' — even if they only say 'research X' and X is a contested or unfamiliar field. NOT for: choosing between named options (that is decision-council), a single fact lookup, subtopic-coverage reports with no contested question (that is deep-research), code questions, or writing a long article."
---

# family — assemble the crew before the job

Before the job, pull in people who read different sources, give them the same briefing, let each work alone, put the findings in one room, and send one person to open every door they say is open.

This is STORM's pre-writing stage (Shao et al., NAACL 2024) run as parallel subagents, with a verification pass that STORM does not have. Be exact about what STORM measured: in its ablation the component that carried outline quality was the *conversation* (reading retrieved material, then asking follow-up questions); removing perspectives barely moved outline recall but roughly halved the number of distinct sources found (99.83 vs 54.36). Human raters found STORM articles better organised (p=0.005) and only suggestively broader (p=0.084, 20 pairs). So the promise here is: more distinct sources, a map of where informed people disagree, and claims that have been checked. Not accuracy by itself, and no edge by itself.

## Why each rule exists

1. **Same brief to every seat, minus the user's opinion.** A seat that has to invent the facts argues with a fiction, so `brief.md` carries the question, constraints, known facts and starting sources. It does not carry what the user currently believes: a stated belief pulls answers toward it (up to 27% on 2023 models, Sharma et al.; still 23.8% of objective questions flipped right-to-wrong on a 2026 frontier model). The belief goes only to the skeptic's card.
2. **Seats are search territories, not voices.** Personas as costumes do not make a single agent more accurate (Zheng et al., EMNLP Findings 2024; the 2023 preprint of the same paper claimed roles "consistently improve" performance, so cite the final version; a 2025 retest on six models found the same null), and detailed persona profiles add nothing over a name (Wang et al., SPP). What does measure is several agents reading *different material*: STORM's perspectives doubled distinct sources; Anthropic's production notes say a worker needs "guidance on the tools and sources to use" and a boundary, and that work should be split by context, not by role. So a seat card spends its words on where to search, what evidence it trusts, and what to leave to others; the biography is one line.
3. **Independent contexts, no contact during fieldwork.** Debate between agents mostly adds nothing beyond voting over their independent answers (Choi et al., NeurIPS 2025); a unanimous wrong majority overturned 23-71% of correct answers across 23 open models, and the harness lets you message a running seat, so the rule has to be explicit: nobody messages a seat while it works. Seats write blind; one synthesizer writes the report after all fieldwork (parallel section-writing produced disjoint reports at LangChain; Anthropic's lead prompt forbids delegating the final report). Blind seats also give a free ablation: any subset of one run approximates a smaller crew (see `references/eval.md`), and mid-run contact would destroy that.
4. **A claim without a source is an opinion.** Seats separate the two in their notes. The verifier only touches sourced claims.
5. **Independent work pays only when something checks it, including the synthesis.** Parallel agents without a central check amplified errors 17x in a 260-configuration study; with a central check, 4x (Kim et al. 2025/26). Production deep-research systems cite correctly only 40-80% of the time (DeepTRACE), and in one 2026 error-localisation study 84.7% of final-report errors originated at the orchestrator, not the searchers. So the verifier checks the seats' claims, and the orchestrator's own bottom line is checked sentence by sentence against the verification table before delivery. In this skill's own runs the verifier downgraded 5 of 15 and 3 of 20 load-bearing claims, and the synthesizer once stitched two numbers from different tests into one sentence. Do not trade verifier budget for more seats.
6. **Disagreement is the product, if it is sourced.** Do not average into beige. A crux counts only when each side rests on different sources; a disagreement manufactured by role instructions on one model is not a finding. Unanimity with heavily overlapping sources is a casting failure; unanimity with independent sources is convergence.
7. **Fixed headcount, nobody hires.** The crew is cast once, the agent count is announced before spawning, and no seat may spawn helpers. This is structural: `family-member` and `family-verifier` (shipped in `agents/`) have no Agent tool. Budget per seat (searches) is the main quality knob; headcount is one way of spending budget, not a separate virtue, and cannot be tuned from single runs.

## Protocol

Work in `family/<slug>/` under the current directory (slug: short, lowercase, hyphenated, from the question). All paths given to seats are absolute. `<skill dir>` below means the base directory this SKILL.md was loaded from (the harness prints it when the skill loads); build the protocol paths on cards from it.

### 0. Frame (inline, no agents)

Write `brief.md`:

- The question in one line.
- What it is for, as three facts: the decision the reader has to make, when, and what result would make them act. The bottom line is written against these.
- Sub-questions, each with what a "yes" would mean (a threshold, a range, or a named outcome), so that seats can give leans the synthesizer can line up.
- Constraints: time window, geography, language, exclusions.
- Known facts, and the starting sources from the casting step so no seat rediscovers them.
- The output language.

If the request is "pick A or B", reframe it as "how do A and B behave on the dimensions the decision turns on", research that, and leave the pick to the user; the report's key judgments are the input to their choice, not the choice. Record the user's current belief, if any, in `cards/skeptic.md` only (step 1), and keep a private copy for the report's "belief vs. finding" line. Only ask the user a question if the answer changes who you would cast.

### 1. Cast (inline, at most two searches)

Read `references/casting.md`. Three moves, in order:

1. **Discover the territories.** One or two searches for overview or "state of" pieces on the topic or a sibling topic. From how they are sectioned and whom they quote, write down the evidence territories that exist and the two or three canonical primary pages you found. The pages go into `brief.md` as "Starting sources". One or two territories that a generic template would never name become seats.
2. **Pull one outsider from an unrelated trade.** State the problem's structure with the nouns removed, name a trade that has lived with that structure for decades, and cast a seat from it, defined by the analogy. Cast it only if the analogy points at a searchable corpus of that trade's rules and post-mortems. On by default and marked "experimental" in the roster: no controlled study has tested it, and single-run seat counts cannot (they depend on which claims the orchestrator chose to verify).
3. **Add the four fixed seats, named as real jobs.** On every question: someone who uses it, someone who builds or runs it, someone who bets on it (an industry VC, a buyer, or the manager with the budget, whichever the question turns on), and the skeptic. Four territories whose material does not overlap and that no discovery search will surface. Jobs someone actually holds, two to five words, no invented colour: persona detail beyond the job title does not change what a seat finds. The skeptic's job is to find the strongest *published* opposing case, not to invent objections: in Nemeth, Brown and Rogers (2001) authentic dissent beat every form of assigned devil's advocate.

Four fixed, plus the outsider, plus the discovered seat when Move 1 found a territory not already covered: five or six. Run the diversity test (first three planned queries and source types must differ). Print the roster as one table (seat code S1..Sn, job title plus at most one clause, how cast), the tier, and the agent count, then continue; the territory lines belong on the cards, not in the table. Wait for approval only if the user asked to approve casts, or if the tier is `deep`.

### 2. Fieldwork (parallel agents)

Write one card per seat to `cards/<seat>.md` (template in `references/seat-protocol.md`), then spawn one `family-member` per seat, all in a single turn, each with the two-line spawn prompt that names only the card path. Long spawn prompts have stalled the harness's permission classifier, and the card on disk is the audit trail. Members return a short summary; read their files, not their transcripts. A seat that stops at its turn cap is resumed with "stop searching, write the note now", never re-run. Nobody messages a seat before it has finished.

### 2.5 Gap rounds (at most 1 in `standard`, at most 3 in `deep`)

After every seat has finished, read each note's "Read but not cited" and "Deliberately not examined" sections; after verification, read the verifier's "Found but not cited" as well. A round fires only on a rule written in the brief: a sub-question with no direct evidence from any seat, a crux with one side unsourced, or a gap that would change the bottom line if filled. A round that fires after verification resumes the verifier for the new claims, by message, with a budget of a few fetches; it does not spawn a second verifier. Write at most two gap questions, each naming the territory and the budget (4 searches), with no seat's findings and no lean of your own, and resume the one or two seats whose territory fits, by message. Record the trigger, the questions and the seats in `amendments.md`. Resumed seats append a "## Post-gap" section to their notes; those claims enter `claims.md` like any other.

In `deep`, repeat while the evidence is still moving: after each round, if the new claims would change a crux's lean or fill an empty side, run another; if a round brings back nothing that touches a crux, or three rounds have run, stop. The stopping rule is about evidence, never about agreement: seats are not asked to respond to each other, and convergence between seats of one model is what conformity produces, not what truth produces. This is Co-STORM's moderator move (questions from retrieved-but-uncited material) applied after fieldwork instead of during it, and it replaces any feedback or debate round.

### 3. Verify (one agent)

From the seat notes write `claims.md` with stable IDs (C01, C02, ...) and seat codes in the "Seats" column (S1, S3), never seat names, so the verifier cannot tell a seat's role. Selection floors first: at least two claims per sub-question, at least one per side of each crux, at least two per seat; then fill the budget by diagnosticity (a claim that, if false, flips a crux), then contested, single-source, surprising, quantitative. Mark each crux's two sides so the verifier searches both. Keep to the tier's claim budget and list what was left out. Spawn one `family-verifier` with `references/verifier-protocol.md`, `claims.md`, and the output path `verification.md`.

### 4. Synthesize (inline)

Read all seat files and `verification.md`. Write `report.md` per `references/report-template.md`: a three-slot bottom line, a key-judgments table of at most seven rows, belief vs. finding, cruxes, blind spots, a source summary, next step, and a maintainer appendix. Then the post-synthesis check, before anything is delivered:

- Every number and every quoted phrase in the bottom line and the key-judgments table must appear verbatim in `verification.md` (or in the brief's known facts). If it does not, rewrite the sentence or tag it [UNVERIFIED]. Two numbers from different tests never share a sentence.
- A claim with verdict MISQUOTED, or flagged CIRCULAR without a second origin, cannot support a key judgment.
- Run the six-item lint in the template and write the score in the appendix. Run `scripts/metrics.py` on `claims.md` and `verification.md` for the seat metrics; do not count by hand.

### 5. Deliver

Reply with the three bottom-line slots copied from the report, at most three cruxes, one blind spot, the path to `report.md`, and the cost line. Append one line to `family/runs.log` (date, slug, tier, seats, tokens, claims checked, downgraded, lint score, gap round used or not). The log is a cost and health record; it is not an eval. How to evaluate the skill is in `references/eval.md`.

## Depth tiers

| Tier | Seats | Searches / seat | Gap round | Verifier claims | Agents spawned | Rough cost |
|---|---|---|---|---|---|---|
| `quick` | none: the orchestrator searches alone, 8 searches | n/a | no | 6-8 | 1 (the verifier) | ~80K tokens |
| `standard` (default) | 5-6 (4 fixed + outsider + discovered when found) | 12 | at most 1, rule-triggered | 20 | seats + 1 | ~600-800K tokens, ~30 min wall (measured: seats 65-110K each with the stop rule, verifier 135K, one gap round 26K) |
| `deep` | 6 | 18 | up to 3, until the cruxes stop moving | 30 | seats + 1 | ~1M+ tokens; confirm with the user first |

Pick `standard` unless the user names a tier or the question is clearly small. When a run needs more, raise searches per seat before adding seats.

## Keeping the bill honest

- The agent count for the tier is the agent count. No helper agents, no "let me spawn an Explore to find sources", no re-running the whole crew because one seat was weak.
- Seats stop at their search budget, or when two searches in a row find no new primary source, and say what they did not cover.
- The verifier gets `claims.md`, never the seat notes.
- Member summaries are capped (250 words).
- Print the cost line from real numbers.
- Do not pass a `model` override when spawning seats or the verifier unless the user asked for one in this run.

## Fallbacks

- `family-member` not resolvable in this session: spawn `general-purpose`, prepend "You have no permission to spawn subagents; do the work in this context" to the prompt, and keep everything else identical. This is a prompt guard, not a structural one (nested spawning is on by default up to three layers), so say so in the cost line.
- No web search available: run `quick` only, and mark every claim UNGROUNDED. Do not pretend.

## Files this skill reads

- `references/casting.md` — the three casting moves, archetype cards, bench, diversity test, the gap round
- `references/seat-protocol.md` — what a seat does, its note schema, the seat card file, the spawn prompt, the gap-round message
- `references/verifier-protocol.md` — verdicts, flags, directness, the spawn prompt
- `references/report-template.md` — report structure, the likelihood scale, the lint
- `references/eval.md` — how to evaluate a configuration change without fooling yourself
- `scripts/metrics.py` — seat metrics from `claims.md` and `verification.md`
