#!/usr/bin/env python3
"""Independent arithmetic review of the single carry-family selector obstruction.

All file inputs are colocated. The output is complete deterministic JSON.
The all-parameter proof is reviewed separately; no fivefold obstruction
target is simulated or asserted to be a counterexample.
"""

from pathlib import Path
from math import comb
import hashlib
import json


HERE = Path(__file__).resolve().parent
ENTRY = (2, 1, 1, 1, 2, 1, 7)
TARGET_ENTRY = (3, 6, 1, 2, 1, 1, 1)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def valuation(n, prime):
    need(n != 0, "valuation of zero")
    n = abs(n)
    if prime == 2:
        return (n & -n).bit_length() - 1
    count = 0
    while n % prime == 0:
        n //= prime
        count += 1
    return count


def words(r, b):
    return ENTRY + (1,) * r + (3, b), TARGET_ENTRY + (1,) * r + (4, b - 1)


def correction(word):
    constant, clock = 0, 0
    for letter in word:
        constant = 3 * constant + (1 << clock)
        clock += letter
    return constant, clock


def replay(n, word, first_hit=False):
    for letter in word:
        need(n > 0 and n % 2, "invalid positive odd state")
        if first_hit:
            need(n > 1, "source hit one before its declared terminal step")
        numerator = 3 * n + 1
        need(valuation(numerator, 2) == letter, "wrong actual exponent")
        n = numerator >> letter
    if first_hit:
        need(n == 1, "source certificate did not finish")
    return n


def finite_control_certificate(n):
    current, letters = n, []
    while current != 1:
        need(len(letters) < 10000, "finite positive control exceeded certificate cap")
        a = valuation(3 * current + 1, 2)
        current = (3 * current + 1) >> a
        letters.append(a)
    replay(n, letters, first_hit=True)
    return tuple(letters)


def finite_obstruction_decision(q):
    """Every contracting inverse is inside this IC2-proved finite range.

    Retains algebraically integral but noncontracting candidates as controls,
    rather than rejecting them before checking their full numerator.
    """
    max_r = (81 * q + 1350).bit_length() - 17
    possible_valuations = 0
    positive_integral = 0
    min_b_minus_r = None
    numerator = (q << 4) - 1  # b=2
    for b in range(2, max_r):
        order = valuation(numerator, 3)
        r = order - 5
        if 0 <= r <= max_r:
            possible_valuations += 1
            need(b >= r, "obstruction allowed a valuation pair with b<r")
            min_b_minus_r = b - r if min_b_minus_r is None else min(min_b_minus_r, b - r)
            d = numerator // 3 ** order
            x_numerator = (d << (r + 16)) - 1351
            if x_numerator % 81 == 0:
                x = x_numerator // 81
                if x > 0:
                    positive_integral += 1
                    need(x > q, "a positive integral contracting inverse survived")
                    source, target = words(r, b)
                    need(replay(x, source) == q and replay(5 * x, target) == 5 * q,
                         "integral noncontracting candidate failed its ordinary words")
        numerator = 2 * numerator + 1
    return {"maximum_r": max_r, "b_values_examined": max(0, max_r - 2),
            "valuation_compatible_pairs": possible_valuations,
            "positive_integral_noncontracting_controls": positive_integral,
            "minimum_b_minus_r": min_b_minus_r, "contracting_returns": 0,
            "source_unit_guard_imposed": False}


def positive_return(r, b):
    # Prescribe x=1 mod3 in the complete numerator, rather than trial
    # lifting the source unit condition after dividing.
    den = 3 ** (r + 9)
    mod = 3 * den
    constant = 1351 * 3 ** (r + 5) + 2 ** (r + 16)
    clock = r + b + 18
    q = (constant + den) * pow(2, -clock, mod) % mod
    if q % 2 == 0:
        q += mod
    if q < 100:
        q += 2 * mod
    numerator = (q << clock) - constant
    need(numerator % den == 0, "constructed positive-control source is nonintegral")
    x = numerator // den
    need(0 < x < q and x % 2 and x % 3 == 1 and q % 2 and q % 3,
         "positive-control guards failed")
    source, target = words(r, b)
    q_word = finite_control_certificate(q)
    replay(x, source + q_word, first_hit=True)
    need(replay(x, source) == q and replay(5 * x, target) == 5 * q,
         "paired positive-return words failed")
    return {"r": r, "b": b, "q": q, "x": x,
            "supplied_q_rank": len(q_word),
            "source_certificate_rank": len(source) + len(q_word),
            "source_unit": True, "strict_height_guard": True,
            "both_ordinary_arms_verified": True}


def main():
    coefficient = 5 * 2 ** 18 - 5 * 3 ** 9 - 1351 * 3 ** 5 - 2 ** 16
    need(coefficient == 818476 > 0, "incorrect b>=r lower-bound coefficient")
    need(2 ** 18 > 3 ** 9 and 1351 % 3 == 1, "exact valuation premise failed")
    need(1324 < 10 * 2 ** (3 ** 2), "all-H binary cutoff base failed")
    need(3 ** 4 - 2 > 0 and 2 * 3 ** 4 - 1 > 0,
         "low-precision contradiction induction failed")
    need(3 ** 3 - 2 > 4 - 4 and 2 * 3 ** 3 - 1 > 0,
         "high-precision contradiction induction failed")
    # Coefficients in z of 2(z-1)^4-(z-1)-3, independent of substitutions.
    polynomial = [2 * comb(4, j) * (-1) ** (4 - j) for j in range(5)]
    polynomial[0] -= 2
    polynomial[1] -= 1
    need(polynomial == [0, -9, 12, -8, 2], "forced valuation factorization failed")
    need(min(1 + 4, 2 * 4, 3 * 4) > 2,
         "higher bracket terms could cancel its exact valuation two")
    formula_controls = 0
    for r in (0, 1, 2, 6, 13, 30):
        for b in (2, 5, 11):
            source, target = words(r, b)
            constant, clock = correction(source)
            target_constant, target_clock = correction(target)
            need(constant == 1351 * 3 ** (r + 5) + 2 ** (r + 16), "source correction failed")
            need(target_constant == 5 * constant and clock == target_clock == r + b + 18,
                 "homogeneous carry interface failed")
            formula_controls += 1
    family = []
    for h in range(4, 10):
        length = 3 ** h
        q = (2 ** (length + 1) - 1) // 3
        need(q > 1 and q % 2 and q % 3 == 2, "rank-one endpoint domain failed")
        replay(q, (length + 1,), first_hit=True)
        need(valuation(q + 1, 3) == h, "rank-one endpoint precision failed")
        m = 3 ** (h - 1)
        t = 1 << m
        z = t + 1
        bracket = -9 + 12 * z - 8 * z * z + 2 * z ** 3
        need(valuation(z, 3) == h and valuation(bracket, 3) == 2,
             "exact high-precision bracket valuation failed")
        need(3 * (t * q - 1) == z * bracket and valuation(t * q - 1, 3) == h + 1,
             "forced r valuation failed")
        need(81 * q + 1351 == 54 * 2 ** length + 1324 < 2 ** (length + 6),
             "exact endpoint height cutoff failed")
        need(m - 2 > h - 4, "forced b did not contradict b<r")
        # Validate the order and half-order congruences without assuming
        # the given finite endpoint decision succeeds.
        modulus = 3 ** h
        need(pow(2, m, modulus) == modulus - 1 and pow(2, 2 * m, modulus) == 1,
             "half-order residue failed")
        need(pow(2, 2 * (m // 3), modulus) != 1, "order has an extra factor of three")
        family.append({"H": h, "q_bits": q.bit_length(), "first_hit_exponent": length + 1,
                       "v3_q_plus_one": h, "forced_b": m - 2, "forced_r": h - 4,
                       "v3_bracket": 2, "finite_complete_decision": finite_obstruction_decision(q)})
    files = ("INVERSE_CARRY_SELECTOR.md", "check_inverse_carry_selector.py")
    report = {"status": "PASS",
              "scope": "No single completed PR170 carry inverse contracts at q_H, H>=4; no fivefold target nonconvergence assertion",
              "input_sha256": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                               for name in files},
              "height_lemma_coefficient": coefficient,
              "factorization_coefficients_in_z": polynomial,
              "source_formula_controls": formula_controls,
              "obstruction_endpoint_controls": family,
              "independent_positive_returns": [positive_return(r, b) for r, b in ((11, 2), (13, 3), (16, 4))],
              "proof_quantifiers": "all H>=4, all r>=0, all b>=2 via the two-case valuation proof",
              "bounded_decisions_used_as_universal_proof": False,
              "fivefold_targets_asserted_nonconvergent": False,
              "full_collatz_proved": False}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
