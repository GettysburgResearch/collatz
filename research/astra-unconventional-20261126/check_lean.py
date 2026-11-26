"""Rebuild every current module and its project imports in an empty output cache.

Also rebuild the retained full-domain conditional consumer. Mathlib and package
oleans are reused; this does not independently rebuild the compiler or Mathlib.
The receipt distinguishes kernel checks from the accompanying written proofs.
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


def imports(source):
    return [name for line in source.read_text().splitlines()
            if line.startswith("import ") for name in line[7:].split()
            if name != "all"]


def code_only(text):
    """Mask Lean's nested comments and string literals before the early token check."""
    out, i, depth, quoted = [], 0, 0, False
    while i < len(text):
        pair = text[i:i+2]
        if depth:
            if pair == "/-":
                depth += 1
                out.extend("  "); i += 2
            elif pair == "-/":
                depth -= 1
                out.extend("  "); i += 2
            else:
                out.append("\n" if text[i] == "\n" else " "); i += 1
        elif quoted:
            if text[i] == "\\":
                out.extend("  "); i += 2
            elif text[i] == '"':
                quoted = False
                out.append(" "); i += 1
            else:
                out.append("\n" if text[i] == "\n" else " "); i += 1
        elif pair == "/-":
            depth = 1
            out.extend("  "); i += 2
        elif pair == "--":
            end = text.find("\n", i)
            end = len(text) if end == -1 else end
            out.extend(" " * (end-i)); i = end
        elif text[i] == '"':
            quoted = True
            out.append(" "); i += 1
        else:
            out.append(text[i]); i += 1
    return "".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--package-cache", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    repo = here.parents[1]
    report = args.report_dir.resolve()
    report.mkdir(parents=True, exist_ok=True)
    pin = json.loads((here / "SOURCES.json").read_text())
    lean, mathlib = args.lean.resolve(), args.mathlib.resolve()
    packages = args.package_cache.resolve()
    current = set(here.rglob("*.lean"))
    candidates = {}
    for path in (repo / "research").rglob("*.lean"):
        candidates.setdefault(path.stem, []).append(path)
    sources, active, done = [], set(), set()

    def visit(path):
        if path in done:
            return
        if path in active:
            raise RuntimeError("Cyclic project import: " + str(path))
        active.add(path)
        for name in imports(path):
            if name in {"Init", "Std", "Lean"} or name.startswith(("Mathlib.", "Std.", "Lean.")):
                continue
            choices = candidates.get(name, [])
            if len(choices) != 1:
                raise RuntimeError("Ambiguous or missing project module: " + name)
            visit(choices[0])
        active.remove(path)
        done.add(path)
        sources.append(path)

    for path in sorted(current):
        visit(path)
    for consumer in pin["retained_conditional_consumers"]:
        visit(repo / consumer)
    if len({p.stem for p in sources}) != len(sources):
        raise RuntimeError("Duplicate compiled module name")
    before = {p: digest(p) for p in sources}
    pinned_dependencies = {row["local"]: row["sha256"] for row in pin["dependencies"]}
    actual_dependencies = {str(p.relative_to(repo)): before[p] for p in sources if p not in current}
    if actual_dependencies != pinned_dependencies:
        raise RuntimeError("Imported project dependencies differ from the source manifest")
    receipt = {
        "status": "INCOMPLETE",
        "scope": "All current Lean files and transitive project dependencies rebuilt from visible source. Selected declaration axiom inventories checked against the standard logical axioms. The retained universal convergence consumers still have OPEN FrontierMerger, or RecordLock and CycleExclusion, premises. The full spectral, lattice, sparse-correction, asymptotic and literature-dependent arguments are written mathematics except for the kernels identified in each lane.",
        "lean_version": subprocess.check_output([str(lean), "--version"], text=True).strip(),
        "mathlib_revision": subprocess.check_output(["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip(),
        "lean_executable_sha256": digest(lean),
        "runtime_library_sha256": digest(lean.parent.parent / "lib/lean/libleanshared.so"),
        "runner_sha256": digest(Path(__file__)),
        "flags": ["-j1", "-DwarningAsError=true", "-DautoImplicit=false"],
        "dependency_cache_policy": "Reuse the supplied Mathlib and external package oleans; the checkout revision is recorded, but no fresh dependency rebuild is claimed.",
        "package_cache_entries": sorted(p.parents[3].name for p in packages.glob("*/.lake/build/lib/lean")),
        "modules": [],
    }
    if pin["compiler_commit"] not in receipt["lean_version"]:
        raise RuntimeError("Unexpected Lean compiler commit")
    if receipt["mathlib_revision"] != pin["mathlib_commit"]:
        raise RuntimeError("Unexpected Mathlib checkout revision")
    for source in sources:
        if re.search(r"\b(sorry|admit|native_decide|sorryAx)\b|^\s*axiom\s", code_only(source.read_text()), re.MULTILINE):
            raise RuntimeError("Unchecked construct in source: " + str(source))
    inventory_re = re.compile(
        r"'([^']+)'\s+(?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)", re.MULTILINE)
    with tempfile.TemporaryDirectory(prefix="collatz-round14-lean-") as tmp:
        env = os.environ.copy()
        paths = [Path(tmp), mathlib / ".lake/build/lib/lean"]
        paths += sorted(packages.glob("*/.lake/build/lib/lean"))
        env["LEAN_PATH"] = os.pathsep.join(map(str, paths))
        for source in sources:
            expected = re.findall(r"^#print axioms (\S+)\s*$", source.read_text(), re.MULTILINE)
            if not expected or len(set(expected)) != len(expected):
                raise RuntimeError("Missing or duplicate selected inventory: " + str(source))
            result = subprocess.run(
                [str(lean), *receipt["flags"], "-o", str(Path(tmp) / (source.stem + ".olean")), str(source)],
                cwd=repo, env=env, text=True, capture_output=True, timeout=300)
            output = result.stdout + result.stderr
            log = report / (source.stem + ".log")
            log.write_text(output)
            found = inventory_re.findall(output)
            unexpected = sorted({a.strip() for _, values in found for a in values.split(",")
                                 if a.strip() and a.strip() not in {"propext", "Classical.choice", "Quot.sound"}})
            reported = [name for name, _ in found]
            passed = (result.returncode == 0 and before[source] == digest(source)
                      and not unexpected and "sorryAx" not in output
                      and len(reported) == len(expected)
                      and all(r == e or r.endswith("." + e) for r, e in zip(reported, expected)))
            receipt["modules"].append({
                "source": str(source.relative_to(repo)), "dependency": source not in current,
                "source_sha256": before[source], "compiler_exit": result.returncode,
                "source_unchanged": before[source] == digest(source),
                "log": str(log.relative_to(repo)) if log.is_relative_to(repo) else str(log),
                "log_sha256": digest(log),
                "axiom_inventories": [{"declaration": name, "axioms": [a.strip() for a in values.split(",") if a.strip()]}
                                     for name, values in found],
                "expected_inventories": expected, "unexpected_axioms": unexpected,
                "passed": passed,
            })
            (report / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
            print(source.stem + ": " + ("PASS" if passed else "FAIL"), flush=True)
            if not passed:
                print(output, flush=True)
                raise SystemExit(1)
    if current != set(here.rglob("*.lean")) or any(before[p] != digest(p) for p in sources):
        raise RuntimeError("Source set changed during replay")
    receipt.update(
        status="PASS", module_count=len(sources), new_module_count=len(current),
        selected_axiom_report_count=sum(len(row["axiom_inventories"]) for row in receipt["modules"]),
        new_selected_axiom_report_count=sum(len(row["axiom_inventories"]) for row in receipt["modules"] if not row["dependency"]),
        all_sources_unchanged=True)
    (report / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS: " + str(len(sources)) + " modules; " + str(receipt["selected_axiom_report_count"]) + " selected inventories.", flush=True)


if __name__ == "__main__":
    main()
