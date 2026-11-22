#!/usr/bin/env python3
"""Exact enclosures of the complete moving-endpoint-tilt occupation sums.

Only integer arithmetic and Fraction are used.  The omitted ORIGINAL sources
have the proved tails 2/(3P) for W and 1/P for the censored B statistic.
No trajectory is assumed to converge and no unbounded orbit search is run.
The enclosure is at one finite bin; it is not a proof that the bins decay.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def ceiling_power_three(n: int) -> tuple[int, int]:
    require(n >= 1, "positive centre required")
    j, power = 0, 1
    while power < n:
        j += 1
        power *= 3
    return j, power


def reciprocal_root_interval(c: int, t: int, scale: int) -> tuple[Fraction, Fraction]:
    """Enclose c**(-1/t), certifying the two integer power inequalities."""
    require(c >= 1 and t >= 1 and scale >= 1, "positive root parameters required")
    target = scale ** t
    lo, hi = 0, scale + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if c * mid ** t <= target:
            lo = mid
        else:
            hi = mid
    require(c * lo ** t <= target < c * (lo + 1) ** t, "root bracket failure")
    lower = Fraction(lo, scale)
    upper = lower if c * lo ** t == target else Fraction(lo + 1, scale)
    return lower, upper


def source_visits(p: int, t: int):
    """All visits of one unchanged odd source to bin t, with censor flags."""
    require(p >= 1 and p % 2 == 1 and t >= 1, "odd positive source and positive bin required")
    initial_j, _ = ceiling_power_three(p)
    c, odd_count = p, 0
    alive = p != 1
    visits = []
    previous_bins = [-initial_j]
    limit = 2 * (t + initial_j) + 2
    for clock in range(1, limit + 1):
        if c % 2:
            c = (3 * c + 1) // 2
            odd_count += 1
        else:
            c //= 2
        if c == 1:
            alive = False
        j, power = ceiling_power_three(c)
        current_bin = odd_count - j
        require(current_bin - previous_bins[-1] in (0, 1), "bin skipped or reversed")
        if len(previous_bins) >= 2:
            require(current_bin >= previous_bins[-2] + 1, "two-step bin increase failed")
        previous_bins.append(current_bin)
        if current_bin == t:
            require(c + 1 <= 3 ** (t + 1) * (p + 1) ** 2, "source-centre budget failed")
            visits.append((clock, c, power, alive))
        if current_bin > t:
            require(1 <= len(visits) <= 2, "positive bin has wrong visit count")
            return visits
    raise ValueError("finite bin termination bound failed")


def encode_fraction(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def certify(t: int, cutoff: int, bits: int) -> dict:
    require(t >= 1 and cutoff >= 1 and bits >= 1, "positive bin, source cutoff, and precision required")
    scale = 2 ** bits
    w0 = Fraction(0)
    b0 = Fraction(0)
    wlo = Fraction(0)
    whi = Fraction(0)
    blo = Fraction(0)
    bhi = Fraction(0)
    visit_count = 0
    censored_visit_count = 0
    maximum_centre = 0
    for p in range(1, cutoff + 1, 2):
        for clock, centre, power, alive in source_visits(p, t):
            lo, hi = reciprocal_root_interval(centre, t, scale)
            w = Fraction(9 ** t, 4 ** clock)
            w0 += w
            wlo += w * lo
            whi += w * hi
            visit_count += 1
            maximum_centre = max(maximum_centre, centre)
            if alive:
                b = Fraction(centre ** 2, p ** 2 * power ** 2)
                b0 += b
                blo += b * lo
                bhi += b * hi
                censored_visit_count += 1
    wtail, btail = Fraction(2, 3 * cutoff), Fraction(1, cutoff)
    require(wlo <= whi <= w0, "W comparison failed")
    require(blo <= bhi <= b0, "B comparison failed")
    return {
        "schema": "collatz-moving-endpoint-tilt-enclosure/v1",
        "status": "exact finite-bin enclosure of an infinite source sum; no asymptotic decay claim",
        "bin": t,
        "endpoint_exponent": {"numerator": 1, "denominator": t},
        "source_cutoff": cutoff,
        "root_precision_bits": bits,
        "odd_sources_retained": (cutoff + 1) // 2,
        "actual_bin_visits": visit_count,
        "visits_before_first_one": censored_visit_count,
        "maximum_retained_centre": maximum_centre,
        "W": {"finite_untilted_sum": encode_fraction(w0),
              "finite_tilted_lower": encode_fraction(wlo),
              "finite_tilted_upper": encode_fraction(whi),
              "omitted_original_source_bound": encode_fraction(wtail),
              "complete_lower": encode_fraction(wlo),
              "complete_upper": encode_fraction(whi + wtail)},
        "B": {"finite_untilted_sum": encode_fraction(b0),
              "finite_tilted_lower": encode_fraction(blo),
              "finite_tilted_upper": encode_fraction(bhi),
              "omitted_original_source_bound": encode_fraction(btail),
              "complete_lower": encode_fraction(blo),
              "complete_upper": encode_fraction(bhi + btail)},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bin", type=int, required=True)
    parser.add_argument("--sources", type=int, default=667)
    parser.add_argument("--precision-bits", type=int, default=24)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = certify(args.bin, args.sources, args.precision_bits)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for name in ("W", "B"):
        row = result[name]
        endpoints = []
        for key in ("complete_lower", "complete_upper"):
            q = row[key]
            endpoints.append(float(Fraction(q["numerator"], q["denominator"])))
        print(f"{name}, exponent 1/{args.bin}: [{endpoints[0]:.12g}, {endpoints[1]:.12g}]")
    print("The JSON endpoints are exact rationals; displayed decimals are only summaries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
