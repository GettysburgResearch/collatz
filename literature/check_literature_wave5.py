#!/usr/bin/env python3
"""Mechanical integrity checks for literature-audit wave 5."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "literature"
IMPORTS = LIT / "imported-theorems"


def fail(message: str) -> None:
    raise SystemExit(f"LITERATURE WAVE-5 CHECK FAILED: {message}")


expected = {"LIT-KTHM-0042", "LIT-KTHM-0043"}
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
    fail(f"missing wave-5 imports: {', '.join(missing)}")

required = [
    LIT / "LIVE_REPO_REVIEW_WAVE5.md",
    LIT / "SOURCE_LEDGER_WAVE5.md",
    LIT / "references-wave5.bib",
    LIT / "UNVERIFIED-WAVE5.md",
    LIT / "claim-maps" / "WAVE5.md",
    LIT / "topic-notes" / "period-nine-tschakaloff-closure.md",
    LIT / "topic-notes" / "fixed-word-s-unit-stitching.md",
    LIT / "topic-notes" / "h-two-place-logarithmic-forms.md",
    LIT / "topic-notes" / "centered-power-arithmetic-blocks.md",
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
    "LIT-KTHM-0042": (
        "minimal period has length at most nine",
        "Gamma(9)",
        "Gamma(10)",
        "distinct R^Z-orbits",
    ),
    "LIT-KTHM-0043": (
        "nondegenerate",
        "proper subsum",
        "finite-rank",
        "cap-stitch",
    ),
}
for ident, needles in markers.items():
    text = found[ident].read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            fail(f"{ident} is missing marker {needle!r}")

review = (LIT / "LIVE_REPO_REVIEW_WAVE5.md").read_text(encoding="utf-8")
for needle in (
    "Period ten",
    "S-unit",
    "Dubickas",
    "nu_K",
    "No native claim is promoted",
):
    if needle not in review:
        fail(f"wave-5 live review is missing marker {needle!r}")

print("LITERATURE WAVE-5 CHECK PASSED")
print(f"Wave-5 imported theorem notes: {len(expected)}")
print(f"Wave-5 required review/map/topic files: {len(required)}")
print(f"Unique bibliography keys across all waves: {len(keys)}")
