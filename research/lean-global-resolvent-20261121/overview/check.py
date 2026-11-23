#!/usr/bin/env python3
"""Reproduce the checkpoint-6 proof chain and audit in a new output directory."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time


LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--dependency-cache", type=Path,
                        help="Optional fast mirror; every supplied artifact is compared byte-for-byte")
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    packet = base.parent
    core = packet / "lean"
    section = packet / "section/lean"
    local = base / "lean"
    jobs = [
        (core, "Collatz.ReverseBasin146"),
        (core, "Collatz.Closure"),
        (core, "Collatz.TerminalCarry"),
        (core, "Collatz.TerminalCarryClosure"),
        (local, "AuditCoreOverview"),
        (section, "ShellCover"),
        (section, "ForwardSection"),
        (section, "BandSteering"),
        (section, "Integer306"),
        (section, "FastForward"),
        (local, "InverseOddBudget"),
        (local, "AuditOverview"),
    ]
    mathlib, lean, out = args.mathlib.resolve(), args.lean.resolve(), args.out.resolve()
    receipt = args.receipt.resolve()
    if out.exists() and any(out.iterdir()):
        parser.error("--out must be absent or empty")
    out.mkdir(parents=True, exist_ok=True)
    receipt.parent.mkdir(parents=True, exist_ok=True)
    actual_lean = subprocess.check_output([str(lean), "--githash"], text=True).strip()
    actual_mathlib = subprocess.check_output(
        ["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip()
    if actual_lean != LEAN_COMMIT or actual_mathlib != MATHLIB_COMMIT:
        parser.error("Lean and Mathlib must match the documented exact pins")
    source_files = [root / (name.replace(".", "/") + ".lean") for root, name in jobs]
    before = {str(p.relative_to(packet)): sha256(p) for p in source_files}
    pins = json.loads((packet / "section/upstream-pins.json").read_text())
    for name in ("ShellCover.lean", "ForwardSection.lean"):
        if sha256(section / name) != pins["sha256"][name]:
            parser.error(f"Frozen upstream source differs: {name}")
    paths = [out, mathlib / ".lake/build/lib/lean"]
    paths += sorted(p / ".lake/build/lib/lean" for p in (mathlib / ".lake/packages").iterdir()
                    if (p / ".lake/build/lib/lean").is_dir())
    verified_cache_files = 0
    if args.dependency_cache:
        cache = args.dependency_cache.resolve()
        for cached in sorted(cache.rglob("*")):
            if not cached.is_file() or not cached.name.endswith(
                    (".olean", ".olean.private", ".olean.server", ".ir")):
                continue
            relative = cached.relative_to(cache)
            originals = [root / relative for root in paths[1:] if (root / relative).is_file()]
            if not originals or sha256(originals[0]) != sha256(cached):
                parser.error(f"Dependency mirror mismatch: {relative}")
            verified_cache_files += 1
        paths.insert(1, cache)
    env = os.environ.copy()
    env["LEAN_PATH"] = os.pathsep.join(map(str, paths))
    result = {
        "schema": "collatz-whole-repository-new-proofs/v1",
        "scope": "Finite theorems and their exact imports; full Collatz remains open",
        "lean_commit": actual_lean,
        "mathlib_commit": actual_mathlib,
        "source_sha256_before": before,
        "fresh_output_directory": str(out),
        "verified_dependency_mirror_files": verified_cache_files,
        "commands": [],
        "success": False,
    }
    for (root, name), source in zip(jobs, source_files, strict=True):
        output = out / (name.replace(".", "/") + ".olean")
        output.parent.mkdir(parents=True, exist_ok=True)
        argv = [str(lean), "-j1", "--root=" + str(root), "-DwarningAsError=true",
                "-o", str(output), str(source)]
        start = time.monotonic()
        proc = subprocess.run(argv, env=env, text=True, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, check=False)
        row = {"module": name, "argv": argv, "exit_code": proc.returncode,
               "seconds": round(time.monotonic() - start, 3), "output": proc.stdout}
        result["commands"].append(row)
        receipt.write_text(json.dumps(result, indent=2) + "\n")
        print(f"{name}: exit {proc.returncode}, {row['seconds']}s", flush=True)
        if proc.returncode or "sorryAx" in proc.stdout:
            print(proc.stdout, flush=True)
            return 1
    after = {str(p.relative_to(packet)): sha256(p) for p in source_files}
    audit = "\n".join(row["output"] for row in result["commands"]
                      if row["module"] in {"AuditCoreOverview", "AuditOverview"})
    actual_count = audit.count("depends on axioms:") + audit.count("does not depend on any axioms")
    expected_count = sum((local / (name + ".lean")).read_text().count("#print axioms ")
                         for name in ("AuditCoreOverview", "AuditOverview"))
    axioms = {name.strip() for group in re.findall(
        r"depends on axioms:\s*\[([^\]]*)\]", audit, re.S)
        for name in group.split(",") if name.strip()}
    result.update({
        "source_sha256_after": after,
        "sources_unchanged": before == after,
        "audited_theorems": actual_count,
        "expected_audits": expected_count,
        "axiom_union": sorted(axioms),
        "success": before == after and actual_count == expected_count
                   and axioms <= {"propext", "Classical.choice", "Quot.sound"},
    })
    receipt.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Audited {actual_count} theorems; success: {result['success']}", flush=True)
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
