#!/usr/bin/env python3
"""Freshly replay checkpoint 11 and its exact project dependency closure."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--dependency-cache", type=Path,
                        help="Optional mirror; every object/IR artifact is authenticated")
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    repo = base.parents[3]
    manifest = json.loads((base / "DEPENDENCIES.json").read_text())
    jobs = manifest["jobs"]
    sources = [repo / row["path"] for row in jobs]
    for row, source in zip(jobs, sources, strict=True):
        if sha256(source) != row["sha256"]:
            parser.error("Pinned source mismatch: " + row["module"])
    lean, mathlib = args.lean.resolve(), args.mathlib.resolve()
    out, receipt = args.out.resolve(), args.receipt.resolve()
    if out.exists() and any(out.iterdir()):
        parser.error("--out must be absent or empty")
    out.mkdir(parents=True, exist_ok=True)
    receipt.parent.mkdir(parents=True, exist_ok=True)
    actual_lean = subprocess.check_output([str(lean), "--githash"], text=True).strip()
    actual_mathlib = subprocess.check_output(
        ["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip()
    if actual_lean != manifest["lean_commit"] or actual_mathlib != manifest["mathlib_commit"]:
        parser.error("Lean and Mathlib must match the documented exact pins")
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
                parser.error("Dependency mirror mismatch: " + str(relative))
            verified_cache_files += 1
        paths.insert(1, cache)
    env = os.environ.copy()
    env["LEAN_PATH"] = os.pathsep.join(map(str, paths))
    before = {row["path"]: sha256(source) for row, source in zip(jobs, sources, strict=True)}
    result = {
        "schema": "collatz-central-attempt-checkpoint11-execution/v1",
        "scope": "Two obstruction results: 14 audited statements and their exact imports; no positive global closing estimate; full Collatz remains open",
        "lean_commit": actual_lean, "mathlib_commit": actual_mathlib,
        "source_sha256_before": before,
        "fresh_output_directory": str(out),
        "verified_dependency_mirror_files": verified_cache_files,
        "commands": [], "success": False,
    }
    for row, source in zip(jobs, sources, strict=True):
        name = row["module"]
        output = out / (name.replace(".", "/") + ".olean")
        output.parent.mkdir(parents=True, exist_ok=True)
        argv = [str(lean), "-j1", "--root=" + str(repo / row["root"]),
                "-DwarningAsError=true", "-o", str(output), str(source)]
        start = time.monotonic()
        proc = subprocess.run(argv, env=env, text=True, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, check=False)
        command = {"module": name, "argv": argv, "exit_code": proc.returncode,
                   "seconds": round(time.monotonic() - start, 3), "output": proc.stdout}
        result["commands"].append(command)
        receipt.write_text(json.dumps(result, indent=2) + "\n")
        print(f"{name}: exit {proc.returncode}, {command['seconds']}s", flush=True)
        if proc.returncode or "sorryAx" in proc.stdout:
            print(proc.stdout, flush=True)
            return 1
    after = {row["path"]: sha256(source) for row, source in zip(jobs, sources, strict=True)}
    audit_rows = [row for row in result["commands"] if row["module"] in manifest["audit_modules"]]
    audit = "\n".join(row["output"] for row in audit_rows)
    counts = {row["module"]: row["output"].count("depends on axioms:")
              + row["output"].count("does not depend on any axioms") for row in audit_rows}
    axioms = {name.strip() for group in re.findall(
        r"depends on axioms:\s*\[([^\]]*)\]", audit, re.S)
        for name in group.split(",") if name.strip()}
    result.update({
        "source_sha256_after": after, "sources_unchanged": before == after,
        "audit_counts": counts, "expected_audit_counts": manifest["audit_modules"],
        "audited_theorems": sum(counts.values()), "axiom_union": sorted(axioms),
        "success": before == after and counts == manifest["audit_modules"]
                   and axioms <= {"propext", "Classical.choice", "Quot.sound"},
    })
    receipt.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Audited {sum(counts.values())} theorems; success: {result['success']}", flush=True)
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
