# Docs Contract (00-14)

Path: `<output_root>/docs/NN-*.md`. Every file must be non-empty, use the title shown, and respect the label rules. `scripts/quality_gate.py` enforces structure; content quality is on you.

Common rules for all files:

- Start with the exact H1 from the table below.
- Every factual claim about the target product carries a label (`VERIFIED` / `INFERRED` / `UNKNOWN` / `NOT TESTED`), written as `[VERIFIED]`, `[INFERRED]`, etc.
- VERIFIED claims carry an `[E-xx]` reference resolving into `research/evidence-log.md`.
- No `TODO`, `TBD`, `FIXME`, or empty placeholder sections. "None found" is an acceptable answer where honest.
- Do not copy the target's prose, icons, or code. Describe behavior in your own words.

## File requirements

### 00-readme-handoff.md
H1: `# 00 - Handoff Readme`

Sections: `## Reading order` (guide a coding agent: which docs to load first), `## What this package is` (evidence-bounded spec, not a legal or pixel-perfect clone plan), `## What not to copy` (assets, text, trademarks, code - clean-room pointer to 09), `## Contract` (list of the 14 files + evidence log path), `## Known limits` (top UNKNOWNs, pointer to 13).

### 01-overview.md
H1: `# 01 - Product Overview`

Sections: `## One-sentence description`, `## Who it is for`, `## Core jobs to be done`, `## Public positioning vs observed behavior` (explicit split - marketing claims go here with NOT TESTED; observed behavior cross-refs 02).

### 02-capability-matrix.md
H1: `# 02 - Capability Matrix`

Table with columns: Capability | Claimed (source) | Tested/Observed | Confidence | Evidence. Every row must have a Confidence cell containing exactly one of: `VERIFIED`, `INFERRED`, `UNKNOWN`, `NOT TESTED`. This table is the quality gate's primary scan target.

### 03-user-flows.md
H1: `# 03 - User Flows`

One `### Flow: <name>` section per major journey. Each flow: actors, trigger, steps (numbered), outcomes, evidence refs on behavioral claims. Flows grounded only in marketing get NOT TESTED.

### 04-data-model.md
H1: `# 04 - Data Model`

Entities, fields, relationships. Infer from UI labels, API docs, and export formats - label inferences INFERRED. Unknown storage/retention goes in 13, not guessed here.

### 05-architecture.md
H1: `# 05 - Architecture`

`## Components`, `## Interfaces between components`, `## Data flow`. Describe a *plausible* target architecture for a clean-room rebuild, distinct from the observed product - mark reconstruction choices as INFERRED and keep observed facts (e.g., "client renders in browser") as VERIFIED where sourced.

### 06-interfaces.md
H1: `# 06 - Interfaces`

`## Public API` (from docs), `## Import/export formats`, `## Integrations`, `## CLI or SDK surface` if any. Missing API docs = UNKNOWN rows, not invented endpoints.

### 07-ux-spec.md
H1: `# 07 - UX Specification`

Key screens/views, primary actions per view, empty states, error states. Ground in screenshots/marketing images with labels; do not invent pixel dimensions.

### 08-dependencies.md
H1: `# 08 - Dependencies`

Third-party services, open-source libs (from repo or package manifests if public), codecs/formats with licensing notes, browser/OS requirements. Unknown licenses → UNKNOWN + open question.

### 09-clean-room-barriers.md
H1: `# 09 - Clean-Room Barriers`

`## Legal/contractual barriers` (ToS restrictions, patents if publicly discussed - not legal advice, flag for counsel), `## Technical barriers` (proprietary formats, DRM, paid-only APIs), `## What must not be copied` (assets, text, trademarks, code). End with: "This is not legal advice; consult counsel before shipping a competing product."

### 10-test-plan.md
H1: `# 10 - Test Plan`

Derive acceptance tests from VERIFIED and INFERRED behavior claims in 02/03. Format each as: `Given / When / Then` or a plain checklist item. Include at least one negative test (unsupported input → expected refusal/error). Marketing-only claims do not get tests; they appear in 13 instead.

### 11-risks.md
H1: `# 11 - Risks`

Table: Risk | Likelihood | Impact | Mitigation. Include at least: legal/ToS risk, thin-evidence risk, dependency/license risk.

### 12-implementation-roadmap.md
H1: `# 12 - Implementation Roadmap`

Phases with exit criteria, ordered by risk-reduction first (prove the hard format/dependency before polishing UI). Mark scope assumptions as INFERRED.

### 13-open-questions.md
H1: `# 13 - Open Questions`

Numbered list. Every UNKNOWN from 02 and every NOT TESTED behavioral claim must appear here or be explicitly cross-referenced. If genuinely none: write "None identified from public sources" and list what was attempted (point to evidence log). The gate requires this file to be non-empty.

### 14-needs-human-review.md
H1: `# 14 - Needs Human Review`

Bulleted list of items a human should confirm before implementation: high-impact UNKNOWNs, legal/ToS items from 09, INFERRED architecture choices, anything where being wrong is expensive. If the list is short, say so - do not pad.
