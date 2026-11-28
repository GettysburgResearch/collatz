#!/usr/bin/env python3
"""Freshly build the actual single-edge maps and audit every public root.

The actual shortcut is stated locally, with only function-iteration and core
Omega imports. Pinned compiled Mathlib and third-party dependencies are reused;
this is not a cold build or an independent LeanChecker replay. Historical
successful receipts are separate.
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
ROOTS = [
    "splitAt_unchanged", "splitAt_even", "iterate_eq_before_hit",
    "splitAt_hit_iff", "splitAt_two_cycle", "splitAt_scaled_cycle",
    "five_genuine_tail", "five_modified_return", "five_eventual_rescaling",
    "finite_table_preserved", "unitFive_unchanged", "unitFive_unit_change",
    "unitFive_period", "unitFive_least_period", "unitFive_hit_iff",
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
    base = Path(__file__).resolve().parent
    sources = {"SingleEdgeSplit": base / "SingleEdgeSplit.lean"}
    receipt = args.receipt.resolve()
    receipt.parent.mkdir(parents=True, exist_ok=True)
    logs = receipt.parent / (receipt.stem + "-logs")
    logs.mkdir(exist_ok=True)

    def run(command: list[str], env=None):
        return subprocess.run(command, env=env, text=True, capture_output=True, timeout=600)

    version = run([str(lean), "--version"])
    pin = run(["git", "-C", str(mathlib), "rev-parse", "HEAD"])
    if version.returncode or "version 4.34.1," not in version.stdout:
        raise SystemExit("Lean 4.34.1 is required")
    if pin.returncode or pin.stdout.strip() != PIN:
        raise SystemExit("Wrong Mathlib source pin")
    before = {name: source.read_bytes() for name, source in sources.items()}
    names = re.findall(r"^theorem\s+([A-Za-z_][A-Za-z0-9_]*)",
                       before["SingleEdgeSplit"].decode(), re.MULTILINE)
    if names != ROOTS:
        raise SystemExit("Public theorem inventory changed")
    cache = mathlib / ".lake/build/lib/lean"
    if not cache.is_dir():
        raise SystemExit("The pinned compiled dependency cache is missing")
    packages = sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
    qualified = ["Collatz.SingleEdgeSplit." + root for root in ROOTS]
    result = {
        "schema": "collatz-single-edge-lean/v1", "success": False,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "compiler": version.stdout.strip(), "mathlib_source_commit": PIN,
        "dependency_manifest_sha256": sha((mathlib / "lake-manifest.json").read_bytes()),
        "source_sha256": {name: sha(data) for name, data in before.items()},
        "runner_sha256": sha(Path(__file__).read_bytes()),
        "public_roots": qualified,
        "scope": "Fifteen finite roots: unchanged branches, exact even halving, generic preservation of prefixes and first-hit sets, the q-to-2q cycle and phase scaling, genuine and modified five tails, eventual rescaling after actual first hit, any prescribed finite branch table, and the single-unit five-to-nine edit with least period ten. Infinite-density, Brownian, minimum-clock and limiting-collision claims remain written and source-qualified. Cached pinned dependencies reused; no cold rebuild or independent LeanChecker run.",
        "steps": [],
    }
    with tempfile.TemporaryDirectory(prefix="collatz-single-edge-") as tmp:
        obj = Path(tmp)
        env = os.environ.copy()
        env["LEAN_PATH"] = os.pathsep.join(map(str, [obj, cache, *packages]))
        common = [str(lean), "-j1", "-DautoImplicit=false", "-DwarningAsError=true"]
        audit_text = "\n".join([
            "import SingleEdgeSplit", "",
            *("#check " + root for root in qualified),
            *("#print axioms " + root for root in qualified), "",
        ])
        audit = obj / "Audit.lean"
        audit.write_text(audit_text)
        (logs / "Audit.lean").write_text(audit_text)
        commands = [
            *((name, common + ["-o", str(obj / (name + ".olean")), str(source)])
              for name, source in sources.items()),
            ("Audit", common + [str(audit)]),
        ]
        for label, command in commands:
            began = time.monotonic()
            print("Compiling " + label, flush=True)
            try:
                proc = run(command, env)
            except subprocess.TimeoutExpired as exc:
                result["steps"].append({"name": label, "timeout_seconds": 600})
                receipt.write_text(json.dumps(result, indent=2) + "\n")
                raise SystemExit("Compiler timeout; no mathematical failure inferred") from exc
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
        unchanged = all(source.read_bytes() == before[name] for name, source in sources.items())
        success = count == len(ROOTS) and not (seen - ALLOWED) and unchanged
        result.update({
            "success": success, "source_unchanged": unchanged,
            "audited_roots": count, "axioms": sorted(seen),
            "finished_utc": datetime.now(timezone.utc).isoformat(),
        })
        receipt.write_text(json.dumps(result, indent=2) + "\n")
        if not success:
            raise SystemExit("The source stability or complete root audit failed")
    print(json.dumps({"success": True, "roots": count, "axioms": sorted(seen)}))


if __name__ == "__main__":
    main()
