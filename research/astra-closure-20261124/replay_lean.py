#!/usr/bin/env python3
"""Build the pinned local Lean module graph in a new isolated directory."""
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


ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "research/astra-closure-20261124"
OLD = ROOT / "research/scalar-carry-cocycle-20261124"
COMPILER = "5045d0056413266e57c625dcd7c365b10e377c52"
MATHLIB = "d13f23b723b8a846827a245b89c10fc7d3f11612"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
SOURCES = [
    PACKET / "dependencies/ActualScalar.lean",
    PACKET / "StrictCarry.lean",
    PACKET / "ActualCarry.lean",
    PACKET / "DebitCarry.lean",
    PACKET / "ActualPrefix.lean",
    OLD / "CarryCocycle.lean",
    OLD / "ResidueDefect.lean",
    PACKET / "CanonicalWindows.lean",
    PACKET / "ActualCanonicalWindows.lean",
    PACKET / "CycleDefectFilters.lean",
    PACKET / "NormCertificate.lean",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--lean-path-file", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    lean = args.lean.resolve()
    out = args.output.resolve()
    if out.is_relative_to(ROOT):
        parser.error("--output must be outside the repository")
    if out.exists() and any(out.iterdir()):
        parser.error("--output must be new or empty")
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if "4.34.1" not in version or COMPILER not in version:
        parser.error("Lean version/commit does not match the recorded checkpoint")
    mathlib_head = subprocess.check_output(
        ["git", "-C", str(args.mathlib.resolve()), "rev-parse", "HEAD"],
        text=True,
    ).strip()
    if mathlib_head != MATHLIB:
        parser.error("Mathlib commit does not match the recorded checkpoint")
    dep_path = args.lean_path_file.read_text(encoding="utf-8").strip()
    if not dep_path:
        parser.error("the Mathlib dependency search path is empty")
    out.mkdir(parents=True, exist_ok=True)
    for source in SOURCES:
        shutil.copyfile(source, out / source.name)
    env = dict(os.environ, LEAN_PATH=str(out) + os.pathsep + dep_path)
    receipt = {
        "schema": "collatz-astra-lean-replay/v1",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "lean_version_output": version,
        "mathlib_commit": mathlib_head,
        "builds": [],
        "success": False,
    }
    receipt_path = out / "LEAN_REPLAY.json"
    for source in SOURCES:
        command = [str(lean), "-j1", "-DwarningAsError=true", "-o",
                   source.stem + ".olean", source.name]
        print("BUILD", source.stem, flush=True)
        result = subprocess.run(command, cwd=out, env=env, text=True,
                                encoding="utf-8", capture_output=True)
        reports = re.findall(r"depends on axioms: \[([^\]]*)\]", result.stdout)
        unexpected = sorted({a.strip() for report in reports
                             for a in report.split(",") if a.strip()}
                            - ALLOWED_AXIOMS)
        row = {
            "source": str(source.relative_to(ROOT)),
            "source_sha256": sha256(source),
            "command": command,
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "axiom_reports": len(reports),
            "unexpected_axioms": unexpected,
        }
        receipt["builds"].append(row)
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        if result.returncode or unexpected:
            print(result.stdout, end="")
            print(result.stderr, end="")
            print("FAIL", source.stem, "receipt:", receipt_path)
            return 1
    receipt["success"] = True
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print("PASS", len(SOURCES), "modules; receipt:", receipt_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
