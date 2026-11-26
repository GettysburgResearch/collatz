"""Replay the packet's exact finite controls in normal and optimized Python.

The receipt records executed finite checks. It does not certify the written
asymptotic arguments, the imported analytic inputs, or universal Collatz.
All output is written outside this source directory.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
CHECKS = (
    ("check_adelic.py", ()),
    ("check_geometric.py", ()),
    ("check_wall_controls.py", ()),
    ("check_wall_periods.py", ("--through", "30")),
    ("check_precision.py", ()),
    ("check_entry_edges.py", ()),
    ("check_fresh_ascent.py", ()),
    ("check_log_tower_independent.py", ()),
    ("check_wall_independent.py", ()),
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.is_relative_to(ROOT):
        parser.error("the output directory must be outside the source packet")
    if output.exists() and any(output.iterdir()):
        parser.error("use a new or empty output directory to preserve prior receipts")
    output.mkdir(parents=True, exist_ok=True)
    source_hashes = {
        p.name: sha(p.read_bytes())
        for p in sorted(ROOT.iterdir())
        if p.suffix in {".lean", ".py"}
    }
    receipt = {
        "schema": "collatz-unconventional-finite-replay/v1",
        "scope": "exact finite controls; not universal Collatz or an analytic proof",
        "started_utc": now(),
        "python": sys.version,
        "source_sha256": source_hashes,
        "checks": [],
        "success": False,
    }
    try:
        for name, extra in CHECKS:
            logs = []
            row = {"script": name, "executions": []}
            receipt["checks"].append(row)
            for mode in ("normal", "optimized"):
                command = [sys.executable, "-X", "utf8", "-B"]
                if mode == "optimized":
                    command.append("-O")
                command += [name, *extra]
                started = now()
                result = subprocess.run(
                    command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    check=False,
                )
                filename = f"{Path(name).stem}-{mode}.log"
                (output / filename).write_bytes(result.stdout)
                row["executions"].append({
                    "mode": mode, "argv": command, "started_utc": started,
                    "finished_utc": now(), "exit_code": result.returncode,
                    "log": filename, "log_sha256": sha(result.stdout),
                })
                if result.returncode:
                    raise RuntimeError(f"{name} failed in {mode} mode; see {filename}")
                logs.append(result.stdout)
            row["byte_identical_modes"] = logs[0] == logs[1]
            if not row["byte_identical_modes"]:
                raise RuntimeError(f"{name} produced different normal and optimized output")
            print(f"PASS {name}: normal and optimized outputs agree", flush=True)
        for name, digest in source_hashes.items():
            if sha((ROOT / name).read_bytes()) != digest:
                raise RuntimeError(f"source changed during replay: {name}")
        receipt["success"] = True
    except Exception as error:
        receipt["error"] = str(error)
        print(f"FAIL {error}", file=sys.stderr)
    finally:
        receipt["finished_utc"] = now()
        (output / "receipt.json").write_text(
            json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
        )
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
