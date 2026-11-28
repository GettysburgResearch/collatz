#!/usr/bin/env python3
"""Freshly compile this packet and audit every public theorem's axioms.

Mathlib and its dependencies are reused from the explicitly supplied pinned
cache. This is not a cold dependency rebuild or an independent LeanChecker run.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
PACKET = Path("research/astra-global-rigidity-20261128")
MATHLIB_PIN = "d13f23b723b8a846827a245b89c10fc7d3f11612"
MODULES = [
    ("WidthCarry", "cycles/WidthCarry.lean", "CollatzResearch.WidthCarry"),
    ("CriticalCountStandalone", "mass/CriticalCountStandalone.lean", "Collatz.CriticalCount"),
    ("BasinDefects", "mass/BasinDefects.lean", "Collatz.CriticalCount"),
    ("MersenneCrests", "mersenne/MersenneCrests.lean", "Collatz.MersenneCrests"),
    ("ProtectedDescent", "cycles/ProtectedDescent.lean", "CollatzResearch.ProtectedDescent"),
    ("RampReference", "mersenne/RampReference.lean", "Collatz.RampReference"),
    ("UpDownCounterexample", "cycles/UpDownCounterexample.lean", "CollatzResearch.UpDownCounterexample"),
    ("UpDownRayBand", "cycles/UpDownRayBand.lean", "CollatzResearch.UpDownRayBand"),
    ("RandomDirectionLoops", "cycles/RandomDirectionLoops.lean", "CollatzResearch.RandomDirectionLoops"),
    ("MovingFloorAntichain", "mass/MovingFloorAntichain.lean", "Collatz.MovingFloor"),
    ("AbsoluteOffsetBudget", "mass/AbsoluteOffsetBudget.lean", "Collatz.AbsoluteOffsetBudget"),
    ("ShiftedRampCores", "mersenne/ShiftedRampCores.lean", "Collatz.ShiftedRampCores"),
    ("GuardedHoles", "cycles/GuardedHoles.lean", "CollatzResearch.GuardedHoles"),
    ("ShiftedSiblingCarries", "mersenne/ShiftedSiblingCarries.lean", "Collatz.ShiftedSiblingCarries"),
    ("CoreTransport", "mersenne/CoreTransport.lean", "Collatz.CoreTransport"),
    ("DepthDeficits", "cycles/DepthDeficits.lean", "Collatz.DepthDeficits"),
    ("PhaseClamping", "cycles/PhaseClamping.lean", "Collatz.PhaseClamping"),
    ("DepthBridge", "cycles/DepthBridge.lean", "Collatz.DepthBridge"),
]


def run(argv, *, env=None, timeout=1800):
    return subprocess.run(argv, cwd=ROOT, env=env, text=True,
                          encoding="utf-8", capture_output=True, timeout=timeout)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def verify_overlay(overlay, roots):
    """Select only matching Mathlib objects; preserve compiler/package import locations."""
    rows = []
    size = 0
    skipped = 0
    for path in sorted(p for p in overlay.rglob("*") if p.is_file()):
        relative = path.relative_to(overlay)
        if relative.parts[0] != "Mathlib" and not relative.name.startswith("Mathlib."):
            skipped += 1
            continue
        originals = [root/relative for root in roots if (root/relative).is_file()]
        if not originals:
            skipped += 1
            continue
        fingerprint = file_sha(path)
        if not any(p.stat().st_size == path.stat().st_size and file_sha(p) == fingerprint
                   for p in originals):
            raise RuntimeError("Cache overlay differs from pinned cache: "+str(relative))
        rows.append([relative.as_posix(), fingerprint])
        size += path.stat().st_size
    return rows, {"files": len(rows), "bytes": size, "unused_extra_files": skipped,
            "verified_manifest_sha256": sha(json.dumps(rows, separators=(",", ":")).encode()),
            "scope": "Only byte-hashed Mathlib matches to the pinned cache are linked into a private directory. Compiler and third-party package objects retain their original import locations. Extra files are not placed on LEAN_PATH. No dependency was rebuilt."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    parser.add_argument("--only", action="append", choices=[name for name, _, _ in MODULES],
                        help="compile only named modules and their packet import dependencies; repeat as needed")
    parser.add_argument("--timeout-seconds", type=int, default=1800,
                        help="wall-time limit for each compiler invocation")
    parser.add_argument("--cache-overlay", type=Path,
                        help="optional read-only dependency cache; only verified matches to pinned cache files are used")
    args = parser.parse_args()
    requested = set(args.only or [name for name, _, _ in MODULES])
    required = set(requested)
    by_name = {name: rel for name, rel, _ in MODULES}
    pending = list(required)
    while pending:
        name = pending.pop()
        source = (ROOT / PACKET / by_name[name]).read_text()
        imports = {token for line in re.findall(r"^import\s+([^\n]+)", source, re.MULTILINE)
                   for token in line.split() if token in by_name}
        for imported in imports - required:
            required.add(imported)
            pending.append(imported)
    selected_modules = [row for row in MODULES if row[0] in required]
    if args.timeout_seconds <= 0:
        parser.error("--timeout-seconds must be positive")
    lean, mathlib, receipt = args.lean.resolve(), args.mathlib.resolve(), args.receipt.resolve()
    receipt.parent.mkdir(parents=True, exist_ok=True)
    logs = receipt.parent / "lean"
    logs.mkdir(exist_ok=True)
    version = run([str(lean), "--version"])
    if version.returncode or "4.34.1" not in version.stdout:
        raise RuntimeError("This replay requires Lean 4.34.1")
    pin = run(["git", "-C", str(mathlib), "rev-parse", "HEAD"])
    if pin.returncode or pin.stdout.strip() != MATHLIB_PIN:
        raise RuntimeError("Mathlib source does not have the required commit")
    cache = mathlib / ".lake/build/lib/lean"
    package_caches = sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
    if not cache.is_dir():
        raise RuntimeError("The pinned Mathlib dependency cache is missing")
    overlay = args.cache_overlay.resolve() if args.cache_overlay else None
    overlay_record = None
    overlay_files = []
    if overlay:
        overlay_files, overlay_record = verify_overlay(overlay, [cache, *package_caches, lean.parent.parent/"lib/lean"])
        print(f"Verified cache overlay: {overlay_record['files']} files", flush=True)
    result = {
        "schema": "collatz-astra-global-rigidity-lean/v1", "success": False,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "compiler": version.stdout.strip(), "mathlib_source_commit": MATHLIB_PIN,
        "dependency_manifest_sha256": sha((mathlib / "lake-manifest.json").read_bytes()),
        "cache_overlay": overlay_record,
        "dependency_scope": "Reused Mathlib and third-party compiled dependencies; fresh objects for every selected packet module; no cold dependency rebuild or independent LeanChecker run.",
        "selection": {"mode": "subset" if args.only else "all",
                      "requested": sorted(requested), "compiled": [row[0] for row in selected_modules],
                      "not_compiled": [row[0] for row in MODULES if row[0] not in required]},
        "mathematical_scope": "Finite carry identities, actual-orbit centered counts, literal basin defects, Mersenne crests, convergence of the explicit protected-descent modification, rational inverse-word comparisons, the explicit up-down cycle counterexample, the finite record table and trapping-band closure, every-word up-down loop bounds, the first-floor antichain, the finite absolute-offset occupation/floor inequalities, actual consecutive shifted-ramp identities, finite reduced-core transport inequalities, shifted sibling carry and gcd identities, finite depth-entry and block-deficit inequalities, phase-clamping legality and reward bounds, finite depth-bridge lattice and swap kernels, separated and automatic hole guards, and the automatic three-or-six-step return arithmetic only. The word-pressure existence and differentiability, full entropy limits and near-maximal asymptotics, unrestricted higher-product theorems, sparse-sum gcd bound, infinite hole scheduling, automatic-chain frequency and growth rates, core transport and retention asymptotics, fixed-root cell laws, solenoid averaging, recent rational-logarithm estimate, random-direction probability threshold, infinite ray/cycle assembly, analytic Gaussian or trace laws, multiplicative sampling, density and prime-distribution inputs, sharp modification asymptotics, and original Collatz conclusion are not formalized here.",
        "modules": [],
    }
    started = time.monotonic()
    public = []
    with tempfile.TemporaryDirectory(prefix="collatz-diagonal-lean-") as tmp:
        obj = Path(tmp)
        verified_overlay = obj/"VerifiedDependencies"
        if overlay:
            for relative, _ in overlay_files:
                link = verified_overlay/relative
                link.parent.mkdir(parents=True, exist_ok=True)
                link.symlink_to(overlay/relative)
        env = os.environ.copy()
        env["LEAN_PATH"] = os.pathsep.join(map(str,
            [obj, *([verified_overlay] if overlay else []), cache, *package_caches]))
        for name, rel, namespace in selected_modules:
            path = PACKET / rel
            source = ROOT / path
            before_bytes = source.read_bytes()
            declarations = re.findall(
                r"^(?:@\[[^\n]*\]\s*)*(?:theorem|lemma)\s+([A-Za-z_][A-Za-z0-9_'.]*)",
                before_bytes.decode(), re.MULTILINE)
            qualified = [namespace+"."+d for d in declarations]
            if not qualified:
                raise RuntimeError("No public theorem declarations found in "+str(path))
            public.extend(qualified)
            begin = time.monotonic()
            try:
                compiled = run([str(lean), "-j1", "-DautoImplicit=false", "-DwarningAsError=true",
                                "-o", str(obj/(name+".olean")), str(path)],
                               env=env, timeout=args.timeout_seconds)
            except subprocess.TimeoutExpired as exc:
                def decoded(value):
                    return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else (value or "")
                compiled = subprocess.CompletedProcess(exc.cmd, 124, decoded(exc.stdout),
                    decoded(exc.stderr)+f"\nCompiler wall-time limit exceeded: {args.timeout_seconds}s\n")
            if source.read_bytes() != before_bytes:
                raise RuntimeError("Source changed during compilation: "+str(path))
            (logs/(name+".stdout.log")).write_text(compiled.stdout)
            (logs/(name+".stderr.log")).write_text(compiled.stderr)
            result["modules"].append({"module": name, "source": path.as_posix(),
                "source_sha256": sha(before_bytes), "exit_code": compiled.returncode,
                "seconds": round(time.monotonic()-begin, 3), "public_theorems": qualified})
            receipt.write_text(json.dumps(result, indent=2)+"\n")
            print(f"{name}: exit {compiled.returncode}; {len(qualified)} public theorems", flush=True)
            if compiled.returncode:
                print(compiled.stdout+compiled.stderr)
                raise SystemExit(1)
        audit = "\n".join([*("import "+name for name, _, _ in selected_modules), "",
                             *("#print axioms "+name for name in public), ""])
        audit_path = obj/"Audit.lean"
        audit_path.write_text(audit)
        checked = run([str(lean), "-j1", "-DautoImplicit=false", "-DwarningAsError=true",
                       str(audit_path)], env=env, timeout=args.timeout_seconds)
        (logs/"Audit.lean").write_text(audit)
        (logs/"Audit.stdout.log").write_text(checked.stdout)
        (logs/"Audit.stderr.log").write_text(checked.stderr)
        inventories = re.findall(r"depends on axioms:\s*\[([^\]]*)\]", checked.stdout)
        seen = {a.strip() for row in inventories for a in row.split(",") if a.strip()}
        covered = len(inventories)+checked.stdout.count("does not depend on any axioms")
        standard = {"propext", "Classical.choice", "Quot.sound"}
        success = checked.returncode == 0 and not (seen-standard) and covered == len(public)
        result.update({"success": success, "public_theorems": len(public),
            "axiom_audit": {"exit_code": checked.returncode, "audited": covered, "axioms": sorted(seen)},
            "seconds": round(time.monotonic()-started, 3),
            "finished_utc": datetime.now(timezone.utc).isoformat()})
        receipt.write_text(json.dumps(result, indent=2)+"\n")
        if not success:
            print(checked.stdout+checked.stderr)
            raise SystemExit("Axiom inventory failed or missed a public theorem")
    print(json.dumps({"success": True, "public_theorems": len(public), "axioms": sorted(seen)}))


if __name__ == "__main__":
    main()
