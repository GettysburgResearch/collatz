#!/usr/bin/env python3
"""Replay the creative-closure packet in a clean complete checkout.

This checks frozen content, exact certificates and bounded experiments.
The infinite written arguments and the open Collatz obligations are distinct.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[2]
FOLDER = Path("reports/2026-11-20-creative-closure")
PROGRAMS = (
    ("analytic-production", "experiments/creative_analytic_flow.py", "analytic-flow-report.json"),
    ("analytic-independent", str(FOLDER / "analytic-independent-check.py"), "analytic-independent-report.json"),
    ("symbolic-production", "experiments/creative_symbolic_order.py", "symbolic-report.json"),
    ("symbolic-independent", "experiments/creative_symbolic_review.py", "symbolic-independent-report.json"),
    ("source-rank-independent", str(FOLDER / "source-rank-independent.py"), "source-rank-independent-report.json"),
    ("occupation-production", "experiments/creative_occupation.py", "occupation-report.json"),
    ("occupation-independent", str(FOLDER / "five-occupation-independent.py"), "five-occupation-independent-report.json"),
    ("five-production", "experiments/creative_five_closure.py", "five-report.json"),
    ("five-independent", str(FOLDER / "occupation-five-independent.py"), "occupation-five-independent-report.json"),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True, timeout=30).stdout


def state():
    require(Path(os.fsdecode(git("rev-parse", "--show-toplevel").strip())).resolve() == ROOT,
            "a complete top-level checkout is required")
    require(not git("status", "--porcelain"), "checkout and index must be clean, including untracked files")
    paths = [os.fsdecode(p) for p in git("ls-tree", "-r", "--name-only", "-z", "HEAD").split(b"\0") if p]
    require(all((ROOT / p).exists() or (ROOT / p).is_symlink() for p in paths), "incomplete checkout")
    require(not any(p.startswith(b"S ") for p in git("ls-files", "-t", "-z").split(b"\0")),
            "sparse or skip-worktree checkout is not supported")
    return {"commit": git("rev-parse", "HEAD").decode().strip(),
            "tree": git("rev-parse", "HEAD^{tree}").decode().strip(),
            "tracked_files": len(paths)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, help="write actual execution evidence outside the checkout")
    parser.add_argument("--manifest-only", action="store_true", help="check frozen bytes without executing the scientific programs")
    args = parser.parse_args()
    if args.receipt and args.receipt.resolve().is_relative_to(ROOT):
        parser.error("--receipt must be outside the checkout")
    if sys.version_info < (3, 11):
        parser.error("Python 3.11 or newer is required")
    receipt = {
        "schema": "collatz-creative-closure-bundle/v1",
        "scope": "frozen-content checks only" if args.manifest_only else "frozen content, exact local certificates and bounded ordinary replays; not a full Collatz proof",
        "manifest_only": args.manifest_only,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version, "platform": sys.platform,
        "commands": [], "success": False,
    }
    try:
        receipt["checkout"] = state()
        print("CHECKOUT", json.dumps(receipt["checkout"], sort_keys=True), flush=True)
        manifest_path = ROOT / FOLDER / "CONTENT_SHA256.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        require(manifest["schema"] == "collatz-creative-closure-content/v1", "unexpected manifest schema")
        for relative, expected in manifest["files"].items():
            path = ROOT / relative
            require(path.resolve().is_relative_to(ROOT), "manifest path escapes checkout")
            require(sha256(path.read_bytes()).hexdigest() == expected, "content mismatch: " + relative)
        receipt["content_manifest_sha256"] = sha256(manifest_path.read_bytes()).hexdigest()
        receipt["content_files_checked"] = len(manifest["files"])
        print("PASS content manifest", receipt["content_files_checked"], "files", flush=True)
        env = dict(os.environ, PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")
        if not args.manifest_only:
            for name, script, report in PROGRAMS:
                for optimized in (False, True):
                    argv = [sys.executable, "-X", "utf8", "-B"]
                    if optimized:
                        argv.append("-O")
                    argv.extend([script, "--compare", str(FOLDER / report)])
                    start = time.monotonic()
                    try:
                        result = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True,
                                                text=True, encoding="utf-8", errors="strict", timeout=240)
                        row = dict(name=name, optimized=optimized, argv=argv, exit_code=result.returncode,
                                   stdout=result.stdout, stderr=result.stderr)
                    except subprocess.TimeoutExpired:
                        row = dict(name=name, optimized=optimized, argv=argv, exit_code=124,
                                   stdout="", stderr="command timed out")
                    row["seconds"] = round(time.monotonic() - start, 3)
                    row["passed"] = row["exit_code"] == 0
                    receipt["commands"].append(row)
                    print("PASS" if row["passed"] else "FAIL", name, "optimized" if optimized else "normal",
                          "exit", row["exit_code"], "seconds", row["seconds"], flush=True)
        receipt["checkout_after"] = state()
        require(receipt["checkout_after"] == receipt["checkout"], "checkout identity changed")
        receipt["success"] = all(row["passed"] for row in receipt["commands"])
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        receipt["error"] = str(exc)
        print("ERROR", exc, file=sys.stderr, flush=True)
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        with args.receipt.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print("PASS" if receipt["success"] else "FAIL", "creative-closure bundle; Collatz remains open", flush=True)
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
