---
name: family
description: "Assemble a crew of 3-6 independent research seats, each sent to a different evidence territory on the SAME framed question (its own context, web search, fixed-schema note), then map consensus, cruxes and blind spots, and send a fact-checker to open every load-bearing source and up/down-weight it. STORM-style multi-perspective research, built for going from 0 to 1 on a field you do not know yet. Use whenever the user wants to 'understand X properly', '从0到1了解', '全面调研', '多角度看看', '帮我研究一下这个领域', 'what am I missing about X', 'is the hype about X real', mentions STORM, a crew, a panel, '组个队', 'family', or '/family' — even if they only say 'research X' and X is a contested or unfamiliar field. NOT for: choosing between named options (that is decision-council), a single fact lookup, subtopic-coverage reports with no contested question (that is deep-research), code questions, or writing a long article."
---

# family — assemble the crew before the job

Before the job, pull in people who read different sources, give them the same briefing, let each work alone, put the findings in one room, and send one person to open every door they say is open.

This is STORM's pre-writing stage (Shao et al., NAACL 2024) run as parallel subagents, with a verification pass that STORM does not have. Be exact about what STORM measured: in its ablation the component that carried outline quality was the *conversation* (reading retrieved material, then asking follow-up questions); removing perspectives barely moved outline recall but roughly halved the number of distinct sources found (99.83 vs 54.36). Human raters found STORM articles better organised (p=0.005) and only suggestively broader (p=0.084, 20 pairs). So the promise here is: more distinct sources, a map of where informed people disagree, and claims that have been checked. Not accuracy by itself, and no edge by itself.

## Why each rule exists

1. **Same brief to every seat, minus the user's opinion.** A seat that has to invent the facts argues with a fiction, so `brief.md` carries the question, constraints, known facts and starting sources. It does not carry what the user currently believes: a belief in the prompt pulls answers toward it (Sharma et al. 2023, up to 27% on 2023 models), and five seats reading the same belief are one anchored committee. The belief goes only to the skeptic's card.
2. **Seats are search territories, not voices.** Personas as costumes do not make a single agent more accurate (Zheng et al., EMNLP Findings 2024; the 2023 preprint of the same paper claimed roles "consistently improve" performance, so cite the final version) and detailed persona profiles add nothing over a name (Wang et al., SPP). What does measure is several agents reading *different material*: STORM's perspectives doubled distinct sources; Anthropic's production notes say the thing a worker needs is "guidance on the tools and sources to use" and a boundary, and that work should be split by context, not by role. So a seat card spends its words on where to search, what evidence it trusts, and what to leave to others; the biography is one line.
3. **Independent contexts, no cross-talk during fieldwork.** Debate between agents mostly adds nothing beyond what voting over their independent answers gives (Choi et al., NeurIPS 2025), and agents conform to a majority. Seats write blind; one synthesizer writes the report after all fieldwork is done (parallel section-writing produced disjoint reports at LangChain; Anthropic's lead prompt forbids delegating the final report).
4. **A claim without a source is an opinion.** Seats separate the two in their notes. The verifier only touches sourced claims.
5. **Independent work pays only when something checks it.** Parallel agents without a central check amplified errors 17x in a 260-configuration study; with a central check, 4x (Kim et al. 2025/26). Production deep-research systems cite correctly only 40-80% of the time (DeepTRACE). The verifier is the best-evidenced part of this pipeline; the first real run confirmed it (5 of 15 load-bearing claims downgraded, two with inverted meaning). Do not trade verifier budget for more seats.
6. **Disagreement is the product, if it is sourced.** Do not average into beige. A crux counts only when each side rests on different sources; a disagreement manufactured by role instructions on one model is not a finding. Unanimity with heavily overlapping sources is a casting failure; unanimity with independent sources is convergence.
7. **Fixed headcount, nobody hires.** The crew is cast once, the agent count is announced before spawning, and no seat may spawn helpers. This is structural: `family-member` and `family-verifier` (shipped in `agents/`; they appear as `family:family-member` and `family:family-verifier` when installed as a plugin) have no Agent tool. Budget per seat (searches) is the main quality knob; headcount is one way of spending budget, not a separate virtue.

## Protocol

Work in `family/<slug>/` under the current directory (slug: short, lowercase, hyphenated, from the question). All paths given to seats are absolute. `<skill dir>` below means the base directory this SKILL.md was loaded from (the harness prints it when the skill loads); build the protocol paths on cards from it.

### 0. Frame (inline, no agents)

Write `brief.md`: the question in one line and what it is *for*; constraints (time window, geography, language, exclusions); known facts; the output language. If the request is really "pick between A and B", stop and use decision-council instead. Record the user's current belief, if any, in `cards/skeptic.md` only (step 1), and keep a private copy for the report's "belief vs. finding" line.

Only ask the user a question if the answer changes who you would cast (ambiguous entity, missing jurisdiction). Otherwise proceed.

### 1. Cast (inline, at most two searches)

Read `references/casting.md`. Three moves, in order:

1. **Discover the territories.** One or two searches for overview or "state of" pieces on the topic or a sibling topic. From how they are sectioned and whom they quote, write down the evidence territories that exist (the issue tracker, the maintainer's release notes, the regulator's enforcement actions, the conference's proceedings, the community's forum) and the two or three canonical primary pages you found. The pages go into `brief.md` as "Starting sources" so no seat spends budget rediscovering them. One or two territories that a generic template would never name become seats.
2. **Pull one outsider from an unrelated trade.** State the problem's structure with the nouns removed, name a trade that has lived with that structure for decades, and cast a seat from it, defined by the analogy. Cast it only if the analogy points at a searchable corpus of that trade's rules and post-mortems. On by default and marked "experimental" in the roster: no controlled study has tested it, and the nearest human evidence (design-analogy studies) favours near analogies for quality and far ones for novelty.
3. **Fill from the archetypes** (practitioner, researcher, market/incentives, historian, skeptic), each renamed to the topic. The skeptic is always cast, and its job is to find the strongest *published* opposing case, not to invent objections: in Nemeth, Brown and Rogers (2001) authentic dissent beat every form of assigned devil's advocate, and their earlier work found assigned advocates mostly make people bolster the original view.

Run the diversity test (first three planned queries and source types must differ). Headcount is what survives: three to five in `standard`, four by default; six only in `deep`. Averaging three independent estimates captures most of the gain of averaging, and Delphi panels of 3 to 11 showed no accuracy difference, so do not pad. Print the roster as one table (seat, who, territory, first question, how cast: discovered / outsider / archetype), the tier, and the agent count, then continue. Wait for approval only if the user asked to approve casts, or if the tier is `deep`.

### 2. Fieldwork (parallel agents)

Write one card per seat to `cards/<seat>.md` (template in `references/seat-protocol.md`), then spawn one `family-member` per seat, all in a single turn, each with the two-line spawn prompt that names only the card path. Long spawn prompts have stalled the harness's permission classifier, and the card on disk is the audit trail. Members return a short summary; read their files, not their transcripts. A seat that hits its turn cap is resumed, not re-run.

### 3. Verify (one agent)

From the seat notes write `claims.md`: the load-bearing claims in priority order. Rank by diagnosticity first (a claim that, if false, flips a crux), then contested-between-seats, single-source, surprising, quantitative. Keep to the tier's claim budget and list what was left out. Spawn one `family-verifier` with `references/verifier-protocol.md`, `claims.md`, and the output path `verification.md`.

### 4. Synthesize (inline)

Read all seat files and `verification.md`. Write `report.md` per `references/report-template.md`. Then do the bottom-line check: every sentence in the bottom line maps to a claim number with a passing verdict, or carries an UNVERIFIED tag; a MISQUOTED or single-origin CIRCULAR claim cannot appear there however many seats liked it. Compute the seat metrics for the Cost section (unique URLs per seat, pairwise overlap, unique verified claims per seat); they are the only cheap evidence of whether a seat earned its budget.

### 5. Deliver

Reply with: the bottom line (three sentences max), the cruxes as a short list, one blind spot, the path to `report.md`, and the cost footer. Append one line to `family/runs.log` (date, slug, tier, seats, tokens, claims checked, downgraded, unique-verified-claims per seat). After ten or twenty runs that log is the eval this skill does not otherwise have.

## Depth tiers

| Tier | Seats | Searches / seat | Verifier claims | Agents spawned | Rough cost |
|---|---|---|---|---|---|
| `quick` | 1 research pass by the orchestrator inline, 8 searches | n/a | 6-8 | 1 (the verifier) | ~80K tokens |
| `standard` (default) | 3-5, typically 4 | 12 | 20 | seats + 1 | ~500K tokens, ~20 min wall (measured: 5 seats × 70-107K, verifier 70K) |
| `deep` | 5-6 | 18 | 30 | seats + 1, plus one anonymised feedback round (casting.md) | ~1M+ tokens; confirm with the user first |

Pick `standard` unless the user names a tier or the question is clearly small. When a run needs more, raise searches per seat before adding seats.

## Keeping the bill honest

- The agent count for the tier is the agent count. No helper agents, no "let me spawn an Explore to find sources", no re-running the whole crew because one seat was weak.
- Seats stop at their search budget and say what they did not cover.
- The verifier gets `claims.md`, never the seat notes.
- Member summaries are capped (250 words).
- Print the cost footer from real numbers.
- Do not pass a `model` override when spawning seats or the verifier unless the user asked for one in this run.

## Fallbacks

- `family-member` not resolvable in this session: spawn `general-purpose`, prepend "You have no permission to spawn subagents; do the work in this context" to the prompt, and keep everything else identical. This is a prompt guard, not a structural one (nested spawning is on by default up to three layers), so say so in the cost footer.
- No web search available: run `quick` only, and mark every claim UNGROUNDED. Do not pretend.

## Files this skill reads

- `references/casting.md` — the three casting moves, archetype cards, bench, diversity test, feedback round
- `references/seat-protocol.md` — what a seat does, its note schema, the seat card file, the spawn prompt
- `references/verifier-protocol.md` — two-axis verdicts, chasing to primary, the spawn prompt
- `references/report-template.md` — report structure and seat metrics
