# Evidence Log Format

Path: `<output_root>/research/evidence-log.md`

Write this file first, before drafting any docs. It is the grounding truth every VERIFIED claim must resolve into.

## Header

```markdown
# Evidence Log - <product name>
Target URL: <primary>
Researched: <YYYY-MM-DD>
Sources attempted: <N fetched> / <M attempted>
```

## Row format

One row per source, not per claim. Claims cite row IDs.

```markdown
## E-01
- URL: https://example.com/pricing
- Fetched: 2026-10-22
- Type: marketing | docs | terms | repo | third-party-review | changelog
- Summary: <one-line description of what this source actually contained>
- Notes: <any access issues, redirects, or thin content>
```

### ID rules

- IDs are sequential, never reused, never rewritten.
- A correction to a source does not edit an old row; append a new row with a `Supersedes: E-xx` note.
- If a fetch fails, still log the attempt:

```markdown
## E-07
- URL: https://example.com/api
- Fetched: 2026-10-22 (failed: 404)
- Type: docs
- Summary: API reference page not found at expected path
```

Failed fetches still matter: they justify UNKNOWN labels later.

## How claims use rows

In docs, a VERIFIED claim looks like:

> Free tier supports up to 3 output formats [E-02].

The `[E-02]` must resolve to a row whose Summary supports the claim. If the source only *implies* the claim, label INFERRED instead:

> Probably rate-limited on the free tier, based on the absence of a paid-only disclaimer [E-05] [INFERRED].

## Label discipline

| Situation | Label |
|---|---|
| Observed directly on a fetched page | VERIFIED |
| Synthesized from multiple sources, not stated verbatim | INFERRED |
| Not found anywhere in public sources | UNKNOWN |
| Stated by marketing but not tested (no trial run) | NOT TESTED |

A source's existence does not make every claim about it VERIFIED. Marketing copy describing a feature is NOT TESTED for behavior; it is VERIFIED only for "the marketing page says X."
