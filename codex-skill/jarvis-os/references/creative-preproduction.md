# Creative Preproduction And Taste Gate

Use this reference for craft-critical user-facing work: apps, websites, landing pages, brands, decks, documents, visualizations, demos, and any artifact where taste, originality, trust, or visual quality materially affects success.

Creative Preproduction is the visual/craft-specific form of the broader Excellence Calibration Gate. If the work is excellence-critical but not visual, use `references/adaptive-operating-patterns.md` and `references/quality-qa-and-critique.md` for calibration. If the work is visual or presentation-heavy, this reference supplies the stronger craft process.

## Craft Criticality

Founder classifies every user-facing project or milestone:

- `utility-only`: plain, efficient UI is acceptable.
- `polished product`: quality UI and visual QA are expected.
- `craft-critical`: taste, differentiation, or presentation materially affects success.
- `signature product`: the artifact must feel distinctive, best-in-field, or brand-defining.

Default for apps/websites/products is at least `polished product`. Upgrade to `craft-critical` or `signature product` when:

- the user says "best", "AAA", "world-class", "beautiful", "not generic", "signature", or similar;
- the artifact is public-facing, portfolio-facing, investor/professor/customer-facing, or brand-defining;
- a user rejects the work as generic, ugly, AI-looking, template-like, or low quality;
- the product's value depends on trust, clarity, delight, taste, or visual differentiation.

Record craft criticality in `project-charter.md`, `current-state.md`, and the relevant work order.

## Required Roles

For `craft-critical` or `signature product` work, Founder/Chief of Staff must add or activate roles before implementation:

- `Creative Director` / `Art Director`: owns taste bar, originality, art direction, and rejection of generic work.
- `Product Designer` / `UX Designer`: owns workflow, interaction, information architecture, and usability.
- `UI Engineer` / `Frontend UI Engineer`: implements the chosen visual system faithfully.
- `Design QA` / `Design Critic`: judges screenshots against art direction and rejects generic output before user review.

One person may inhabit multiple roles only for small scopes, but the work order must still separate responsibilities.

## Reference Intelligence

Before implementing or re-implementing craft-critical visuals, the Creative Director runs reference intelligence:

1. Gather 5-10 best-in-class references.
2. Gather 3-5 anti-references.
3. Extract patterns: density, layout rhythm, typography, color/material logic, controls, interaction tone, motion, empty states, artifact presentation.
4. Name forbidden cliches: generic SaaS dashboard, card soup, decorative gradients, random pills/badges, glassmorphism, default component-library look, meaningless dark theme, oversized marketing layout, weak typography.
5. State what will be borrowed as principles, not copied.

These references also satisfy the benchmark/reference part of Excellence Calibration for visual work.

Browse the web when current examples, visual trends, product references, or best-in-class artifacts matter. Use known local references only when enough relevant context is already present.

## Art Direction Brief

Before code, produce a short art direction brief:

- target feel;
- product metaphor;
- emotional tone;
- visual principles;
- layout/composition principles;
- typography direction;
- color/material rules;
- interaction tone;
- what it must never look like.

The brief must be concrete enough for Design QA to reject weak screenshots.

## Divergent Concepts

For craft-critical or rejected work, produce at least three divergent concepts before implementation:

- conservative excellent;
- high-end field-standard;
- bold signature;
- optional weird-but-practical.

Critique each for value, originality, feasibility, product fit, implementation cost, and risk. Choose one internally. Do not ask the user to choose unless the choice changes strategy, brand, release posture, cost, or explicitly requested taste direction.

## Implementation Gate

Do not start major implementation until:

- craft criticality is classified;
- required design roles exist or responsibilities are explicitly assigned;
- reference intelligence is complete where needed;
- art direction brief exists;
- divergent concepts were considered;
- one direction is chosen internally.

For small UI fixes, a compact version is acceptable, but repeated rejection or generic output immediately re-enters full Creative Preproduction.

## Generic UI Kill Switch

Design QA must reject internally if screenshots look:

- generic, template-like, or AI-generated;
- card-heavy without product-specific reason;
- gradient/glass/decorative without information function;
- default component-library shaped;
- visually sparse where the product needs density;
- cluttered where the product needs calm;
- weak in typography, rhythm, hierarchy, or spacing;
- disconnected from the product metaphor;
- like it could belong to any unrelated SaaS/productivity app.

If the kill switch triggers, do not restyle incrementally and do not ask the user for taste. Re-enter Creative Preproduction.

## Screenshot-Based Design QA

For UI/visual work, verify with screenshots before internal acceptance:

- desktop/default viewport;
- narrow/mobile or constrained viewport when relevant;
- core workflow state;
- empty state;
- modal/export/detail state when relevant;
- before/after comparison for redesign work.

Design QA scores:

- originality;
- hierarchy;
- density/rhythm;
- product fit;
- visual confidence;
- interaction clarity;
- whether a strong specialist would be embarrassed by it.

If weak, create a corrective work order and continue internally.

## Rejection Protocol

When the user rejects visual quality or originality:

1. Mark the current direction rejected or technically accepted but aesthetically rejected.
2. Identify whether failure is concept, art direction, layout/composition, visual language, interaction, or polish.
3. Add or activate Creative Director and Design QA if missing.
4. Run reference intelligence.
5. Produce a revised art direction brief.
6. Generate divergent concepts.
7. Implement the chosen direction.
8. Run screenshot-based Design QA.
9. Report the internal decision and next task.

Do not stop with "needs your taste judgment" until this process has been exhausted and the remaining decision is genuinely owner-level.

## Applicability Beyond UI

Use this same pattern for:

- websites and landing pages;
- slide decks and documents;
- data visualizations and research figures;
- demos and launch assets;
- brand/identity work;
- any deliverable where originality, trust, or presentation quality is core to success.
