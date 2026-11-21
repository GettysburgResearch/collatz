#!/usr/bin/env python3
"""Freshly replay the exact dependencies and three new Lean modules.

The analytic rate optimization, infinite measures, and energy synthesis are
outside this formal replay. No dependency is downloaded by this script.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time


STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
NEW_MODULES = ["ReturnSynthesis", "WitnessSynthesis", "RepeatedTail", "WideAudit"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parent
    root = packet.parent.parent
    manifest = json.loads((packet / "DEPENDENCIES.json").read_text())
    modules = list(manifest["files"])
    for item in modules:
        actual = hashlib.sha256((root / item["path"]).read_bytes()).hexdigest()
        if actual != item["sha256"]:
            raise SystemExit(f"Pinned source mismatch: {item['path']}")
    modules += [{"module": name, "kind": "new" if name != "WideAudit" else "audit",
                 "path": str((packet / "lean" / f"{name}.lean").relative_to(root))}
                for name in NEW_MODULES]
    lean = args.lean.resolve()
    mathlib = args.mathlib.resolve()
    report_dir = args.report_dir.resolve()
    report_dir.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env["PATH"] = str(lean.parent) + os.pathsep + env.get("PATH", "")
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    if (f"version {manifest['lean_version']}," not in version
            or manifest["lean_commit"] not in version):
        raise SystemExit(f"Lean version mismatch: {version}")
    pin = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mathlib,
                                  text=True).strip()
    if pin != manifest["mathlib_commit"]:
        raise SystemExit(f"Mathlib pin mismatch: {pin}")
    inherited = subprocess.check_output(
        [str(lean.with_name("lake")), "env", "printenv", "LEAN_PATH"],
        cwd=mathlib, env=env, text=True,
    ).strip()
    report = {
        "status": "running", "lean_version": version, "mathlib_commit": pin,
        "warnings_as_errors": True, "fresh_local_module_output": True,
        "module_count": len(modules), "new_public_theorem_count": 22,
        "modules": [],
        "scope": "Pinned local dependencies and all 22 public theorems in the three new modules.",
        "not_formalized": [
            "The optimized O(N/log N) asymptotic and its explicit numerical specialization",
            "The infinite source measures, discounted resolvent, and full fourth-log-moment sum",
            "The canonical stationary-density and finite-cylinder operator arguments",
            "A total erasure dispatcher or the required aggregate return-transport estimate",
            "Universal Collatz convergence",
        ],
    }
    logs = []

    def save() -> None:
        (report_dir / "lean-check.json").write_text(json.dumps(report, indent=2) + "\n")
        (report_dir / "lean-build.log").write_text("\n".join(logs).rstrip() + "\n")

    save()
    try:
        with tempfile.TemporaryDirectory(prefix="collatz-wide-build-") as tmp:
            env["LEAN_PATH"] = tmp + os.pathsep + inherited
            for item in modules:
                path = root / item["path"]
                start = time.monotonic()
                result = subprocess.run(
                    [str(lean), "-j1", "-DwarningAsError=true", "-o",
                     str(Path(tmp) / f"{item['module']}.olean"), str(path)],
                    cwd=path.parent, env=env, text=True, stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT, timeout=180,
                )
                seconds = round(time.monotonic() - start, 3)
                groups = re.findall(r"depends on axioms:\s*\[([^]]*)\]",
                                    result.stdout, re.S)
                axioms = sorted({a.strip() for group in groups
                                 for a in group.split(",") if a.strip()})
                record = dict(item, sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                              exit_code=result.returncode, seconds=seconds,
                              printed_axioms=axioms, printed_audit_count=len(groups))
                report["modules"].append(record)
                logs.append(f"MODULE {item['module']}\n{result.stdout}\n")
                save()
                print(f"{item['module']}: exit={result.returncode}, {seconds}s", flush=True)
                if result.returncode or not set(axioms) <= STANDARD_AXIOMS:
                    print(result.stdout, flush=True)
                    raise RuntimeError(f"Replay failed for {item['module']}")
                if item["module"] == "WideAudit" and len(groups) != 22:
                    raise RuntimeError("The combined audit did not print all 22 theorem dependencies")
        report["status"] = "passed"
        save()
        print("Fresh replay passed; all 22 new public theorem audits are standard only.")
    except BaseException as error:
        report["status"] = "failed"
        report["error"] = str(error)
        save()
        raise


if __name__ == "__main__":
    main()
