#!/usr/bin/env python3
"""Fresh, pinned replay of the exact finite diagnostics, not of Collatz."""
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
import tempfile


ROOT = Path(__file__).resolve().parents[3]
SOURCE = "research/central-closure-20261124/lean/ClosureDiagnostics.lean"
LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
EXPECTED = {
    "inverse_difference", "fixed_type_debit", "refill_family",
    "refill_run_parities", "source_reservoir_five",
    "destination_reservoir_factor", "increasing_refill", "concrete_refill",
    "positive_weights_increase", "restricted_tree_transfer_counterexample",
}
STANDARD = {"propext", "Classical.choice", "Quot.sound"}


def sha256(data: bytes) -> str:
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
        raise ValueError("unexpected Lean version: " + version)
    if mathlib_head != MATHLIB_COMMIT:
        raise ValueError("unexpected Mathlib commit: " + mathlib_head)
    paths = [mathlib / ".lake/build/lib/lean", *sorted(
        (mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))]
    if not paths[0].is_dir():
        raise ValueError("Mathlib must already be built")
    original = ROOT / SOURCE
    receipt = {
        "schema": "collatz-central-closure-replay/v1",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "one finite Lean source, ten named declaration audits; not Collatz",
        "source": SOURCE, "source_sha256": sha256(original.read_bytes()),
        "compiler": str(compiler), "lean_version": version,
        "lean_commit": LEAN_COMMIT, "mathlib_commit": mathlib_head,
        "success": False,
    }
    with tempfile.TemporaryDirectory(prefix="collatz-central-closure-") as temporary:
        build = Path(temporary)
        source = build / original.name
        shutil.copyfile(original, source)
        argv = [str(compiler), "-j1", "-DwarningAsError=true", "-o",
                source.with_suffix(".olean").name, source.name]
        env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, [build, *paths])))
        result = subprocess.run(argv, cwd=build, env=env, capture_output=True,
                                text=True, timeout=300)
        audits = {}
        for name, axioms in re.findall(
                r"'CentralClosure\.([^']+)' (?:depends on axioms: \[([^]]*)\]|"
                r"does not depend on any axioms)", result.stdout):
            if name in audits:
                raise ValueError("duplicate audit: " + name)
            audits[name] = sorted(x.strip() for x in axioms.split(",") if x.strip())
        unexpected = sorted({a for ax in audits.values() for a in ax} - STANDARD)
        compiled = source.with_suffix(".olean")
        receipt.update(argv=argv, exit_code=result.returncode,
                       stdout=result.stdout, stderr=result.stderr,
                       audits=audits, unexpected_axioms=unexpected,
                       missing_audits=sorted(EXPECTED - audits.keys()),
                       extra_audits=sorted(audits.keys() - EXPECTED),
                       olean_sha256=sha256(compiled.read_bytes()) if compiled.exists() else None)
        receipt["success"] = (result.returncode == 0 and set(audits) == EXPECTED
                              and not unexpected and compiled.exists())
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    print(result.stdout, end="")
    print(result.stderr, end="")
    print("PASS" if receipt["success"] else "FAIL", "finite Lean diagnostics")
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
