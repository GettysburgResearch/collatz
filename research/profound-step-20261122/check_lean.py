#!/usr/bin/env python3
"""Compile this packet's new Lean modules against hash-bound prior builds.

The two raw PR185 dependencies are preserved byte for byte. Generated wrappers
change only module/export headers. The previous eleven modules are reused only
after checking the source and artifact hashes in their successful receipts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time

MATHLIB = "d13f23b723b8a846827a245b89c10fc7d3f11612"
NEW = [
    ("ClockLags", "operator/ClockLags.lean", "CollatzShell.ClockLags"),
    ("AsynchronousKernel", "transport/AsynchronousKernel.lean", "CollatzShell.AsynchronousKernel"),
    ("BlockCompression", "arithmetic/BlockCompression.lean", "CollatzShell.BlockCompression"),
    ("AffineCarry", "mergers/AffineCarry.lean", "CollatzShell.AffineCarry"),
    ("CarryCapture", "mergers/CarryCapture.lean", "CollatzShell.CarryCapture"),
]
PRIOR = ["ShellCover", "ForwardSection", "SectionDynamics", "RisingReturns",
         "BandDescent", "BandRotation", "BandMass"]
LITERATURE = {
    "EntranceRenewal": "lean/EntranceRenewal.lean",
    "RetainedTransport": "lean/RetainedTransport.lean",
    "BandArithmetic": "arithmetic/BandArithmetic.lean",
    "MixedBaseNormalForm": "mergers/MixedBaseNormalForm.lean",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bind(receipt: Path, sources: dict[str, Path], output: Path) -> list[dict]:
    data = json.loads(receipt.read_text())
    if not data.get("success") or data.get("mathlib_commit") != MATHLIB:
        raise RuntimeError("Prior receipt is not successful at the pinned Mathlib")
    result = []
    for name, source in sources.items():
        records = [r for r in data["commands"] if r["module"] == name]
        if len(records) != 1 or records[0]["exit_code"] != 0:
            raise RuntimeError("Missing successful prior module: " + name)
        record = records[0]
        artifact = output / (name + ".olean")
        if (sha(source) != record["source_sha256"]
                or sha(artifact) != record["olean_sha256"]):
            raise RuntimeError("Changed prior source or artifact: " + name)
        result.append({"module": name, "source_sha256": sha(source),
                       "olean_sha256": sha(artifact),
                       "receipt_sha256": sha(receipt), "recompiled": False})
    return result


def wrapper(raw: str) -> str:
    lines = raw.splitlines(keepends=True)
    end = 0
    while end < len(lines) and (lines[end].startswith("import ") or not lines[end].strip()):
        end += 1
    header = "".join("public " + line if line.startswith("import ") else line
                     for line in lines[:end])
    return "module\n\n" + header + "@[expose] public section\n\n" + "".join(lines[end:])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    for key in ("lean", "mathlib", "dependencies-output", "literature-output",
                "dependencies-receipt", "literature-receipt", "output", "receipt"):
        ap.add_argument("--" + key, type=Path, required=True)
    ap.add_argument("--timeout", type=int, default=900)
    args = ap.parse_args()
    packet = Path(__file__).resolve().parent
    root = packet.parent.parent
    lean, mathlib = args.lean.resolve(), args.mathlib.resolve()
    deps, lit = args.dependencies_output.resolve(), args.literature_output.resolve()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    generated = out / "generated"
    generated.mkdir(exist_ok=True)
    env = dict(os.environ)
    env["PATH"] = str(lean.parent) + os.pathsep + env.get("PATH", "")
    version = subprocess.check_output([str(lean), "--version"], env=env, text=True).strip()
    if "version 4.34.1," not in version:
        raise RuntimeError("Lean 4.34.1 is required")
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib, text=True).strip()
    if head != MATHLIB:
        raise RuntimeError("Mathlib pin changed")
    if subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"],
                               cwd=mathlib, text=True):
        raise RuntimeError("Mathlib tracked sources changed")
    old = root / "research/band-completion-20261121"
    old_sources = {name: ((deps / "generated") if name in PRIOR[:4] else old / "lean")
                  / (name + ".lean") for name in PRIOR}
    bindings = bind(args.dependencies_receipt, old_sources, deps)
    prior_lit = root / "research/literature-closing-20261121"
    bindings += bind(args.literature_receipt,
                     {name: prior_lit / rel for name, rel in LITERATURE.items()}, lit)
    for item in json.loads((old / "upstream-files.json").read_text())["files"]:
        if sha(root / item["local_path"]) != item["sha256"]:
            raise RuntimeError("Pinned original vendor changed: " + item["local_path"])

    vendor = json.loads((packet / "mergers/DEPENDENCIES.json").read_text())
    jobs = []
    for item in vendor:
        name = item["name"]
        source = packet / "mergers/vendor" / (name + ".lean")
        if sha(source) != item["sha256"]:
            raise RuntimeError("Raw PR185 vendor changed: " + name)
        target = generated / source.name
        target.write_text(wrapper(source.read_text()))
        # The exact generated bytes are recorded even if whitespace in a prior
        # agent's independently built header wrapper differs.
        jobs.append((name, target))

    env["LEAN_PATH"] = os.pathsep.join(map(str, [out, lit, deps,
        mathlib / ".lake/build/lib/lean",
        *sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean")),
        lean.parent.parent / "lib/lean"]))
    jobs += [(name, packet / rel) for name, rel, _ in NEW]
    audited = []
    audit = "module\n" + "".join("import " + name + "\n" for name, _, _ in NEW)
    for name, rel, namespace in NEW:
        for decl in re.findall(r"^theorem\s+(\w+)", (packet / rel).read_text(), re.M):
            q = namespace + "." + decl
            audited.append(q)
            audit += "#print axioms " + q + "\n"
    audit_path = out / "ProfoundAudit.lean"
    audit_path.write_text(audit)
    jobs.append(("ProfoundAudit", audit_path))
    receipt = {"schema": "collatz-profound-lean-replay/v1", "lean_version": version,
               "mathlib_commit": head, "prior_bindings": bindings,
               "vendor_bindings": vendor, "audited_declarations": audited,
               "commands": [], "success": False,
               "scope": "Five new modules and their transitive axioms; written analytic and Matveev arguments are not Lean theorems. Full Collatz remains open."}
    rc = 0
    for name, source in jobs:
        argv = [str(lean), "-j", "1", "-DwarningAsError=true", "-o",
                str(out / (name + ".olean")), source.name]
        print("START " + name, flush=True)
        source_digest = sha(source)
        start = time.monotonic()
        try:
            p = subprocess.run(argv, cwd=source.parent, env=env, text=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               timeout=args.timeout)
            rc, log = p.returncode, p.stdout
        except subprocess.TimeoutExpired as exc:
            rc, log = 124, exc.stdout or ""
            if isinstance(log, bytes):
                log = log.decode(errors="replace")
            log += "\nExplicit per-module timeout exceeded.\n"
        if sha(source) != source_digest:
            rc = 1
            log += "\nSource changed during compilation; this run cannot certify its final bytes.\n"
        if name == "ProfoundAudit" and rc == 0:
            for body in re.findall(r"depends on axioms:\s*\[([^\]]*)\]", log):
                if not {x.strip() for x in body.split(",") if x.strip()} <= {
                        "propext", "Classical.choice", "Quot.sound"}:
                    rc = 1
                    log += "\nUnexpected axiom dependency.\n"
            for decl in audited:
                if "'" + decl + "'" not in log:
                    rc = 1
                    log += "\nMissing axiom report for " + decl + "\n"
        record = {"module": name, "source_sha256": source_digest, "argv": argv,
                  "cwd": str(source.parent), "LEAN_PATH": env["LEAN_PATH"],
                  "exit_code": rc, "seconds": round(time.monotonic() - start, 3), "output": log}
        if rc == 0:
            record["olean_sha256"] = sha(out / (name + ".olean"))
        receipt["commands"].append(record)
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
        (out / (name + ".log")).write_text(log)
        print(f"DONE {name}: {rc}, {record['seconds']} seconds", flush=True)
        if log:
            print(log, flush=True)
        if rc:
            break
    receipt["success"] = rc == 0 and len(receipt["commands"]) == len(jobs)
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
