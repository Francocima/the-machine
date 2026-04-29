# Projects

## the-machine

**Project key:** the-machine
**Working directory:** /Users/cimaf/Claude/Code/the-machine
**Status:** Setup phase

**Context:** Personal AI automations hub for Franco Cima. Built on the WAT framework (Workflows, Agents, Tools). Claude is the primary agent; subagents are Claude API instances in `agents/`; tools are deterministic Python scripts in `tools/`; workflows are markdown SOPs in `workflows/`.

**Stack:** Python, Claude API, Gmail, Google Drive, Supabase, PostHog, BigQuery

**Personal knowledge base:** `/Users/cimaf/Claude/Knowledge Bases/AI Brain` — read `wiki/index.md` for Franco's background and context.

**Pending:**
- Build first automation workflow end-to-end (add `ANTHROPIC_API_KEY` to `.env` first to test agents)
- Set up Supabase backend for memory if desired (replace local markdown)
- Copy `agents/_template/` when first real subagent is needed
