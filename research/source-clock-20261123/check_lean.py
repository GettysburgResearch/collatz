#!/usr/bin/env python3
"""Compile this packet's new Lean modules and audit every public theorem.

Reuses installed, pinned Mathlib dependencies. Does not download or rebuild
historical project proofs, and does not certify the written infinite arguments.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time


STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def overlay_mathlib(cache: Path, output: Path, modules: list[dict]) -> None:
    """Keep cached dependencies read-only while rebuilding selected modules.

    Lean resolves a package from its first root, so a partial Mathlib overlay
    must also expose the installed files. Only ancestor directories of the
    rebuilt modules are real directories; unrelated cache entries are links.
    """
    stems = {item["module"].removeprefix("Mathlib.").replace(".", "/")
             for item in modules}
    local_dirs = {""}
    for stem in stems:
        parent = Path(stem).parent
        while str(parent) != ".":
            local_dirs.add(parent.as_posix())
            parent = parent.parent

    def expose(relative: str) -> None:
        target = output / relative
        target.mkdir(parents=True, exist_ok=True)
        source = cache / relative
        if not source.is_dir():
            return
        for entry in source.iterdir():
            rel = (Path(relative) / entry.name).as_posix()
            if rel in local_dirs:
                expose(rel)
            elif any(rel == stem or rel.startswith(stem + ".") for stem in stems):
                continue
            else:
                (output / rel).symlink_to(entry, target_is_directory=entry.is_dir())

    expose("")
    for relative in local_dirs:
        (output / relative).mkdir(parents=True, exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    root = packet.parent.parent
    deps = json.loads((packet / "DEPENDENCIES.json").read_text())
    inventory = json.loads((packet / "THEOREMS.json").read_text())
    lean = args.lean.resolve()
    mathlib = args.mathlib.resolve()
    report_dir = args.report_dir.resolve()
    report_dir.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env["PATH"] = str(lean.parent) + os.pathsep + env.get("PATH", "")
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if (f"version {deps['lean_version']}," not in version
            or deps["lean_commit"] not in version):
        raise SystemExit(f"Wrong Lean compiler: {version}")
    pin = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib,
                                  text=True).strip()
    if pin != deps["mathlib_commit"]:
        raise SystemExit(f"Wrong Mathlib commit: {pin}")
    dirty = subprocess.check_output(["git", "diff", "HEAD", "--name-only"],
                                    cwd=mathlib, text=True)
    if dirty.strip():
        raise SystemExit("Mathlib has modified tracked sources")
    bootstrap = deps.get("fresh_mathlib_dependencies", [])
    for item in deps["direct_mathlib_imports"] + bootstrap:
        if digest(mathlib / item["source_path"]) != item["sha256"]:
            raise SystemExit(f"Mathlib import mismatch: {item['module']}")
    inherited = subprocess.check_output(
        [str(lean.with_name("lake")), "env", "printenv", "LEAN_PATH"],
        cwd=mathlib, env=env, text=True).strip()
    expected_names: list[str] = []
    modules: list[str] = []
    for item in inventory["modules"]:
        module = item["module"]
        source = (packet / "lean" / f"{module}.lean").read_text()
        if re.findall(r"^theorem\s+(\w+)", source, re.M) != item["theorems"]:
            raise SystemExit(f"Theorem inventory mismatch: {module}")
        expected_names.extend(
            f"CollatzSourceClock.{module}.{name}" for name in item["theorems"])
        modules.append(module)
    if len(expected_names) != inventory["public_theorem_count"]:
        raise SystemExit("Theorem count mismatch")
    modules.append(inventory["audit_module"])
    original_hashes = {module: digest(packet / "lean" / f"{module}.lean")
                       for module in modules}
    report = {
        "status": "running", "lean_version": version,
        "lean_binary_sha256": digest(lean), "mathlib_commit": pin,
        "direct_imports": deps["direct_mathlib_imports"],
        "fresh_mathlib_dependencies": [],
        "fresh_local_output": True, "warnings_as_errors": True,
        "new_public_theorem_count": len(expected_names),
        "historical_project_modules_rebuilt": 0,
        "scope": inventory["scope"], "modules": [],
    }
    logs: list[str] = []

    def save() -> None:
        (report_dir / "lean-check.json").write_text(json.dumps(report, indent=2) + "\n")
        (report_dir / "lean-build.log").write_text("\n".join(logs).rstrip() + "\n")

    save()
    try:
        with tempfile.TemporaryDirectory(prefix="collatz-source-clock-lean-") as out:
            env["LEAN_PATH"] = out + os.pathsep + inherited
            if bootstrap:
                cache = mathlib / ".lake/build/lib/lean/Mathlib"
                if not cache.is_dir():
                    raise RuntimeError(f"Installed Mathlib cache missing: {cache}")
                overlay_mathlib(cache, Path(out) / "Mathlib", bootstrap)
            for item in bootstrap:
                source = mathlib / item["source_path"]
                target = Path(out) / (item["module"].replace(".", "/") + ".olean")
                target.parent.mkdir(parents=True, exist_ok=True)
                started = time.monotonic()
                result = subprocess.run(
                    [str(lean), "-j1", "-DwarningAsError=true", "-o",
                     str(target), str(source)],
                    cwd=mathlib, env=env, text=True,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=240)
                seconds = round(time.monotonic() - started, 3)
                report["fresh_mathlib_dependencies"].append({
                    **item, "exit_code": result.returncode, "seconds": seconds})
                logs.append(f"DEPENDENCY {item['module']}\n{result.stdout}")
                save()
                print(f"{item['module']}: exit={result.returncode}, seconds={seconds}",
                      flush=True)
                if result.returncode:
                    print(result.stdout, flush=True)
                    raise RuntimeError(f"Dependency compilation failed: {item['module']}")
            for module in modules:
                source = packet / "lean" / f"{module}.lean"
                started = time.monotonic()
                result = subprocess.run(
                    [str(lean), "-j1", "-DwarningAsError=true", "-o",
                     str(Path(out) / f"{module}.olean"), str(source)],
                    cwd=source.parent, env=env, text=True,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=240)
                seconds = round(time.monotonic() - started, 3)
                axioms = sorted({a.strip()
                                 for group in re.findall(r"depends on axioms:\s*\[([^]]*)\]",
                                                         result.stdout, re.S)
                                 for a in group.split(",") if a.strip()})
                audited = re.findall(r"'([^']+)' (?:depends on axioms:|does not depend on any axioms)",
                                     result.stdout)
                report["modules"].append({
                    "module": module, "path": str(source.relative_to(root)),
                    "sha256": digest(source), "exit_code": result.returncode,
                    "seconds": seconds, "axioms": axioms,
                    "audited_declarations": audited,
                })
                logs.append(f"MODULE {module}\n{result.stdout}")
                save()
                print(f"{module}: exit={result.returncode}, seconds={seconds}", flush=True)
                if result.returncode:
                    print(result.stdout, flush=True)
                    raise RuntimeError(f"Compilation failed: {module}")
                if not set(axioms) <= STANDARD_AXIOMS:
                    raise RuntimeError(f"Unexpected axiom dependency: {module}")
                if module == inventory["audit_module"] and audited != expected_names:
                    raise RuntimeError("Audit did not cover the exact public theorem inventory")
        if any(digest(packet / "lean" / f"{module}.lean") != sha
               for module, sha in original_hashes.items()):
            raise RuntimeError("Source changed during compilation")
        if any(digest(mathlib / item["source_path"]) != item["sha256"]
               for item in deps["direct_mathlib_imports"] + bootstrap):
            raise RuntimeError("Mathlib source changed during compilation")
        report["status"] = "passed"
        save()
        print(f"Fresh compilation and all {len(expected_names)} theorem audits passed.")
    except BaseException as error:
        report["status"] = "failed"
        report["error"] = str(error)
        save()
        raise


if __name__ == "__main__":
    main()
