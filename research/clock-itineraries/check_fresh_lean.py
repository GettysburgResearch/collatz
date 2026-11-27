"""Build the proof packet from fresh Lean objects and audit the printed axioms."""
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

IMPORT = re.compile(r"^(?:(?:public|private) )?import (?:all )?(\w+)", re.MULTILINE)
PRINT = re.compile(r"^\s*#print axioms\s+\S+", re.MULTILINE)
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def compile_module(source, output, lean, env):
    obj = output / (source.stem + ".olean")
    command = [lean, "-j1", "-DwarningAsError=true", "-Dlinter.deprecated=false",
               "-DautoImplicit=false", "-DElab.async=false", "-o", str(obj), source.name]
    proc = subprocess.run(command, cwd=source.parent, env=env, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, encoding="utf8", errors="replace")
    log = proc.stdout
    (output / (source.stem + ".log")).write_text(log, encoding="utf8")
    if proc.returncode or not obj.is_file():
        raise RuntimeError(f"{source.name} failed\n{log[-5000:]}")
    reports = re.findall(r"depends on axioms:\s*\[([^\]]*)\]", log)
    clean = log.count("does not depend on any axioms")
    expected = len(PRINT.findall(source.read_text(encoding="utf8")))
    names = {n.strip() for report in reports for n in report.split(",") if n.strip()}
    if len(reports) + clean != expected or names - ALLOWED or "sorryAx" in log:
        raise RuntimeError(f"unexpected axiom report in {source.name}\n{log[-2500:]}")
    return {"file": source.name, "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "reports": expected, "axioms": sorted(names)}


def check(root, output, lean, mathlib, workers):
    files = list(root.glob("*.lean")) + list((root / "mathlib").glob("*.lean"))
    sources = {p.stem: p for p in files}
    if len(files) != len(sources):
        raise ValueError("Local module names must be unique")
    deps = {m: set(IMPORT.findall(p.read_text(encoding="utf8"))) & sources.keys()
            for m, p in sources.items()}
    lake = mathlib / ".lake"
    libs = [lake / "build/lib/lean"]
    if not (libs[0] / "Mathlib/Data/Fintype/Pi.olean").is_file():
        raise ValueError("Supply a built Mathlib checkout with its dependency cache")
    libs.extend(sorted((lake / "packages").glob("*/.lake/build/lib/lean")))
    env = dict(os.environ, LEAN_PATH=os.pathsep.join(str(p) for p in [output, *libs]))
    version = subprocess.check_output([lean, "--version"], text=True).strip()
    print(version, flush=True)
    completed, active = {}, {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        while len(completed) < len(sources):
            for m in sorted(sources.keys() - completed.keys() - set(active.values())):
                if deps[m] <= completed.keys():
                    job = pool.submit(compile_module, sources[m], output, lean, env)
                    active[job] = m
            if not active:
                raise RuntimeError("Local import dependency cycle")
            finished, _ = concurrent.futures.wait(active, return_when=concurrent.futures.FIRST_COMPLETED)
            for job in finished:
                m = active.pop(job)
                completed[m] = job.result()
                print(f"{m} passed ({completed[m]['reports']} axiom reports)", flush=True)
    total = sum(row["reports"] for row in completed.values())
    receipt = {"lean": version, "module_count": len(completed), "axiom_reports": total,
               "modules": [completed[m] for m in sorted(completed)]}
    print(f"{len(completed)} modules, {total} axiom reports", flush=True)
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", default="lean", help="Lean 4.34.1 executable")
    parser.add_argument("--mathlib", required=True, type=Path, help="built Mathlib checkout")
    parser.add_argument("--jobs", type=int, default=3)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    lean = shutil.which(args.lean)
    if not lean:
        parser.error("Lean executable not found")
    with tempfile.TemporaryDirectory(prefix="collatz-lean-") as tmp:
        receipt = check(Path(__file__).resolve().parent, Path(tmp), str(Path(lean).resolve()),
                        args.mathlib.resolve(), args.jobs)
    if args.receipt:
        args.receipt.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf8")


if __name__ == "__main__":
    main()
