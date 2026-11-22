#!/usr/bin/env python3
"""Rebuild the whole-repository continuation into fresh Lean output.

The complete certificate, signed carry, affine merger, finite profile and
inverse-history modules use core Lean only. This driver never imports previously compiled project
or vendored project objects, and does not require Mathlib.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time


VENDOR_ORDER = [
    "ReverseBasin146", "Closure", "Witness", "DirectedInduction",
    "WitnessEnergy", "SourceWitness", "GapMultiset", "UnboundedGapReset",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    args = parser.parse_args()
    project = Path(__file__).resolve().parent
    lean = args.lean.absolute()
    output = args.output.resolve()
    receipt = args.receipt.resolve()
    if output.exists() and any(output.rglob("*.olean")):
        parser.error("--output must not contain precompiled .olean files")
    output.mkdir(parents=True, exist_ok=True)
    receipt.parent.mkdir(parents=True, exist_ok=True)
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if "version 4.34.1," not in version:
        parser.error(f"unexpected Lean version: {version}")

    upstream = json.loads((project / "vendor/pr177/SOURCE.json").read_text())
    for row in upstream["files"]:
        path = project / row["local_path"]
        if digest(path) != row["sha256"]:
            parser.error(f"frozen upstream bytes changed: {row['local_path']}")
        blob = hashlib.sha1(b"blob " + str(path.stat().st_size).encode() + b"\0" + path.read_bytes()).hexdigest()
        if blob != row["git_blob_sha"]:
            parser.error(f"frozen upstream Git blob mismatch: {row['local_path']}")

    modules = [(f"Collatz.{name}", f"vendor/pr177/Collatz/{name}.lean")
               for name in VENDOR_ORDER]
    modules += [(f"CollatzGlobalClosure.{name}", f"CollatzGlobalClosure/{name}.lean")
                for name in ["EndpointSteering", "InverseBudget",
                             "ReservedMergerCompleteness", "MaximalReserve",
                             "AsynchronousReset", "TerminalReset",
                             "PeriodicTraceTail", "SignedCarry", "SignedCarryReturns",
                             "MergerClockRigidity", "OddReturnClock", "FiniteProfileDrift"]]
    modules.append(("CollatzGlobalClosureCore", "CollatzGlobalClosureCore.lean"))
    paths = [output]
    env = os.environ.copy()
    env["LEAN_PATH"] = os.pathsep.join(map(str, paths))
    report = {
        "status": "RUNNING",
        "scope": "core-only complete-certificate, signed carry, affine merger, finite profile, inverse-history, and finite-trace continuation",
        "lean_version": version,
        "mathlib_required": False,
        "driver_sha256": digest(Path(__file__).resolve()),
        "upstream": upstream,
        "project": str(project),
        "fresh_output": str(output),
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
            "module": module, "source": relative, "source_sha256": digest(source),
            "command": command, "exit_code": result.returncode,
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
        row["stdout"].count("depends on axioms:") +
        row["stdout"].count("does not depend on any axioms")
        for row in report["commands"]
    )
    save()
    print(f"Passed {len(modules)} source compilations; receipt: {receipt}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
