#!/usr/bin/env python3
"""Strict, source-bound replay of the eight inherited finite Lean kernels.

Usage: python replay.py --lean /path/to/lean --mathlib /path/to/mathlib \
         --output /path/to/reports

Requires the Lean/Mathlib revisions recorded below and built Mathlib/package
oleans. This checks the finite declarations, not the surrounding analytic prose.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time

LEAN_VERSION = "4.34.1"
MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
EXPECTED_COUNTS = {
    "CarryBudget.lean": 6, "CarryCocycle.lean": 4, "MahlerCore.lean": 8,
    "PhasePacking.lean": 8, "RepeatObstruction.lean": 6,
    "RepetitionWindow.lean": 11, "ResidueDefect.lean": 6,
    "TwoSidedPacking.lean": 13,
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    lean, mathlib, output = (p.resolve() for p in
                             (args.lean, args.mathlib, args.output))
    output.mkdir(parents=True, exist_ok=True)
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    commit = subprocess.check_output(
        ["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip()
    if not re.search(r"\b" + re.escape(LEAN_VERSION) + r"\b", version):
        raise RuntimeError(f"Unexpected Lean version: {version}")
    if commit != MATHLIB_COMMIT:
        raise RuntimeError(f"Unexpected Mathlib revision: {commit}")
    libraries = [mathlib / ".lake/build/lib/lean"]
    libraries.extend(sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean")))
    env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, libraries)))
    receipt = {"scope": "eight inherited finite kernels; no global Collatz proof",
               "lean_version": version, "mathlib_commit": commit,
               "allowed_axioms": sorted(ALLOWED_AXIOMS),
               "replay_script_sha256": digest(Path(__file__)),
               "expected_files": EXPECTED_COUNTS, "files": [],
               "completed": False, "all_passed": False}
    success = True
    sources = sorted(Path(__file__).resolve().parent.glob("*.lean"))
    if {p.name for p in sources} != set(EXPECTED_COUNTS):
        raise RuntimeError("The expected eight source files are not all present")
    for source in sources:
        before = digest(source)
        source_text = source.read_text()
        namespace = re.findall(r"^namespace (\S+)", source_text, re.M)
        if len(namespace) != 1:
            raise RuntimeError(f"Expected one namespace in {source}")
        expected = {namespace[0] + "." + n for n in
                    re.findall(r"^theorem\s+(\S+)", source_text, re.M)}
        if len(expected) != EXPECTED_COUNTS[source.name]:
            raise RuntimeError(f"Unexpected public declaration count in {source}")
        command = [str(lean), "-j1", "-DwarningAsError=true", str(source)]
        started = time.monotonic()
        result = subprocess.run(command, env=env, text=True, stdin=subprocess.DEVNULL,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                timeout=1800, check=False)
        elapsed = time.monotonic() - started
        log = output / (source.stem + ".final.log")
        log.write_text(result.stdout)
        audits = {}
        for name, axiom_text in re.findall(
                r"'([^']+)' depends on axioms: \[([^\]]*)\]", result.stdout):
            audits[name] = [s.strip() for s in axiom_text.split(",") if s.strip()]
        for name in re.findall(r"'([^']+)' does not depend on any axioms", result.stdout):
            audits[name] = []
        unexpected_axioms = sorted({a for values in audits.values() for a in values}
                                  - ALLOWED_AXIOMS)
        after = digest(source)
        passed = (result.returncode == 0 and before == after
                  and set(audits) == expected and not unexpected_axioms
                  and "sorryAx" not in result.stdout)
        success = success and passed
        entry = {"file": source.name, "sha256": before,
                 "source_unchanged": before == after, "command": command,
                 "exit_code": result.returncode, "seconds": round(elapsed, 3),
                 "expected_public_theorems": len(expected),
                 "axiom_audits": audits, "unexpected_axioms": unexpected_axioms,
                 "log": log.name, "log_sha256": digest(log), "passed": passed}
        receipt["files"].append(entry)
        receipt["completed"] = len(receipt["files"]) == len(EXPECTED_COUNTS)
        receipt["all_passed"] = success and receipt["completed"]
        (output / "final-replay.json").write_text(json.dumps(receipt, indent=2) + "\n")
        print(f"{source.name}: exit={result.returncode}, "
              f"audits={len(audits)}/{len(expected)}, passed={passed}, "
              f"seconds={elapsed:.3f}", flush=True)
        if not passed:
            print(result.stdout, flush=True)
    print(f"All eight kernels passed: {success}", flush=True)
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
