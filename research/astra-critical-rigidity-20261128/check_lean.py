#!/usr/bin/env python3
"""Compile selected mathematical modules freshly and audit their public roots.

The caller supplies Lean 4.34.1 and the pinned Mathlib cache. Dependency objects
are reused. This is neither a cold dependency build nor a LeanChecker replay.
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
PACKET = Path("research/astra-critical-rigidity-20261128")
MATHLIB = "d13f23b723b8a846827a245b89c10fc7d3f11612"
MODULES = {
    "AffineOrbit": ("formal/AffineOrbit.lean", "Collatz.PoweredAffine",
        "Actual shortcut parity-word identity, repeated affine center identity, and exact changing-center/reference telescopes. No Subspace Theorem or asymptotic height bound is formalized."),
    "TernaryLanding": ("ordinary/TernaryLanding.lean", "Collatz.TernaryLanding",
        "Actual odd-denominator numerator recursion consumes exactly the odd grade, has the full native prefix carry, reaches displayed ternary height zero for positive starts, and preserves ternary units at positive levels. Its rational word value and complete dyadic numerator translation are proved. For pure-three unit sources this supplies first integer landing semantics; all quantitative landing and probability bounds remain written."),
    "MarkedLandingWord": ("ordinary/MarkedLandingWord.lean", "Collatz.MarkedLandingWord",
        "The exact carry equation is sufficient for every actual positive-level parity departure; appending a last odd departure has the stated carry; a prescribed last-odd word has a positive ternary-unit first preimage exactly when the target residue is eligible and exceeds the zero-source affine endpoint. Quantitative real/dyadic routing and reciprocal renewal laws remain written."),
    "AdjacentWordClosure": ("ordinary/AdjacentWordClosure.lean", "Collatz.AdjacentWordClosure",
        "Final affine divisibility characterizes an actual native word; every odd-step progression realizes each word; the equal-grade ordered carry equation preserves an adjacent pair; arbitrarily large positive odd sources and their triples realize both calendars and remain unmatched through the complete supplied loop. The converse construction is supplied by the separate PrefixCarryClosure and ClockCarryEquivalence modules."),
    "ConditionalParitySuffix": ("literature/ConditionalParitySuffix.lean", "Collatz.ConditionalParitySuffix",
        "Every odd-step progression has precisely one parameter residue realizing a supplied ordinary parity word; a full modulus shift preserves the actual prefix and translates its endpoint; conditional on an odd input and a realized multiplier prefix, exactly one coefficient residue realizes each prescribed physical suffix. Quenched coefficient selection, Brownian release laws and population limits remain written."),
    "SynchronousPhase": ("ordinary/SynchronousPhase.lean", "Collatz.SynchronousPhase",
        "Actual same-date meeting on positive integers is an equivalence; shortcut and doubling induce an invertible quotient shift; phase return is equivalent to a genuine periodic tail; a finite equal-phase family has one common actual date. On the periodic locus phase equality is physical equality, and any off-locus collision forces the exact same later first-entry date. The quotient shift construction is additionally audited but is not counted as another theorem root. All density, Gaussian and limiting collision criteria remain written."),
    "FiniteBranchCapture": ("literature/FiniteBranchCapture.lean", "Collatz.FiniteBranchCapture",
        "Every actual positive shortcut trajectory attains a global minimum, which passes every finite no-smaller-state guard. Any modified rule changing all guarded vertices has a first physical disagreement by that minimum, with an exactly shared prefix. Explicit local routing and forced-change assumptions give the first designated-set entrance between one date before and three dates after disagreement. The analytic shadowing, phase construction, computability margins and probability laws remain written."),
    "OneSparseOrbit": ("literature/OneSparseOrbit.lean", "Collatz.OneSparseOrbit",
        "After one true odd departure all subsequent states are ternary units; the entire predecessor set of every ternary multiple is its dyadic halving ray. Explicit selected odd multiples grow under an additive change of at most two; the actual modified iteration diverges, and all sources outside selected dyadic rays retain their whole true prefix until the anchor. Density estimates, statistical limits and the conditional unit-change converse remain written."),
    "RoundedOrbitCapture": ("literature/RoundedOrbitCapture.lean", "Collatz.RoundedOrbitCapture",
        "The actual least-odd rounding has error zero or one on every odd departure, is injective there and has exact geometric iterate bounds. A bounded decidable search equals the whole forward closure of Boolean seeds. The constructed map preserves all even edges and every edge through the seed barrier; any genuine hit forces its actual modified trajectory into the growing closure, including earlier capture. Seed sparsity, capture densities and probabilistic comparisons remain written."),
    "SparseNativeTargets": ("ordinary/SparseNativeTargets.lean", "Collatz.SparseNativeTargets",
        "The native affine balance exactly characterizes actual parity and endpoint; the full ternary divisor and height characterize attainable integer targets. Odd-gap calendars have exact grade, clock and carry, and their suffix fixes the actual target residue independently of all earlier steps. A finite union of genuine visiting sources is bounded by the sum of eligible target-residue counts. Stationary densities, transport and asymptotic sparse-target bounds remain written."),
    "InverseSuffixTransport": ("ordinary/InverseSuffixTransport.lean", "Collatz.InverseSuffixTransport",
        "An actual source is at most its endpoint times the full dyadic inverse factor. A target below the threshold reached before the first odd entrance lies on its exact halving coast. A sufficiently large genuine odd entrance precedes the entire k-step suffix, and the ordered integer suffix read there equals the original incoming list. Distributional transport, Brownian limits and inverse-density estimates remain written."),
    "PairedClock": ("ordinary/PairedClock.lean", "Collatz.PairedClock",
        "Actual two-source discrepancy, its source-independent bound and exact halving, and the quadratic native-clock bound for unmatched odd ternary-power pairs. The fixed-target classification is formalized separately in JointTargets."),
    "SignedReturnRouter": ("ordinary/SignedReturnRouter.lean", "Collatz.SignedReturnRouter",
        "Constructive signed affine calendar routes: descent to a nonzero translation with the exceptional detour, positive contraction, both signs and reset to either adjacent orientation with linear combined-grade bounds. Includes three public cost identities. Physical replay is proved in PrefixCarryClosure."),
    "PrefixCarryClosure": ("ordinary/PrefixCarryClosure.lean", "Collatz.PrefixCarryClosure",
        "Integral affine routes force every upper physical parity when the lower word is realized. Every actual nonmerged adjacent prefix with ternary-unit endpoints closes at linear grade cost. Every ordinary odd source/triple suffix yields equal-grade ordered carry words extending its actual calendars after the explicit first-step substitution."),
    "ClockCarryEquivalence": ("ordinary/ClockCarryEquivalence.lean", "Collatz.ClockCarryEquivalence",
        "Connected two-way reduction between actual ordinary unmatched horizons and ordered carry words; existence and the exact sandwich for both finite maxima; equivalence of the global logarithmic clock bound and the bound at each word pair's actual common grade. The truth of the remaining logarithmic arithmetic bound is not assumed or proved."),
    "CrossGrade": ("ordinary/CrossGrade.lean", "Collatz.PairedClock",
        "Actual two-grade exponential native-clock bound, including the exact discount for simultaneous odd departures. The associated logarithmic estimate is a written corollary."),
    "JointTargets": ("ordinary/JointTargets.lean", "Collatz.PairedClock",
        "Full classification of fixed positive targets admitting unbounded odd joint predecessors of uniformly bounded total grade: exactly the forward-comparable ternary-unit pairs. Includes the explicit incomparable-source height bound."),
    "BoundaryRanks": ("ordinary/BoundaryRanks.lean", "Collatz.BoundaryRanks",
        "Calendar-weighted prefix/suffix identities for actual finite-dimensional submodule ranks with arbitrary endpoint dimensions, and the dimension bound from shared independent directions. The analytic endpoint estimate remains a written proof."),
    "OrderedMismatchWindows": ("cycles/OrderedMismatchWindows.lean", "Collatz.OrderedMismatchWindows",
        "Exact total length of wrapped fixed-budget mismatch windows, permutation of terminal costs, and the summed finite endpoint inequality. No limiting mismatch or denominator theorem is formalized."),
    "EventFactorRank": ("cycles/EventFactorRank.lean", "Collatz.EventFactorRank",
        "Independence of nonnegative weighted prime-valuation rows from strict pairwise overlap bounds, the common-point interval gap estimate, and the resulting finite-dimensional rank obstruction. The full Collatz gcd inputs and integrated height estimates remain written proofs."),
    "ReferenceDivisibility": ("formal/ReferenceDivisibility.lean", "Collatz.ReferenceDivisibility",
        "Integer-cleared actual and reference affine laws imply a complete dyadic divisor and its nonzero height cost. No asymptotic height statement or Subspace Theorem is formalized."),
    "RotationOccupation": ("cycles/RotationOccupation.lean", "Collatz.RotationOccupation",
        "Cleared odd traces, an exact partial unequal final edge, the complete two-sided divisor at an interior date, and elementary spacing/counting kernels. The global rotation-occupation and limiting pressure theorems remain written proofs."),
    "TwoGradePairOrder": ("cycles/TwoGradePairOrder.lean", "Collatz.TwoGradePairOrder",
        "The pair-order and pair-sum injectivity kernel for an integer octave with exact doubling, two-valued affine tags and a transitive physical shift. The cyclic integer sign propagation, weighted identity and Eisenstein separation are proved. Construction of this input structure from an ordinary Collatz cycle remains a written argument."),
    "ResidueFiberOrder": ("cycles/ResidueFiberOrder.lean", "Collatz.ResidueFiberOrder",
        "A periodic ordered lift with an equivariant group-valued residue, strict order preservation on each residue fiber and a full cyclic phase has residue multiplier of exactly the full period. The finite-order monotonicity and phase obstruction are proved. The physical dyadic lift construction, inversion count and width-nine sufficient condition remain written arguments."),
    "IntegerMinorConcentration": ("literature/IntegerMinorConcentration.lean", "Collatz.IntegerMinorConcentration",
        "An exact integer row congruence implies divisibility of the determinant times every coefficient; a columnwise Leibniz bound and a nonzero coefficient force a minor to vanish below its modulus. Coefficient heights are unrestricted. The physical packet selection, Cramer basis step, valuation-level counting and effective asymptotic landing bounds remain written."),
    "FullDenominatorPairZero": ("cycles/FullDenominatorPairZero.lean", "Collatz.FullDenominatorPairZero",
        "For a scaled integer pair comparison on a transitive native cycle, one zero forces divisibility by the entire denominator coprime to two. Dividing by that denominator yields an integer recurrence with forcing between minus two and two; persistence of a nonzero sign then forces every comparison to be zero. The physical chart and sparse-recurrence exclusion remain written."),
    "NativeTubeZero": ("cycles/NativeTubeZero.lean", "Collatz.NativeTubeZero",
        "On a finite native comparison tube scaled by its complete denominator coprime to three, a terminal zero forces every preceding comparison and every integer forcing in [-2,2] to vanish. No cyclic closure, transitivity, spatial ordering or denominator-size premise is used. Construction of the actual binary tube, prime dilation, entropy and asymptotic band-exit applications remain written."),
    "PooledMultiplicityCapacity": ("cycles/PooledMultiplicityCapacity.lean", "Collatz.PooledMultiplicityCapacity",
        "For a literal binary coordinate array separating every pair of h-multisets, k independent multiplicities up to cap can be padded by a reference when k*cap <= h. Their exact finite injection gives (cap+1)^k <= (h+1)^n. The actual cyclic code, pooled active-row count and sharp asymptotic denominator rate remain written."),
    "RotationRecurrenceRank": ("cycles/RotationRecurrenceRank.lean", "Collatz.RotationRecurrenceRank",
        "For the actual dyadic cumulative input and physical affine recurrence, any constant shifted-input ratio run is shorter than a supplied monic recurrence degree. Literal valuation agreement on a supplied circular partition gives p <= u*(d-1). Constructing the physical minimal recurrence and partition, the exact equality family and all denominator asymptotics remain written."),
    "GuardedTernaryTube": ("cycles/GuardedTernaryTube.lean", "Collatz.GuardedTernaryTube",
        "Genuine varying dyadic windings accumulate the complete ternary guard divisor. With full denominator coprime to three, one terminal zero forces every comparison and forcing to vanish when nonzero forcings have g preceding zero dates and absolute value below 3^(g+1). The supplied guard is inside the finite edge interval. Actual chart construction, prime dilation, generalized Vandermonde bounds and residence estimates remain written."),
}
ALLOWED_AXIOMS = {"Classical.choice", "Quot.sound", "propext"}
ADDITIONAL_DEFINITIONS = {"SynchronousPhase": ["Collatz.SynchronousPhase.shift"]}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run(command: list[str], env: dict[str, str] | None = None,
        timeout: int = 1800) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, env=env, text=True,
                          capture_output=True, timeout=timeout)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--only", action="append", choices=sorted(MODULES))
    parser.add_argument("--temporary-root", type=Path)
    args = parser.parse_args()
    lean, mathlib = args.lean.resolve(), args.mathlib.resolve()
    version = run([str(lean), "--version"])
    if version.returncode or "version 4.34.1," not in version.stdout:
        raise SystemExit("Expected Lean 4.34.1")
    pin = run(["git", "-C", str(mathlib), "rev-parse", "HEAD"])
    if pin.returncode or pin.stdout.strip() != MATHLIB:
        raise SystemExit("Unexpected Mathlib source pin")
    cache = mathlib / ".lake/build/lib/lean"
    packages = sorted((mathlib / ".lake/packages").glob("*/.lake/build/lib/lean"))
    if not cache.is_dir():
        raise SystemExit("Mathlib dependency cache missing")
    wanted = set(args.only or MODULES)
    required = set(wanted)
    pending = list(required)
    while pending:
        name = pending.pop()
        source = (ROOT / PACKET / MODULES[name][0]).read_text()
        for line in re.findall(r"^import\s+([^\n]+)", source, re.MULTILINE):
            for dependency in line.split():
                if dependency in MODULES and dependency not in required:
                    required.add(dependency)
                    pending.append(dependency)
    selected = [name for name in MODULES if name in required]
    receipt = args.receipt.resolve()
    receipt.parent.mkdir(parents=True, exist_ok=True)
    logdir = receipt.parent / (receipt.stem + "-logs")
    logdir.mkdir(exist_ok=True)
    result = {
        "schema": "collatz-critical-rigidity-lean/v1", "success": False,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "compiler": version.stdout.strip(), "mathlib_source_commit": MATHLIB,
        "dependency_manifest_sha256": digest((mathlib / "lake-manifest.json").read_bytes()),
        "dependency_scope": "Pinned cached Mathlib and third-party objects reused; every selected packet object freshly compiled. No cold rebuild or independent LeanChecker run.",
        "requested": sorted(wanted), "compiled": selected, "modules": [],
    }
    began = time.monotonic()
    public: list[str] = []
    with tempfile.TemporaryDirectory(prefix="collatz-critical-lean-",
                                    dir=args.temporary_root) as tmp:
        obj = Path(tmp)
        env = os.environ.copy()
        env["LEAN_PATH"] = os.pathsep.join(map(str, [obj, cache, *packages]))
        for name in selected:
            relative, namespace, scope = MODULES[name]
            source = ROOT / PACKET / relative
            before = source.read_bytes()
            names = re.findall(r"^(?:@\[[^\n]*\]\s*)*(?:theorem|lemma)\s+([A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)*)",
                               before.decode(), re.MULTILINE)
            qualified = [namespace + "." + n for n in names]
            if not qualified:
                raise SystemExit("No public theorem roots in " + str(source))
            if len(qualified) != len(set(qualified)):
                raise SystemExit("Duplicate public theorem roots in " + str(source))
            public.extend(qualified)
            start = time.monotonic()
            check = run(
                [str(lean), "-j1", "-DautoImplicit=false", "-DwarningAsError=true",
                 "-o", str(obj / (name + ".olean")), str(source)], env=env)
            if source.read_bytes() != before:
                raise SystemExit("Source changed during compilation: " + str(source))
            (logdir / (name + ".stdout.log")).write_text(check.stdout)
            (logdir / (name + ".stderr.log")).write_text(check.stderr)
            result["modules"].append({
                "module": name, "source": (PACKET / relative).as_posix(),
                "source_sha256": digest(before), "exit_code": check.returncode,
                "seconds": round(time.monotonic() - start, 3),
                "public_roots": qualified, "mathematical_scope": scope,
            })
            receipt.write_text(json.dumps(result, indent=2) + "\n")
            print(f"{name}: exit {check.returncode}; {len(qualified)} public roots", flush=True)
            if check.returncode:
                print(check.stdout + check.stderr)
                raise SystemExit(1)
        extra = [root for module in selected for root in ADDITIONAL_DEFINITIONS.get(module, [])]
        audit_text = "\n".join([*("import " + n for n in selected), "",
                                *("#print axioms " + n for n in public + extra), ""])
        audit_path = obj / "Audit.lean"
        audit_path.write_text(audit_text)
        audit = run([str(lean), "-j1", "-DautoImplicit=false", "-DwarningAsError=true",
                     str(audit_path)], env=env)
        (logdir / "Audit.lean").write_text(audit_text)
        (logdir / "Audit.stdout.log").write_text(audit.stdout)
        (logdir / "Audit.stderr.log").write_text(audit.stderr)
        rows = re.findall(r"depends on axioms:\s*\[([^\]]*)\]", audit.stdout)
        seen = {a.strip() for row in rows for a in row.split(",") if a.strip()}
        count = len(rows) + audit.stdout.count("does not depend on any axioms")
        success = audit.returncode == 0 and count == len(public) + len(extra) and not (seen - ALLOWED_AXIOMS)
        result.update({"success": success, "public_roots": len(public),
            "additional_audited_definitions": extra,
            "axiom_audit": {"exit_code": audit.returncode, "audited": count,
                            "axioms": sorted(seen)},
            "finished_utc": datetime.now(timezone.utc).isoformat(),
            "seconds": round(time.monotonic() - began, 3)})
        receipt.write_text(json.dumps(result, indent=2) + "\n")
        if not success:
            print(audit.stdout + audit.stderr)
            raise SystemExit("Axiom inventory failed or missed a public theorem")
    print(json.dumps({"success": True, "public_roots": len(public), "axioms": sorted(seen)}))


if __name__ == "__main__":
    main()
