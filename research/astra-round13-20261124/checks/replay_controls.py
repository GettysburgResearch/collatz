#!/usr/bin/env python3
"""Run the scoped exact finite controls in normal and optimized Python modes."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
PACKET = "research/astra-round13-20261124/checks/"
SOURCES = [
    *[PACKET + name + ".py" for name in (
        "band_controls", "cycle_budget", "prime_power_controls", "affine_ray_controls",
        "high_floor_control", "cover_control", "horizon_controls")],
    "research/fixed-source-repetition-round11-20261124/repetition_controls.py",
    "research/phase-packing-round12-20261124/phase_controls.py",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    receipt = dict(schema="collatz-astra-round13-controls/v1",
                   started_utc=datetime.now(timezone.utc).isoformat(),
                   scope="exact finite checks only; not universal convergence or a Lean replay",
                   python=sys.version, sympy=importlib.metadata.version("sympy"),
                   rows=[], success=False)
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")
    for relative in SOURCES:
        source = ROOT / relative
        outputs = []
        for optimized in (False, True):
            argv = [sys.executable, *(["-O"] if optimized else []),
                    "-X", "utf8", "-B", relative]
            print("RUN", "optimized" if optimized else "normal", relative, flush=True)
            start = time.monotonic()
            try:
                result = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True,
                                        text=True, timeout=600)
                row = dict(source=relative, optimized=optimized, argv=argv,
                           sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                           exit_code=result.returncode, stdout=result.stdout,
                           stderr=result.stderr)
            except subprocess.TimeoutExpired:
                row = dict(source=relative, optimized=optimized, argv=argv,
                           sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                           exit_code=124, stdout="", stderr="control timed out")
            row["seconds"] = round(time.monotonic() - start, 3)
            row["stdout_sha256"] = hashlib.sha256(row["stdout"].encode()).hexdigest()
            receipt["rows"].append(row)
            outputs.append(row["stdout"])
            print("EXIT", row["exit_code"], row["seconds"], "seconds", flush=True)
            args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
            if row["exit_code"]:
                print(row["stderr"], flush=True)
                return 1
        if outputs[0] != outputs[1]:
            receipt["error"] = "normal and optimized outputs differ: " + relative
            args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
            return 1
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    receipt["success"] = True
    receipt["all_normal_optimized_outputs_equal"] = True
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS finite controls; no universal conclusion", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
