# Learning Pulse

Use this reference when the user asks what JARVIS learned, when an R&D loop needs a self-improvement readout, or when Reflex/Friction candidates should be summarized without starting another implementation task.

A Learning Pulse is a compact visible report of JARVIS metabolism: what was noticed, what was captured, what was promoted, what was ignored or archived, and what should be watched next.

## Pulse Contract

A Learning Pulse should be:

- short enough to read in under a minute;
- grounded in actual Reflex candidates, Friction Inbox items, recent work orders, handoffs, or project memory;
- separated into captured, promoted, rejected/archived, and watch-next lanes;
- honest about no signal when nothing meaningful was learned;
- private by default unless explicitly sanitized for public use.

It must not:

- invent learning that was not captured or observed;
- promote candidates into standing rules by itself;
- become a second task board;
- list every historical item when only recent signal matters;
- leak private project or user details into public artifacts.

## When To Run

Run a Learning Pulse when:

- the user asks what JARVIS learned recently;
- a Reflex candidate was created or promoted;
- several meaningful sessions happened since the last pulse;
- the R&D loop needs to choose between pure ideation and evidence-backed candidates;
- three R&D idea loops have completed since the last pulse;
- the R&D loop has no fresh unpromoted Friction or Reflex evidence before pure ideation;
- self-improvement feels invisible and the user needs a compact state readout.

Skip it for tiny tasks, ordinary closeouts, and R&D starts where a recent pulse or fresh unpromoted evidence already answers the learning question.

## Cadence

Learning Pulse Cadence is manual and lightweight, not background automation.

Run a compact pulse before pure R&D ideation when either condition is true:

- cadence trigger: three R&D idea loops completed since the last pulse;
- empty-evidence trigger: the Friction Inbox and Reflex candidates have no fresh unpromoted signal, and the agent would otherwise invent from memory.

Do not run a pulse just because a loop starts. If a recent pulse is still current or a strong unpromoted candidate is already obvious, use that evidence directly.

## Sources

Use the smallest relevant source set:

- `company/reflex-candidates/`
- `company/friction-inbox/`
- recent `company/idea-cards/`
- recent `company/work-orders/`
- `company/current-state.md`
- project memory and handoffs only when needed

Do not scan the whole vault by default.

## Format

Use this compact shape:

```text
Learning Pulse
- Captured:
- Promoted:
- Rejected / archived:
- Watch next:
- Net effect:
```

If no meaningful learning exists:

```text
Learning Pulse
- Captured: none worth preserving
- Promoted: none
- Watch next: <one concrete signal to watch, or none>
- Net effect: no durable learning change
```

## Promotion Boundary

A Learning Pulse can recommend promotion, but it cannot make standing behavior changes alone.

Promotion still goes through:

- R&D Idea Loop;
- work order;
- eval/check;
- template update;
- memory update;
- explicit approval when required.

## Dogfood Use

At the start of an R&D idea loop, run a compact pulse before pure ideation when cadence or empty-evidence triggers apply. Prefer a strong captured signal over novelty.
