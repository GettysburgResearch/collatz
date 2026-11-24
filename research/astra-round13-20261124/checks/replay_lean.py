#!/usr/bin/env python3
"""Replay the named finite Lean sources in a fresh private build directory.

Requires the pinned Lean and an already built Mathlib checkout. This does not
download dependencies or formalize the surrounding written arguments.
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
import tempfile
import time

ROOT = Path(__file__).resolve().parents[3]
PACKET = "research/astra-round13-20261124/lean/"
SOURCES = [
    "research/lean-shell-cover/ShellCover.lean",
    "research/lean-dyadic-descent-20261121/OffsetDescent.lean",
    "research/lean-shell-cover/ForwardSection.lean",
    *[PACKET + name + ".lean" for name in (
        "AffinePairReturn", "PairedLanguage", "MarkedHalfReturn", "AuditBandReturn",
        "CycleBudget", "IntegerClock", "DyadicSubtotal", "CycleNormComplete",
        "HighFloorNorm", "DefectCover", "GuardedPredecessor")],
    "research/fixed-source-repetition-round11-20261124/RepetitionWindow.lean",
    "research/phase-packing-round12-20261124/PhasePacking.lean",
]
LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--timeout", type=int, default=600,
                        help="maximum seconds for each source")
    args = parser.parse_args()
    compiler = args.lean.resolve()
    mathlib = args.mathlib.resolve()
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
    receipt = dict(schema="collatz-astra-round13-lean/v1",
                   started_utc=datetime.now(timezone.utc).isoformat(),
                   scope="finite sources and named declaration axiom audit; not full Collatz",
                   compiler=str(compiler), lean_version=version,
                   lean_commit=LEAN_COMMIT, mathlib_commit=mathlib_head,
                   rows=[], success=False)
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="collatz-round13-") as temporary:
        build = Path(temporary)
        env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, [build, *paths])))
        for relative in SOURCES:
            original = ROOT / relative
            source = build / original.name
            shutil.copyfile(original, source)
            argv = [str(compiler), "-j1", "-DwarningAsError=true", "-o",
                    source.with_suffix(".olean").name, source.name]
            print("RUN", relative, flush=True)
            started = time.monotonic()
            try:
                result = subprocess.run(argv, cwd=build, env=env, capture_output=True,
                                        text=True, timeout=args.timeout)
                row = dict(source=relative, sha256=digest(source.read_bytes()), argv=argv,
                           exit_code=result.returncode, stdout=result.stdout,
                           stderr=result.stderr)
            except subprocess.TimeoutExpired as exc:
                row = dict(source=relative, sha256=digest(source.read_bytes()), argv=argv,
                           exit_code=124, stdout=(exc.stdout or b"").decode(errors="replace"),
                           stderr="source compilation timed out")
            row["seconds"] = round(time.monotonic() - started, 3)
            axioms = set()
            for listing in re.findall(r"depends on axioms: \[([^]]*)\]", row["stdout"]):
                axioms.update(a.strip() for a in listing.split(",") if a.strip())
            row["printed_axioms"] = sorted(axioms)
            row["unexpected_axioms"] = sorted(axioms - STANDARD_AXIOMS)
            receipt["rows"].append(row)
            print("EXIT", row["exit_code"], relative, row["seconds"], "seconds", flush=True)
            if row["stdout"]:
                print(row["stdout"], end="", flush=True)
            if row["stderr"]:
                print(row["stderr"], end="", flush=True)
            args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
            if row["exit_code"] or row["unexpected_axioms"]:
                break
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    receipt["success"] = (len(receipt["rows"]) == len(SOURCES)
                          and all(r["exit_code"] == 0 and not r["unexpected_axioms"]
                                  for r in receipt["rows"]))
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS" if receipt["success"] else "FAIL", "scoped Lean replay", flush=True)
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
