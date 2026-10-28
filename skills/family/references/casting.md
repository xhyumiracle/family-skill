# Casting the crew

A seat is a search territory with a point of view attached: **what evidence it trusts and where that evidence lives**, **what it asks first**, and **what it is paid by**. Two seats that would run the same first three queries are one seat wearing two hats. Cast for different queries.

## How the crew gets cast: two moves, in order

### Move 1: Discover the territories (one or two searches)

Search for how the field already carves itself up: an overview, a survey, a "state of X" piece, a conference programme, a well-sectioned Wikipedia article on the topic or a sibling topic. Write down two things:

- **Territories**: the distinct places evidence lives (the issue tracker, the maintainer's release notes, the regulator's enforcement actions, the proceedings of one conference, the practitioners' forum, the filings, an archaeological record). A territory none of the five perspectives below would reach is a candidate seat; mark it "discovered" in the roster.
- **Starting sources**: the two or three canonical primary pages you just found. They go into `brief.md` so that no seat spends budget rediscovering them (in the first run, five seats all re-fetched the same official doc).

If the topic is too new or too private for overviews to exist, say so and skip. Do not invent a discovered seat from imagination.

### Move 2: Fill the five perspectives

Each perspective is one kind of evidence, taken from a published method, so the set applies to any question: a product, a policy, a historical event, a scientific claim, a personal decision. Together they triangulate in the sense of qualitative research methods: different data sources, different lenses, independent investigators (Denzin 1978; Patton 1999).

| Perspective | Who, in general | Where the method comes from |
|---|---|---|
| **First-hand** | the people closest to the evidence: users, participants, patients, the team that ran the experiment, the people who lived through it; for history, contemporaries and primary sources | argument from position to know (Walton, Reed, Macagno 2008); data-source triangulation |
| **Expert** | the people who explain how and why: builders, clinicians, scientists, scholars of the subject | argument from expert opinion (Walton et al.); the "expert" role in Critical Systems Heuristics (Ulrich 1983) |
| **Stakes** | the people who decide, pay, benefit, or bear the consequences: investors, buyers, regulators, employers, funders, those affected without a say | the beneficiary, decision-maker and witness-for-the-affected roles in Critical Systems Heuristics (Ulrich 1983) |
| **Dissent** | the strongest published case against the prevailing answer in the field (and against the user's belief, if they stated one), named after the real dissenting group | minority dissent widens search and thinking in a group (Nemeth 1986); authentic dissent beat every form of assigned devil's advocate (Nemeth, Brown, Rogers 2001); structured dissent beat expert-only approaches (Schweiger, Sandberg, Ragan 1986; Schwenk 1990); one dissenting answer reduced LLM conformity to a majority (Zhu et al., ACL 2025) |
| **Outside view** | someone from another field that has handled the same structure, bringing how comparable cases usually turned out | the outside view and reference-class forecasting (Kahneman, Lovallo 1993; Flyvbjerg 2006) |

How to fill them on a given question. Generate the candidates from the question and pick the team for relevance and difference together: in AgentInit (EMNLP 2025 Findings) teams generated from the query and chosen on the Pareto front of task relevance and team diversity beat predefined roles, and either criterion alone did worse. Here the five perspectives are the diversity axis and the question supplies relevance:

- **Write one or two candidates per perspective**, each a real job or source for this question, then keep the one per perspective whose territory is most relevant and least like the others'. A perspective with no relevant candidate is dropped or replaced, which can leave fewer than five; that is allowed (AgentInit's selected teams averaged two to three agents out of a possible five).

- **Name each as a real job or source for this question**, two to five words: "a healthy CGM user three months in", "a late-Roman historian", "an industry VC", "the MOND researchers". A real job carries its territory and its incentive in the name.
- **Stakes** takes whichever of decides / pays / benefits / bears the consequences the question turns on. When nobody real has a stake (a pure science or history question), fill the seat by method triangulation instead: a second discipline or method that reads different evidence (the archaeologist next to the historian, the simulation group next to the detector group), and say so in the roster.
- **Dissent** takes the prevailing answer in the field as its target, so it works on questions with no stance; it is also the only seat told the user's current belief (on its card, not in the brief). It finds the strongest published dissent and does not invent objections; contrarian claims without sources go under "Positions I hold without evidence". Never dropped.
- **Outside view**: write the problem's structure in one sentence with the nouns removed ("one question, several independent estimators with different information, then aggregation"; "a medical sensor sold to healthy people"), name a field that has lived with that structure for decades, and cast from it only if that field has a searchable corpus of cases, rules or post-mortems. It brings base rates and the field's rules; it does not estimate quantities in the target field, and its claims about the target field go through the verifier like everyone else's. Mark it "experimental": the outside view has evidence in forecasting, a cross-field seat in LLM research has none yet. If no analogy is credible, write "no credible outside view" and run four.
- **A territory from Move 1** replaces the perspective whose material overlaps most with another seat's on this question; it never adds a sixth.
- **Never invent a holder.** A perspective with nobody real behind it is replaced or left out.

Persona detail beyond the job title adds nothing (SPP; Zheng et al.): what a seat finds depends on its territory. A category with qualifiers bolted on ("an analyst who reads pricing pages like filings") is the same seat said badly, and invented colour ("woken at 3am by a failed signature") is noise.

### Headcount

Five in `standard` and `deep` (four perspectives plus the outside view), three in `mini` (dissent plus the two perspectives most relevant to the question). Averaging three independent analysts captured most of the gain of averaging fifty (Mandel et al. 2018) and Delphi panels of 3, 7 and 11 showed no accuracy difference (Rowe, Wright 2001), while every seat costs 70-110K tokens; nothing shows six beats five. Never six. `deep` adds rounds, not seats. Searches per seat is the quality knob. The specific combination of five has no controlled study behind it; `family/runs.log` records each seat's unique confirmed claims and `references/eval.md` holds the leave-one-seat-out design that can test it.

## The five perspective cards

Each card names where the seat looks and what it is paid by. Rename it to the topic before spawning.

### 1. First-hand (亲历者)
- **Trusts:** direct accounts and raw records: user reports, forums, support tickets, field notes, datasets and lab logs, diaries, contemporary accounts, primary sources.
- **Asks first:** what do the people closest to it actually see?
- **Paid by:** their own experience.
- **Edge:** tacit knowledge, failure modes nobody writes papers about, the gap between the claim and the practice.
- **Misses:** the mechanism, the base rate, how their own position bends what they see.

### 2. Expert (内行)
- **Trusts:** peer review, replication, effect sizes, ablation tables, technical documentation. Papers, surveys, meta-analyses, textbooks, design docs, reports with methods sections.
- **Asks first:** what does the best available evidence say about how and why, what was the baseline, and how big was the effect?
- **Paid by:** being right in print, or the thing working.
- **Edge:** grading evidence, separating mechanism from anecdote, knowing which results failed to replicate or reversed between versions.
- **Misses:** anything too new or too commercial to be published; what first-hand people already know.

### 3. Stakes (利益相关方)
- **Trusts:** who decides, who pays, who benefits, who bears the cost. Filings, funding, pricing, budgets, policy documents, regulations, contracts, hiring data, impact assessments.
- **Asks first:** who wins and who loses depending on the answer, and what are they doing about it?
- **Paid by:** their position: money, power, or the consequences they live with.
- **Edge:** incentive mapping, what the people with power need you to believe, the consequences for those affected without a say.
- **Misses:** value nobody pays for, slow science. With no stakes at all on the question, swap this seat for a second method (Move 2).

### 4. Dissent (异见)
- **Trusts:** the strongest version of the opposite case as it already exists in print: critics with a track record, retractions, failed replications, lawsuits, negative reviews, the communities that chose the other way.
- **Asks first:** what is the prevailing answer here, who has argued with evidence that it is wrong, and what is their best case?
- **Paid by:** catching the error before it costs something.
- **Edge:** this is the only seat told the user's current belief (on its card, not in the brief), and it attacks the belief with published dissent. In Nemeth, Brown and Rogers (2001) authentic dissent beat all three forms of assigned devil's advocate; their earlier work found assigned advocates mostly make people bolster the original view.
- **Misses:** upside. A dissent seat with vibes and no sources is useless; contrarian claims without evidence go under "Positions I hold without evidence".

### 5. Outside view (外部视角)
- **Trusts:** comparable cases from a field that has handled the same structure: their records, base rates, rules and post-mortems; earlier waves of the same idea.
- **Asks first:** how did comparable cases usually turn out?
- **Paid by:** pattern and precedent; suspicious of "this time is different".
- **Edge:** base rates, the rules that field paid to learn, the names of the last three things that promised this.
- **Misses:** genuine novelty. Any number about the target field must come from target-field evidence.

The dissent seat is never dropped.

## The bench (jobs to pull from when a card does not fit)

- **An industry VC** (stakes): trusts rounds, exits, who got bought and why. Asks: what does this look like in five years if it works, and who gets to own it?
- **A procurement security officer who writes the RFPs** (stakes): trusts what buyers put in a requirements list and what they sign. Asks: would this get past my checklist, and would anyone pay for it?
- **A regulator or a lawyer in the field** (stakes): trusts statutes, enforcement actions, court filings. Asks: what is actually allowed, and who has been punished?
- **A paying customer in month four** (first-hand): trusts their own time and money. Asks: would I keep paying for this?
- **An engineer who would build it themselves** (expert): trusts what they could ship. Asks: what is the simplest thing that does 80% of this, and why did they not do that?
- **A journalist on this beat** (dissent or first-hand): trusts documents and on-record sources, distrusts press releases. Asks: who benefits from me believing this?
- **Someone who worked inside and left** (first-hand): trusts what they saw. Asks: what does everyone inside know and nobody say?
- **A headhunter in the field** (stakes): trusts who is hiring for what. Asks: which roles are being staffed and which are disappearing?
- **A historian of the field** (outside view): trusts archives and previous waves. Asks: when did this happen before, and how did it end?
- **The local version**: the China / EU / specific-jurisdiction holder of any perspective.
- **An incident investigator** (first-hand or dissent): trusts harm reports and post-mortems. Asks: who got hurt when this went wrong at scale?

## Fitting the cast to the topic (hypothetical rosters, not runs)

**"Obsidian sync for an agent-written vault"** → First-hand: someone who ran LiveSync on a VPS for a year. Expert: a distributed-systems researcher on conflict semantics. Stakes: replaced by the discovered territory *the LiveSync maintainer's release notes and troubleshooting docs* (nobody pays or decides here beyond the user). Dissent: people who run agents against vaults without live sync, told the user's belief "the VM must hold a live synced copy". Outside view: a CI engineer who runs bots and humans committing to one repo (two writers, one shared tree, delayed visibility).

**"Why did the Western Roman Empire fall?"** → First-hand: a classicist who works from the contemporary sources (Ammianus, Salvian). Expert: a late-Roman historian. Stakes: nobody alive has a stake, so a second method: an archaeologist of the material record (pottery, coinage, settlement). Dissent: the "transformation, not fall" school of late antiquity. Outside view: comparative researchers of societal collapse (other empires' trajectories).

**"Are prediction markets a usable information source for policy forecasting?"** → First-hand: a market maker who provides liquidity. Expert: a quant who studies manipulation. Stakes: a regulator who rules on event contracts. Dissent: the researchers who argue thin liquidity makes prices unreadable, told the user's belief. Outside view: forecast verification in meteorology (probabilities people want to read as truth; Brier scores are the trade's rule).

## Diversity test (run before spawning)

For each proposed seat write its first three planned queries and the source types it will open. If two seats would run the same first queries, they are one seat: merge them and fill the gap from the bench. If every seat's sources are web articles, you have five bloggers; push at least two seats toward primary material (papers, filings, repos, data). The "trusts / asks first / paid by" lines are the means of generating different queries, not the test.

## Evidence rounds (at most 1 in standard, up to 3 in deep; after verification)

Not a debate. Each round is a Delphi round over verified evidence: an anonymised crux list (each side with its verified claims and verdicts) plus at most two gap questions, sent to the seats that are party to a crux or own the gap's territory, with 4 searches each. A seat may hold with a new source, concede by naming the verified claim that changed its mind, or reframe; nothing else counts. No seat names, no position statements passed along, no contact with seats still working. The verifier is resumed for the new claims. Another round runs only if the last one moved a crux (a lean changed, an empty side was filled, a concession was made); a round that moves nothing ends it, three is the cap. "Until the seats agree" is never the rule: seats of one model agreeing is conformity, not evidence.
