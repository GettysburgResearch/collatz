#!/usr/bin/env python3
"""Compile each local Lean module and check every requested #print axioms report.

Run from a Mathlib project with its environment, e.g.
    lake env python3 /path/to/replay_lean.py --mathlib .
An optional source directory may contain additional standalone modules.
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


ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
PRINT = re.compile(r"^#print\s+axioms\s+([\w.']+)\s*$", re.MULTILINE)
IMPORT = re.compile(r"^(?:public\s+)?import\s+([\w.]+)\s*$", re.MULTILINE)
RESULT = re.compile(r"^'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)$")


def dependency_order(files):
    by_name = {path.stem: path for path in files}
    waiting = {
        name: {dep for dep in IMPORT.findall(path.read_text()) if dep in by_name}
        for name, path in by_name.items()
    }
    order = []
    while waiting:
        available = sorted(name for name, deps in waiting.items() if not deps)
        if not available:
            raise ValueError(f"module import cycle: {sorted(waiting)}")
        for name in available:
            order.append(by_name[name])
            del waiting[name]
        for deps in waiting.values():
            deps.difference_update(available)
    return order


def check_output(source, output):
    requested = PRINT.findall(source)
    reports = {}
    for line in output.splitlines():
        if not line.strip():
            continue
        match = RESULT.fullmatch(line)
        if not match:
            raise ValueError(f"unexpected Lean output: {line}")
        declaration, raw = match.groups()
        axioms = [item.strip() for item in (raw or "").split(",") if item.strip()]
        if declaration in reports or set(axioms) - ALLOWED_AXIOMS:
            raise ValueError(f"duplicate declaration or unexpected axiom: {line}")
        reports[declaration] = axioms
    if not requested or len(requested) != len(reports):
        raise ValueError(f"expected {len(requested)} axiom reports, received {len(reports)}")
    for name in requested:
        matches = [decl for decl in reports if decl == name or decl.endswith("." + name)]
        if len(matches) != 1:
            raise ValueError(f"no unique axiom report for {name}")
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--lean", default="lean", help="Lean executable in the Mathlib environment")
    parser.add_argument("--mathlib", type=Path, help="Mathlib checkout whose git revision will be recorded")
    parser.add_argument("--receipt", type=Path, help="write the JSON result to this file")
    args = parser.parse_args()
    root = args.source_dir.resolve()
    sources = dependency_order(sorted(root.glob("*.lean")))
    if not sources:
        parser.error(f"no Lean modules in {root}")
    version = subprocess.check_output([args.lean, "--version"], text=True).strip()
    githash = subprocess.check_output([args.lean, "--githash"], text=True).strip()
    result = {"lean": version, "lean_git_commit": githash, "warning_as_error": True,
              "auto_implicit": False, "modules": []}
    if args.mathlib:
        result["mathlib_git_commit"] = subprocess.check_output(
            ["git", "-C", str(args.mathlib), "rev-parse", "HEAD"], text=True
        ).strip()
    with tempfile.TemporaryDirectory(prefix="collatz-lean-") as tmp:
        env = os.environ.copy()
        env["LEAN_PATH"] = os.pathsep.join(filter(None, (tmp, env.get("LEAN_PATH"))))
        for path in sources:
            output = Path(tmp) / (path.stem + ".olean")
            process = subprocess.run(
                [args.lean, "-j1", "-DwarningAsError=true", "-DautoImplicit=false",
                 "-R", str(root), "-o", str(output), str(path)],
                capture_output=True, text=True, env=env
            )
            if process.returncode:
                sys.stderr.write(process.stdout + process.stderr)
                raise SystemExit(process.returncode)
            if not output.is_file():
                raise RuntimeError(f"missing compiled module for {path.name}")
            reports = check_output(path.read_text(), process.stdout + process.stderr)
            result["modules"].append({
                "file": path.name,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "axioms": reports,
            })
            print(f"{path.name} passed ({len(reports)} axiom reports)", file=sys.stderr, flush=True)
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.receipt:
        args.receipt.write_text(text)
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
