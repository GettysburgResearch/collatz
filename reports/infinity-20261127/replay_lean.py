"""Rebuild an explicit ordered list of Lean modules and audit printed axioms.

The manifest is a JSON list of repository-relative source paths. Outputs must
be outside the checkout. This checks only the actual declarations compiled;
written arguments and external mathematical inputs have separate status.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time

LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
ALLOWED = {"propext", "Quot.sound", "Classical.choice"}


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    repo, ml, out = args.repo.resolve(), args.mathlib.resolve(), args.out.resolve()
    require(not out.is_relative_to(repo), "Output must be outside repository")
    out.mkdir(parents=True, exist_ok=False)
    build = out / "build"
    build.mkdir()
    modules_bytes = args.manifest.read_bytes()
    modules = json.loads(modules_bytes)
    require(isinstance(modules, list) and modules, "Expected nonempty source list")
    require(len(modules) == len(set(modules)), "Repeated source")
    require(len(modules) == len({Path(p).stem for p in modules}), "Module-name collision")
    for rel in modules:
        source = (repo / rel).resolve()
        require(source.is_relative_to(repo) and source.suffix == ".lean", "Invalid source path")
    before = {rel: (repo / rel).read_bytes() for rel in modules}
    version = subprocess.check_output([str(args.lean), "--version"], text=True).strip()
    require(LEAN_COMMIT in version, "Unexpected Lean version")
    require(git(ml, "rev-parse", "HEAD") == MATHLIB_COMMIT, "Unexpected mathlib commit")
    ml_manifest = (ml / "lake-manifest.json").read_bytes()
    require(ml_manifest == subprocess.check_output(["git", "-C", str(ml), "show", "HEAD:lake-manifest.json"]), "Changed mathlib manifest")
    packages = json.loads(ml_manifest)["packages"]
    lib = Path(".lake/build/lib/lean")
    paths = [build, ml / lib] + [ml / ".lake/packages" / p["name"] / lib for p in packages]
    env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, paths)))
    receipt = {
        "scope": "Fresh Lean source compilation, annotated declaration axiom audits only",
        "driver_sha256": digest(Path(__file__).read_bytes()),
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "repo_head": git(repo, "rev-parse", "HEAD"),
        "repo_tree": git(repo, "rev-parse", "HEAD^{tree}"),
        "working_status": git(repo, "status", "--porcelain"),
        "lean_version": version,
        "mathlib_commit": MATHLIB_COMMIT,
        "mathlib_manifest_sha256": digest(ml_manifest),
        "manifest_sha256": digest(modules_bytes),
        "dependency_revisions": {p["name"]: p["rev"] for p in packages},
        "modules": [],
    }
    for rel in modules:
        source = repo / rel
        name = source.stem
        expected = len(re.findall(rb"^#print axioms ", before[rel], re.M))
        require(expected > 0, f"No explicit declaration audit: {rel}")
        command = [str(args.lean), "-j1", "-DElab.async=false", "-DwarningAsError=true",
                   "-o", str(build / (name + ".olean")), str(source)]
        started = time.monotonic()
        result = subprocess.run(command, cwd=repo, env=env, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True)
        (out / (name + ".log")).write_text(result.stdout)
        declarations = {}
        # Lean may wrap a long declaration's axiom list over several lines.
        for match in re.finditer(r"^'([^']+)' depends on axioms: \[([^\]]*)\]", result.stdout, re.M):
            declarations[match[1]] = [a.strip() for a in match[2].split(",") if a.strip()]
        for match in re.finditer(r"^'([^']+)' does not depend on any axioms", result.stdout, re.M):
            declarations[match[1]] = []
        row = {
            "path": rel, "source_sha256": digest(before[rel]), "command": command,
            "exit_code": result.returncode, "elapsed_seconds": round(time.monotonic()-started, 3),
            "output_sha256": digest(result.stdout.encode()), "declarations": declarations,
        }
        receipt["modules"].append(row)
        (out / "receipt.json").write_text(json.dumps(receipt, indent=2)+"\n")
        require(result.returncode == 0, f"Compilation failed: {rel}; inspect {name}.log")
        require(len(declarations) == expected, f"Missing or duplicated declaration audit: {rel}")
        require(all(set(a) <= ALLOWED for a in declarations.values()), f"Unexpected axiom: {rel}")
        require(source.read_bytes() == before[rel], f"Source changed during replay: {rel}")
        row["object_sha256"] = digest((build / (name + ".olean")).read_bytes())
        print(f"PASS {rel}: {expected} audited declarations", flush=True)
    require(all((repo / p).read_bytes() == b for p, b in before.items()), "Source changed during replay")
    require(args.manifest.read_bytes() == modules_bytes, "Manifest changed during replay")
    receipt["finished_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    receipt["complete"] = True
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2)+"\n")


if __name__ == "__main__":
    main()
