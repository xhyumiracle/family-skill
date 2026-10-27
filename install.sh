#!/usr/bin/env bash
# Installs the family skill and its two agents into ~/.claude without the plugin system.
# After this, the skill is /family and the agents are family-member / family-verifier.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$HOME/.claude/skills" "$HOME/.claude/agents"
rm -rf "$HOME/.claude/skills/family"
cp -r "$HERE/skills/family" "$HOME/.claude/skills/family"
cp "$HERE/agents/family-member.md" "$HERE/agents/family-verifier.md" "$HOME/.claude/agents/"
echo "installed: ~/.claude/skills/family and ~/.claude/agents/family-{member,verifier}.md"
echo "start a new Claude Code session; agents are read at session start."
