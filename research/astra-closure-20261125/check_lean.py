#!/usr/bin/env python3
"""Rebuild this packet in a fresh project cache; reuse a pinned Mathlib cache."""
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

ROOT = Path(__file__).resolve().parents[2]
PACKET = Path("research/astra-closure-20261125")
MATHLIB = "d13f23b723b8a846827a245b89c10fc7d3f11612"
MODULES = [
    ("EscapeCore", Path("research/astra-universal-descent-20261124/EscapeCore.lean"), False),
    ("UniversalProposal", Path("research/astra-universal-proof-20261124/UniversalProposal.lean"), False),
    ("TowerDeadline", PACKET / "descent/TowerDeadline.lean", True),
    ("MaximalWords", PACKET / "descent/MaximalWords.lean", True),
    ("PowerRealization", PACKET / "descent/PowerRealization.lean", True),
    ("PrimeSwitch", PACKET / "cycles/PrimeSwitch.lean", True),
    ("NineteenMerger", PACKET / "cycles/NineteenMerger.lean", True),
    ("GateVisits", PACKET / "escape/GateVisits.lean", True),
    ("PeriodicColor", PACKET / "global/PeriodicColor.lean", True),
    ("FinalProposal", PACKET / "FinalProposal.lean", True),
]


def run(argv: list[str], *, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(argv, cwd=ROOT, env=env, text=True, capture_output=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    args = parser.parse_args()
    receipt_path = args.receipt.resolve()
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    logs = receipt_path.parent / "lean"
    logs.mkdir(exist_ok=True)
    lean = str(args.lean.resolve())
    mathlib = args.mathlib.resolve()
    version = run([lean, "--version"])
    if version.returncode or "4.34.1" not in version.stdout:
        raise RuntimeError("This receipt requires Lean 4.34.1")
    pin = run(["git", "-C", str(mathlib), "rev-parse", "HEAD"])
    if pin.returncode or pin.stdout.strip() != MATHLIB:
        raise RuntimeError("Mathlib source checkout does not have the pinned identity")
    cache = mathlib / ".lake/build/lib/lean"
    package_caches = sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
    if not cache.is_dir():
        raise RuntimeError("Mathlib object cache is absent")
    result: dict[str, object] = {
        "schema": "collatz-astra-closure-lean/v1",
        "compiler": version.stdout.strip(),
        "mathlib": MATHLIB,
        "dependency_manifest_sha256": hashlib.sha256((mathlib / "lake-manifest.json").read_bytes()).hexdigest(),
        "scope": "All eight new modules and two resident imports, fresh project objects; cached pinned Mathlib dependencies. Written analytic and rational-cycle theorems are not formalized in full.",
        "modules": [],
        "success": False,
    }
    started = time.monotonic()
    public: list[str] = []
    imported_public: list[str] = []
    with tempfile.TemporaryDirectory(prefix="collatz-nov25-lean-") as temporary:
        obj = Path(temporary)
        env = os.environ.copy()
        env["LEAN_PATH"] = os.pathsep.join(map(str, [obj, cache, *package_caches]))
        for name, path, new in MODULES:
            source = ROOT / path
            declarations = re.findall(r"^theorem\s+([A-Za-z_][A-Za-z0-9_']*)", source.read_text(), re.MULTILINE)
            qualified = [name + "." + declaration for declaration in declarations]
            (public if new else imported_public).extend(qualified)
            before = time.monotonic()
            compiled = run([lean, "-DautoImplicit=false", "-DwarningAsError=true", "-o", str(obj / (name + ".olean")), str(path)], env=env)
            (logs / (name + ".stdout.log")).write_text(compiled.stdout)
            (logs / (name + ".stderr.log")).write_text(compiled.stderr)
            result["modules"].append({
                "module": name, "source": path.as_posix(), "new": new,
                "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "exit_code": compiled.returncode,
                "seconds": round(time.monotonic() - before, 3),
                "public_theorems": qualified,
            })
            receipt_path.write_text(json.dumps(result, indent=2) + "\n")
            print(f"{name}: exit {compiled.returncode}; {len(qualified)} public theorem declarations", flush=True)
            if compiled.returncode:
                print(compiled.stdout + compiled.stderr)
                raise SystemExit(1)
        audit_source = "\n".join([*("import " + name for name, _, _ in MODULES), "", *("#print axioms " + declaration for declaration in public + imported_public), ""])
        audit_path = obj / "Audit.lean"
        audit_path.write_text(audit_source)
        audited = run([lean, "-DautoImplicit=false", "-DwarningAsError=true", str(audit_path)], env=env)
        (logs / "Audit.lean").write_text(audit_source)
        (logs / "Audit.stdout.log").write_text(audited.stdout)
        (logs / "Audit.stderr.log").write_text(audited.stderr)
        inventories = re.findall(r"depends on axioms:\s*\[([^\]]*)\]", audited.stdout)
        standard = {"propext", "Classical.choice", "Quot.sound"}
        seen = {a.strip() for inv in inventories for a in inv.split(",") if a.strip()}
        covered = len(inventories) + audited.stdout.count("does not depend on any axioms")
        success = audited.returncode == 0 and not (seen - standard) and covered == len(public + imported_public)
        result.update({
            "new_public_theorems": len(public),
            "imported_public_theorems": len(imported_public),
            "axiom_audit": {"exit_code": audited.returncode, "audited": covered, "axioms": sorted(seen)},
            "seconds": round(time.monotonic() - started, 3),
            "success": success,
        })
        receipt_path.write_text(json.dumps(result, indent=2) + "\n")
        if not success:
            print(audited.stdout + audited.stderr)
            raise SystemExit("Axiom audit failed or missed a declaration")
    print(json.dumps({"success": True, "new_public_theorems": len(public), "imported_public_theorems": len(imported_public), "axioms": sorted(seen)}))


if __name__ == "__main__":
    main()
