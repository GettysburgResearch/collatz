#!/usr/bin/env python3
"""Mechanical integrity checks for literature-audit wave 4."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "literature"
IMPORTS = LIT / "imported-theorems"


def fail(message: str) -> None:
    raise SystemExit(f"LITERATURE WAVE-4 CHECK FAILED: {message}")


expected = {f"LIT-KTHM-{n:04d}" for n in range(34, 42)}
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
    fail(f"missing wave-4 imports: {', '.join(missing)}")

required = [
    LIT / "LIVE_REPO_REVIEW_WAVE4.md",
    LIT / "SOURCE_LEDGER_WAVE4.md",
    LIT / "references-wave4.bib",
    LIT / "UNVERIFIED-WAVE4.md",
    LIT / "claim-maps" / "WAVE4.md",
    LIT / "topic-notes" / "padic-tschakaloff-periodic-closure.md",
    LIT / "topic-notes" / "centered-rational-power-orbits.md",
    LIT / "topic-notes" / "q-lucas-dyadic-pade.md",
    LIT / "topic-notes" / "sections-purification-minplus.md",
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
    "LIT-KTHM-0034": ("f_R(z)", "distinct", "R-orbits"),
    "LIT-KTHM-0035": ("greater than one", "q_n odd", "notin Q"),
    "LIT-KTHM-0036": ("one-counter", "ultimately periodic", "Scope boundary"),
    "LIT-KTHM-0037": ("atomless", "pure action", "temporal"),
    "LIT-KTHM-0038": ("Sec(f)", "minimal", "van der Put"),
    "LIT-KTHM-0039": ("formal multiplicative", "Y_(m+1)=Y_m^2", "preloaded"),
    "LIT-KTHM-0040": ("state-dependent", "finite trap", "Farkas"),
    "LIT-KTHM-0041": ("{-1,0,1}", "two-arc", "Dubickas"),
}
for ident, needles in markers.items():
    text = found[ident].read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            fail(f"{ident} is missing marker {needle!r}")

review = (LIT / "LIVE_REPO_REVIEW_WAVE4.md").read_text(encoding="utf-8")
for needle in (
    "Väänänen--Wallisser",
    "Dubickas",
    "INDEPENDENTLY RECONSTRUCTED",
    "ordinary Collatz counterexample",
):
    if needle not in review:
        fail(f"wave-4 live review is missing marker {needle!r}")

print("LITERATURE WAVE-4 CHECK PASSED")
print(f"Wave-4 imported theorem notes: {len(expected)}")
print(f"Wave-4 required review/map/topic files: {len(required)}")
print(f"Unique bibliography keys across all waves: {len(keys)}")
