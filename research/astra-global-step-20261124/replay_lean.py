#!/usr/bin/env python3
"""Compile only this packet's local Lean graph in a new isolated directory."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[2]
PACKET = Path(__file__).resolve().parent
COMPILER = "5045d0056413266e57c625dcd7c365b10e377c52"
MATHLIB = "d13f23b723b8a846827a245b89c10fc7d3f11612"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_order(sources: dict[str, bytes]) -> list[str]:
    """Order local imports without relying on any preexisting local object."""
    pending = set(sources)
    ordered: list[str] = []
    dependencies = {}
    for name, data in sources.items():
        imports = re.findall(r"^(?:public\s+)?import\s+([A-Za-z0-9_.]+)",
                             data.decode("utf-8"), re.MULTILINE)
        dependencies[name] = set(imports) & set(sources)
    while pending:
        ready = sorted(name for name in pending if not dependencies[name] & pending)
        if not ready:
            raise ValueError("local Lean import cycle")
        ordered.extend(ready)
        pending.difference_update(ready)
    return ordered


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--lean-path-file", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    lean, out = args.lean.resolve(), args.output.resolve()
    if out.is_relative_to(ROOT):
        parser.error("--output must be outside the repository")
    if out.exists() and any(out.iterdir()):
        parser.error("--output must be new or empty")
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if "4.34.1" not in version or COMPILER not in version:
        parser.error("the Lean version/commit does not match this checkpoint")
    mathlib_head = subprocess.check_output(
        ["git", "-C", str(args.mathlib.resolve()), "rev-parse", "HEAD"],
        text=True,
    ).strip()
    if mathlib_head != MATHLIB:
        parser.error("the Mathlib commit does not match this checkpoint")
    dep_path = args.lean_path_file.read_text(encoding="utf-8").strip()
    if not dep_path:
        parser.error("the dependency search path is empty")
    sources = {p.stem: p.read_bytes() for p in sorted(PACKET.glob("*.lean"))}
    if not sources:
        parser.error("the research packet has no Lean sources")
    try:
        order = source_order(sources)
    except ValueError as exc:
        parser.error(str(exc))
    out.mkdir(parents=True, exist_ok=True)
    for name, data in sources.items():
        (out / (name + ".lean")).write_bytes(data)
    env = dict(os.environ, LEAN_PATH=str(out) + os.pathsep + dep_path)
    receipt = {
        "schema": "collatz-global-step-lean-replay/v1",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "lean_version_output": version,
        "mathlib_commit": mathlib_head,
        "module_order": order,
        "builds": [],
        "success": False,
    }
    receipt_path = out / "LEAN_REPLAY.json"
    for name in order:
        command = [str(lean), "-j1", "-DwarningAsError=true", "-o",
                   name + ".olean", name + ".lean"]
        print("BUILD", name, flush=True)
        result = subprocess.run(command, cwd=out, env=env, text=True,
                                encoding="utf-8", capture_output=True)
        audits = re.findall(r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]",
                            result.stdout)
        expected_count = len(re.findall(r"^#print axioms\s+", sources[name].decode(),
                                        re.MULTILINE))
        unexpected = sorted({a.strip() for _, report in audits
                             for a in report.split(",") if a.strip()} - ALLOWED_AXIOMS)
        complete = expected_count > 0 and len(audits) == expected_count
        diagnostics = bool(re.search(r"\b(?:warning|error):", result.stdout + result.stderr))
        row = {
            "source": str((PACKET / (name + ".lean")).relative_to(ROOT)),
            "source_sha256": digest(sources[name]),
            "command": command,
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "audited_declarations": [decl for decl, _ in audits],
            "axiom_reports": len(audits),
            "expected_axiom_reports": expected_count,
            "complete_axiom_reports": complete,
            "unexpected_axioms": unexpected,
            "compiler_diagnostics": diagnostics,
        }
        receipt["builds"].append(row)
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        if result.returncode or unexpected or not complete or diagnostics:
            print(result.stdout, end="")
            print(result.stderr, end="")
            print("FAIL", name, "receipt:", receipt_path)
            return 1
    unchanged = all((PACKET / (name + ".lean")).read_bytes() == data
                    for name, data in sources.items())
    receipt["sources_unchanged_during_replay"] = unchanged
    receipt["success"] = unchanged
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print("PASS" if unchanged else "FAIL", len(order), "modules; receipt:", receipt_path)
    return 0 if unchanged else 1


if __name__ == "__main__":
    raise SystemExit(main())
