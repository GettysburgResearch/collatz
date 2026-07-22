#!/usr/bin/env python3
"""Mechanical integrity checks for literature-audit wave 6."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "literature"
IMPORTS = LIT / "imported-theorems"


def fail(message: str) -> None:
    raise SystemExit(f"LITERATURE WAVE-6 CHECK FAILED: {message}")


expected = {f"LIT-KTHM-{n:04d}" for n in range(44, 48)}
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
    fail(f"missing wave-6 imports: {', '.join(missing)}")

required = [
    LIT / "LIVE_REPO_REVIEW_WAVE6.md",
    LIT / "SOURCE_LEDGER_WAVE6.md",
    LIT / "references-wave6.bib",
    LIT / "UNVERIFIED-WAVE6.md",
    LIT / "claim-maps" / "WAVE6.md",
    LIT / "topic-notes" / "completion-limit-separation.md",
    LIT / "topic-notes" / "block-qgaussian-all-period-program.md",
    LIT / "topic-notes" / "fixed-period-to-sadic-limit.md",
    LIT / "topic-notes" / "room-two-block-product-formula.md",
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
    "LIT-KTHM-0044": (
        "Cross-completion",
        "2^N/(1+2^N)",
        "product formula",
        "PADIC/T-9418",
    ),
    "LIT-KTHM-0045": (
        "decimation identity",
        "m_(rN+h)",
        "Stieltjes",
        "Vandermonde",
    ),
    "LIT-KTHM-0046": (
        "Christoffel",
        "residue-class functionals",
        "block",
        "Nonconsequences",
    ),
    "LIT-KTHM-0047": (
        "Delta_(n+1)Delta_(n-1)/Delta_n^2",
        "cubic bulk",
        "orthogonal-polynomial",
        "Scope boundary",
    ),
}
for ident, needles in markers.items():
    text = found[ident].read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            fail(f"{ident} is missing marker {needle!r}")

review = (LIT / "LIVE_REPO_REVIEW_WAVE6.md").read_text(encoding="utf-8")
for needle in (
    "WITHDRAWN",
    "decimated q-Gaussian",
    "twelve-bit",
    "all fixed periods",
    "No theorem in this review",
):
    if needle not in review:
        fail(f"wave-6 live review is missing marker {needle!r}")

print("LITERATURE WAVE-6 CHECK PASSED")
print(f"Wave-6 imported theorem notes: {len(expected)}")
print(f"Wave-6 required review/map/topic files: {len(required)}")
print(f"Unique bibliography keys across all waves: {len(keys)}")
