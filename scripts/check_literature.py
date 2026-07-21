#!/usr/bin/env python3
"""Static validation for the repository literature layer.

Checks BibTeX citation keys, relative Markdown links, atomic-import IDs, and
branch qualification in claim maps. The script performs no network access.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "literature"
BIB = LIT / "references.bib"


def markdown_files() -> list[Path]:
    return sorted(
        p
        for p in [ROOT / "LITERATURE.md", *LIT.rglob("*.md"), *ROOT.glob("reports/**/*.md")]
        if p.is_file()
    )


def bib_keys() -> set[str]:
    text = BIB.read_text(encoding="utf-8")
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", text))


def cited_keys(text: str) -> set[str]:
    found: set[str] = set()
    for group in re.findall(r"\[@([^\]]+)\]", text):
        for part in group.split(";"):
            key = part.strip()
            if key.startswith("@"):
                key = key[1:]
            key = key.split(",", 1)[0].strip()
            if key:
                found.add(key)
    return found


def relative_links(text: str) -> list[str]:
    links: list[str] = []
    for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = raw.strip().split(" ", 1)[0].strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = unquote(target.split("#", 1)[0])
        if target:
            links.append(target)
    return links


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    keys = bib_keys()
    used: set[str] = set()
    mds = markdown_files()

    for path in mds:
        text = path.read_text(encoding="utf-8")
        for key in cited_keys(text):
            used.add(key)
            if key not in keys:
                errors.append(f"{path.relative_to(ROOT)}: missing BibTeX key {key}")

        for link in relative_links(text):
            target = (path.parent / link).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {link}")
                continue
            if not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken relative link: {link}")

    imports = sorted((LIT / "imported-theorems").glob("KTHM-*.md"))
    seen_ids: dict[str, Path] = {}
    for path in imports:
        match = re.match(r"(KTHM-\d{4})-", path.name)
        if not match:
            errors.append(f"invalid imported-theorem filename: {path.name}")
            continue
        kid = match.group(1)
        if kid in seen_ids:
            errors.append(f"duplicate {kid}: {seen_ids[kid]} and {path}")
        seen_ids[kid] = path
        first = path.read_text(encoding="utf-8").splitlines()[0]
        if kid not in first:
            errors.append(f"{path.relative_to(ROOT)}: first heading omits {kid}")

    # Claim maps must never use ambiguous bare low-numbered IDs in code spans.
    qualified_prefixes = ("PR3/", "CLAUDE/", "TERM/")
    claim_pattern = re.compile(r"`((?:[A-Z]+/)?[DLTOXQCRMK]-\d{4})`")
    for path in sorted((LIT / "claim-maps").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for token in claim_pattern.findall(text):
            if not token.startswith(qualified_prefixes):
                errors.append(f"{path.relative_to(ROOT)}: ambiguous bare claim ID `{token}`")

    unused = sorted(keys - used)
    if unused:
        warnings.append("uncited BibTeX entries: " + ", ".join(unused))

    print(f"checked {len(mds)} Markdown files")
    print(f"checked {len(keys)} BibTeX entries; {len(used)} cited")
    print(f"checked {len(imports)} atomic theorem imports")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("literature validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
