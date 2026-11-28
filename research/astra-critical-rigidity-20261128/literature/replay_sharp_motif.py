"""Strictly rebuild the pinned finite-router proof and the local specialization."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


HERE = Path(__file__).resolve().parent
PIN = "505d3fe782922904e86477990cc5d41e9110edda"
MATHLIB = "d13f23b723b8a846827a245b89c10fc7d3f11612"
MODULES = ("TernaryPowerLift", "TwoGapRouting", "FixedGapClock", "SharpClock",
           "AffineProfiles", "Threshold", "FirstArrival", "BlockClock")
ROOTS = ("Collatz.BlockClock.cover", "Collatz.SharpMotif.consecutive_subcritical_motifs")
AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def head(repo):
    return subprocess.check_output(["git", "-C", repo, "rev-parse", "HEAD"], text=True).strip()


def main():
    parser = argparse.ArgumentParser()
    for name in ("prior_repo", "mathlib", "lean", "receipt"):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    if head(args.mathlib) != MATHLIB:
        raise ValueError("Mathlib commit mismatch")
    prior = json.loads((HERE / "ROUTER_REPLAY.json").read_text())["prior_proof"]
    compiled = []
    with tempfile.TemporaryDirectory(prefix="collatz-fresh-router-") as tmp:
        stage = Path(tmp)
        roots = [stage, args.mathlib / ".lake/build/lib/lean"]
        roots.extend(sorted((args.mathlib / ".lake/packages").glob("*/.lake/build/lib/lean")))
        env = {**os.environ, "LEAN_PATH": os.pathsep.join(map(str, roots))}
        for name in (*MODULES, "SharpMotifInput", "Audit"):
            target = stage / (name + ".lean")
            if name in MODULES:
                unit = "merger/" + name + ".lean"
                source = f"{PIN}:research/astra-infinite-descent-20261127/{unit}"
                data = subprocess.check_output(["git", "-C", args.prior_repo, "show", source])
                target.write_bytes(data)
                if digest(target) != prior["matching_source_sha256"][unit]:
                    raise ValueError(f"source hash mismatch for {name}")
            elif name == "SharpMotifInput":
                shutil.copyfile(HERE / (name + ".lean"), target)
            else:
                target.write_text("import SharpMotifInput\n" + "\n".join(
                    f"#check {root}\n#print axioms {root}" for root in ROOTS) + "\n")
            cmd = [str(args.lean), "-j", "1", "-DwarningAsError=true", "-o",
                   name + ".olean", name + ".lean"]
            run = subprocess.run(cmd, cwd=stage, env=env, text=True, capture_output=True)
            print(name, run.returncode, flush=True)
            if run.returncode:
                raise RuntimeError(run.stdout + run.stderr)
            if "sorry" in run.stdout + run.stderr or run.stderr.strip():
                raise RuntimeError("unexpected compiler output: " + run.stdout + run.stderr)
            for group in re.findall(r"depends on axioms: \[([^\]]*)\]", run.stdout):
                if not set(group.split(", ")) <= AXIOMS:
                    raise ValueError("unexpected axiom: " + group)
            if name == "Audit":
                for root in ROOTS:
                    if not re.search(re.escape("'" + root + "' depends on axioms: ") +
                                     r"\[propext, Classical.choice, Quot.sound\]", run.stdout):
                        raise ValueError("missing standard audit for " + root)
            compiled.append({"module": name, "source_sha256": digest(target),
                             "command": cmd[1:], "exit_code": run.returncode,
                             "stdout": run.stdout})
    receipt = {"schema": "collatz-sharp-motif-lean/v1", "prior_commit": PIN,
               "mathlib_commit": MATHLIB, "compiler_sha256": digest(args.lean),
               "compiler": subprocess.check_output([args.lean, "--version"], text=True).strip(),
               "verified_roots": ROOTS, "runner_sha256": digest(Path(__file__)),
               "modules": compiled, "scope": "Fresh eight-module rebuild, local application, and isolated transitive axiom audit. The open-trajectory optimality proof is written."}
    args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
