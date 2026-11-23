#!/usr/bin/env python3
"""Exact finite certificates for proposed rational Collatz parity duals.

The all-input termination proof is RATIONAL_DUAL_CERTIFICATE.md,
Sections 3--6. This is a reproduction program, not a Collatz proof.
"""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from pathlib import Path


def step(x: int) -> int:
    assert x > 0
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def numerator_step(w: int, d: int) -> int:
    assert d > 0 and d % 2 == 1
    return w // 2 if w % 2 == 0 else (3 * w + d) // 2


def valuation2(z: int) -> int:
    assert z != 0
    z = abs(z)
    return (z & -z).bit_length() - 1


def decide_dual(n: int, a: int, d: int) -> dict:
    """Return a literal cycle or the first actual parity failure.

    No step limit, assumption of Collatz convergence, floating-point
    threshold, or oracle for an infinite parity itinerary is used.
    """
    assert n > 0 and d > 0 and d % 2 == 1
    x, w, j = n, a, 0
    small: dict[int, tuple[int, int]] = {}
    history: list[tuple[int, int]] = []
    local = Counter()

    def rejection_at(deadline: int, reason: str) -> dict:
        nonlocal x, w, j
        # Every earlier state has passed. Include the predicted terminal
        # state in the checks; the result is a concrete finite witness.
        while j < deadline:
            assert x % 2 != w % 2
            history.append((x, w))
            x, w = step(x), numerator_step(w, d)
            j += 1
        assert x % 2 == w % 2
        return {
            "accepted": False, "reason": reason,
            "failure_index": j, "failure_state": [x, w],
            "local_inequalities": dict(sorted(local.items())),
        }

    while True:
        if x % 2 == w % 2:
            return rejection_at(j, "observed_parity_failure")

        if x == 1:
            if w == 2 * d:
                assert step(x) == 2
                assert numerator_step(w, d) == d
                assert numerator_step(d, d) == 2 * d
                return {
                    "accepted": True, "reason": "standard_pair_cycle",
                    "cycle_entry": j, "period": 2,
                    "cycle_state": [x, w],
                    "local_inequalities": dict(sorted(local.items())),
                }
            return rejection_at(
                j + valuation2(w - 2 * d), "wrong_dual_at_one"
            )

        if w == 0:
            return rejection_at(
                j + valuation2(x + 1), "zero_numerator"
            )

        if 1 <= w <= d:
            if w in small:
                i, old_x = small[w]
                if x == old_x:
                    # Check the full literal pair cycle and every parity
                    # test in it, rather than only its endpoint identity.
                    cx, cw = x, w
                    for _ in range(j - i):
                        assert cx % 2 != cw % 2
                        cx, cw = step(cx), numerator_step(cw, d)
                    assert (cx, cw) == (x, w)
                    return {
                        "accepted": True, "reason": "paired_cycle",
                        "cycle_entry": i, "period": j - i,
                        "cycle_state": [x, w],
                        "local_inequalities": dict(sorted(local.items())),
                    }
                return rejection_at(
                    j + valuation2(x - old_x),
                    "repeated_numerator_unequal_integer",
                )
            small[w] = (j, x)
            assert len(small) <= d

        nx, nw = step(x), numerator_step(w, d)
        product, next_product = x * abs(w), nx * abs(nw)
        assert x >= 2
        if w < 0:
            if nw < 0:
                assert 6 * next_product <= 5 * product
                local["negative_contraction"] += 1
            elif nw > 0:
                assert 4 * next_product <= d * product
                local["negative_to_positive_crossing"] += 1
            else:
                local["negative_to_zero_crossing"] += 1
        elif w > d:
            assert (2 * d + 4) * next_product <= (2 * d + 3) * product
            local["positive_large_contraction"] += 1
        else:
            assert 4 * next_product <= (d + 3) * product
            local["positive_small_expansion"] += 1
        history.append((x, w))
        x, w, j = nx, nw, j + 1


def dual_from_explicit_termination(n: int) -> Fraction:
    """Examples only: reverse a directly checked terminating trajectory."""
    path, x = [], n
    seen = set()
    while x != 1:
        assert x not in seen and len(path) < 10000
        seen.add(x)
        path.append(x)
        x = step(x)
    y = Fraction(2)
    for x in reversed(path):
        y = 2 * y if x % 2 else (2 * y - 1) / 3
    assert y.denominator % 2 == 1
    return y


def main() -> None:
    totals = Counter()
    inequalities = Counter()
    examples = []

    def record(n: int, a: int, d: int, result: dict) -> None:
        totals["cases"] += 1
        totals["accepted" if result["accepted"] else "rejected"] += 1
        totals[result["reason"]] += 1
        inequalities.update(result["local_inequalities"])

    # Exact rational duals of finitely and explicitly terminated sources.
    # This only creates test examples; it is not an input to the decider.
    for n in range(1, 101):
        y = dual_from_explicit_termination(n)
        a, d = y.numerator, y.denominator
        result = decide_dual(n, a, d)
        assert result["accepted"]
        record(n, a, d, result)
        if n in (1, 2, 3, 4, 5, 7, 8, 27):
            examples.append({"n": n, "a": a, "d": d, **result})

        # Numerator difference 2^k*d has exact 2-adic valuation k.
        # These candidates match k parity bits and fail at state k.
        k = 1 + n % 11
        changed = a + (2 ** k) * d
        rejected = decide_dual(n, changed, d)
        assert not rejected["accepted"]
        assert rejected["failure_index"] == k
        record(n, changed, d, rejected)

    # Signed grids exercise all branches, including unreduced denominators.
    for n in range(1, 21):
        for d in (1, 3, 5, 9, 15):
            for a in range(-12, 13):
                result = decide_dual(n, a, d)
                record(n, a, d, result)

    # A literal -1/3 -> 0 crossing, followed through the zero-tail failure.
    zero_case = decide_dual(6, -5, 15)
    assert not zero_case["accepted"]
    assert zero_case["reason"] == "zero_numerator"
    assert zero_case["failure_index"] == 3
    examples.append({"n": 6, "a": -5, "d": 15, **zero_case})

    output = {
        "status": "all exact assertions passed",
        "scope": "finite implementation checks, not a Collatz proof",
        "generated_true_duals": 100,
        "prescribed_prefix_rejections": 100,
        "signed_grid_cases": 2500,
        "additional_named_zero_case": 1,
        "totals_excluding_additional_named_zero_case": dict(sorted(totals.items())),
        "verified_local_inequalities": dict(sorted(inequalities.items())),
        "examples": examples,
    }
    target = Path(__file__).with_name("rational-dual-check.json")
    target.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({
        "status": output["status"],
        "cases": totals["cases"] + 1,
        "result_file": str(target),
        "local_inequalities": output["verified_local_inequalities"],
    }, indent=2))


if __name__ == "__main__":
    main()
