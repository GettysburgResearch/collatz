#!/usr/bin/env python3
"""Replay the pinned section imports and all new proofs in a fresh output directory."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time


MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
MODULES = [
    "ShellCover", "ForwardSection", "SectionDynamics", "RisingReturns",
    "BandSteering", "FanGeometry", "CountCriterion", "PopulationTransfer",
    "BandCriterion", "SectionTransport", "Audit",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True,
                        help="New, empty directory for generated Lean outputs")
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    source = base / "lean"
    mathlib = args.mathlib.resolve()
    lean = args.lean.resolve()
    out = args.out.resolve()
    receipt_path = args.receipt.resolve()
    if out.exists() and any(out.iterdir()):
        parser.error("--out must be absent or empty; old project outputs are not reused")
    out.mkdir(parents=True, exist_ok=True)
    receipt_path.parent.mkdir(parents=True, exist_ok=True)

    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    actual_lean = subprocess.check_output([str(lean), "--githash"], text=True).strip()
    actual_mathlib = subprocess.check_output(
        ["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip()
    if actual_lean != LEAN_COMMIT or actual_mathlib != MATHLIB_COMMIT:
        parser.error("Lean or mathlib does not match the documented exact pin")

    before = {p.name: digest(p) for p in sorted(source.glob("*.lean"))}
    pins = json.loads((base / "upstream-pins.json").read_text())
    for name, expected in pins["sha256"].items():
        if before.get(name) != expected:
            parser.error(f"Pinned upstream source mismatch: {name}")

    paths = [out, mathlib / ".lake/build/lib/lean"]
    paths.extend(sorted(p / ".lake/build/lib/lean"
                        for p in (mathlib / ".lake/packages").iterdir()
                        if (p / ".lake/build/lib/lean").is_dir()))
    env = os.environ.copy()
    env["LEAN_PATH"] = os.pathsep.join(map(str, paths))
    commands = []
    result = {
        "schema": "collatz-marked-population-lean-replay/v1",
        "scope": "Pinned imports and new partial theorem types; not a proof of Collatz",
        "lean_version": version,
        "lean_commit": actual_lean,
        "mathlib_commit": actual_mathlib,
        "upstream": pins,
        "source_sha256_before": before,
        "fresh_output_directory": str(out),
        "commands": commands,
        "success": False,
    }
    for module in MODULES:
        argv = [str(lean), "-j1", "--root=" + str(source),
                "-DwarningAsError=true", "-o", str(out / (module + ".olean")),
                str(source / (module + ".lean"))]
        started = time.monotonic()
        proc = subprocess.run(argv, env=env, text=True, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, check=False)
        elapsed = round(time.monotonic() - started, 3)
        output = proc.stdout
        commands.append({"module": module, "argv": argv, "exit_code": proc.returncode,
                         "seconds": elapsed, "output": output})
        receipt_path.write_text(json.dumps(result, indent=2) + "\n")
        print(f"{module}: exit {proc.returncode}, {elapsed}s", flush=True)
        if proc.returncode or "sorryAx" in output:
            print(output, flush=True)
            return 1
    after = {p.name: digest(p) for p in sorted(source.glob("*.lean"))}
    result["source_sha256_after"] = after
    result["sources_unchanged"] = before == after
    audit = commands[-1]["output"]
    result["audited_public_theorems"] = audit.count("depends on axioms:") + audit.count(
        "does not depend on any axioms")
    axioms = {name.strip() for group in re.findall(
        r"depends on axioms:\s*\[([^\]]*)\]", audit, re.S)
        for name in group.split(",") if name.strip()}
    allowed = {"propext", "Classical.choice", "Quot.sound"}
    expected = (source / "Audit.lean").read_text().count("#print axioms ")
    result["axiom_union"] = sorted(axioms)
    result["axioms_standard_only"] = axioms <= allowed
    result["all_public_theorems_audited"] = result["audited_public_theorems"] == expected
    result["success"] = before == after and axioms <= allowed and result[
        "all_public_theorems_audited"]
    receipt_path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Audited {result['audited_public_theorems']} public theorems; "
          f"sources unchanged: {before == after}", flush=True)
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
