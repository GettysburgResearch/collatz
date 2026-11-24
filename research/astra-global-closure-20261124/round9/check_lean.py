"""Rebuild the complete round-nine Lean proposal in an empty project cache.

Existing Mathlib/package oleans are reused. All eight project modules, including
the three byte-identical pinned dependencies, are rebuilt from visible source.
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
    parser.add_argument("--report-dir", required=True, type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    repo = here.parents[2]
    report = args.report_dir.resolve()
    report.mkdir(parents=True, exist_ok=True)
    # Topological order, with explicitly expected inventory counts.
    order = [
        ("vendor/TernaryItinerary.lean", 10, True),
        ("vendor/SourceDeletion.lean", 8, True),
        ("vendor/MinimumFailure.lean", 15, True),
        ("critical/CycleOrder.lean", 13, False),
        ("rows/FiniteSurvival.lean", 7, False),
        ("rows/BarrierEnvelope.lean", 6, False),
        ("arithmetic/LiteralCarry.lean", 9, False),
        ("formal/FinalProposal.lean", 8, False),
    ]
    files = {here / relative for relative, _, _ in order}
    if files != set(here.rglob("*.lean")):
        raise RuntimeError("unaccounted or missing Lean module")
    sources = {p.stem: p for p in files}
    if len(sources) != len(files):
        raise RuntimeError("duplicate module name")
    original = {p.stem: digest(p) for p in files}
    for source in files:
        for line in source.read_text().splitlines():
            if re.match(r"\s*(axiom|sorry|admit)\b", line):
                raise RuntimeError("unchecked declaration in " + str(source))
            if line.startswith("import "):
                for name in line[7:].split():
                    if name not in {"all", "Std", "Init"} and not name.startswith("Mathlib.") and name not in sources:
                        raise RuntimeError("unaccounted local import: " + name)
    for row in json.loads((here / "vendor/SOURCES.json").read_text()):
        if digest(repo / row["local"]) != row["sha256"]:
            raise RuntimeError("pinned dependency differs from recorded source")
    mathlib = args.mathlib.resolve()
    lean = args.lean.resolve()
    receipt = {
        "scope": "Eight project modules rebuilt from source in an empty project cache; existing Mathlib/package oleans reused. Five new modules and three pinned dependencies. Analytic theorems and full written cycle assembly are not claimed as Lean formalizations.",
        "lean_version": subprocess.check_output([str(lean), "--version"], text=True).strip(),
        "mathlib_revision": subprocess.check_output(["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip(),
        "lean_executable_sha256": digest(lean),
        "runtime_library_sha256": digest(lean.parent.parent / "lib/lean/libleanshared.so"),
        "runner_sha256": digest(Path(__file__)),
        "flags": ["-j1", "-DwarningAsError=true"],
        "modules": [], "status": "INCOMPLETE",
    }
    with tempfile.TemporaryDirectory(prefix="collatz-round9-lean-") as tmp:
        env = os.environ.copy()
        paths = [Path(tmp), mathlib / ".lake/build/lib/lean"]
        paths += sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
        env["LEAN_PATH"] = os.pathsep.join(map(str, paths))
        for relative, expected, dependency in order:
            source = here / relative
            name = source.stem
            result = subprocess.run(
                [str(lean), "-j1", "-DwarningAsError=true", "-o", str(Path(tmp) / (name + ".olean")), str(source)],
                cwd=repo, env=env, text=True, capture_output=True, timeout=300)
            output = result.stdout + result.stderr
            log = report / (name + ".log")
            log.write_text(output)
            inventories = [line for line in output.splitlines() if "depends on axioms" in line or "does not depend on any axioms" in line]
            unexpected = []
            for line in inventories:
                match = re.search(r"axioms: \[(.*)\]", line)
                if match:
                    unexpected += [s.strip() for s in match.group(1).split(",") if s.strip() and s.strip() not in {"propext", "Classical.choice", "Quot.sound"}]
            unchanged = original[name] == digest(source)
            passed = result.returncode == 0 and unchanged and not unexpected and len(inventories) == expected
            receipt["modules"].append({
                "module": name, "dependency": dependency,
                "source": str(source.relative_to(repo)), "source_sha256": original[name],
                "compiler_exit": result.returncode, "source_unchanged": unchanged,
                "log": str(log.relative_to(repo)) if log.is_relative_to(repo) else str(log),
                "log_sha256": digest(log), "axiom_reports": inventories,
                "expected_axiom_report_count": expected, "unexpected_axioms": unexpected, "passed": passed,
            })
            (report / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
            print(name + ": " + ("PASS" if passed else "FAIL"), flush=True)
            if not passed:
                print(output, flush=True)
                raise SystemExit(1)
    if any(original[name] != digest(source) for name, source in sources.items()):
        raise RuntimeError("project sources changed during replay")
    receipt.update(status="PASS", module_count=len(sources), new_module_count=5,
                   selected_axiom_report_count=sum(row[1] for row in order),
                   new_selected_axiom_report_count=sum(row[1] for row in order if not row[2]),
                   all_sources_unchanged=True)
    (report / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS: eight modules; 43 new and 33 dependency inventories; unchanged sources.", flush=True)


if __name__ == "__main__":
    main()
