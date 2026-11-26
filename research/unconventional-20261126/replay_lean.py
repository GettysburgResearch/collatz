#!/usr/bin/env python3
"""Rebuild every Lean module in this packet and check every local theorem's axioms.

Uses the version-pinned external Mathlib build; does not rebuild Mathlib itself.
No project oleans are reused. Compilation and audit failures are fatal under
both normal and optimized Python. Receipts contain the exact source identities.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
DECLARATION = re.compile(r"^(?:private\s+)?theorem\s+([\w']+)", re.MULTILINE)
REQUEST = re.compile(r"^#print\s+axioms\s+([\w.']+)\s*$", re.MULTILINE)
REPORT = re.compile(r"^'([^']+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)$")
FLAGS = ["-j1", "-DwarningAsError=true", "-DautoImplicit=false", "--json"]


def output(command):
    return subprocess.check_output(command, text=True).strip()


def parse_audits(source, lean_output):
    requested = [n.rsplit(".", 1)[-1] for n in REQUEST.findall(source)]
    declarations = DECLARATION.findall(source)
    if not declarations or sorted(requested) != sorted(declarations):
        raise ValueError("local theorems and axiom-audit requests differ")
    if len(set(requested)) != len(requested):
        raise ValueError("duplicate axiom-audit request")
    reports = {}
    for line in lean_output.splitlines():
        if not line.strip():
            continue
        message = json.loads(line)
        if message.get("severity") != "information":
            raise ValueError(f"unexpected Lean diagnostic: {message}")
        match = REPORT.fullmatch(message["data"].strip())
        if not match:
            raise ValueError(f"unexpected Lean information: {message['data']}")
        name, dependencies = match.groups()
        axioms = [a.strip() for a in (dependencies or "").split(",") if a.strip()]
        if name in reports or set(axioms) - ALLOWED:
            raise ValueError(f"duplicate report or unapproved axiom: {message['data']}")
        reports[name] = axioms
    if sorted(n.rsplit(".", 1)[-1] for n in reports) != sorted(requested):
        raise ValueError("compiler reports differ from the requested local theorems")
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--lean", default="lean")
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    mathlib = args.mathlib.resolve()
    lean_commit = output([args.lean, "--githash"])
    mathlib_commit = output(["git", "-C", str(mathlib), "rev-parse", "HEAD"])
    if (lean_commit, mathlib_commit) != (LEAN_COMMIT, MATHLIB_COMMIT):
        raise SystemExit(f"dependency pin mismatch: {lean_commit}, {mathlib_commit}")
    if output(["git", "-C", str(mathlib), "status", "--porcelain", "--untracked-files=no"]):
        raise SystemExit("tracked Mathlib sources are dirty")
    sources = sorted(root.rglob("*.lean"))
    if not sources or len({p.name for p in sources}) != len(sources):
        raise SystemExit("missing modules or duplicate module basenames")
    olean_root = mathlib / ".lake/build/lib/lean"
    if not (olean_root / "Mathlib.olean").is_file():
        raise SystemExit("the pinned external Mathlib build is unavailable")
    packages = sorted(mathlib.glob(".lake/packages/*/.lake/build/lib/lean"))
    receipt = {
        "lean": output([args.lean, "--version"]),
        "lean_commit": lean_commit,
        "mathlib_commit": mathlib_commit,
        "flags": FLAGS,
        "dependency_scope": "precompiled pinned Mathlib; every project module rebuilt",
        "modules": [],
    }
    with tempfile.TemporaryDirectory(prefix="collatz-unconventional-lean-") as tmp:
        destination = Path(tmp)
        env = dict(os.environ)
        env["LEAN_PATH"] = os.pathsep.join(str(p) for p in (destination, olean_root, *packages))
        for source in sources:
            data = source.read_bytes()
            target = destination / source.with_suffix(".olean").name
            command = [args.lean, *FLAGS, "-R", str(source.parent), "-o", str(target), str(source)]
            result = subprocess.run(command, env=env, text=True, capture_output=True)
            if result.returncode or result.stderr:
                sys.stderr.write(result.stdout + result.stderr)
                raise SystemExit(result.returncode or 1)
            if not target.is_file() or target.stat().st_size == 0:
                raise RuntimeError(f"no compiled object for {source.name}")
            audits = parse_audits(data.decode("utf-8"), result.stdout)
            relative = source.relative_to(root).as_posix()
            receipt["modules"].append({
                "path": relative,
                "sha256": hashlib.sha256(data).hexdigest(),
                "axioms": audits,
            })
            print(f"{relative}: {len(audits)} theorem audits passed", file=sys.stderr, flush=True)
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        for key in ("lean_commit", "mathlib_commit", "flags", "modules"):
            if receipt[key] != expected[key]:
                raise SystemExit(f"receipt mismatch in {key}")
    serialized = json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
    if args.receipt:
        args.receipt.write_text(serialized, encoding="utf-8")
    else:
        sys.stdout.write(serialized)


if __name__ == "__main__":
    main()
