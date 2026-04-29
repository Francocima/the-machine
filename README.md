# the-machine

Personal AI automations hub built on the **WAT framework** (Workflows, Agents, Tools).

## How it works

| Layer | What it is | Where it lives |
|---|---|---|
| Workflows | Markdown SOPs — what to do and how | `workflows/` |
| Agent | Claude — reads workflows, orchestrates everything | `wat_claude.md` |
| Subagents | Claude API instances — probabilistic, task-specific reasoning | `agents/` |
| Tools | Python scripts — deterministic execution | `tools/` |

## Structure

```
agents/         # Claude API subagents — probabilistic, task-specific (system_prompt.md + agent.py)
tools/          # Python scripts for deterministic execution (API calls, transforms, queries)
workflows/      # Markdown SOPs defining automations
memory/         # Session memory — projects, rules, session history
.tmp/           # Temporary files — gitignored, disposable
.env            # Secrets — never committed (see .env.example)
wat_claude.md   # Agent operating instructions
CLAUDE.md       # Claude Code project context
```

## Integrations

Gmail · Google Drive · Supabase · PostHog · BigQuery
