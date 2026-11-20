#!/usr/bin/env python3
"""Replay this packet in a real clean checkout; write its receipt outside it.

This checks content and exact finite evidence. It does not prove Collatz,
re-prove imported theorems, or replace review of the written arguments.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


PACKET = Path(__file__).resolve().parent
ROOT = PACKET.parents[1]
REPORTS = ROOT / "reports/2026-11-20-deep-reverse-closure"


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def git(*arguments):
    return subprocess.check_output(["git", *arguments], cwd=ROOT, text=True).strip()


def checkout():
    return {"commit": git("rev-parse", "HEAD"),
            "tree": git("rev-parse", "HEAD^{tree}"),
            "status": git("status", "--porcelain"),
            "tracked_files": len(git("ls-files").splitlines())}


def content_check():
    data = json.loads((REPORTS / "content-manifest.json").read_text(encoding="utf8"))
    for item in data["files"]:
        path = (ROOT / item["path"]).resolve()
        need(path.is_relative_to(ROOT), "manifest path leaves checkout")
        need(path.is_file(), "missing manifest file: " + item["path"])
        need(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"],
             "content changed: " + item["path"])
    return len(data["files"])


def replay(job):
    script, optimized = job
    args = [sys.executable, "-X", "utf8", "-B"]
    if optimized:
        args.append("-OO")
    args.append(str(script.relative_to(ROOT)))
    if script.name == "check_height_review.py":
        args += ["--certificate", str((PACKET / "deep_reverse_certificate.json").relative_to(ROOT))]
    elif script.name == "check_reverse_kernel_review.py":
        args += ["--proof", str((PACKET / "REVERSE_CERTIFICATE_KERNEL.md").relative_to(ROOT))]
    elif script.name == "check_mersenne_depth_review.py":
        args += ["--manuscript", str((PACKET / "MERSENNE_WITNESS_DEPTH.md").relative_to(ROOT))]
    start = time.monotonic()
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True,
                            encoding="utf8", timeout=180)
    need(result.returncode == 0,
         script.name + " failed: " + result.stderr + result.stdout)
    body = json.loads(result.stdout)
    return {"script": script.name, "optimized": optimized, "argv": args,
            "exit_code": result.returncode,
            "seconds": round(time.monotonic() - start, 3),
            "stdout_sha256": hashlib.sha256(result.stdout.encode("utf8")).hexdigest(),
            "result": body, "stderr": result.stderr}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    output = args.receipt.resolve()
    need(not output.is_relative_to(ROOT), "receipt must be outside the checkout")
    started = datetime.now(timezone.utc).isoformat()
    before = checkout()
    need(not before["status"], "complete replay requires a clean checkout")
    count = content_check()
    scripts = sorted(p for p in PACKET.glob("check_*.py") if p.name != "check_packet.py")
    need(bool(scripts), "no scientific checkers")
    jobs = [(script, optimized) for script in scripts for optimized in (False, True)]
    with ThreadPoolExecutor(max_workers=4) as pool:
        executions = list(pool.map(replay, jobs))
    for left, right in zip(executions[::2], executions[1::2]):
        need(left["script"] == right["script"] and
             left["stdout_sha256"] == right["stdout_sha256"],
             "normal and optimized reports differ: " + left["script"])
    need(content_check() == count, "manifest count changed")
    after = checkout()
    need(after == before, "checkout changed during scientific replay")
    receipt = {"schema": "collatz-deep-reverse-replay/v1",
               "scope": "content hashes and finite exact evidence, not a full Collatz proof",
               "started_utc": started,
               "finished_utc": datetime.now(timezone.utc).isoformat(),
               "checkout": before, "checkout_after": after,
               "manifest_files": count, "scientific_programs": len(scripts),
               "successful_executions": len(executions),
               "normal_optimized_reports_identical": True,
               "executions": executions, "success": True}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf8")
    print(json.dumps({k: receipt[k] for k in ("success", "checkout", "manifest_files",
          "scientific_programs", "successful_executions", "normal_optimized_reports_identical")},
          indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
