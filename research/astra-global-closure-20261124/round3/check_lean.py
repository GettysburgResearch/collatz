"""Rebuild this packet and its two project imports in an empty olean directory.

Requires an already provisioned, compatible Lean/Mathlib environment.  It does
not download dependencies, and it records reuse of the Mathlib build cache.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--runtime-library", type=Path)
    parser.add_argument("--report-dir", required=True, type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    repo = here.parents[2]
    report = args.report_dir.resolve()
    report.mkdir(parents=True, exist_ok=True)
    sources = {p.stem: p for p in sorted(here.rglob("*.lean"))}
    new_names = set(sources)
    sources.update({
        "CycleShadows": here.parent / "structural/CycleShadows.lean",
        "ResidualDescent": here.parent / "closing/descent/ResidualDescent.lean",
    })
    order, visiting, done = [], set(), set()

    def visit(name):
        if name in done:
            return
        if name in visiting:
            raise RuntimeError("cyclic project import: " + name)
        visiting.add(name)
        for line in sources[name].read_text().splitlines():
            if line.startswith("import "):
                for dependency in line[7:].split():
                    if dependency in sources:
                        visit(dependency)
        visiting.remove(name)
        done.add(name)
        order.append(name)

    for name in sorted(new_names):
        visit(name)
    mathlib = args.mathlib.resolve()
    version = subprocess.check_output([str(args.lean), "--version"], text=True).strip()
    revision = subprocess.check_output(
        ["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True
    ).strip()
    receipt = {
        "scope": "Fresh build of this packet and its complete local project import closure; existing Mathlib and package oleans reused.",
        "lean_version": version, "mathlib_revision": revision,
        "lean_executable_sha256": digest(args.lean),
        "flags": ["-j1", "-DwarningAsError=true"], "modules": [],
        "status": "INCOMPLETE",
    }
    if args.runtime_library:
        library = args.runtime_library / "libleanshared.so"
        receipt["runtime_library_sha256"] = digest(library)
    with tempfile.TemporaryDirectory(prefix="collatz-round3-lean-") as tmp:
        env = os.environ.copy()
        paths = [Path(tmp), mathlib / ".lake/build/lib/lean"]
        paths += sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
        env["LEAN_PATH"] = os.pathsep.join(map(str, paths))
        if args.runtime_library:
            env["LD_LIBRARY_PATH"] = str(args.runtime_library)
        for name in order:
            source = sources[name]
            before = digest(source)
            command = [str(args.lean), "-j1", "-DwarningAsError=true",
                       "-o", str(Path(tmp) / (name + ".olean")), str(source)]
            result = subprocess.run(command, cwd=repo, env=env, text=True,
                                    capture_output=True, timeout=240)
            output = result.stdout + result.stderr
            log = report / (name + ".log")
            log.write_text(output)
            inventories = [line for line in output.splitlines()
                           if "depends on axioms" in line or "does not depend on any axioms" in line]
            allowed = {"propext", "Classical.choice", "Quot.sound"}
            unexpected = []
            for line in inventories:
                match = re.search(r"axioms: \[(.*)\]", line)
                if match:
                    unexpected += [s.strip() for s in match.group(1).split(",")
                                   if s.strip() and s.strip() not in allowed]
            passed = (result.returncode == 0 and before == digest(source)
                      and not unexpected and bool(inventories))
            receipt["modules"].append({
                "module": name, "new_module": name in new_names,
                "source": str(source.relative_to(repo)), "source_sha256": before,
                "compiler_exit": result.returncode, "source_unchanged": before == digest(source),
                "log": str(log.relative_to(repo)) if log.is_relative_to(repo) else str(log),
                "log_sha256": digest(log), "axiom_reports": inventories,
                "unexpected_axioms": unexpected, "passed": passed,
            })
            (report / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
            print(name + ": " + ("PASS" if passed else "FAIL"), flush=True)
            if not passed:
                print(output, flush=True)
                raise SystemExit(1)
    receipt["status"] = "PASS"
    receipt["new_module_count"] = len(new_names)
    receipt["new_selected_axiom_reports"] = sum(
        len(m["axiom_reports"]) for m in receipt["modules"] if m["new_module"]
    )
    (report / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("All source hashes and selected axiom inventories passed.", flush=True)


if __name__ == "__main__":
    main()
