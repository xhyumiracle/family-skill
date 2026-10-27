# Casting the crew

A seat is a search territory with a point of view attached: **what evidence it trusts and where that evidence lives**, **what it asks first**, and **what it is paid by**. Two seats that would run the same first three queries are one seat wearing two hats. Cast for different queries.

## How the crew gets cast: three moves, in order

The fixed "practitioner / academic / trader / historian / skeptic" list is a community template, not a measured optimum. The two moves that give a crew its coverage come first; the template fills what is left.

### Move 1 — Discover the territories (one or two searches)

Search for how the field already carves itself up: an overview, a survey, a "state of X" piece, a conference programme, a well-sectioned Wikipedia article on the topic or a sibling topic. Write down two things:

- **Territories**: the distinct places evidence lives (the issue tracker, the maintainer's release notes, the regulator's enforcement actions, the proceedings of one conference, the practitioners' forum, the filings). Each territory a generic template would not name is a candidate seat; keep one or two. Mark them "discovered" in the roster.
- **Starting sources**: the two or three canonical primary pages you just found. They go into `brief.md` so that no seat spends budget rediscovering them (in the first run, five seats all re-fetched the same official doc).

If the topic is too new or too private for overviews to exist, say so and skip. Do not invent a discovered seat from imagination.

### Move 2 — Outsider from an unrelated trade (on by default, experimental)

Write the problem's structure in one sentence with the nouns removed. "Two writers, one shared file, no lock, delayed visibility, deletions propagate." "One question, several independent estimators with different information, then aggregation." "A gatekeeper whose incentives differ from the people it screens." Then ask which trade has lived with exactly that structure for decades, and what rules it paid to learn.

Cast the seat only if the analogy points at a **searchable corpus** of that trade's rules, standards or post-mortems (CI engineering for bots and humans on one repo; intelligence tradecraft for independent estimators and source grading; aviation checklists for medical error). The outsider brings those rules and the trade's accident record; it does not estimate quantities in the target field, and any claim it makes about the target field goes through the verifier like everyone else's.

Mark it "experimental" in the roster. No controlled study has tested cross-trade seats in LLM research; human design studies find far analogies raise novelty and near ones raise quality. Single-run seat counts cannot judge it either (they depend on which claims the orchestrator chose to verify); the leave-one-seat-out arm in `references/eval.md` can. If no analogy is credible, write "no credible outsider" and fill from the archetypes.

### Move 3 — Fill with real jobs

Every seat is named after a job someone actually holds, in two to five words: "an industry VC", "a procurement security officer who writes the RFPs", "a trader who has followed this for years", "a historian of the field". A real job carries its territory and its incentive in the name. A category with qualifiers bolted on ("an analyst who reads pricing pages like filings") is the same seat said badly, and invented colour ("woken at 3am by a failed signature") adds nothing: persona detail beyond a name does not change what a seat finds (SPP), the territory does.

The crew is four fixed seats plus the two dynamic ones from moves 1 and 2. The fixed seats are defined by evidence territory, not by job, because what the evidence rewards is seats that read different material (STORM's perspectives doubled distinct sources; persona detail adds nothing; the diversity-prediction argument that collective error falls with the diversity of independent inputs). Four territories exist for almost any question, read material that does not overlap, and cannot be found by a discovery search, so they are fixed:

- **uses it**: the people who live with it (reviews, forums, support tickets, whether they still pay in month four); the job is a user of the thing in this field;
- **builds it**: the people who make or run it (code, issue trackers, design docs, post-mortems); the job is an engineer, an operator, a clinician, whoever does it for a living;
- **bets on it**: the people with money at stake (funding, exits, pricing pages, budgets); the job is an industry VC, a buyer, or a manager with the budget, whichever the question turns on;
- **picks it apart**: the skeptic, who hunts published opposition (authentic dissent beats assigned advocacy).

Study, rules and precedent (researchers, regulators, historians) are also common territories, but they are the ones a discovery search finds, so they take the dynamic seat when they matter. Fixed seats also keep rosters comparable across runs, which the eval in `references/eval.md` needs. Dynamic: the outsider, always; the discovered territory, when Move 1 finds one not already covered. That is five or six. No specific fixed list has experimental support, including this one; `family/runs.log` records each seat's unique confirmed claims so the choice can be tested later rather than argued. The five archetype cards below are the incentive checklist behind the fixed seats, not names to use.

### Headcount

Run the diversity test after the three moves. Headcount is five or six by construction (four fixed, the outsider, and the discovered seat when Move 1 finds one); it drops to five when there is no credible outsider analogy and no discovered territory at once only in a field so small that two fixed seats would read the same material, in which case merge them. In the roster, each seat is its job title plus at most one clause; the territory lines live on the card, not in the table. The numbers people quote for "optimal" are narrow: ChatEval peaked at 3-4 roles on one evaluation benchmark with ChatGPT (60.0 → 62.5%); averaging three human analysts captured most of the gain of averaging fifty; Delphi panels of 3, 7 and 11 showed no accuracy difference. None of that says five is right, and an eval of twenty questions cannot tell four seats from five. Searches per seat is the quality knob; add a seat only when its territory is one no other seat touches, and do not tune headcount from single runs.

## The five default archetypes

Each card names where the seat looks. Rename it to the topic before spawning.

### 1. Practitioner (从业者)
- **Trusts:** what ships, what breaks, what people complain about after six months. Changelogs, issue trackers, postmortems, forum threads by people who have done it, job postings, support docs.
- **Asks first:** who uses this every day, and what do they curse at?
- **Paid by:** getting the thing to work.
- **Edge:** tacit knowledge, failure modes nobody writes papers about, the gap between the demo and the Tuesday.
- **Misses:** long cycles, theory, how their own trade's incentives bend what they see.

### 2. Researcher (研究员)
- **Trusts:** peer review, pre-registration, replication, effect sizes, ablation tables. Papers, surveys, meta-analyses, leaderboards, technical reports with methods sections.
- **Asks first:** what does the best available evidence say, what was the baseline, and how big was the effect?
- **Paid by:** being right in print.
- **Edge:** grading evidence, separating mechanism from anecdote, knowing which results failed to replicate or reversed between versions.
- **Misses:** anything too new or too commercial to be published; speed; what practitioners already know.

### 3. Market / Incentives (交易员)
- **Trusts:** prices, flows, who is paying whom. Filings, funding rounds, pricing pages, earnings calls, hiring data, prediction markets, contract terms.
- **Asks first:** who has money at stake here, and what are they actually betting?
- **Paid by:** being early and right; respects base rates because being wrong is expensive.
- **Edge:** incentive mapping, timing, calibrated scepticism of hype, what the sellers need you to believe.
- **Misses:** value that is not monetised, slow science, things with no market yet.
- Rename to *Economist* or *Incentives analyst* for topics without a market.

### 4. Historian (历史学家)
- **Trusts:** primary documents and long time series. Archives, old papers, retrospectives, Wikipedia "History" sections and talk pages, obituaries of failed projects, previous waves of the same idea.
- **Asks first:** when did this happen before, and how did it end?
- **Paid by:** pattern and precedent; suspicious of "this time is different".
- **Edge:** cycles, base rates, path dependence, the names of the last three things that promised this.
- **Misses:** genuine novelty.

### 5. Skeptic (怀疑论者) — the authentic-dissent seat
- **Trusts:** the strongest version of the opposite case as it already exists in print: critics with a track record, retractions, failed replications, lawsuits, negative reviews, the communities that chose the other way.
- **Asks first:** who has argued, with evidence, that the mainstream story is wrong, and what is their best case?
- **Paid by:** catching the error before it costs something.
- **Edge:** the skeptic is the only seat told the user's current belief (on its card, not in the brief) and attacks it by finding published dissent, not by inventing objections. In Nemeth, Brown and Rogers (2001) authentic dissent beat all three forms of assigned devil's advocate; their earlier work found assigned advocates mostly make people bolster the original view.
- **Misses:** upside. A skeptic with vibes and no sources is useless; contrarian claims without evidence go under "Positions I hold without evidence".

The skeptic is never dropped.

## The bench (jobs to pull from when an archetype does not fit)

- **An industry VC** — trusts rounds, exits, who got bought and why. Asks: what does this look like in five years if it works, and who gets to own it?
- **A procurement security officer who writes the RFPs** — trusts what buyers put in a requirements list and what they sign. Asks: would this get past my checklist, and would anyone pay for it?
- **A regulator or a lawyer in the field** — trusts statutes, enforcement actions, court filings. Asks: what is actually allowed, and who has been punished?
- **A paying customer in month four** — trusts their own time and money. Asks: would I keep paying for this?
- **An engineer who would build it themselves** — trusts what they could ship. Asks: what is the simplest thing that does 80% of this, and why did they not do that?
- **A journalist on this beat** — trusts documents and on-record sources, distrusts press releases. Asks: who benefits from me believing this?
- **Someone who worked inside and left** — trusts what they saw. Asks: what does everyone inside know and nobody say?
- **A headhunter in the field** — trusts who is hiring for what. Asks: which roles are being staffed and which are disappearing?
- **The local version** — the China / EU / specific-jurisdiction practitioner.
- **The user five years on** — asks which of today's concerns will have mattered.
- **An incident investigator** — trusts harm reports and post-mortems. Asks: who got hurt when this went wrong at scale?

## Fitting the cast to the topic (hypothetical rosters, not runs)

**"Obsidian sync for an agent-written vault"** → Discovered: *the LiveSync maintainer's release notes and troubleshooting docs as a territory*. Outsider: *a CI engineer who runs bots and humans committing to one repo* (two writers, one shared tree, delayed visibility). Archetypes: a practitioner who ran LiveSync on a VPS for a year; a distributed-systems researcher on conflict semantics; the skeptic, whose card carries the user's belief "the VM must hold a live synced copy" and whose first job is to find people who run agents against vaults without live sync. Four or five seats. (The actual first run used the five renamed archetypes on this topic; this roster is what the three moves would produce.)

**"Are prediction markets a usable information source for policy forecasting?"** → Discovered: *market makers and liquidity providers* (every overview has a section on liquidity). Outsider: *forecast verification in meteorology* (a thin market whose prices people want to read as probabilities; Brier scores are the trade's rule). Archetypes: a quant on manipulation; a historian of Iowa Electronic Markets; the skeptic, told the user's belief "liquidity is too thin to trust". Bench: swap the historian for a regulator if the question is about legality.

## Diversity test (run before spawning)

For each proposed seat write its first three planned queries and the source types it will open. If two seats would run the same first queries, they are one seat: merge them and fill the gap from the bench. If every seat's sources are web articles, you have five bloggers; push at least two seats toward primary material (papers, filings, repos, data). The "trusts / asks first / paid by" lines are the means of generating different queries, not the test.

## Gap rounds (at most 1 in standard, at most 3 in deep; after fieldwork, before verification)

Co-STORM's moderator raised questions from material that had been retrieved but not cited, and its ablation says the moderator mattered more than the number of experts (small differences on an LLM-judge scale, no significance test, and third-party re-runs found Co-STORM's source diversity below STORM's; so borrow the mechanism, not the architecture). Here the mechanism runs once, after every seat has finished, from the seats' own "Read but not cited" and "Deliberately not examined" sections.

Rule, written in the brief before fieldwork: fire only if a sub-question has no direct evidence from any seat, or a named gap would change the bottom line if filled. Write at most two questions. Each names the territory and a budget of 4 searches and carries no finding from any seat and no lean of the orchestrator's. Resume the one or two seats whose territory fits (the message template is in seat-protocol.md). Record trigger, questions and seats in `amendments.md`. Resumed seats append "## Post-gap" to their notes; the claims go through the verifier like all others. In deep, another round runs only if the last one moved a crux (changed a lean or filled an empty side); a round that touches no crux ends the loop, and three rounds is the cap. No debate, no messages to seats that are still working, and never "until the seats agree": seats of one model agreeing is conformity, not evidence.
