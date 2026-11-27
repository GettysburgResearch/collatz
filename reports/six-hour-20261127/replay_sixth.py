"""Replay the exact new Lean sources and deterministic finite research controls.

This checks the recorded Lean implications and deterministic finite statements.
It does not prove either open extinction estimate, formalize the external
analytic source counts, or settle Collatz.
The output directory must be new and outside the repository.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time


BASE = Path(".")
LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}
MODULES = [
    ('research/unconventional-20261126/CoreBranching.lean', 12),
    ('research/six-hour-20261127/coupling/PeakRigidity.lean', 4),
    ('research/six-hour-20261127/coupling/AnchorRoute.lean', 8),
    ('research/six-hour-20261127/coupling/NativeShadow.lean', 6),
    ('research/six-hour-20261127/coupling/NativeVisitors.lean', 3),
    ('research/six-hour-20261127/coupling/AnchorLookup.lean', 1),
    ('research/six-hour-20261127/coupling/NativeClassification.lean', 6),
    ('research/six-hour-20261127/escape/SignedHeightGauge.lean', 4),
    ('research/six-hour-20261127/escape/RationalSourceSector.lean', 6),
    ('research/six-hour-20261127/arithmetic/RivalPressure.lean', 3),
]
CONTROLS = [
    ('research/six-hour-20261127/coupling/check_native_shadow.py',
     'research/six-hour-20261127/coupling/NATIVE_SHADOW_CONTROLS.json', []),
    ('research/six-hour-20261127/escape/check_signed_heights.py',
     'research/six-hour-20261127/escape/SIGNED_HEIGHT_CONTROLS.json', []),
    ('research/six-hour-20261127/escape/check_rational_sector.py',
     'research/six-hour-20261127/escape/RATIONAL_SECTOR_CONTROLS.json', []),
    ('research/six-hour-20261127/arithmetic/check_rival_pressure.py',
     'research/six-hour-20261127/arithmetic/RIVAL_PRESSURE_CONTROLS.json', []),
]
EXTRA_INPUTS = [
    'research/six-hour-20261127/arithmetic/check_four_copy_tails.py',
    'research/six-hour-20261127/arithmetic/rival_pressure.cpp',
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def git(directory, *args):
    return subprocess.check_output(["git", "-C", str(directory), *args], text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--only", choices=["all", "lean", "controls"], default="all")
    args = parser.parse_args()
    modules = MODULES
    controls = CONTROLS
    repo, out, ml = args.repo.resolve(), args.out.resolve(), args.mathlib.resolve()
    require(not out.is_relative_to(repo), "Output must be outside the checkout")
    require(args.jobs > 0, "jobs must be positive")
    out.mkdir(parents=True, exist_ok=False)
    build = out / "build"
    build.mkdir()
    manifest = (ml / "lake-manifest.json").read_bytes()
    version = subprocess.check_output([str(args.lean), "--version"], text=True).strip()
    require(LEAN_COMMIT in version, "Unexpected Lean compiler commit")
    require(git(ml, "rev-parse", "HEAD") == MATHLIB_COMMIT, "Unexpected mathlib commit")
    require(manifest == subprocess.check_output(
        ["git", "-C", str(ml), "show", "HEAD:lake-manifest.json"]), "Modified mathlib manifest")
    packages = json.loads(manifest)["packages"]
    lib = Path(".lake/build/lib/lean")
    paths = [build, ml / lib] + [ml / ".lake/packages" / p["name"] / lib for p in packages]
    env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, paths)))
    extra_before = {rel: (repo / rel).read_bytes() for rel in EXTRA_INPUTS}
    receipt = {
        "scope": "Exact new finite Lean statements and listed deterministic finite controls only",
        "requested_kind": args.only,
        "repo_head_at_start": git(repo, "rev-parse", "HEAD"),
        "repo_tree_at_start": git(repo, "rev-parse", "HEAD^{tree}"),
        "working_tree_status_at_start": git(repo, "status", "--porcelain"),
        "lean_version": version,
        "mathlib_commit": MATHLIB_COMMIT,
        "mathlib_manifest_sha256": sha(manifest),
        "dependency_revisions": {p["name"]: p["rev"] for p in packages},
        "extra_input_sha256": {rel: sha(data) for rel, data in extra_before.items()},
        "lean": [], "controls": [],
    }
    if args.only in {"all", "lean"}:
        for rel, count in modules:
            source = repo / BASE / rel
            before = source.read_bytes()
            module = source.stem
            command = [str(args.lean), "-DwarningAsError=true", "-o",
                       str(build / (module + ".olean")), str(source)]
            start = time.monotonic()
            result = subprocess.run(command, cwd=repo, env=env,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            (out / (module + ".log")).write_text(result.stdout)
            declarations = {}
            for line in result.stdout.splitlines():
                match = re.fullmatch(r"'([^']+)' depends on axioms: \[([^\]]*)\]", line)
                if match:
                    declarations[match[1]] = match[2].split(", ") if match[2] else []
                match = re.fullmatch(r"'([^']+)' does not depend on any axioms", line)
                if match:
                    declarations[match[1]] = []
            row = {
                "path": (BASE / rel).as_posix(), "source_sha256": sha(before),
                "command": command, "exit_code": result.returncode,
                "elapsed_seconds": round(time.monotonic() - start, 3),
                "output_sha256": sha(result.stdout.encode()), "declarations": declarations,
            }
            receipt["lean"].append(row)
            (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
            require(result.returncode == 0, f"Lean rejected {rel}; see {module}.log")
            require(len(declarations) == count, f"Missing declaration audit in {rel}")
            require(all(set(a) <= ALLOWED_AXIOMS for a in declarations.values()),
                    f"Unexpected axiom in {rel}")
            require(source.read_bytes() == before, f"Source changed during replay: {rel}")
            print(f"LEAN PASS {rel}: {count} declarations", flush=True)

    def replay_control(pair):
        script, expected = (repo / BASE / p for p in pair[:2])
        control_args = pair[2]
        source_before, expected_before = script.read_bytes(), expected.read_bytes()
        row = {"script": script.relative_to(repo).as_posix(),
               "source_sha256": sha(source_before),
               "expected": expected.relative_to(repo).as_posix(),
               "expected_sha256": sha(expected_before), "runs": []}
        outputs = []
        for optimized in [False, True]:
            command = [sys.executable, "-X", "utf8", "-B"]
            if optimized:
                command.append("-O")
            command.extend([str(script), *control_args])
            start = time.monotonic()
            result = subprocess.run(command, cwd=repo, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            name = script.parent.name + "_" + script.stem + ("_optimized" if optimized else "")
            (out / (name + ".stdout")).write_bytes(result.stdout)
            (out / (name + ".stderr")).write_bytes(result.stderr)
            require(result.returncode == 0, f"Control failed: {name}")
            require(json.loads(result.stdout) == json.loads(expected_before),
                    f"Finite payload differs: {name}")
            row["runs"].append({"command": command, "exit_code": result.returncode,
                                "elapsed_seconds": round(time.monotonic()-start, 3),
                                "stdout_sha256": sha(result.stdout),
                                "stderr_sha256": sha(result.stderr),
                                "complete_json_matches": True})
            outputs.append(result.stdout)
        require(outputs[0] == outputs[1], f"Optimization changes output: {script}")
        require(script.read_bytes() == source_before and expected.read_bytes() == expected_before,
                f"Control inputs changed during replay: {script}")
        row["normal_optimized_bytes_equal"] = True
        return row

    if args.only in {"all", "controls"}:
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            for row in pool.map(replay_control, controls):
                receipt["controls"].append(row)
                (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
                print(f"CONTROL PASS {row['script']}: normal and optimized", flush=True)
    require(all((repo / rel).read_bytes() == data for rel, data in extra_before.items()),
            "Auxiliary control inputs changed during replay")
    receipt["all_requested_checks_passed"] = True
    receipt["working_tree_status_at_end"] = git(repo, "status", "--porcelain")
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"receipt": str(out / "receipt.json"),
                      "lean_declarations": sum(len(r["declarations"]) for r in receipt["lean"]),
                      "controls": len(receipt["controls"]), "passed": True}), flush=True)


if __name__ == "__main__":
    main()
