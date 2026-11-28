#!/usr/bin/env python3
"""Freshly compile the actual inverse-climb arithmetic and audit its roots.

The build pattern follows the preceding packet's check_lean.py. Pinned
compiled Mathlib and third-party dependencies are reused; this is not a
cold dependency build or an independent LeanChecker replay.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time


PIN = "d13f23b723b8a846827a245b89c10fc7d3f11612"
NAMESPACE = "Collatz.InverseClimb"
ROOTS = [
    "residue_exponent_table",
    "block_from_parameter",
    "exists_doubling_block",
]
ALLOWED = {"Classical.choice", "Quot.sound", "propext"}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--lean", type=Path, required=True)
    ap.add_argument("--mathlib", type=Path, required=True)
    ap.add_argument("--receipt", type=Path, required=True)
    args = ap.parse_args()
    lean, mathlib = args.lean.resolve(), args.mathlib.resolve()
    source = Path(__file__).resolve().with_name("InverseClimb.lean")
    receipt = args.receipt.resolve()
    receipt.parent.mkdir(parents=True, exist_ok=True)
    logs = receipt.parent / (receipt.stem + "-logs")
    logs.mkdir(exist_ok=True)

    def run(command: list[str], env=None):
        return subprocess.run(command, env=env, text=True,
                              capture_output=True, timeout=600)

    version = run([str(lean), "--version"])
    pin = run(["git", "-C", str(mathlib), "rev-parse", "HEAD"])
    if version.returncode or "version 4.34.1," not in version.stdout:
        raise SystemExit("Lean 4.34.1 is required")
    if pin.returncode or pin.stdout.strip() != PIN:
        raise SystemExit("Wrong Mathlib source pin")
    before = source.read_bytes()
    names = re.findall(r"^theorem\s+([A-Za-z_][A-Za-z0-9_]*)",
                       before.decode(), re.MULTILINE)
    if names != ROOTS:
        raise SystemExit("Public theorem inventory changed")
    cache = mathlib / ".lake/build/lib/lean"
    if not cache.is_dir():
        raise SystemExit("The pinned compiled dependency cache is missing")
    packages = sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
    qualified = [NAMESPACE + "." + root for root in ROOTS]
    result = {
        "schema": "collatz-inverse-climb-lean/v1",
        "success": False,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "compiler": version.stdout.strip(),
        "mathlib_source_commit": PIN,
        "dependency_manifest_sha256": sha((mathlib / "lake-manifest.json").read_bytes()),
        "source_sha256": sha(before),
        "runner_sha256": sha(Path(__file__).read_bytes()),
        "public_roots": qualified,
        "scope": "Three finite actual-integer inverse-block roots. The harmonic atom, cocycle infinite product, summable gains and canonical-selection obstruction remain written. The residue table uses explicit witnesses and kernel-checked norm_num, not native_decide. Cached pinned dependencies reused; no cold rebuild or independent LeanChecker run.",
        "steps": [],
    }
    with tempfile.TemporaryDirectory(prefix="collatz-inverse-climb-") as tmp:
        obj = Path(tmp)
        env = os.environ.copy()
        env["LEAN_PATH"] = os.pathsep.join(map(str, [obj, cache, *packages]))
        common = [str(lean), "-j1", "-DautoImplicit=false", "-DwarningAsError=true"]
        audit_text = "\n".join([
            "import InverseClimb", "",
            *("#check " + root for root in qualified),
            *("#print axioms " + root for root in qualified), "",
        ])
        audit = obj / "Audit.lean"
        audit.write_text(audit_text)
        (logs / "Audit.lean").write_text(audit_text)
        commands = [
            ("InverseClimb", common + ["-o", str(obj / "InverseClimb.olean"), str(source)]),
            ("Audit", common + [str(audit)]),
        ]
        for label, command in commands:
            began = time.monotonic()
            proc = run(command, env)
            (logs / (label + ".stdout.log")).write_text(proc.stdout)
            (logs / (label + ".stderr.log")).write_text(proc.stderr)
            result["steps"].append({
                "name": label, "exit_code": proc.returncode,
                "elapsed_seconds": round(time.monotonic() - began, 3),
                "stdout_sha256": sha(proc.stdout.encode()),
                "stderr_sha256": sha(proc.stderr.encode()),
            })
            receipt.write_text(json.dumps(result, indent=2) + "\n")
            if proc.returncode:
                print(proc.stdout + proc.stderr)
                raise SystemExit(1)
        rows = re.findall(r"depends on axioms:\s*\[([^\]]*)\]", proc.stdout)
        seen = {a.strip() for row in rows for a in row.split(",") if a.strip()}
        count = len(rows) + proc.stdout.count("does not depend on any axioms")
        unchanged = source.read_bytes() == before
        success = count == len(ROOTS) and not (seen - ALLOWED) and unchanged
        result.update({
            "success": success,
            "source_unchanged": unchanged,
            "audited_roots": count,
            "axioms": sorted(seen),
            "finished_utc": datetime.now(timezone.utc).isoformat(),
        })
        receipt.write_text(json.dumps(result, indent=2) + "\n")
        if not success:
            raise SystemExit("The source stability or complete root audit failed")
    print(json.dumps({"success": True, "roots": count, "axioms": sorted(seen)}))


if __name__ == "__main__":
    main()
