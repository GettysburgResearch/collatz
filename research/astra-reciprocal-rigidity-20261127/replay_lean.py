#!/usr/bin/env python3
"""Rebuild this packet's Lean files from fresh local oleans and record scope.

Mathlib and its package cache must already be built at the pinned revision.
This script does not install dependencies or admit missing proofs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

MATHLIB_PIN = "d13f23b723b8a846827a245b89c10fc7d3f11612"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--dependency-overlay", type=Path,
                        help="optional additional cache built from the same pinned mathlib source")
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--modules", nargs="*")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    lean, mathlib = args.lean.resolve(), args.mathlib.resolve()
    pin = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib, text=True).strip()
    if pin != MATHLIB_PIN:
        raise SystemExit(f"wrong mathlib revision: {pin}")
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if "4.34.1" not in version:
        raise SystemExit(f"wrong Lean version: {version}")
    files = sorted(p for p in root.rglob("*.lean") if not any(v.startswith(".") for v in p.relative_to(root).parts))
    by_name = {p.stem: p for p in files}
    if len(by_name) != len(files):
        raise SystemExit("duplicate local module names")
    dependencies = {}
    for name, path in by_name.items():
        imports = re.findall(r"^import\s+([^\n]+)", path.read_text(), re.M)
        dependencies[name] = {v for row in imports for v in row.split() if v in by_name}
    ordered, visiting = [], set()

    def visit(name: str) -> None:
        if name in ordered:
            return
        if name in visiting:
            raise SystemExit("cyclic local imports")
        if name not in by_name:
            raise SystemExit(f"unknown requested module: {name}")
        visiting.add(name)
        for child in sorted(dependencies[name]):
            visit(child)
        visiting.remove(name)
        ordered.append(name)

    for name in args.modules or sorted(by_name):
        visit(name)
    source_hashes = {name: sha(by_name[name]) for name in ordered}
    rows = []
    success = True
    started = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with tempfile.TemporaryDirectory(prefix="collatz-lean-replay-") as build:
        primary_cache = mathlib / ".lake/build/lib/lean"
        dependency_cache = primary_cache
        if args.dependency_overlay:
            # Lean resolves a namespace at its first directory on LEAN_PATH.
            # A partial Mathlib directory therefore shadows the later complete
            # cache instead of falling through for each missing module. Merge
            # the pinned caches by symlink, preferring the primary cache and
            # admitting only Mathlib files from the supplemental directory.
            dependency_cache = Path(build) / "dependencies"
            dependency_cache.mkdir()
            for source, mathlib_only in ((primary_cache, False),
                                         (args.dependency_overlay.resolve(), True)):
                for file in source.rglob("*"):
                    relative = file.relative_to(source)
                    if mathlib_only and relative.parts[0] != "Mathlib":
                        continue
                    if not file.is_file():
                        continue
                    target = dependency_cache / relative
                    if not target.exists():
                        target.parent.mkdir(parents=True, exist_ok=True)
                        target.symlink_to(file.resolve())
        cache = [Path(build), dependency_cache, *sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))]
        env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, cache)))
        for name in ordered:
            path = by_name[name]
            command = [str(lean), "-j1", "-DautoImplicit=false", "-DwarningAsError=true", "-DElab.async=false", "-o", str(Path(build)/(name+".olean")), path.name]
            t = time.monotonic()
            result = subprocess.run(command, cwd=path.parent, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            axioms = set()
            for group in re.findall(r"depends on axioms:\s*\[([^\]]*)\]", result.stdout):
                axioms.update(v.strip() for v in group.split(",") if v.strip())
            forbidden = sorted(axioms - ALLOWED_AXIOMS)
            unchanged = sha(path) == source_hashes[name]
            ok = result.returncode == 0 and not forbidden and unchanged and "sorryAx" not in result.stdout
            rows.append({"module": name, "path": str(path.relative_to(root)), "sha256": source_hashes[name],
                         "flags": command[1:5], "exit_code": result.returncode, "elapsed_seconds": round(time.monotonic()-t, 3),
                         "printed_axioms": sorted(axioms), "forbidden_axioms": forbidden,
                         "source_unchanged_during_build": unchanged, "output": result.stdout, "passed": ok})
            print(json.dumps({k: rows[-1][k] for k in ("module", "exit_code", "elapsed_seconds", "printed_axioms", "passed")}), flush=True)
            if not ok:
                print(result.stdout, flush=True)
                success = False
                break
    all_unchanged = all(sha(by_name[name]) == digest for name, digest in source_hashes.items())
    success = success and all_unchanged and len(rows) == len(ordered)
    receipt = {"schema": "collatz-lean-packet-replay/v1", "started_utc": started,
               "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "lean_version": version, "mathlib_revision": pin, "requested_modules": ordered,
               "dependency_cache": "merged pinned Mathlib symlinks" if args.dependency_overlay else "primary pinned Mathlib cache",
               "fresh_local_output_directory": True, "source_hashes": source_hashes,
               "all_sources_unchanged": all_unchanged, "modules": rows, "passed": success,
               "scope": "Kernel compilation of the listed finite declarations and their explicit hypotheses; not a proof of Collatz or a replay of external mathematical sources."}
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
    raise SystemExit(0 if success else 1)


if __name__ == "__main__":
    main()
