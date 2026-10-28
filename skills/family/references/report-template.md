# Report template

`report.md` has two layers. The first screen is for a reader who has ten minutes and a decision to make; everything below the rule is for audit and for the maintainer. Write in the user's language. Headings are the contract; the text under each is guidance.

## The likelihood scale

Likelihood and confidence are different things and never share a sentence. Likelihood uses this seven-level scale with its range (ICD 203; readers pull bare words toward 50%, the range stops that). Confidence (high / medium / low) is about the evidence base and gets its own sentence with the reason.

| English | 中文 | Range |
|---|---|---|
| almost no chance | 几乎不可能 | 1-5% |
| very unlikely | 很不可能 | 5-20% |
| unlikely | 不太可能 | 20-45% |
| roughly even chance | 大致五五开 | 45-55% |
| likely | 可能 | 55-80% |
| very likely | 很可能 | 80-95% |
| almost certain | 几乎确定 | 95-99% |

Confidence below high must carry one of these reasons: indirect evidence (other models, tasks, populations or years), single origin, seats disagree, fidelity problems in the sources, or not verified.

## Template

```markdown
# <Question>

<one line: tier, seats, date, path to this run's folder>

## Bottom line
① <one sentence: what to do or what to believe, written against the decision in the brief>
② <one sentence: the likelihood on the scale with its range> <one sentence: confidence high/medium/low and the reason>
③ <one sentence: the linchpin assumption, and the indicator that would overturn it>
(claims: C03, C07, C12)

At most 150 words. Numbers and quoted phrases here must appear verbatim in verification.md.

## Key judgments
| # | Judgment | Likelihood (range) / confidence | Strongest confirmed source | What would change it | Claims |
|---|---|---|---|---|---|
At most seven rows. A judgment no seat disputed but nobody verified carries [UNVERIFIED]. Agreement among seats is not evidence; a verified source is.

## Belief vs. finding
<one or two lines: what the user believed going in (from the dissent seat's card), and whether the verified evidence supports, weakens or leaves it open. If an earlier report on this topic exists, say which judgments changed and which new evidence changed them. Omit only if no belief was stated and no earlier report exists.>

## Cruxes
<one subsection per crux; a crux counts only when each side rests on different sources:>
### Crux N: <the tension in one sentence>
- **Side A** (<seat codes>): <claim>; <evidence, verdict>
- **Side B** (<seat codes>): <claim>; <evidence, verdict>
- **What would settle it:** <a concrete observation, dataset or event>
- **Current lean:** <scale word (range)>, or "open" plus the indicator to watch

## Blind spots
<at most three; first the one that would change the bottom line. Sources: the seats' "Deliberately not examined" and "Read but not cited" sections, topics no source touched, the orchestrator's own read.>

## Source summary
<three to five lines: what the source base is made of, where it is weak (indirect, vendor, single origin), which sources carry the key judgments.>
<then only the rows that touch a key judgment and are PARTIAL, MISQUOTED, CONTRADICTED, NOT-VERIFIED or indirect: ID · short claim · verdict · the verifier's note>
Full table: verification.md

## Next step
<two to four bullets: the first thing to read, the one person to ask, the experiment to run, the fact only the reader can supply>

---

## Appendix (for the maintainer)
Seats: <code · name · how cast · core position · what the verifier downgraded, one line each>
Evidence rounds: <none, or per round: the trigger, cruxes sent, seats resumed, what moved (lean changed / side filled / concession), what came back>
Cost: seats N · searches N (seats) + N (verifier) · fetches N · claims checked N / N listed · agents spawned N · tokens <per seat and verifier> · wall time
Seat metrics (scripts/metrics.py): <per seat code: claims contributed · CONFIRMED only this seat · PARTIAL · MISQUOTED>
Lint: <score>/6
Not verified: <claim IDs left NOT-VERIFIED>
```

## Lint (six binary checks, score recorded in the appendix)

1. The bottom line has exactly the three slots and is at most 150 words.
2. Every key judgment carries claim IDs or [UNVERIFIED].
3. No key judgment rests on a MISQUOTED claim or a CIRCULAR claim without a second origin.
4. Every crux has both sides sourced with different sources.
5. Every crux has a "What would settle it" line.
6. Blind spots is non-empty.

## Rules the template enforces

- The bottom line is downstream of the verification table, and the orchestrator is the most likely place for a final-report error. Hence the verbatim check: if a number or phrase is not in `verification.md`, it does not go in the first screen.
- A crux is not resolved by majority. Three seats against two is still a crux unless the verified evidence favours one side.
- Seat leans are not aggregated into medians in the report; five seats on one model are not five independent estimators. Where seats gave ranges, a key-judgment row may show the span (min to max).
- Length is a cost to the reader. Above the rule, cut rather than compress.
