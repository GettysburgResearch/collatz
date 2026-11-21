"""Record actual new-packet execution in a clean, complete checkout.

The optional fast runtime is only a storage optimization: all of its files
must match the pinned original toolchain/dependency cache byte for byte.
No compiler, cache installer, or network downloader is invoked here.
"""

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("root", type=Path)
parser.add_argument("receipt", type=Path)
parser.add_argument("expected_head")
parser.add_argument("--lean-runtime", required=True, type=Path)
parser.add_argument("--mathlib", required=True, type=Path)
parser.add_argument("--fast-root", type=Path)
args = parser.parse_args()
root, receipt = args.root.resolve(), args.receipt.resolve()
runtime, mathlib = args.lean_runtime.resolve(), args.mathlib.resolve()
fast = args.fast_root.resolve() if args.fast_root else None
project = root / "research/reframe-20261121/lean"
pin = "d13f23b723b8a846827a245b89c10fc7d3f11612"
modules = ["DiscretePump", "MarkedDyadicTransport", "MergerPopulationPacking"]
selected_runtime = fast or runtime
env = dict(os.environ, PATH=str(selected_runtime / "bin") + os.pathsep + os.environ["PATH"],
           MATHLIB_DIR=str(mathlib))
if fast:
    env["REFRAME_IMPORT_OVERLAY"] = str(fast / "deps")
else:
    env.pop("REFRAME_IMPORT_OVERLAY", None)


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def git(*values, cwd=root):
    return subprocess.check_output(["git", *values], cwd=cwd, text=True).strip()


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def state():
    tracked = git("ls-files").splitlines()
    if tracked != git("ls-tree", "-r", "--name-only", "HEAD").splitlines():
        raise RuntimeError("Index is not the complete HEAD tree")
    if not all((root / name).is_file() for name in tracked):
        raise RuntimeError("A tracked file is absent")
    tree = git("rev-parse", "HEAD^{tree}")
    if git("write-tree") != tree:
        raise RuntimeError("Index differs from HEAD")
    return {"head": git("rev-parse", "HEAD"), "tree": tree,
            "tracked_files": len(tracked),
            "status": git("status", "--porcelain", "--untracked-files=all")}


def source_hashes():
    paths = git("ls-files", "research/reframe-20261121",
                "reports/2026-11-21-reframe").splitlines()
    paths += ["research/band-return-20261121/lean/vendor/" + name + ".lean"
              for name in ["ShellCover", "ForwardSection"]]
    return {name: digest(root / name) for name in sorted(paths)}


def mathlib_state():
    head = git("rev-parse", "HEAD", cwd=mathlib)
    clean = subprocess.run(["git", "diff", "--quiet", "HEAD", "--"],
                           cwd=mathlib).returncode == 0
    if head != pin or not clean:
        raise RuntimeError("Mathlib is not at the clean pinned revision")
    return {"head": head, "tracked_changes": False}


def verify_fast_copy():
    if not fast:
        return None
    origins = sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
    origins += [mathlib / ".lake/build/lib/lean", runtime / "lib/lean"]
    total = count = 0
    combined = hashlib.sha256()
    started = time.monotonic()
    for path in sorted(p for p in fast.rglob("*") if p.is_file()):
        rel = path.relative_to(fast)
        if rel.parts[0] == "deps":
            tail = Path(*rel.parts[1:])
            origin = next((base / tail for base in origins if (base / tail).is_file()), None)
        else:
            origin = runtime / rel
        if origin is None or not origin.is_file():
            raise RuntimeError("Fast copy has no pinned original: " + str(rel))
        if path.stat().st_size != origin.stat().st_size:
            raise RuntimeError("Fast copy size mismatch: " + str(rel))
        checksum = digest(path)
        if checksum != digest(origin):
            raise RuntimeError("Fast copy byte mismatch: " + str(rel))
        combined.update((str(rel) + "\0" + checksum + "\n").encode())
        count += 1
        total += path.stat().st_size
    result = {"root": str(fast), "runtime_origin": str(runtime), "files": count,
              "bytes": total, "aggregate_sha256": combined.hexdigest()}
    print(json.dumps({"verified_fast_copy": result,
                      "seconds": round(time.monotonic() - started, 3)}), flush=True)
    return result


record = {"started_utc": stamp(), "success": False, "commands": [],
          "scope": "New reframe Lean packet, all-public-theorem axiom audit, and exact Green arithmetic replay; full Collatz remains open.",
          "validator_sha256": digest(Path(__file__)),
          "runtime_origin": str(runtime), "selected_runtime": str(selected_runtime)}
try:
    record["before"] = state()
    if record["before"]["head"] != args.expected_head or record["before"]["status"]:
        raise RuntimeError("Wrong head or dirty checkout")
    if (project / ".build").exists():
        raise RuntimeError("A fresh packet output directory is required")
    record["mathlib_before"] = mathlib_state()
    record["source_sha256"] = source_hashes()
    record["fast_copy_before"] = verify_fast_copy()
    public = []
    for module in modules:
        contents = (project / (module + ".lean")).read_text()
        namespaces = re.findall(r"^namespace\s+(\S+)\s*$", contents, re.M)
        if len(namespaces) != 1:
            raise RuntimeError("Unexpected namespace layout: " + module)
        names = re.findall(r"^(?:theorem|lemma)\s+(\w+)", contents, re.M)
        public.extend(namespaces[0] + "." + name for name in names)
    audited = re.findall(r"^#print axioms (\S+)",
                         (project / "ReframeAudit.lean").read_text(), re.M)
    if not public or len(public) != len(audited) or set(public) != set(audited):
        raise RuntimeError("Public theorem audit coverage differs from source declarations")
    record["public_theorems"] = sorted(public)

    commands = [[str(selected_runtime / "bin/lean"), "--version"],
                ["bash", "research/reframe-20261121/lean/build.sh"],
                ["python", "-X", "utf8", "-B",
                 "research/reframe-20261121/global_mass_green_certificate.py"]]
    for command in commands:
        print(json.dumps({"running": command}), flush=True)
        started = time.monotonic()
        result = subprocess.run(command, cwd=root, env=env, capture_output=True, text=True)
        record["commands"].append({"argv": command, "cwd": str(root),
                                   "exit_code": result.returncode,
                                   "stdout": result.stdout, "stderr": result.stderr,
                                   "seconds": round(time.monotonic() - started, 3)})
        if result.returncode:
            raise RuntimeError("Command failed: " + str(command))

    marker = "Checking new ReframeAudit\n"
    output = record["commands"][1]["stdout"]
    if output.count(marker) != 1:
        raise RuntimeError("Cannot locate the dedicated complete axiom audit")
    entries = re.findall(r"'([^']+)'\s+(?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)",
                         output.split(marker, 1)[1], re.S)
    dependencies = {}
    for name, body in entries:
        axioms = [item.strip() for item in body.split(",") if item.strip()]
        if set(axioms) - {"propext", "Classical.choice", "Quot.sound"}:
            raise RuntimeError("Unexpected axioms: " + name + " " + str(axioms))
        if name in dependencies:
            raise RuntimeError("Duplicate axiom output: " + name)
        dependencies[name] = axioms
    if set(dependencies) != set(audited):
        raise RuntimeError("Missing or unexpected theorem output")
    record["axiom_dependencies"] = dependencies
    record["public_theorem_count"] = len(dependencies)
    record["after"] = state()
    record["mathlib_after"] = mathlib_state()
    record["fast_copy_after"] = verify_fast_copy()
    if record["after"] != record["before"] or source_hashes() != record["source_sha256"]:
        raise RuntimeError("Checkout or proof inputs changed during execution")
    if record["mathlib_after"] != record["mathlib_before"]:
        raise RuntimeError("Mathlib source changed during execution")
    if record["fast_copy_after"] != record["fast_copy_before"]:
        raise RuntimeError("Fast runtime/cache copy changed during execution")
    record["success"] = True
except Exception as error:
    record["error"] = str(error)
record["finished_utc"] = stamp()
receipt.parent.mkdir(parents=True, exist_ok=True)
receipt.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
print(json.dumps({"success": record["success"], "head": record.get("before", {}).get("head"),
                  "commands": len(record["commands"]),
                  "public_theorems": record.get("public_theorem_count"),
                  "receipt": str(receipt), "error": record.get("error")}), flush=True)
if not record["success"]:
    raise SystemExit(1)
