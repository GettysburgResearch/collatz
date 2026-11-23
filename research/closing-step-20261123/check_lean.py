#!/usr/bin/env python3
"""Freshly compile and audit the complete-label finite collision inequality.

Exact joint decoding is an explicit theorem premise; no carry-moment bound is assumed proved here.
Installed pinned Mathlib dependencies are reused without modification.
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


THEOREMS = ['weighted_sum_cauchy', 'labelled_collision_bound', 'complete_carry_recovery']
STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    mathlib = args.mathlib.resolve()
    lean = args.lean.resolve()
    reports = args.report_dir.resolve()
    reports.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env["PATH"] = str(lean.parent) + os.pathsep + env.get("PATH", "")
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if ("version 4.34.1," not in version
            or "5045d0056413266e57c625dcd7c365b10e377c52" not in version):
        raise SystemExit(f"Unexpected Lean compiler: {version}")
    pin = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib,
                                  text=True).strip()
    if pin != "d13f23b723b8a846827a245b89c10fc7d3f11612":
        raise SystemExit(f"Unexpected Mathlib: {pin}")
    if subprocess.check_output(["git", "diff", "HEAD", "--name-only"],
                               cwd=mathlib, text=True).strip():
        raise SystemExit("Mathlib has modified tracked source files")
    source = packet / "lean/WeightedCollision.lean"
    audit = packet / "lean/WeightedCollisionAudit.lean"
    if re.findall(r"^theorem\s+(\w+)", source.read_text(), re.M) != THEOREMS:
        raise SystemExit("Public theorem inventory mismatch")
    imports = re.findall(r"^import\s+(\S+)", source.read_text(), re.M)
    dependency_hashes = {
        module: digest(mathlib / (module.replace(".", "/") + ".lean"))
        for module in imports
    }
    source_hashes = {p.name: digest(p) for p in (source, audit)}
    inherited = subprocess.check_output(
        [str(lean.with_name("lake")), "env", "printenv", "LEAN_PATH"],
        cwd=mathlib, env=env, text=True).strip()
    expected = [f"CollatzClosing.WeightedCollision.{name}"
                for name in THEOREMS]
    report = {
        "status": "running", "lean_version": version,
        "lean_binary_sha256": digest(lean), "mathlib_commit": pin,
        "new_public_theorem_count": len(THEOREMS),
        "scope": "Finite weighted collision transport retaining all labels, plus full quotient/residue carry recovery; no infinite collision estimate or universal closure",
        "fresh_local_output": True, "warnings_as_errors": True,
        "historical_project_modules_rebuilt": 0,
        "source_sha256": source_hashes,
        "direct_import_sha256": dependency_hashes,
        "modules": [],
    }
    logs = []
    with tempfile.TemporaryDirectory(prefix="collatz-weighted-collision-") as out:
        env["LEAN_PATH"] = out + os.pathsep + inherited
        for path in (source, audit):
            result = subprocess.run(
                [str(lean), "-j1", "-DwarningAsError=true", "-o",
                 str(Path(out) / (path.stem + ".olean")), str(path)],
                cwd=path.parent, env=env, text=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
            logs.append(f"MODULE {path.name}\n{result.stdout}")
            axioms = sorted({a.strip()
                             for group in re.findall(r"depends on axioms:\s*\[([^]]*)\]",
                                                     result.stdout, re.S)
                             for a in group.split(",") if a.strip()})
            audited = re.findall(
                r"'([^']+)' (?:depends on axioms:|does not depend on any axioms)",
                result.stdout)
            report["modules"].append({
                "module": path.stem, "exit_code": result.returncode,
                "axioms": axioms, "audited_declarations": audited,
            })
            if result.returncode or not set(axioms) <= STANDARD_AXIOMS:
                report["status"] = "failed"
                break
            if path == audit and audited != expected:
                report["status"] = "failed"
                report["error"] = "Incomplete declaration audit"
                break
    if any(digest(p) != source_hashes[p.name] for p in (source, audit)):
        report["status"] = "failed"
        report["error"] = "Source changed during compilation"
    if report["status"] == "running":
        report["status"] = "passed"
    (reports / "weighted-collision-lean-check.json").write_text(json.dumps(report, indent=2) + "\n")
    (reports / "weighted-collision-lean-build.log").write_text("\n".join(logs).rstrip() + "\n")
    print(json.dumps(report, indent=2))
    if report["status"] != "passed":
        print("\n".join(logs))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
