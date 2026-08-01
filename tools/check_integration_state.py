#!/usr/bin/env python3
"""Cheap structural checks for the integrated Collatz state.

This validates schemas, identifiers, dispositions, promotion states, and local
navigation. It does not verify mathematics or replay scientific computations.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

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
ALLOWED_PROOF_RESIDENCY = {
    "frozen_source_reference",
    "local_proof_packet",
    "open_obligation",
    "historical_record",
}
ALLOWED_DISPOSITIONS = {
    "CANONICALIZED BY REFERENCE",
    "CLEAN EXTRACTION REQUIRED",
    "MERGE CANDIDATE AFTER FIXES",
    "PRESERVE AS RESEARCH/REFERENCE",
    "CONTINUE ACTIVE DEVELOPMENT",
    "DEFER PENDING REVIEW",
    "DEFER PENDING DEPENDENCY OR REPAIR",
    "SUPERSEDED/ABSORBED",
    "REJECT/CLOSE CANDIDATE",
    "UNREVIEWED",
    "MIXED—CLAIM-LEVEL ACTION REQUIRED",
}
ALLOWED_ACTIONS = {
    "KEEP OPEN",
    "IMPORT CLEAN PACKET THEN CLOSE",
    "MERGE AFTER REVIEWED FIX",
    "CLOSE AS SUPERSEDED WITH DURABLE POINTER",
    "CLOSE AS REJECTED WHILE PRESERVING REFUTATIONS",
    "NO ACTION UNTIL REVIEW",
}


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


def require_sha(value: Any, label: str) -> None:
    require(isinstance(value, str) and bool(SHA_RE.fullmatch(value)), f"invalid SHA: {label}")


def check_frozen_snapshot() -> tuple[int, int]:
    data = load_json(ROOT / "docs/integration/2026-08-01/open-prs.json")
    prs = data.get("open_prs", [])
    require(data.get("open_pr_count") == 45, "frozen open_pr_count must remain 45")
    require(len(prs) == 45, "frozen snapshot must contain 45 source PR rows")
    require(data.get("main_sha") == "0ae0c67bb058f9a7c56cc7744fe5bf2650a7cb84", "frozen main changed")
    require(data.get("cutoff_utc") == "2026-08-01T21:16:40Z", "frozen cutoff changed")
    require(set(data.get("unreviewed_prs", [])) == {67, 68, 69}, "frozen unreviewed set changed")

    numbers = [row.get("number") for row in prs]
    require(len(numbers) == len(set(numbers)), "duplicate PR numbers in frozen snapshot")

    reviewed = 0
    for row in prs:
        require_sha(row.get("head_sha_at_cutoff"), f"cutoff head PR #{row.get('number')}")
        frozen = row.get("reviewed_sha")
        if frozen is not None:
            reviewed += 1
            require_sha(frozen, f"reviewed head PR #{row.get('number')}")
        else:
            require(row.get("review_wave_status") == "UNREVIEWED", f"missing UNREVIEWED status for PR #{row.get('number')}")
    require(reviewed == 42, f"expected 42 reviewed PRs, found {reviewed}")
    return len(prs), reviewed


def check_lifecycle() -> tuple[Counter[str], Counter[str]]:
    frozen = load_json(ROOT / "docs/integration/2026-08-01/open-prs.json")
    frozen_rows = {row["number"]: row for row in frozen["open_prs"]}
    data = load_json(ROOT / "docs/integration/2026-08-02-lifecycle/pr-lifecycle.json")
    rows: list[dict[str, Any]] = []
    parts = data.get("parts", [])
    require(parts, "lifecycle part index is empty")
    for part in parts:
        part_path = ROOT / "docs/integration/2026-08-02-lifecycle" / part["path"]
        part_data = load_json(part_path)
        part_rows = part_data.get("records", [])
        require(len(part_rows) == part.get("record_count"), f"lifecycle part count mismatch: {part.get('part')}")
        require([row.get("number") for row in part_rows] == part.get("prs"), f"lifecycle part PR mismatch: {part.get('part')}")
        rows.extend(part_rows)

    require(data.get("source_pr_population_count") == 45, "lifecycle population must be 45")
    require(len(rows) == 45, "lifecycle ledger must contain 45 records")
    require(data.get("frozen_cutoff_utc") == frozen.get("cutoff_utc"), "lifecycle cutoff differs from frozen snapshot")
    require(data.get("frozen_main") == frozen.get("main_sha"), "lifecycle frozen main differs")
    require(set(data.get("allowed_integration_dispositions", [])) == ALLOWED_DISPOSITIONS, "lifecycle disposition vocabulary mismatch")
    require(set(data.get("allowed_recommended_actions", [])) == ALLOWED_ACTIONS, "lifecycle action vocabulary mismatch")

    numbers = [row.get("number") for row in rows]
    require(set(numbers) == set(frozen_rows), "lifecycle PR population differs from frozen source population")
    require(len(numbers) == len(set(numbers)), "duplicate PR number in lifecycle ledger")

    required_nonempty = {
        "title",
        "cutoff_head",
        "review_status",
        "mathematical_review_verdict",
        "claim_level_exceptions",
        "current_head",
        "current_head_observed_at_utc",
        "post_cutoff_delta",
        "delta_from_reviewed_sha_classification",
        "remaining_useful_material",
        "integration_disposition",
        "recommended_repository_action",
        "closure_criteria",
        "durable_destination_before_closure",
        "dependency_or_merge_order",
        "rationale",
    }

    for row in rows:
        number = row["number"]
        for field in required_nonempty:
            require(isinstance(row.get(field), str) and row[field].strip(), f"empty lifecycle field {field} for PR #{number}")
        require_sha(row["cutoff_head"], f"lifecycle cutoff head PR #{number}")
        require_sha(row["current_head"], f"lifecycle current head PR #{number}")
        require(row["cutoff_head"] == frozen_rows[number]["head_sha_at_cutoff"], f"cutoff head mismatch for PR #{number}")
        require(row["integration_disposition"] in ALLOWED_DISPOSITIONS, f"invalid disposition for PR #{number}")
        require(row["recommended_repository_action"] in ALLOWED_ACTIONS, f"invalid action for PR #{number}")
        require(isinstance(row.get("prerequisites"), list) and row["prerequisites"], f"missing prerequisites for PR #{number}")
        require(isinstance(row.get("links"), dict) and row["links"].get("pull_request"), f"missing links for PR #{number}")
        require(isinstance(row.get("integrated_records"), list), f"integrated_records must be a list for PR #{number}")
        require(isinstance(row.get("secondary_dispositions"), list), f"secondary_dispositions must be a list for PR #{number}")
        require(all(x in ALLOWED_DISPOSITIONS for x in row["secondary_dispositions"]), f"invalid secondary disposition for PR #{number}")
        reviewed_sha = row.get("reviewed_sha")
        frozen_reviewed = frozen_rows[number].get("reviewed_sha")
        require(reviewed_sha == frozen_reviewed, f"reviewed SHA mismatch for PR #{number}")
        if reviewed_sha is not None:
            require_sha(reviewed_sha, f"lifecycle reviewed head PR #{number}")
        else:
            require(row["integration_disposition"] == "UNREVIEWED", f"unreviewed PR #{number} must use UNREVIEWED disposition")
            require(row["recommended_repository_action"] == "NO ACTION UNTIL REVIEW", f"unreviewed PR #{number} must defer action")

    pr74 = next(row for row in rows if row["number"] == 74)
    require(pr74["integration_disposition"] == "SUPERSEDED/ABSORBED", "PR #74 lifecycle decision changed")
    require("PR #84" in pr74["closure_criteria"], "PR #74 closure trigger must cite PR #84")
    require("not as mathematically rejected" in pr74["closure_criteria"], "PR #74 closure semantics missing")

    dispositions = Counter(row["integration_disposition"] for row in rows)
    actions = Counter(row["recommended_repository_action"] for row in rows)
    require(dict(dispositions) == data.get("disposition_counts"), "lifecycle disposition counts do not match index")
    require(dict(actions) == data.get("recommended_action_counts"), "lifecycle action counts do not match index")
    return dispositions, actions


def check_registry() -> tuple[int, int, int]:
    registry = load_json(ROOT / "claims/registry.json")
    require(registry.get("schema_version") == "1.1", "registry schema must be 1.1")
    parts = registry.get("parts", [])
    require(parts, "registry part index is empty")
    records: list[dict[str, Any]] = []
    for part in parts:
        part_path = ROOT / "claims" / part["path"]
        part_data = load_json(part_path)
        part_records = part_data.get("records", [])
        require(len(part_records) == part.get("record_count"), f"registry part count mismatch: {part.get('path')}")
        require([r.get("id") for r in part_records] == part.get("ids"), f"registry part ID mismatch: {part.get('path')}")
        records.extend(part_records)
    require(len(records) == registry.get("record_count"), "registry total count mismatch")
    ids = [record.get("id") for record in records]
    require(len(ids) == len(set(ids)), "duplicate registry IDs")
    require(all(isinstance(x, str) and x for x in ids), "empty registry ID")
    require("RD-BRIDGE-001" in ids, "missing SC*/FC* bridge obligation")

    canonical_count = 0
    roadmap_count = 0
    for record in records:
        rid = record["id"]
        require(record.get("mathematical_status") in ALLOWED_MATH, f"invalid mathematical status for {rid}")
        require(record.get("integration_status") in ALLOWED_INTEGRATION, f"invalid integration status for {rid}")
        require(record.get("promotion_state") in ALLOWED_PROMOTION, f"invalid promotion state for {rid}")
        require(record.get("proof_residency") in ALLOWED_PROOF_RESIDENCY, f"invalid proof residency for {rid}")
        require(isinstance(record.get("promotion_gate"), str) and record["promotion_gate"].strip(), f"missing promotion gate for {rid}")
        require(isinstance(record.get("record_specific_promotion_review"), str) and record["record_specific_promotion_review"].strip(), f"missing review gate for {rid}")
        if record.get("integration_status") == "canonical":
            require(isinstance(record.get("proof_import_plan"), str) and record["proof_import_plan"].strip(), f"missing import plan for {rid}")
        require(bool(record.get("statement")), f"missing statement for {rid}")
        require(bool(record.get("scope")), f"missing scope for {rid}")
        for source in record.get("sources", []):
            require(isinstance(source.get("pr"), int), f"invalid source PR for {rid}")
            require_sha(source.get("commit"), f"source {rid}")
            require(source.get("claim_ids"), f"missing source claim IDs for {rid}")
            require(source.get("paths"), f"missing source paths for {rid}")
        review = record.get("review", {})
        require_sha(review.get("report_ref"), f"review report {rid}")
        require(bool(review.get("report_path")), f"missing report path for {rid}")

        if record["integration_status"] == "canonical":
            canonical_count += 1
            require(record["promotion_state"] in {"candidate_in_draft_pr", "accepted_reference_record", "accepted_with_local_proof"}, f"bad canonical promotion state for {rid}")
        if record["integration_status"] == "roadmap":
            roadmap_count += 1
            require(record["promotion_state"] in {"roadmap_candidate_in_draft_pr", "roadmap_accepted"}, f"bad roadmap promotion state for {rid}")

    require(canonical_count == 8, f"expected 8 candidate/accepted canonical records, found {canonical_count}")
    require(roadmap_count == 3, f"expected 3 roadmap records, found {roadmap_count}")

    canonical_md = (ROOT / "claims/CANONICAL.md").read_text(encoding="utf-8")
    for rid in ids:
        require(rid in canonical_md, f"{rid} missing from CANONICAL.md")
    require("candidate-canonical" in canonical_md.lower() or "candidate canonical" in canonical_md.lower(), "CANONICAL.md must expose draft promotion boundary")

    aliases = load_json(ROOT / "claims/aliases.json")
    alias_targets = set(aliases.get("canonical_aliases", {}))
    require(alias_targets.issubset(set(ids)), f"alias targets missing from registry: {sorted(alias_targets - set(ids))}")
    return len(records), canonical_count, roadmap_count


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
        "docs/integration/2026-08-02-lifecycle/README.md",
        "docs/integration/2026-08-02-lifecycle/PR_LIFECYCLE.md",
        "docs/integration/2026-08-02-lifecycle/PROOF_IMPORT_PLAN.md",
        "docs/integration/2026-08-02-lifecycle/PROMOTION_AUDIT.md",
        "docs/integration/2026-08-02-lifecycle/SC_FC_BRIDGE.md",
        "docs/integration/2026-08-02-lifecycle/NEXT_WAVES.md",
        "docs/integration/2026-08-02-lifecycle/OWNER_DECISIONS.md",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/A-03-20.md",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/B-32-50.md",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/C-51-64.md",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/D-65-74.md",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/E-76-83.md",
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

    for rel in [
        "claims/registry.json",
        "claims/registry/canonical-1.json",
        "claims/registry/canonical-2.json",
        "claims/registry/roadmap.json",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle.json",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/records-A1-03-11.json",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/records-A2-12-20.json",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/records-B1-32-38.json",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/records-B2-42-50.json",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/records-C1-51-57.json",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/records-C2-60-64.json",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/records-D1-65-69.json",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/records-D2-70-74.json",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/records-E1-76-79.json",
        "docs/integration/2026-08-02-lifecycle/pr-lifecycle/records-E2-80-83.json",
    ]:
        require((ROOT / rel).is_file(), f"missing lifecycle machine-readable part: {rel}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    require("unsolved" in readme, "README must state that Collatz is unsolved")
    require("finite compatibility" in readme and "2-adic completion" in readme, "README must preserve extraction boundaries")
    require("candidate canonical" in readme or "candidate-canonical" in readme, "README must expose draft promotion state")
    require("proposed roadmap bridge" in readme, "README must not overstate SC*/FC* bridge")

    current = (ROOT / "docs/integration/CURRENT.md").read_text(encoding="utf-8")
    require("2026-08-01" in current and "2026-08-02-lifecycle" in current, "CURRENT.md must point to snapshot and lifecycle continuation")


def main() -> int:
    try:
        pr_count, reviewed_count = check_frozen_snapshot()
        dispositions, actions = check_lifecycle()
        record_count, canonical_count, roadmap_count = check_registry()
        check_navigation()
    except CheckError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print(
        "OK: "
        f"{pr_count} frozen source PRs, {reviewed_count} reviewed at exact SHAs; "
        f"{sum(dispositions.values())} lifecycle dispositions; "
        f"{record_count} registry records ({canonical_count} candidate/accepted canonical, "
        f"{roadmap_count} roadmap)."
    )
    print("Disposition counts:", json.dumps(dict(sorted(dispositions.items())), ensure_ascii=False, sort_keys=True))
    print("Recommended action counts:", json.dumps(dict(sorted(actions.items())), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
