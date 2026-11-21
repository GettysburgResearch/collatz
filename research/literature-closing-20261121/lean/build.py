#!/usr/bin/env python3
"""Replay the literature-closing Lean packet and audit every public theorem.

The dependency packet and Mathlib retain their exact source pins.  An existing
successful dependency receipt can be reused only after the source and every
compiled dependency have been checked against its recorded digests.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
MODULES = [
    ("EntranceRenewal", "lean/EntranceRenewal.lean", "CollatzShell.ForwardSection.EntranceRenewal"),
    ("RetainedTransport", "lean/RetainedTransport.lean", "CollatzShell.ForwardSection.RetainedTransport"),
    ("BandArithmetic", "arithmetic/BandArithmetic.lean", "CollatzShell.BandArithmetic"),
    ("MixedBaseNormalForm", "mergers/MixedBaseNormalForm.lean", "CollatzShell.MixedBaseNormalForm"),
]
DEPENDENCIES = ["ShellCover", "ForwardSection", "SectionDynamics", "RisingReturns",
                "BandDescent", "BandRotation", "BandMass"]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--lean", type=Path, required=True)
    ap.add_argument("--mathlib", type=Path, required=True)
    ap.add_argument("--receipt", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--dependencies-output", type=Path, required=True)
    ap.add_argument("--reuse-dependency-receipt", type=Path)
    ap.add_argument("--timeout", type=int, default=900)
    args = ap.parse_args()
    packet = Path(__file__).resolve().parent.parent
    previous = packet.parent / "band-completion-20261121"
    lean, mathlib = args.lean.resolve(), args.mathlib.resolve()
    output, deps = args.output.resolve(), args.dependencies_output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env["PATH"] = str(lean.parent) + os.pathsep + env.get("PATH", "")
    version = subprocess.check_output([str(lean), "--version"], text=True, env=env).strip()
    if "version 4.34.1," not in version:
        raise RuntimeError("This packet requires Lean 4.34.1")
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib, text=True).strip()
    if head != MATHLIB_COMMIT:
        raise RuntimeError("Mathlib source pin mismatch")
    dirty = subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"],
                                    cwd=mathlib, text=True)
    if dirty:
        raise RuntimeError("The pinned Mathlib sources have tracked changes")

    dependency_receipt = args.reuse_dependency_receipt
    if dependency_receipt is None:
        dependency_receipt = output / "dependency-replay.json"
        cmd = [sys.executable, str(previous / "lean/build.py"), "--lean", str(lean),
               "--mathlib", str(mathlib), "--output", str(deps), "--receipt",
               str(dependency_receipt), "--timeout", str(args.timeout)]
        subprocess.run(cmd, check=True, env=env)
    dep_record = json.loads(dependency_receipt.read_text())
    if not dep_record.get("success") or dep_record.get("mathlib_commit") != head:
        raise RuntimeError("Dependency replay is not successful at the required pin")
    bindings = []
    for name in DEPENDENCIES:
        records = [r for r in dep_record["commands"] if r["module"] == name]
        if len(records) != 1 or records[0]["exit_code"] != 0:
            raise RuntimeError("Missing successful dependency: " + name)
        record = records[0]
        source = (deps / "generated" if name in DEPENDENCIES[:4] else previous / "lean") / (name + ".lean")
        artifact = deps / (name + ".olean")
        if sha(source) != record["source_sha256"] or sha(artifact) != record["olean_sha256"]:
            raise RuntimeError("Dependency source or artifact mismatch: " + name)
        bindings.append({"module": name, "source_sha256": sha(source), "olean_sha256": sha(artifact)})
    upstream_manifest = json.loads((previous / "upstream-files.json").read_text())
    repository = packet.parent.parent
    for item in upstream_manifest["files"]:
        if sha(repository / item["local_path"]) != item["sha256"]:
            raise RuntimeError("Pinned upstream file mismatch: " + item["local_path"])

    library_paths = [output, deps, mathlib / ".lake/build/lib/lean"]
    library_paths += sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
    library_paths.append(lean.parent.parent / "lib/lean")
    env["LEAN_PATH"] = os.pathsep.join(map(str, library_paths))

    audit_path = output / "LiteratureAudit.lean"
    audit = "module\n" + "".join("import " + name + "\n" for name, _, _ in MODULES)
    audited = []
    for name, rel, namespace in MODULES:
        for theorem in re.findall(r"^theorem\s+(\w+)", (packet / rel).read_text(), re.M):
            qualified = namespace + "." + theorem
            audited.append(qualified)
            audit += "#print axioms " + qualified + "\n"
    audit_path.write_text(audit)
    receipt = {
        "schema": "collatz-literature-lean-replay/v1",
        "lean_version": version,
        "mathlib_commit": head,
        "dependency_receipt_sha256": sha(dependency_receipt),
        "dependency_bindings": bindings,
        "audited_declarations": audited,
        "commands": [],
        "success": False,
        "scope": "The listed exact Lean theorems; no universal Collatz theorem or analytic transport premise is asserted.",
    }
    rc = 0
    jobs = [(name, packet / rel) for name, rel, _ in MODULES] + [("LiteratureAudit", audit_path)]
    for name, source in jobs:
        cmd = [str(lean), "-j", "1", "-DwarningAsError=true", "-o", str(output / (name + ".olean")), source.name]
        print("START " + name, flush=True)
        start = time.monotonic()
        try:
            run = subprocess.run(cmd, cwd=source.parent, env=env, text=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, timeout=args.timeout)
            rc, log = run.returncode, run.stdout
        except subprocess.TimeoutExpired as exc:
            rc, log = 124, exc.stdout or ""
            if isinstance(log, bytes):
                log = log.decode(errors="replace")
            log += "\nExplicit per-module timeout exceeded.\n"
        if name == "LiteratureAudit" and rc == 0:
            for body in re.findall(r"depends on axioms:\s*\[([^\]]*)\]", log):
                axioms = {x.strip() for x in body.split(",") if x.strip()}
                if not axioms <= {"propext", "Classical.choice", "Quot.sound"}:
                    rc = 1
                    log += "\nUnexpected axiom dependency.\n"
            for qualified in audited:
                if "'" + qualified + "'" not in log:
                    rc = 1
                    log += "\nMissing axiom report: " + qualified + "\n"
        record = {"module": name, "source_sha256": sha(source), "argv": cmd,
                  "exit_code": rc, "seconds": round(time.monotonic() - start, 3), "output": log}
        if rc == 0:
            record["olean_sha256"] = sha(output / (name + ".olean"))
        receipt["commands"].append(record)
        (output / (name + ".log")).write_text(log)
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
        print(f"DONE {name}: exit {rc}, {record['seconds']} s", flush=True)
        if log:
            print(log, flush=True)
        if rc:
            break
    receipt["success"] = rc == 0 and len(receipt["commands"]) == len(jobs)
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    return rc


if __name__ == "__main__":
    sys.exit(main())
