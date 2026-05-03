---
sidebar_position: 9
---

# Sunset Review Ledger

The Sunset Review Ledger is a lightweight inventory for workflow features that were added with a Sunset Clause.

It exists because a good R&D loop should not only add capabilities. It should also revisit them after real use and decide whether they still earn their complexity.

## When To Use It

Use a ledger when:

- several R&D changes have active sunset clauses;
- review triggers are scattered across work orders or idea cards;
- the team is doing status, maintenance, or Stack Compression Check;
- process debt is starting to hide in old decisions.

Skip it when a project has only one or two obvious trial features. The ledger should reduce search, not create a new ceremony.

## What To Track

Keep each row short:

| Field | Meaning |
| --- | --- |
| Feature | task ID, feature name, or decision |
| Added | what changed in the workflow |
| Trigger | when it should be reviewed |
| Evidence | what usage has shown so far |
| Likely outcome | `keep`, `simplify`, `merge`, `retire`, or `extend trial` |
| Next action | what to check or do next |
| Status | `watch`, `due`, `reviewed`, `merged`, or `retired` |

Do not copy whole work orders into the ledger. Link them.

## Review Outcomes

Use the same outcomes as Sunset Clause:

- `keep`: still useful as written;
- `simplify`: useful, but heavier than needed;
- `merge`: should be folded into an existing rule, card, or template;
- `retire`: no longer earns its complexity;
- `extend trial`: not enough evidence yet.

If review changes standing behavior, create or update the relevant work order, docs, template, or reference. Do not silently weaken rules.

## Practical Prompt

```text
Jarvis, use JARVIS OS.

Review the Sunset Review Ledger for this project.
Find due or noisy workflow features, recommend keep/simplify/merge/retire/extend-trial,
and create the smallest follow-up work order only where action is justified.
```

