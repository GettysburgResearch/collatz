#!/usr/bin/env python3
"""Execute this packet's Lean build and dependency audit; do not infer Collatz."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time

PACKET = Path(__file__).resolve().parent
ROOT = PACKET.parents[1]
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def git(*args: str) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True).strip()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sources() -> dict[str, str]:
    return {
        str(p.relative_to(ROOT)): digest(p)
        for p in sorted(PACKET.rglob("*"))
        if p.is_file() and ".lake" not in p.parts and "__pycache__" not in p.parts
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lake", default="lake")
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    if args.receipt.resolve().is_relative_to(ROOT):
        parser.error("write the receipt outside the checkout")
    receipt = {
        "schema": "collatz-lean-checkpoint/v1",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "actual Lean execution and declaration dependencies; no full Collatz proof",
        "commit": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "tracked_clean": not git("status", "--porcelain", "--untracked-files=no"),
        "source_sha256_before": sources(),
        "commands": [],
        "success": False,
    }
    try:
        pins = json.loads((PACKET / "upstream-files.json").read_text())
        for pin in pins["files"]:
            if digest(ROOT / pin["local_path"]) != pin["sha256"]:
                raise ValueError("imported source changed: " + pin["local_path"])
        receipt["upstream_pins_match"] = True
        cmds = [
            [args.lake, "env", "lean", "--version"],
            [args.lake, "build"],
            [args.lake, "env", "lean", "-DwarningAsError=true", "CheckpointAudit.lean"],
        ]
        for argv in cmds:
            start = time.monotonic()
            result = subprocess.run(argv, cwd=PACKET / "lean", text=True,
                                    capture_output=True, timeout=300)
            row = {"argv": argv, "exit_code": result.returncode,
                   "stdout": result.stdout, "stderr": result.stderr,
                   "seconds": round(time.monotonic() - start, 3)}
            receipt["commands"].append(row)
            print("RUN", " ".join(argv), "EXIT", result.returncode, flush=True)
            if result.returncode:
                raise ValueError(result.stdout + result.stderr)
        if "version 4.34.1," not in receipt["commands"][0]["stdout"]:
            raise ValueError("this recorded execution requires Lean 4.34.1")
        audit = receipt["commands"][-1]["stdout"]
        expected = set(re.findall(r"^#print axioms ([A-Za-z0-9_.]+)",
                                  (PACKET / "lean/CheckpointAudit.lean").read_text(), re.M))
        axioms = {name: [x.strip() for x in body.split(",") if x.strip()]
                  for name, body in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", audit)}
        for name in re.findall(r"'([^']+)' does not depend on any axioms", audit):
            axioms[name] = []
        receipt["audited_axioms"] = axioms
        if set(axioms) != expected:
            raise ValueError("printed declarations do not match the audit inventory")
        if any(set(xs) - ALLOWED for xs in axioms.values()):
            raise ValueError("an audited declaration uses an unapproved axiom")
        receipt["source_sha256_after"] = sources()
        if receipt["source_sha256_before"] != receipt["source_sha256_after"]:
            raise ValueError("packet sources changed during execution")
        receipt["success"] = True
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        receipt["error"] = str(exc)
        print("ERROR", str(exc), flush=True)
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS" if receipt["success"] else "FAIL", receipt["scope"], flush=True)
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
