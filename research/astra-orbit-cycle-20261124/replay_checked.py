"""Replay the published Lean copies from inside the pinned Mathlib checkout."""
import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
EXPECTED_LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
EXPECTED_MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
ALLOWED = {"propext", "Quot.sound", "Classical.choice"}


def declared_axioms(output):
    tables = {}
    for name, dependencies in re.findall(
        r"'([^']+)' depends on axioms: \[([^\]]*)\]", output
    ):
        tables[name.split(".")[-1]] = {a.strip() for a in dependencies.split(",")}
    for name in re.findall(r"'([^']+)' does not depend on any axioms", output):
        tables[name.split(".")[-1]] = set()
    return tables


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mathlib", type=pathlib.Path)
    parser.add_argument("--sources", type=pathlib.Path, default=ROOT / "audited_lean")
    parser.add_argument("--receipt", type=pathlib.Path, default=ROOT.parents[1] / "reports/astra-review-20261124/COMPILE_RECEIPT.json")
    args = parser.parse_args()
    mathlib = args.mathlib.resolve()
    def run(*cmd):
        return subprocess.run(cmd, cwd=mathlib, capture_output=True, text=True, check=True).stdout.strip()
    if run("git", "rev-parse", "HEAD") != EXPECTED_MATHLIB_COMMIT:
        sys.exit("Mathlib commit differs from the audit pin")
    if run("lake", "env", "lean", "-g") != EXPECTED_LEAN_COMMIT:
        sys.exit("Lean compiler commit differs from the audit pin")

    for item in json.loads(args.receipt.read_text()):
        src = (args.sources / item["checked"]).resolve()
        if hashlib.sha256(src.read_bytes()).hexdigest() != item["checked_sha256"]:
            sys.exit(f"Source bytes differ: {src.name}")
        result = subprocess.run(
            ["lake", "env", "lean", "-j1", "-DwarningAsError=true", str(src)],
            cwd=mathlib, capture_output=True, text=True,
        )
        output = result.stdout + result.stderr
        print(output, end="")
        if result.returncode:
            sys.exit(f"Lean exited {result.returncode} for {src.name}")
        found = declared_axioms(output)
        expected = {name.split(".")[-1]: set(values) for name, values in item["axioms"].items()}
        if found != expected or not all(values <= ALLOWED for values in found.values()):
            sys.exit(f"Printed declarations or axiom sets differ: {src.name}")
        print(f"{src.name}: passed, {len(found)} declarations")


if __name__ == "__main__":
    main()
