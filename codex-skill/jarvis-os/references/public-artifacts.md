# Lightweight Public Artifact Framing

Use this reference for small public-facing artifacts where audience, trust, tone, privacy, or deployment state matters, but full Specialist Mode / Creative Preproduction would be too heavy.

Examples:

- personal profile or application sites;
- small portfolio pages;
- public README or project pages;
- public-facing emails, bios, one-pagers, decks, and simple landing pages;
- deployed static sites with personal data, photos, or contact details.

Do not use this reference for purely private scripts, mechanical edits, tiny copy fixes, or routine bug fixes where the audience and quality bar are already obvious.

## Framing Check

Before building or substantially revising a small public artifact, run a compact framing check:

1. Audience: who will read, judge, or use this?
2. Decision/job: what should the artifact help them decide or do?
3. Trust/tone: what should it make them feel, and what would undermine trust?
4. Artifact role: is this a profile, application support page, public documentation, pitch, proof, demo, or reference?
5. Avoid list: what would be wrong, generic, cringe, misleading, overdesigned, or off-purpose?
6. Missing material info: is contact, call-to-action, deployment destination, privacy boundary, consent, or source material missing?

If the answers are obvious from the prompt and context, infer them and proceed. If not, ask the smallest useful question batch, usually 2-3 direct questions. Do not dump a long questionnaire for a small artifact.

## External References

If the user gives a URL, skill, design reference, repo, doc, screenshot, or named external resource and says to check, use, follow, or consider it:

- read or inspect it before treating the artifact as ready;
- apply only the relevant guidance, not blind copying;
- respect license, privacy, and source boundaries;
- if access fails, say so explicitly and state the fallback path.

Silent skipping of a named reference is a defect.

## Lightweight Craft Calibration

For small public artifacts, write or hold a tiny direction before implementation:

- Audience:
- Purpose:
- Tone:
- Trust signals:
- Avoid:
- Verification:

Example shape:

```text
Audience: potential reviewers evaluating whether this person/project is credible.
Purpose: make the next contact or decision easier.
Tone: calm, specific, human, not corporate.
Avoid: criteria dump, fake captions, gimmicky UI, template SaaS polish.
Verification: render desktop/mobile, check public data, inspect links/deployment.
```

Escalate to full Creative Preproduction when the artifact is craft-critical, signature-level, high-stakes, repeatedly rejected, or the user asks for best-in-field / AAA / world-class quality.

## Personal And Public Data Boundary

Treat personal photos, contact details, documents, addresses, IDs, private memories, and application material as public-data boundaries.

- Ask before the first upload, public deployment, or third-party publication unless the user has already authorized that specific destination.
- Strip or avoid shipping unnecessary metadata when handling photos or documents.
- Do not invent captions, biographical claims, credentials, affiliations, dates, or preferences.
- If a generated page includes people, personal facts, or claims about the user, verify that the claims come from user-provided material or clearly marked assumptions.

## Deployment Closeout

For deployed public artifacts, closeout must distinguish local state from production state:

- local latest files;
- live URL or deployment target;
- whether local and deployed content match;
- whether preview servers were stopped or intentionally left running;
- privacy/public-data caveats;
- exact next option if they do not match.

If local changes are not deployed, do not call the public artifact fully updated. Report the mismatch as:

```text
Local change ready, not deployed.
Options:
- Deploy: publish the local change to <target>.
- Pause: leave production unchanged and preserve the local diff.
```

## Final Check

Before completion, ask:

- Does the artifact serve the actual audience and decision?
- Did it avoid generic, gimmicky, or off-purpose structure?
- Were named references handled or explicitly marked inaccessible?
- Are photos, captions, claims, and links truthful?
- Were desktop/mobile/rendered views checked when relevant?
- Are local and deployed states synchronized, or is the mismatch explicit?
