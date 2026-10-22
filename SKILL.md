---
name: product-spec-research
description: Research a real product from its public surface and produce an implementation-ready specification package with per-claim evidence labels and a fixed docs/00-14 handoff contract. Use whenever the user wants to spec a product for rebuild, plan a free/open-source alternative to an existing tool, do competitive research that must turn into buildable docs, reverse-engineer a product's features from its website, or asks things like "spec this product", "research competitor X for our rewrite", "what would it take to clone 2anything", "implementation-ready spec for <url/product>", or wants a structured handoff to a coding agent. Covers converters, web apps/SaaS, and desktop utilities via category presets. Even if the user does not say "spec" or "research", trigger when they paste a product URL and want a buildable plan from it.
---

# Product Spec Research

Turn a live product into an evidence-labeled, agent-consumable spec package.

A coding agent given "clone Notion" will hallucinate behavior, invent formats, and smooth over unknowns. This skill exists because that failure is the default. The discipline is simple: collect sources first, label every factual claim, and hand off a fixed file set that a downstream agent can load without guessing.

## When to use

- Rebuild / free-alternative planning for an existing product
- Competitive research that must become implementation docs, not a slide deck
- "Outside-in" diligence: what does this product actually do, per public evidence?

## When NOT to use

- Teardown scorecards, SWOT decks, market positioning memos - different deliverable
- Pixel-perfect website cloning - different skill class
- Reverse-engineering binaries/APKs - needs RE tooling, out of scope
- Legal advice - you provide clean-room *awareness*, never counsel

## Workflow

### 1. Intake

Extract from conversation. Ask only for missing pieces:

- **Target**: product name + public URL(s). Required.
- **Category preset**: converter | web-app | desktop-utility. Infer from the target; confirm if unsure.
- **Output root**: default `research/<slug>/` relative to cwd. Overridable by user.
- **Access facts**: does a public docs site exist? pricing page? repository? Does the user have a trial account you should *not* rely on by default?

Optional: if the user pastes a `target.md`, treat it as the source of truth for target identity and category; still confirm category before research.

State the four labels up front so expectations match output:

| Label | Meaning |
|---|---|
| VERIFIED | Observed on a fetched public source; evidence-log row with URL + date |
| INFERRED | Reasonable synthesis from sources; not directly observed |
| UNKNOWN | Not found in public sources; listed as open question, never guessed |
| NOT TESTED | Claimed by marketing but not verified from a runnable/trial experience |

### 2. Research (public surface only)

Fetch public pages: home, pricing, docs, changelog, terms, API reference, GitHub if open-source. Prefer pages that describe *behavior* over slogans.

Do **not** invent sources. If a page 404s or is blocked, log the attempt and move on - absence of evidence becomes UNKNOWN, not fabricated detail.

Write `research/evidence-log.md` **before** drafting docs. Format: see `references/evidence-log-format.md`.

### 3. Read the category checklist

Open `references/category-checklists/<preset>.md`. It lists the axes that make that category's spec *deep* rather than generic. Work through it while drafting docs.

### 4. Draft the docs/ contract

Produce these files under `<output_root>/docs/` (see `references/docs-contract.md` for per-file requirements):

```
00-readme-handoff.md   05-architecture.md     10-test-plan.md
01-overview.md         06-interfaces.md       11-risks.md
02-capability-matrix.md 07-ux-spec.md         12-implementation-roadmap.md
03-user-flows.md       08-dependencies.md     13-open-questions.md
04-data-model.md       09-clean-room-barriers.md  14-needs-human-review.md
```

Every factual claim in these docs carries one of the four labels. VERIFIED claims carry an `[E-xx]` reference that resolves to a row in the evidence log. Where a claim is only marketing-sourced, say so - do not present marketing copy as tested behavior.

### 5. Run the quality gate

```
python <skill-path>/scripts/quality_gate.py <output_root>
```

The gate checks: file presence, label coverage on capability rows, evidence-ref resolution, open-questions section, no `TODO` placeholders. Exit 0 = pass; non-zero = fix findings before presenting.

If the gate fails, fix the docs (not the gate) and re-run. Presenting ungated output defeats the point of the contract.

### 6. Present + flag human review

When the gate passes, summarize for the user:

- Which labels dominated (how much is VERIFIED vs UNKNOWN?)
- Top items in `14-needs-human-review.md`
- Clean-room reminder: do not copy assets, text, or code from the target

Do not claim the spec is "complete" or "implementation-ready without further research." It is *evidence-bounded*: as deep as public sources allow, honest about where they stop.

## Hard rules

- Never fabricate a capability, format, price, or benchmark. UNKNOWN is always safer than a wrong VERIFIED.
- Never present a marketing claim as tested behavior. Label NOT TESTED unless you actually ran the product.
- Evidence log rows are append-only once written; corrections get a new dated row.
- Do not fetch authenticated pages or use credentials. Public surface only unless the user explicitly opts into a trial account workflow and logs that context.
- Do not copy target assets, code, or text into the output. Specs describe behavior; they do not repackage expression.

## Reference index

| File | Read when |
|---|---|
| `references/docs-contract.md` | Drafting docs 00-14; check per-file sections and label rules |
| `references/evidence-log-format.md` | Writing or resolving evidence-log rows |
| `references/category-checklists/converter.md` | Target is a format-conversion tool |
| `references/category-checklists/web-app.md` | Target is a SaaS / web app |
| `references/category-checklists/desktop-utility.md` | Target is a desktop or mobile utility |
| `scripts/quality_gate.py` | After drafting, before presenting |
