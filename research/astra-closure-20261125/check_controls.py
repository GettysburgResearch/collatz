#!/usr/bin/env python3
"""Run the new exact finite programs in normal and optimized Python."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
PACKET = Path("research/astra-closure-20261125")
PROGRAMS = [
    PACKET / "escape/check_rows.py",
    PACKET / "cycles/check.py",
    PACKET / "cycles/check_joint.py",
    PACKET / "cycles/check_basin.py",
]


def execute(job: tuple[Path, bool]) -> dict[str, object]:
    path, optimized = job
    argv = [sys.executable, "-B", *( ["-O"] if optimized else []), str(path)]
    start = time.monotonic()
    result = subprocess.run(argv, cwd=ROOT, text=True, capture_output=True)
    print(f"{path.name} optimized={optimized}: exit {result.returncode}", flush=True)
    return {
        "source": path.as_posix(),
        "sha256": hashlib.sha256((ROOT / path).read_bytes()).hexdigest(),
        "optimized": optimized, "argv": argv, "exit_code": result.returncode,
        "seconds": round(time.monotonic() - start, 3),
        "stdout": result.stdout, "stderr": result.stderr,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", required=True, type=Path)
    args = parser.parse_args()
    start = time.monotonic()
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(execute, [(p, opt) for p in PROGRAMS for opt in (False, True)]))
    identical = all(results[i]["stdout"] == results[i+1]["stdout"] for i in range(0, len(results), 2))
    success = all(r["exit_code"] == 0 for r in results) and identical
    receipt = {
        "schema": "collatz-astra-closure-finite/v1", "python": sys.version,
        "scope": "Only the new finite exact controls, not universal Collatz verification or the asymptotic theorems.",
        "runs": results, "normal_optimized_stdout_identical": identical,
        "seconds": round(time.monotonic() - start, 3), "success": success,
    }
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"success": success, "runs": len(results), "normal_optimized_stdout_identical": identical}))
    if not success:
        for r in results:
            if r["exit_code"]:
                print(r["stdout"], r["stderr"])
        raise SystemExit(1)


if __name__ == "__main__":
    main()
