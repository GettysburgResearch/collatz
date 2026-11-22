#!/usr/bin/env python3
"""Replay the band packet against the pinned Lean and Mathlib versions.

The four upstream inputs remain byte-identical in vendor/. Their generated
compilation inputs opt into Lean's supported module/export syntax. GridAt,
its decidability instance, and visit_exists receive public visibility for
exposed definitions; all formulas and proof bodies are unchanged.
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
DEPENDENCIES = ["ShellCover", "ForwardSection", "SectionDynamics", "RisingReturns"]
NEW_MODULES = ["BandDescent", "BandRotation", "BandMass"]
NAMESPACES = {
    "BandDescent": "CollatzShell.BandDescent",
    "BandRotation": "CollatzShell.BandRotation",
    "BandMass": "CollatzShell.ForwardSection.BandMass",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module_input(raw):
    # Lean's exposed public firstMesh body names this helper explicitly.
    # This is a visibility change only; no formula or proof body is changed.
    raw = raw.replace("private def GridAt (", "def GridAt (")
    raw = raw.replace("private instance (h p : Nat) : Decidable (GridAt h p)",
                      "instance (h p : Nat) : Decidable (GridAt h p)")
    raw = raw.replace("private theorem visit_exists (", "theorem visit_exists (")
    lines = raw.splitlines(keepends=True)
    count = 0
    while count < len(lines) and lines[count].startswith("import "):
        count += 1
    if not count:
        raise ValueError("Expected an initial block of imports")
    return ("module\n" + "".join("public " + line for line in lines[:count])
            + "\n@[expose] public section\n" + "".join(lines[count:]))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--lean", required=True, type=Path, help="Lean 4.34.1 executable")
    ap.add_argument("--mathlib", required=True, type=Path, help="Matching prebuilt Mathlib checkout")
    ap.add_argument("--receipt", required=True, type=Path, help="JSON execution receipt outside the source tree")
    ap.add_argument("--output", type=Path, help="Optional separate build directory; default lean/.build")
    ap.add_argument("--phase", choices=["all", "dependencies", "new"], default="all")
    ap.add_argument("--timeout", type=int, default=900, help="Per-module seconds")
    args = ap.parse_args()
    root = Path(__file__).resolve().parent
    packet = root.parent
    repository = packet.parent.parent
    lean = args.lean.resolve()
    mathlib = args.mathlib.resolve()
    output = args.output.resolve() if args.output else root / ".build"
    generated = output / "generated"
    generated.mkdir(parents=True, exist_ok=True)
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if "version 4.34.1," not in version:
        raise RuntimeError("This packet is pinned to Lean 4.34.1")
    mathlib_head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib, text=True).strip()
    if mathlib_head != MATHLIB_COMMIT:
        raise RuntimeError("Mathlib commit differs from the packet pin")
    base_path = subprocess.check_output([str(lean.with_name("lake")), "env", "printenv", "LEAN_PATH"], cwd=mathlib, text=True).strip()
    env = dict(os.environ)
    env["LEAN_PATH"] = os.pathsep.join([str(output), base_path, str(lean.parent.parent / "lib/lean")])
    receipt = {
        "schema": "collatz-band-lean-replay/v1",
        "lean_version": version,
        "mathlib_commit": mathlib_head,
        "mathlib_tracked_changes": subprocess.check_output(
            ["git", "status", "--porcelain", "--untracked-files=no"], cwd=mathlib, text=True),
        "phase": args.phase,
        "upstream": [],
        "commands": [],
        "success": False,
        "scope": "The listed Lean declarations; no claim of universal Collatz convergence.",
    }
    manifest = json.loads((packet / "upstream-files.json").read_text())
    for item in manifest["files"]:
        source = repository / item["local_path"]
        if digest(source) != item["sha256"]:
            raise RuntimeError("Upstream source hash mismatch: " + str(source))
        target = generated / source.name
        target.write_text(module_input(source.read_text()))
        receipt["upstream"].append({**item, "generated_sha256": digest(target)})
    modules = DEPENDENCIES + NEW_MODULES if args.phase == "all" else (DEPENDENCIES if args.phase == "dependencies" else NEW_MODULES)
    audited = []
    if args.phase != "dependencies":
        audit = "module\n" + "".join("import " + name + "\n" for name in NEW_MODULES)
        for name in NEW_MODULES:
            for theorem in re.findall(r"^theorem\s+(\w+)", (root / (name + ".lean")).read_text(), re.M):
                qualified = NAMESPACES[name] + "." + theorem
                audited.append(qualified)
                audit += "#print axioms " + qualified + "\n"
        (generated / "BandAudit.lean").write_text(audit)
        modules = modules + ["BandAudit"]
        receipt["audited_declarations"] = audited
    rc = 0
    for name in modules:
        source = generated / (name + ".lean") if name in DEPENDENCIES or name == "BandAudit" else root / (name + ".lean")
        cmd = [str(lean), "-j", "1", "-DwarningAsError=true", "-o", str(output / (name + ".olean")), source.name]
        print("START " + name, flush=True)
        start = time.monotonic()
        try:
            run = subprocess.run(cmd, cwd=source.parent, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=args.timeout)
            rc, log = run.returncode, run.stdout
        except subprocess.TimeoutExpired as exc:
            rc = 124
            log = exc.stdout or ""
            if isinstance(log, bytes):
                log = log.decode(errors="replace")
            log += "\nReplay exceeded the explicit per-module timeout.\n"
        if name == "BandAudit" and rc == 0:
            dependencies = re.findall(r"depends on axioms:\s*\[([^\]]*)\]", log)
            for dependency_list in dependencies:
                found = {item.strip() for item in dependency_list.split(",") if item.strip()}
                if not found <= {"propext", "Classical.choice", "Quot.sound"}:
                    rc = 1
                    log += "\nUnexpected axiom dependency in audit.\n"
            for theorem in audited:
                if "'" + theorem + "'" not in log:
                    rc = 1
                    log += "\nMissing audit output for " + theorem + "\n"
        (output / (name + ".log")).write_text(log)
        command = {"module": name, "source_sha256": digest(source), "argv": cmd, "exit_code": rc,
                   "seconds": round(time.monotonic() - start, 3), "output": log}
        if rc == 0:
            command["olean_sha256"] = digest(output / (name + ".olean"))
        receipt["commands"].append(command)
        print(f"DONE {name}: exit {rc}, {command['seconds']} s", flush=True)
        if log:
            print(log, flush=True)
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
        if rc:
            break
    receipt["success"] = rc == 0 and len(receipt["commands"]) == len(modules)
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    return rc


if __name__ == "__main__":
    sys.exit(main())
