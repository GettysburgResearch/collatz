#!/usr/bin/env python3
"""Cheap structural validation for the durable Collatz front door.

This checks navigation, registry semantics, exact provenance fields, and frozen
integration facts. It does not verify mathematics or replay scientific work.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

REQUIRED_ROOT_FILES = {"README.md", "AGENTS.md", "CONTRIBUTING.md", "STATE.md"}
REMOVED_ROOT_DASHBOARDS = {"START_HERE.md", "CURRENT_KNOWLEDGE.md", "FRONTIERS.md"}
REQUIRED_DURABLE_PATHS = {
    "docs/RESEARCH_MAP.md",
    "research/README.md",
    "research/RESULTS_CATALOG.md",
    "research/integrated/README.md",
    "research/integrated/ordinary-extraction/README.md",
    "research/integrated/completion-ghost/README.md",
    "research/integrated/periodic-tails/README.md",
    "research/integrated/coefficient-stopping/README.md",
    "research/integrated/finite-safety-automata/README.md",
    "research/integrated/six-branch-rigidity/README.md",
    "research/integrated/factor-complexity/README.md",
    "claims/README.md",
    "claims/CANONICAL.md",
    "claims/registry.json",
    "claims/registry/canonical-1.json",
    "claims/registry/canonical-2.json",
    "claims/registry/roadmap.json",
    "claims/aliases.json",
    "archive/README.md",
    "docs/integration/CURRENT.md",
    "docs/integration/2026-08-01/open-prs.json",
    "docs/integration/2026-08-02-lifecycle/pr-lifecycle.json",
}

STALE_PATTERNS = {
    "draft PR #84": re.compile(r"draft\s+PR\s+#84", re.I),
    "draft PR #85": re.compile(r"draft\s+PR\s+#85", re.I),
    "PR #85 URL": re.compile(r"github\.com/GettysburgResearch/collatz/pull/85", re.I),
    "round-specific branch": re.compile(r"agent/integration-front-door-round1", re.I),
    "round-specific prose": re.compile(r"\bRound\s+1\b|\bRound\s+2\b", re.I),
    "draft packet metadata": re.compile(r"local_packets_introduced_by_draft_pr|proof_residency_gate", re.I),
    "active candidate state": re.compile(r'"promotion_state"\s*:\s*"(?:roadmap_)?candidate_in_draft_pr"'),
}


class CheckError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckError(message)


def load_json(relative: str) -> Any:
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CheckError(f"missing JSON: {relative}") from exc
    except json.JSONDecodeError as exc:
        raise CheckError(f"invalid JSON in {relative}: {exc}") from exc


def require_sha(value: Any, label: str) -> None:
    require(isinstance(value, str) and SHA_RE.fullmatch(value) is not None, f"invalid SHA for {label}")


def active_markdown_files() -> list[Path]:
    files = [
        ROOT / "README.md",
        ROOT / "AGENTS.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "STATE.md",
        ROOT / "docs/RESEARCH_MAP.md",
        ROOT / "research/README.md",
        ROOT / "research/RESULTS_CATALOG.md",
        ROOT / "claims/README.md",
        ROOT / "claims/CANONICAL.md",
        ROOT / "archive/README.md",
        ROOT / "docs/integration/CURRENT.md",
    ]
    files.extend(sorted((ROOT / "research/integrated").rglob("*.md")))
    return files


def active_text_files() -> list[Path]:
    files = active_markdown_files()
    files.extend(
        ROOT / rel
        for rel in (
            "claims/registry.json",
            "claims/registry/canonical-1.json",
            "claims/registry/canonical-2.json",
            "claims/registry/roadmap.json",
            "claims/aliases.json",
        )
    )
    return files


def check_tree() -> None:
    for relative in REQUIRED_ROOT_FILES | REQUIRED_DURABLE_PATHS:
        require((ROOT / relative).exists(), f"missing required path: {relative}")
    for relative in REMOVED_ROOT_DASHBOARDS:
        require(not (ROOT / relative).exists(), f"redundant root dashboard still present: {relative}")
    require(not (ROOT / "archive/integration/README.md").exists(), "redundant second archive index still present")


def check_links() -> int:
    checked = 0
    for path in active_markdown_files():
        relative = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError as exc:
                raise CheckError(f"link escapes repository: {relative} -> {target}") from exc
            require(resolved.exists(), f"broken local link: {relative} -> {target}")
            checked += 1
    return checked


def check_no_stale_transactional_language() -> None:
    for path in active_text_files():
        relative = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        for label, pattern in STALE_PATTERNS.items():
            require(pattern.search(text) is None, f"stale transactional language ({label}) in {relative}")


def load_records() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    registry = load_json("claims/registry.json")
    require(registry.get("schema_version") == "1.3", "registry schema must be 1.3")
    require(registry.get("record_count") == 11, "registry must index 11 records")
    require_sha(registry.get("accepted_by_merge_commit"), "accepted_by_merge_commit")

    records: list[dict[str, Any]] = []
    for part in registry.get("parts", []):
        part_path = "claims/" + part["path"]
        data = load_json(part_path)
        part_records = data.get("records", [])
        require(len(part_records) == part.get("record_count"), f"part count mismatch: {part_path}")
        require([row.get("id") for row in part_records] == part.get("ids"), f"part ID mismatch: {part_path}")
        records.extend(part_records)
    require(len(records) == 11, "loaded record count must be 11")
    ids = [row.get("id") for row in records]
    require(len(ids) == len(set(ids)), "duplicate registry ID")
    return registry, records


def check_registry() -> tuple[int, int, int]:
    registry, records = load_records()
    by_id = {row["id"]: row for row in records}
    expected_canonical = {
        "IC-EXTRACT-001", "IC-GHOST-001", "IC-PERIODIC-001", "IC-SC-001",
        "IC-AUT-001", "IC-RIG-001", "IC-REF-001", "IC-REP-001",
    }
    expected_roadmap = {"RD-SC-001", "RD-FC-001", "RD-BRIDGE-001"}
    require(expected_canonical | expected_roadmap == set(by_id), "registry ID set changed")
    require("candidate_in_draft_pr" not in registry.get("status_vocabulary", {}).get("promotion_state", []), "active promotion vocabulary still exposes candidate-in-draft state")

    for rid in expected_canonical:
        row = by_id[rid]
        require(row.get("integration_status") == "canonical", f"{rid} must be canonical")
        require(row.get("promotion_state") in {"accepted_reference_record", "accepted_with_local_proof"}, f"invalid accepted state for {rid}")
        require(row.get("proof_residency") == "local_proof_packet", f"{rid} must have local proof residency")
        packet = row.get("local_packet")
        require(isinstance(packet, str) and (ROOT / packet).is_file(), f"missing local packet for {rid}")
        for source in row.get("sources", []):
            require(isinstance(source.get("pr"), int), f"invalid source PR for {rid}")
            require_sha(source.get("commit"), f"source {rid}")
            require(source.get("claim_ids"), f"missing source claim IDs for {rid}")
            require(source.get("paths"), f"missing source paths for {rid}")
        review = row.get("review", {})
        require_sha(review.get("report_ref"), f"review {rid}")
        require(isinstance(review.get("report_path"), str) and review["report_path"], f"missing review path for {rid}")

    exact_local_verified = {"IC-EXTRACT-001", "IC-GHOST-001", "IC-SC-001", "IC-AUT-001", "IC-RIG-001", "IC-REP-001"}
    for rid in exact_local_verified:
        row = by_id[rid]
        require(row.get("mathematical_status") == "verified", f"{rid} must remain verified")
        require(row.get("promotion_state") == "accepted_with_local_proof", f"{rid} must be accepted_with_local_proof")

    ref = by_id["IC-REF-001"]
    require(ref.get("mathematical_status") == "refuted", "IC-REF-001 must remain a refuted source statement")
    require(ref.get("promotion_state") == "accepted_with_local_proof", "IC-REF-001 refutation must be accepted with local proof")

    periodic = by_id["IC-PERIODIC-001"]
    require(periodic.get("mathematical_status") == "source-qualified", "pending periodic synthesis must not be marked verified")
    require(periodic.get("component_mathematical_status") == "verified_at_exact_source_shas", "periodic component status missing")
    require(periodic.get("integrated_statement_status") == "pending_narrow_review", "periodic synthesis review flag missing")
    require(periodic.get("promotion_state") == "accepted_reference_record", "periodic synthesis should remain a source-qualified reference")
    periodic_packet = (ROOT / periodic["local_packet"]).read_text(encoding="utf-8")
    require("PENDING NARROW INDEPENDENT REVIEW" in periodic_packet, "periodic packet lost its narrow-review warning")

    rig = by_id["IC-RIG-001"]
    rig_scope = (rig.get("scope") or "").lower()
    for term in ("six-branch", "complete-tree", "full-tail", "finite-control", "eventual-integrality"):
        require(term in rig_scope, f"IC-RIG-001 scope lost load-bearing term: {term}")

    rep = by_id["IC-REP-001"]
    require(rep.get("dependency_residency") == "source-pinned", "IC-REP-001 dependency residency must be source-pinned")
    require(rep.get("self_contained") is False, "IC-REP-001 must not be called self-contained")
    deps = rep.get("dependency_sources", [])
    require(len(deps) == 1, "IC-REP-001 must have one structured PR #16 dependency source")
    dep = deps[0]
    require(dep.get("pr") == 16, "factor dependency PR must be #16")
    require(dep.get("commit") == "900ba417c968d8a41bc56a30d3ccc941284d8ce2", "factor dependency source SHA mismatch")
    expected_paths = {
        "research/adelic-cusp/claims/L-9313-centered-error-full-shift-cylinder.md",
        "research/adelic-cusp/claims/T-9315-centered-rational-power-equivalence.md",
        "research/adelic-cusp/claims/T-9316-efficient-recurrence-thue-morse.md",
    }
    require({c.get("path") for c in dep.get("claims", [])} == expected_paths, "factor dependency paths mismatch")
    require(all(c.get("clause_used") for c in dep.get("claims", [])), "factor dependency clauses missing")
    require(dep.get("status") == "independently_verified_at_exact_source_sha", "factor dependency status missing")
    dep_review = dep.get("review", {})
    require(dep_review.get("review_ref") == "a518db7feece37513ddcda729553e8b8c4c4d657", "factor dependency review SHA mismatch")
    require(set(dep_review.get("report_paths", [])) == {
        "reports/gpt56-review-9315-01/2026-07-22-15-centered-recurrence-adversarial-review.md",
        "reports/gpt56-review-9315-01/CLAIM_MATRIX.md",
    }, "factor dependency review paths mismatch")
    factor_packet = (ROOT / rep["local_packet"]).read_text(encoding="utf-8")
    for token in (dep["commit"], dep_review["review_ref"], *expected_paths, *dep_review["report_paths"]):
        require(token in factor_packet, f"factor packet missing exact dependency provenance: {token}")
    require("not self-contained" in factor_packet.lower(), "factor packet must say it is not self-contained")

    for rid in expected_roadmap:
        row = by_id[rid]
        require(row.get("integration_status") == "roadmap", f"{rid} must remain roadmap")
        require(row.get("promotion_state") == "roadmap_accepted", f"{rid} roadmap acceptance missing")
        require(row.get("proof_residency") == "open_obligation", f"{rid} must remain an open obligation")
    require(by_id["RD-SC-001"].get("mathematical_status") == "open", "SC* must remain open")
    require(by_id["RD-FC-001"].get("mathematical_status") == "open", "FC* must remain open")
    bridge = by_id["RD-BRIDGE-001"]
    require(bridge.get("mathematical_status") == "proposed", "bridge must remain proposed")
    require(bridge.get("integrated_statement_status") == "pending_narrow_review", "bridge review flag missing")

    aliases = load_json("claims/aliases.json")
    require(set(aliases.get("canonical_aliases", {})) == expected_canonical | expected_roadmap, "alias target set mismatch")
    return len(expected_canonical), len(expected_roadmap), len(exact_local_verified)


def check_catalog() -> int:
    text = (ROOT / "research/RESULTS_CATALOG.md").read_text(encoding="utf-8")
    required_families = [
        "Centered/adelic", "Corrected 256-stage", "H induced-system", "Regular-sanctuary",
        "Padé", "Full-denominator cycle", "quotient-refund", "Negative-cycle pulse",
        "Positive coefficient", "Six-branch extensions", "Rewrite/termination", "5x+1",
        "Literature and cross-model",
    ]
    for family in required_families:
        require(family.lower() in text.lower(), f"results catalog missing family: {family}")
    require(text.count("https://github.com/GettysburgResearch/collatz/commit/") >= 12, "catalog lacks exact-SHA source pointers")
    require(text.count("review") >= 12, "catalog lacks review boundaries")
    require("#67, #68, and #69" in text, "catalog must preserve unreviewed frozen-wave boundary")
    return len(required_families)


def check_frozen_archive() -> tuple[int, int]:
    snapshot = load_json("docs/integration/2026-08-01/open-prs.json")
    require(snapshot.get("cutoff_utc") == "2026-08-01T21:16:40Z", "frozen cutoff changed")
    require(snapshot.get("main_sha") == "0ae0c67bb058f9a7c56cc7744fe5bf2650a7cb84", "frozen main changed")
    require(snapshot.get("open_pr_count") == 45, "frozen source PR count changed")
    rows = snapshot.get("open_prs", [])
    require(len(rows) == 45, "frozen snapshot must have 45 rows")
    require(set(snapshot.get("unreviewed_prs", [])) == {67, 68, 69}, "frozen unreviewed set changed")
    reviewed = sum(row.get("reviewed_sha") is not None for row in rows)
    require(reviewed == 42, f"expected 42 reviewed frozen PRs, found {reviewed}")
    for row in rows:
        require_sha(row.get("head_sha_at_cutoff"), f"cutoff PR #{row.get('number')}")
        if row.get("reviewed_sha") is not None:
            require_sha(row["reviewed_sha"], f"reviewed PR #{row.get('number')}")

    lifecycle = load_json("docs/integration/2026-08-02-lifecycle/pr-lifecycle.json")
    require(lifecycle.get("source_pr_population_count") == 45, "lifecycle source population changed")
    require(lifecycle.get("frozen_cutoff_utc") == snapshot.get("cutoff_utc"), "lifecycle cutoff mismatch")
    require(lifecycle.get("frozen_main") == snapshot.get("main_sha"), "lifecycle frozen main mismatch")
    return len(rows), reviewed


def main() -> int:
    try:
        check_tree()
        link_count = check_links()
        check_no_stale_transactional_language()
        canonical_count, roadmap_count, verified_count = check_registry()
        family_count = check_catalog()
        frozen_count, reviewed_count = check_frozen_archive()
    except CheckError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        "OK: durable front door; "
        f"{canonical_count} integrated records "
        f"({verified_count} verified local proofs, 1 accepted refutation, 1 source-qualified periodic synthesis), "
        f"{roadmap_count} roadmap records, {family_count} reviewed research families, "
        f"{link_count} curated local links, frozen {frozen_count}/{reviewed_count} PR snapshot preserved."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
