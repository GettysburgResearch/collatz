#!/usr/bin/env python3
"""Compile the seven regularity-rigidity modules, then verify their transitive axiom reports."""

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
SOURCES = (
    "LeanCore.lean",
    "continuation/ReturnRigidity.lean",
    "pointwise-fibers/PointwiseFiber.lean",
    "pointwise-fibers/OrdinaryFiber.lean",
    "pointwise-fibers/RelativeState.lean",
    "pointwise-fibers/FinitePressure.lean",
    "pointwise-fibers/TwoBlockRouter.lean",
)
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
DECLARATION = re.compile(r"^(?:private\s+)?theorem\s+([\w']+)", re.MULTILINE)
REQUEST = re.compile(r"^#print\s+axioms\s+([\w.']+)\s*$", re.MULTILINE)
REPORT = re.compile(r"^'([^']+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)$")
FLAGS = ["-j1", "-DwarningAsError=true", "-DautoImplicit=false", "--json"]


def checked_output(args):
    return subprocess.check_output(args, text=True).strip()


def axiom_reports(source, lean_output):
    requested = REQUEST.findall(source)
    declarations = DECLARATION.findall(source)
    if not declarations or sorted(requested) != sorted(declarations) or len(set(requested)) != len(requested):
        raise ValueError("the local theorem list and the #print axioms requests differ")
    reports = {}
    for line in lean_output.splitlines():
        if not line.strip():
            continue
        message = json.loads(line)
        if message.get("severity") != "information":
            raise ValueError(f"unexpected Lean message: {message}")
        match = REPORT.fullmatch(message["data"].strip())
        if match is None:
            raise ValueError(f"unexpected Lean information: {message['data']}")
        name, dependencies = match.groups()
        axioms = [a.strip() for a in (dependencies or "").split(",") if a.strip()]
        if name in reports or set(axioms) - ALLOWED:
            raise ValueError(f"duplicate report or unexpected axiom: {message['data']}")
        reports[name] = axioms
    # Private names include the logical module name. Match against terminal components.
    if sorted(name.rsplit(".", 1)[-1] for name in reports) != sorted(requested):
        raise ValueError("compiler reports differ from the requested theorem list")
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True, help="the pinned Mathlib checkout with cached oleans")
    parser.add_argument("--lean", default="lean", help="Lean executable (default from PATH)")
    parser.add_argument("--receipt", type=Path, help="write JSON here (default stdout)")
    parser.add_argument("--check", type=Path, help="compare module hashes, axiom lists, flags, and version pins")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    mathlib = args.mathlib.resolve()
    lean_hash = checked_output([args.lean, "--githash"])
    mathlib_hash = checked_output(["git", "-C", str(mathlib), "rev-parse", "HEAD"])
    if (lean_hash, mathlib_hash) != (LEAN_COMMIT, MATHLIB_COMMIT):
        raise SystemExit(f"dependency pin mismatch: Lean {lean_hash}, Mathlib {mathlib_hash}")
    mathlib_oleans = mathlib / ".lake/build/lib/lean"
    if not (mathlib_oleans / "Mathlib.olean").is_file():
        raise SystemExit(f"expected cached Mathlib oleans in {mathlib_oleans}")
    packages = sorted(mathlib.glob(".lake/packages/*/.lake/build/lib/lean"))
    receipt = {
        "lean": checked_output([args.lean, "--version"]),
        "lean_commit": lean_hash,
        "mathlib_commit": mathlib_hash,
        "flags": FLAGS,
        "modules": [],
    }
    with tempfile.TemporaryDirectory(prefix="collatz-regularity-lean-") as tmp:
        output = Path(tmp)
        env = dict(os.environ)
        env["LEAN_PATH"] = os.pathsep.join(str(path) for path in (output, mathlib_oleans, *packages))
        for relative in SOURCES:
            path = root / relative
            data = path.read_bytes()
            olean = output / path.with_suffix(".olean").name
            command = [args.lean, *FLAGS, "-R", str(path.parent), "-o", str(olean), str(path)]
            result = subprocess.run(command, text=True, capture_output=True, env=env)
            if result.returncode or result.stderr:
                sys.stderr.write(result.stdout + result.stderr)
                raise SystemExit(result.returncode or 1)
            if not olean.is_file() or olean.stat().st_size == 0:
                raise RuntimeError(f"missing compiled output for {relative}")
            reports = axiom_reports(data.decode("utf-8"), result.stdout)
            receipt["modules"].append({
                "path": relative,
                "sha256": hashlib.sha256(data).hexdigest(),
                "axioms": reports,
            })
            print(f"{relative} passed ({len(reports)} theorems)", file=sys.stderr, flush=True)
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        for key in ("lean_commit", "mathlib_commit", "flags", "modules"):
            if expected[key] != receipt[key]:
                raise SystemExit(f"receipt mismatch in {key}")
    text = json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
    if args.receipt:
        args.receipt.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
