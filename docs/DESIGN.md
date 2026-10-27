# Design notes and evidence

Why each part of the skill is the way it is, which parts have evidence, which are untested, and where the numbers come from. Bracketed numbers match the footnotes in the README; the full list is at the end.

The skill has audited itself twice. Round 1 (on v0.1.0) produced v0.2.0: seats as search territories, the user's belief only to the skeptic, a verifier with a two-axis verdict, an estimates table, seat metrics, a feedback round. Round 2 (on v0.2.0, `examples/family-skill-v03/`) found that four of those additions had never run, that the seat metrics depended on which claims the orchestrator chose to verify, and that the orchestrator's own bottom line had passed a stitched number through the check. v0.3.0 is the result of round 2. Both runs are on disk with their briefs, seat notes, claims lists and verification tables.

## 1. Independent seats, one writer

**Evidence.** Majority voting alone accounts for most of the gains attributed to multi-agent debate; debate alone does not improve expected correctness, though biasing belief updates toward correction helps [1]. When current open models are exposed to a unanimous wrong majority mid-task they abandon 22.8% (MMLU) to 71.0% (SimpleQA) of their correct answers, and authority labels pull answers toward the endorsed one regardless of correctness [2]. Parallel section-writing produced disjoint reports at LangChain; Anthropic's lead prompt forbids delegating the final report [15]. Independent parallel agents without a central check amplified errors 17.2x in a 260-configuration study; centralised coordination contained it to 4.4x [16].

**What we did.** Seats write blind and nobody messages them during fieldwork; the harness allows it, so the rule is explicit. One synthesizer writes after all fieldwork. Blind seats also give a free experimental design: any subset of one run approximates a smaller crew (see §9).

## 2. Seats as search territories

**Evidence.** Personas in system prompts did not improve accuracy on 2,410 factual questions across four model families [3]; a 2025 retest on six models found the same null for in-domain expert personas and harm from low-knowledge ones [3]. Detailed persona profiles added nothing over a bare name [4]. In STORM's ablation, removing perspectives moved outline recall from 92.73 to 92.39 but roughly halved distinct sources found (99.83 vs 54.36); removing the follow-up conversation hurt more (88.75) [5]. Anthropic's production notes: each worker needs "guidance on the tools and sources to use" and a boundary, and work should be split by context, not by role [5] [15].

**What we did.** The card's weight is on where to search, what evidence to trust, what to leave to other seats, and a stop rule. The biography is one line. The diversity test compares planned queries and source types, not labels.

## 3. The user's belief, the skeptic, and the outsider

**Evidence.** A stated belief pulls answers toward it: up to 27% on 2023 models [6], and a 2026 frontier model still changed right answers to wrong ones in 23.8% of objective scenarios to please the user [6]. Authentic dissent beat every form of assigned devil's advocate [7]. Delphi panels of 3 to 11 showed no accuracy difference, and averaging three independent analysts captured most of the gain of averaging fifty [17] [18]. No controlled study has tested a cross-trade "outsider" seat on LLM research; single-run seat counts cannot judge it because they depend on which claims the orchestrator verified (round 2, evaluator and skeptic seats).

**What we did.** The belief goes only to the skeptic's card. The skeptic's job is to find published dissent. The outsider is on by default, marked experimental, and judged by the eval design in `references/eval.md`, not by run counts. Default headcount is four; an eval of twenty questions detects only large effects [19], so headcount is not tuned from runs.

## 4. The verifier

**Evidence.** Production deep-research systems cite correctly 40-80% of the time and carry large fractions of unsupported statements [8]. Fine-grained verdict scales do not reproduce: professional fact-checkers diverged on 30.4% of 749 matched claims, with rating granularity the largest single cause (98 of 228), and merging ratings to two levels lifted agreement only from 69.6% to 74.2% [9]; in the Admiralty two-axis system the skill's v0.2.0 verifier copied, 87% of 695 field ratings fell on the diagonal and one cell held 75% of them (Baker 1968, as summarised by Icard 2024) [10]; an LLM judge re-run three times on the same input gave the same binary label only 61-79% of the time, and majority vote over runs beat the best single run [10]; structured GRADE criteria raised inter-rater agreement from about 0.3 to about 0.7 in one study, while GRADE applied in real reviews reached only κ 0.18-0.44 in another: either way, fine-grained certainty labels are unreliable [10]. Indirectness (evidence from other models, tasks, populations or years) is a named GRADE domain, and in round 1 at least six of seventeen confirmed claims carried such a caveat with no place in the labels to record it (round 2, grade seat). The two-axis verdict in v0.2.0 never ran: round 1's table had a single verdict column (round 2, all five seats).

**What we did.** Four verdicts (CONFIRMED primary/secondary, PARTIAL, MISQUOTED inverted/stitched/absent, NOT-VERIFIED), two flags only with evidence (CIRCULAR, CONTRADICTED), a direct/indirect mark with a reason, a source-risk phrase that never raises a verdict, and a mechanically derived "eligible" column. Every PARTIAL or MISQUOTED quotes the original and adjacent sentence so a reader can re-judge. Twenty claims in `standard`: round 1's downgrades sat at positions 14, 15 and 18 of 20, so a 15-claim budget would have missed them. Counter-evidence searches only for high-risk sources, single-origin quantitative claims and both sides of each crux.

## 5. Checking the synthesis

**Evidence.** In a 2026 error-localisation study of an open deep-research system, 84.7% of final-report errors originated at the orchestrator rather than the search agents [11]. In round 1 this skill's own synthesizer stitched "+10% coverage" (a difference in the share of ratings ≥4) to "p=0.084" (the test on the mean difference) in one sentence; the check passed because it keyed on claim verdicts, not on sentences (round 2, reader seat).

**What we did.** Every number and quoted phrase in the bottom line and key judgments must appear verbatim in the verification table, or the sentence is rewritten or tagged. A six-item lint is scored in the appendix.

## 6. The report's shape

**Evidence.** Intelligence analytic standards require a clear main message up front, a seven-level likelihood scale with numeric ranges, confidence stated separately and never in the same sentence as likelihood, and indicators that would alter the judgment [12]. Systematic reviews cap the findings table at seven outcomes and keep the detailed evidence profile for authors and auditors, not readers [13]. In one small randomised trial (18 vs 15 readers), readers with a summary-of-findings table answered correctly 93% vs 44% and 87% vs 11% and found key information in about 90 seconds instead of four minutes [14]. Rapid reviews keep "one rates, a second checks", fewer than seven outcomes, and a footnoted reason for every downgrade [20]; GRADE's fixed wording ("likely", "may") was acceptable to more than 60% of users [20]. Both of this skill's earlier reports broke their own 3-5 sentence limit on the bottom line and buried the actionable sentence (round 2, reader seat).

**What we did.** A three-slot bottom line (what to do; likelihood with range, confidence with reason; linchpin assumption and its indicator), at most seven key judgments, cruxes, at most three blind spots, a source summary, next step; everything else below a rule in a maintainer appendix. Seat leans are not aggregated into medians: five seats on one model are not five estimators.

## 7. The gap round

**Evidence.** Co-STORM's moderator raises questions from sources retrieved but not yet cited; its ablation reports that removing the moderator hurt more than cutting experts, but the differences are small on a 1-5 LLM-judge scale with no significance test; third-party runs found Co-STORM's source diversity at or below STORM's on most backbones (Co-STORM's own table shows a small advantage), and none of them ablated the moderator, so the result has not been replicated [21]. Anthropic's lead agent adjusts between waves, not during them [15]. Round 1's verifier listed Co-STORM under "found but not cited" and nobody followed up until a whole new run.

**What we did.** One rule-triggered round after fieldwork and before verification: at most two questions from the seats' "read but not cited" and "deliberately not examined" sections, sent to one or two finished seats, questions only, logged in `amendments.md`. It replaces the never-run feedback round.

## 8. Budget and model

**Evidence.** On BrowseComp, token usage alone explained 80% of the performance variance; upgrading a model generation beat doubling the token budget; the measured multi-agent configuration used an Opus lead with Sonnet subagents [15]. Frontier models' errors are correlated even across providers [22]. Two runs of this skill, one with Sonnet seats and one with Opus seats, had downgrade rates of 5/15 and 3/20 on different topics (Fisher p≈0.25): noise.

**What we did.** The skill names no model; seats follow the user's subagent default. Searches per seat is the knob; raise it before adding seats.

## 9. Evaluating the skill

**Evidence.** In Miller's worked example, detecting a 3-point difference needs about 969 independent questions; paired designs cut variance for free; CLT error bars below a few hundred points are badly over-confident [19]. A deep-research agent re-run on the same query under temperature perturbations changed most of its findings (total variance 0.76 on findings vs 0.44 on citations, one open 30B agent on short-answer questions) [23]. Binary rubric grading agrees with experts about 20 points better than ternary, and LLM-rewritten rubrics degrade agreement by 15-20 points [24]; direct 0-10 scoring agrees with humans under 60% of the time [25]. Leave-one-out attribution found bottleneck agents as well as combinatorial methods at far lower cost, and introspective LLM judges did not (a workshop result on hierarchical code-generation systems) [26].

**What we did.** `references/eval.md`: pre-registered questions and binary rubrics, arms built from subsets of one blind run with shared verification, paired statistics, a judge calibrated against the owner's labels, stop rules written first. `runs.log` is a cost and health log, not an eval. `scripts/metrics.py` computes seat metrics; hand counts are banned after round 1's came out wrong.

## Removed, and why

- Codex "second model" seat (0.2.0): untested, harness-specific, and cross-provider errors are correlated [22].
- The credibility axis, weight arrows, seat-estimates table and full ledger in the reader's path (0.3.0): never ran, or ran and carried no information (weight was "=" in 27 of 35 rows); fine labels do not reproduce [9] [10].
- The anonymised feedback round (0.3.0): never ran; replaced by the gap round.
- Seat confidence column (0.3.0): no downstream consumer; the verifier's verdict is the confidence.

## Not yet tested

The outsider seat, the discovered seat, the gap round, the default headcount, strongest-model-per-seat, and the verifier's re-run agreement. The eval design exists; nobody has run it.

## References

1. Choi, Zhu, Li. Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models? NeurIPS 2025. arxiv.org/abs/2508.17536
2. Hussain, Nielbo. 2026. arxiv.org/abs/2608.11247 (23 open models, peer pressure); Qu, Fu, Hu. Easier to Mislead Than to Correct. 2026. arxiv.org/abs/2606.01637
3. Zheng et al. When "A Helpful Assistant" Is Not Really Helpful. EMNLP Findings 2024. arxiv.org/abs/2311.10054; Basil et al. Prompting Science Report 4. 2025. arxiv.org/abs/2512.05858
4. Wang et al. Unleashing the Emergent Cognitive Synergy in LLMs (Solo Performance Prompting). arxiv.org/abs/2307.05300
5. Shao et al. Assisting in Writing Wikipedia-like Articles From Scratch with LLMs (STORM). NAACL 2024. arxiv.org/abs/2402.14207
6. Sharma et al. Towards Understanding Sycophancy in Language Models. ICLR 2024. arxiv.org/abs/2310.13548; SuperSycophantic. NeurIPS 2026. neurips.cc/virtual/2026/poster/148794
7. Nemeth, Brown, Rogers. Devil's advocate versus authentic dissent. European Journal of Social Psychology 2001. doi 10.1002/ejsp.58
8. Venkit et al. DeepTRACE. ICLR 2026. arxiv.org/abs/2509.04499
9. Lee et al. "Fact-checking" fact checkers. HKS Misinformation Review 2023. doi 10.37016/mr-2020-126
10. Icard. A Dynamic Logic for Information Evaluation in Intelligence. 2024. arxiv.org/abs/2405.19968 (on Baker, McKendry, Mace 1968); Haldar, Hockenmaier. Rating Roulette. Findings of EMNLP 2025. arxiv.org/abs/2510.27106; Mustafa et al. The GRADE approach is reproducible. J Clin Epidemiol 2013; Hartling et al. 2012. PMC3320617 (GRADE κ 0.18-0.44 in real reviews).
11. Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research. 2026. arxiv.org/abs/2608.24306
12. Intelligence Community Directive 203, Analytic Standards. 2015, rev. 2023. dni.gov/files/documents/ICD/ICD-203.pdf
13. Cochrane Handbook ch. 14; GRADE Handbook (evidence profile vs. summary of findings). cochrane.org; gdt.gradepro.org
14. Rosenbaum, Glenton, Oxman. Summary-of-findings tables in Cochrane reviews improved understanding and rapid retrieval of key information. J Clin Epidemiol 2010.
15. Anthropic. How we built our multi-agent research system. 2025. anthropic.com/engineering/multi-agent-research-system; Anthropic. Building multi-agent systems: when and how to use them. 2026; LangChain. Open Deep Research. 2025.
16. Kim et al. Towards a Science of Scaling Agent Systems. 2025/2026. arxiv.org/abs/2512.08296
17. Rowe, Wright. Expert opinions in forecasting: the role of the Delphi technique. 2001.
18. Mandel, Karvetski, Dhami. Boosting intelligence analysts' judgment accuracy. Judgment and Decision Making 2018.
19. Miller. Adding Error Bars to Evals. 2024. arxiv.org/abs/2411.00640; Bowyer, Aitchison, Ivanova. Position: Don't use the CLT in LLM evals with fewer than a few hundred datapoints. ICML 2025. arxiv.org/abs/2503.01747
20. Gartlehner et al. Rating the certainty of evidence in rapid reviews. BMJ EBM 2023. PMC10850678; Santesso et al. GRADE guidelines 26. J Clin Epidemiol 2020.
21. Jiang et al. Into the Unknown Unknowns (Co-STORM). EMNLP 2024. arxiv.org/abs/2408.15232; RAPID, ACL Findings 2025, arxiv.org/abs/2503.00751; OmniThink, EMNLP 2025, arxiv.org/abs/2501.09751
22. Kim, Garg, Peng, Garg. Correlated Errors in Large Language Models. ICML 2025. arxiv.org/abs/2506.07962
23. Evaluating Stochasticity in Deep Research Agents. 2026. arxiv.org/abs/2602.23271
24. ResearchRubrics. ICLR 2026. arxiv.org/abs/2511.07685; github.com/scaleapi/researchrubrics
25. LiveResearchBench. ICLR 2026. arxiv.org/abs/2510.14240
26. Lu et al. Agents that Matter. ICLR 2026. arxiv.org/abs/2605.27621
27. Cemri et al. Why Do Multi-Agent LLM Systems Fail? (MAST). 2025. arxiv.org/abs/2503.13657
28. Kelly, Budescu, Dhami, Mandel. Source reliability and information credibility in intelligence analysis. Judgment and Decision Making 2025.
29. Dhuliawala et al. Chain-of-Verification. 2023. arxiv.org/abs/2309.11495
30. Tran, Kiela. 2026. arxiv.org/abs/2604.02460 (single vs multi-agent at equal token budgets)
