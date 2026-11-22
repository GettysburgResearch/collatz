#!/usr/bin/env python3
"""Rebuild the finite phase module and independently audit its public declarations.

Requires the existing pinned compiler and a tracked-clean pinned Mathlib
checkout. It performs no dependency installation or download.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

MATHLIB_PIN = "d13f23b723b8a846827a245b89c10fc7d3f11612"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
ROOT = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def capture(command: list[str], *, cwd: Path, env=None) -> str:
    return subprocess.check_output(command, cwd=cwd, env=env, text=True,
                                   stderr=subprocess.STDOUT).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--lake", type=Path, required=True)
    parser.add_argument("--output", type=Path,
                        help="External build/evidence directory; defaults to a fresh temporary directory")
    args = parser.parse_args()
    mathlib, lean, lake = (p.resolve() for p in (args.mathlib, args.lean, args.lake))
    version = capture([str(lean), "--version"], cwd=ROOT)
    if "version 4.34.1," not in version:
        raise SystemExit(f"Wrong Lean version: {version}")
    head = capture(["git", "rev-parse", "HEAD"], cwd=mathlib)
    if head != MATHLIB_PIN:
        raise SystemExit(f"Expected Mathlib {MATHLIB_PIN}; found {head}")
    subprocess.run(["git", "diff", "--quiet", "HEAD", "--"], cwd=mathlib, check=True)

    imports = {}
    for line in (ROOT / "imports.sha256").read_text().splitlines():
        expected, relative = line.split(maxsplit=1)
        relative = relative.lstrip("*")
        path = (mathlib / relative).resolve()
        if not path.is_relative_to(mathlib) or digest(path) != expected:
            raise SystemExit(f"Import source hash mismatch: {relative}")
        imports[relative] = expected

    proof = ROOT / "ActualPhaseEstimate.lean"
    source = proof.read_text()
    if re.search(r"\b(?:sorry|admit)\b|^\s*(?:axiom|opaque)\s", source, re.MULTILINE):
        raise SystemExit("Proof source contains a forbidden placeholder or axiom declaration")
    declarations = re.findall(r"^(?:def|theorem)\s+(\w+)", source, re.MULTILINE)
    full_names = {f"CollatzActualPhase.{name}" for name in declarations}
    audit = ROOT / "AuditActualPhaseEstimate.lean"
    audited = set(re.findall(r"^#print axioms (\S+)", audit.read_text(), re.MULTILINE))
    if audited != full_names:
        raise SystemExit(f"Audit mismatch: missing={full_names-audited}, extra={audited-full_names}")

    output = (args.output or Path(tempfile.mkdtemp(prefix="collatz-phase-build-"))).resolve()
    if output.is_relative_to(ROOT.parents[3]):
        raise SystemExit("The output directory must be outside the repository checkout")
    build = output / "oleans"
    evidence = output
    build.mkdir(parents=True, exist_ok=True)
    evidence.mkdir(parents=True, exist_ok=True)
    lake_path = capture([str(lake), "env", "printenv", "LEAN_PATH"], cwd=mathlib)
    env = dict(os.environ)
    env["LEAN_PATH"] = f"{build}:{ROOT}:{lake_path}"
    commands = []
    outputs = {}
    for module in ("ActualPhaseEstimate", "AuditActualPhaseEstimate"):
        command = [str(lean), "-j1", "-DautoImplicit=false", "-DwarningAsError=true", "-o",
                   str(build / f"{module}.olean"), str(ROOT / f"{module}.lean")]
        print(f"Checking {module}", flush=True)
        run = subprocess.run(command, cwd=ROOT, env=env, text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (evidence / f"{module}.log").write_text(run.stdout)
        commands.append({"command": command, "exit_code": run.returncode})
        outputs[module] = run.stdout
        if run.returncode:
            print(run.stdout, end="")
            raise SystemExit(run.returncode)

    audit_text = outputs["AuditActualPhaseEstimate"]
    dependencies = {}
    for name, axioms in re.findall(
            r"'([^']+)' depends on axioms: \[([^\]]*)\]", audit_text, re.DOTALL):
        dependencies[name] = sorted(a.strip() for a in axioms.split(",") if a.strip())
    for name in re.findall(r"'([^']+)' does not depend on any axioms", audit_text):
        dependencies[name] = []
    if set(dependencies) != full_names:
        raise SystemExit(f"Compiler axiom output mismatch: {set(dependencies)^full_names}")
    if any(set(axioms) - ALLOWED_AXIOMS for axioms in dependencies.values()):
        raise SystemExit(f"Nonstandard axiom dependency: {dependencies}")

    receipt = {
        "status": "passed",
        "scope": "Finite actual-edge phase estimate and public-declaration axiom audit only",
        "lean_version": version,
        "lean_binary_sha256": digest(lean),
        "mathlib_commit": head,
        "mathlib_tracked_clean": True,
        "direct_import_source_sha256": imports,
        "source_sha256": {p.name: digest(p) for p in (proof, audit, ROOT / "build.py")},
        "commands": commands,
        "public_declarations": sorted(full_names),
        "axiom_dependencies": dependencies,
        "allowed_axioms": sorted(ALLOWED_AXIOMS),
        "downloads_performed": False,
    }
    (evidence / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"Passed: {len(full_names)} public declarations; standard axioms only.", flush=True)


if __name__ == "__main__":
    main()
