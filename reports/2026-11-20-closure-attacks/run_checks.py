#!/usr/bin/env python3
"""Replay this packet in a clean checkout; write a receipt outside it."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time


ROOT = Path(__file__).resolve().parents[2]
PACKET = Path("research/closure-attacks-20261120")
REPORTS = Path("reports/2026-11-20-closure-attacks")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    output = args.receipt.resolve()
    require(not output.is_relative_to(ROOT), "receipt must be outside the checkout")
    require(not output.exists(), "refusing to replace an existing execution receipt")
    before = git("status", "--porcelain", "--untracked-files=all")
    require(not before, "a clean complete checkout is required")
    require(git("rev-parse", "--is-inside-work-tree") == "true", "not a git checkout")
    require(not any(line.startswith("S ") for line in git("ls-files", "-t").splitlines()),
            "sparse or skip-worktree checkout is not a complete replay")
    manifest_path = ROOT / REPORTS / "CONTENT_SHA256.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for path, expected in manifest["files"].items():
        require(digest((ROOT / path).read_bytes()) == expected,
                "content hash mismatch: " + path)
    record = {
        "schema": 1,
        "started_at_utc": now(),
        "checkout": str(ROOT),
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "tracked_files": len(git("ls-files").splitlines()),
        "clean_before": True,
        "manifest_sha256": digest(manifest_path.read_bytes()),
        "verified_content_files": len(manifest["files"]),
        "checks": [],
        "evidence_boundary": (
            "Exact report comparisons and file identities; written proofs establish "
            "universal conditional and arithmetic statements. Floating logarithms "
            "remain diagnostics. No global Collatz proof or external Lean build."
        ),
    }
    specs = [
        ("merger/check_single_multiplier.py", "merger/single_multiplier_report.json", False),
        ("merger/check_physical_returns.py", "merger/physical_returns_report.json", False),
        ("arithmetic/check_arithmetic_closure.py", "arithmetic/arithmetic-closure-report.json", True),
        ("merger/check_arithmetic_review.py", "merger/arithmetic_review_report.json", False),
        ("critical/check_single_slice_energy.py", "critical/single_slice_energy_receipt.json", False),
    ]
    try:
        with tempfile.TemporaryDirectory(prefix="collatz-closure-checks-") as tmp:
            for index, (script, expected_file, writes_report) in enumerate(specs):
                argv = [sys.executable, "-X", "utf8", "-B", str(PACKET / script)]
                actual_path = Path(tmp) / (str(index) + ".json")
                if writes_report:
                    argv += ["--output", str(actual_path)]
                start = time.monotonic()
                result = subprocess.run(
                    argv, cwd=ROOT, text=True, encoding="utf-8",
                    capture_output=True, timeout=180,
                )
                entry = {
                    "command": argv,
                    "returncode": result.returncode,
                    "seconds": round(time.monotonic() - start, 6),
                    "stdout_sha256": digest(result.stdout.encode("utf-8")),
                    "stderr": result.stderr,
                    "expected_report": str(PACKET / expected_file),
                }
                record["checks"].append(entry)
                require(result.returncode == 0,
                        script + " failed:\n" + result.stdout + result.stderr)
                actual_bytes = actual_path.read_bytes() if writes_report else result.stdout.encode("utf-8")
                expected_bytes = (ROOT / PACKET / expected_file).read_bytes()
                require(json.loads(actual_bytes) == json.loads(expected_bytes),
                        script + " did not reproduce the frozen report")
                entry["actual_report_sha256"] = digest(actual_bytes)
                entry["expected_report_sha256"] = digest(expected_bytes)
                entry["report_comparison"] = "PASS (JSON equality)"
                entry["byte_identical_report"] = actual_bytes == expected_bytes
        after = git("status", "--porcelain", "--untracked-files=all")
        record["clean_after"] = not after
        require(not after, "checker modified the checkout")
        require(git("rev-parse", "HEAD") == record["head"], "HEAD changed during replay")
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
        "verified_content_files": record["verified_content_files"],
        "checks_passed": len(record["checks"]),
        "clean_before": record["clean_before"],
        "clean_after": record["clean_after"],
        "receipt": str(output),
        "receipt_sha256": digest(output.read_bytes()),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
