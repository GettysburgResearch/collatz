#!/usr/bin/env python3
"""Replay this packet against a built, exactly pinned Mathlib checkout.

Usage: python check_lean.py --mathlib /path/to/mathlib4 --lean /path/to/lean
       --report-dir /path/to/reports

The script recompiles every listed local module into a fresh directory.  It
does not assert or formalize the analytic population theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time


MATHLIB_PIN = "d13f23b723b8a846827a245b89c10fc7d3f11612"
LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
MODULES = [
    "ShellCover", "ForwardSection", "SectionDynamics", "RisingReturns",
    "CarryBlocks", "CarrySection", "BandTransport", "BandParityBridge",
    "BandPopulationCriterion",
    "UnitPopulationTransport", "WitnessGlobal",
    "InverseDensityPotential", "MarkedDensityPotential",
    "BandClosure", "Audit",
]
STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--lean", type=Path,
                        default=Path(shutil.which("lean") or "lean"))
    parser.add_argument("--report-dir", required=True, type=Path)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    source = packet / "lean"
    mathlib = args.mathlib.resolve()
    lean = args.lean.resolve()
    report_dir = args.report_dir.resolve()
    report_dir.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env["PATH"] = str(lean.parent) + os.pathsep + env.get("PATH", "")
    pin = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib,
                                  text=True).strip()
    if pin != MATHLIB_PIN:
        raise SystemExit(f"Mathlib pin mismatch: {pin}")
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if "version 4.34.1," not in version or LEAN_COMMIT not in version:
        raise SystemExit(f"Lean version mismatch: {version}")
    inherited = subprocess.check_output(
        [str(lean.with_name("lake")), "env", "printenv", "LEAN_PATH"],
        cwd=mathlib, env=env, text=True,
    ).strip()
    records = []
    logs = []
    with tempfile.TemporaryDirectory(prefix="forward-band-build-", dir=packet) as tmp:
        env["LEAN_PATH"] = tmp + os.pathsep + inherited
        for module in MODULES:
            path = source / f"{module}.lean"
            start = time.monotonic()
            result = subprocess.run(
                [str(lean), "-j1", "-DwarningAsError=true", "-o",
                 str(Path(tmp) / f"{module}.olean"), str(path)],
                cwd=source, env=env, text=True, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, timeout=180,
            )
            seconds = round(time.monotonic() - start, 3)
            logs.append(f"MODULE {module}\n{result.stdout}\n")
            axioms = sorted(set(
                item.strip()
                for group in re.findall(r"depends on axioms:\s*\[([^]]*)\]",
                                        result.stdout, re.S)
                for item in group.split(",") if item.strip()
            ))
            record = {
                "module": module, "source": f"lean/{module}.lean",
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "exit_code": result.returncode, "seconds": seconds,
                "printed_axioms": axioms,
            }
            records.append(record)
            (report_dir / "lean-build.log").write_text("\n".join(logs).rstrip() + "\n")
            print(f"{module}: exit={result.returncode}, {seconds}s", flush=True)
            if result.returncode or not set(axioms) <= STANDARD_AXIOMS:
                print(result.stdout, flush=True)
                raise SystemExit(f"Replay failed for {module}")
    report = {
        "status": "passed", "lean_version": version, "mathlib_commit": pin,
        "warnings_as_errors": True, "fresh_local_module_output": True,
        "module_count": len(records), "modules": records,
        "scope": "Local Lean modules and their printed axiom audits.",
        "not_formalized": [
            "The analytic controlled atom floor and marked population theorem",
            "Joint clock mixing and uniform natural predecessor density",
            "The Abel and harmonic ordinary inverse-envelope constructions",
            "A sublinear upper envelope on all large marked ordinary inputs",
            "An unconditional cubic survivor upper bound",
            "Universal Collatz convergence",
        ],
    }
    (report_dir / "lean-check.json").write_text(json.dumps(report, indent=2) + "\n")
    print("All local modules passed; printed axioms are standard only.", flush=True)


if __name__ == "__main__":
    main()
