#!/usr/bin/env python3
"""Replay the packet's fixed exact controls without overwriting their records.

Runs each primary control in both normal and optimized Python, compares the
complete parsed JSON, then runs the independently authored supplemental checks.
Assertion-based supplemental checks explicitly reject optimized execution.
These finite checks support specified interfaces; they are not a Collatz proof.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    repo = root.parents[1]
    reports = repo / "reports/unconventional-20261126"
    cases = [
        ("operator/check_operator.py", "OPERATOR_CONTROLS.json"),
        ("operator/check_bergman.py", "BERGMAN_CONTROLS.json"),
        ("arithmetic/check_adelic.py", "ADELIC_CONTROLS.json"),
        ("arithmetic/check_tripling.py", "TRIPLING_CONTROLS.json"),
        ("arithmetic/check_coupled.py", "COUPLED_CONTROLS.json"),
    ]
    receipt = {
        "scope": "complete fixed finite controls and separately authored supplemental checks",
        "python": sys.version,
        "primary_runs": [],
        "independent_runs": [],
    }
    for relative, record in cases:
        script = root / relative
        expected = json.loads((reports / record).read_text(encoding="utf-8"))
        before = hashlib.sha256(script.read_bytes()).hexdigest()
        for optimized in (False, True):
            flags = ["-O", "-B"] if optimized else ["-B"]
            command = [sys.executable, *flags, str(script)]
            result = subprocess.run(command, text=True, capture_output=True, timeout=180)
            if result.returncode or result.stderr:
                raise RuntimeError(f"{relative}: {result.stdout}\n{result.stderr}")
            payload = json.loads(result.stdout)
            if payload != expected:
                raise ValueError(f"complete control mismatch: {relative}, optimized={optimized}")
            receipt["primary_runs"].append({
                "path": relative, "optimized": optimized, "source_sha256": before,
                "record": record, "record_sha256": hashlib.sha256((reports / record).read_bytes()).hexdigest(),
                "exit_code": result.returncode, "full_payload_equal": True,
            })
            print(f"{relative}: {'optimized' if optimized else 'normal'} complete replay passed", file=sys.stderr, flush=True)
        if hashlib.sha256(script.read_bytes()).hexdigest() != before:
            raise RuntimeError(f"source changed during replay: {relative}")
    for script in sorted((reports / "reviews").glob("review_*.py")):
        result = subprocess.run([sys.executable, "-B", str(script)], text=True,
                                capture_output=True, timeout=180)
        if result.returncode or result.stderr:
            raise RuntimeError(f"independent replay failed: {script.name}: {result.stdout}\n{result.stderr}")
        entry = {
            "path": script.relative_to(repo).as_posix(),
            "source_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
            "exit_code": 0, "stdout": result.stdout,
        }
        if "if not __debug__:" in script.read_text(encoding="utf-8"):
            denied = subprocess.run([sys.executable, "-O", "-B", str(script)],
                                    text=True, capture_output=True, timeout=20)
            if denied.returncode == 0 or "requires Python without -O or -OO" not in denied.stderr:
                raise RuntimeError(f"optimized-mode guard failed: {script.name}")
            entry["optimized_mode_explicitly_rejected"] = True
        receipt["independent_runs"].append(entry)
        print(f"{script.name}: independent finite controls passed", file=sys.stderr, flush=True)
    serialized = json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
    if args.receipt:
        args.receipt.write_text(serialized, encoding="utf-8")
    else:
        sys.stdout.write(serialized)


if __name__ == "__main__":
    main()
