#!/usr/bin/env python3
"""Replay the new exact controls in normal and optimized Python.

Uses only the standard library. The original numerical package replay is a
separate command. Written analytic proofs and finite arithmetic controls have
different scopes; neither this driver nor repository integrity proves Collatz.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

from replay_sources import ARCHIVE, V3, authenticate, require


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def encode(value) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def run(script: str, arguments: list[str], optimized: bool):
    command = [sys.executable, "-X", "utf8", "-B"]
    if optimized:
        command.append("-O")
    command += [str(HERE / script), *arguments]
    completed = subprocess.run(command, cwd=ROOT, capture_output=True,
                               text=True, encoding="utf-8", timeout=180)
    return command, completed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    _, source_count = authenticate()
    pin_manifest = json.loads((ARCHIVE / "pinned-pr146-manifest.json").read_text())
    pin_root = ARCHIVE / "pinned-pr146"
    for row in pin_manifest["files"]:
        require(digest(pin_root / row["path"]) == row["sha256"],
                "Pinned dependency hash mismatch: " + row["path"])

    watched = sorted(p for p in HERE.iterdir() if p.is_file())
    hashes_before = {p.name: digest(p) for p in watched}
    certificate_path = ARCHIVE / "source" / V3 / "farkas_certificates_r4_r6.json"
    jobs = [
        ("ordinary_dirichlet", "check_ordinary_dirichlet.py",
         ["--source-root", str(pin_root)], True),
        ("farkas_and_ruelle", "check_farkas_and_ruelle.py",
         ["--certificates", str(certificate_path)], True),
        ("mahler_and_integrality", "check_mahler_and_integrality.py", [], False),
        ("routes_bundle", "check_routes_bundle.py",
         ["--bundle", str(ARCHIVE / "source/collatz_routes_bundle")], True),
    ]
    result = {
        "schema": "collatz-gemini-dirichlet-exact-replay/v1",
        "scope": "Eight scoped exact replays and two rejection controls; written infinite proofs remain separate.",
        "collatz_proved": False,
        "python": sys.version,
        "archived_files_authenticated": source_count,
        "dependency_commit": pin_manifest["commit"],
        "dependency_files_authenticated": len(pin_manifest["files"]),
        "scientific_packet_sha256": hashes_before,
        "checks": [],
        "rejection_controls": [],
    }
    with TemporaryDirectory(prefix="collatz-dirichlet-checks-") as scratch:
        tmp = Path(scratch)
        for name, script, arguments, writes_output in jobs:
            payloads = []
            modes = []
            for optimized in (False, True):
                output = tmp / (name + ("-optimized" if optimized else "") + ".json")
                actual_args = arguments + (["--output", str(output)] if writes_output else [])
                command, completed = run(script, actual_args, optimized)
                require(completed.returncode == 0,
                        f"{name} failed, optimized={optimized}: {completed.stderr}")
                payload = (json.loads(output.read_text()) if writes_output
                           else json.loads(completed.stdout))
                require(payload.get("status") == "PASS", name + " did not report PASS")
                payloads.append(payload)
                modes.append({"optimized": optimized, "command": command,
                              "exit_code": completed.returncode,
                              "stderr": completed.stderr,
                              "stdout_sha256": sha256(completed.stdout.encode()).hexdigest()})
            require(payloads[0] == payloads[1], name + " changes under Python optimization")
            if name == "routes_bundle":
                exported = json.loads((HERE / "bellman-p5-certificate.json").read_text())
                require(payloads[0]["exact_Bellman_certificate"] == exported,
                        "Exported Bellman certificate differs from exact reconstruction")
            result["checks"].append({
                "name": name, "runs": modes, "normal_optimized_payloads_identical": True,
                "payload_sha256": sha256(encode(payloads[0]).encode()).hexdigest(),
                "payload": payloads[0],
            })

        # Reject a broken serialized Farkas normalization in both modes.
        # No attachment or accepted certificate is modified.
        damaged = json.loads(certificate_path.read_text())
        damaged["r4_s0840"]["w"][-1] = 0
        damaged_path = tmp / "damaged-normalization.json"
        damaged_path.write_text(encode(damaged), encoding="utf-8")
        for optimized in (False, True):
            command, completed = run("check_farkas_and_ruelle.py",
                                     ["--certificates", str(damaged_path)], optimized)
            require(completed.returncode != 0 and "ValueError" in completed.stderr,
                    "Broken serialized normalization was accepted")
            result["rejection_controls"].append({
                "name": "broken_Farkas_normalization", "optimized": optimized,
                "command": command, "exit_code": completed.returncode,
                "rejected": True, "stderr": completed.stderr,
            })

    _, count_after = authenticate()
    require(count_after == source_count, "Source count changed during replay")
    require(hashes_before == {p.name: digest(p) for p in watched},
            "Scientific packet changed during replay")
    result["status"] = "PASS"
    result["accepted_replays"] = sum(len(x["runs"]) for x in result["checks"])
    result["expected_rejections"] = len(result["rejection_controls"])
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(encode(result), encoding="utf-8")
    print(encode({k: result[k] for k in
                  ("status", "scope", "collatz_proved", "archived_files_authenticated",
                   "dependency_files_authenticated", "accepted_replays", "expected_rejections")}),
          end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
