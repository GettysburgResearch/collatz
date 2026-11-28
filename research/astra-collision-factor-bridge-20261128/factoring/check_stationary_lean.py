#!/usr/bin/env python3
"""Freshly compile the integer-window bridge and audit its three roots.

Supply Lean 4.34.1. Both project modules are compiled into a new temporary
directory and import only Lean core Omega. No Mathlib objects are required.
This is not a rebuild of the Lean standard library or a LeanChecker run.
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

ROOT = Path(__file__).resolve().parents[3]
PACKET = Path("research/astra-collision-factor-bridge-20261128/factoring")
MODULES = [
    ("StationaryWindow", PACKET / "StationaryWindow.lean"),
    ("StationaryWindowAudit", PACKET / "StationaryWindowAudit.lean"),
]
PUBLIC_ROOTS = [
    "Collatz.StationaryWindow.window_add",
    "Collatz.StationaryWindow.window_le",
    "Collatz.StationaryWindow.window_shift_bound",
]

ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--temporary-root", type=Path)
    args = parser.parse_args()
    lean = args.lean.resolve()

    def run(command: list[str], env: dict[str, str] | None = None):
        return subprocess.run(command, cwd=ROOT, env=env, text=True,
                              capture_output=True, timeout=900)

    version = run([str(lean), "--version"])
    if version.returncode or "version 4.34.1," not in version.stdout:
        raise SystemExit("Expected Lean 4.34.1")
    receipt = args.receipt.resolve()
    receipt.parent.mkdir(parents=True, exist_ok=True)
    logs = receipt.parent / (receipt.stem + "-logs")
    logs.mkdir(exist_ok=True)
    result = {
        "schema": "collatz-stationary-window-lean/v1",
        "success": False,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "compiler": version.stdout.strip(),
        "scope": "Fresh complete two-module project closure and separate import/type/axiom audit. Only Lean core Omega is imported; no Mathlib objects are used. No rebuild of the Lean standard library or independent LeanChecker run. Three finite integer-window roots, with no probability or analytic statement formalized.",
        "public_roots": PUBLIC_ROOTS,
        "steps": [],
    }
    began = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="collatz-stationary-window-lean-",
                                    dir=args.temporary_root) as directory:
        objects = Path(directory)
        env = os.environ.copy()
        env["LEAN_PATH"] = str(objects)
        for name, relative in MODULES:
            source = ROOT / relative
            before = source.read_bytes()
            command = [str(lean), "-j1", "-DautoImplicit=false",
                       "-DwarningAsError=true", "-o",
                       str(objects / (name + ".olean")), str(source)]
            started = time.monotonic()
            checked = run(command, env)
            stdout, stderr = checked.stdout.encode(), checked.stderr.encode()
            (logs / (name + ".stdout.log")).write_bytes(stdout)
            (logs / (name + ".stderr.log")).write_bytes(stderr)
            unchanged = source.read_bytes() == before
            result["steps"].append({
                "module": name,
                "source": relative.as_posix(),
                "source_sha256": sha256(before),
                "command": command,
                "exit_code": checked.returncode,
                "elapsed_seconds": round(time.monotonic() - started, 4),
                "source_unchanged": unchanged,
                "stdout_sha256": sha256(stdout),
                "stderr_sha256": sha256(stderr),
            })
            receipt.write_text(json.dumps(result, indent=2) + "\n")
            if checked.returncode or not unchanged:
                print(checked.stdout + checked.stderr)
                raise SystemExit("Compilation failed or source changed: " + name)
            if name == "StationaryWindowAudit":
                rows = re.findall(
                    r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]",
                    checked.stdout,
                )
                no_axioms = re.findall(r"'([^']+)' does not depend on any axioms", checked.stdout)
                seen_roots = [root for root, _ in rows] + no_axioms
                seen_axioms = {
                    axiom.strip() for _, axioms in rows
                    for axiom in axioms.split(",") if axiom.strip()
                }
                if sorted(seen_roots) != sorted(PUBLIC_ROOTS):
                    raise SystemExit("Axiom audit omitted or duplicated a public root")
                if seen_axioms - ALLOWED_AXIOMS:
                    raise SystemExit("Unexpected axioms: " + str(seen_axioms))
                result["axiom_audit"] = {
                    "roots": seen_roots, "axioms": sorted(seen_axioms),
                }
    result.update({
        "success": True,
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": round(time.monotonic() - began, 4),
    })
    receipt.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"success": True, "public_roots": len(PUBLIC_ROOTS),
                      "axioms": result["axiom_audit"]["axioms"]}))


if __name__ == "__main__":
    main()
