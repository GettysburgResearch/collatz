#!/usr/bin/env python3
"""Check this packet's exact file, review, source, and Lean-receipt bindings.

This checks identities and validation scope, not the truth of the written
analytic arguments. It does not compile Lean or rebuild historical proofs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path,
                        help="optional result JSON outside the checkout")
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    root = packet.parent.parent
    reports = root / "reports/2026-11-23-source-clock"
    if args.receipt and args.receipt.resolve().is_relative_to(root):
        parser.error("--receipt must be outside the checked repository")
    manifest = json.loads((reports / "FILES.json").read_text())
    sources = json.loads((packet / "SOURCES.json").read_text())
    reviews = json.loads((reports / "REVIEW_SCOPE.json").read_text())
    deps = json.loads((packet / "DEPENDENCIES.json").read_text())
    inventory = json.loads((packet / "THEOREMS.json").read_text())
    lean = json.loads((reports / "lean-check.json").read_text())
    for item in manifest["files"]:
        data = (root / item["path"]).read_bytes()
        require(sha(data) == item["sha256"] and len(data) == item["bytes"],
                "Manifest mismatch: " + item["path"])
    actual_files = {p.relative_to(root).as_posix()
                    for folder in (packet, reports) for p in folder.rglob("*")
                    if p.is_file() and p != reports / "FILES.json"}
    require(actual_files == {item["path"] for item in manifest["files"]},
            "Manifest does not cover exactly this packet's files")
    for item in sources["files"]:
        data = subprocess.check_output(
            ["git", "show", item["commit"] + ":" + item["path"]],
            cwd=root, timeout=30)
        require(sha(data) == item["sha256"] and len(data) == item["bytes"],
                "Frozen source mismatch: " + item["path"])
    for item in reviews["bindings"]:
        data = (root / item["artifact"]).read_bytes()
        review = (root / item["review"]).read_bytes()
        require(sha(data) == item["artifact_sha256"],
                "Reviewed artifact changed: " + item["artifact"])
        require(sha(review) == item["review_sha256"],
                "Review changed: " + item["review"])
        require(item["artifact_sha256"] in review.decode(),
                "Review does not identify the exact artifact")
    require(lean["status"] == "passed", "Lean receipt is not a pass")
    require(lean["mathlib_commit"] == deps["mathlib_commit"], "Mathlib pin mismatch")
    require(deps["lean_commit"] in lean["lean_version"], "Compiler pin mismatch")
    require(lean["direct_imports"] == deps["direct_mathlib_imports"],
            "Direct-import pins differ from compiled receipt")
    require(lean["warnings_as_errors"] and lean["fresh_local_output"],
            "Lean run does not meet the declared checking scope")
    require(lean["historical_project_modules_rebuilt"] == 0,
            "Unexpected historical rebuild")
    expected_names = ["CollatzSourceClock." + row["module"] + "." + name
                      for row in inventory["modules"] for name in row["theorems"]]
    require(len(expected_names) == inventory["public_theorem_count"] ==
            lean["new_public_theorem_count"], "Public theorem count mismatch")
    for item in lean["modules"]:
        require(item["exit_code"] == 0 and
                sha((root / item["path"]).read_bytes()) == item["sha256"],
                "Compiled source mismatch: " + item["path"])
    audit = lean["modules"][-1]
    require(audit["module"] == inventory["audit_module"] and
            audit["audited_declarations"] == expected_names,
            "Axiom audit does not cover the complete public inventory")
    require(set(audit["axioms"]) <= {"propext", "Classical.choice", "Quot.sound"},
            "Nonstandard axiom found")
    boot = lean["fresh_mathlib_dependencies"]
    require([{k: row[k] for k in ("module", "source_path", "sha256")}
             for row in boot] == deps["fresh_mathlib_dependencies"] and
            all(row["exit_code"] == 0 for row in boot),
            "Fresh Mathlib bootstrap does not match its pins")
    checked_links = 0
    for relative in sorted(actual_files):
        path = root / relative
        if path.suffix == ".json":
            json.loads(path.read_text())
        if path.suffix != ".md":
            continue
        for destination in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if ":" in destination or destination.startswith("#"):
                continue
            target = destination.split("#", 1)[0]
            require((path.parent / target).exists(),
                    f"Broken relative link in {relative}: {destination}")
            checked_links += 1
    result = {"status": "passed", "scope": "exact identities and scope, not mathematical proof",
              "manifest_files": len(manifest["files"]), "manifest_excludes_only_itself": True,
              "frozen_source_files": len(sources["files"]),
              "proof_review_bindings": len(reviews["bindings"]),
              "compiled_sources": len(lean["modules"]),
              "audited_declarations": len(expected_names),
              "fresh_mathlib_dependencies": len(boot), "relative_links": checked_links}
    output = json.dumps(result, indent=2) + "\n"
    if args.receipt:
        args.receipt.write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
