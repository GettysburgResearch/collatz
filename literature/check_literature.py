#!/usr/bin/env python3
"""Integrity checks for the citation-critical literature suite."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "literature"
IMPORTS = LIT / "imported-theorems"


def fail(message: str) -> None:
    raise SystemExit(f"LITERATURE CHECK FAILED: {message}")


# Imported theorem identifiers must be unique and wave 1 + wave 2 contiguous.
expected = {f"LIT-KTHM-{n:04d}" for n in range(1, 28)}
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
    fail(f"missing imported theorem notes: {', '.join(missing)}")

required = [
    ROOT / "LITERATURE.md",
    LIT / "SOURCE_LEDGER.md",
    LIT / "CLAIM_CROSSWALK.md",
    LIT / "APPLICABILITY_AUDITS.md",
    LIT / "UNVERIFIED.md",
    LIT / "references.bib",
    LIT / "LIVE_REPO_REVIEW_WAVE2.md",
    LIT / "SOURCE_LEDGER_WAVE2.md",
    LIT / "references-wave2.bib",
    LIT / "claim-maps" / "PR3.md",
    LIT / "claim-maps" / "CLAUDE.md",
    LIT / "claim-maps" / "TERMINATION.md",
    LIT / "claim-maps" / "PR3-WAVE2.md",
    LIT / "claim-maps" / "PR11.md",
    LIT / "claim-maps" / "REGULAR.md",
    LIT / "claim-maps" / "IDEAS-8-9.md",
    LIT / "claim-maps" / "TERMINATION-WAVE2.md",
]
for path in required:
    if not path.is_file():
        fail(f"missing required file {path.relative_to(ROOT)}")

# Local Markdown links in the suite should resolve when they are relative file links.
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for path in [ROOT / "LITERATURE.md", LIT / "LIVE_REPO_REVIEW_WAVE2.md", LIT / "README.md"]:
    text = path.read_text(encoding="utf-8")
    for target in link_re.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        clean = target.split("#", 1)[0]
        if clean and not (path.parent / clean).resolve().exists():
            fail(f"broken local link {target!r} in {path.relative_to(ROOT)}")

# No research-tool citation artifacts may enter the repository.
stale_patterns = ("fileciteturn", "turn0search", "turn1search", "cite", "filecite")
for path in required + [found[i] for i in sorted(expected)]:
    text = path.read_text(encoding="utf-8")
    for pattern in stale_patterns:
        if pattern in text:
            fail(f"stale research-tool marker {pattern!r} in {path.relative_to(ROOT)}")

# Bibliographic keys must be unique within each file.
for bib in (LIT / "references.bib", LIT / "references-wave2.bib"):
    keys = re.findall(r"@\w+\{([^,]+),", bib.read_text(encoding="utf-8"))
    if len(keys) != len(set(keys)):
        fail(f"duplicate BibTeX key in {bib.relative_to(ROOT)}")

# The blocking PR11 correction must retain both a counterexample and the qualified condition.
correction = (IMPORTS / "LIT-KTHM-0024-minkowski-cancellation.md").read_text(encoding="utf-8")
for needle in ("D_0=", "E=", "diam", "R(D_0)+1<2^L"):
    if needle not in correction:
        fail(f"PR11 correction is missing marker {needle!r}")

print("LITERATURE CHECK PASSED")
print(f"Imported theorem notes: {len(expected)}")
print("Live program maps: PR3, CLAUDE, TERM, PR11, REGULAR, issues 8/9")
