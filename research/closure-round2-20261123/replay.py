#!/usr/bin/env python3
"""Bounded exact controls for the three closing attempts.

The cycle controls exercise cyclic cuts and the complete numerical modulus.
The pressure controls transport one finite source function through actual odd
orbits, retaining collisions and repeated visits to a periodic root. They do
not truncate the reference measure at a moving endpoint height. No finite
control here asserts an escaping component or settles the Collatz conjecture.
All checks remain active with Python optimization enabled.
"""

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def carry(word):
    result = 0
    for i, bit in enumerate(word):
        if bit:
            result = 3 * result + 2**i
    return result


def neighbors(word):
    answer = set()
    for i in range(len(word)):
        j = (i + 1) % len(word)
        if word[i] != word[j]:
            other = list(word)
            other[i], other[j] = other[j], other[i]
            answer.add(tuple(other))
    return answer


def cycle_controls(max_length=12):
    counts = defaultdict(int)
    zero_fibres = defaultdict(list)
    nontrivial_gcd_examples = []
    for length in range(1, max_length + 1):
        for word in product((0, 1), repeat=length):
            weight = sum(word)
            denominator = 2**length - 3**weight
            if weight == 0 or denominator <= 0:
                continue
            counts["positive_complete_words"] += 1
            require(gcd(denominator, 6) == 1, "denominator is not a 2,3-unit")
            numerator = carry(word)
            if numerator % denominator == 0:
                zero_fibres[length, weight].append(word)
            for right in range(length):
                if word[right] == 0:
                    continue
                left = right - 1
                while left >= 0 and word[left] == 0:
                    h = right - left
                    other = word[:left] + (1,) + (0,) * h + word[right + 1:]
                    other_carry = carry(other)
                    factor = 2**left * 3**sum(word[right + 1:])
                    require(numerator - other_carry == factor * (2**h - 1),
                            "complete moving-letter identity failed")
                    counts["moving_letter_identities"] += 1
                    if numerator % denominator == 0:
                        require(gcd(denominator, other_carry)
                                == gcd(denominator, 2**h - 1),
                                "complete gcd transport failed")
                        counts["zero_residue_gcd_transports"] += 1
                    if h == 1:
                        g1, g2 = gcd(denominator, numerator), gcd(denominator, other_carry)
                        require(gcd(g1, g2) == 1 and denominator % (g1 * g2) == 0,
                                "adjacent cancellation factors are not disjoint")
                        counts["adjacent_disjoint_factor_checks"] += 1
                        if g1 > 1 and g2 > 1 and len(nontrivial_gcd_examples) < 3:
                            nontrivial_gcd_examples.append({
                                "word": "".join(map(str, word)), "cut": left,
                                "D": denominator, "gcds": [g1, g2],
                            })
                    left -= 1
            if length >= 5 and denominator > 2 * 3**(length // 2):
                seen = set()
                odd_count = 0
                for i, bit in enumerate(word):
                    cut = (2**i * pow(pow(3, odd_count, denominator), -1, denominator)) % denominator
                    require(cut not in seen and (-cut) % denominator not in seen,
                            "cyclic cut units collided up to sign")
                    seen.add(cut)
                    odd_count += bit
                counts["cyclic_cut_separation_checks"] += 1

    for (length, weight), words in zero_fibres.items():
        denominator = 2**length - 3**weight
        if length >= 5 and denominator > 2 * 3**(length // 2):
            occupied = set()
            for word in words:
                hood = neighbors(word) | {word}
                require(not occupied.intersection(hood), "closed zero neighborhoods overlap")
                occupied.update(hood)
            counts["closed_neighborhood_fibres"] += 1
        for h in range(1, length + 1):
            if denominator <= 3**h:
                continue
            # Check every cyclic placement, including windows crossing the origin.
            for start in range(length):
                outside = [i for i in range(length)
                           if (i - start) % length >= h]
                keys = [tuple(word[i] for i in outside) for word in words]
                require(len(set(keys)) == len(keys), "complement-window injection failed")
                counts["cyclic_window_injections"] += 1
    return {"maximum_length": max_length, "counts": dict(counts),
            "nontrivial_adjacent_gcd_examples": nontrivial_gcd_examples,
            "scope": "bounded exact controls; all-word claims use the written and Lean proofs"}


def odd_step(n):
    require(n > 0 and n % 2 == 1 and n % 3 != 0, "not an ordinary odd unit")
    value = 3 * n + 1
    gap = 0
    while value % 2 == 0:
        value //= 2
        gap += 1
    require(gap > 0 and value % 3 != 0, "invalid ordinary odd image")
    return value, gap


def correction(n):
    return Fraction(3 * n, 3 * n + 1)


def rational_record(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def pressure_controls(depth=24):
    # A finite source function, not a truncated endpoint measure.
    seed = {1: Fraction(2), 5: Fraction(3, 2), 7: Fraction(4, 3),
            13: Fraction(5, 4), 19: Fraction(6, 5), 23: Fraction(7, 6),
            31: Fraction(8, 7), 37: Fraction(9, 8), 91: Fraction(10, 9)}
    current = dict(seed)
    reference = sum((f / n**2 for n, f in seed.items()), Fraction(0))
    loss = Fraction(0)
    merged_terms = 0
    discarded_periodic_repeat = Fraction(0)
    for clock in range(depth):
        for n, value in current.items():
            contribution = value * (1 - correction(n)**2) / n**2
            loss += contribution
            if n == 1 and clock > 0:
                discarded_periodic_repeat += contribution
        next_values = defaultdict(Fraction)
        for n, value in current.items():
            q, gap = odd_step(n)
            if q in next_values:
                merged_terms += 1
            # Exact inverse-branch coefficient in P_2, transported forward.
            next_values[q] += value * Fraction(3, 2**gap)**2
        current = dict(next_values)
    residual_from_endpoints = sum((f / n**2 for n, f in current.items()), Fraction(0))
    residual_from_sources = Fraction(0)
    for n, f in seed.items():
        q, lam = n, Fraction(1)
        for _ in range(depth):
            lam *= correction(q)
            q, _ = odd_step(q)
        residual_from_sources += f * lam**2 / n**2
    require(residual_from_sources == residual_from_endpoints, "original-source identity failed")
    require(loss + residual_from_sources == reference, "finite loss telescope failed")
    require(merged_terms > 0 and discarded_periodic_repeat > 0,
            "controls did not exercise collisions and periodic repetition")
    require(loss - discarded_periodic_repeat + residual_from_sources != reference,
            "discarding repeated periodic visits was not detected")
    return {"parameter_s": 2, "depth": depth, "source_count": len(seed),
            "endpoint_merges_retained": merged_terms,
            "reference_mass": rational_record(reference),
            "loss": rational_record(loss),
            "residual": rational_record(residual_from_sources),
            "periodic_visit_deletion_rejected": True,
            "scope": "exact finite identity; no claim that the infinite residual vanishes"}


def source_controls():
    q, clock, records = 7, 0, []
    for h in range(1, 5):
        q, gap = odd_step(q)
        clock += gap
        records.append({"odd_depth": h, "endpoint": q, "total_gap": clock,
                        "forward_coefficient_above_one": 3**h > 2**clock})
    require(all(row["forward_coefficient_above_one"] for row in records[:3])
            and not records[-1]["forward_coefficient_above_one"],
            "finite-prefix scope control failed")
    incoming_23 = (2 * 23 - 1) // 3
    require(incoming_23 == 15 and incoming_23 % 3 == 0,
            "unit-domain residue control failed")
    return {"finite_source": 7, "prefixes": records,
            "root_23_gap_one_source": incoming_23,
            "root_23_source_is_excluded_nonunit": True,
            "scope": "these convergent controls are not hypothetical infinite pressure maxima"}


def main():
    print(json.dumps({
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "cycles": cycle_controls(), "pressure": pressure_controls(),
        "source": source_controls(),
    }, indent=2))


if __name__ == "__main__":
    main()
