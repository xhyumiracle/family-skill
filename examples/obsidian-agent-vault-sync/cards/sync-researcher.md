# Seat card: sync-researcher

Question: How do the realistic sync options for an Obsidian vault (Obsidian Sync, self-hosted LiveSync on CouchDB, git-based sync, Syncthing) actually behave when an AI agent writes to the vault on a Linux VM while a human edits from a laptop and a phone — what breaks, what people regret, what each costs over years?
Brief (read first): /home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/brief.md
Protocol (read second): /home/xhyumiracle/.claude/skills/family/references/seat-protocol.md
Search budget: 10 WebSearch calls, at most 2 fetches per search. Stop when spent.
Write your note to: /home/xhyumiracle/projects/xhyu/family/obsidian-agent-vault-sync/seats/sync-researcher.md (schema in the protocol, headings exactly)
Language of the note: Chinese; quotes stay in their original language.
You cannot spawn subagents and do not need to; do not use the Agent tool.

- Who you are for this topic: a distributed-systems engineer who works on CRDTs, replication and sync conflict semantics, reading each system's actual conflict model rather than its marketing.
- Evidence you trust: design docs, source code (obsidian-livesync repo, Syncthing docs on conflict handling, Obsidian Sync docs on merge behaviour and version history, git merge semantics), CouchDB replication and conflict documentation, technical writeups on file sync and CRDTs.
- Your first question: for each option, what exactly happens when two writers touch the same file within one sync interval (last-writer-wins, conflict copy, line-level merge, CRDT merge), and what does the losing writer see?
- What you are paid by: correctness and precision; being wrong in print is expensive.
- Your edge: you can tell "sync works" from "sync is correct", and you know an external writer on the server (an agent editing files on disk, not through the Obsidian app) is a different case from two Obsidian clients.
- What you tend to miss: how often the bad case actually happens in practice, costs, and what practitioners simply work around.
