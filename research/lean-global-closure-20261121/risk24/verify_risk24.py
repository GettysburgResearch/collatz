#!/usr/bin/env python3
"""Compile only the two new Lean cores and audit all their public theorems.

The 2-adic identification and infinite mathematical proofs remain written
arguments. This driver copies unchanged sources to a temporary directory,
appends only axiom queries, and writes its receipt outside the checkout.
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

FILES = ("TriadicDual.lean", "SiblingSourceSeparation.lean")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(argv: list[str], cwd: Path) -> dict:
    proc = subprocess.run(argv, cwd=cwd, text=True, encoding="utf-8",
                          capture_output=True, timeout=120,
                          env=dict(os.environ, PYTHONUTF8="1"))
    return {"argv": argv, "exit_code": proc.returncode,
            "stdout": proc.stdout, "stderr": proc.stderr}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    lean, receipt = args.lean.resolve(), args.receipt.resolve()
    checkout = folder.parents[2]
    if receipt.is_relative_to(checkout):
        parser.error("the receipt must be outside the source checkout")
    result = {
        "schema": "collatz-risk24-formal-evidence/v1",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "two new Lean core/Std modules; no universal witness construction or infinite analytic formalization",
        "source_sha256": {name: digest(folder / name) for name in FILES},
        "driver_sha256": digest(Path(__file__).resolve()),
        "lean_binary_sha256": digest(lean),
        "commands": [],
    }
    with tempfile.TemporaryDirectory(prefix="collatz-risk24-") as temporary:
        work = Path(temporary)
        result["version"] = run([str(lean), "--version"], work)
        for filename in FILES:
            source = (folder / filename).read_text(encoding="utf-8")
            namespace = re.search(r"(?m)^namespace\s+([\w.]+)", source)
            names = re.findall(r"(?m)^theorem\s+(\w+)", source)
            if namespace is None or not names:
                raise RuntimeError(f"missing namespace or public theorems: {filename}")
            full_names = [f"{namespace.group(1)}.{name}" for name in names]
            definitions = ([f"{namespace.group(1)}.stopClock"]
                           if filename == "TriadicDual.lean" else [])
            expected = full_names + definitions
            queries = "\n".join(f"#print axioms {name}" for name in expected)
            (work / filename).write_text(
                source + "\n-- Complete public theorem and clock audit\n" + queries + "\n",
                encoding="utf-8")
            row = run([str(lean), filename], work)
            row.update(source=filename, theorems_audited=full_names,
                       definitions_audited=definitions)
            audits = [line for line in row["stdout"].splitlines()
                      if "depends on axioms:" in line
                      or "does not depend on any axioms" in line]
            bad: set[str] = set()
            allowed = {"propext", "Classical.choice", "Quot.sound"}
            for line in audits:
                found = re.search(r"depends on axioms:\s*\[(.*?)\]", line)
                if found:
                    bad.update(a.strip() for a in found.group(1).split(",")
                               if a.strip() and a.strip() not in allowed)
            row["unexpected_axioms"] = sorted(bad)
            row["audit_complete"] = all(
                any(f"'{name}'" in line for line in audits) for name in expected)
            result["commands"].append(row)
    result["success"] = (
        result["version"]["exit_code"] == 0
        and "4.34.1" in result["version"]["stdout"]
        and all(row["exit_code"] == 0 and row["audit_complete"]
                and not row["unexpected_axioms"] for row in result["commands"]))
    result["finished_utc"] = datetime.now(timezone.utc).isoformat()
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": result["success"],
        "commands": [{"source": row["source"], "exit_code": row["exit_code"],
                      "public_theorems": len(row["theorems_audited"]),
                      "audit_complete": row["audit_complete"]}
                     for row in result["commands"]],
        "receipt": str(receipt), "receipt_sha256": digest(receipt)}, indent=2))
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
