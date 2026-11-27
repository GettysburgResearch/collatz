#!/usr/bin/env python3
"""Compile all new modules in a fresh project cache and audit their theorem axioms."""
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
PACKET = Path("research/astra-six-hour-20261127")
MATHLIB = "d13f23b723b8a846827a245b89c10fc7d3f11612"
MODULES = [
    ("MinimumCode", PACKET / "arithmetic/MinimumCode.lean", "Collatz.SixHour.MinimumCode"),
    ("PeriodicSiblings", PACKET / "arithmetic/PeriodicSiblings.lean", "Collatz.SixHour.PeriodicSiblings"),
    ("ColorWords", PACKET / "arithmetic/ColorWords.lean", "Collatz.SixHour.ColorWords"),
    ("FareyCurrent", PACKET / "global/FareyCurrent.lean", "Collatz.SixHour.Farey"),
    ("EllipticMarkers", PACKET / "global/EllipticMarkers.lean", "Collatz.SixHour.Markers"),
    ("FormalTransport", PACKET / "root/FormalTransport.lean", "Collatz.SixHour.FormalTransport"),
    ("TernaryQuotient", PACKET / "arithmetic/TernaryQuotient.lean", "Collatz.SixHour.TernaryQuotient"),
    ("CanonicalBirths", PACKET / "global/CanonicalBirths.lean", "CanonicalBirths"),
    ("ClosedSupport", PACKET / "root/ClosedSupport.lean", "Collatz.SixHour.ClosedSupport"),
    ("CycleSurgery", PACKET / "arithmetic/CycleSurgery.lean", "Collatz.SixHour.CycleSurgery"),
    ("TiltedGreen", PACKET / "global/TiltedGreen.lean", "Collatz.SixHour.TiltedGreen"),
    ("PotentialAssembly", PACKET / "root/PotentialAssembly.lean", "Collatz.SixHour.PotentialAssembly"),
    ("RationalGreen", PACKET / "root/RationalGreen.lean", "Collatz.SixHour.RationalGreen"),
    ("AdaptiveGreen", PACKET / "global/AdaptiveGreen.lean", "Collatz.SixHour.AdaptiveGreen"),
    ("RationalEnergy", PACKET / "root/RationalEnergy.lean", "Collatz.SixHour.RationalEnergy"),
    ("RankDivision", PACKET / "arithmetic/RankDivision.lean", "Collatz.SixHour.RankDivision"),
    ("OrdinaryRelations", PACKET / "global/OrdinaryRelations.lean", "Collatz.SixHour.OrdinaryRelations"),
]


def run(argv: list[str], *, env: dict[str, str] | None = None,
        cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(argv, cwd=cwd, env=env, text=True, capture_output=True)


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
        "schema": "collatz-astra-six-hour-lean/v1",
        "compiler": version.stdout.strip(),
        "mathlib": MATHLIB,
        "dependency_manifest_sha256": hashlib.sha256((mathlib / "lake-manifest.json").read_bytes()).hexdigest(),
        "scope": f"All {len(MODULES)} packet modules, with fresh project objects and pinned Mathlib dependencies. The absent cached Mathlib.Tactic.Field object is built from the pinned source in a temporary overlay. This checks finite word, modular, Farey, sibling, orbit transport, representative-window kernels, conditional finite-crossing/countability, cycle surgery, Green arithmetic, adaptive coefficient bounds, and the conditional implications from explicit rational finite-sum estimates to ordinary Collatz convergence. The energy criterion retains both the uniform bound and uniform target decay. No witness for any open criterion or positive bounded potential is supplied. The divisor counting, interval-complexity estimates, inverse-path laws, analytic singularity and local-mass inputs, closed-support measure-zero application, harmonic trace asymptotics, character analysis, birth-current limits, Green integrals and ordinary upper bounds, energy converse, RH-assisted cycle census, Poisson limits, and other infinite analytic arguments are written proofs and retained inputs, not formalized by this build.",
        "modules": [],
        "success": False,
    }
    started = time.monotonic()
    public: list[str] = []
    imported_public: list[str] = []
    with tempfile.TemporaryDirectory(prefix="collatz-six-hour-lean-") as temporary:
        obj = Path(temporary)
        # A partial Mathlib namespace masks the later cached root. Populate the
        # overlay with symlinks, replacing only Field by a fresh pinned build.
        overlay = obj / "Mathlib"
        (overlay / "Tactic").mkdir(parents=True)
        for child in (cache / "Mathlib").iterdir():
            if child.name != "Tactic":
                (overlay / child.name).symlink_to(child, target_is_directory=child.is_dir())
        for child in (cache / "Mathlib/Tactic").iterdir():
            if child.name != "Field" and not child.name.startswith("Field."):
                (overlay / "Tactic" / child.name).symlink_to(child, target_is_directory=child.is_dir())
        env = os.environ.copy()
        env["LEAN_PATH"] = os.pathsep.join(map(str, [obj, cache, *package_caches]))
        field_source = mathlib / "Mathlib/Tactic/Field.lean"
        field_bytes = field_source.read_bytes()
        field = run([lean, "-DwarningAsError=true", "-o",
                     str(overlay / "Tactic/Field.olean"), str(field_source)], env=env, cwd=mathlib)
        (logs / "Mathlib_Field.stdout.log").write_text(field.stdout)
        (logs / "Mathlib_Field.stderr.log").write_text(field.stderr)
        result["rebuilt_dependencies"] = [{"module": "Mathlib.Tactic.Field",
            "source_sha256": hashlib.sha256(field_bytes).hexdigest(),
            "exit_code": field.returncode, "source_pin": MATHLIB}]
        if field.returncode or field_source.read_bytes() != field_bytes:
            receipt_path.write_text(json.dumps(result, indent=2) + "\n")
            print(field.stdout + field.stderr)
            raise SystemExit("Pinned Mathlib.Tactic.Field rebuild failed")
        print("Mathlib.Tactic.Field: fresh pinned dependency build", flush=True)
        for name, path, namespace in MODULES:
            source = ROOT / path
            source_bytes = source.read_bytes()
            declarations = re.findall(r"^(?:@\[[^\n]*\]\s*)*(?:theorem|lemma)\s+([A-Za-z_][A-Za-z0-9_'.]*)", source_bytes.decode(), re.MULTILINE)
            qualified = [namespace + "." + declaration for declaration in declarations]
            public.extend(qualified)
            before = time.monotonic()
            compiled = run([lean, "-DautoImplicit=false", "-DwarningAsError=true", "-o", str(obj / (name + ".olean")), str(path)], env=env)
            if source.read_bytes() != source_bytes:
                raise RuntimeError("Source changed during compilation: " + str(path))
            (logs / (name + ".stdout.log")).write_text(compiled.stdout)
            (logs / (name + ".stderr.log")).write_text(compiled.stderr)
            result["modules"].append({
                "module": name, "source": path.as_posix(), "new": True,
                "sha256": hashlib.sha256(source_bytes).hexdigest(),
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
