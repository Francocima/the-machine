# Global Rules

## Feedback

- Always read the relevant workflow before executing any automation. WHY: WAT architecture — Claude is the orchestrator, not the executor.
- Check `tools/` for existing scripts before writing new ones. WHY: Avoid duplication; reuse deterministic scripts.
- Check `agents/` for existing subagents before building new ones. WHY: Same reuse principle as tools.
- Never store secrets outside `.env`. WHY: Safety rule from project setup.
- Final outputs go to cloud (Sheets, Drive); `.tmp/` is for intermediate processing only. WHY: Local files are disposable by design.
- Always read existing framework/architecture files before proposing structure. WHY: First plan ignored `wat_claude.md` and had to be rewritten after user interrupted.
- When "skills" or "agents" is ambiguous, ask before building. WHY: Claude API subagents and slash commands are completely different implementations.

## Patterns

## References

- Personal wiki: `/Users/cimaf/Claude/Knowledge Bases/AI Brain` — start at `wiki/index.md`
- WAT framework rules: `wat_claude.md` at project root
