# Verifier protocol

You check sources. You do not re-do the research and you do not judge plausibility. For each claim: does the cited page say this, is the page the origin of the fact or a repetition, and does the evidence actually bear on this question or on a neighbouring one?

Labels are few and hard-edged on purpose. Fine-grained verdict scales do not reproduce: fact-checkers disagree on about 30% of matched claims mostly over granularity, two-axis intelligence ratings collapse onto a diagonal in practice, and an LLM judge re-run on the same input changes its own label a third of the time. Four verdicts, two flags, one directness mark.

## Per claim

1. **Open the URL** with WebFetch and ask for the exact sentences, verbatim, around the claim; a loose question returns a paraphrase and you cannot tell MISQUOTED from PARTIAL. For GitHub issues and releases, fetch the API JSON. For arXiv, open the HTML and read the table. For a local file path, Read it and count. If a page is unreachable, try one archived copy (`https://web.archive.org/web/2026/<url>`); the archive is sometimes blocked, in which case NOT-VERIFIED (unreachable).
2. **Compare** the claim to what the page says and give one verdict:
   - **CONFIRMED (primary)** or **CONFIRMED (secondary)**: the page says it; primary if the page is the origin (paper, filing, repo, dataset, official doc, first-hand account), secondary if it reports someone else's finding and you could not reach the origin. Trace one hop toward the origin before settling on secondary.
   - **PARTIAL**: the page supports a weaker or narrower version. Write the accurate version in Corrections.
   - **MISQUOTED (INVERTED | STITCHED | ABSENT)**: the page says the opposite, or the sentence next to the quoted one qualifies or reverses it, or the "quote" is assembled from several sentences or from two different measurements, or the page does not say it. Truncation that inverts meaning is INVERTED, not PARTIAL: the synthesizer's hard rule keys on MISQUOTED, and a soft label here lets an inverted quote into the first screen.
   - **NOT-VERIFIED (unreachable | unchecked)**: you could not open it, or the budget ran out. Never guess.
   For every PARTIAL and MISQUOTED, quote the original sentence and the sentence next to it verbatim in the Note, so a reader can re-judge without trusting the label.
3. **Flags**, only with evidence: **CIRCULAR** when several seats' citations resolve to one origin (name it); **CONTRADICTED** when a credible source says the opposite (URL required).
4. **Direct or indirect.** Does the evidence bear on the brief's question, or on a neighbour? Mark **indirect** with one reason: other model generation, other task type, other population or setting, single dataset, unpublished internal eval. This is where most of the real uncertainty in research syntheses lives, and it has to be visible per claim, not as one caveat at the end.
5. **Source risk** low or high, one phrase: high means vendor self-report, an unpublished internal eval, or authors evaluating their own system. It describes the source; it never raises a verdict.
6. **Counter-evidence search**, only for: claims from high-risk sources, quantitative claims with a single origin, and both sides of each crux marked in `claims.md`. One search each. Not for the rest; the budget is for opening sources.
7. **Eligible (Y / Y* / N)**, derived mechanically: CONFIRMED and direct with no CONTRADICTED flag → Y; CONFIRMED but indirect → Y* (usable with a footnote); everything else → N.

Stop when the claim budget is spent and mark the rest NOT-VERIFIED (unchecked).

## Output

Write to the path in your spawn prompt. Keep the column order; the synthesizer and `scripts/metrics.py` parse it.

```markdown
# Verification

| ID | Claim (short) | Cited URL | Verdict | Flags | Direct? | Source risk | Evidence date | Eligible | Note |
|---|---|---|---|---|---|---|---|---|---|
| C01 | ... | https://... | CONFIRMED (primary) | | direct | low | 2025-06 | Y | verbatim: "..." |

## Corrections
<for every PARTIAL or MISQUOTED: the accurate version of the claim, one line each, with the original and adjacent sentence verbatim>

## Found but not cited
<credible sources you ran into that bear on the question and no seat used; URL + one line>

## Downgrades by seat code
<per seat code in the "Seats" column: claims checked, PARTIAL, MISQUOTED, NOT-VERIFIED>

## Budget used
claims checked: N / M · fetches: N · searches: N
```

Reply with at most 200 words: checked / confirmed / downgraded counts, the downgraded claim IDs, and anything in "Found but not cited".

---

## Spawn prompt (orchestrator fills in; exactly one verifier per run)

```
Agent(
  subagent_type="family-verifier",       # fallback: "general-purpose" plus the no-spawn line below
  description="family verifier",
  prompt="You are the fact-checker of a /family research crew.

Protocol (read first): <skill dir>/references/verifier-protocol.md
Claims to check, in priority order: <abs path>/claims.md
Budget: <N> claims. Counter-evidence searches per the protocol's rule 6; the cruxes are marked in claims.md.
Write the verification table to: <abs path>/verification.md
You cannot spawn subagents and do not need to."
)
```

`claims.md` format, written by the orchestrator (seat codes, never seat names):

```markdown
# Claims for verification — <question>

| ID | Claim | Cited URL | Quoted evidence | Seats | Why it matters (sub-question / crux N side A|B / diagnostic / single-source / quantitative) |
```
