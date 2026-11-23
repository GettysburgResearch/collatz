#!/usr/bin/env python3
"""Compile only this packet's Lean cores and run its exact finite controls.

The infinite-dimensional and measure-theoretic proofs remain written proofs.
This driver never rebuilds the previous project corpus and writes no outputs
into the source checkout. Run without -O so the finite-control assertions run.
"""

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


ROOT = Path(__file__).resolve().parent
LEAN_FILES = ["InverseBranching.lean", "PrimeBalanceObstruction.lean"]
CONTROL_FILES = [
    "check_fourier_interface.py",
    "check_cycle_obstructions.py",
    "check_hardy_flows.py",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str], cwd: Path) -> dict:
    completed = subprocess.run(
        command, cwd=cwd, text=True, encoding="utf-8",
        capture_output=True, timeout=120,
        env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1"),
    )
    return {"argv": command, "exit_code": completed.returncode,
            "stdout": completed.stdout, "stderr": completed.stderr}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    if not __debug__:
        parser.error("run without Python optimization; the controls use assertions")
    lean = args.lean.resolve()
    receipt = args.receipt.resolve()
    checkout = ROOT.parents[2]
    if receipt.is_relative_to(checkout):
        parser.error("write the receipt outside the source checkout")
    if not lean.is_file():
        parser.error("--lean must name an existing Lean executable")

    result = {
        "schema": "collatz-risk23-local-evidence/v1",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "two new core/Std Lean modules and exact finite controls; not a Collatz proof or an analytic formalization",
        "python": sys.version,
        "lean_binary_sha256": sha256(lean),
        "source_sha256": {n: sha256(ROOT / n) for n in LEAN_FILES + CONTROL_FILES},
        "commands": [],
        "success": False,
    }
    with tempfile.TemporaryDirectory(prefix="collatz-risk23-") as temporary:
        work = Path(temporary)
        version = run([str(lean), "--version"], work)
        result["lean_version"] = version
        for name in LEAN_FILES:
            source = (ROOT / name).read_text(encoding="utf-8")
            namespace = re.search(r"(?m)^namespace\s+([\w.]+)", source)
            if namespace is None:
                raise ValueError(f"missing namespace in {name}")
            names = re.findall(r"(?m)^theorem\s+(\w+)", source)
            if not names:
                raise ValueError(f"no public theorems in {name}")
            audit = "\n".join(f"#print axioms {namespace.group(1)}.{n}" for n in names)
            target = work / name
            target.write_text(source + "\n-- Complete public theorem audit\n" + audit + "\n", encoding="utf-8")
            row = run([str(lean), name], work)
            row["source"] = name
            row["public_theorems_audited"] = names
            audit_lines = [line for line in row["stdout"].splitlines()
                           if "depends on axioms:" in line or "does not depend on any axioms" in line]
            row["axiom_audit_lines"] = audit_lines
            allowed = {"propext", "Classical.choice", "Quot.sound"}
            bad_axioms = set()
            for line in audit_lines:
                match = re.search(r"depends on axioms:\s*\[(.*?)\]", line)
                if match:
                    bad_axioms.update(a.strip() for a in match.group(1).split(",")
                                      if a.strip() and a.strip() not in allowed)
            row["unexpected_axioms"] = sorted(bad_axioms)
            row["audit_complete"] = all(any(
                f"'{namespace.group(1)}.{n}'" in line for line in audit_lines)
                for n in names)
            result["commands"].append(row)
        for name in CONTROL_FILES:
            shutil.copyfile(ROOT / name, work / name)
            row = run([sys.executable, "-X", "utf8", "-B", name], work)
            row["source"] = name
            if row["exit_code"] == 0:
                row["finite_control_result"] = json.loads(row["stdout"])
            result["commands"].append(row)

    result["success"] = version["exit_code"] == 0 and all(
        row["exit_code"] == 0 and not row.get("unexpected_axioms")
        and row.get("audit_complete", True)
        for row in result["commands"]
    )
    result["finished_utc"] = datetime.now(timezone.utc).isoformat()
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": result["success"],
        "commands": [{"source": row["source"], "exit_code": row["exit_code"],
                      "audit_complete": row.get("audit_complete")}
                     for row in result["commands"]],
        "receipt": str(receipt), "receipt_sha256": sha256(receipt),
    }, indent=2))
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
