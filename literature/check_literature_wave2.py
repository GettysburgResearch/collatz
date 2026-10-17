#!/usr/bin/env python3
"""Mechanical integrity checks for literature-audit wave 2."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "literature"
IMPORTS = LIT / "imported-theorems"


def fail(message: str) -> None:
    raise SystemExit(f"LITERATURE WAVE-2 CHECK FAILED: {message}")


expected = {
    f"LIT-KTHM-{n:04d}" for n in range(15, 28)
}
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
    fail(f"missing wave-2 imports: {', '.join(missing)}")

required = [
    LIT / "LIVE_REPO_REVIEW_WAVE2.md",
    LIT / "SOURCE_LEDGER_WAVE2.md",
    LIT / "references-wave2.bib",
    LIT / "claim-maps" / "PR3-WAVE2.md",
    LIT / "claim-maps" / "PR11.md",
    LIT / "claim-maps" / "REGULAR.md",
    LIT / "claim-maps" / "IDEAS-8-9.md",
    LIT / "claim-maps" / "TERMINATION-WAVE2.md",
]
for path in required:
    if not path.is_file():
        fail(f"missing required file {path.relative_to(ROOT)}")

stale_patterns = ("fileciteturn", "turn0search", "turn1search", "cite")
for path in required + [found[i] for i in sorted(expected)]:
    text = path.read_text(encoding="utf-8")
    for pattern in stale_patterns:
        if pattern in text:
            fail(f"stale research-tool marker {pattern!r} in {path.relative_to(ROOT)}")

# The PR11 correction must carry both the counterexample and the qualified condition.
correction = (IMPORTS / "LIT-KTHM-0024-minkowski-cancellation.md").read_text(encoding="utf-8")
for needle in ("D_0=", "E=", "diam", "R(D_0)+1<2^L"):
    if needle not in correction:
        fail(f"PR11 correction is missing marker {needle!r}")

print("LITERATURE WAVE-2 CHECK PASSED")
print(f"Wave-2 imported theorem notes: {len(expected)}")
print(f"Wave-2 claim maps: 4")
