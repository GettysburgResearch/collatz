#!/usr/bin/env python3
"""Mechanical integrity checks for literature wave 8."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "literature/LIVE_REPO_REVIEW_WAVE8.md",
    "literature/SOURCE_LEDGER_WAVE8.md",
    "literature/references-wave8.bib",
    "literature/claim-maps/WAVE8.md",
    "literature/UNVERIFIED-WAVE8.md",
    "literature/imported-theorems/LIT-KTHM-0053-six-branch-rational-base-minimal-word.md",
    "literature/imported-theorems/LIT-KTHM-0054-stationary-transported-cylinder.md",
    "literature/topic-notes/wave8-six-branch-rational-base.md",
    "literature/topic-notes/wave8-pulse-resultant-repetition.md",
    "literature/topic-notes/wave8-centered-power-and-h-duals.md",
    "reports/gpt56-pro-03/2026-07-23-8-literature-audit-wave8.md",
]


def fail(message: str) -> None:
    print(f"WAVE 8 CHECK FAILED: {message}", file=sys.stderr)
    raise SystemExit(1)


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

    imported = sorted((ROOT / "literature/imported-theorems").glob("LIT-KTHM-005[34]-*.md"))
    ids = []
    for path in imported:
        match = re.search(r"LIT-KTHM-(\d{4})", path.name)
        if not match:
            fail(f"bad imported-theorem filename: {path.name}")
        ids.append(match.group(1))
        text = path.read_text(encoding="utf-8")
        if "Gap audit" not in text:
            fail(f"missing gap audit in {path.name}")
        if "counterexample" not in text.lower():
            fail(f"missing counterexample boundary in {path.name}")

    if ids != ["0053", "0054"]:
        fail(f"unexpected wave-8 imported IDs: {ids}")

    review = (ROOT / "literature/LIVE_REPO_REVIEW_WAVE8.md").read_text(encoding="utf-8")
    for token in ["971.866577", "3^12/2^19", "No such integer"]:
        if token not in review:
            fail(f"review missing token {token!r}")

    unverified = (ROOT / "literature/UNVERIFIED-WAVE8.md").read_text(encoding="utf-8")
    if unverified.count("## U8-") < 10:
        fail("UNVERIFIED-WAVE8.md has too few entries")

    print("LITERATURE WAVE 8 CHECK PASSED")
    print(f"Required files: {len(REQUIRED)}")
    print(f"Imported theorem notes: {len(imported)}")


if __name__ == "__main__":
    main()
