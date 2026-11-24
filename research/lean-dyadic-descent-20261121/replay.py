#!/usr/bin/env python3
"""Rebuild the pinned Collatz section and the new Lean results sequentially.

Provide a populated mathlib checkout and the Lean 4.34.1 bin directory.
Build outputs and receipts are deliberately placed outside the repository.
The receipt distinguishes proof checking from the repository integrity gate.
"""

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time


MATHLIB = "d13f23b723b8a846827a245b89c10fc7d3f11612"
UPSTREAM = {
    "ShellCover": "76477e195c733e8b8c9fdf523d954d85375b3ac244ee0590127192743bffc88c",
    "ForwardSection": "f134020b95f79c3b90cfe104c7d4234ee8d162c97acaa02c6aefc6ec86d19ae4",
    "SectionDynamics": "94c05e9cfc738b319acb52e9c6f07b0344dc87cb31ed4ed49cb2540fde51c9ac",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--lean-bin", required=True, type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    out = (args.out or Path(tempfile.mkdtemp(prefix="collatz-dyadic-replay-"))).resolve()
    if out == root or root in out.parents:
        parser.error("--out must be outside the repository")
    out.mkdir(parents=True, exist_ok=True)
    mathlib = args.mathlib.resolve()
    lean_bin = args.lean_bin.resolve()
    head = subprocess.check_output(["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip()
    if head != MATHLIB:
        raise RuntimeError(f"mathlib pin mismatch: {head}")
    sources = []
    for module, expected in UPSTREAM.items():
        path = here.parent / "lean-shell-cover" / (module + ".lean")
        if digest(path) != expected:
            raise RuntimeError(f"upstream source pin mismatch: {module}")
        sources.append(path)
    sources += [here / (name + ".lean") for name in
                ["OffsetDescent", "MarkedOffsetReturn", "PhaseFrequency"]]
    if (here / "InfiniteDescent.lean").exists():
        sources.append(here / "InfiniteDescent.lean")
    before = {str(p.relative_to(root)): digest(p) for p in sources}
    env = os.environ.copy()
    env["PATH"] = str(lean_bin) + os.pathsep + env.get("PATH", "")
    env["LEAN_PATH"] = str(out)
    version = subprocess.check_output([str(lean_bin / "lean"), "--version"], text=True).strip()
    if "version 4.34.1," not in version:
        raise RuntimeError(f"Lean version mismatch: {version}")
    receipt = {"scope": "Lean proof checking at pinned sources; not a proof of full Collatz",
               "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "lean_version": version, "mathlib_commit": head,
               "source_sha256": before, "commands": [], "success": False}
    try:
        for path in sources:
            argv = [str(lean_bin / "lake"), "env", "lean", "-j1", "-R", str(path.parent),
                    "-DwarningAsError=true", "-o", str(out / (path.stem + ".olean")), str(path)]
            print(f"Checking {path.name}", flush=True)
            started = time.monotonic()
            proc = subprocess.run(argv, cwd=mathlib, env=env, text=True, capture_output=True, timeout=900)
            log = proc.stdout + proc.stderr
            (out / (path.stem + ".log")).write_text(log, encoding="utf-8")
            receipt["commands"].append({"source": str(path.relative_to(root)),
                                         "argv": argv, "exit_code": proc.returncode,
                                         "seconds": round(time.monotonic() - started, 3),
                                         "stdout": proc.stdout, "stderr": proc.stderr})
            print(f"{path.name}: exit {proc.returncode}", flush=True)
            if proc.returncode:
                print(log, flush=True)
                raise RuntimeError(f"Lean rejected {path.name}")
            if "sorryAx" in log:
                raise RuntimeError(f"admitted theorem in axiom audit: {path.name}")
            allowed = {"propext", "Classical.choice", "Quot.sound"}
            for found in re.findall(r"depends on axioms: \[([^]]*)\]", log):
                names = {name.strip() for name in found.split(",") if name.strip()}
                if names - allowed:
                    raise RuntimeError(f"unexpected axioms in {path.name}: {sorted(names - allowed)}")
        after = {str(p.relative_to(root)): digest(p) for p in sources}
        receipt["sources_unchanged"] = before == after
        if before != after:
            raise RuntimeError("source files changed during compilation")
        receipt["success"] = True
    finally:
        receipt["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        (out / "lean-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        print(f"Receipt: {out / 'lean-receipt.json'}", flush=True)


if __name__ == "__main__":
    main()
