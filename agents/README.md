# agents/

Claude API-powered subagents. Each agent is a separate Claude instance with its own system prompt and toolset.

## What goes here

Agents handle tasks that require probabilistic reasoning — writing, summarising, classifying, generating structured output. They are NOT deterministic; use `tools/` for that.

## Folder pattern

```
agents/
└── agent-name/
    ├── system_prompt.md    # The agent's role, rules, and output format
    └── agent.py            # Entry point — call run(input) to invoke
```

## How to invoke from a workflow

Workflows never call agents directly. Claude (the primary agent) reads the workflow, decides when a subagent is needed, then runs:

```bash
python agents/agent-name/agent.py
```

Or imports and calls `run(input)` inline.

The subagent returns a string. The primary agent uses that output to continue the workflow.

## How to build a new agent

1. Copy `_template/` and rename the folder
2. Edit `system_prompt.md` — define the role, tools available, output format, and rules
3. Edit `agent.py` if the agent needs specific tools or a different model
4. Reference the agent in the relevant workflow SOP

## Rules

- One agent per task type — don't build Swiss Army knife agents
- System prompt lives in `system_prompt.md`, not hardcoded in `agent.py`
- Always use prompt caching on the system prompt (already in the template)
- Agents return plain text or JSON — no side effects unless explicitly designed for it
