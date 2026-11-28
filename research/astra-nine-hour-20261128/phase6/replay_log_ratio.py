#!/usr/bin/env python3
"""Rebuild the public rational logarithm-ratio endpoint from its source closure.

Input is the unchanged anc/lean directory from arXiv:2610.28079's source
distribution. This driver neither downloads nor patches the imported research.
It uses the same pinned Lean and already compiled Mathlib as this packet.
The endpoint types and their recursive axiom reports are retained in the receipt.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
MATHLIB_COMMIT = "d13f23b723b8a846827a245b89c10fc7d3f11612"
TARGETS = ["QuadraticPi.RationalLogRatioTheorem", "QuadraticPi.RationalTwoLogLinearForm"]
ENDPOINTS = [
    "QuadraticPi.rationalLogRatio_irrationalityExponent_bounds",
    "QuadraticPi.log_two_div_log_three_irrationalityExponent_bounds",
    "QuadraticPi.rationalTwoLog_linearForm_lowerBound",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(ok: bool, why: str) -> None:
    if not ok:
        raise RuntimeError(why)


def git(path: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(path), *args], text=True).strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ["source", "lean", "mathlib", "receipt", "build_parent", "lock"]:
        ap.add_argument("--" + name.replace("_", "-"), type=Path, required=True)
    ap.add_argument("--timeout", type=int, default=300)
    args = ap.parse_args()
    root = args.source.resolve()
    receipt = {
        "schema": "collatz-external-log-ratio-replay/v1", "passed": False,
        "source": "https://arxiv.org/abs/2610.28079",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Fresh unchanged local import closure and endpoint axiom audit; cached pinned Mathlib; no claim that all manuscript results were replayed.",
        "targets": TARGETS, "modules": [],
    }
    try:
        version = subprocess.check_output([str(args.lean), "--version"], text=True).strip()
        check("4.34.1" in version and LEAN_COMMIT[:12] in version, "Wrong Lean compiler")
        receipt["lean"] = {"version": version, "sha256": sha(args.lean)}
        check(git(args.mathlib, "rev-parse", "HEAD") == MATHLIB_COMMIT, "Wrong Mathlib pin")
        check(not git(args.mathlib, "status", "--porcelain", "--untracked-files=no"), "Dirty Mathlib")
        manifest = json.loads((args.mathlib / "lake-manifest.json").read_text())
        packages = args.mathlib / manifest["packagesDir"]
        deps = []
        for p in manifest["packages"]:
            directory = packages / p["name"]
            check(git(directory, "rev-parse", "HEAD") == p["rev"], "Wrong dependency " + p["name"])
            check(not git(directory, "status", "--porcelain", "--untracked-files=no"), "Dirty dependency " + p["name"])
            deps.append({"name": p["name"], "sha": p["rev"]})
        receipt["mathlib"] = MATHLIB_COMMIT
        receipt["dependencies"] = deps
        paths = {".".join(p.relative_to(root).with_suffix("").parts): p for p in root.rglob("*.lean")}
        seen, active, external, order = set(), set(), set(), []

        def visit(name: str) -> None:
            if name in seen:
                return
            check(name not in active, "Cyclic import " + name)
            if name not in paths:
                check(name.startswith(("Mathlib.", "Lean.", "Init.", "Std.")) or name in {"Mathlib", "Lean", "Init", "Std"}, "Missing source " + name)
                external.add(name)
                seen.add(name)
                return
            active.add(name)
            for line in paths[name].read_text().splitlines():
                match = re.match(r"\s*(?:public\s+)?import\s+(?:all\s+)?(.+)", line)
                if match:
                    for dep in match[1].split("--")[0].split():
                        visit(dep)
            active.remove(name)
            seen.add(name)
            order.append(name)

        for target in TARGETS:
            visit(target)
        receipt["external_imports"] = sorted(external)
        source_hashes = {name: sha(paths[name]) for name in order}
        build = Path(tempfile.mkdtemp(prefix="log-ratio-clean-", dir=args.build_parent))
        receipt["build_directory"] = str(build)
        search = [build, args.mathlib / ".lake/build/lib/lean"]
        search.extend(packages / p["name"] / ".lake/build/lib/lean" for p in manifest["packages"])
        env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, search)))
        flags = ["-j1", "-DElab.async=false", "-DwarningAsError=true", "-DautoImplicit=false", "-DmaxHeartbeats=4000000"]
        receipt["flags"] = flags

        def compile_one(source: Path, module: str, package_root: Path) -> dict:
            output = build / Path(*module.split(".")).with_suffix(".olean")
            output.parent.mkdir(parents=True, exist_ok=True)
            cmd = [str(args.lean), *flags, "-R", str(package_root), "-o", str(output), str(source)]
            started = time.monotonic()
            with args.lock.open("a") as lock:
                fcntl.flock(lock, fcntl.LOCK_EX)
                result = subprocess.run(cmd, cwd=package_root, env=env, capture_output=True, text=True, timeout=args.timeout)
            return {"module": module, "sha256": sha(source), "exit_code": result.returncode,
                    "seconds": round(time.monotonic() - started, 4), "stdout": result.stdout, "stderr": result.stderr}

        for i, name in enumerate(order, 1):
            print(f"[{i}/{len(order)}] {name}", flush=True)
            row = compile_one(paths[name], name, root)
            receipt["modules"].append(row)
            check(row["exit_code"] == 0, f"Compilation failed: {name}\n{row['stdout']}\n{row['stderr']}")
            args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")

        audit = build / "RationalRatioEndpointAudit.lean"
        text = "\n".join("import " + target for target in TARGETS)
        text += "\nimport Lean.Util.CollectAxioms\nimport Lean.Elab.Command\n"
        text += "\n".join("#print " + name + "\n#print axioms " + name for name in ENDPOINTS)
        text += "\nopen Lean Elab Command in\nrun_cmd do\n  let allowed : Array Name := #[`propext, `Classical.choice, `Quot.sound]\n"
        text += "  for name in #[" + ", ".join("`" + name for name in ENDPOINTS) + "] do\n"
        text += '    let axioms ← collectAxioms name\n    let unexpected := axioms.filter (fun a => !allowed.contains a)\n    unless unexpected.isEmpty do\n      throwError "Unexpected axioms for {name}: {unexpected}"\n'
        audit.write_text(text)
        row = compile_one(audit, "RationalRatioEndpointAudit", build)
        receipt["endpoint_audit"] = row
        check(row["exit_code"] == 0, "Endpoint audit failed\n" + row["stdout"] + row["stderr"])
        check(source_hashes == {name: sha(paths[name]) for name in order}, "Source changed during replay")
        receipt["passed"] = True
        print("PASS: unchanged closure and three endpoint audits", flush=True)
    except Exception as exc:
        receipt["error"] = str(exc)
        print("FAIL: " + str(exc), flush=True)
    receipt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
