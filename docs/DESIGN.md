# Design notes and evidence

This file says why each part of the skill is the way it is, which parts have evidence, which are untested, and where the numbers come from. The version 0.2.0 rewrite came out of running the skill on itself (`examples/family-skill-design/`): five seats read the skill files and the literature, a verifier opened 20 load-bearing sources (17 confirmed at the primary source, 3 partial), and the edits below follow that report.

## The six design choices

### 1. How the perspectives are generated

**Evidence.** STORM discovers perspectives by surveying related articles; it does not use a fixed list. In its ablation (Table 3, GPT-4), removing perspectives moved outline heading recall from 92.73 to 92.39, while removing the writer-expert conversation moved it to 88.75. Removing perspectives roughly halved the distinct sources found (Table 5: 99.83 vs 54.36). Solo Performance Prompting found dynamically identified personas beat a fixed generic set, and that detailed persona profiles added nothing over a name. No study compares a fixed archetype template against discovered seats, and none tests a cross-trade "outsider" seat on open-ended research; the nearest human evidence (design-analogy studies) favours near analogies for quality and far ones for novelty.

**What we did.** Three moves: discover evidence territories from how the field sections itself (STORM's move, one or two searches), one outsider from an unrelated trade chosen by structural analogy (on by default, marked experimental, only cast when the analogy points at a searchable corpus), then the archetypes renamed to the topic. Each run records per-seat unique verified claims so the outsider's value can be judged over runs instead of argued. In the self-review run the outsider (an intelligence-analysis methodologist) produced 6 of the 10 claims that only one seat found; that is one run on a topic close to its trade.

### 2. How many seats

**Evidence.** ChatEval's "3-4 roles peak" is ChatGPT on one evaluation benchmark, 60.0% to 62.5%. Averaging as few as three human analysts captured most of the gain of averaging fifty (Mandel, Karvetski and Dhami, 2018). Delphi panels of 3, 7 and 11 showed no accuracy difference (Rowe and Wright, 2001). In Anthropic's research system, token usage alone explained 80% of the performance variance on BrowseComp, and their lead prompt defaults to three subagents.

**What we did.** Three to five seats in `standard`, four by default, six only in `deep`; searches per seat is the quality knob and is raised before seats are added. The diversity test is on planned queries and source types, not on labels.

### 3. How detailed the seat card is

**Evidence.** Personas in system prompts do not improve accuracy (Zheng et al., EMNLP Findings 2024; the 2023 preprint of the same paper claimed the opposite, so cite the final version). Detailed profiles do not beat names (SPP). Anthropic's production notes say each worker needs "an objective, an output format, guidance on the tools and sources to use, and clear task boundaries", and that work should be divided by context boundaries rather than by role.

**What we did.** The biography is one line. The card's weight is on the territory (where to search, what evidence to trust), what to leave to other seats, a stop rule, and the first question.

### 4. Independent seats vs. debate

**Evidence.** Majority voting alone accounts for most of the gains attributed to multi-agent debate; debate alone does not improve expected correctness, though biasing belief updates toward correction helps (Choi, Zhu and Li, NeurIPS 2025). LLM agents conform to a majority (BenchForm, ICLR 2025). Parallel section-writing produced disjoint reports (LangChain Open Deep Research); Anthropic's lead prompt forbids delegating the final report. In Delphi studies the "reasons" feedback condition improved accuracy most, and discussion over-weights the eloquent.

**What we did.** Seats write blind; one synthesizer writes after all fieldwork. The deep tier's feedback round is anonymised, happens after verification, and a seat may only hold a position with a new source or concede by naming the verified claim that changed its mind.

### 5. A separate verification pass

**Evidence.** Production deep-research systems have citation accuracy of 40-80% and large fractions of unsupported statements (DeepTRACE, ICLR 2026). Independent parallel agents without central checking amplified errors 17.2x; centralised coordination contained it to 4.4x (Kim et al., 2025/2026). In MAST's taxonomy of multi-agent failures, missing or incorrect verification accounts for about 17% of failures, and adding task-objective verification improved one system by 15.6%. Intelligence analysts let a source's reliability leak into how much they believed the specific report (Kelly et al., 2025); the Admiralty code separates the two axes for that reason. In our first run the verifier downgraded 5 of 15 claims, two of them meaning-inverting, but labelled them PARTIAL, so the hard rule keyed on MISQUOTED never fired.

**What we did.** One batched verifier that receives the claims, not the notes; verdicts on two axes (fidelity/provenance, credibility); a quote inverted by truncation or stitching is MISQUOTED; only independent corroboration can raise a claim's weight; 20 claims in `standard`; per-seat downgrade rates.

### 6. Budget and model

**Evidence.** Anthropic's measured multi-agent system used an Opus lead with Sonnet subagents and outperformed single-agent Opus by 90.2% on their internal eval at about 15x the tokens of a chat; upgrading a model generation beat doubling the token budget. Claude Code's own cost guidance recommends Sonnet for teammates. Frontier models' errors are correlated even across providers (Kim, Garg, Peng and Garg, ICML 2025, one leaderboard dataset). With reasoning tokens held constant, single agents matched or beat multi-agent systems on multi-hop reasoning (Tran and Kiela, 2026).

**What we did.** The skill does not name a model; seats follow the user's subagent default, and the orchestrator does not pass a model override unless asked. Across our two runs, Sonnet seats gave a 5/15 downgrade rate with two inversions and Opus seats 3/20 with none, on different topics. Where the strongest model matters most, on the evidence, is the verifier and the synthesis.

## Things we removed and why

- **Codex "second model" seat.** Untested, harness-specific, and correlated errors across providers mean it buys less independence than it looks.
- **The user's belief in the shared brief.** Sycophancy channel; now only the skeptic's card carries it.
- **Assigned devil's advocate.** Replaced by a skeptic whose job is finding published dissent.
- **Inline three-persona `quick` tier.** One model wearing three hats, with the one evidenced step (verification) missing; now one research pass plus a small verifier.
- **Full-crew cross-examination.** Re-running every seat was the costliest step with the least evidence; now a targeted, anonymised feedback round after verification.

## Things we have not tested

The outsider seat, the discovered seat, the default headcount, the feedback round, and strongest-model-per-seat. `family/runs.log` accumulates per-run seat metrics (unique URLs, overlap, unique verified claims per seat, downgrade rate) so these can be judged after ten or twenty runs rather than argued. A `solo` baseline (one strong agent with the crew's total search budget plus the same verifier) is the comparison we would run first.

## References

- Shao et al. 2024. Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (STORM). NAACL. arxiv.org/abs/2402.14207
- Jiang et al. 2024. Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations (Co-STORM). EMNLP. arxiv.org/abs/2408.15232
- Wang et al. 2023. Unleashing the Emergent Cognitive Synergy in Large Language Models (Solo Performance Prompting). arxiv.org/abs/2307.05300
- Zheng et al. 2024. When "A Helpful Assistant" Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models. EMNLP Findings. arxiv.org/abs/2311.10054
- Chan et al. 2023. ChatEval. arxiv.org/abs/2308.07201
- Choi, Zhu, Li 2025. Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models? NeurIPS. arxiv.org/abs/2508.17536
- Weng et al. 2025. Do as We Do, Not as You Think: the Conformity Dynamics in LLM-Based Multi-Agent Systems (BenchForm). ICLR. arxiv.org/abs/2501.13381
- Kim et al. 2025/2026. Towards a Science of Scaling Agent Systems. arxiv.org/abs/2512.08296
- Venkit et al. 2025. DeepTRACE. ICLR 2026. arxiv.org/abs/2509.04499
- Cemri et al. 2025. Why Do Multi-Agent LLM Systems Fail? (MAST). arxiv.org/abs/2503.13657
- Kim, Garg, Peng, Garg 2025. Correlated Errors in Large Language Models. ICML. arxiv.org/abs/2506.07962
- Tran and Kiela 2026. arxiv.org/abs/2604.02460
- Sharma et al. 2023. Towards Understanding Sycophancy in Language Models. ICLR 2024. arxiv.org/abs/2310.13548
- Dhuliawala et al. 2023. Chain-of-Verification. arxiv.org/abs/2309.11495
- Anthropic 2025. How we built our multi-agent research system. anthropic.com/engineering/multi-agent-research-system
- Anthropic 2026. Building multi-agent systems: when and how to use them. claude.com/resources/articles/building-multi-agent-systems-when-and-how-to-use-them
- LangChain 2025. Open Deep Research. langchain.com/blog/open-deep-research
- Mandel, Karvetski, Dhami 2018. Boosting intelligence analysts' judgment accuracy: What works, what fails? Judgment and Decision Making 13(6).
- Kelly, Budescu, Dhami, Mandel 2025. The effect of source reliability and information credibility on judgments of information quality in intelligence analysis. Judgment and Decision Making 20.
- Nemeth, Brown, Rogers 2001. Devil's advocate versus authentic dissent. European Journal of Social Psychology. doi 10.1002/ejsp.58
- Rowe and Wright 2001. Expert opinions in forecasting: the role of the Delphi technique. In Principles of Forecasting.
- Mellers et al. 2014 and Hauenstein et al. 2025 on the Good Judgment Project (teaming effects contested between the two).
