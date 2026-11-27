#!/usr/bin/env python3
"""Replay exact finite controls in ordinary and optimized Python."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

PACKET = Path(__file__).resolve().parent
CHECKERS = ["cycles/check_height_entropy.py", "cycles/check_width_entropy.py", "mersenne/check_mersenne.py"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", required=True, type=Path)
    args = parser.parse_args()
    receipt = {"schema": "collatz-global-finite/v1", "success": False,
               "started_utc": datetime.now(timezone.utc).isoformat(),
               "scope": "Bounded exact controls only; no infinite theorem or Collatz proof.",
               "python": sys.version, "checkers": []}
    for relative in CHECKERS:
        path = PACKET / relative
        before = path.read_bytes()
        row = {"path": relative, "sha256": hashlib.sha256(before).hexdigest(), "runs": []}
        for mode in ([], ["-O"]):
            command = [sys.executable, "-X", "utf8", "-B", *mode, str(path)]
            result = subprocess.run(command, cwd=PACKET, capture_output=True, text=True, timeout=120)
            row["runs"].append({"optimized": bool(mode), "exit_code": result.returncode,
                                "stdout": result.stdout, "stderr": result.stderr})
        if before != path.read_bytes():
            raise RuntimeError("Source changed during replay: " + relative)
        row["success"] = (all(r["exit_code"] == 0 and not r["stderr"] for r in row["runs"])
                          and row["runs"][0]["stdout"] == row["runs"][1]["stdout"])
        receipt["checkers"].append(row)
        print(relative, "PASS" if row["success"] else "FAIL", flush=True)
    receipt["success"] = all(r["success"] for r in receipt["checkers"])
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
