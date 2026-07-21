#!/usr/bin/env python3
"""Mechanical integrity checks for literature-audit wave 3."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "literature"
IMPORTS = LIT / "imported-theorems"


def fail(message: str) -> None:
    raise SystemExit(f"LITERATURE WAVE-3 CHECK FAILED: {message}")


expected = {f"LIT-KTHM-{n:04d}" for n in range(28, 33)}
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
    fail(f"missing wave-3 imports: {', '.join(missing)}")

required = [
    LIT / "LIVE_REPO_REVIEW_WAVE3.md",
    LIT / "SOURCE_LEDGER_WAVE3.md",
    LIT / "UNVERIFIED-WAVE3.md",
    LIT / "references-wave3.bib",
    LIT / "claim-maps" / "WAVE3.md",
    LIT / "topic-notes" / "completion-height-principle.md",
    LIT / "topic-notes" / "erdos-kahane-carry-rigidity.md",
    LIT / "topic-notes" / "causal-foundry-and-padic-automata.md",
    LIT / "topic-notes" / "padic-logarithm-stage-bulk.md",
    LIT / "topic-notes" / "collatz-spine-many-to-one.md",
    ROOT / "reports" / "gpt56-pro-03" / "2026-07-21-7-literature-audit-wave3.md",
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

# Bibliography keys must be unique across all waves.
bib_files = [
    LIT / "references.bib",
    LIT / "references-wave2.bib",
    LIT / "references-wave3.bib",
]
keys: dict[str, Path] = {}
for path in bib_files:
    if not path.is_file():
        fail(f"missing bibliography {path.relative_to(ROOT)}")
    for key in re.findall(r"@\w+\{([^,\s]+),", path.read_text(encoding="utf-8")):
        if key in keys:
            fail(f"duplicate bibliography key {key}: {keys[key]} and {path}")
        keys[key] = path

# Load-bearing theorem notes must preserve their exact boundaries.
markers = {
    "LIT-KTHM-0028": ("1/2", "Phi", "ordinary integer"),
    "LIT-KTHM-0030": ("lambda/8", "m+1", "transcendental", "preload"),
    "LIT-KTHM-0031": ("N(K)=N(K-2)+N(K-3)", "rho^3=rho+1", "log_2(rho)", "0.405685"),
    "LIT-KTHM-0032": ("many-to-one", "m(u)/m(root)", "ordinary integer"),
}
for ident, needles in markers.items():
    text = found[ident].read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            fail(f"{ident} is missing marker {needle!r}")

# The live review must keep the central nonclaim explicit.
review = (LIT / "LIVE_REPO_REVIEW_WAVE3.md").read_text(encoding="utf-8")
for needle in (
    "ordinary positive integer",
    "No located source constructs",
    "Independently review PR #16",
    "completion-height",
):
    if needle not in review:
        fail(f"wave-3 live review is missing marker {needle!r}")

print("LITERATURE WAVE-3 CHECK PASSED")
print(f"Wave-3 imported theorem notes: {len(expected)}")
print(f"Wave-3 required review/map/topic/report files: {len(required)}")
print(f"Unique bibliography keys across all waves: {len(keys)}")
