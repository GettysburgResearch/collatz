"""Replay the four published PR201 BigInt controls without changing originals."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "research/killed-green-head-closure-20261124"
REPORT = Path(__file__).resolve().parent


def main() -> None:
    node = shutil.which("node")
    if node is None:
        raise RuntimeError("Node is required for exact BigInt replay")
    records = []
    for relative in ["", "continuation", "prefix-density", "two-end-bridge"]:
        source = PACKET / relative / "controls.js"
        published = json.loads((source.parent / "CONTROLS.json").read_text())
        if "result" in published:
            expected = published["result"]
        elif "execution" in published:
            expected = published["execution"]["result"]
        elif "checks" in published:
            expected = published["checks"]
        else:
            raise RuntimeError((str(source), "unknown published receipt format"))
        result = subprocess.run([node, str(source)], cwd=ROOT, capture_output=True, text=True)
        if result.returncode != 0 or result.stderr:
            raise RuntimeError((str(source), result.returncode, result.stdout, result.stderr))
        actual = json.loads(result.stdout)
        if actual != expected:
            raise RuntimeError((str(source), "receipt mismatch", actual, expected))
        records.append({
            "path": str(source.relative_to(ROOT)),
            "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "exit_code": result.returncode,
            "published_receipt_matched": True,
            "counts": actual,
        })
    constants = {
        "rho_upper": 8 * 3125**24 < 3456**24,
        "rho_lower": 27 * 3125 > 8 * 3456,
        "sigma_below_rho": 27 * 3456 < 32 * 3125,
        "log_slack": 5**10 > 8 * 4**10,
    }
    if not all(constants.values()):
        raise RuntimeError(constants)
    receipt = {
        "published_input_head": "73a145ca99448a78219bd149e273f33b6e3fda4b",
        "node_version": subprocess.check_output([node, "--version"], text=True).strip(),
        "python_version": sys.version.split()[0],
        "checks": records,
        "independent_simple_path_constants": constants,
        "scope": "Finite exact arithmetic only; not an analytic or global Collatz proof.",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
