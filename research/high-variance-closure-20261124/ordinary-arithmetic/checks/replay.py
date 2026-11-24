#!/usr/bin/env python3
"""Fresh replay of the ordinary companion, ancestor toll and pair-merger kernels."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


PACKET = Path(__file__).resolve().parents[1]
ROOT = PACKET.parents[2]
LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
QUARTER_SHA256 = "9799954b9bc35e270d72399f319c40004f272169c17285ff8fe296657db7a272"
STANDARD = {"propext", "Classical.choice", "Quot.sound"}
BIASED_SHA256 = "f9be262b47615a2c19e1070b9efc38f948aa8573c75e751869c3a92ecdd64be2"
MODULES = (
    (PACKET.parent / "lean/QuarterShift.lean", "QuarterShift", {
        "balanced_step", "balanced_path", "odd_run", "even_run", "below_twenty",
    }, False),
    (PACKET.parent / "continuation/lean/BiasedParity.lean", "BiasedParity", {
        "highPrefix", "geometricTerm", "summableOfHits", "boundedIffHits", "summableIffHits",
    }, False),
    (PACKET / "lean/DyadicCompanion.lean", "DyadicCompanion", {
        "heightDrop", "visitsSmall", "smallFails", "integralCompanionImpossible",
    }, True),
    (PACKET / "lean/ResetAncestor.lean", "ResetAncestor", {
        "uniqueParent", "equalToll", "delayedMerge", "nonperiodicBranch",
    }, True),
    (PACKET / "lean/PeriodicBoundary.lean", "PeriodicBoundary", {
        "everyStateMerges", "liftedWalk", "alignedNumerators",
    }, True),
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    compiler, mathlib = args.lean.resolve(), args.mathlib.resolve()
    version = subprocess.check_output([str(compiler), "--version"], text=True).strip()
    mathlib_head = subprocess.check_output(
        ["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip()
    if "4.34.1" not in version or LEAN_COMMIT[:12] not in version:
        raise ValueError("unexpected compiler: " + version)
    if mathlib_head != MATHLIB_COMMIT:
        raise ValueError("unexpected Mathlib checkout: " + mathlib_head)
    if digest(MODULES[0][0].read_bytes()) != QUARTER_SHA256:
        raise ValueError("the pinned QuarterShift dependency changed")
    if digest(MODULES[1][0].read_bytes()) != BIASED_SHA256:
        raise ValueError("the pinned BiasedParity dependency changed")
    paths = [mathlib / ".lake/build/lib/lean", *sorted(
        (mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))]
    if not paths[0].is_dir():
        raise ValueError("Mathlib must already be built")
    receipt = {
        "schema": "collatz-ordinary-arithmetic-replay/v1",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "eleven new public declaration audits plus ten pinned dependency audits; four finite controls in two modes; no all-source arithmetic membership proof",
        "python": sys.version, "compiler": str(compiler), "lean_version": version,
        "lean_commit": LEAN_COMMIT, "mathlib_commit": mathlib_head,
        "lean": [], "finite_controls": [], "success": False,
    }
    with tempfile.TemporaryDirectory(prefix="collatz-ordinary-arithmetic-") as temporary:
        build = Path(temporary)
        env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, [build, *paths])))
        for original, namespace, names, is_new in MODULES:
            source = build / original.name
            shutil.copyfile(original, source)
            argv = [str(compiler), "-j1", "-DwarningAsError=true", "-DautoImplicit=false", "-o",
                    source.with_suffix(".olean").name, source.name]
            result = subprocess.run(argv, cwd=build, env=env, capture_output=True,
                                    text=True, timeout=240)
            audits = {}
            for name, axioms in re.findall(
                    r"'([^']+)' (?:depends on axioms: \[([^]]*)\]|"
                    r"does not depend on any axioms)", result.stdout):
                if name in audits:
                    raise ValueError("duplicate audit: " + name)
                audits[name] = sorted(x.strip() for x in axioms.split(",") if x.strip())
            expected = {namespace + "." + name for name in names}
            unexpected = sorted({a for row in audits.values() for a in row} - STANDARD)
            compiled = source.with_suffix(".olean")
            success = result.returncode == 0 and set(audits) == expected and not unexpected and compiled.exists()
            receipt["lean"].append({
                "source": str(original.relative_to(ROOT)), "source_sha256": digest(original.read_bytes()),
                "new_in_this_checkpoint": is_new, "fresh_dependency_order": True,
                "argv": argv, "exit_code": result.returncode,
                "stdout": result.stdout, "stderr": result.stderr, "audits": audits,
                "unexpected_axioms": unexpected, "missing_audits": sorted(expected-audits.keys()),
                "extra_audits": sorted(audits.keys()-expected),
                "olean_sha256": digest(compiled.read_bytes()) if compiled.exists() else None,
                "success": success,
            })
            print("PASS" if success else "FAIL", namespace, len(audits), "axiom audits", flush=True)
            if not success:
                print(result.stdout, end="", flush=True)
                print(result.stderr, end="", flush=True)

        for name in ("companion_checks.py", "reset_exit_control.py", "boundary_recurrence_control.py", "negative_kernel_control.py"):
            original = PACKET / "checks" / name
            reference = None
            for optimized in (False, True):
                argv = [sys.executable, "-X", "utf8", "-B"]
                if optimized:
                    argv.append("-O")
                argv.append(str(original))
                result = subprocess.run(argv, cwd=build, capture_output=True,
                                        text=True, timeout=90)
                if reference is None:
                    reference = result.stdout
                success = result.returncode == 0 and result.stdout == reference
                receipt["finite_controls"].append({
                    "source": str(original.relative_to(ROOT)), "source_sha256": digest(original.read_bytes()),
                    "argv": argv, "optimized": optimized, "exit_code": result.returncode,
                    "stdout": result.stdout, "stderr": result.stderr,
                    "same_stdout_across_modes": result.stdout == reference, "success": success,
                })
                print("PASS" if success else "FAIL", name, "optimized" if optimized else "normal", flush=True)
                print(result.stdout, end="", flush=True)
                if result.stderr:
                    print(result.stderr, end="", flush=True)

    receipt["success"] = all(row["success"] for row in receipt["lean"] + receipt["finite_controls"])
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS" if receipt["success"] else "FAIL", "ordinary arithmetic and merger kernels; Collatz remains open")
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
