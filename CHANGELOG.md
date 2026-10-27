# Changelog

## 0.2.0 — 2026-10-27

Rewritten after running the skill on itself (5 seats + verifier, 20 claims checked; see `examples/family-skill-design/`).

- Seats are search territories, not personas. Cards spend their words on where to search and what to leave to others; the biography is one line.
- Casting is three moves: discover territories from how the field sections itself, one outsider from an unrelated trade (on by default, marked experimental), then the archetypes.
- The user's current belief goes only to the skeptic's card, never into the shared brief.
- The skeptic looks for published dissent instead of inventing objections.
- Verifier verdicts split into two axes (fidelity/provenance and credibility); a quote inverted by truncation or stitching is MISQUOTED, not PARTIAL; standard budget 20 claims.
- Deep tier's cross-examination became an anonymised, post-verification, new-evidence-required feedback round.
- Quick tier is one inline research pass plus a small verifier.
- Report gained a seat-estimates table, a belief-vs-finding line, and per-seat metrics; runs append to `family/runs.log`.
- Fixed two citations in the rules (Zheng et al. version; ChatEval misattribution).
- Removed the Codex "second model" seat: untested, harness-specific, and frontier models' errors are correlated across providers anyway.

## 0.1.0 — 2026-10-27

First version: five renamed archetypes, independent seats, batched verifier, three depth tiers, agents without the Agent tool. First real run: `examples/obsidian-agent-vault-sync/`.
