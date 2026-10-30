#!/usr/bin/env python3
"""Exact arithmetic checks and explicitly finite diagnostics for DREG-001--007.

No experiment in this file proves the OPEN dyadic regularity hypothesis.
The finite observable R_M is exact rational. Diagnostic moments are floats,
labelled EMPIRICAL; all asserted arithmetic identities use Python integers or
fractions.Fraction. No network, external package, or conjectural oracle is used.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def bounded_tau(n: int, limit: int, known: dict[int, int]) -> int | None:
    """Return the exact hitting time if certified within limit; else None.

    Known tails are exact finite proofs obtained by earlier paths; they may
    shortcut the simulation but do not change the declared clock bound.
    """
    x = n
    path: list[int] = []
    while x not in known and len(path) < limit:
        path.append(x)
        x = shortcut(x)
    if x not in known:
        return None
    total = len(path) + known[x]
    tail = known[x]
    for y in reversed(path):
        tail += 1
        known[y] = tail
    return total if total <= limit else None


def parity_checks(max_bits: int = 12) -> list[dict[str, int]]:
    checks = []
    for bits in range(1, max_bits + 1):
        modulus = 1 << bits
        parity_codes = set()
        for residue in range(modulus):
            x, code = residue, 0
            for j in range(bits):
                code |= (x & 1) << j
                x = shortcut(x)
            parity_codes.add(code)
        if len(parity_codes) != modulus:
            raise AssertionError(("parity bijection failed", bits))
        preimages = [0] * modulus
        for residue in range(2 * modulus):
            preimages[shortcut(residue) % modulus] += 1
        if any(value != 2 for value in preimages):
            raise AssertionError(("Haar residue balance failed", bits))
        checks.append({"bits": bits, "parity_codes": modulus,
                       "preimages_per_residue": 2})
    return checks


def scalar_defect_checks() -> int:
    count = 0
    for b in range(3, 65):
        for bp in (b - 1, b, b + 1):
            for time in (*range(1, 129), 1_000, 1_000_000):
                old = Fraction(b, b + time)
                new = Fraction(bp, bp + time - 1)
                actual = abs(new - old)
                exact_numerator = abs((bp - b) * time + b)
                exact = Fraction(exact_numerator,
                                 (b + time) * (bp + time - 1))
                if actual != exact or actual > Fraction(1, b - 1):
                    raise AssertionError((b, bp, time, actual))
                count += 1
    return count


def empirical_variances(values: list[float], cutoff: int,
                        bits_list: list[int], logarithmic: bool) -> list[dict]:
    """Weighted least-squares residual at one finite cutoff, not a limit."""
    rows = []
    for bits in bits_list:
        modulus = 1 << bits
        weights = [0.0] * modulus
        first = [0.0] * modulus
        second = [0.0] * modulus
        for n in range(1, cutoff + 1):
            residue = n % modulus
            weight = 1.0 / n if logarithmic else 1.0
            value = values[n]
            weights[residue] += weight
            first[residue] += weight * value
            second[residue] += weight * value * value
        total_weight = math.fsum(weights)
        residual = math.fsum(
            second[a] - first[a] * first[a] / weights[a]
            for a in range(modulus) if weights[a] > 0
        ) / total_weight
        rows.append({"bits": bits, "modulus": modulus,
                     "within_class_variance": residual,
                     "status": "EMPIRICAL_FINITE_CUTOFF"})
    return rows


def run(maximum: int) -> dict:
    if maximum < 100:
        raise ValueError("Choose --maximum at least 100.")
    known = {1: 0}
    reference_multiplier = 32
    times: list[int | None] = [None] * (maximum + 1)
    unresolved = []
    for n in range(1, maximum + 1):
        times[n] = bounded_tau(n, reference_multiplier * n.bit_length(), known)
        if times[n] is None:
            unresolved.append(n)
    multipliers = (1, 2, 4, 8, 16, 32)
    horizon_rows = []
    values_at_32 = [0.0] * (maximum + 1)
    for multiplier in multipliers:
        hits = 0
        values = []
        maximum_truncation_error = Fraction(0)
        for n in range(1, maximum + 1):
            b, time = n.bit_length(), times[n]
            hit = time is not None and time <= multiplier * b
            value = Fraction(b, b + time) if hit else Fraction(0)
            if hit:
                hits += 1
            if time is not None:
                reference_value = Fraction(b, b + time)
                err = reference_value - value
                maximum_truncation_error = max(maximum_truncation_error, err)
                if err > Fraction(1, multiplier + 1):
                    raise AssertionError(("uniform truncation bound", n,
                                          multiplier, str(err)))
            values.append(float(value))
            if multiplier == reference_multiplier:
                values_at_32[n] = float(value)
        horizon_rows.append({
            "multiplier": multiplier,
            "clock": "M * bit_length(n) shortcut steps",
            "certified_hits": hits,
            "unresolved_at_this_clock": maximum - hits,
            "empirical_mean": math.fsum(values) / maximum,
            "largest_observed_truncation_error": str(maximum_truncation_error),
            "proved_uniform_error_budget": f"1/{multiplier + 1}",
            "status": "EMPIRICAL_FINITE_CUTOFF",
        })
    maximum_defect_ratio = Fraction(0)
    defect_witness = None
    tested_defects = 0
    for n in range(4, maximum + 1):
        time = times[n]
        if time is None:
            continue
        b, bp = n.bit_length(), shortcut(n).bit_length()
        if abs(bp - b) > 1:
            raise AssertionError(("bit length bound", n))
        old = Fraction(b, b + time)
        new = Fraction(bp, bp + time - 1)
        ratio = abs(new - old) * (b - 1)
        if ratio > 1:
            raise AssertionError(("orbit defect bound", n, str(ratio)))
        if ratio > maximum_defect_ratio:
            maximum_defect_ratio, defect_witness = ratio, n
        tested_defects += 1
    cutoffs = sorted(set(x for x in (1000, 10000, maximum) if x <= maximum))
    diagnostics = []
    for cutoff in cutoffs:
        for logarithmic in (False, True):
            diagnostics.append({
                "cutoff": cutoff,
                "observable": "R_32",
                "weighting": "harmonic normalized by H_X" if logarithmic
                             else "uniform on [1,X]",
                "rows": empirical_variances(values_at_32, cutoff,
                                             [0, 2, 4, 6, 8], logarithmic),
                "warning": "Fixed-cutoff moments do not prove conditional limiting moments or dyadic regularity.",
            })
    finite_times = [(t, n) for n, t in enumerate(times) if t is not None]
    return {
        "schema": "collatz-dyadic-regularity-diagnostic-v1",
        "map": "shortcut: even n/2, odd (3n+1)/2",
        "status": "BOUNDED_CHECKS_ONLY_REGULARITY_OPEN",
        "maximum_input": maximum,
        "reference_clock_multiplier": reference_multiplier,
        "reference_unresolved_count": len(unresolved),
        "reference_unresolved_first_20": unresolved[:20],
        "maximum_certified_shortcut_time_and_input": list(max(finite_times)),
        "scalar_defect_cases": scalar_defect_checks(),
        "parity_and_Haar_residue_checks": parity_checks(),
        "orbit_defect_checks": tested_defects,
        "largest_observed_defect_to_bound_ratio": str(maximum_defect_ratio),
        "defect_witness_input": defect_witness,
        "finite_horizon_diagnostics": horizon_rows,
        "finite_fiber_variances": diagnostics,
        "external_Lean_build_replayed": False,
        "full_Collatz_proved": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--maximum", type=int, default=100_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = run(args.maximum)
    text = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(json.dumps({"output": str(args.output),
                          "maximum_input": output["maximum_input"],
                          "reference_unresolved_count": output["reference_unresolved_count"],
                          "scalar_defect_cases": output["scalar_defect_cases"],
                          "orbit_defect_checks": output["orbit_defect_checks"],
                          "full_Collatz_proved": False}, sort_keys=True))
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
