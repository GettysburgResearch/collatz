#!/usr/bin/env python3
"""Replay the frozen global-closure packet in a clean complete checkout.

This checks exact symbolic and bounded evidence. It does not prove Collatz,
the forward-five closure law, or the reciprocal-psi closing estimate.
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
FOLDER = Path("reports/2026-11-20-global-closure")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True, timeout=30).stdout


def state():
    require(Path(os.fsdecode(git("rev-parse", "--show-toplevel").strip())).resolve() == ROOT,
            "a complete top-level repository checkout is required")
    require(not git("status", "--porcelain"), "checkout and index must be clean, including untracked files")
    paths = [os.fsdecode(p) for p in git("ls-tree", "-r", "--name-only", "-z", "HEAD").split(b"\0") if p]
    require(all((ROOT / p).exists() or (ROOT / p).is_symlink() for p in paths), "incomplete checkout")
    require(not any(p.startswith(b"S ") for p in git("ls-files", "-t", "-z").split(b"\0")),
            "sparse or skip-worktree checkout is not supported")
    return {
        "commit": git("rev-parse", "HEAD").decode().strip(),
        "tree": git("rev-parse", "HEAD^{tree}").decode().strip(),
        "tracked_files": len(paths),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, help="write actual execution evidence outside the checkout")
    args = parser.parse_args()
    if args.receipt and args.receipt.resolve().is_relative_to(ROOT):
        parser.error("--receipt must be outside the checkout")
    if sys.version_info < (3, 11):
        parser.error("Python 3.11 or newer is required")
    receipt = {
        "schema": "collatz-global-closure-bundle/v1",
        "scope": "frozen content, exact symbolic certificate checks and bounded replays; not a full Collatz proof",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "platform": sys.platform,
        "commands": [],
        "success": False,
    }
    try:
        receipt["checkout"] = state()
        print("CHECKOUT", json.dumps(receipt["checkout"], sort_keys=True), flush=True)
        manifest_path = ROOT / FOLDER / "CONTENT_SHA256.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        require(manifest["schema"] == "collatz-global-closure-content/v1", "unexpected manifest schema")
        for relative, expected in manifest["files"].items():
            path = ROOT / relative
            require(path.resolve().is_relative_to(ROOT), "manifest path escapes checkout")
            require(sha256(path.read_bytes()).hexdigest() == expected, "content mismatch: " + relative)
        receipt["content_manifest_sha256"] = sha256(manifest_path.read_bytes()).hexdigest()
        receipt["content_files_checked"] = len(manifest["files"])
        print("PASS content manifest", receipt["content_files_checked"], "files", flush=True)
        commands = []
        for name in ("arithmetic", "merger", "transport"):
            commands.append(("production-" + name,
                             [f"experiments/global_closure_{name}.py", "--compare", str(FOLDER / f"{name}-report.json")],
                             "success"))
        for name, script, report in (
            ("arithmetic", "arithmetic-independent-check.py", "arithmetic-independent-report.json"),
            ("merger", "check_merger_independent.py", "merger-independent-report.json"),
            ("closing", "check_closing_independent.py", "closing-independent-report.json"),
        ):
            commands.append(("review-" + name,
                             [str(FOLDER / script), "--compare", str(FOLDER / report)], "success"))
        commands.append(("review-transport", [str(FOLDER / "arithmetic-transport-independent.py")], "json_compare"))
        commands.append(("production-arithmetic-optimized-refusal",
                         ["-O", "experiments/global_closure_arithmetic.py", "--compare", str(FOLDER / "arithmetic-report.json")],
                         "expected_refusal"))
        env = dict(os.environ, PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")
        for name, command, expectation in commands:
            argv = [sys.executable, "-X", "utf8", "-B", *command]
            start = time.monotonic()
            try:
                result = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True,
                                        text=True, encoding="utf-8", errors="strict", timeout=180)
                row = dict(name=name, argv=argv, exit_code=result.returncode,
                           stdout=result.stdout, stderr=result.stderr, expectation=expectation)
            except subprocess.TimeoutExpired:
                row = dict(name=name, argv=argv, exit_code=124, stdout="", stderr="command timed out", expectation=expectation)
            row["seconds"] = round(time.monotonic() - start, 3)
            if expectation == "expected_refusal":
                row["passed"] = (row["exit_code"] == 1 and
                                 "verification requires assertions; optimized Python is not supported" in row["stderr"])
            elif expectation == "json_compare":
                expected = json.loads((ROOT / FOLDER / "arithmetic-transport-independent.json").read_text(encoding="utf-8"))
                try:
                    row["passed"] = row["exit_code"] == 0 and json.loads(row["stdout"]) == expected
                except json.JSONDecodeError:
                    row["passed"] = False
            else:
                row["passed"] = row["exit_code"] == 0
            receipt["commands"].append(row)
            print("PASS" if row["passed"] else "FAIL", name,
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
        args.receipt.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("PASS" if receipt["success"] else "FAIL", "global-closure bundle; global premises remain open", flush=True)
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
