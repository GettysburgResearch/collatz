#!/usr/bin/env python3
"""Compile the section attack from sources into a fresh output directory.

Only the pinned mathlib/dependency cache is reused.  --full also rebuilds the
earlier project modules and the project entrypoint.  Every command, source hash,
exit status, and axiom report is retained in the requested JSON receipt.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


MATHLIB_PIN = "d13f23b723b8a846827a245b89c10fc7d3f11612"
LEAN_VERSION = "4.34.1"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()
    project = Path(__file__).resolve().parent
    lean = args.lean.resolve()
    mathlib = args.mathlib.resolve()
    output = args.output.resolve()
    receipt = args.receipt.resolve()
    if output.exists() and any(output.rglob("*.olean")):
        parser.error("--output must not contain previously compiled .olean files")
    output.mkdir(parents=True, exist_ok=True)
    receipt.parent.mkdir(parents=True, exist_ok=True)
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if f"version {LEAN_VERSION}," not in version:
        parser.error(f"unexpected Lean version: {version}")
    mathlib_head = subprocess.check_output(
        ["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True
    ).strip()
    if mathlib_head != MATHLIB_PIN:
        parser.error(f"mathlib must be at {MATHLIB_PIN}; found {mathlib_head}")
    source_manifest = project / "vendor/pr173/SOURCE.json"
    upstream = json.loads(source_manifest.read_text(encoding="utf-8"))
    for row in upstream["files"]:
        if digest(project / row["local_path"]) != row["sha256"]:
            parser.error(f"frozen upstream source changed: {row['local_path']}")

    modules = [("CollatzGlobalClosure.EndpointSteering", "CollatzGlobalClosure/EndpointSteering.lean")]
    if args.full:
        modules += [
            (f"CollatzGlobalClosure.{name}", f"CollatzGlobalClosure/{name}.lean")
            for name in ["RelativeParityBarrier", "LocalProfileObstruction", "SiblingRigidity"]
        ]
    modules += [(name, f"vendor/pr173/{name}.lean") for name in [
        "ShellCover", "ForwardSection", "SectionDynamics", "RisingReturns"
    ]]
    modules += [
        (f"CollatzGlobalClosure.{name}", f"CollatzGlobalClosure/{name}.lean")
        for name in [
            "BandOffset", "MarkedCylinders", "MarkedResetWitness",
            "SectionResetReturns", "BandWord", "SectionBridge",
            "BandCollision", "SectionFeatureRanks"
        ]
    ]
    if args.full:
        modules.append(("CollatzGlobalClosure", "CollatzGlobalClosure.lean"))

    paths = [output, mathlib / ".lake/build/lib/lean"]
    paths += sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
    env = os.environ.copy()
    env["LEAN_PATH"] = os.pathsep.join(map(str, paths))
    report = {
        "status": "RUNNING",
        "scope": "full project" if args.full else "new band modules and exact frozen dependencies",
        "driver_sha256": digest(Path(__file__).resolve()),
        "project": str(project),
        "lean_version": version,
        "mathlib_head": mathlib_head,
        "upstream": upstream,
        "fresh_project_output": str(output),
        "LEAN_PATH": env["LEAN_PATH"],
        "commands": [],
    }

    def save() -> None:
        receipt.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    save()
    for module, relative in modules:
        source = project / relative
        dest = output.joinpath(*module.split(".")).with_suffix(".olean")
        dest.parent.mkdir(parents=True, exist_ok=True)
        command = [str(lean), "-j1", "-DwarningAsError=true", "-DautoImplicit=false",
                   "-o", str(dest), str(source)]
        start = time.monotonic()
        print(f"Compiling {module}", flush=True)
        result = subprocess.run(command, cwd=project, env=env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        row = {
            "module": module,
            "source": relative,
            "source_sha256": digest(source),
            "command": command,
            "exit_code": result.returncode,
            "elapsed_seconds": round(time.monotonic() - start, 3),
            "stdout": result.stdout,
            "olean_sha256": digest(dest) if result.returncode == 0 and dest.exists() else None,
        }
        report["commands"].append(row)
        print(f"  exit={result.returncode}, seconds={row['elapsed_seconds']}", flush=True)
        if result.stdout:
            print(result.stdout, end="" if result.stdout.endswith("\n") else "\n", flush=True)
        if result.returncode != 0:
            report["status"] = "FAILED"
            save()
            return result.returncode
        save()
    report["status"] = "PASSED"
    report["module_count"] = len(modules)
    report["axiom_report_count"] = sum(
        row["stdout"].count("depends on axioms:") + row["stdout"].count("does not depend on any axioms")
        for row in report["commands"]
    )
    save()
    print(f"Passed {len(modules)} source compilations; receipt: {receipt}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
