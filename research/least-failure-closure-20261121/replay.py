#!/usr/bin/env python3
"""Replay this packet's exact finite checks against frozen complete reports."""
import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import time

CASES = (
    ("check_multistep_core_returns.py", "multistep-core-returns-report"),
    ("check_fixed_defect_core_returns.py", "fixed-defect-core-returns-report"),
    ("check_excursion_frequency.py", "excursion-frequency-report"),
    ("check_homogeneous_five_transport.py", "homogeneous-five-report"),
    ("check_homogeneous_localization.py", "homogeneous-localization-report"),
    ("check_expanded_renewal.py", "expanded-renewal-report"),
    ("check_core_returns_independent.py", "core-returns-independent-report"),
    ("check_transport_review.py", "transport-review-report"),
    ("check_renewal_review.py", "renewal-review-report"),
)


def digest(data):
    return sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    started = datetime.now(timezone.utc).isoformat()
    records = []
    for script, stem in CASES:
        for optimized in (False, True):
            report = packet / (stem + ("-oo" if optimized else "") + ".json")
            command = [sys.executable, "-X", "utf8", "-B"]
            if optimized:
                command.append("-OO")
            command.append(script)
            before = time.monotonic()
            result = subprocess.run(command, cwd=packet, capture_output=True, timeout=60)
            expected = report.read_bytes()
            record = {
                "command": command,
                "checker_sha256": digest((packet/script).read_bytes()),
                "expected_report": report.name,
                "expected_sha256": digest(expected),
                "stdout_sha256": digest(result.stdout),
                "stdout_bytes": len(result.stdout),
                "stderr": result.stderr.decode("utf-8", errors="replace"),
                "exit_code": result.returncode,
                "elapsed_seconds": round(time.monotonic()-before, 6),
                "complete_report_equal": result.stdout == expected,
            }
            record["passed"] = (result.returncode == 0 and not result.stderr
                                and record["complete_report_equal"])
            records.append(record)
    pairs_equal = all((packet/(stem+".json")).read_bytes() ==
                      (packet/(stem+"-oo.json")).read_bytes()
                      for _, stem in CASES)
    passed = pairs_equal and all(r["passed"] for r in records)
    receipt = {
        "status": "PASS" if passed else "FAIL",
        "started_utc": started,
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": sys.version,
        "programs": len(CASES), "executions": len(records),
        "all_normal_optimized_reports_identical": pairs_equal,
        "records": records,
        "scope": "Finite arithmetic and domain controls only. Written proofs supply universal quantifiers and named dependencies; no Collatz proof is asserted.",
    }
    encoded = json.dumps(receipt, indent=2, sort_keys=True)+"\n"
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(encoded, encoding="utf-8")
    print(json.dumps({k:receipt[k] for k in
                      ("status","programs","executions",
                       "all_normal_optimized_reports_identical")}, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
