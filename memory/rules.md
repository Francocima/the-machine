# Global Rules

## Feedback

- Always read the relevant workflow before executing any automation. WHY: WAT architecture — Claude is the orchestrator, not the executor.
- Check `tools/` for existing scripts before writing new ones. WHY: Avoid duplication; reuse deterministic scripts.
- Never store secrets outside `.env`. WHY: Safety rule from project setup.
- Final outputs go to cloud (Sheets, Drive); `.tmp/` is for intermediate processing only. WHY: Local files are disposable by design.

## Patterns

## References

- Personal wiki: `/Users/cimaf/Claude/Knowledge Bases/Personal - Franco` — start at `wiki/index.md`
- WAT framework rules: `wat_claude.md` at project root
