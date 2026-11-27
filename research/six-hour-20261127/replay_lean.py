#!/usr/bin/env python3
"""Rebuild every Lean module in this packet and check every local theorem's axioms.

Reuses the version-pinned external Mathlib build, rebuilding the two listed
missing dependency modules from unchanged pinned sources in a temporary mirror.
Local modules are compiled in import dependency order. No project oleans are reused. Compilation and audit failures are fatal under
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
DECLARATION = re.compile(r"^(?:private\s+)?theorem\s+([\w.']+)", re.MULTILINE)
REQUEST = re.compile(r"^#print\s+axioms\s+([\w.']+)\s*$", re.MULTILINE)
REPORT = re.compile(r"^'([^']+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)$")
FLAGS = ["-j1", "-DwarningAsError=true", "-DautoImplicit=false", "--json"]
REBUILD_DEPENDENCIES = [
    "Mathlib/Algebra/Order/GroupWithZero/Action/Synonym",
    "Mathlib/Topology/Connected/TotallyDisconnected",
]


def output(command):
    return subprocess.check_output(command, text=True).strip()


def parse_audits(source, lean_output):
    requested = [n.rsplit(".", 1)[-1] for n in REQUEST.findall(source)]
    declarations = [n.rsplit(".", 1)[-1] for n in DECLARATION.findall(source)]
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
    # Local module names are deliberately unique and compiled into one fresh root.
    by_name = {p.stem: p for p in sources}
    dependencies = {}
    for p in sources:
        names = [name for line in re.findall(r"^import\s+(.+)$", p.read_text(), re.MULTILINE)
                 for name in line.split()]
        dependencies[p] = {by_name[name] for name in names if name in by_name}
    pending, ordered = set(sources), []
    while pending:
        ready = sorted(p for p in pending if not (dependencies[p] & pending))
        if not ready:
            raise SystemExit("cyclic local Lean imports")
        ordered.extend(ready)
        pending.difference_update(ready)
    sources = ordered
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
        "rebuilt_dependencies": [],
        "modules": [],
    }
    with tempfile.TemporaryDirectory(prefix="collatz-six-hour-lean-") as tmp:
        destination = Path(tmp)
        dependency_root = destination / "dependencies"
        # Lean resolves a module root from the first matching search directory.
        # Mirror the pinned cache with file symlinks, then fill only the two
        # missing dependency objects from their unchanged pinned sources.
        for original in olean_root.rglob("*"):
            relative = original.relative_to(olean_root)
            target = dependency_root / relative
            if original.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            elif not any(relative.as_posix().startswith(module + ".")
                         for module in REBUILD_DEPENDENCIES):
                target.parent.mkdir(parents=True, exist_ok=True)
                target.symlink_to(original)
        env = dict(os.environ)
        env["LEAN_PATH"] = os.pathsep.join(
            str(p) for p in (destination, dependency_root, olean_root, *packages))
        for module in REBUILD_DEPENDENCIES:
            source = mathlib / (module + ".lean")
            target = dependency_root / (module + ".olean")
            target.parent.mkdir(parents=True, exist_ok=True)
            command = [args.lean, *FLAGS, "-R", str(mathlib),
                       "-o", str(target), str(source)]
            result = subprocess.run(command, env=env, text=True, capture_output=True,
                                    cwd=mathlib)
            if result.returncode or result.stdout or result.stderr:
                sys.stderr.write(result.stdout + result.stderr)
                raise SystemExit(result.returncode or 1)
            if not target.is_file():
                raise RuntimeError(f"missing dependency object: {module}")
            receipt["rebuilt_dependencies"].append({
                "path": module + ".lean",
                "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "exit_code": result.returncode,
            })
            print(f"{module}: pinned dependency rebuilt", file=sys.stderr, flush=True)
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
