#!/usr/bin/env python3
"""Rebuild this packet from an empty object directory and audit its theorems.

Requires Lean 4.34.1 and a built Mathlib checkout at the revision below.
The receipt records execution, source hashes, all commands and complete output.
It does not certify the written analytic arguments or close Collatz.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone

MATHLIB_REVISION = "d13f23b723b8a846827a245b89c10fc7d3f11612"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
ROOT = Path(__file__).resolve().parent


def public_theorems(text: str) -> list[str]:
    """Read this packet's simple namespace/section/declaration conventions.

    Every extracted name is resolved again by Lean in the generated audit.
    This is an inventory helper, not a Lean parser or a proof checker.
    """
    scopes: list[tuple[str, str]] = []
    result: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^namespace\s+([A-Za-z0-9_.]+)\s*$", line)
        if match:
            scopes.append(("namespace", match.group(1)))
            continue
        if re.match(r"^section(?:\s+[A-Za-z0-9_]+)?\s*$", line):
            scopes.append(("section", ""))
            continue
        if re.match(r"^end(?:\s+[A-Za-z0-9_.]+)?\s*$", line):
            if not scopes:
                raise ValueError("Unmatched end while inventorying declarations")
            scopes.pop()
            continue
        match = re.match(r"^(?:theorem|lemma)\s+([A-Za-z0-9_'.]+)", line)
        if match:
            prefix = ".".join(name for kind, name in scopes if kind == "namespace")
            result.append((prefix + "." if prefix else "") + match.group(1))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", default=shutil.which("lean"))
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    if not args.lean:
        parser.error("Lean executable not found; supply --lean")
    lean = str(Path(args.lean).resolve())
    mathlib = args.mathlib.resolve()
    receipt = {"scope": "fresh Lean elaboration and public theorem axiom audit; not Collatz",
               "started_utc": datetime.now(timezone.utc).isoformat(),
               "commands": [], "sources": [], "success": False}
    args.receipt.parent.mkdir(parents=True, exist_ok=True)

    def run(argv: list[str], *, env=None, cwd=None) -> subprocess.CompletedProcess:
        process = subprocess.run(argv, capture_output=True, text=True, env=env, cwd=cwd)
        receipt["commands"].append({"argv": argv, "cwd": str(cwd) if cwd else None,
                                    "exit_code": process.returncode,
                                    "stdout": process.stdout, "stderr": process.stderr})
        if process.returncode:
            raise RuntimeError(f"Command failed: {argv}\n{process.stdout}\n{process.stderr}")
        return process

    try:
        version = run([lean, "--version"]).stdout.strip()
        receipt["lean_version"] = version
        if "version 4.34.1," not in version:
            raise RuntimeError(f"Expected Lean 4.34.1, observed {version}")
        revision = run(["git", "-C", str(mathlib), "rev-parse", "HEAD"]).stdout.strip()
        receipt["mathlib_revision"] = revision
        if revision != MATHLIB_REVISION:
            raise RuntimeError("Mathlib revision differs from the pinned source")
        dirty = run(["git", "-C", str(mathlib), "status", "--porcelain", "--untracked-files=no"]).stdout
        if dirty:
            raise RuntimeError("Mathlib has tracked changes")
        manifest_path = mathlib / "lake-manifest.json"
        manifest = json.loads(manifest_path.read_text())
        receipt["mathlib_manifest_sha256"] = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
        receipt["dependencies"] = []
        for package in manifest["packages"]:
            directory = mathlib / ".lake/packages" / package["name"]
            if not directory.is_dir():
                raise RuntimeError(f"Missing dependency checkout: {directory}")
            actual = run(["git", "-C", str(directory), "rev-parse", "HEAD"]).stdout.strip()
            tracked_changes = run(["git", "-C", str(directory), "status", "--porcelain",
                                   "--untracked-files=no"]).stdout
            if actual != package["rev"] or tracked_changes:
                raise RuntimeError(f"Dependency identity mismatch: {package['name']}")
            receipt["dependencies"].append({"name": package["name"], "revision": actual})

        files = sorted(ROOT.glob("*/*.lean"))
        modules = {path.stem: path for path in files}
        if len(modules) != len(files) or not files:
            raise RuntimeError("Missing sources or duplicate module names")
        dependencies = {name: set(re.findall(r"^import\s+([A-Za-z0-9_.]+)",
                                             path.read_text(), re.M)) & modules.keys()
                        for name, path in modules.items()}
        pending, order = set(modules), []
        while pending:
            ready = sorted(name for name in pending if not dependencies[name] & pending)
            if not ready:
                raise RuntimeError("Cyclic local imports")
            order.extend(ready)
            pending.difference_update(ready)
        names = []
        for name in order:
            source = modules[name]
            declarations = public_theorems(source.read_text())
            names.extend(declarations)
            receipt["sources"].append({"path": str(source.relative_to(ROOT)),
                "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "module": name, "public_theorems": declarations})
        if len(names) != len(set(names)):
            raise RuntimeError("Duplicate theorem inventory entry")

        with tempfile.TemporaryDirectory(prefix="collatz-ultra-lean-") as temporary:
            output = Path(temporary)
            library_paths = [output, mathlib / ".lake/build/lib/lean"]
            library_paths.extend(sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean")))
            env = dict(os.environ)
            env["LEAN_PATH"] = os.pathsep.join(map(str, library_paths))
            for name in order:
                source = modules[name]
                print(f"Compiling {source.relative_to(ROOT)}", flush=True)
                run([lean, "-DwarningAsError=true", "-DautoImplicit=false",
                     f"--root={source.parent}", "-o", str(output / f"{name}.olean"),
                     str(source)], env=env, cwd=source.parent)
            audit = output / "PublicAudit.lean"
            audit.write_text("\n".join(f"import {name}" for name in order) + "\n\n" +
                             "\n".join(f"#print axioms {name}" for name in names) + "\n")
            result = run([lean, "-DwarningAsError=true", "-DautoImplicit=false",
                          str(audit)], env=env, cwd=output)
            reports = re.findall(r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)",
                                 result.stdout)
            reported = {name for name, _ in reports}
            if reported != set(names):
                raise RuntimeError(f"Incomplete audit: missing {set(names)-reported}, extra {reported-set(names)}")
            all_axioms = {axiom.strip() for _, axiom_list in reports
                          for axiom in axiom_list.split(",") if axiom.strip()}
            receipt["public_theorem_count"] = len(names)
            receipt["transitive_axioms"] = sorted(all_axioms)
            if not all_axioms <= ALLOWED_AXIOMS:
                raise RuntimeError(f"Unexpected axiom dependencies: {all_axioms-ALLOWED_AXIOMS}")
            for entry in receipt["sources"]:
                if hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest() != entry["sha256"]:
                    raise RuntimeError(f"Source changed during build: {entry['path']}")
            receipt["success"] = True
            print(f"PASS: {len(order)} modules; {len(names)} public theorems; axioms {sorted(all_axioms)}")
    except Exception as error:
        receipt["error"] = str(error)
        print(f"FAIL: {error}", flush=True)
    finally:
        receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
        args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
