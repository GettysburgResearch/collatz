#!/usr/bin/env python3
"""Fresh pinned Lean replay and exact finite controls; not a proof of Collatz."""
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
ROOT = PACKET.parents[1]
LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
MODULES = {
    "EnvelopeCertificate": ("RestrictedEnvelope", {
        "matched_sum", "shadow_tail", "ordinary_clocks", "small_box",
        "source_bound", "negIter_add", "root_stays",
        "complete_tree_candidate_bound", "center_witnesses", "score_bounded",
        "envelope_strict_increase", "checks",
    }),
    "NonlinearTransport": ("RestrictedEnvelope", {
        "strict_matched_nonlinear_transport",
    }),
    "QuarterShift": ("QuarterShift", {
        "balanced_step", "balanced_path", "odd_run", "even_run", "below_twenty",
    }),
    "FourTritDelay": ("FourTritDelay", {"oddRun", "exactArms"}),
    "OrientedBoundary": ("OrientedBoundary", {
        "childChoice", "zeroTriple", "inverseThird", "forbiddenGap",
    }),
}
CONTROLS = (
    "rank_certificate.py", "transfer_control.py", "tilt_control.py",
    "boundary_control.py",
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
        raise ValueError("unexpected Lean compiler: " + version)
    if mathlib_head != MATHLIB_COMMIT:
        raise ValueError("unexpected Mathlib commit: " + mathlib_head)
    paths = [mathlib / ".lake/build/lib/lean", *sorted(
        (mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))]
    if not paths[0].is_dir():
        raise ValueError("the pinned Mathlib checkout must already be built")
    receipt = {
        "schema": "collatz-high-variance-closure-replay/v1",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "five Lean modules, 24 named axiom audits and four finite controls in two modes; not Collatz",
        "python": sys.version, "compiler": str(compiler), "lean_version": version,
        "lean_commit": LEAN_COMMIT, "mathlib_commit": mathlib_head,
        "lean": [], "finite_controls": [], "success": False,
    }
    with tempfile.TemporaryDirectory(prefix="collatz-high-variance-") as temporary:
        temporary = Path(temporary)
        for module, (namespace, expected) in MODULES.items():
            original = PACKET / "lean" / (module + ".lean")
            build = temporary / module
            build.mkdir()
            copied = build / original.name
            shutil.copyfile(original, copied)
            argv = [str(compiler), "-j1", "-DwarningAsError=true", "-o",
                    module + ".olean", copied.name]
            env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, [build, *paths])))
            result = subprocess.run(argv, cwd=build, env=env, capture_output=True,
                                    text=True, timeout=240)
            audits = {}
            for name, axioms in re.findall(
                    r"'([^']+)' (?:depends on axioms: \[([^]]*)\]|"
                    r"does not depend on any axioms)", result.stdout):
                if name in audits:
                    raise ValueError("duplicate axiom audit: " + name)
                audits[name] = sorted(x.strip() for x in axioms.split(",") if x.strip())
            expected_full = {namespace + "." + name for name in expected}
            unexpected = sorted({a for row in audits.values() for a in row} - STANDARD_AXIOMS)
            compiled = build / (module + ".olean")
            success = (result.returncode == 0 and set(audits) == expected_full
                       and not unexpected and compiled.exists())
            receipt["lean"].append({
                "source": str(original.relative_to(ROOT)),
                "source_sha256": digest(original.read_bytes()),
                "fresh_empty_build_directory": True,
                "argv": argv, "exit_code": result.returncode,
                "stdout": result.stdout, "stderr": result.stderr,
                "audits": audits, "unexpected_axioms": unexpected,
                "missing_audits": sorted(expected_full - audits.keys()),
                "extra_audits": sorted(audits.keys() - expected_full),
                "olean_sha256": digest(compiled.read_bytes()) if compiled.exists() else None,
                "success": success,
            })
            print(("PASS" if success else "FAIL"), module, len(audits), "axiom audits", flush=True)
            if not success:
                print(result.stdout, end="", flush=True)
                print(result.stderr, end="", flush=True)

        for name in CONTROLS:
            original = PACKET / "checks" / name
            reference_output = None
            for optimized in (False, True):
                argv = [sys.executable, "-X", "utf8", "-B"]
                if optimized:
                    argv.append("-O")
                argv.append(str(original))
                result = subprocess.run(argv, cwd=temporary, capture_output=True,
                                        text=True, timeout=90)
                if reference_output is None:
                    reference_output = result.stdout
                success = result.returncode == 0 and result.stdout == reference_output
                receipt["finite_controls"].append({
                    "source": str(original.relative_to(ROOT)),
                    "source_sha256": digest(original.read_bytes()),
                    "optimized": optimized, "argv": argv,
                    "exit_code": result.returncode, "stdout": result.stdout,
                    "stderr": result.stderr, "same_stdout_across_modes": result.stdout == reference_output,
                    "success": success,
                })
                print(("PASS" if success else "FAIL"), name,
                      "optimized" if optimized else "normal", flush=True)
                print(result.stdout, end="", flush=True)
                if result.stderr:
                    print(result.stderr, end="", flush=True)

    receipt["success"] = all(row["success"] for row in receipt["lean"] + receipt["finite_controls"])
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS" if receipt["success"] else "FAIL", "scoped replay; not a proof of Collatz")
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
