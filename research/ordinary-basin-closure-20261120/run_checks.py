#!/usr/bin/env python3
"""Replay this proof packet; compare ordinary and optimized Python executions."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
SCRIPTS = (
    "check_certificate_carry.py",
    "check_certificate_carry_review.py",
    "certify_expanding_return.py",
    "check_expanding_return_review.py",
    "check_primitive_trace.py",
    "check_two_macro_normalization.py",
)


def run_one(name, optimized):
    command = [sys.executable, "-B"]
    if optimized:
        command.append("-OO")
    command.append(str(ROOT / name))
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(f"{name} failed ({result.returncode}): {result.stderr}")
    if result.stderr:
        raise RuntimeError(f"{name} emitted unexpected stderr: {result.stderr}")
    return result.stdout, json.loads(result.stdout)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, help="write the complete JSON replay receipt")
    args = parser.parse_args()
    checks = {}
    for name in SCRIPTS:
        normal_text, report = run_one(name, False)
        optimized_text, optimized_report = run_one(name, True)
        if normal_text != optimized_text or report != optimized_report:
            raise RuntimeError(f"{name}: normal and optimized results differ")
        checks[name] = {
            "normal": "passed",
            "optimized": "passed",
            "byte_identical": True,
            "report": report,
        }
    source_hashes = {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(ROOT.iterdir())
        if path.is_file() and path.suffix in (".md", ".py", ".json")
    }
    receipt = {
        "status": "exact packet replays passed; Collatz remains unresolved",
        "evidence": "written universal proofs plus exact finite implementation checks",
        "source_sha256": source_hashes,
        "checks": checks,
    }
    serialized = json.dumps(receipt, sort_keys=True, indent=2) + "\n"
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(serialized)
    summary = {
        "status": receipt["status"],
        "scripts": len(checks),
        "executions": 2 * len(checks),
        "all_normal_and_optimized_outputs_identical": True,
        "scripts_checked": list(checks),
    }
    print(json.dumps(summary, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
