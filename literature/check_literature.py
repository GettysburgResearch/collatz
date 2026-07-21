#!/usr/bin/env python3
"""Integrity checks for the citation-critical literature suite."""

from __future__ import annotations

import re
import sys
from pathlib import Path

LIT_DIR = Path(__file__).resolve().parent
ROOT = LIT_DIR.parent
BIB = LIT_DIR / "references.bib"


def bib_keys(text: str) -> set[str]:
    return set(re.findall(r"@\w+\{([^,\s]+)\s*,", text))


def citation_keys(text: str) -> set[str]:
    return set(re.findall(r"\[@([A-Za-z0-9_:-]+)\]", text))


def relative_links(text: str) -> list[str]:
    links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)
    return [
        link.split("#", 1)[0]
        for link in links
        if link
        and not link.startswith(("http://", "https://", "mailto:", "#"))
    ]


def main() -> int:
    errors: list[str] = []
    keys = bib_keys(BIB.read_text(encoding="utf-8"))
    if not keys:
        errors.append("references.bib contains no parsed entries")

    md_files = sorted(ROOT.rglob("*.md"))
    all_citations: set[str] = set()

    forbidden = ("fileciteturn", "cite", "/mnt/data/")
    for path in md_files:
        text = path.read_text(encoding="utf-8")
        all_citations |= citation_keys(text)

        for token in forbidden:
            if token in text:
                errors.append(f"{path.relative_to(ROOT)} contains forbidden artifact {token!r}")

        for link in relative_links(text):
            target = (path.parent / link).resolve()
            if not target.exists():
                errors.append(
                    f"{path.relative_to(ROOT)} has missing local link {link!r}"
                )

    missing_keys = sorted(all_citations - keys)
    if missing_keys:
        errors.append(f"citation keys missing from BibTeX: {missing_keys}")

    theorem_dir = LIT_DIR / "imported-theorems"
    seen_ids: set[str] = set()
    for path in sorted(theorem_dir.glob("*.md")):
        match = re.match(r"(LIT-KTHM-\d{4})-", path.name)
        if not match:
            errors.append(f"bad imported-theorem filename: {path.name}")
            continue
        theorem_id = match.group(1)
        if theorem_id in seen_ids:
            errors.append(f"duplicate imported theorem ID: {theorem_id}")
        seen_ids.add(theorem_id)
        first_line = path.read_text(encoding="utf-8").splitlines()[0]
        if theorem_id not in first_line:
            errors.append(f"{path.name} first line does not contain {theorem_id}")

    expected = {f"LIT-KTHM-{i:04d}" for i in range(1, 15)}
    if seen_ids != expected:
        errors.append(
            "imported theorem ID set mismatch: "
            f"missing={sorted(expected-seen_ids)}, extra={sorted(seen_ids-expected)}"
        )

    if errors:
        print("LITERATURE CHECK FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("LITERATURE CHECK PASSED")
    print(f"- Markdown files: {len(md_files)}")
    print(f"- BibTeX entries: {len(keys)}")
    print(f"- Referenced citation keys: {len(all_citations)}")
    print(f"- Imported theorem notes: {len(seen_ids)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
