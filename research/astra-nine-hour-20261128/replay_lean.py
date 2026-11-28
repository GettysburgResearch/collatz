#!/usr/bin/env python3
"""Strictly rebuild this packet in fresh storage and audit its declarations.

Adapted from PR212 at 505d3fe782922904e86477990cc5d41e9110edda,
research/astra-infinite-descent-20261127/replay_lean.py. The all-declaration
audit and dependency checks are retained; this pass uses a new packet root.

Requires the pinned Lean release and an already built, clean Mathlib checkout.
This script never downloads dependencies or changes the source checkout.
The receipt covers these source files, not a fresh build of all of Mathlib.
"""

from __future__ import annotations

import argparse
import fcntl
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time


PACKET = Path(__file__).resolve().parent
MATHLIB_SHA = "d13f23b723b8a846827a245b89c10fc7d3f11612"
LEAN_VERSION = "4.34.1"
LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(directory: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(directory), *args], text=True
    ).strip()


def dependency(directory: Path, expected: str) -> dict:
    head = git(directory, "rev-parse", "HEAD")
    dirty = git(directory, "status", "--porcelain", "--untracked-files=no")
    require(head == expected, f"Unexpected dependency head: {directory}: {head}")
    require(not dirty, f"Tracked dependency changes: {directory}: {dirty}")
    return {"path": str(directory), "head": head, "tracked_clean": True}


def ordered_sources() -> list[Path]:
    sources = sorted(PACKET.rglob("*.lean"))
    by_name = {p.stem: p for p in sources}
    require(len(by_name) == len(sources), "Duplicate flat Lean module names")
    require(bool(sources), "No Lean sources")
    ordered: list[Path] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(name: str) -> None:
        if name in visited:
            return
        require(name not in visiting, f"Cyclic local import: {name}")
        visiting.add(name)
        source = by_name[name]
        # Lean's module system also permits `public import` and `import all`.
        # Both carry the same local build dependency, while `all` controls
        # visibility rather than naming another module.
        for match in re.finditer(
                r"^[ \t]*(?:public\s+)?import\s+(?:all\s+)?([^\n]+)",
                source.read_text(), re.M):
            for imported in match.group(1).split("--")[0].split():
                if imported in by_name:
                    visit(imported)
                else:
                    require(imported.startswith(("Mathlib.", "Lean.", "Init.", "Std."))
                            or imported in {"Mathlib", "Lean", "Init", "Std"},
                            f"Unaccounted local dependency: {source}: {imported}")
        visiting.remove(name)
        visited.add(name)
        ordered.append(source)

    for name in sorted(by_name):
        visit(name)
    return ordered


def audit_source(modules: list[str]) -> str:
    quoted = ", ".join("`" + name for name in modules)
    # A legacy (non-`module`) root loads the private level transitively for
    # both legacy and new module files. See Lean.Environment.importModules.
    # This also permits the packet's deliberate mix of the two file styles.
    return "\n".join("import " + name for name in modules) + r'''
import Lean.Util.CollectAxioms
import Lean.Elab.Command
set_option autoImplicit false
set_option warningAsError true
open Lean Elab Command in
run_cmd do
  let env ← getEnv
  let selected : Array Name := #[''' + quoted + r''']
  let allowed : Array Name := #[`propext, `Classical.choice, `Quot.sound]
  let mut count : Nat := 0
  for (name, _) in env.constants.toList do
    if let some idx := env.getModuleIdxFor? name then
      let origin := env.header.moduleNames[idx]!
      if selected.contains origin then
        let axioms ← collectAxioms name
        let unexpected := axioms.filter (fun a => !allowed.contains a)
        unless unexpected.isEmpty do
          throwError "Unexpected axioms for {name}: {unexpected}"
        count := count + 1
        let row := Json.mkObj [
          ("module", toJson origin.toString),
          ("declaration", toJson name.toString),
          ("axioms", toJson ((axioms.qsort Name.lt).map Name.toString))]
        logInfo m!"AXIOM_ROW {row.compress}"
  if count == 0 then throwError "No packet declarations were audited"
  logInfo m!"AXIOM_COUNT {count}"
'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True,
                        help="JSON receipt path; use a path outside the checkout")
    parser.add_argument("--build-parent", type=Path,
                        help="Parent for a new, uniquely named build directory")
    parser.add_argument("--lock", type=Path,
                        help="Optional shared lock; serializes each compiler invocation")
    parser.add_argument("--timeout", type=int, default=300,
                        help="Seconds allowed for each compiler invocation")
    parser.add_argument("--jobs", type=int, default=1,
                        help="Lean worker count; packet modules still build sequentially")
    args = parser.parse_args()
    args.lean = args.lean.resolve()
    args.mathlib = args.mathlib.resolve()
    receipt: dict = {
        "schema": "collatz-nine-hour-lean/v1",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Fresh strict compilation of this packet and transitive axiom audit; "
                 "not a fresh Mathlib build or proof of Collatz",
        "passed": False,
        "modules": [],
    }
    try:
        version = subprocess.check_output([str(args.lean), "--version"], text=True).strip()
        require(f"version {LEAN_VERSION}" in version, f"Wrong Lean: {version}")
        require(LEAN_COMMIT[:12] in version, f"Wrong Lean compiler commit: {version}")
        receipt["lean"] = {"path": str(args.lean), "version": version,
                           "binary_sha256": digest(args.lean)}
        receipt["mathlib"] = dependency(args.mathlib, MATHLIB_SHA)
        manifest_path = args.mathlib / "lake-manifest.json"
        manifest = json.loads(manifest_path.read_text())
        receipt["mathlib_manifest_sha256"] = digest(manifest_path)
        packages = args.mathlib / manifest["packagesDir"]
        receipt["dependencies"] = [
            dependency(packages / p["name"], p["rev"])
            for p in manifest["packages"]
        ]
        sources = ordered_sources()
        before = {str(p.relative_to(PACKET)): digest(p) for p in sources}
        build = Path(tempfile.mkdtemp(prefix="collatz-nine-hour-",
                                     dir=args.build_parent))
        receipt["build_directory"] = str(build)
        paths = [build, args.mathlib / ".lake/build/lib/lean"]
        paths.extend(packages / p["name"] / ".lake/build/lib/lean"
                     for p in manifest["packages"])
        env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, paths)))
        require(args.jobs > 0, "Lean worker count must be positive")
        flags = [f"-j{args.jobs}", "-DElab.async=false", "-DwarningAsError=true", "-DautoImplicit=false",
                 "-DmaxHeartbeats=4000000"]
        receipt["flags"] = flags

        def compile_file(source: Path, relative: str) -> dict:
            started = time.monotonic()
            print(f"Building {source.stem}", flush=True)
            # Every packet import uses a flat module name. Set the compiler's
            # package root to this source's parent so that private declaration
            # names agree with that import, including nested pinned sources.
            command = [str(args.lean), *flags, "-R", str(source.parent),
                       "-o", str(build / (source.stem + ".olean")),
                       str(source)]
            # Lean requires the input file to lie inside its selected root.
            # The generated audit intentionally lives in the fresh build
            # directory outside the immutable source checkout.
            compile_root = build if source.parent == build else PACKET
            if args.lock is not None:
                args.lock.parent.mkdir(parents=True, exist_ok=True)
                with args.lock.open("a") as lock_file:
                    fcntl.flock(lock_file, fcntl.LOCK_EX)
                    result = subprocess.run(command, cwd=compile_root, env=env,
                                            text=True, capture_output=True,
                                            timeout=args.timeout)
            else:
                result = subprocess.run(command, cwd=compile_root, env=env,
                                        text=True, capture_output=True,
                                        timeout=args.timeout)
            row = {"source": relative, "sha256": digest(source),
                   "exit_code": result.returncode,
                   "seconds": round(time.monotonic() - started, 4),
                   "module_root": str(source.parent),
                   "stdout": result.stdout, "stderr": result.stderr}
            print(f"{source.stem}: exit {result.returncode}, {row['seconds']}s", flush=True)
            return row

        for source in sources:
            row = compile_file(source, str(source.relative_to(PACKET)))
            receipt["modules"].append(row)
            require(row["exit_code"] == 0,
                    f"Lean failed: {row['source']}\n{row['stdout']}\n{row['stderr']}")

        audit = build / "PacketAxiomAudit.lean"
        audit.write_text(audit_source([p.stem for p in sources]))
        row = compile_file(audit, "<generated-all-declaration-audit>")
        receipt["audit_command"] = row
        require(row["exit_code"] == 0,
                f"Axiom audit failed\n{row['stdout']}\n{row['stderr']}")
        audited = [json.loads(line.split("AXIOM_ROW ", 1)[1])
                   for line in row["stdout"].splitlines() if "AXIOM_ROW " in line]
        require(bool(audited), "No machine-readable axiom audit rows")
        require({item["module"] for item in audited} == {p.stem for p in sources},
                "A packet module has no declarations in the aggregate audit")
        receipt["declarations"] = sorted(audited, key=lambda item: item["declaration"])
        receipt["module_declaration_counts"] = {
            source.stem: sum(item["module"] == source.stem for item in audited)
            for source in sources
        }
        receipt["private_declaration_count"] = sum(
            item["declaration"].startswith("_private.") for item in audited)
        # Preserve all decoded rows once, rather than duplicating the same
        # declaration list in one very large escaped stdout string.
        audit_stdout = receipt["audit_command"].pop("stdout")
        receipt["audit_command"]["stdout_sha256"] = hashlib.sha256(audit_stdout.encode()).hexdigest()
        receipt["audit_command"]["stdout_rows_decoded_in"] = "declarations"
        receipt["audit_command"]["count_message"] = [
            line for line in audit_stdout.splitlines() if "AXIOM_COUNT " in line
        ]
        receipt["declaration_count"] = len(audited)
        receipt["module_count"] = len(sources)
        after_sources = ordered_sources()
        after = {str(p.relative_to(PACKET)): digest(p) for p in after_sources}
        require(before == after, "Packet sources changed during the rebuild")
        receipt["source_hashes"] = before
        receipt["passed"] = True
        print(f"PASS: {len(sources)} modules, {len(audited)} declarations", flush=True)
    except Exception as exc:
        receipt["error"] = str(exc)
        print(f"FAIL: {exc}", flush=True)
    finally:
        receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
