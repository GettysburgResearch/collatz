"""Rebuild this packet's registered finite Lean kernels and audit their axioms.

Requires Lean 4.34.1 and its matching Mathlib checkout with built dependencies.
This does not formalize the written analytic arguments or external inputs.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

SOURCES = {
    "arithmetic/AffineBranchPadding.lean": [
        "Collatz.AffineBranchPadding.grade_append",
        "Collatz.AffineBranchPadding.numerator_append",
        "Collatz.AffineBranchPadding.suffix_preserves_residue",
    ],
    "dynamics/OrdinaryPhaseBound.lean": [
        "Collatz.OrdinaryPhase.oneStep",
        "Collatz.OrdinaryPhase.ordinaryPhaseBound",
    ],
    "dynamics/SourceEnvelope.lean": [
        "Collatz.OrdinaryPhase.stepNumerator",
        "Collatz.OrdinaryPhase.sourceEnvelope",
    ],
    "outside/CommonPrimeAlignment.lean": [
        "AstraWild.CommonPrimeAlignment.centerDefectDvd",
        "AstraWild.CommonPrimeAlignment.centerAlignment",
    ],
}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def run(command, cwd, env):
    p = subprocess.run(command, cwd=cwd, env=env, text=True, capture_output=True)
    if p.returncode:
        raise RuntimeError(json.dumps({"command": command, "stdout": p.stdout,
                                       "stderr": p.stderr, "returncode": p.returncode}))
    return {"command": command, "exit_code": p.returncode,
            "stdout": p.stdout, "stderr": p.stderr}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--lean", required=True, type=Path)
    ap.add_argument("--mathlib", required=True, type=Path)
    ap.add_argument("--mathlib-artifacts", type=Path,
                    help="Override the Mathlib build directory for a separate cache")
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()
    packet = Path(__file__).resolve().parent
    mathlib = args.mathlib.resolve()
    artifacts = [(args.mathlib_artifacts or mathlib / ".lake/build/lib/lean").resolve()]
    artifacts += sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
    if not (artifacts[0] / "Mathlib").is_dir():
        raise RuntimeError("Matching Mathlib build artifacts are missing")
    lean = str(args.lean.resolve())
    receipt = {"scope": "Finite kernels only; cached third-party objects reused",
               "allowed_axioms": sorted(ALLOWED), "modules": [], "audit_roots": []}
    manifest = mathlib / "lake-manifest.json"
    if manifest.exists():
        receipt["mathlib_lake_manifest_sha256"] = hashlib.sha256(manifest.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix="collatz-wild-lean-") as tmp:
        build = Path(tmp)
        env = dict(os.environ)
        env["LEAN_PATH"] = os.pathsep.join(map(str, [build] + artifacts))
        receipt["version"] = run([lean, "--version"], build, env)["stdout"].strip()
        imports = []
        roots = []
        for relative, names in SOURCES.items():
            source = packet / relative
            raw = source.read_bytes()
            local = build / source.name
            local.write_bytes(raw)
            record = run([lean, "-j1", "-DElab.async=false",
                          "-DwarningAsError=true", "-DautoImplicit=false",
                          "-o", str(local.with_suffix(".olean")), source.name], build, env)
            record.update({"source": relative,
                           "source_sha256": hashlib.sha256(raw).hexdigest()})
            receipt["modules"].append(record)
            print(json.dumps({"compiled": relative}), flush=True)
            imports.append("import " + source.stem)
            roots.extend(names)
        audit = "\n".join(imports + ["#print axioms " + r for r in roots]) + "\n"
        (build / "Audit.lean").write_text(audit)
        checked = run([lean, "-j1", "-DElab.async=false",
                       "-DwarningAsError=true", "-DautoImplicit=false", "Audit.lean"],
                      build, env)
        printed = dict(re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", checked["stdout"]))
        for root in roots:
            if root not in printed:
                raise RuntimeError("Missing axiom report: " + root)
            axioms = {s.strip() for s in printed[root].split(",") if s.strip()}
            if not axioms <= ALLOWED:
                raise RuntimeError("Unexpected axioms for " + root + ": " + repr(axioms))
            receipt["audit_roots"].append({"declaration": root, "axioms": sorted(axioms)})
        receipt["audit"] = checked
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"modules": len(SOURCES), "roots": len(roots),
                      "output": str(args.output), "status": "passed"}))


if __name__ == "__main__":
    main()
