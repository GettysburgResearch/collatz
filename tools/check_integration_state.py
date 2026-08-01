#!/usr/bin/env python3
"""Lightweight consistency checks for the integrated Collatz repository state."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
ALLOWED_MATH = {"verified", "source-qualified", "empirical", "proposed", "open", "refuted", "superseded"}
ALLOWED_INTEGRATION = {"canonical", "roadmap", "reference-only", "deferred", "quarantined"}


class CheckError(RuntimeError):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CheckError(f"missing file: {path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise CheckError(f"invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckError(message)


def check_snapshot() -> tuple[int, int]:
    data = load_json(ROOT / "docs/integration/2026-08-01/open-prs.json")
    prs = data.get("open_prs", [])
    require(data.get("open_pr_count") == 45, "snapshot open_pr_count must be 45")
    require(len(prs) == 45, "snapshot must contain 45 PR rows")
    numbers = [row.get("number") for row in prs]
    require(len(numbers) == len(set(numbers)), "duplicate PR numbers in snapshot")
    require(set(data.get("unreviewed_prs", [])) == {67, 68, 69}, "unreviewed PR set must be {67,68,69}")

    reviewed = 0
    for row in prs:
        head = row.get("head_sha_at_cutoff", "")
        require(bool(SHA_RE.fullmatch(head)), f"invalid current head SHA for PR #{row.get('number')}")
        frozen = row.get("reviewed_sha")
        if frozen is not None:
            reviewed += 1
            require(bool(SHA_RE.fullmatch(frozen)), f"invalid reviewed SHA for PR #{row.get('number')}")
        else:
            require(row.get("review_wave_status") == "UNREVIEWED", f"missing review status for PR #{row.get('number')}")
    require(reviewed == 42, f"expected 42 reviewed PRs, found {reviewed}")
    return len(prs), reviewed


def check_registry() -> tuple[int, int]:
    registry = load_json(ROOT / "claims/registry.json")
    records = registry.get("records", [])
    ids = [record.get("id") for record in records]
    require(len(ids) == len(set(ids)), "duplicate canonical/roadmap IDs")
    require(all(isinstance(x, str) and x for x in ids), "empty registry ID")

    canonical_count = 0
    for record in records:
        rid = record["id"]
        require(record.get("mathematical_status") in ALLOWED_MATH, f"invalid mathematical status for {rid}")
        require(record.get("integration_status") in ALLOWED_INTEGRATION, f"invalid integration status for {rid}")
        require(bool(record.get("statement")), f"missing statement for {rid}")
        require(bool(record.get("scope")), f"missing scope for {rid}")
        for source in record.get("sources", []):
            require(isinstance(source.get("pr"), int), f"invalid source PR for {rid}")
            require(bool(SHA_RE.fullmatch(source.get("commit", ""))), f"invalid source SHA for {rid}")
            require(source.get("claim_ids"), f"missing source claim IDs for {rid}")
        review = record.get("review", {})
        require(bool(SHA_RE.fullmatch(review.get("report_ref", ""))), f"invalid report ref for {rid}")
        require(bool(review.get("report_path")), f"missing report path for {rid}")
        if record.get("integration_status") == "canonical":
            canonical_count += 1

    canonical_md = (ROOT / "claims/CANONICAL.md").read_text(encoding="utf-8")
    for rid in ids:
        require(rid in canonical_md, f"{rid} missing from CANONICAL.md")

    aliases = load_json(ROOT / "claims/aliases.json")
    alias_targets = set(aliases.get("canonical_aliases", {}))
    require(alias_targets.issubset(set(ids)), f"alias targets missing from registry: {sorted(alias_targets - set(ids))}")
    return len(records), canonical_count


def check_navigation() -> None:
    markdown_paths = [
        "README.md",
        "STATE.md",
        "CONTRIBUTING.md",
        "claims/README.md",
        "claims/CANONICAL.md",
        "docs/INTEGRATION_PRACTICE.md",
        "docs/integration/CURRENT.md",
        "docs/integration/2026-08-01/SNAPSHOT.md",
        "docs/integration/2026-08-01/STATE.md",
        "docs/integration/2026-08-01/REVIEW_COVERAGE.md",
        "docs/integration/2026-08-01/INTEGRATION_REPORT.md",
        "docs/integration/2026-08-01/STRATEGIC_OUTLOOK.md",
        "docs/integration/2026-08-01/HANDOFF.md",
        "docs/integration/2026-08-01/POST_CUTOFF.md",
    ]
    for rel in markdown_paths:
        require((ROOT / rel).is_file(), f"missing navigation target: {rel}")

    for rel in markdown_paths:
        path = ROOT / rel
        for match in MARKDOWN_LINK_RE.finditer(path.read_text(encoding="utf-8")):
            target = match.group(1).split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError as exc:
                raise CheckError(f"relative link escapes repository in {rel}: {target}") from exc
            require(resolved.exists(), f"broken relative link in {rel}: {target}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    require("unsolved" in readme, "README must state that Collatz is unsolved")
    require("finite compatibility" in readme and "2-adic completion" in readme, "README must preserve extraction boundaries")

    current = (ROOT / "docs/integration/CURRENT.md").read_text(encoding="utf-8")
    require("2026-08-01" in current, "CURRENT.md must point to the timestamped snapshot")


def main() -> int:
    try:
        pr_count, reviewed_count = check_snapshot()
        record_count, canonical_count = check_registry()
        check_navigation()
    except CheckError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print(
        "OK: "
        f"{pr_count} open PRs, {reviewed_count} reviewed at frozen SHAs, "
        f"{record_count} registry records, {canonical_count} canonical records."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
