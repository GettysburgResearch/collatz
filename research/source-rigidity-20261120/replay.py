#!/usr/bin/env python3
"""Replay exact finite controls without changing any frozen report."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys


CHECKS = (
    ("check_shifted_core_transitions.py", "shifted-core-report.json"),
    ("check_shifted_core_review.py", "shifted-core-independent-report.json"),
    ("check_shifted_smooth_cycles.py", "shifted-smooth-cycles-report.json"),
    ("check_endpoint_capacity.py", "endpoint-capacity-report.json"),
    ("check_critical_cutoffs.py", "critical-cutoffs-report.json"),
    ("check_merger_remains.py", "merger_remains_report.json"),
    ("check_merger_independent.py", "merger-independent-report.json"),
    ("review_shifted_smooth_replay.py", "review-shifted-smooth-replay.json"),
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    repository = packet.parent.parent
    if args.receipt is not None:
        receipt_path = args.receipt.resolve()
        if receipt_path == repository or repository in receipt_path.parents:
            parser.error("write the receipt outside the checkout")
    results = []
    passed = True
    for script, report in CHECKS:
        expected = (packet / report).read_bytes()
        for mode in ((), ("-OO",)):
            command = [sys.executable, "-X", "utf8", "-B", *mode,
                       str((packet / script).relative_to(repository))]
            completed = subprocess.run(command, cwd=repository,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, timeout=60)
            match = completed.stdout == expected
            ok = completed.returncode == 0 and match and not completed.stderr
            passed = passed and ok
            results.append({
                "script": script,
                "mode": "-OO" if mode else "normal",
                "command": command,
                "script_sha256": sha256((packet / script).read_bytes()).hexdigest(),
                "report": report,
                "report_sha256": sha256(expected).hexdigest(),
                "stdout_sha256": sha256(completed.stdout).hexdigest(),
                "stdout_bytes": len(completed.stdout),
                "exit_code": completed.returncode,
                "complete_report_byte_match": match,
                "stderr": completed.stderr.decode("utf-8", errors="replace"),
                "passed": ok,
            })
            print(f"{'PASS' if ok else 'FAIL'} {script} "
                  f"{'-OO' if mode else 'normal'}")
    receipt = {
        "status": "PASS" if passed else "FAIL",
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "scope": "Exact finite controls and complete frozen-report comparisons; "
                 "not a proof of infinite claims or an external theorem.",
        "executions": results,
    }
    if args.receipt is not None:
        receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n",
                                encoding="utf-8")
    print(f"{receipt['status']}: {len(results)} exact replay executions")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
