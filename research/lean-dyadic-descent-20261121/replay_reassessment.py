#!/usr/bin/env python3
"""Freshly check the whole-repository reassessment's three new Lean modules.

All five proof inputs and the complete public-theorem audit are compiled
sequentially. No prebuilt local proof module is reused. Mathlib and Lean are
pinned; the generated files and actual execution receipt stay outside the
checkout. This is separate from repository integrity validation.
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
LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
PINNED = {
    "research/lean-shell-cover/ShellCover.lean":
        "76477e195c733e8b8c9fdf523d954d85375b3ac244ee0590127192743bffc88c",
    "research/lean-dyadic-descent-20261121/OffsetDescent.lean":
        "e0af0b1cbe4c4d90b34272bbbc45f25f6a084072dd17c2eb24be9e31641fde8b",
}
NEW = {
    "CoefficientCounting": "CollatzShell.CoefficientCounting",
    "CoefficientPeaks": "CollatzShell.CoefficientPeaks",
    "CertificateBoundary": "CollatzShell.CertificateBoundary",
}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--lean-bin", required=True, type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    root = packet.parents[1]
    out = (args.out or Path(tempfile.mkdtemp(prefix="collatz-reassessment-"))).resolve()
    if out == root or root in out.parents:
        parser.error("--out must be outside the repository")
    if out.exists() and any(out.iterdir()):
        parser.error("--out must be empty for a fresh build")
    out.mkdir(parents=True, exist_ok=True)
    mathlib, lean_bin = args.mathlib.resolve(), args.lean_bin.resolve()
    head = subprocess.check_output(
        ["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip()
    if head != MATHLIB:
        raise RuntimeError(f"Mathlib pin mismatch: {head}")
    dirty = subprocess.check_output(
        ["git", "-C", str(mathlib), "status", "--porcelain", "--untracked-files=no"], text=True)
    if dirty:
        raise RuntimeError("Mathlib has tracked modifications")
    version = subprocess.check_output([str(lean_bin / "lean"), "--version"], text=True).strip()
    if "version 4.34.1," not in version or LEAN_COMMIT not in version:
        raise RuntimeError(f"Lean pin mismatch: {version}")
    sources = [root / name for name in PINNED] + [packet / f"{name}.lean" for name in NEW]
    for name, expected in PINNED.items():
        if digest(root / name) != expected:
            raise RuntimeError(f"Imported source pin mismatch: {name}")
    hashes = {str(p.relative_to(root)): digest(p) for p in sources}
    declarations = []
    for name, namespace in NEW.items():
        source = (packet / f"{name}.lean").read_text(encoding="utf-8")
        declarations.extend(f"{namespace}.{d}" for d in
                            re.findall(r"^(?:theorem|lemma)\s+([\w']+)", source, re.MULTILINE))
    if not declarations or len(declarations) != len(set(declarations)):
        raise RuntimeError("Invalid public-theorem audit inventory")
    audit = out / "ReassessmentAudit.lean"
    audit.write_text("\n".join([f"import {m}" for m in NEW] +
                               [f"#print axioms {d}" for d in declarations]) + "\n", encoding="utf-8")
    env = os.environ.copy()
    env["PATH"] = str(lean_bin) + os.pathsep + env.get("PATH", "")
    env["LEAN_PATH"] = str(out)
    receipt = {
        "scope": "Fresh five-module Lean replay and all new public theorem axiom audits; full Collatz remains open",
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "lean_version": version,
        "mathlib_commit": head,
        "mathlib_tracked_clean": True,
        "source_sha256": hashes,
        "runner_sha256": digest(Path(__file__)),
        "audited_declarations": declarations,
        "commands": [],
        "success": False,
    }
    try:
        for path in sources + [audit]:
            argv = [str(lean_bin / "lake"), "env", "lean", "-j1", "-R", str(path.parent),
                    "-DwarningAsError=true", "-o", str(out / f"{path.stem}.olean"), str(path)]
            print(f"Checking {path.name}", flush=True)
            start = time.monotonic()
            proc = subprocess.run(argv, cwd=mathlib, env=env, text=True,
                                  capture_output=True, timeout=1200)
            output = proc.stdout + proc.stderr
            (out / f"{path.stem}.log").write_text(output, encoding="utf-8")
            receipt["commands"].append({
                "source": str(path.relative_to(root)) if root in path.parents else str(path),
                "argv": argv, "exit_code": proc.returncode,
                "seconds": round(time.monotonic() - start, 3),
                "stdout": proc.stdout, "stderr": proc.stderr,
            })
            print(f"{path.name}: exit {proc.returncode}", flush=True)
            if proc.returncode:
                print(output, flush=True)
                raise RuntimeError(f"Lean rejected {path.name}")
            if "sorryAx" in output:
                raise RuntimeError(f"Admitted proof in {path.name}")
            for found in re.findall(r"depends on axioms: \[([^]]*)\]", output):
                axioms = {s.strip() for s in found.split(",") if s.strip()}
                if axioms - ALLOWED:
                    raise RuntimeError(f"Unexpected axioms: {sorted(axioms - ALLOWED)}")
            if path == audit:
                observed = set(re.findall(
                    r"'([^']+)' (?:depends on axioms|does not depend on any axioms)", output))
                if observed != set(declarations):
                    raise RuntimeError(f"Incomplete audit: missing={set(declarations)-observed}")
                receipt["axiom_audit_complete"] = True
        receipt["sources_unchanged"] = hashes == {str(p.relative_to(root)): digest(p) for p in sources}
        if not receipt["sources_unchanged"]:
            raise RuntimeError("Proof sources changed during replay")
        receipt["success"] = True
    finally:
        receipt["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        destination = out / "lean-receipt.json"
        destination.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        print(f"Receipt: {destination}", flush=True)


if __name__ == "__main__":
    main()
