# the-machine

Personal AI automations hub for Franco Cima.

## Architecture

This project follows the **WAT framework** — read `wat_claude.md` before doing anything else. It defines how you operate, how to use tools, and how to handle failures.

## Stack

- **Agent**: Claude (you) — primary orchestrator
- **Subagents**: Claude API instances in `agents/` — probabilistic, task-specific
- **Tools**: Python scripts in `tools/` — deterministic execution
- **Workflows**: Markdown SOPs in `workflows/`
- **Secrets**: `.env` (never committed)
- **Temp files**: `.tmp/` (gitignored, disposable)

## Integrations

Gmail, Google Drive, Supabase, PostHog, BigQuery — credentials in `.env`.

## Session Memory

This project uses local markdown memory in `memory/`:

- `memory/projects.md` — project state and pending items (primary context source)
- `memory/rules.md` — cross-session rules and references
- `memory/sessions/` — per-session records saved by `/wrapup`

Run `/startup` at the beginning of every session to load context. Run `/wrapup` before closing to save actions, decisions, rules, and pending items. Memory is the source of truth — not CLAUDE.md.

## Personal Knowledge Base

Franco's personal wiki lives at:
`/Users/cimaf/Claude/Knowledge Bases/Personal - Franco`

Read its `claude.md` for operating instructions. When you need context about Franco (background, career, skills, goals, history), start with `wiki/index.md` then read relevant pages.

Use this when: personalizing automations, writing anything in Franco's voice, or answering questions that require personal context.

## Rules

- Read the relevant workflow before executing any automation
- Check `tools/` for existing scripts before writing new ones
- Check `agents/` for existing subagents before building new ones
- Never store secrets outside `.env`
- Final outputs go to cloud (Google Sheets, Drive); `.tmp/` is for intermediate processing only
