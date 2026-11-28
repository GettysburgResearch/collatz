#!/usr/bin/env python3
"""Finite sanity checks for the written bounded-affine spectral estimate.

Only the Python standard library is required. These numerical checks catch
frequency, rational-translation, and shift-index errors. They do not replace
the exact proof in FINITE_AFFINE_GAP.md or certify an asymptotic spectral gap.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    # (sign, exponent of 3, even translation numerator, ternary denominator)
    # This is an inverse-symmetric list, with the final involution self-inverse.
    charts = [
        (1, 1, 0, 0), (1, -1, 0, 0),
        (1, 0, 2, 0), (1, 0, -2, 0),
        (1, 1, 2, 0), (1, -1, -2, 1),
        (-1, 0, 2, 1),
    ]
    R, S, B = 1, 1, 2
    J = max(R, S)
    cases = []
    individual_checks = 0
    largest_mean_error = 0.0
    largest_norm_error = 0.0
    for w in (8, 10, 12, 14, 16, 18):
        Q = 1 << w
        N = Q // 2
        maps = [(sign * pow(3, r, Q) % Q,
                 numerator * pow(3, -s, Q) % Q)
                for sign, r, numerator, s in charts]
        assert all(a % 2 == 1 and b % 2 == 0 for a, b in maps)
        for a, b in maps:
            inverse_a = pow(a, -1, Q)
            assert (inverse_a, -inverse_a * b % Q) in maps
        for m in range(1, 6):
            if 3 ** (J + m - 1 + R) >= Q / 4:
                continue
            coefficients = [math.sin(math.pi * (i + 1) / (m + 1))
                            for i in range(m)]
            frequencies = [3 ** (J + i) for i in range(m)]
            values = [
                math.fsum(c * math.cos(2 * math.pi * k * x / Q)
                          for c, k in zip(coefficients, frequencies))
                for x in range(1, Q, 2)
            ]
            mean_error = abs(math.fsum(values) / N)
            norm = math.fsum(value * value for value in values) / N
            exact_norm = math.fsum(c * c for c in coefficients) / 2
            norm_error = abs(norm - exact_norm)
            assert mean_error < 2e-12
            assert norm_error < 2e-11
            largest_mean_error = max(largest_mean_error, mean_error)
            largest_norm_error = max(largest_norm_error, norm_error)
            rayleigh_terms = []
            refined_bounds = []
            for chart, (a, b) in zip(charts, maps):
                sign, r, numerator, s = chart
                squared_difference = math.fsum(
                    (values[((a * (2 * i + 1) + b) % Q - 1) // 2]
                     - values[i]) ** 2
                    for i in range(N)
                ) / N
                relative_difference = squared_difference / norm
                translation_phase = (
                    2 * math.pi * abs(numerator)
                    * 3 ** (J + m - 1 - s) / Q
                )
                bound = (math.pi * abs(r) / (m + 1)
                         + translation_phase) ** 2
                assert relative_difference <= bound + 2e-10, (
                    w, m, chart, relative_difference, bound)
                rayleigh_terms.append(relative_difference / 2)
                refined_bounds.append(bound / 2)
                individual_checks += 1
            rayleigh = math.fsum(rayleigh_terms) / len(charts)
            refined_bound = math.fsum(refined_bounds) / len(charts)
            uniform_bound = (
                math.pi * R / (m + 1)
                + 2 * math.pi * B * 3 ** (J + m - 1) / Q
            ) ** 2 / 2
            assert rayleigh <= refined_bound + 2e-10
            assert refined_bound <= uniform_bound + 2e-10
            cases.append({
                "w": w, "Q": Q, "packet_length": m,
                "rayleigh": rayleigh, "refined_bound": refined_bound,
                "uniform_bound": uniform_bound,
            })
    multiplier_checks = 0
    for w in range(3, 19):
        Q, L = 1 << w, 1 << (w - 2)
        assert pow(3, L, Q) == 1 and pow(3, L // 2, Q) != 1
        assert all(pow(3, r, 8) != 7 for r in range(2))
        for Rm in (1, 2, 3, 7, 15):
            # Symmetric uniform integer exponents [-Rm,Rm], plus free sign.
            lamb = math.fsum(math.cos(2 * math.pi * r / L)
                             for r in range(-Rm, Rm + 1)) / (2 * Rm + 1)
            second_moment = Rm * (Rm + 1) / 3
            bound = 2 * math.pi ** 2 * second_moment / L ** 2
            assert 1 - lamb <= bound + 2e-14
            multiplier_checks += 1
    report = {
        "schema": "collatz-bounded-affine-gap-check/v1",
        "utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Finite floating-point sanity checks of exact written formulas; no claimed spectral-gap lower bound or formal proof.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "charts": charts,
        "packet_cases": len(cases),
        "individual_chart_checks": individual_checks,
        "multiplier_character_checks": multiplier_checks,
        "largest_absolute_mean_error": largest_mean_error,
        "largest_absolute_norm_error": largest_norm_error,
        "cases": cases,
        "success": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in (
        "success", "packet_cases", "individual_chart_checks",
        "multiplier_character_checks", "largest_absolute_mean_error",
        "largest_absolute_norm_error")}, indent=2))


if __name__ == "__main__":
    main()
