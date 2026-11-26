#!/usr/bin/env python3
"""Replay complete third-wave finite records in normal and optimized Python.

These executions check finite arithmetic and implementations, not the written
infinite theorems or their external analytic dependencies.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    repo = root.parents[1]
    reports = repo / "reports/unconventional-20261126"
    cases = [
        (root / "arithmetic/check_modular_carry.py", "MODULAR_CARRY_CONTROLS.txt"),
        (root / "defects/check_reset_rigidity.py", "RESET_RIGIDITY_CONTROLS.json"),
        (root / "defects/check_persistent_divisor.py", "PERSISTENT_DIVISOR_CONTROLS.json"),
        (root / "defects/check_depth_ratios.py", "DEPTH_RATIO_CONTROLS.txt"),
        (root / "defects/check_two_block_swap.py", "TWO_BLOCK_SWAP_CONTROLS.json"),
        (root / "defects/check_prefix_swap.py", "PREFIX_SWAP_CONTROLS.json"),
        (root / "trace/check_dirichlet_current.py", "DIRICHLET_CONTROL.json"),
        (root / "trace/check_critical_gates.py", "CRITICAL_GATE_CONTROLS.json"),
        (reports / "reviews/review_final_arithmetic.py", "FINAL_ARITHMETIC_REVIEW_CONTROLS.json"),
        (reports / "reviews/review_annular_current.py", "ANNULAR_REVIEW_CONTROLS.json"),
    ]
    receipt = {"scope": "third-wave complete finite records only", "python": sys.version,
               "runs": []}
    for script, record_name in cases:
        record = reports / record_name
        expected_text = record.read_text(encoding="utf-8")
        is_json = record.suffix == ".json"
        expected = json.loads(expected_text) if is_json else expected_text
        before, record_hash = digest(script), digest(record)
        for optimized in (False, True):
            flags = ["-O", "-B"] if optimized else ["-B"]
            result = subprocess.run([sys.executable, *flags, str(script)],
                                    capture_output=True, text=True, timeout=300)
            if result.returncode or result.stderr:
                raise RuntimeError(f"{script.name}: {result.stdout}\n{result.stderr}")
            actual = json.loads(result.stdout) if is_json else result.stdout
            if actual != expected:
                raise ValueError(f"complete record mismatch: {script.name}, optimized={optimized}")
            receipt["runs"].append({"path": script.relative_to(repo).as_posix(),
                "source_sha256": before, "record": record_name, "record_sha256": record_hash,
                "optimized": optimized, "exit_code": 0, "complete_payload_equal": True})
            print(f"{script.name}: {'optimized' if optimized else 'normal'} complete replay passed",
                  file=sys.stderr, flush=True)
        if digest(script) != before or digest(record) != record_hash:
            raise RuntimeError(f"input changed during replay: {script.name}")
    serialized = json.dumps(receipt, indent=2) + "\n"
    if args.receipt:
        args.receipt.write_text(serialized, encoding="utf-8")
    else:
        sys.stdout.write(serialized)


if __name__ == "__main__":
    main()
