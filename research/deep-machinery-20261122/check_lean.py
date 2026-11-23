#!/usr/bin/env python3
"""Replay the pinned local dependencies and every new public theorem.

Uses a fresh output directory, an exact Lean/Mathlib pin, warnings as errors,
and a separate complete axiom audit. No dependencies are downloaded. Infinite
analytic statements in the written notes are outside this formal replay.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time


STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    root = packet.parent.parent
    manifest = json.loads((packet / "DEPENDENCIES.json").read_text())
    public = json.loads((packet / "THEOREMS.json").read_text())
    modules = list(manifest["files"])
    for item in modules:
        actual = hashlib.sha256((root / item["path"]).read_bytes()).hexdigest()
        if actual != item["sha256"]:
            raise SystemExit(f"Pinned source mismatch: {item['path']}")
    theorem_count = 0
    for item in public["modules"]:
        path = packet / "lean" / f"{item['module']}.lean"
        source = path.read_text()
        actual_names = re.findall(r"^theorem\s+(\w+)", source, re.M)
        if actual_names != item["theorems"]:
            raise SystemExit(f"Public theorem inventory mismatch: {path.name}")
        expected = len(item["theorems"])
        theorem_count += expected
        modules.append({"module": item["module"], "kind": "new",
                        "path": str(path.relative_to(root)), "expected_audits": expected})
    modules.append({"module": "DeepMachineryAudit", "kind": "audit",
                    "path": str((packet / "lean" / "DeepMachineryAudit.lean").relative_to(root)),
                    "expected_audits": theorem_count})
    if theorem_count != public["public_theorem_count"]:
        raise SystemExit("Public theorem total does not match inventory")
    lean = args.lean.resolve()
    mathlib = args.mathlib.resolve()
    report_dir = args.report_dir.resolve()
    report_dir.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env["PATH"] = str(lean.parent) + os.pathsep + env.get("PATH", "")
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if (f"version {manifest['lean_version']}," not in version
            or manifest["lean_commit"] not in version):
        raise SystemExit(f"Lean version mismatch: {version}")
    pin = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib,
                                  text=True).strip()
    if pin != manifest["mathlib_commit"]:
        raise SystemExit(f"Mathlib pin mismatch: {pin}")
    inherited = subprocess.check_output(
        [str(lean.with_name("lake")), "env", "printenv", "LEAN_PATH"],
        cwd=mathlib, env=env, text=True,
    ).strip()
    report = {
        "status": "running", "lean_version": version, "mathlib_commit": pin,
        "warnings_as_errors": True, "fresh_local_module_output": True,
        "module_count": len(modules), "new_public_theorem_count": theorem_count,
        "modules": [],
        "scope": "Pinned dependencies, all public theorems in THEOREMS.json, and a separate complete axiom audit.",
        "not_formalized": [
            "The imported population, canonical-envelope, and ordinary harmonic construction",
            "The Goldie comparison, conditional coding, and sibling singularity",
            "Symmetric recurrence and the canonical antisymmetric-current calculation",
            "The high-linear canonical sibling lower bound or a universal target merger",
            "Universal Collatz convergence, including exclusion of nontrivial cycles",
        ],
    }
    logs: list[str] = []

    def save() -> None:
        (report_dir / "lean-check.json").write_text(json.dumps(report, indent=2) + "\n")
        (report_dir / "lean-build.log").write_text("\n".join(logs).rstrip() + "\n")

    save()
    try:
        with tempfile.TemporaryDirectory(prefix="collatz-deep-machinery-build-") as tmp:
            env["LEAN_PATH"] = tmp + os.pathsep + inherited
            for item in modules:
                path = root / item["path"]
                start = time.monotonic()
                result = subprocess.run(
                    [str(lean), "-j1", "-DwarningAsError=true", "-o",
                     str(Path(tmp) / f"{item['module']}.olean"), str(path)],
                    cwd=path.parent, env=env, text=True, stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT, timeout=240,
                )
                seconds = round(time.monotonic() - start, 3)
                groups = re.findall(r"depends on axioms:\s*\[([^]]*)\]",
                                    result.stdout, re.S)
                axioms = sorted({a.strip() for group in groups
                                 for a in group.split(",") if a.strip()})
                # The audited arithmetic modules currently all print standard
                # dependencies. An axiom-free declaration is accepted too.
                axiom_free = len(re.findall(r"does not depend on any axioms", result.stdout))
                audit_count = len(groups) + axiom_free
                record = dict(item, sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                              exit_code=result.returncode, seconds=seconds,
                              printed_axioms=axioms, printed_audit_count=audit_count)
                report["modules"].append(record)
                logs.append(f"MODULE {item['module']}\n{result.stdout}\n")
                save()
                print(f"{item['module']}: exit={result.returncode}, {seconds}s", flush=True)
                if result.returncode or not set(axioms) <= STANDARD_AXIOMS:
                    print(result.stdout, flush=True)
                    raise RuntimeError(f"Replay failed for {item['module']}")
                if "expected_audits" in item and audit_count != item["expected_audits"]:
                    raise RuntimeError(f"Incomplete theorem audit: {item['module']}")
        report["status"] = "passed"
        save()
        print(f"Fresh replay passed; all {theorem_count} new public theorem audits are standard only.")
    except BaseException as error:
        report["status"] = "failed"
        report["error"] = str(error)
        save()
        raise


if __name__ == "__main__":
    main()
