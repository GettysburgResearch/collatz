#!/usr/bin/env python3
"""Mechanical integrity checks for literature wave 9."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "literature/LIVE_REPO_REVIEW_WAVE9.md",
    "literature/SOURCE_LEDGER_WAVE9.md",
    "literature/references-wave9.bib",
    "literature/claim-maps/WAVE9.md",
    "literature/UNVERIFIED-WAVE9.md",
    "literature/imported-theorems/LIT-KTHM-0055-rational-ceiling-linear-observables.md",
    "literature/imported-theorems/LIT-KTHM-0056-approximate-multiplication-residue-map.md",
    "literature/imported-theorems/LIT-KTHM-0057-six-branch-zero-digit-gate.md",
    "literature/topic-notes/wave9-zero-digit-and-approximate-multiplication.md",
    "reports/gpt56-pro-03/2026-07-29-9-literature-audit-wave9.md",
]


def fail(message: str) -> None:
    print(f"WAVE 9 CHECK FAILED: {message}", file=sys.stderr)
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

    imported = sorted((ROOT / "literature/imported-theorems").glob("LIT-KTHM-005[567]-*.md"))
    ids: list[str] = []
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

    if ids != ["0055", "0056", "0057"]:
        fail(f"unexpected wave-9 imported IDs: {ids}")

    review = (ROOT / "literature/LIVE_REPO_REVIEW_WAVE9.md").read_text(encoding="utf-8")
    for token in [
        "7153",
        "zero digit",
        "approximate-multiplication",
        "971.866577472",
        "No positive-integer Collatz counterexample",
    ]:
        if token not in review:
            fail(f"review missing token {token!r}")

    unverified = (ROOT / "literature/UNVERIFIED-WAVE9.md").read_text(encoding="utf-8")
    if unverified.count("## U9-") < 12:
        fail("UNVERIFIED-WAVE9.md has too few entries")

    bib = (ROOT / "literature/references-wave9.bib").read_text(encoding="utf-8")
    for key in [
        "Dubickas2009LinearMaps",
        "DubickasMossinghoff2009",
        "AndrieuEliahouVivion2026",
        "Matveev2000",
        "Chim2025",
    ]:
        if f"{{{key}," not in bib:
            fail(f"bibliography missing {key}")

    print("LITERATURE WAVE 9 CHECK PASSED")
    print(f"Required files: {len(REQUIRED)}")
    print(f"Imported theorem notes: {len(imported)}")


if __name__ == "__main__":
    main()
