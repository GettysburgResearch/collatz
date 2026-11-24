"""Rebuild all five round-seven modules from source in an empty project cache.

This uses an already provisioned Lean/Mathlib environment. Existing Mathlib
and package oleans are reused; no project olean is reused or downloaded.
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
    files = sorted(here.rglob("*.lean"))
    sources = {p.stem: p for p in files}
    expected = {"CompanionContent": 7, "UnitTripling": 9,
                "OddUnitLift": 5, "ShortSuffix": 12, "TriplingBoundary": 7}
    if len(sources) != len(files) or set(sources) != set(expected):
        raise RuntimeError("unexpected module set or duplicate module names")
    for source in files:
        for line in source.read_text().splitlines():
            if line.startswith("import ") and any(
                not name.startswith("Mathlib.") for name in line[7:].split()
            ):
                raise RuntimeError("unaccounted local import in " + str(source))
    original = {name: digest(source) for name, source in sources.items()}
    mathlib = args.mathlib.resolve()
    receipt = {
        "scope": "Fresh compilation of all five new modules, which have no local project imports; existing Mathlib/package oleans reused.",
        "lean_version": subprocess.check_output([str(args.lean), "--version"], text=True).strip(),
        "mathlib_revision": subprocess.check_output(
            ["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip(),
        "lean_executable_sha256": digest(args.lean),
        "runner_sha256": digest(Path(__file__)),
        "flags": ["-j1", "-DwarningAsError=true"],
        "modules": [], "status": "INCOMPLETE",
    }
    if args.runtime_library:
        receipt["runtime_library_sha256"] = digest(args.runtime_library / "libleanshared.so")
    with tempfile.TemporaryDirectory(prefix="collatz-round7-lean-") as tmp:
        env = os.environ.copy()
        paths = [Path(tmp), mathlib / ".lake/build/lib/lean"]
        paths += sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
        env["LEAN_PATH"] = os.pathsep.join(map(str, paths))
        if args.runtime_library:
            env["LD_LIBRARY_PATH"] = str(args.runtime_library)
        for name, source in sources.items():
            result = subprocess.run(
                [str(args.lean), "-j1", "-DwarningAsError=true",
                 "-o", str(Path(tmp) / (name + ".olean")), str(source)],
                cwd=repo, env=env, text=True, capture_output=True, timeout=240)
            output = result.stdout + result.stderr
            log = report / (name + ".log")
            log.write_text(output)
            inventories = [line for line in output.splitlines()
                           if "depends on axioms" in line or "does not depend on any axioms" in line]
            unexpected = []
            for line in inventories:
                match = re.search(r"axioms: \[(.*)\]", line)
                if match:
                    unexpected += [s.strip() for s in match.group(1).split(",")
                                   if s.strip() and s.strip() not in
                                   {"propext", "Classical.choice", "Quot.sound"}]
            unchanged = original[name] == digest(source)
            passed = (result.returncode == 0 and unchanged and not unexpected
                      and len(inventories) == expected[name])
            receipt["modules"].append({
                "module": name, "source": str(source.relative_to(repo)),
                "source_sha256": original[name], "compiler_exit": result.returncode,
                "source_unchanged": unchanged,
                "log": str(log.relative_to(repo)) if log.is_relative_to(repo) else str(log),
                "log_sha256": digest(log), "axiom_reports": inventories,
                "expected_axiom_report_count": expected[name],
                "unexpected_axioms": unexpected, "passed": passed,
            })
            (report / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
            print(name + ": " + ("PASS" if passed else "FAIL"), flush=True)
            if not passed:
                print(output, flush=True)
                raise SystemExit(1)
    if any(original[name] != digest(source) for name, source in sources.items()):
        raise RuntimeError("project sources changed during replay")
    receipt.update(status="PASS", module_count=len(sources),
                   selected_axiom_report_count=sum(expected.values()),
                   all_sources_unchanged=True)
    (report / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"PASS: {len(sources)} modules, {sum(expected.values())} selected inventories, unchanged sources.", flush=True)


if __name__ == "__main__":
    main()
