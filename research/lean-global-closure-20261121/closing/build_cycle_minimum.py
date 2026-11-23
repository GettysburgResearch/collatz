#!/usr/bin/env python3
"""Compile the exact full-cycle minimum theorem and audit its declarations.

Only these two project sources are compiled. The pinned installed Mathlib and
its dependencies are reused; no claim of rebuilding those dependencies is made.
Output objects and receipts must be outside this source directory.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time


MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("lean", "mathlib", "deps", "output", "receipt"):
        parser.add_argument(f"--{name}", required=True, type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    lean, mathlib, deps, output, receipt = (
        getattr(args, name).resolve()
        for name in ("lean", "mathlib", "deps", "output", "receipt")
    )
    if output.is_relative_to(here) or receipt.is_relative_to(here):
        parser.error("output and receipt must be outside the source directory")
    if output.exists() and any(output.rglob("*.olean")):
        parser.error("output must not contain precompiled project objects")
    if not deps.is_dir():
        parser.error("--deps must identify the installed dependency object directory")
    output.mkdir(parents=True, exist_ok=True)
    receipt.parent.mkdir(parents=True, exist_ok=True)

    def capture(command: list[str], cwd: Path = here) -> str:
        return subprocess.check_output(command, cwd=cwd, text=True).strip()

    version = capture([str(lean), "--version"])
    if "version 4.34.1," not in version or LEAN_COMMIT not in version:
        parser.error(f"unexpected Lean compiler: {version}")
    revision = capture(["git", "rev-parse", "HEAD"], mathlib)
    status = capture(["git", "status", "--porcelain=v1"], mathlib)
    if revision != MATHLIB_COMMIT or status:
        parser.error("Mathlib must have the pinned commit and a clean source worktree")

    env = os.environ.copy()
    env["LEAN_PATH"] = os.pathsep.join(
        str(p) for p in (output, mathlib / ".lake/build/lib/lean", deps)
    )
    report = {
        "status": "RUNNING",
        "scope": "Exact product deficit, whole finite-cycle product identity, and natural-number minimum bound using the full denominator.",
        "excluded_scope": "Parity-word realization, zero-atom counting and the census algorithm are written proofs; Matveev is an external source-qualified dependency; no full cycle exclusion.",
        "lean_version": version,
        "mathlib_commit": revision,
        "mathlib_source_worktree_clean": not status,
        "dependency_scope": "Reused installed compiled Mathlib and package dependencies; only the two named project sources were freshly compiled.",
        "LEAN_PATH": env["LEAN_PATH"],
        "source_sha256": {
            name: sha(here / name)
            for name in ("CycleMinimum.lean", "CycleMinimumAudit.lean", "build_cycle_minimum.py")
        },
        "commands": [],
    }

    def save() -> None:
        receipt.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    save()
    audit = ""
    for module in ("CycleMinimum", "CycleMinimumAudit"):
        source = here / f"{module}.lean"
        obj = output / f"{module}.olean"
        command = [str(lean), "-j1", "-DwarningAsError=true", "-DautoImplicit=false",
                   "-o", str(obj), str(source)]
        start = time.monotonic()
        result = subprocess.run(command, cwd=here, env=env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (output / f"{module}.full.log").write_text(result.stdout, encoding="utf-8")
        compact = "\n".join(line for line in result.stdout.splitlines()
                            if not line.startswith("IMPORT_CLOSURE "))
        report["commands"].append({
            "module": module, "command": command, "exit_code": result.returncode,
            "elapsed_seconds": round(time.monotonic() - start, 3),
            "stdout_without_import_listing": compact,
            "full_stdout_sha256": hashlib.sha256(result.stdout.encode()).hexdigest(),
            "olean_sha256": sha(obj) if obj.exists() and result.returncode == 0 else None,
        })
        print(f"{module}: exit={result.returncode}", flush=True)
        if result.returncode:
            report["status"] = "FAILED"
            save()
            print(result.stdout)
            return result.returncode
        audit = result.stdout
        save()

    axioms = [line for line in audit.splitlines() if "depends on axioms:" in line]
    allowed = {"propext", "Classical.choice", "Quot.sound"}
    if len(axioms) != 5 or "sorryAx" in audit:
        raise RuntimeError("Unexpected exported-declaration audit")
    for line in axioms:
        names = line.split("depends on axioms:", 1)[1].strip().strip("[]")
        if not set(names.split(", ")) <= allowed:
            raise RuntimeError(f"Unexpected axiom: {line}")
    imports = [line.removeprefix("IMPORT_CLOSURE ") for line in audit.splitlines()
               if line.startswith("IMPORT_CLOSURE ")]
    manifest = receipt.parent / "cycle-minimum-import-closure.txt"
    manifest.write_text("\n".join(imports) + "\n", encoding="utf-8")
    report.update({
        "status": "PASSED", "fresh_project_source_count": 2,
        "audited_declaration_count": len(axioms), "audited_axioms": axioms,
        "direct_imports": [line.removeprefix("import ")
                           for line in (here / "CycleMinimum.lean").read_text().splitlines()
                           if line.startswith("import ")],
        "import_name_count_including_checked_module": len(imports),
        "import_name_manifest": manifest.name,
        "import_name_manifest_sha256": sha(manifest),
        "import_manifest_scope": "Names in the loaded environment, not a claim of a dependency source rebuild.",
    })
    save()
    print(f"Passed: two fresh project compilations, {len(axioms)} axiom audits; {receipt}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
