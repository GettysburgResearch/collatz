"""Replay the finite Lean kernels and frozen PR202/203 proof bodies.

Uses a prebuilt Lean 4.34.1/mathlib checkout; does not build dependencies.
Prints a JSON execution receipt. No output files are written into the checkout.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}
BASE = Path("research/astra-joint-closure-20261124")
REPORT = Path("reports/astra-joint-closure-20261124")
IMPORTS = "\n".join([
    "import Mathlib.Tactic.LinearCombination",
    "import Mathlib.Tactic.Linarith",
    "import Mathlib.Tactic.NormNum",
    "import Mathlib.Tactic.Ring", "",
])
SOURCES = [
    ("ordinary/InternalMerge.lean", "InternalMerge"),
    ("arithmetic/FiniteCycleTests.lean", "FiniteCycleTests"),
    ("upstream/ClockTransport.lean", "SynchronizedBasinBlocks"),
    ("upstream/MixedTransport.lean", "MixedTransport"),
]
ORIGINALS = [
    (202, "ClockTransport", "SynchronizedBasinBlocks",
     "3b10b24d12d4b349cb20f4cbc83086c8a09f807e",
     "research/synchronized-long-basin-blocks-20261124/ClockTransport.lean",
     "b0081dbb22740f89e7d369c9933d704d3074a539"),
    (203, "MixedTransport", "MixedTransport",
     "3f2c89f12b057b8bb8655bd6fc794c772aa8b65d",
     "research/mixed-adic-basin-density-20261124/MixedTransport.lean",
     "9375fd1abd56f63a92ee4de9cad7630d1a179199"),
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def blob_id(data):
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def compile_source(lean, env, source, namespace, name, strict):
    text = source.decode()
    require(not re.search(r"\b(?:sorry|admit|native_decide)\b|^\s*axiom\s",
                          text, re.M), "Unchecked proof construct")
    names = [namespace + "." + name for name in
             re.findall(r"^theorem\s+(\w+)", text, re.M)]
    require(bool(names), "No theorem declarations found")
    queries = "\n" + "".join(f"#print axioms {n}\n" for n in names)
    actual = source + queries.encode()
    with tempfile.TemporaryDirectory(prefix="collatz-joint-lean-") as temp:
        file = Path(temp) / f"{name}.lean"
        file.write_bytes(actual)
        command = [str(lean), "-j1"]
        if strict:
            command.append("-DwarningAsError=true")
        command.append(file.name)
        process = subprocess.run(command, cwd=temp, env=env,
                                 capture_output=True, text=True)
    output = process.stdout + process.stderr
    require(process.returncode == 0, name + " rejected:\n" + output)
    axioms = {}
    diagnostics = []
    for line in output.splitlines():
        match = re.fullmatch(r"'([^']+)' depends on axioms: \[([^\]]*)\]", line)
        empty = re.fullmatch(r"'([^']+)' does not depend on any axioms", line)
        if match:
            axioms[match[1]] = match[2].split(", ") if match[2] else []
        elif empty:
            axioms[empty[1]] = []
        else:
            diagnostics.append(line)
    require(set(axioms) == set(names), "Incomplete theorem audit: " + output)
    for theorem, used in axioms.items():
        require(set(used) <= ALLOWED_AXIOMS,
                "Unexpected axiom for " + theorem + ": " + str(used))
    return {
        "command": ["lean", *command[1:]], "exit_code": process.returncode,
        "source_sha256": sha(source), "compiler_input_sha256": sha(actual),
        "theorem_count": len(names), "axioms": axioms,
        "diagnostics": "\n".join(diagnostics).strip(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--repo", type=Path,
                        default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    lean, mathlib, repo = args.lean.resolve(), args.mathlib.resolve(), args.repo.resolve()
    version = subprocess.check_output([lean, "--version"], text=True).strip()
    require(LEAN_COMMIT in version, "Unexpected Lean version")
    revision = subprocess.check_output(
        ["git", "-C", mathlib, "rev-parse", "HEAD"], text=True).strip()
    require(revision == MATHLIB_COMMIT, "Unexpected mathlib revision")
    manifest = (mathlib / "lake-manifest.json").read_bytes()
    paths = [mathlib / ".lake/build/lib/lean",
             *sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))]
    env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, paths)))
    result = {"lean_version": version, "mathlib_commit": revision,
              "mathlib_manifest_sha256": sha(manifest),
              "dependency_scope": "Reused prebuilt supporting dependencies; no fresh mathlib build.",
              "frozen_import_only": [], "working_sources": []}
    for pr, name, namespace, commit, path, blob in ORIGINALS:
        original = (repo / REPORT / "upstream-originals" / (name + ".lean")).read_bytes()
        require(blob_id(original) == blob, "Original source blob mismatch")
        require(original.startswith(b"import Mathlib\n"), "Unexpected original imports")
        transformed = IMPORTS.encode() + original.removeprefix(b"import Mathlib\n")
        result["frozen_import_only"].append({
            "pr": pr, "commit": commit, "path": path, "git_blob": blob,
            "original_sha256": sha(original),
            "transformation": "Replace only import Mathlib by the four listed narrow imports.",
            "imports": IMPORTS.splitlines(),
            **compile_source(lean, env, transformed, namespace, name, False),
        })
    for relative, namespace in SOURCES:
        path = BASE / relative
        result["working_sources"].append({
            "path": path.as_posix(),
            **compile_source(lean, env, (repo / path).read_bytes(), namespace,
                             Path(relative).stem, True),
        })
    result["distinct_theorems"] = sum(x["theorem_count"] for x in result["working_sources"])
    result["successful_compiler_executions"] = len(ORIGINALS) + len(SOURCES)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
