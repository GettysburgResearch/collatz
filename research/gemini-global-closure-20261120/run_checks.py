#!/usr/bin/env python3
"""Run the scoped mathematical replays, preserving their finite evidence limits.

Default checks need only Python's standard library. --replay-upload additionally
runs the original package in a temporary copy; its route 3 requires NumPy.
Nothing in this driver verifies universal Collatz convergence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


PACKET = Path(__file__).resolve().parent
REPO = PACKET.parents[1]
ARCHIVE = REPO / "archive/gemini-proposals-20261120"
SOURCE = ARCHIVE / "source"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--replay-upload", action="store_true")
    args = parser.parse_args()
    manifest = json.loads((ARCHIVE / "source-manifest.json").read_text())
    expected = manifest["source_sha256"]
    observed = {
        str(path.relative_to(SOURCE)): sha256(path)
        for path in sorted(SOURCE.rglob("*")) if path.is_file()
    }
    require(observed == expected, "Archived source inventory or bytes changed")

    specs = [
        ("check_routes_1_5.py", ["--proposal-root", str(SOURCE)]),
        ("verify_inverse_transport.py", []),
        ("check_hermite_pade_audit.py", []),
    ]
    runs = []
    for script, arguments in specs:
        previous_output = None
        for optimized in (False, True):
            command = [sys.executable]
            if optimized:
                command.append("-O")
            command += ["-X", "utf8", "-B", str(PACKET / script), *arguments]
            process = subprocess.run(command, cwd=REPO, capture_output=True, text=True)
            require(process.returncode == 0,
                    f"{script} failed (optimized={optimized}):\n{process.stdout}\n{process.stderr}")
            result = json.loads(process.stdout)
            require(str(result.get("status", "")).startswith("PASS"),
                    f"{script} did not report a successful scoped check")
            if previous_output is not None:
                require(process.stdout == previous_output,
                        f"{script} changed output under optimized Python")
            previous_output = process.stdout
            runs.append({
                "script": script,
                "optimized": optimized,
                "returncode": process.returncode,
                "stderr": process.stderr,
                "stdout_sha256": hashlib.sha256(process.stdout.encode()).hexdigest(),
                "result": result,
            })

    upload_replay = {"executed_in_this_run": False}
    if args.replay_upload:
        with tempfile.TemporaryDirectory(prefix="collatz-gemini-replay-") as temporary:
            copied = Path(temporary) / "source"
            shutil.copytree(SOURCE, copied)
            process = subprocess.run(
                [sys.executable, "-X", "utf8", "-B", str(copied / "run_all_verifiers.py")],
                cwd=copied, capture_output=True, text=True,
            )
            require(process.returncode == 0,
                    f"Original package replay failed:\n{process.stdout}\n{process.stderr}")
            require((copied / "verification_receipt.json").read_bytes()
                    == (SOURCE / "verification_receipt.json").read_bytes(),
                    "Original verification receipt was not reproduced exactly")
            upload_replay = {
                "executed_in_this_run": True,
                "returncode": process.returncode,
                "stdout": process.stdout,
                "stderr": process.stderr,
                "receipt_byte_identical": True,
                "receipt_sha256": sha256(copied / "verification_receipt.json"),
                "scope": "Reproduced the five original finite calculations; prose claims audited separately.",
            }

    receipt = {
        "status": "PASS_SCOPED_ARITHMETIC",
        "collatz_proved": False,
        "python": sys.version,
        "archived_files_authenticated": len(observed),
        "uploaded_zip_sha256": manifest["uploaded_zip_sha256"],
        "source_sha256": {
            path.name: sha256(path) for path in sorted(PACKET.iterdir())
            if path.is_file() and path.suffix in (".md", ".py")
        },
        "runs": runs,
        "upload_replay": upload_replay,
        "evidence_scope": (
            "Finite exact arithmetic and semantic countercontrols in normal and optimized Python. "
            "General claims rest on the written proofs and their stated dependencies. "
            "No Lean build, full convergence theorem, or external mathematical acceptance is claimed."
        ),
    }
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.receipt:
        args.receipt.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
