#!/usr/bin/env python3
"""Rebuild the three Lean proofs in isolation and replay the exact finite controls."""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

SOURCE = Path(__file__).resolve().parent
IMPORT = re.compile(r"^\s*(?:public\s+)?(?:meta\s+)?import(?:\s+all)?\s+(Mathlib\.[\w.']+)", re.M)
PROOFS = ("FiniteTrace", "HeckeRank", "CutoffRank")
AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def run(command, **kwargs):
    return subprocess.run(command, text=True, check=True, **kwargs)


def build_missing(lean, mathlib, output, env, jobs):
    cache = mathlib / ".lake/build/lib/lean"
    # Lean resolves a module tree in the first available root. Retain entries
    # from a partial shared cache while compiling only missing mathlib modules.
    run(["cp", "-as", cache / "Mathlib", output / "Mathlib"])
    needed = {}
    visited = set()

    def visit(module):
        if module in visited:
            return
        visited.add(module)
        relative = Path(*module.split("."))
        if (output / relative.with_suffix(".olean")).exists():
            return
        source = mathlib / relative.with_suffix(".lean")
        dependencies = set(IMPORT.findall(source.read_text()))
        needed[module] = dependencies
        for dependency in dependencies:
            visit(dependency)

    for name in PROOFS:
        for module in IMPORT.findall((SOURCE / f"{name}.lean").read_text()):
            visit(module)

    def compile_one(module):
        relative = Path(*module.split("."))
        target = output / relative.with_suffix(".olean")
        target.parent.mkdir(parents=True, exist_ok=True)
        run([lean, "-o", target, relative.with_suffix(".lean")], cwd=mathlib, env=env)

    print(f"Building {len(needed)} missing mathlib dependencies", flush=True)
    running = {}
    with futures.ThreadPoolExecutor(jobs) as pool:
        while needed or running:
            pending = set(needed) | set(running.values())
            for module in list(needed):
                if len(running) >= jobs:
                    break
                if needed[module].isdisjoint(pending):
                    running[pool.submit(compile_one, module)] = module
                    del needed[module]
            if not running:
                raise RuntimeError("Unresolved mathlib dependency cycle")
            completed, _ = futures.wait(running, return_when=futures.FIRST_COMPLETED)
            for task in completed:
                task.result()
                del running[task]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path, help="Lean 4.34.1 executable")
    parser.add_argument("--mathlib", required=True, type=Path, help="mathlib source checkout with cached dependencies")
    parser.add_argument("--jobs", default=2, type=int)
    parser.add_argument("--temp-root", type=Path, help="parent directory for the disposable build")
    args = parser.parse_args()
    lean, mathlib = args.lean.resolve(), args.mathlib.resolve()
    if args.jobs < 1:
        parser.error("--jobs must be positive")
    controls = run([sys.executable, SOURCE / "finite_controls.py"], capture_output=True).stdout
    if controls != (SOURCE / "FINITE_CONTROLS.json").read_text():
        raise RuntimeError("Finite replay differs from the saved exact controls")
    run([lean, "--version"])
    with tempfile.TemporaryDirectory(dir=args.temp_root) as temp:
        output = Path(temp)
        paths = [output, mathlib / ".lake/build/lib/lean",
                 *(mathlib / ".lake/packages").glob("*/.lake/build/lib/lean")]
        env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, paths)))
        build_missing(lean, mathlib, output, env, args.jobs)
        for name in PROOFS:
            result = run([lean, "-DwarningAsError=true", "-o", output / f"{name}.olean",
                          f"{name}.lean"], cwd=SOURCE, env=env, capture_output=True)
            print(result.stdout, end="")
            if name == "CutoffRank":
                inventories = re.findall(r"depends on axioms: \[([^]]*)\]", result.stdout)
                if len(inventories) != 5 or any(set(row.split(", ")) - AXIOMS for row in inventories):
                    raise RuntimeError("Unexpected public theorem axiom inventory")
    print("Three Lean modules and exact finite controls passed.")


if __name__ == "__main__":
    main()
