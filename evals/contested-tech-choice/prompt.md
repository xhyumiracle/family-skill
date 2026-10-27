---
tags: [family]
max_turns: 60
timeout_seconds: 1500
allowed_tools: [Read, Write, Glob, Grep, Bash, WebSearch, WebFetch, Agent, Skill]
---

I'm setting up an Obsidian vault that an AI agent will write to on a Linux VM, and I also edit it from a laptop and phone. I want to understand the whole sync landscape properly before committing: Obsidian Sync vs self-hosted LiveSync (CouchDB) vs git-based vs Syncthing. Not just "which one", I want to know how these actually behave under concurrent writes from an agent, what breaks, what people regret, what it costs over years. /family
