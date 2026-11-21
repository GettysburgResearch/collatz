#!/usr/bin/env python3
"""Check the quantitative continuation and audit every new public theorem.

Use the pinned Mathlib checkout and Lean 4.34.1. By default every source is
compiled sequentially into a fresh output directory outside this repository.
The optional --base-build reuses the seven unchanged baseline modules only
after checking their successful receipt, source hashes, and compiler pins;
that earlier actual receipt and the reused artifact hashes are embedded.
The receipt records actual commands, output, source hashes, and dependencies.
This proof check is separate from tools/validate.py's repository gate.
"""

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time

from replay import MATHLIB, UPSTREAM


VENDOR = {
    "ReturnFourier": "a758b7b8c6b1827a5f96eb8ae32196c0145a0280229b6fa22bf899c3cd348ed3",
    "MarkPhase": "bd4cc9ef10cbaa91b8d8a8ea83f1d9dfbbf644d0235ceff77452c18abdf199d9",
    "MarkFrequency": "7786fd2c3eccecf8dedb931233c9ae1da059a8d883fb1e8250304b6c4df84921",
}
NEW = {
    "ExponentCoverage": "CollatzShell.ExponentCoverage",
    "MergerDispatch": "CollatzShell.MergerDispatch",
    "AnalyticCoupling": "CollatzShell.ForwardSection.AnalyticCoupling",
    "TemporalDensity": "CollatzShell.TemporalDensity",
}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--lean-bin", type=Path, required=True)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--base-build", type=Path,
                        help="Reuse the seven unchanged modules from a successful replay.py build")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    out = (args.out or Path(tempfile.mkdtemp(prefix="collatz-continuation-"))).resolve()
    if out == root or root in out.parents:
        parser.error("--out must be outside the repository")
    if out.exists() and any(out.iterdir()):
        parser.error("--out must be empty for a fresh proof build")
    out.mkdir(parents=True, exist_ok=True)
    mathlib, lean_bin = args.mathlib.resolve(), args.lean_bin.resolve()
    head = subprocess.check_output(["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip()
    if head != MATHLIB:
        raise RuntimeError(f"Mathlib pin mismatch: {head}")
    dirty = subprocess.check_output(
        ["git", "-C", str(mathlib), "status", "--porcelain", "--untracked-files=no"], text=True)
    if dirty:
        raise RuntimeError("The pinned Mathlib checkout has tracked modifications")
    sources = []
    for name, expected in UPSTREAM.items():
        p = here.parent / "lean-shell-cover" / f"{name}.lean"
        if digest(p) != expected:
            raise RuntimeError(f"PR173 source pin mismatch: {name}")
        sources.append(p)
    sources += [here / f"{m}.lean" for m in
                ["OffsetDescent", "MarkedOffsetReturn", "PhaseFrequency", "InfiniteDescent"]]
    for name, expected in VENDOR.items():
        p = here / "vendor-pr178" / f"{name}.lean"
        if digest(p) != expected:
            raise RuntimeError(f"PR178 source pin mismatch: {name}")
        sources.append(p)
    sources += [here / f"{m}.lean" for m in NEW]
    hashes = {str(p.relative_to(root)): digest(p) for p in sources}
    declarations = []
    for name, namespace in NEW.items():
        source = (here / f"{name}.lean").read_text(encoding="utf-8")
        declarations += [f"{namespace}.{d}" for d in
                         re.findall(r"^theorem\s+([\w']+)", source, re.MULTILINE)]
    if not declarations:
        raise RuntimeError("No new public theorems found for the audit")
    audit = out / "ContinuationAudit.lean"
    audit.write_text("\n".join([f"import {m}" for m in NEW] +
                               [f"#print axioms {d}" for d in declarations]) + "\n", encoding="utf-8")
    env = os.environ.copy()
    env["PATH"] = str(lean_bin) + os.pathsep + env.get("PATH", "")
    env["LEAN_PATH"] = str(out)
    version = subprocess.check_output([str(lean_bin / "lean"), "--version"], text=True).strip()
    if "version 4.34.1," not in version:
        raise RuntimeError(f"Lean version mismatch: {version}")
    receipt = {
        "scope": "Fresh Lean compilation and theorem axiom audit; full Collatz remains open",
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "lean_version": version,
        "mathlib_commit": head,
        "mathlib_tracked_clean": True,
        "pr173_commit": "fa0c9e2a2851e6324391e39c17afcb5913185aec",
        "pr178_commit": "0bb13b800e4e97f9fd3091b1a3d2e98b49911b7c",
        "source_sha256": hashes,
        "runner_sha256": digest(Path(__file__)),
        "audited_declarations": declarations,
        "commands": [],
        "success": False,
    }
    jobs = sources
    if args.base_build:
        base = args.base_build.resolve()
        proof = base / "lean-receipt.json"
        previous = json.loads(proof.read_text(encoding="utf-8"))
        if not (previous.get("success") and previous.get("sources_unchanged") and
                previous.get("mathlib_commit") == head and previous.get("lean_version") == version):
            raise RuntimeError("The supplied baseline receipt is not a successful build at these pins")
        artifacts = {}
        for p in sources[:7]:
            key = str(p.relative_to(root))
            if previous["source_sha256"].get(key) != hashes[key]:
                raise RuntimeError(f"Baseline source differs: {key}")
            artifact = base / f"{p.stem}.olean"
            artifacts[artifact.name] = digest(artifact)
            shutil.copy2(artifact, out / artifact.name)
        receipt["reused_baseline"] = {
            "scope": "Seven unchanged modules compiled in the recorded earlier build",
            "receipt_sha256": digest(proof), "receipt": previous,
            "olean_sha256": artifacts,
        }
        jobs = sources[7:]
    try:
        for p in jobs + [audit]:
            argv = [str(lean_bin / "lake"), "env", "lean", "-j1", "-R", str(p.parent),
                    "-DwarningAsError=true", "-o", str(out / f"{p.stem}.olean"), str(p)]
            print(f"Checking {p.name}", flush=True)
            start = time.monotonic()
            proc = subprocess.run(argv, cwd=mathlib, env=env, text=True,
                                  capture_output=True, timeout=1200)
            output = proc.stdout + proc.stderr
            (out / f"{p.stem}.log").write_text(output, encoding="utf-8")
            receipt["commands"].append({
                "source": str(p.relative_to(root)) if root in p.parents else str(p),
                "argv": argv, "exit_code": proc.returncode,
                "seconds": round(time.monotonic() - start, 3),
                "stdout": proc.stdout, "stderr": proc.stderr,
            })
            print(f"{p.name}: exit {proc.returncode}", flush=True)
            if proc.returncode:
                print(output, flush=True)
                raise RuntimeError(f"Lean rejected {p.name}")
            if "sorryAx" in output:
                raise RuntimeError(f"Admitted proof in {p.name}")
            for found in re.findall(r"depends on axioms: \[([^]]*)\]", output):
                axioms = {s.strip() for s in found.split(",") if s.strip()}
                if axioms - ALLOWED:
                    raise RuntimeError(f"Unexpected axioms: {sorted(axioms - ALLOWED)}")
            if p == audit:
                observed = set(re.findall(r"'([^']+)' (?:depends on axioms|does not depend on any axioms)", output))
                if observed != set(declarations):
                    raise RuntimeError(f"Audit coverage mismatch: missing={set(declarations)-observed}")
                receipt["axiom_audit_complete"] = True
        receipt["sources_unchanged"] = hashes == {str(p.relative_to(root)): digest(p) for p in sources}
        if not receipt["sources_unchanged"]:
            raise RuntimeError("Proof sources changed during this build")
        receipt["success"] = True
    finally:
        receipt["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        destination = out / "lean-receipt.json"
        destination.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        print(f"Receipt: {destination}", flush=True)


if __name__ == "__main__":
    main()
