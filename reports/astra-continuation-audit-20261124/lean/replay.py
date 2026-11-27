"""Replay PR201's import-only candidates and their standalone finite audit copies."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

from cover_source import generate


PR_HEAD = "73a145ca99448a78219bd149e273f33b6e3fda4b"
MATHLIB_HEAD = "d13f23b723b8a846827a245b89c10fc7d3f11612"
LEAN_HEAD = "5045d0056413266e57c625dcd7c365b10e377c52"
BASE = Path("research/killed-green-head-closure-20261124")
ORIGINALS = {
    "KilledMoment": BASE / "KilledMoment.lean",
    "OctavePhase": BASE / "continuation/OctavePhase.lean",
    "PrefixDensity": BASE / "prefix-density/PrefixDensity.lean",
    "TwoEndBridge": BASE / "two-end-bridge/TwoEndBridge.lean",
}
THEOREM_COUNTS = {"KilledMoment": 4, "OctavePhase": 7, "PrefixDensity": 7,
                  "TwoEndBridge": 4, "OrdinaryGapWord": 11, "ExactClockRouter": 5,
                  "TriplingCover": 4, "Residue1": 2, "Residue5": 2}
EXTRA_AUDITS = {
    "ExactClockRouter": ["Collatz.OrdinaryGapWord.Word.beta", "Collatz.OrdinaryGapWord.twoGapWord"],
    "TriplingCover": ["Collatz.TriplingCover." + name for name in
                      ["Op", "Rule", "rule", "Row", "evaluate", "advance", "run", "triple",
                       "Tree", "child", "check", "Rules", "Covers"]],
    "OctavePhase": ["Collatz.OctavePhase.variation"],
    "PrefixDensity": ["Collatz.PrefixDensity.run"],
    "OrdinaryGapWord": ["Collatz.OrdinaryGapWord." + name for name in
                        ["Word", "Word.depth", "Word.clock", "Word.carry",
                         "PositiveOdd", "Path", "shortcut"]],
}
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}


def git(directory, *args):
    return subprocess.check_output(["git", "-C", directory, *args])


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check(condition, error):
    if not condition:
        raise ValueError(error)


def audit(lean, env, name, source, extra, build):
    """Check the actual source, with read-only axiom queries appended."""
    commands = "".join(f"#print axioms {n}\n" for n in extra).encode()
    with tempfile.TemporaryDirectory() as directory:
        file_name = f"{name}.lean"
        (Path(directory) / file_name).write_bytes(source + commands)
        command = ["lean", "-j1", file_name]
        args = [lean, *command[1:]]
        if name in {"OrdinaryGapWord", "TriplingCover"}:
            args.extend(["-o", build / f"{name}.olean"])
            command.extend(["-o", f"<build>/{name}.olean"])
        process = subprocess.run(args, cwd=directory, env=env,
                                 capture_output=True, text=True, check=False)
    output = process.stdout + process.stderr
    check(process.returncode == 0, f"Lean rejected {name}:\n{output}")
    axioms = {}
    for line in output.splitlines():
        match = re.fullmatch(r"'([^']+)' depends on axioms: \[([^\]]*)\]", line)
        if match:
            axioms[match[1]] = match[2].split(", ") if match[2] else []
        else:
            match = re.fullmatch(r"'([^']+)' does not depend on any axioms", line)
            if match:
                axioms[match[1]] = []
    check(len(axioms) == THEOREM_COUNTS[name] + len(extra), f"Missing axiom audit: {output}")
    for theorem, used in axioms.items():
        check(set(used) <= ALLOWED_AXIOMS, f"Unexpected axiom in {theorem}: {used}")
    diagnostics = "\n".join(line for line in output.splitlines() if not
                            re.match(r"^'.+' (?:depends on|does not depend on)", line)).strip()
    return {"command": command, "exit_code": process.returncode,
            "source_sha256_before_axiom_queries": digest(source),
            "compiler_input_sha256": digest(source + commands),
            "diagnostics": diagnostics, "axioms": axioms}


def main(build):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", required=True, type=Path, help="built pinned mathlib checkout")
    parser.add_argument("--lean", type=Path, required=True, help="pinned Lean executable")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    mathlib = args.mathlib.resolve()
    lean_exe = args.lean.resolve()
    repo = args.repo.resolve()
    lean_version = subprocess.check_output([lean_exe, "--version"], text=True).strip()
    check(LEAN_HEAD in lean_version, "Lean commit mismatch")
    check(git(mathlib, "rev-parse", "HEAD").decode().strip() == MATHLIB_HEAD,
          "mathlib commit mismatch")
    manifest = (mathlib / "lake-manifest.json").read_bytes()
    check(manifest == git(mathlib, "show", "HEAD:lake-manifest.json"), "manifest mismatch")
    packages = json.loads(manifest)["packages"]
    lib = Path(".lake/build/lib/lean")
    paths = [build, *(mathlib / ".lake/packages" / item["name"] / lib for item in packages)]
    paths.append(mathlib / lib)
    env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, paths)))
    result = {"source_pr": 201, "source_commit": PR_HEAD, "mathlib_commit": MATHLIB_HEAD,
              "mathlib_manifest_sha256": digest(manifest), "lean_version": lean_version,
              "import_only": {}, "verified": {}, "certificates": {}}
    for name in THEOREM_COUNTS:
        if name in {"Residue1", "Residue5"}:
            residue = int(name[-1])
            table = BASE / "global-bridge" / f"cover{residue}.txt"
            generated = generate(repo / table, residue)
            result["certificates"][name] = {
                "table": table.as_posix(), "table_sha256": digest((repo / table).read_bytes()),
                **audit(lean_exe, env, name, generated, [], build),
            }
            continue
        path = BASE / "verified" / f"{name}.lean"
        updated = (repo / path).read_bytes()
        if name in ORIGINALS:
            original_path = ORIGINALS[name]
            spec = f"{PR_HEAD}:{original_path}"
            old = git(repo, "cat-file", "blob", spec)
            imports = b"\n".join(line for line in updated.splitlines() if line.startswith(b"import "))
            check(old.startswith(b"import Mathlib\n"), "Unexpected original imports")
            import_only = imports + b"\n" + old.removeprefix(b"import Mathlib\n")
            result["import_only"][name] = {
                "original_path": original_path.as_posix(), "original_sha256": digest(old),
                "original_git_blob": git(repo, "rev-parse", spec).decode().strip(),
                "replacement_imports": imports.decode().splitlines(),
                **audit(lean_exe, env, name, import_only, [], build),
            }
        result["verified"][name] = {"path": path.as_posix(),
                                     **audit(lean_exe, env, name, updated,
                                             EXTRA_AUDITS.get(name, []), build)}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as build_dir:
        main(Path(build_dir))
