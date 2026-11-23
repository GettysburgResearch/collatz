#!/usr/bin/env python3
"""Check new packet identities, review bindings, and recorded formal scope.

This does not check the truth of written proofs or recompile Lean. Pass
--check-sources after fetching the exact peer commits in SOURCES.json.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess


PACKET = Path(__file__).resolve().parent
ROOT = PACKET.parent.parent
REPORTS = ROOT / "reports/2026-11-23-closing-step"
STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def run(check_sources: bool) -> dict:
    manifest = read_json(PACKET / "MANIFEST.json")
    actual = {
        p.relative_to(ROOT).as_posix()
        for folder in (PACKET, REPORTS)
        for p in folder.rglob("*")
        if p.is_file() and p != PACKET / "MANIFEST.json"
    }
    expected = {row["path"] for row in manifest["files"]}
    require(len(expected) == len(manifest["files"]), "Duplicate manifest path")
    require(actual == expected,
            f"Manifest coverage differs: missing={sorted(expected-actual)}, "
            f"extra={sorted(actual-expected)}")
    for row in manifest["files"]:
        require(sha256(ROOT / row["path"]) == row["sha256"],
                f"File hash mismatch: {row['path']}")

    bindings = read_json(PACKET / "REVIEW_BINDINGS.json")["bindings"]
    for row in bindings:
        review = ROOT / row["review"]
        require(sha256(review) == row["review_sha256"],
                f"Review hash mismatch: {row['review']}")
        require(sha256(ROOT / row["target"]) == row["target_sha256"],
                f"Reviewed target changed: {row['target']}")
        require(row["target_sha256"] in review.read_text(),
                f"Review does not contain target hash: {row['review']}")

    inventory = read_json(PACKET / "THEOREMS.json")
    declarations = []
    compiled_sources = 0
    for module in inventory["modules"]:
        source = ROOT / module["source"]
        audit = ROOT / module["audit"]
        names = re.findall(r"^theorem\s+(\w+)", source.read_text(), re.M)
        require(names == module["theorems"],
                f"Public theorem inventory changed: {source.name}")
        full_names = [module["namespace"] + "." + name for name in names]
        declarations.extend(full_names)
        receipt = read_json(ROOT / module["receipt"])
        require(receipt["status"] == "passed", "Unsuccessful Lean receipt")
        require(receipt["fresh_local_output"] and receipt["warnings_as_errors"],
                "Lean receipt lacks fresh strict compilation")
        require(receipt["historical_project_modules_rebuilt"] == 0,
                "Unexpected historical proof rebuild")
        require(inventory["lean_commit"] in receipt["lean_version"]
                and f"version {inventory['lean_version']}," in receipt["lean_version"],
                "Lean compiler identity mismatch")
        require(receipt["lean_binary_sha256"] == inventory["lean_binary_sha256"],
                "Lean executable hash mismatch")
        require(receipt["mathlib_commit"] == inventory["mathlib_commit"],
                "Mathlib identity mismatch")
        require(receipt["new_public_theorem_count"] == len(names),
                "Receipt theorem count differs")
        for file in (source, audit):
            require(receipt["source_sha256"].get(file.name) == sha256(file),
                    f"Compiled source changed: {file.name}")
            compiled_sources += 1
        actual_audits = []
        for result in receipt["modules"]:
            require(result["exit_code"] == 0, "Failed compiler result")
            require(set(result["axioms"]) <= STANDARD_AXIOMS,
                    "Nonstandard axiom in recorded audit")
            actual_audits.extend(result["audited_declarations"])
        require(actual_audits == full_names, "Incomplete declaration audit")
        direct_imports = re.findall(r"^import\s+(\S+)", source.read_text(), re.M)
        require(set(direct_imports) == set(receipt["direct_import_sha256"]),
                "Direct import inventory differs")

    require(len(declarations) == inventory["public_theorem_count"] == 3,
            "Unexpected total public theorem count")
    require(len(set(declarations)) == len(declarations),
            "Duplicate public declaration")

    sources = read_json(PACKET / "SOURCES.json")["sources"]
    checked_sources = 0
    if check_sources:
        for row in sources:
            reference = f"{row['commit']}:{row['path']}"
            try:
                body = git("show", reference)
                blob = git("rev-parse", reference).decode().strip()
            except subprocess.CalledProcessError as exc:
                raise ValueError(
                    f"Missing source object {reference}; fetch its exact commit first"
                ) from exc
            require(blob == row["git_blob"], f"Source blob differs: {reference}")
            require(hashlib.sha256(body).hexdigest() == row["sha256"],
                    f"Source contents differ: {reference}")
            checked_sources += 1

    snapshot = read_json(REPORTS / "SOURCE_REFRESH.json")
    require(snapshot["own_base"] == "7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161",
            "Own base-head provenance differs")
    require(len(snapshot["advanced_peer_heads"]) == 4,
            "Expected four refreshed peer branches")

    return {
        "schema": "collatz-closing-step-packet-check/v1",
        "status": "passed",
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "checkout_head": git("rev-parse", "HEAD").decode().strip(),
        "manifest_files": len(expected),
        "manifest_sha256": sha256(PACKET / "MANIFEST.json"),
        "review_bindings": len(bindings),
        "compiled_source_files": compiled_sources,
        "public_theorems": len(declarations),
        "source_files_listed": len(sources),
        "source_files_checked": checked_sources,
        "peer_source_check_requested": check_sources,
        "advanced_peer_branches": len(snapshot["advanced_peer_heads"]),
        "scope": "File/source identities, review bindings, and recorded fresh Lean core scope; not a proof of Collatz or a fresh compiler run.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-sources", action="store_true")
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    if args.receipt and args.receipt.resolve().is_relative_to(ROOT):
        parser.error("Write the check receipt outside the tested checkout")
    try:
        receipt = run(args.check_sources)
    except (ValueError, OSError, KeyError, subprocess.SubprocessError) as exc:
        receipt = {"status": "failed", "error": str(exc)}
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))
    return 0 if receipt["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
