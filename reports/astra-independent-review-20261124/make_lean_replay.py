"""Reconstruct the reviewed finite Lean kernels from their pinned Git objects."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess


IMPORTS = """import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Rat.Lemmas
"""
# Only these proof lines change. Binder names and mathematical statements are preserved.
REPAIRS = {
    "PhasePacking.lean": [
        ("mul_le_mul_right₀", "mul_le_mul_iff_left₀", 2),
        ("by field_simp; ring", "by field_simp", 2),
        ("mul_le_mul_of_nonneg_left ht (sq_nonneg y)",
         "mul_le_mul_of_nonneg_left ht (pow_nonneg ((by norm_num : (0 : ℚ) ≤ 1).trans hy) 2)", 1),
    ],
    "CarryCocycle.lean": [
        ("by gcongr <;> norm_num", "by gcongr; norm_num", 1),
        ("congr 1 <;> omega", "congr 1; omega", 1),
        ("rw [pow_add]; norm_num <;> ring", "rw [pow_add]; norm_num; ring", 1),
    ],
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_audited(repo, record):
    object_name = f"{record['source_commit']}:{record['source_path']}"
    git = ["git", "-C", str(repo)]
    blob = subprocess.check_output([*git, "rev-parse", object_name], text=True).strip()
    raw = subprocess.check_output([*git, "cat-file", "blob", object_name])
    if blob != record["git_blob"] or digest(raw) != record["sha256"]:
        raise ValueError(f"Source identity mismatch at {object_name}")
    body = raw.decode("utf-8")
    namespace = next(line.split()[1] for line in body.splitlines() if line.startswith("namespace "))
    audit = "".join(f"#print axioms {name}\n" for name in record["all_declarations"])
    audited = f"{body}\nnamespace {namespace}\n{audit}end {namespace}\n"
    if digest(audited.encode("utf-8")) != record["appended_sha256"]:
        raise ValueError(f"Axiom supplement mismatch at {object_name}")
    return audited


def repaired(name, source):
    for old, new, count in REPAIRS.get(name, ()):
        if source.count(old) != count:
            raise ValueError(f"Repair context mismatch for {name}: {old}")
        source = source.replace(old, new)
    return source


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True, help="Git checkout with the pinned PR objects")
    parser.add_argument("--out", type=Path, required=True, help="New output directory")
    parser.add_argument("--mode", choices=("original", "repaired-bundle"), required=True)
    args = parser.parse_args()
    records = json.loads(Path(__file__).with_name("declaration-manifest.json").read_text(encoding="utf-8"))
    outputs = {}
    bundle = IMPORTS + "\n"
    for record in records:
        name = Path(record["source_path"]).name
        audited = read_audited(args.repo, record)
        if args.mode == "original":
            outputs[Path(str(record["pr"])) / name] = audited
        else:
            _, body = repaired(name, audited).split("\n", 1)
            bundle += "\n" + body
    if args.mode == "repaired-bundle":
        outputs[Path("FixedBundle.lean")] = bundle
    args.out.mkdir(parents=True, exist_ok=False)
    for relative, content in outputs.items():
        path = args.out / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        data = content.encode("utf-8")
        path.write_bytes(data)
        print(f"{digest(data)}  {relative}")


if __name__ == "__main__":
    main()
