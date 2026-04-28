# Decision Log

Use this file only for decisions that materially affect future work, system behavior, workflow policy, or architecture.

## Entry Format

```md
## YYYY-MM-DD - Decision Title

- Context:
- Decision:
- Rationale:
- Consequence:
```

## 2026-04-28 - Add Company Mode to the public template

- Context: JARVIS Light started as a markdown-first continuity workflow. Larger projects also need specialist role separation, task boards, review gates, and a way to adopt existing repos or research folders without one agent trying to do everything at once.
- Decision: Add optional JARVIS Company Mode to the public template, including a separate Codex skill, company-mode templates, Greenfield Mode, Adoption Mode, out-of-box critique, and Git/PR guidance.
- Rationale: Company Mode keeps JARVIS Light lightweight for normal work while giving serious projects a structured operating layer when needed.
- Consequence: Users can install only the base JARVIS skill or also install Company Mode for Founder / Chief of Staff / specialist-role workflows.
