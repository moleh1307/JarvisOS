# R&D Idea Loop

Use this reference when a Specialist Mode team is explicitly running a continuous improvement, product R&D, workflow R&D, or idea-by-idea loop.

The loop exists to turn creative ideas into tested workflow changes without letting brainstorming become theater.

## Loop Contract

Run one idea at a time:

1. Ideation role proposes one out-of-box idea.
2. Relevant team roles discuss the idea.
3. If rejected, record the rejection reason and return to ideation.
4. If accepted, Chief of Staff or project manager converts it into a short task list.
5. The team implements the task list.
6. The project or skill is refreshed.
7. The team dogfoods the new feature in the next cycle.
8. Return to one new idea.

Do not batch many unrelated ideas unless the user explicitly asks for a broad brainstorm. A loop is strongest when every idea must survive discussion, implementation planning, and dogfood evidence.

## Idea Quality Bar

A strong idea should be:

- non-obvious enough to improve the system, not just restate an existing rule;
- practical enough to implement in the current tool and memory environment;
- small enough to become one to five tasks;
- useful enough that the team will actually dogfood it;
- safe for public/private boundaries if it affects reusable templates.

Reject or revise ideas that require pretending background work happens without an automation, leaking private memory, adding ceremony without payoff, or depending on tools that are unavailable.

## Team Discussion

Keep discussion compact. Use only the roles that can materially improve the decision:

- Ideation role: why this idea matters.
- Workflow/Product role: whether it fits the operating model and user value.
- Engineering role: whether it is implementable without bloat.
- QA/Red-team role: what can fail, leak, or become ceremony.
- Chief of Staff: final accept/reject and task-list conversion.

Record the decision in an idea card when the idea is accepted, rejected for a durable reason, or likely to matter later.

## Accepted Idea Handling

For accepted ideas:

- create or update an idea card;
- create one work order when the implementation is single-scope;
- create a short task list when the idea naturally splits into two to five tasks;
- mark lifecycle state and risk lane for meaningful work orders;
- define verification and dogfood evidence before implementation begins.

Dogfood evidence should answer:

- Which new behavior was used?
- Where was it used?
- Did it help, fail, or add overhead?
- What should the next loop learn from it?

## Rejected Idea Handling

For rejected ideas, keep only the useful reason:

- already covered by an existing rule;
- too much ceremony;
- weak user value;
- unsafe public/private boundary;
- needs more field evidence;
- blocked by missing capability;
- better as a later candidate.

Do not preserve long rejection debates. Preserve the insight that should prevent repeating the same weak idea.

## Anti-Ceremony Rules

- Do not create idea cards for tiny one-off suggestions.
- Do not run the full loop for urgent bug fixes or obvious maintenance.
- Do not let the ideation role override evidence, safety, or user direction.
- Do not treat "creative" as permission to ignore verification.
- Do not return to ideation until the accepted feature is refreshed and dogfooded, unless a real blocker appears.

