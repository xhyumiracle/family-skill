# Brief — Which design choices in a multi-perspective research pipeline have evidence behind them?

## Question
For an LLM-agent research pipeline that casts several independent perspective-seats on one question and then sends a separate agent to verify sources (the STORM pattern run as parallel subagents), which design choices have evidence behind them and which are folklore? Concretely: (a) how the set of perspectives should be generated (fixed archetype template vs. discovered from how the field sections itself vs. one seat cast from an unrelated trade by structural analogy); (b) how many seats; (c) how detailed a seat card needs to be; (d) blind-independent seats vs. debate or a cross-examination round; (e) whether a separate source-verification pass is worth its cost; (f) what depth and budget are worth paying for, including whether the strongest model per seat pays off.

## What it is for
Revising the owner's own Claude Code skill, `family`. Every seat must read the skill's files and critique the actual artifact, not the idea in general:
- /home/xhyumiracle/.claude/skills/family/SKILL.md
- /home/xhyumiracle/.claude/skills/family/references/casting.md
- /home/xhyumiracle/.claude/skills/family/references/seat-protocol.md
- /home/xhyumiracle/.claude/skills/family/references/verifier-protocol.md
- /home/xhyumiracle/.claude/skills/family/references/report-template.md
The deliverable is a map of the evidence plus concrete, file-level change proposals (keep / change / add / remove), each tied to a source or explicitly marked as judgment.

## Constraints
- Literature and engineering reports from 2023 to October 2026. Prefer primary sources: papers with ablations and effect sizes, engineering posts with measured numbers, repositories that report runs. Flag pre-2024 results as possibly outdated by model improvements.
- The harness is Claude Code: seats are subagents that run in parallel, have web search and fetch, cannot spawn sub-agents, and write notes to disk; an orchestrator synthesizes. Advice that needs a different harness is out of scope unless it is a cheap change.
- Out of scope: coding agents, agent frameworks (AutoGen, CrewAI, LangGraph) as products, prompt-injection security, long-form article generation. In scope only where such work reports evidence about the six design choices above.

## Known facts (all seats start from these)
- STORM (Shao et al., NAACL 2024): perspective-guided question asking plus simulated writer-expert conversations, grounded in retrieved sources. Reported +25% absolute on "well organized" and +10% on "broad coverage" vs. an outline-driven retrieval baseline, judged with experienced Wikipedia editors. The original method discovers perspectives by surveying related articles; it does not use a fixed persona list. Co-STORM (EMNLP 2024) adds a moderator and a shared mind map.
- The skill's first real run (2026-10-27, Obsidian sync topic): 5 seats + 1 verifier, 482K subagent tokens, about 20 minutes wall; seats used 70-107K tokens each. The verifier opened all 15 cited sources and downgraded 5 claims to PARTIAL; two of those changed the meaning of a claim (a truncated maintainer quote that inverted the maintainer's position; "atomic writes fixed it" was actually "routing writes through an MCP server"). Seats disagreed on four cruxes; no unanimity.
- Prior art on GitHub (all 0-6 stars): hadufer/claude-storm, HirogaKatageri research plugin, mediagato/storm-research (user approves the perspective list first), zrabin/panel-skill (diversity-enforced lenses, one batched verifier, light ~200K tokens; its README cites Zheng et al. 2023 on personas not reliably helping, Wang et al. SPP on bare persona names working as well as detailed profiles, Chan et al. ChatEval on diverse roles beating identical roles with accuracy peaking at 3-4 roles, and states that on short artifacts a single strong agent finds about as much, the measurable edge being verification and severity calibration), Kanorin-chan/perspectives-skill (re-casts if every persona agrees).
- Anthropic's engineering post "How we built our multi-agent research system" (anthropic.com/engineering/multi-agent-research-system) exists; secondary summaries attribute to it a >90% improvement over single-agent on an internal eval with an Opus lead and Sonnet subagents, and roughly 15x token use vs. chat. Seats should verify figures against the original.
- Two 2025 surveys organise the field as actors / interaction types (cooperation, competition, debate) / structures / strategies (role-based, rule-based, model-based) / coordination (Tran et al., arXiv 2501.06322) and as communication architecture and protocols (arXiv 2502.14321).

## Owner's current belief
Two beliefs, both to be attacked by the skeptic: (1) casting one seat from an unrelated trade by structural analogy, plus discovering one or two topic-native seats from how the field sections itself, produces better research than a fixed five-archetype template; (2) running seats on the strongest available model is worth the cost.

## Output language
Chinese for notes and the report; quotes stay in their original language.
