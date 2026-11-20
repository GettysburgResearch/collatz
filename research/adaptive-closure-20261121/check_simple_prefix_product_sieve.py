#!/usr/bin/env python3
"""Exact finite checks for SIMPLE_PREFIX_PRODUCT_SIEVE.md, not a proof search."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(n):
    require(isinstance(n, int) and n > 0, "positive ordinary input required")
    return (3 * n + 1) // 2 if n & 1 else n // 2


def odd_map(n):
    require(isinstance(n, int) and n > 0 and n & 1, "positive odd input required")
    n = 3 * n + 1
    return n // (n & -n)


def check_odd_segment(segment):
    require(bool(segment), "nonempty segment required")
    require(all(isinstance(n, int) and n > 0 and n & 1 for n in segment),
            "positive odd segment required")
    require(len(set(segment)) == len(segment), "simple segment required")
    require(all(odd_map(a) == b for a, b in zip(segment, segment[1:])),
            "consecutive odd segment required")
    ordered = sorted(segment)
    for rank, bound in enumerate(ordered, 1):
        require(rank ** 40 <= 4 ** 40 * bound ** 39, "finite count inequality")
    reciprocal_mass = sum((Fraction(1, n) for n in segment), Fraction())
    require(reciprocal_mass ** 40 * min(segment) <= 160 ** 40,
            "finite reciprocal inequality")
    return len(ordered)


def small_segments():
    counts = 0
    checked_thresholds = 0
    for start in range(1, 258, 2):
        segment = []
        seen = set()
        n = start
        while n not in seen and len(segment) < 96:
            seen.add(n)
            segment.append(n)
            n = odd_map(n)
        checked_thresholds += check_odd_segment(segment)
        counts += 1
    rejected = 0
    for segment in ([], [1, 1], [3, 7], [2], [-1]):
        try:
            check_odd_segment(segment)
        except ValueError:
            rejected += 1
        else:
            raise ValueError("negative segment control was accepted")
    return {"segments": counts, "thresholds": checked_thresholds,
            "rejected_controls": rejected}


def check_source(k, label, cap=50000):
    require(k > 0 and k % 4 != 0, "eligible k required")
    X, Y, n = 128 * k + 1, 64 * k + 1, 27 * k + 1
    z = Y
    for _ in range(6):
        z = shortcut(z)
    require(z == n, "six-step lower-arm identity")
    floor = Fraction(5 * X, 8 * 176106)
    require(floor >= 80 ** 40, "large-floor hypothesis")
    require(8 * 176106 * n < 5 * 65536 * X, "antecedent margin")
    z = n
    b = 0
    product = Fraction(1)
    seen = set()
    first_floor = None
    first_crossing = None
    for clock in range(cap + 1):
        require(z * 2 ** clock == n * 3 ** b * product,
                "exact multiplicative identity")
        if first_floor is None and z < floor:
            first_floor = {"clock": clock, "state": str(z)}
        if 2 ** 17 * 3 ** b < 2 ** clock:
            first_crossing = {"clock": clock, "odd_count": b,
                              "state": str(z)}
            require(first_floor is not None, "crossing must force a floor hit")
            require(176106 * int(first_floor["state"]) * 8 < 5 * X,
                    "exact smaller-antecedent margin")
            break
        if z in seen:
            raise ValueError("source repeated before coefficient crossing")
        seen.add(z)
        if z & 1:
            product *= Fraction(3 * z + 1, 3 * z)
            b += 1
        z = shortcut(z)
    require(first_crossing is not None, "finite execution cap exhausted")
    require(product < 2, "product below 2 in these actual examples")
    return {"label": label, "k": str(k), "start": str(n),
            "distinct_input_states": len(seen),
            "first_floor_hit": first_floor,
            "first_coefficient_crossing": first_crossing,
            "correction_product_below_2": True}


def main():
    require(8 * 3125 ** 24 < 3456 ** 24, "source exponent margin")
    require(Fraction(3125, 3456) > Fraction(8, 27), "eta > 2/3")
    require(5 * 65536 * 128 - 8 * 176106 * 27 == 3904144,
            "linear coefficient arithmetic")
    require(5 * 65536 - 8 * 176106 == -1081168,
            "constant coefficient arithmetic")
    require(3904144 - 1081168 == 2822976 > 0, "all-k margin")
    examples = [check_source((2 ** 270 - 1) // 27, "power-of-two lower state")]
    for exponent in (281, 443, 605):
        numerator = 8 * 2 ** exponent - 22
        require(numerator % 243 == 0, "rank-five parameter integrality")
        examples.append(check_source(numerator // 243,
                                     f"rank-five Mersenne exponent {exponent}"))
    report = {
        "status": "finite exact checks passed; no universal closure claimed",
        "source_head": "fd991063721e9c157d318e40bb20131762f7d750",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "small_segment_checks": small_segments(),
        "large_floor_threshold": str(80 ** 40),
        "actual_fixed_source_examples": examples,
        "scope": [
            "All numerical checks use integers or exact rational arithmetic.",
            "The 71-path directed cover is imported, not rechecked here.",
            "The finite source examples do not settle the Mersenne progression.",
            "The uniform segment estimate is justified by the written proof.",
            "No independence is assumed beyond a binary cylinder modulus."
        ]
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
