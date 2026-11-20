#!/usr/bin/env python3
"""Run this packet's exact finite checks in a clean complete checkout."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
PACKET = Path("research/global-forcing-20261121")
REPORTS = Path("reports/2026-11-21-global-forcing")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def now():
    return datetime.now(timezone.utc).isoformat()


def check_manifest(manifest):
    for path, expected in manifest["files"].items():
        target = (ROOT / path).resolve()
        require(target.is_relative_to(ROOT), "manifest path outside checkout")
        require(digest(target.read_bytes()) == expected, "content mismatch: " + path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    output = args.receipt.resolve()
    require(not output.is_relative_to(ROOT), "receipt must be outside checkout")
    require(not output.exists(), "refusing to replace an execution receipt")
    require(git("rev-parse", "--is-inside-work-tree") == "true", "not a checkout")
    require(not git("status", "--porcelain", "--untracked-files=all"),
            "a clean complete checkout is required")
    flags = git("ls-files", "-v").splitlines()
    require(not any(row.startswith("S ") or row[:1].islower() for row in flags),
            "sparse, skip-worktree or assume-unchanged entries are not a complete replay")
    sparse = subprocess.run(
        ["git", "config", "--bool", "--get", "core.sparseCheckout"],
        cwd=ROOT, text=True, capture_output=True,
    )
    require(sparse.returncode in (0, 1) and sparse.stdout.strip() != "true",
            "sparse checkout is not a complete replay")
    manifest_path = ROOT / REPORTS / "CONTENT_SHA256.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    check_manifest(manifest)
    record = {
        "schema": "collatz-global-forcing-execution/v1",
        "started_at_utc": now(),
        "checkout": str(ROOT),
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "tracked_files": len(flags),
        "clean_before": True,
        "manifest_sha256": digest(manifest_path.read_bytes()),
        "verified_content_files": len(manifest["files"]),
        "python": sys.version,
        "checks": [],
        "evidence_boundary": (
            "Exact finite calculations and byte-identical frozen reports. "
            "Written arguments establish all-parameter statements; named external "
            "theorems remain external inputs. No universal Collatz proof, "
            "exhaustive cycle census, or formal proof-assistant build is claimed."
        ),
    }
    specs = [
        ("arithmetic/check_shifted_rank.py", "arithmetic/shifted-rank-report.json"),
        ("certificates/check_carry_compiler.py", "certificates/carry-compiler-report.json"),
        ("energy/check_renewal_phase.py", "energy/renewal_phase_report.json"),
    ]
    try:
        for script, reference in specs:
            expected = (ROOT / PACKET / reference).read_bytes()
            first = None
            for optimized in (False, True):
                argv = [sys.executable, "-X", "utf8", "-B"]
                if optimized:
                    argv.append("-OO")
                argv.append(str(PACKET / script))
                started = time.monotonic()
                result = subprocess.run(
                    argv, cwd=ROOT, capture_output=True, timeout=180,
                )
                entry = {
                    "command": argv,
                    "optimized": optimized,
                    "returncode": result.returncode,
                    "seconds": round(time.monotonic() - started, 6),
                    "stdout_sha256": digest(result.stdout),
                    "stderr": result.stderr.decode("utf-8", errors="replace"),
                    "expected_report": str(PACKET / reference),
                    "expected_report_sha256": digest(expected),
                    "byte_identical_report": result.stdout == expected,
                }
                record["checks"].append(entry)
                require(result.returncode == 0,
                        script + " failed: " + entry["stderr"])
                require(result.stdout == expected,
                        script + " did not reproduce the full frozen report")
                require(json.loads(result.stdout).get("status") == "PASS",
                        script + " report did not pass")
                if first is not None:
                    require(result.stdout == first, "optimization changed the report")
                first = result.stdout
        check_manifest(manifest)
        record["clean_after"] = not git("status", "--porcelain", "--untracked-files=all")
        require(record["clean_after"], "checker modified the checkout")
        require(git("rev-parse", "HEAD") == record["head"], "HEAD changed during replay")
        require(git("rev-parse", "HEAD^{tree}") == record["tree"], "tree changed during replay")
        record["status"] = "PASS"
    except Exception as error:
        record["status"] = "FAIL"
        record["error"] = str(error)
        record["clean_after"] = not git("status", "--porcelain", "--untracked-files=all")
        raise
    finally:
        record["finished_at_utc"] = now()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": record["status"],
        "head": record["head"],
        "tree": record["tree"],
        "checks_passed": len(record["checks"]),
        "verified_content_files": record["verified_content_files"],
        "clean_before": record["clean_before"],
        "clean_after": record["clean_after"],
        "receipt": str(output),
        "receipt_sha256": digest(output.read_bytes()),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
