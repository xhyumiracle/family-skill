# Brief — What should change in family v0.3?

## Question
Given the `family` skill at v0.2.0 (files below) and the evidence gathered when the skill reviewed itself once already (round-1 report below), what should change in v0.3? Five sub-questions: (a) the orchestrator's role: Co-STORM reports that removing the moderator hurts more than cutting the number of experts, and family's orchestrator never intervenes between casting and synthesis; should it steer mid-run, and how, without turning seats into a debate? (b) evaluation: what would a 10-20 question eval with rubrics look like for this skill, and which metric would actually discriminate between seat configurations (3 vs 4 vs 5 seats, outsider on/off, model tiers)? (c) is the two-axis verifier verdict and the 20-claim budget a net gain or noise? (d) is the report template load-bearing for a reader who has to act on it in ten minutes, and what is clutter? (e) what in v0.2.0 is over-engineering that should be cut?

## What it is for
Deciding the v0.3 edits of an open-source Claude Code skill (github.com/xhyumiracle/family-skill). Every seat must read the v0.2.0 files and critique the artifact, not the idea:
- /home/xhyumiracle/projects/xhyu/family-skill/skills/family/SKILL.md
- /home/xhyumiracle/projects/xhyu/family-skill/skills/family/references/casting.md
- /home/xhyumiracle/projects/xhyu/family-skill/skills/family/references/seat-protocol.md
- /home/xhyumiracle/projects/xhyu/family-skill/skills/family/references/verifier-protocol.md
- /home/xhyumiracle/projects/xhyu/family-skill/skills/family/references/report-template.md
- Round-1 self-review report (what v0.2.0 was built from): /home/xhyumiracle/projects/xhyu/family/family-skill-design/report.md
- Both runs' metrics: /home/xhyumiracle/projects/xhyu/family/runs.log
Deliverable: file-level change proposals (keep / change / add / remove), each tied to a source or marked judgment.

## Constraints
- 2024 to October 2026 literature and engineering reports; primary sources preferred (papers with tables, benchmark repos, rubric definitions, engineering posts with numbers). Do not re-litigate round 1's settled points (blind seats, one verifier, seats as territories) unless you have new evidence; cite the round-1 report row instead.
- Harness: Claude Code subagents, parallel, web search + fetch, no nested spawning; the orchestrator is the main session and can read files and spawn once. Proposals must fit that.
- Out of scope: coding agents, agent frameworks as products, long-form article generation.

## Known facts
- v0.2.0 shipped 2026-10-27 after round 1: seats are search territories, user belief only to the skeptic, two-axis verifier (fidelity/provenance + credibility), MISQUOTED-INVERTED rule, 20-claim budget, deep-tier anonymised feedback round, quick tier = one inline pass + small verifier, report with Estimates table and seat metrics, runs.log.
- Round 1: 5 seats (opus) + verifier, 606K subagent tokens, 20/20 claims checked, 17 PRIMARY-CONFIRMED, 3 PARTIAL. The outsider (intelligence tradecraft) produced 6 of the 10 single-seat verified claims. Round 0 (Obsidian topic, sonnet seats): 15 checked, 5 PARTIAL, two meaning-inverting quotes labelled PARTIAL instead of MISQUOTED.
- Co-STORM (Jiang et al., EMNLP 2024, arXiv 2408.15232): a moderator that raises questions from unused information steers the discourse; ablations with one expert + moderator and with multiple experts but no moderator both underperform the full system, and removing the moderator hurts more (from the paper's text as summarised in search; seats should verify the table).
- Deep-research evaluation in 2026 is rubric-based: DeepResearch Bench (ICLR 2026, 100 tasks, 22 domains, report quality + citation accuracy, human-alignment study), ResearchRubrics (ICLR 2026; leading systems under 68% rubric compliance), Dr. Bench (arXiv 2510.02190), LiveResearchBench (ICLR 2026). Surveys: arXiv 2506.18096, 2508.12752.
- The skill never names a model; seats follow the user's subagent default.

## Starting sources (already known; do not spend budget rediscovering)
- https://arxiv.org/abs/2408.15232 (Co-STORM)
- https://arxiv.org/abs/2506.11763 (DeepResearch Bench)
- https://mlanthology.org/iclr/2026/sharma2026iclr-researchrubrics/ (ResearchRubrics)
- https://arxiv.org/abs/2510.02190 (Dr. Bench)
- https://www.anthropic.com/engineering/multi-agent-research-system

## Output language
Chinese for notes and report; quotes stay in their original language.
