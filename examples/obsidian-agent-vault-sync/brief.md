# Brief — Obsidian vault sync for an agent-written vault

## Question
How do the realistic sync options for an Obsidian vault (Obsidian Sync, self-hosted LiveSync on CouchDB, git-based sync, Syncthing) actually behave when an AI agent writes to the vault on a Linux VM while a human edits the same vault from a laptop and a phone — what breaks, what people regret, and what each costs over years?

## What it is for
Mapping the field before committing. The owner is building an "agent-native" personal knowledge base and the sync choice is the open decision. This run is to understand the landscape and failure modes, not to pick a winner on its own.

## Constraints
- State of the world as of October 2026. Flag anything older than 2025 as possibly stale (Obsidian releases often; LiveSync has had breaking changes).
- Platforms: Linux VM (headless, agent runs here, writes plain markdown files directly on disk), macOS/Linux laptop, iOS or Android phone.
- Prefer primary sources: official docs, pricing pages, GitHub issues and discussions, source code, changelogs, first-hand forum/Reddit reports with dates. Blog roundups are secondary.
- Scope exclusions: not evaluating note-taking apps other than Obsidian; not evaluating cloud drives (iCloud/Dropbox/Google Drive) except as a historical comparison for conflict behaviour.

## Known facts (all seats start from these)
- The VM already exists and runs other services, so self-hosting has near-zero marginal infrastructure cost; the question is operational cost and risk, not server rent.
- The agent needs plain-file access to the vault on the VM (it reads and writes `.md` files directly, not through the Obsidian app). Obsidian the desktop app is not necessarily running on the VM.
- The vault will also receive a large one-time import from Notion later; the Notion source is kept, never deleted.
- The owner is technically strong (runs Caddy, systemd services, Node apps) and is cost-aware but not cost-constrained.

## Owner's current belief
No firm lean. Working assumption that is worth attacking: that the VM must hold a live, continuously synced copy of the vault for the agent to work on it.

## Output language
Chinese for the report and notes; quotes stay in their original language.
