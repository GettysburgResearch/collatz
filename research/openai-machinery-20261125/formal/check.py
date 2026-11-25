"""Verify frozen bytes, build the connected Lean project, and audit its claims.

Run with Lean/Lake 4.34.1 on PATH after obtaining the pinned Mathlib packages.
The receipt distinguishes compilation from the much larger source-qualified
upstream results. An existing Mathlib binary cache is permitted.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PACKET = ROOT.parent
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pinned_sources():
    checked = {}
    upstream = json.loads((ROOT / "UPSTREAM.json").read_text())
    for module, record in upstream["modules"].items():
        path = ROOT / (module.replace(".", "/") + ".lean")
        if digest(path) != record["sha256"] or path.stat().st_size != record["bytes"]:
            raise ValueError(f"OpenAI pinned bytes differ: {path}")
        checked[str(path.relative_to(PACKET))] = digest(path)
    origin = json.loads((PACKET / "tensor/pr192/ORIGIN.json").read_text())
    for record in origin["files"]:
        path = PACKET / "tensor/pr192" / record["file"]
        if digest(path) != record["sha256"]:
            raise ValueError(f"PR192 pinned bytes differ: {path}")
        checked[str(path.relative_to(PACKET))] = digest(path)
    spec = importlib.util.spec_from_file_location("clock_checks", PACKET / "clock/check_lean.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for name, expected in module.SOURCE_HASHES.items():
        path = PACKET / "clock/pr206" / (name + ".lean")
        if digest(path) != expected:
            raise ValueError(f"PR206 pinned bytes differ: {path}")
        checked[str(path.relative_to(PACKET))] = digest(path)
    return checked


def run(command):
    result = subprocess.run(command, cwd=ROOT, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(result.stdout, end="", flush=True)
    if result.returncode:
        raise RuntimeError(f"exit {result.returncode}: {' '.join(command)}")
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    receipt = {"schema": "collatz-openai-lean/v1", "success": False,
               "started_utc": datetime.now(timezone.utc).isoformat(),
               "scope": "14 frozen source files; connected local proofs; not a rebuild of the headline upstream theorems"}
    try:
        receipt["frozen_sources"] = pinned_sources()
        version = run(["lean", "--version"]).strip()
        if not version.startswith("Lean (version 4.34.1,"):
            raise ValueError("Lean 4.34.1 required")
        receipt["lean"] = version
        manifest = json.loads((ROOT / "lake-manifest.json").read_text())
        packages = {p["name"]: p["rev"] for p in manifest["packages"]}
        if packages["mathlib"] != "d13f23b723b8a846827a245b89c10fc7d3f11612":
            raise ValueError("wrong Mathlib pin")
        receipt["package_pins"] = packages
        receipt["build_stdout"] = run(["lake", "build"])
        actual = {}
        for name, expected in packages.items():
            package = ROOT / ".lake/packages" / name
            actual[name] = subprocess.check_output(
                ["git", "-C", str(package), "rev-parse", "HEAD"], text=True).strip()
            if actual[name] != expected:
                raise ValueError(f"loaded package revision differs: {name}")
        receipt["actual_package_revisions"] = actual
        output = run(["lake", "env", "lean", "-DwarningAsError=true", "Audit.lean"])
        expected = set(re.findall(r"^#print axioms (\S+)$", (ROOT / "Audit.lean").read_text(), re.M))
        found = re.findall(r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", output)
        if {name for name, _ in found} != expected or len(found) != len(expected):
            raise ValueError("incomplete or duplicate public declaration audit")
        audited = {}
        for name, axioms in found:
            deps = {a.strip() for a in axioms.split(",") if a.strip()}
            if not deps <= ALLOWED:
                raise ValueError(f"unexpected axiom for {name}: {deps - ALLOWED}")
            audited[name] = sorted(deps)
        receipt["declarations"] = audited
        receipt["local_sources"] = {
            str(p.relative_to(PACKET)): digest(p)
            for directory in (ROOT, PACKET / "tensor", PACKET / "fourier")
            for p in sorted(directory.glob("*.lean"))
        }
        receipt["success"] = True
        print(f"PASS: {len(receipt['frozen_sources'])} frozen files; {len(audited)} declaration audits.")
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as exc:
        receipt["error"] = str(exc)
        print(f"FAIL: {exc}", file=sys.stderr)
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
