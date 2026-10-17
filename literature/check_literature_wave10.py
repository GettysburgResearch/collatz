#!/usr/bin/env python3
"""Mechanical integrity checks for literature wave 10."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "literature/LIVE_REPO_REVIEW_WAVE10.md",
    "literature/SOURCE_LEDGER_WAVE10.md",
    "literature/references-wave10.bib",
    "literature/claim-maps/WAVE10.md",
    "literature/UNVERIFIED-WAVE10.md",
    "literature/imported-theorems/LIT-KTHM-0058-dubickas-centered-limit-points.md",
    "literature/imported-theorems/LIT-KTHM-0059-dubickas-small-interval-boundary.md",
    "literature/imported-theorems/LIT-KTHM-0060-matveev-log2-log3-specialization.md",
    "literature/imported-theorems/LIT-KTHM-0061-fixed-support-pulse-finite-reduction.md",
    "literature/imported-theorems/LIT-KTHM-0062-bugeaud-simultaneous-madic.md",
    "literature/imported-theorems/LIT-KTHM-0063-chim-padic-two-logarithms.md",
    "literature/experiments/LIT-X-0058-centered-dubickas/run.py",
    "literature/experiments/LIT-X-0058-centered-dubickas/results/canonical.json",
    "literature/experiments/LIT-X-0060-matveev-specialization/run.py",
    "literature/experiments/LIT-X-0060-matveev-specialization/results/canonical.json",
    "reports/gpt56-pro-03/2026-07-31-10-full-pdf-source-audit.md",
]


def fail(msg: str) -> None:
    raise SystemExit(f"WAVE 10 CHECK FAILED: {msg}")


def main() -> None:
    for rel in REQUIRED:
        path = ROOT / rel
        if not path.is_file():
            fail(f"missing {rel}")
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            fail(f"empty {rel}")
        if "\t" in text:
            fail(f"tab character in {rel}")

    imports = sorted((ROOT / "literature/imported-theorems").glob("LIT-KTHM-00[56][0-9]-*.md"))
    ids = []
    for path in imports:
        m = re.search(r"LIT-KTHM-(\d{4})", path.name)
        if m and 58 <= int(m.group(1)) <= 63:
            ids.append(m.group(1))
            text = path.read_text(encoding="utf-8")
            if "Gap audit" not in text:
                fail(f"missing gap audit in {path.name}")
            if "counterexample" not in text.lower() and "cycle" not in text.lower():
                fail(f"missing objective boundary in {path.name}")
    if ids != ["0058", "0059", "0060", "0061", "0062", "0063"]:
        fail(f"unexpected imported IDs {ids}")

    centered = json.loads((ROOT / "literature/experiments/LIT-X-0058-centered-dubickas/results/canonical.json").read_text())
    if not centered["lift_improves_direct_bound"] or not centered["lift_still_subcritical"]:
        fail("centered source verdict changed")

    matveev = json.loads((ROOT / "literature/experiments/LIT-X-0060-matveev-specialization/results/canonical.json").read_text())
    if matveev["matveev_constant"]["safe_integer_upper_bound"] != 748000000:
        fail("Matveev constant changed")
    if matveev["fixed_support_thresholds"]["P3-(1,2)"]["maximum_support_with_positive_rate"] != 18:
        fail("P3 support threshold changed")
    if matveev["fixed_support_thresholds"]["P11-(1,1,1,2,1,1,4)"]["maximum_support_with_positive_rate"] != 117:
        fail("P11 support threshold changed")

    print("LITERATURE WAVE 10 CHECK PASSED")
    print(f"Required files: {len(REQUIRED)}")
    print(f"Imported theorem notes: {len(ids)}")


if __name__ == "__main__":
    main()
