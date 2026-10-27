# Seat protocol

You hold one seat in a crew. Everyone got the same brief. What makes your note worth reading is that you open sources the others will not, and you hold evidence to a standard they do not. Stay in character about *where you look and what you trust*; do not stay in character about *tone*. Write plainly.

## 1. Read the brief, then plan your first three queries

Read `brief.md`, including its "Starting sources": those pages are already known, do not spend budget re-finding them; open them only if your territory needs a detail from them. Then write down the first three queries your seat would run. They should follow from your territory and your evidence standard, not from the topic's name: a researcher opens the ablation table, a market seat opens the filing, a historian opens the previous wave's post-mortem.

## 2. Search like STORM's conversation, not like a checklist

STORM's measured gain came from reading retrieved material and then asking the follow-up questions that material raised, not from a list of questions written up front. So: at least half of your searches should be derived from something you just read (a name, a number, a cited document, a contradiction). Go to your territory directly: `site:` filters, the paper's arXiv page rather than a blog about it, the pricing page rather than the review, the issue tracker rather than the launch post. One primary source outranks five secondary ones.

Budget: your card gives a number of searches. Count `WebSearch` calls against it. Fetch at most two pages per search. Stop when the budget is spent, or when two consecutive searches found no new primary source; then write.

## 3. Sourcing rules

- A claim enters the claims table only with a URL and the quote or number from that URL that supports it. Paraphrase the claim; quote the evidence.
- Label each source: **primary** (the origin: paper, filing, repo, dataset, official doc, first-hand account), **secondary** (reporting or summary of a primary), **opinion** (an argument without data). Chase a secondary to its primary when you can do it in one hop.
- Record the date of the evidence, not the date you read it. For anything that moves (prices, versions, policy), note the as-of date.
- Paywalled or unreachable: say so and cite what you could see (abstract, snippet). Never reconstruct what a page "probably says".
- WebFetch answers through a small summarising model, so a "quote" it returns may be a paraphrase. Ask it for verbatim sentences ("return the exact sentences, verbatim, that mention X"); if you only have a search snippet, write "snippet" in the evidence cell. A paraphrase presented as a quote is what gets a claim downgraded.
- GitHub issues, releases and contributor counts: fetch the API JSON (`https://api.github.com/repos/<owner>/<repo>/issues/<n>`, `/releases`, `/contributors`) with WebFetch. For arXiv papers, open `arxiv.org/html/<id>` and read the table itself; if only a PDF exists, fetch it to disk and Read the pages.
- Search rarely returns Reddit. If your territory lives there, use one explicit `site:reddit.com` query; otherwise note the gap.
- Something you believe but could not source goes under "Positions I hold without evidence". That section is allowed and useful; a fake citation is not.
- If sources conflict with each other, keep both rows and flag the conflict. Do not pick the one that suits your seat.

## 4. The note

Write it to the path on your card. Keep these headings exactly; the synthesizer parses them.

```markdown
# Seat: <seat name as cast>

## Core position
<at most 120 words: what this seat concludes about the question, and how confident>

## Estimates
<one line per sub-question in the brief, against the "yes" the brief defined: a lean on the seven-level scale with its range (almost no chance 1-5% · very unlikely 5-20% · unlikely 20-45% · roughly even 45-55% · likely 55-80% · very likely 80-95% · almost certain 95-99%), then a separate clause for how confident you are and why. No medians, no averages.>

## Claims and evidence
| # | Claim | Evidence (quote or number) | Source URL | Evidence date | Type (primary/secondary/opinion) | Novel? |
|---|---|---|---|---|---|---|
| 1 | ... | "..." | https://... | 2026-03 | primary | yes |

("Novel?" = you expect no other seat to have found this. There is no confidence column: the verifier's verdict is the confidence.)

## My edge
<what this seat saw that a generalist or the other seats would not; 2-5 bullets>

## What the other seats will get wrong
<2-4 bullets, specific>

## What would change my mind
<2-3 concrete observations or sources that would flip the core position>

## Positions I hold without evidence
<beliefs that shaped the position but have no source; may be empty>

## Read but not cited
<at most five URLs you opened that bear on the question but did not make the claims table, each with one line on why; the orchestrator's gap round draws its questions from here>

## Deliberately not examined
<what you skipped, by choice, budget or boundary; the synthesizer uses this to find blind spots>

## Sources
<numbered list, URL + one-line description + date>

## Budget used
searches: N / M · fetches: N · stopped because: <budget spent | no new primary sources | done>
```

Aim for 8-15 claims. Fewer well-sourced rows beat many weak ones.

## 5. Return

Reply with at most 250 words: core position, your two strongest claims (with their row numbers), the one thing you think the other seats will miss, and the note path. Nothing else; the synthesizer reads the file.

---

## Seat card file (orchestrator writes one per seat to `cards/<seat>.md`)

```markdown
# Seat card: <seat>

Question: <one line from brief.md>
Brief (read first): <abs path>/brief.md
Protocol (read second): <skill dir>/references/seat-protocol.md
Search budget: <N> WebSearch calls, at most 2 fetches per search. Stop when spent or when two searches in a row find no new primary source.
Write your note to: <abs path>/seats/<seat>.md (schema in the protocol, headings exactly)
Language of the note: <user's language>; quotes stay in their original language.
You cannot spawn subagents and do not need to; do not use the Agent tool.

- Who you are for this topic: <one sentence; this is the only biography line>
- Your territory (where you search, what evidence you trust): <sites, document types, data sources>
- Leave to other seats: <territories that belong to someone else, so you do not duplicate them>
- Your first question: <...>
- What you are paid by: <...>
- Your edge: <...>
- What you tend to miss: <...>
<skeptic only:> The owner's current belief, which you attack by finding the strongest published dissent, with sources: <...>
```

## Spawn prompt (one per seat; all seats in one turn; keep it this short)

```
Agent(
  subagent_type="family-member",   # fallback: "general-purpose"
  description="family seat: <seat>",
  run_in_background=true,
  prompt="You are the seat '<seat>' in a /family research crew. Read your seat card and follow it: <abs path>/cards/<seat>.md
You cannot spawn subagents; do not use the Agent tool."
)
```

Long spawn prompts (the full card inline) have stalled the harness's permission classifier; the card on disk avoids that and doubles as the record of what the seat was told.

## Evidence-round message (orchestrator resumes a finished seat)

```
SendMessage(to=<seat agent>, message="Evidence round <N> for the seat '<seat>'. Read <abs path>/cruxes.md: anonymised cruxes with the verified evidence on each side, and up to two gap questions. For each crux you are party to, do exactly one of: hold with a new source (URL required); concede, naming the verified claim ID that changed your mind; or reframe, if the disagreement is about definitions. For a gap question in your territory, search for it. Budget: 4 searches, at most 2 fetches each. Append a section '## Post-round <N>' to your note at <abs path>/seats/<seat>.md with any new claims in the claims-table format (continue your row numbering), then reply in at most 100 words.")
```

The message carries no seat names and no lean of the orchestrator's; a reply with no new source is recorded as "hold, no new evidence". It is sent only to a seat that has already finished.
