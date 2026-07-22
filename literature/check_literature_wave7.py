#!/usr/bin/env python3
"""Mechanical integrity checks for literature-audit wave 7."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "literature"
IMPORTS = LIT / "imported-theorems"


def fail(message: str) -> None:
    raise SystemExit(f"LITERATURE WAVE-7 CHECK FAILED: {message}")


expected = {f"LIT-KTHM-{n:04d}" for n in range(48, 53)}
found: dict[str, Path] = {}
for path in sorted(IMPORTS.glob("LIT-KTHM-*.md")):
    match = re.match(r"(LIT-KTHM-\d{4})", path.name)
    if not match:
        continue
    ident = match.group(1)
    if ident in found:
        fail(f"duplicate imported-theorem ID {ident}: {found[ident]} and {path}")
    found[ident] = path

missing = sorted(expected - set(found))
if missing:
    fail(f"missing wave-7 imports: {', '.join(missing)}")

required = [
    LIT / "LIVE_REPO_REVIEW_WAVE7.md",
    LIT / "SOURCE_LEDGER_WAVE7.md",
    LIT / "references-wave7.bib",
    LIT / "UNVERIFIED-WAVE7.md",
    LIT / "claim-maps" / "WAVE7.md",
    LIT / "topic-notes" / "integer-first-counterexample-architecture.md",
    LIT / "topic-notes" / "linear-height-quotient-refund.md",
    LIT / "topic-notes" / "restricted-rational-base-integer-search.md",
    LIT / "topic-notes" / "primitive-cycle-prime-sieves.md",
]
for path in required:
    if not path.is_file():
        fail(f"missing required file {path.relative_to(ROOT)}")

stale_patterns = ("fileciteturn", "turn0search", "turn1search", "cite", "filecite")
for path in required + [found[i] for i in sorted(expected)]:
    text = path.read_text(encoding="utf-8")
    for pattern in stale_patterns:
        if pattern in text:
            fail(f"stale research-tool marker {pattern!r} in {path.relative_to(ROOT)}")

bib_files = [
    LIT / "references.bib",
    LIT / "references-wave2.bib",
    LIT / "references-wave3.bib",
    LIT / "references-wave4.bib",
    LIT / "references-wave5.bib",
    LIT / "references-wave6.bib",
    LIT / "references-wave7.bib",
]
keys: dict[str, Path] = {}
for path in bib_files:
    if not path.is_file():
        fail(f"missing bibliography {path.relative_to(ROOT)}")
    for key in re.findall(r"@\w+\{([^,\s]+),", path.read_text(encoding="utf-8")):
        if key in keys:
            fail(f"duplicate bibliography key {key}: {keys[key]} and {path}")
        keys[key] = path

markers = {
    "LIT-KTHM-0048": ("Modified division", "finite representation", "ordinary-marker", "Nonconsequences"),
    "LIT-KTHM-0049": ("all distinct", "infinite sequential", "ABSTRACT STATE", "Nonconsequences"),
    "LIT-KTHM-0050": ("477424", "quotient", "3^[A(B)]", "coherent infinite"),
    "LIT-KTHM-0051": ("233", "792", "0,138", "local minima"),
    "LIT-KTHM-0052": ("184", "292", "92", "167385996821689"),
}
for ident, needles in markers.items():
    text = found[ident].read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            fail(f"{ident} is missing marker {needle!r}")

review = (LIT / "LIVE_REPO_REVIEW_WAVE7.md").read_text(encoding="utf-8")
for needle in (
    "full unconditional counterexample",
    "linear-height quotient refund",
    "Issue #39",
    "Issues #9 and #41",
    "No theorem in this review",
):
    if needle not in review:
        fail(f"wave-7 live review is missing marker {needle!r}")

print("LITERATURE WAVE-7 CHECK PASSED")
print(f"Wave-7 imported theorem notes: {len(expected)}")
print(f"Wave-7 required review/map/topic files: {len(required)}")
print(f"Unique bibliography keys across all waves: {len(keys)}")
