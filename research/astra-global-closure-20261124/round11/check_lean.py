"""Rebuild all round-eleven project Lean modules in an empty project output cache.

The three pinned PR192 dependencies and round-ten TowerClock are rebuilt too. Cached Mathlib and package
oleans are reused; neither the compiler nor Mathlib is rebuilt by this script.
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
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    repo = here.parents[2]
    report = args.report_dir.resolve()
    report.mkdir(parents=True, exist_ok=True)
    order = [
        ("../round9/vendor/SourceDeletion.lean", True),
        ("../round9/vendor/MinimumFailure.lean", True),
        ("../round10/vendor/SmoothCore.lean", True),
        ("../round10/closure/TowerClock.lean", True),
        ("closure/AnchorDescent.lean", False),
        ("closure/AnchorControl.lean", False),
        ("diagonal/TraceCensus.lean", False),
        ("cycle/LocalDenominator.lean", False),
        ("formal/TemplateChain.lean", False),
        ("formal/FinalProposal.lean", False),
    ]
    sources = [(here / relative).resolve() for relative, _ in order]
    local = {p for p in sources if p.is_relative_to(here)}
    if local != set(here.rglob("*.lean")):
        raise RuntimeError("Unaccounted round-eleven Lean file")
    if len({p.stem for p in sources}) != len(sources):
        raise RuntimeError("Duplicate local Lean module name")
    before = {p: digest(p) for p in sources}
    for row in json.loads((here / "SOURCES.json").read_text())["dependencies"]:
        if digest(repo / row["local"]) != row["sha256"]:
            raise RuntimeError("Pinned source hash differs: " + row["local"])
    lean = args.lean.resolve()
    mathlib = args.mathlib.resolve()
    receipt = {
        "status": "INCOMPLETE",
        "scope": "Ten project modules, including four unchanged dependencies, rebuilt from visible source. The source-qualified S-unit finiteness, complete analytic cycle criterion, trace recurrence and external floor coverage remain written mathematics. The final universal consumer has an explicit OPEN premise.",
        "lean_version": subprocess.check_output([str(lean), "--version"], text=True).strip(),
        "mathlib_revision": subprocess.check_output(["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip(),
        "lean_executable_sha256": digest(lean),
        "runtime_library_sha256": digest(lean.parent.parent / "lib/lean/libleanshared.so"),
        "runner_sha256": digest(Path(__file__)),
        "flags": ["-j1", "-DwarningAsError=true"],
        "modules": [],
    }
    pin = json.loads((here / "SOURCES.json").read_text())
    if pin["compiler_commit"] not in receipt["lean_version"]:
        raise RuntimeError("Unexpected Lean compiler commit")
    if receipt["mathlib_revision"] != pin["mathlib_commit"]:
        raise RuntimeError("Unexpected Mathlib revision")
    module_names = {p.stem for p in sources}
    for source in sources:
        for line in source.read_text().splitlines():
            if re.match(r"\s*(axiom|sorry|admit)\b", line):
                raise RuntimeError("Unchecked declaration: " + str(source))
            if line.startswith("import "):
                for name in line[7:].split():
                    if name not in {"all", "Std", "Init"} and not name.startswith("Mathlib.") and name not in module_names:
                        raise RuntimeError("Unaccounted import: " + name)
    with tempfile.TemporaryDirectory(prefix="collatz-round11-lean-") as tmp:
        env = os.environ.copy()
        paths = [Path(tmp), mathlib / ".lake/build/lib/lean"]
        paths += sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
        env["LEAN_PATH"] = os.pathsep.join(map(str, paths))
        for source, (_, dependency) in zip(sources, order):
            expected = re.findall(r"^#print axioms (\S+)\s*$", source.read_text(), re.MULTILINE)
            if not expected or len(set(expected)) != len(expected):
                raise RuntimeError("Missing or duplicate selected inventory")
            result = subprocess.run(
                [str(lean), "-j1", "-DwarningAsError=true", "-o", str(Path(tmp) / (source.stem + ".olean")), str(source)],
                cwd=repo, env=env, text=True, capture_output=True, timeout=300)
            output = result.stdout + result.stderr
            log = report / (source.stem + ".log")
            log.write_text(output)
            inventories = [line for line in output.splitlines() if "depends on axioms" in line or "does not depend on any axioms" in line]
            unexpected = []
            reported = []
            for line in inventories:
                name = re.search(r"^'([^']+)'", line)
                if name:
                    reported.append(name.group(1).split(".")[-1])
                axioms = re.search(r"axioms: \[(.*)\]", line)
                if axioms:
                    unexpected += [s.strip() for s in axioms.group(1).split(",") if s.strip() and s.strip() not in {"propext", "Classical.choice", "Quot.sound"}]
            passed = result.returncode == 0 and before[source] == digest(source) and not unexpected and reported == expected
            receipt["modules"].append({
                "source": str(source.relative_to(repo)), "dependency": dependency,
                "source_sha256": before[source], "compiler_exit": result.returncode,
                "source_unchanged": before[source] == digest(source),
                "log": str(log.relative_to(repo)) if log.is_relative_to(repo) else str(log),
                "log_sha256": digest(log), "axiom_reports": inventories,
                "expected_inventories": expected, "unexpected_axioms": unexpected,
                "passed": passed,
            })
            (report / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
            print(source.stem + ": " + ("PASS" if passed else "FAIL"), flush=True)
            if not passed:
                print(output, flush=True)
                raise SystemExit(1)
    if any(before[p] != digest(p) for p in sources):
        raise RuntimeError("Source changed during replay")
    receipt.update(
        status="PASS", module_count=len(sources), new_module_count=6,
        selected_axiom_report_count=sum(len(row["axiom_reports"]) for row in receipt["modules"]),
        new_selected_axiom_report_count=sum(len(row["axiom_reports"]) for row in receipt["modules"] if not row["dependency"]),
        all_sources_unchanged=True)
    (report / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS: ten modules; " + str(receipt["selected_axiom_report_count"]) + " selected inventories; sources unchanged.", flush=True)


if __name__ == "__main__":
    main()
