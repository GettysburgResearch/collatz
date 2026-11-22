#!/usr/bin/env python3
"""Strict replay of the two merger modules and their 21 public statements.

Supply a Lean import path containing the pinned ShellCover and matching
Mathlib outputs. Prior Collatz proofs are not recompiled by this driver.
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


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def wrapper(raw: str) -> str:
    lines = raw.splitlines(keepends=True)
    i = 0
    while i < len(lines) and (lines[i].startswith("import ") or not lines[i].strip()):
        i += 1
    head = "".join("public " + line if line.startswith("import ") else line
                   for line in lines[:i])
    return "module\n\n" + head + "@[expose] public section\n\n" + "".join(lines[i:])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--import-path", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--reuse-receipt", type=Path, action="append", default=[])
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    lean = args.lean.resolve()
    lean_path = str(output) + ":" + args.import_path
    environment = os.environ.copy()
    environment["LEAN_PATH"] = lean_path
    environment["PATH"] = str(lean.parent) + ":" + environment.get("PATH", "")
    previous = []
    for path in args.reuse_receipt:
        data = json.loads(path.read_text(encoding="utf-8"))
        previous.extend(data if isinstance(data, list) else data.get("runs", [data]))

    receipt = {"status": "RUNNING", "global_collatz_proved": False,
               "driver_sha256": digest(Path(__file__)), "runs": []}

    def save() -> None:
        args.receipt.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")

    def compile_file(name: str, source: Path, cwd: Path, allow_reuse: bool) -> None:
        artifact = output / (name + ".olean")
        command = [str(lean), "-j", "1", "-DwarningAsError=true",
                   "-o", str(artifact), str(source)]
        binding = {"name": name, "command": command, "cwd": str(cwd),
                   "LEAN_PATH": lean_path, "source_sha256": digest(source)}
        old = next((row for row in previous if allow_reuse and
                    row.get("exit_code") == 0 and artifact.exists() and
                    all(row.get(key) == value for key, value in binding.items()) and
                    row.get("olean_sha256") == digest(artifact)), None)
        if old is not None:
            row = dict(old)
            row["execution"] = "Reused completed run after exact source/artifact/command/path checks"
            receipt["runs"].append(row)
            save()
            return
        start = time.monotonic()
        result = subprocess.run(command, cwd=cwd, env=environment, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        row = {**binding, "seconds": time.monotonic() - start,
               "exit_code": result.returncode, "output": result.stdout,
               "execution": "Executed by this driver"}
        if result.returncode == 0:
            row["olean_sha256"] = digest(artifact)
        receipt["runs"].append(row)
        save()
        if result.returncode:
            raise RuntimeError(name + " failed:\n" + result.stdout)

    try:
        deps = json.loads((base / "DEPENDENCIES.json").read_text(encoding="utf-8"))
        receipt["dependencies"] = deps
        for dep in deps:
            raw_source = base / "vendor" / (dep["name"] + ".lean")
            if digest(raw_source) != dep["sha256"]:
                raise RuntimeError("Pinned dependency source changed: " + dep["name"])
            generated = output / (dep["name"] + ".lean")
            generated.write_text(wrapper(raw_source.read_text(encoding="utf-8")), encoding="utf-8")
            if digest(generated) != dep["wrapper_sha256"]:
                raise RuntimeError("Dependency wrapper changed: " + dep["name"])
            compile_file(dep["name"], generated, output, True)

        declarations = []
        for name in ("AffineCarry", "CarryCapture"):
            source = base / (name + ".lean")
            compile_file(name, source, base, True)
            declarations.extend("CollatzShell." + name + "." + theorem
                                for theorem in re.findall(r"^theorem\s+(\w+)",
                                                          source.read_text(), re.M))
        audit = output / "CarryAudit.lean"
        audit.write_text("module\n\npublic import AffineCarry\npublic import CarryCapture\n\n" +
                         "\n".join("#print axioms " + name for name in declarations) + "\n",
                         encoding="utf-8")
        compile_file("CarryAudit", audit, output, False)
        audit_text = receipt["runs"][-1]["output"]
        for name in declarations:
            if "'" + name + "'" not in audit_text:
                raise RuntimeError("Missing axiom audit for " + name)
        allowed = {"propext", "Classical.choice", "Quot.sound"}
        used = set()
        for content in re.findall(r"depends on axioms:\s*\[([^\]]*)\]", audit_text):
            used.update(x.strip() for x in content.split(",") if x.strip())
        if not used <= allowed or "sorryAx" in audit_text:
            raise RuntimeError("Unexpected axiom dependency: " + repr(used))
        receipt.update(status="PASSED", public_statements=len(declarations),
                       declarations=declarations, axiom_dependencies=sorted(used))
        save()
        print(json.dumps({"status": receipt["status"], "public_statements": len(declarations),
                          "axioms": sorted(used)}))
    except Exception as error:
        receipt.update(status="FAILED", error=str(error))
        save()
        raise


if __name__ == "__main__":
    main()
