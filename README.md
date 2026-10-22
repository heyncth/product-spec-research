# product-spec-research

Research a real product from its public surface and produce an implementation-ready specification package with per-claim evidence labels and a fixed `docs/00-14` handoff contract.

Built for clean-room rebuilds: free/open-source alternatives, competitor research that must become buildable docs, and agent-consumable handoffs. Not a teardown deck generator.

## What it does

1. **Intake** - target URL(s), category preset, output root (conversation-first; optional `target.md`)
2. **Research** - public pages only (home, pricing, docs, changelog, terms, repos)
3. **Evidence log first** - every source gets an `E-xx` row with URL + date; failed fetches logged too
4. **Docs 00-14** - capability matrix, user flows, data model, architecture, interfaces, test plan, risks, roadmap, open questions, human-review list
5. **Quality gate** - `scripts/quality_gate.py` checks file presence, label coverage, evidence-ref resolution; exits non-zero on failure

Every factual claim carries one of:

| Label | Meaning |
|---|---|
| `VERIFIED` | Observed on a fetched public source; has `[E-xx]` ref |
| `INFERRED` | Reasonable synthesis; not directly observed |
| `UNKNOWN` | Not found in public sources; listed as open question, never guessed |
| `NOT TESTED` | Claimed by marketing but not verified from a runnable/trial experience |

## Install

Copy this directory into your agent's skills path, e.g. Claude Code / opencode:

```bash
# opencode
cp -r product-spec-research ~/.config/opencode/skills/
```

Requires Python 3.8+ for the quality gate (stdlib only).

## Usage

```
/spec product-spec-research Research Notion from its public docs and give me
an implementation-ready spec under research/notion-spec/.
```

Or just paste a product URL and ask for a buildable spec - the skill description is written to trigger on that.

Category presets ship for: **converter**, **web-app**, **desktop-utility**. Add a new preset by dropping a checklist in `references/category-checklists/`.

## Layout

```
SKILL.md                          # workflow + hard rules
scripts/quality_gate.py           # deterministic output gate
references/
  docs-contract.md                # per-file requirements for docs/00-14
  evidence-log-format.md          # E-xx row format + label discipline
  category-checklists/
    converter.md  web-app.md  desktop-utility.md
evals/evals.json                  # test prompts
```

## Out of scope

- Teardown scorecards / SWOT decks
- Pixel-perfect website cloning
- Binary / APK reverse engineering
- Legal advice (clean-room awareness only - consult counsel)

## Evidence from iteration-1 evals

Against three real targets (2anything, Notion, HandBrake), assertion pass rate:

| Configuration | Pass rate |
|---|---|
| with skill | 100% |
| without skill (baseline) | 17% |

## License

MIT. See [LICENSE](LICENSE).
