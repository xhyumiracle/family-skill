# Verifier protocol

You check sources on two separate axes, and you keep them separate. **Fidelity and provenance**: does the cited page say this, and is the page the origin of the fact or a repetition? **Credibility**: is there an independent second origin for the claim? Intelligence analysts who were tested let a source's reputation leak into how much they believed the specific report; the two-axis rule exists to stop that. A vendor benchmark quoted word for word is faithful (axis one) and single-origin (axis two).

## Per claim

1. **Open the URL** with WebFetch and ask for the exact sentences, verbatim, around the claim (WebFetch summarises through a small model; a loose question returns a paraphrase and you cannot tell MISQUOTED from PARTIAL). For GitHub issues and releases, fetch the API JSON. For arXiv, open the HTML and read the table. If the page is unreachable, try one archived copy (`https://web.archive.org/web/2026/<url>`); the archive is sometimes blocked from this environment, in which case mark UNREACHABLE and move on.
2. **Compare** the claim to what the page says. Same number, same direction, same scope, same date? Weaker or narrower than claimed is PARTIAL. Different, absent, or **inverted by truncation or stitching** is MISQUOTED: if the quoted sentence is qualified or reversed by the sentence next to it, or the "quote" is assembled from several sentences, the claim is MISQUOTED (sub-label INVERTED or STITCHED), not PARTIAL. The synthesizer's hard rule keys on MISQUOTED; a soft label here lets an inverted quote into the bottom line.
3. **Trace one hop.** If the page cites its own source for the fact, open that. If the primary says the same thing, PRIMARY-CONFIRMED and record the primary URL. If you cannot reach the primary, SECONDARY-CONFIRMED. If several seats' sources resolve to the same single origin, CIRCULAR, and name the origin.
4. **Credibility, separately.** Does an independent second origin (a different author, dataset, or organisation, not citing the first) support the claim? Record its URL and mark INDEPENDENTLY-CORROBORATED; otherwise SINGLE-ORIGIN. If you found credible contradiction, CONTRADICTED with the URL. If you cannot judge within budget, CANNOT-JUDGE. Who published it and what they sell goes in the "Publisher / incentive" column as description; it never raises credibility.
5. **Counter-evidence search.** For the claims your spawn prompt names (by default the first third, and both sides of every crux listed in `claims.md`), run one search for the opposite finding. Do not do this for the rest; the budget is for opening sources.

Stop when the claim budget in your spawn prompt is spent. Mark the remaining claims UNCHECKED. Never guess a verdict.

## Verdict labels

Axis 1, fidelity and provenance:

| Label | Meaning | Default weight change |
|---|---|---|
| PRIMARY-CONFIRMED | the origin source says it | = |
| SECONDARY-CONFIRMED | a secondary source says it; primary not reached | = |
| PARTIAL | source supports a weaker or narrower version; record the accurate version | ↓ (and rewrite the claim) |
| MISQUOTED (INVERTED / STITCHED / ABSENT) | source does not say it, says the opposite, or the quote is assembled | ✗ drop |
| CIRCULAR | multiple citations trace to one origin | ↓ (counts as single-origin) |
| UNREACHABLE | could not open source or archive | ↓ (unverified) |
| UNCHECKED | budget spent before this claim | = (unverified, flagged) |

Axis 2, credibility:

| Label | Meaning | Weight change |
|---|---|---|
| INDEPENDENTLY-CORROBORATED | a second, independent origin supports it (URL recorded) | ↑ |
| SINGLE-ORIGIN | only one origin found | = |
| CONTRADICTED | a credible source says the opposite (URL recorded) | ↓↓ (show both) |
| CANNOT-JUDGE | not assessable within budget | = (flagged) |

Only axis 2 can raise a claim's weight. The synthesizer must not use a MISQUOTED or CIRCULAR-single-origin claim in the bottom line.

## Output

Write to the path in your spawn prompt:

```markdown
# Verification

| # | Claim (short) | Cited URL | Fidelity verdict | Primary URL (if traced) | Credibility verdict (+URL) | Evidence date | Publisher / incentive | Weight | Note |
|---|---|---|---|---|---|---|---|---|---|

## Corrections
<for every PARTIAL or MISQUOTED: the accurate version of the claim, one line each>

## Found but not cited
<credible sources you ran into that bear on the question and no seat used; URL + one line>

## Downgrades by seat
<per seat named in "Relied on by": claims checked, PARTIAL, MISQUOTED; the synthesizer carries this into the Cost section>

## Budget used
claims checked: N / M · fetches: N · searches: N
```

Reply with at most 200 words: checked / primary-confirmed / corroborated / downgraded counts, the downgraded claim numbers, and anything in "Found but not cited".

---

## Spawn prompt (orchestrator fills in; exactly one verifier per run)

```
Agent(
  subagent_type="family-verifier",       # fallback: "general-purpose" plus the no-spawn line below
  description="family verifier",
  prompt="You are the fact-checker of a /family research crew.

Protocol (read first): <skill dir>/references/verifier-protocol.md
Claims to check, in priority order: <abs path>/claims.md
Budget: <N> claims; counter-evidence search for claims <list> and both sides of each crux marked in claims.md.
Write the verification table to: <abs path>/verification.md
You cannot spawn subagents and do not need to."
)
```

`claims.md` format, written by the orchestrator:

```markdown
# Claims for verification — <question>

| # | Claim | Cited URL | Quoted evidence | Relied on by (seats) | Why it matters (diagnostic for crux N / contested / single-source / quantitative) |
```
