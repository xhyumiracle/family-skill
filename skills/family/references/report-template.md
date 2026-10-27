# Report template

Write `report.md` in the user's language. Headings below are the contract; the content under each is guidance. Keep the whole thing readable in ten minutes; the seat notes and the verification table are on disk for anyone who wants the long version.

```markdown
# <Question>

<one line: tier, seats, date, path to this run's folder>

## Bottom line
<three to five sentences. What the crew concluded, how confident, and the single biggest caveat. Every sentence maps to a claim number whose verdict passed, or carries [UNVERIFIED]. Agreement among seats is not evidence; a verified source is.>

## Belief vs. finding
<one or two lines: what the user believed going in (from the skeptic's card), and whether the verified evidence supports, weakens or leaves it open. Omit if the user stated no belief.>

## What every seat agreed on
<bullets. Each with the strongest verified evidence and its verdict label. If agreement rests on overlapping sources, say so; if sources are independent, say that too, because that is the strong signal.>

## Seat estimates
<one small table: each sub-question of the brief as a row, each seat's lean (yes / no / unsure, or a number) as a column, plus a median or spread. This is the aggregation step; it sits beside the narrative, it does not replace it. Disagreement is shown as spread, never settled by majority.>

## Where they disagree (the cruxes)
<one subsection per crux; a crux counts only when each side rests on different sources:>
### Crux N: <the tension in one sentence>
- **Side A** (<seats>): <claim> — <evidence, verdict label>
- **Side B** (<seats>): <claim> — <evidence, verdict label>
- **What would settle it:** <a concrete observation, dataset or event>
- **Current lean:** <which side the verified evidence favours, or "open">

## Blind spots
<what no seat examined. Sources: the seats' "deliberately not examined" sections, topics no source touched, the orchestrator's own read. At least one. Say which, if any, would change the bottom line.>

## Evidence ledger
<the verification table, condensed: # · claim · fidelity verdict · credibility verdict · weight · primary URL. Include UNCHECKED rows so the reader knows what was not verified.>

## The seats, one line each
<seat — how cast — core position — its edge — what the verifier downgraded>

## Open questions and next step
<two to four bullets. The first thing to read, the one person to ask, the experiment to run.>

## Cost
seats: N · searches: N (sum of seat budgets used) · claims checked: N / N listed · agents spawned: N · tokens: <per seat and verifier, if reported> · wall time: <if known>
Seat metrics: <per seat: unique URLs · URLs shared with another seat · verified claims only this seat produced>
Not verified: <claim numbers left UNCHECKED or UNREACHABLE>
```

Rules the template enforces:

- The bottom line is downstream of the ledger. A MISQUOTED or single-origin CIRCULAR claim cannot appear in it even if all seats liked it; a claim no seat disputed but nobody verified carries [UNVERIFIED].
- A crux is not resolved by majority. Three seats against two is still a crux unless the verified evidence favours one side.
- Blind spots is never empty. If you truly found none, that is itself a casting-failure note.
- Cost and seat metrics come from counting the notes and the ledger, not from estimates. The seat metrics are the only running evidence of whether a seat (especially the outsider) earns its budget; append them to `family/runs.log`.
