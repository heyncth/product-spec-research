#!/usr/bin/env python3
"""Quality gate for product-spec-research output.

Checks the docs/00-14 contract, label coverage on capability rows,
evidence-ref resolution, and absence of placeholder text.

Usage:
    python quality_gate.py <output_root>

Exit codes: 0 = pass, 1 = findings (printed), 2 = usage error.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LABELS = ("VERIFIED", "INFERRED", "UNKNOWN", "NOT TESTED")
LABEL_ALT = "|".join(LABELS)

REQUIRED_DOCS = [
    "00-readme-handoff.md",
    "01-overview.md",
    "02-capability-matrix.md",
    "03-user-flows.md",
    "04-data-model.md",
    "05-architecture.md",
    "06-interfaces.md",
    "07-ux-spec.md",
    "08-dependencies.md",
    "09-clean-room-barriers.md",
    "10-test-plan.md",
    "11-risks.md",
    "12-implementation-roadmap.md",
    "13-open-questions.md",
    "14-needs-human-review.md",
]

PLACEHOLDER_RE = re.compile(r"\b(TODO|TBD|FIXME|XXX)\b", re.IGNORECASE)
EVIDENCE_REF_RE = re.compile(r"\[E-(\d+)\]")
CAP_ROW_RE = re.compile(r"^\|(.+)\|\s*$")


def find_evidence_ids(log_text: str) -> set[int]:
    return {int(m) for m in re.findall(r"^##\s+E-(\d+)", log_text, re.MULTILINE)}


def check(output_root: Path) -> list[dict]:
    findings: list[dict] = []

    def add(severity: str, path: str, msg: str) -> None:
        findings.append({"severity": severity, "path": str(path), "message": msg})

    docs_dir = output_root / "docs"
    log_path = output_root / "research" / "evidence-log.md"

    if not docs_dir.is_dir():
        add("error", docs_dir, "missing docs/ directory")
        return findings
    if not log_path.is_file():
        add("error", log_path, "missing research/evidence-log.md")
        return findings

    log_text = log_path.read_text(encoding="utf-8", errors="replace")
    evidence_ids = find_evidence_ids(log_text)
    if not evidence_ids:
        add("error", log_path, "no '## E-xx' rows found")

    docs: dict[str, str] = {}
    for name in REQUIRED_DOCS:
        p = docs_dir / name
        if not p.is_file():
            add("error", p, "required doc missing")
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        docs[name] = text
        if not text.strip():
            add("error", p, "doc is empty")
            continue
        if not text.lstrip().startswith("# "):
            add("error", p, "doc must start with an H1 title")
        ph = PLACEHOLDER_RE.search(text)
        if ph:
            add("error", p, f"placeholder text found: {ph.group(0)}")

    # Capability matrix: every table row must carry a confidence label.
    cap = docs.get("02-capability-matrix.md", "")
    if cap:
        cap_rows = [
            line for line in cap.splitlines() if CAP_ROW_RE.match(line) and "---" not in line
        ]
        # drop header row if present (first data row containing 'Capability')
        data_rows = [r for r in cap_rows if "Capability" not in r]
        if not data_rows:
            add("error", docs_dir / "02-capability-matrix.md", "no capability rows found")
        unlabeled = [r for r in data_rows if not re.search(LABEL_ALT, r)]
        if unlabeled:
            add(
                "error",
                docs_dir / "02-capability-matrix.md",
                f"{len(unlabeled)} capability row(s) missing a confidence label",
            )
        # VERIFIED rows in matrix should carry an evidence ref
        for r in data_rows:
            if "VERIFIED" in r and not EVIDENCE_REF_RE.search(r):
                add(
                    "warning",
                    docs_dir / "02-capability-matrix.md",
                    "VERIFIED row without [E-xx] reference: " + r.strip()[:80],
                )

    # Evidence-ref resolution across all docs
    for name, text in docs.items():
        for ref in EVIDENCE_REF_RE.findall(text):
            if int(ref) not in evidence_ids:
                add(
                    "error",
                    docs_dir / name,
                    f"[E-{ref}] does not resolve to a row in the evidence log",
                )

    # Open questions must be substantive
    oq = docs.get("13-open-questions.md", "")
    if oq and len(oq.strip()) < 40:
        add("error", docs_dir / "13-open-questions.md", "too short; list items or 'None identified'")

    # Human review section
    hr = docs.get("14-needs-human-review.md", "")
    if hr and len(hr.strip()) < 40:
        add("error", docs_dir / "14-needs-human-review.md", "too short; list review items")

    # Clean-room reminder present
    cr = docs.get("09-clean-room-barriers.md", "")
    if cr and "not legal advice" not in cr.lower():
        add(
            "warning",
            docs_dir / "09-clean-room-barriers.md",
            "missing 'not legal advice' disclaimer",
        )

    return findings


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    output_root = Path(argv[1])
    if not output_root.exists():
        print(f"error: path not found: {output_root}")
        return 2

    findings = check(output_root)
    errors = [f for f in findings if f["severity"] == "error"]
    warnings = [f for f in findings if f["severity"] == "warning"]

    report = {
        "output_root": str(output_root),
        "passed": not errors,
        "errors": len(errors),
        "warnings": len(warnings),
        "findings": findings,
    }
    print(json.dumps(report, indent=2))

    if errors:
        print(f"\nGATE FAIL: {len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"\nGATE PASS: 0 errors, {len(warnings)} warning(s)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
