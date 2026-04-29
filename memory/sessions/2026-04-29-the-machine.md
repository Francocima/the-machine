# 2026-04-29 - the-machine

**Project:** the-machine
**Working directory:** /Users/cimaf/Claude/Code/the-machine

## Summary

Full project scaffold built from a nearly empty repo. Aligned the structure to the WAT framework (defined in `wat_claude.md`) with `workflows/`, `tools/`, `agents/`, and `memory/` folders. Added Claude Code config, personal wiki reference, session memory system, and a Claude API subagent template with prompt caching.

## Actions taken

- Read `wat_claude.md` — WAT framework (Workflows, Agents, Tools) already defined by Franco
- Created `CLAUDE.md` — project context, stack, session memory instructions, personal wiki reference
- Created `.gitignore` — excludes `.env`, `.tmp/`, credentials, pyc files
- Created `.env.example` — placeholder keys for Gmail, Drive, Supabase, PostHog, BigQuery
- Created `.claude/settings.json` — Claude Code permissions for Python/shell ops
- Created `tools/README.md` and `workflows/README.md` — convention guides
- Created `.tmp/.gitkeep` — disposable temp folder, gitignored
- Connected Obsidian personal wiki via CLAUDE.md reference (path: `/Users/cimaf/Claude/Knowledge Bases/Personal - Franco`)
- Created `memory/projects.md`, `memory/rules.md`, `memory/sessions/` — local markdown backend for startup/wrapup
- Created `agents/README.md` — subagent conventions
- Created `agents/_template/system_prompt.md` — starter prompt structure
- Created `agents/_template/agent.py` — Claude API entry point with prompt caching on system prompt
- Updated `README.md` — full WAT table including subagents layer
- Committed and pushed to GitHub — commit `6537add`

## Decisions made

- Aligned to `wat_claude.md` exactly after initial plan was redirected — no extra layers beyond WAT
- `agents/` at top level, not inside `tools/` — subagents are probabilistic (Claude API), tools are deterministic; mixing would blur WAT separation
- `system_prompt.md` as a file separate from `agent.py` — prompts should be editable without touching code
- Personal wiki connected via CLAUDE.md path reference only — no symlink, no data duplication; Claude can read any filesystem path
- Local markdown backend for `memory/` — no Supabase configured yet

## Rules learned

- Always read existing framework/architecture files before proposing structure. WHY: first plan ignored `wat_claude.md` and user had to interrupt and redirect.
- When "skills" or "agents" is ambiguous, ask. WHY: user meant Claude API subagents (Option 2), not slash commands (Option 1) — two very different implementations.
- Simplicity beats complexity — don't add layers (prompts/, integrations/, scripts/) that WAT doesn't define. WHY: Franco's explicit preference stated in his global CLAUDE.md.

## Pending items

- Build first automation workflow end-to-end (add `ANTHROPIC_API_KEY` to `.env` first to test agents)
- Set up Supabase backend for memory if desired (replace local markdown)
- Copy `agents/_template/` when first real subagent is needed

## Data discovered

- Personal wiki path: `/Users/cimaf/Claude/Knowledge Bases/Personal - Franco`
- GitHub remote: https://github.com/Francocima/the-machine.git
- Initial scaffold commit: `6537add`
- `.env.example` keys: `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `POSTHOG_API_KEY`, `POSTHOG_PROJECT_ID`, `GOOGLE_APPLICATION_CREDENTIALS`

## Problems and solutions

- First plan proposed agents/, prompts/, integrations/, memory/ without consulting wat_claude.md → user interrupted → rewrote plan aligned to WAT framework
