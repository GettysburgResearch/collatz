#!/usr/bin/env python3
"""Exact recognition of a supplied triadic complementary candidate.

This is a verifier, not a universal candidate constructor. The written
completeness proof uses the pinned finite triadic rigidity theorem. No
unbounded orbit search appears in recognize(). All checks remain enabled
under python -O. Standard library only.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def reduce_triadic(a: int, r: int) -> tuple[int, int]:
    if r < 0:
        raise ValueError("negative denominator exponent")
    if a == 0:
        return 0, 0
    while r and a % 3 == 0:
        a //= 3
        r -= 1
    return a, r


def ordinary_certificate(states: list[int]) -> dict:
    require(states and states[-1] == 1, "missing terminal one")
    for left, right in zip(states, states[1:]):
        require(shortcut(left) == right, "invalid ordinary edge")
    result = {"shortcut_clock": len(states) - 1, "states": states}
    if states[0] % 2:
        exponents = [i for i, value in enumerate(states) if value % 2]
        odd_steps = len(exponents) - 1
        carry = sum(3 ** (odd_steps - 1 - j) * 2 ** exponents[j]
                    for j in range(odd_steps))
        require(3 ** odd_steps * states[0] + carry == 2 ** exponents[-1],
                "output tuple does not satisfy the complete identity")
        result["odd_steps"] = odd_steps
        result["exponents"] = exponents
    return result


def recognize(n: int, a: int, r: int) -> dict:
    """Decide a/3^r = Omega(n), for n>0, and return a hit certificate.

    The negative phase uses at most bit_length(abs(reduced a)) steps.
    Large binary-encoded r is rejected before constructing 3**r.
    """
    if n <= 0:
        raise ValueError("the ordinary input must be positive")
    a, r = reduce_triadic(a, r)
    A = abs(a)
    E = A.bit_length()
    base = {"n": n, "reduced_a": a, "reduced_r": r,
            "negative_step_budget": E, "negative_steps": 0}

    def reject(reason: str, count: int = 0) -> dict:
        return dict(base, accepted=False, reason=reason, negative_steps=count)

    if a >= 0:
        terminals = {(1, 2, 0): [1], (2, 1, 0): [2, 1],
                     (4, 1, 1): [4, 2, 1]}
        states = terminals.get((n, a, r))
        if states is None:
            return reject("nonnegative_candidate_classification")
        return dict(base, accepted=True, reason="exceptional_positive_pair",
                    certificate=ordinary_certificate(states))

    # A successful reduced negative code has r>=2, r<=E+1, and
    # 3**r <= A+2**(r+1). The first filter avoids a huge power construction.
    if r < 2 or r > E + 1:
        return reject("exponent_height")
    q = 3 ** r
    if q > A + 2 ** (r + 1):
        return reject("sharp_height")

    x, w, exponent = n, a, r
    states = [n]
    for count in range(1, E + 1):
        if w >= 0 or exponent == 0:
            return reject("negative_domain_exit", count - 1)
        if x % 2 + w % 2 != 1:
            return reject("parity_mismatch", count - 1)
        previous_abs = -w
        if x % 2:
            require(w % 2 == 0, "nonintegral even dual branch")
            x = (3 * x + 1) // 2
            w //= 2
        else:
            require(q % 3 == 0, "denominator exponent mismatch")
            q //= 3
            numerator = w + q
            require(numerator % 2 == 0, "nonintegral odd dual branch")
            w = numerator // 2
            exponent -= 1
            x //= 2
        states.append(x)
        if w >= 0:
            if (x, w, exponent) != (4, 1, 1):
                return reject("wrong_first_crossing", count)
            states.extend([2, 1])
            result = dict(base, accepted=True, reason="exact_first_crossing",
                          negative_steps=count,
                          certificate=ordinary_certificate(states))
            require(result["certificate"]["shortcut_clock"] <= E + 2,
                    "binary-length clock bound failed")
            return result
        require(2 * (-w) <= previous_abs, "negative halving invariant failed")
        if exponent == 0:
            return reject("negative_integral_endpoint", count)
    raise RuntimeError("negative phase exhausted its proved binary-length budget")


def supplied_fixture(n: int) -> tuple[int, int, int]:
    """Finite independent controls only; never called by recognize()."""
    x, states = n, []
    for _ in range(10000):
        if x == 1:
            break
        states.append(x)
        x = shortcut(x)
    else:
        raise RuntimeError("fixture control exceeded its stated cutoff")
    dual = Fraction(2)
    for x in reversed(states):
        dual = 2 * dual if x % 2 else (2 * dual - 1) / 3
    denominator, r = dual.denominator, 0
    while denominator % 3 == 0:
        denominator //= 3
        r += 1
    require(denominator == 1, "fixture dual is not triadic")
    return dual.numerator, r, len(states)


def self_test() -> dict:
    fixtures = [1, 2, 3, 4, 5, 7, 8, 16, 27, 65, 129, 193, 257, 513,
                1023, 6171]
    records = []
    wrong = 0
    for n in fixtures:
        a, r, clock = supplied_fixture(n)
        result = recognize(n, a, r)
        require(result["accepted"], "true fixture rejected")
        require(result["certificate"]["shortcut_clock"] == clock,
                "first-hit clock differs from independent fixture")
        padded = recognize(n, 27 * a, r + 3)
        require(padded == result, "unreduced representation changed the result")
        for aa, rr in [(a + 2, r), (a - 2, r), (a, r + 1), (0, r)]:
            require(not recognize(n, aa, rr)["accepted"], "wrong candidate accepted")
            wrong += 1
        records.append({"n": n, "a": a, "r": r, "clock": clock,
                        "budget": result["negative_step_budget"],
                        "negative_steps": result["negative_steps"]})
    for n in (16, 24):
        wrong_cross = recognize(n, -1, 2)
        require(not wrong_cross["accepted"] and
                wrong_cross["reason"] == "wrong_first_crossing",
                "wrong sign crossing was treated as success")
    huge = recognize(8, -1, 10 ** 100)
    require(not huge["accepted"] and huge["reason"] == "exponent_height",
            "giant binary exponent was not rejected before exponentiation")
    for r in range(2, 18):
        n = 2 ** (r + 1)
        a = 2 ** (r + 1) - 3 ** r
        require(recognize(n, a, r)["accepted"], "sharp all-even code rejected")
    digest = hashlib.sha256(json.dumps(records, sort_keys=True,
                                      separators=(",", ":")).encode()).hexdigest()
    return {"status": "PASS", "scope": "finite new-recognizer controls only",
            "true_fixtures": len(fixtures), "unreduced_fixtures": len(fixtures),
            "wrong_candidates": wrong, "wrong_crossings": 2,
            "giant_exponent_controls": 1, "sharp_equality_family_controls": 16,
            "fixture_sha256": digest, "fixtures": records}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--n", type=int)
    parser.add_argument("--a", type=int)
    parser.add_argument("--r", type=int)
    args = parser.parse_args()
    if args.self_test:
        result = self_test()
    elif None not in (args.n, args.a, args.r):
        result = recognize(args.n, args.a, args.r)
    else:
        parser.error("provide --self-test or all of --n, --a, --r")
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
