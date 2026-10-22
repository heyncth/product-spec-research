# Category Checklist - Converter

Use when the target is a format-conversion tool (file converters, media transcoders, document converters, image pipelines). Work these axes while drafting docs 02, 06, 10.

## Format matrix

Build an explicit input → output matrix from public docs/marketing. For every pair, one of: supported / unsupported / unknown. Do not assume symmetric support (PNG→PDF supported does not imply PDF→PNG).

Document for each format:

- Exact container/codec/variant names as the product names them (e.g., "MP4 (H.264)" not just "video")
- Lossy vs lossless
- Whether conversion preserves metadata (EXIF, tags, bookmarks) - VERIFIED only if stated
- Max file size / resolution / duration limits on each tier

## Engine and dependency axes

- Which engines/power the conversion (FFmpeg, LibreOffice, cloud API) - public repos or docs may reveal this
- Local vs cloud processing (privacy implication - flag in 09 if cloud)
- Hardware acceleration claims (GPU, video-toolbox) - usually marketing → NOT TESTED
- Offline capability

## Quality and fidelity

- Quality knobs offered (CRF, bitrate, presets)
- Batch conversion limits and queue behavior
- Parallelism claims
- What happens on failure (partial output, error report, retry)

## Pricing / tier gates

- Which formats/limits are free vs paid
- Watermarks, ads, or export restrictions on free tier

## Test-plan seeds (docs/10)

- Round-trip: input → output → re-input preserves expected properties
- Edge inputs: empty file, corrupt file, 0-byte, oversized file
- Unsupported format → expected error, not silent success
- Metadata preservation asserted only where VERIFIED; else open question

## Clean-room note

Converter UX is often thin; the hard part is format coverage and fidelity. Specs must not copy the target's exact format list as if it were your design - record it as observed behavior, then design your own matrix with honest gaps.
