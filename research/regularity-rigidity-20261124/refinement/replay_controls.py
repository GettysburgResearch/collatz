#!/usr/bin/env python3
"""Replay the five frozen PR200 exact JavaScript controls.

These are bounded arithmetic checks, not proofs of asymptotic results.
The four pre-existing JSON outputs are compared as parsed data. The common
suffix output is checked against the published exact profile. Every source
and expected-output byte stream is bound to the receipt by SHA-256.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", required=True, type=Path)
    args = parser.parse_args()
    base = Path(__file__).resolve().parents[1]
    node = shutil.which("node")
    if not node:
        raise SystemExit("node is required")
    cases = [
        ("ratio_pressure.js", "RATIO_CONTROLS.json"),
        ("phase_controls.js", "PHASE_CONTROLS.json"),
        ("continuation/controls.js", "continuation/CONTROLS.json"),
        ("pointwise-fibers/controls.js", "pointwise-fibers/CONTROLS.json"),
        ("pointwise-fibers/COMMON_SUFFIX_CONTROL.js", None),
    ]
    receipt = {
        "scope": "Five bounded exact arithmetic replays; no asymptotic or global Collatz verification",
        "frozen_input_head": "abf36c63b4d0181541d7e029d390d6f636940750",
        "runner_sha256": sha256(Path(__file__).resolve()),
        "node_version": subprocess.check_output([node, "--version"], text=True).strip(),
        "python_version": sys.version.split()[0],
        "cases": [],
    }
    env = {"PATH": os.environ.get("PATH", ""), "LANG": "C.UTF-8"}
    for rel, expected_rel in cases:
        path = base / rel
        started = time.monotonic()
        result = subprocess.run(
            [node, str(path)], cwd=base, env=env, text=True,
            capture_output=True, timeout=180, check=False,
        )
        if result.returncode != 0 or result.stderr:
            raise RuntimeError(f"{rel}: exit {result.returncode}: {result.stderr}")
        actual = json.loads(result.stdout)
        entry = {
            "script": rel,
            "source_sha256": sha256(path),
            "exit_code": result.returncode,
            "elapsed_seconds": round(time.monotonic() - started, 6),
            "result": actual,
        }
        if expected_rel:
            expected_path = base / expected_rel
            expected = json.loads(expected_path.read_text(encoding="utf-8"))
            if actual != expected:
                raise RuntimeError(f"{rel}: output differs from {expected_rel}")
            entry.update(expected=expected_rel, expected_sha256=sha256(expected_path),
                         exact_json_match=True)
        else:
            expected = {
                "states": 16, "clock": 83,
                "parameterResidue": "4483086877358389416883568",
                "end": "208724745227658145", "grade": 37,
                "sourceOdds": 36, "paths": 544,
                "sourceWord": "10100111000011110001110100011100101010001110101101111001111000000000000000010101000",
                "stateList": [[0, "0"], [-1, "-2"], [-1, "1"],
                              [0, "-3"], [0, "-2"], [0, "-1"], [0, "1"], [0, "2"], [0, "3"],
                              [1, "-3"], [1, "-2"], [1, "-1"], [1, "0"], [1, "1"], [1, "2"], [1, "3"]],
            }
            if actual != expected:
                raise RuntimeError("Common suffix result differs from the published exact profile")
            entry["exact_published_profile_match"] = True
        receipt["cases"].append(entry)
        print(f"PASS {rel}", flush=True)
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.receipt}")


if __name__ == "__main__":
    main()
