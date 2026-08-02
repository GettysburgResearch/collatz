#!/usr/bin/env python3
"""Cheap structural checks for the integrated Collatz repository.

This checker validates information architecture, registry schemas, exact-SHA
provenance fields, local proof residency, stable links, and immutable archive
facts. It does not verify mathematics or replay scientific computations.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

FROZEN_CUTOFF = "2026-08-01T21:16:40Z"
FROZEN_MAIN = "0ae0c67bb058f9a7c56cc7744fe5bf2650a7cb84"
MERGED_PR84_COMMIT = "7ed553faea8350050ca4c7d742c049f90211a8bd"

EXPECTED_IC = {
    "IC-EXTRACT-001",
    "IC-GHOST-001",
    "IC-PERIODIC-001",
    "IC-SC-001",
    "IC-AUT-001",
    "IC-RIG-001",
    "IC-REF-001",
    "IC-REP-001",
}
EXPECTED_RD = {"RD-SC-001", "RD-FC-001", "RD-BRIDGE-001"}

ALLOWED_MATH = {
    "verified",
    "source-qualified",
    "empirical",
    "proposed",
    "open",
    "refuted",
    "superseded",
}
ALLOWED_INTEGRATION = {
    "canonical",
    "roadmap",
    "reference-only",
    "deferred",
    "quarantined",
}
ALLOWED_PROMOTION = {
    "candidate_in_draft_pr",
    "accepted_reference_record",
    "accepted_with_local_proof",
    "roadmap_candidate_in_draft_pr",
    "roadmap_accepted",
    "retired",
}
ALLOWED_RESIDENCY = {
    "frozen_source_reference",
    "local_proof_packet",
    "open_obligation",
    "historical_record",
}

FRONT_FILES = [
    "README.md",
    "STATE.md",
    "START_HERE.md",
    "AGENTS.md",
    "CURRENT_KNOWLEDGE.md",
    "FRONTIERS.md",
    "CONTRIBUTING.md",
    "research/README.md",
    "research/integrated/README.md",
    "claims/README.md",
    "claims/CANONICAL.md",
    "archive/README.md",
    "archive/integration/README.md",
    "docs/integration/CURRENT.md",
]

LOCAL_PACKETS = [
    "research/integrated/ordinary-extraction/README.md",
    "research/integrated/completion-ghost/README.md",
    "research/integrated/periodic-tails/README.md",
    "research/integrated/coefficient-stopping/README.md",
    "research/integrated/finite-safety-automata/README.md",
    "research/integrated/six-branch-rigidity/README.md",
    "research/integrated/factor-complexity/README.md",
]


class CheckError(RuntimeError):
    """Raised when a structural integration invariant fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckError(message)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CheckError(f"missing file: {path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise CheckError(f"invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def require_sha(value: Any, label: str) -> None:
    require(
        isinstance(value, str) and SHA_RE.fullmatch(value) is not None,
        f"invalid SHA for {label}: {value!r}",
    )


def require_text(value: Any, label: str) -> None:
    require(isinstance(value, str) and value.strip() != "", f"missing text: {label}")


def iter_registry_records() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    index = load_json(ROOT / "claims/registry.json")
    require(index.get("schema_version") == "1.2", "registry schema must be 1.2")
    require(index.get("merged_integration_pr") == 84, "registry must record merged PR #84")
    require(
        index.get("merged_integration_commit") == MERGED_PR84_COMMIT,
        "registry merged PR #84 commit changed",
    )

    records: list[dict[str, Any]] = []
    for part in index.get("parts", []):
        require_text(part.get("path"), "registry part path")
        path = ROOT / "claims" / part["path"]
        data = load_json(path)
        require(data.get("schema_version") == "1.2", f"registry part schema mismatch: {path}")
        part_records = data.get("records", [])
        require(
            len(part_records) == part.get("record_count"),
            f"registry part count mismatch: {path.relative_to(ROOT)}",
        )
        require(
            [record.get("id") for record in part_records] == part.get("ids"),
            f"registry part ID mismatch: {path.relative_to(ROOT)}",
        )
        records.extend(part_records)

    require(len(records) == index.get("record_count") == 11, "registry must contain 11 records")
    ids = [record.get("id") for record in records]
    require(len(ids) == len(set(ids)), "duplicate integrated record ID")
    require(set(ids) == EXPECTED_IC | EXPECTED_RD, "integrated record population changed")
    return index, records


def check_registry() -> tuple[int, int, int]:
    _index, records = iter_registry_records()
    by_id = {record["id"]: record for record in records}

    for record in records:
        rid = record["id"]
        require(record.get("mathematical_status") in ALLOWED_MATH, f"bad math status: {rid}")
        require(record.get("integration_status") in ALLOWED_INTEGRATION, f"bad integration status: {rid}")
        require(record.get("promotion_state") in ALLOWED_PROMOTION, f"bad promotion state: {rid}")
        require(record.get("proof_residency") in ALLOWED_RESIDENCY, f"bad proof residency: {rid}")
        require_text(record.get("statement"), f"statement {rid}")
        require_text(record.get("scope"), f"scope {rid}")
        require_text(record.get("promotion_gate"), f"promotion gate {rid}")
        require_text(record.get("record_specific_promotion_review"), f"review boundary {rid}")

        for source in record.get("sources", []):
            require(isinstance(source.get("pr"), int), f"bad source PR: {rid}")
            require_sha(source.get("commit"), f"source commit {rid}")
            require(bool(source.get("claim_ids")), f"missing source IDs: {rid}")
            require(bool(source.get("paths")), f"missing source paths: {rid}")

        review = record.get("review", {})
        require_sha(review.get("report_ref"), f"review report {rid}")
        require_text(review.get("report_path"), f"review report path {rid}")

    canonical = [record for record in records if record["id"] in EXPECTED_IC]
    roadmap = [record for record in records if record["id"] in EXPECTED_RD]

    require(len(canonical) == 8, "expected eight integrated reference records")
    require(len(roadmap) == 3, "expected three roadmap records")

    for record in canonical:
        rid = record["id"]
        require(record.get("integration_status") == "canonical", f"IC record not canonical: {rid}")
        require(
            record.get("promotion_state") in {"accepted_reference_record", "accepted_with_local_proof"},
            f"IC record is not accepted post-merge: {rid}",
        )
        require(record.get("proof_residency") == "local_proof_packet", f"missing local proof residency: {rid}")
        packet = record.get("local_packet")
        require_text(packet, f"local packet {rid}")
        require((ROOT / packet).is_file(), f"local packet missing for {rid}: {packet}")

    for record in roadmap:
        rid = record["id"]
        require(record.get("integration_status") == "roadmap", f"RD record not roadmap: {rid}")
        require(record.get("promotion_state") == "roadmap_accepted", f"roadmap not accepted: {rid}")
        require(record.get("proof_residency") == "open_obligation", f"roadmap residency wrong: {rid}")

    require(
        by_id["IC-PERIODIC-001"].get("integration_wording_status") == "pending_narrow_review",
        "periodic synthesis must remain pending narrow review",
    )
    require(
        by_id["RD-BRIDGE-001"].get("integration_wording_status") == "pending_narrow_review",
        "SC*/FC* bridge must remain pending narrow review",
    )
    require(
        by_id["IC-REP-001"].get("dependency_residency") == "source_pinned_pr16",
        "factor-complexity repair must expose source-pinned PR #16 dependencies",
    )

    for record in records:
        require(
            record.get("promotion_state") not in {"candidate_in_draft_pr", "roadmap_candidate_in_draft_pr"},
            f"stale pre-merge promotion state remains on active record: {record['id']}",
        )

    canonical_md = (ROOT / "claims/CANONICAL.md").read_text(encoding="utf-8")
    for rid in EXPECTED_IC | EXPECTED_RD:
        require(rid in canonical_md, f"{rid} missing from claims/CANONICAL.md")

    aliases = load_json(ROOT / "claims/aliases.json")
    alias_targets = set(aliases.get("canonical_aliases", {}))
    require(alias_targets.issubset(EXPECTED_IC | EXPECTED_RD), "alias target missing from registry")
    return len(records), len(canonical), len(roadmap)


def check_front_stage() -> None:
    for rel in FRONT_FILES + LOCAL_PACKETS:
        require((ROOT / rel).is_file(), f"missing front-stage file: {rel}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for required in ["START_HERE.md", "CURRENT_KNOWLEDGE.md", "FRONTIERS.md", "AGENTS.md"]:
        require(required in readme, f"README missing front-door link: {required}")
    require("PR_LIFECYCLE.md" not in readme, "README must not route newcomers into lifecycle ledger")
    require("UNSOLVED" in readme, "README must state UNSOLVED")

    state = (ROOT / "STATE.md").read_text(encoding="utf-8")
    require("pull/85" in state, "STATE.md must point to current draft PR #85")
    require(MERGED_PR84_COMMIT in state, "STATE.md must record merged PR #84 commit")

    knowledge = (ROOT / "CURRENT_KNOWLEDGE.md").read_text(encoding="utf-8")
    frontiers = (ROOT / "FRONTIERS.md").read_text(encoding="utf-8")
    for rid in EXPECTED_IC:
        require(rid in knowledge, f"CURRENT_KNOWLEDGE missing {rid}")
    for rid in EXPECTED_RD:
        require(rid in frontiers or rid.replace("RD-", "") in frontiers, f"FRONTIERS missing {rid}")
    require("PROPOSED" in knowledge, "proposed connections must be labeled")
    require("PENDING NARROW" in knowledge.upper(), "knowledge page must expose pending narrow review")

    active_paths = [
        "README.md",
        "STATE.md",
        "START_HERE.md",
        "AGENTS.md",
        "CURRENT_KNOWLEDGE.md",
        "FRONTIERS.md",
        "claims/README.md",
        "claims/CANONICAL.md",
        "docs/integration/CURRENT.md",
    ]
    stale_phrases = [
        "while pr #84 remains an unmerged draft",
        "pr #84 currently uses candidate states",
        "repository status: pr #84 is an unmerged draft",
        "draft pr #84 now adds",
        "there were 46 open prs only because draft integration pr #84",
    ]
    for rel in active_paths:
        text = (ROOT / rel).read_text(encoding="utf-8").lower()
        for phrase in stale_phrases:
            require(phrase not in text, f"stale post-merge phrase in {rel}: {phrase}")


def resolve_markdown_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>")
    if not target or target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    return (source.parent / target).resolve()


def check_markdown_links(paths: Iterable[str]) -> int:
    checked = 0
    root_resolved = ROOT.resolve()
    for rel in paths:
        source = ROOT / rel
        text = source.read_text(encoding="utf-8")
        for raw in MARKDOWN_LINK_RE.findall(text):
            target = resolve_markdown_target(source, raw)
            if target is None:
                continue
            try:
                target.relative_to(root_resolved)
            except ValueError as exc:
                raise CheckError(f"link escapes repository in {rel}: {raw}") from exc
            require(target.exists(), f"broken local link in {rel}: {raw}")
            checked += 1
    return checked


def check_frozen_archive() -> tuple[int, int]:
    data = load_json(ROOT / "docs/integration/2026-08-01/open-prs.json")
    prs = data.get("open_prs", [])
    require(data.get("open_pr_count") == 45, "frozen open_pr_count must remain 45")
    require(len(prs) == 45, "frozen snapshot must contain 45 source PR rows")
    require(data.get("main_sha") == FROZEN_MAIN, "frozen main changed")
    require(data.get("cutoff_utc") == FROZEN_CUTOFF, "frozen cutoff changed")
    require(set(data.get("unreviewed_prs", [])) == {67, 68, 69}, "frozen unreviewed set changed")

    numbers = [row.get("number") for row in prs]
    require(len(numbers) == len(set(numbers)), "duplicate PR number in frozen snapshot")
    reviewed = 0
    for row in prs:
        require_sha(row.get("head_sha_at_cutoff"), f"frozen PR #{row.get('number')}")
        reviewed_sha = row.get("reviewed_sha")
        if reviewed_sha is None:
            require(row.get("review_wave_status") == "UNREVIEWED", "missing UNREVIEWED marker")
        else:
            require_sha(reviewed_sha, f"reviewed PR #{row.get('number')}")
            reviewed += 1
    require(reviewed == 42, f"expected 42 reviewed source PRs, found {reviewed}")

    lifecycle = load_json(ROOT / "docs/integration/2026-08-02-lifecycle/pr-lifecycle.json")
    require(lifecycle.get("source_pr_population_count") == 45, "lifecycle archive population changed")
    require(lifecycle.get("frozen_cutoff_utc") == FROZEN_CUTOFF, "lifecycle cutoff changed")
    require(lifecycle.get("frozen_main") == FROZEN_MAIN, "lifecycle frozen main changed")
    return len(prs), reviewed


def main() -> int:
    try:
        frozen_count, reviewed_count = check_frozen_archive()
        registry_count, canonical_count, roadmap_count = check_registry()
        check_front_stage()
        links_checked = check_markdown_links(FRONT_FILES + LOCAL_PACKETS)
    except CheckError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        "OK: "
        f"front door present; {canonical_count} accepted reference records, "
        f"{roadmap_count} accepted roadmap records, {len(LOCAL_PACKETS)} local packets, "
        f"{registry_count} total registry records, {links_checked} local links checked; "
        f"frozen archive remains {frozen_count} PRs / {reviewed_count} reviewed."
    )
    print("NOTE: structural validation only; mathematics and scientific computations were not verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
