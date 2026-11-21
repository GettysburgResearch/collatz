"""Exact controls for the signed-debt normalization attempt.

This is a route experiment, not a convergence checker or a proof.  Its fixed
controls exhibit the obstruction at a completed carry block, not just at an
intermediate expanding Collatz step.  All arithmetic is integral or Fraction.
"""

from fractions import Fraction
import json


def odd_step(n: int) -> tuple[int, int]:
    assert n > 0 and n % 2 == 1
    m = 3 * n + 1
    a = 0
    while m % 2 == 0:
        m //= 2
        a += 1
    return a, m


def advance(x, y, coefficient, debt):
    a, xx = odd_step(x)
    b, yy = odd_step(y)
    kk = coefficient * Fraction(2**a, 2**b)
    cc = (3 * debt + coefficient - 1) / 2**b
    assert yy == kk * xx - cc
    return xx, yy, kk, cc, a, b


def state(x, y, coefficient, debt, **extra):
    return {
        "source": x,
        "target": y,
        "coefficient": str(coefficient),
        "debt": str(debt),
        **extra,
    }


def first_carry_control(start: int):
    x, y = start, 5 * start
    coefficient, debt = Fraction(5), Fraction(0)
    trace = [state(x, y, coefficient, debt)]
    for _ in range(100):
        if x == 1:
            break
        x, y, coefficient, debt, a, b = advance(x, y, coefficient, debt)
        trace.append(state(x, y, coefficient, debt, source_exp=a, target_exp=b))
    else:
        raise RuntimeError("Fixed control unexpectedly exceeded its source budget")
    assert x == 1 and y > 1 and 0 <= debt < coefficient / 2
    before_coefficient, before_debt = coefficient, debt
    source_end = state(x, y, coefficient, debt)
    padding = []
    for _ in range(5):
        x, y, coefficient, debt, a, b = advance(x, y, coefficient, debt)
        assert a == 2 and x == 1
        padding.append(state(x, y, coefficient, debt, source_exp=a, target_exp=b))
        if y == 1:
            return {"start": start, "source_trace": trace,
                    "padding": padding, "target_reached_one": True}
        if 2 * debt >= coefficient:
            coefficient /= 2
            debt -= coefficient
            assert y == coefficient - debt and 0 <= debt < coefficient / 2
            return {
                "start": start,
                "source_trace": trace,
                "source_end": source_end,
                "padding": padding,
                "after_carry": state(x, y, coefficient, debt),
                "coefficient_growth": str(coefficient / before_coefficient),
                "debt_change": str(debt - before_debt),
            }
    raise AssertionError("The five-step carry estimate failed")


def valuation_regeneration(h: int):
    assert h >= 3 and h % 2 == 1
    n = (2 ** (h + 2) - 5) // 3
    a, q = odd_step(n)
    assert 3 * n + 1 == 4 * (2**h - 1)
    assert a == 2 and q == 2**h - 1
    assert (n + 1) % 4 == 2 and q + 1 == 2**h
    return {"h": h, "source": n, "target": q, "exponent": a,
            "source_v2_plus_one": 1, "target_v2_plus_one": h}


if __name__ == "__main__":
    print(json.dumps({
        "carry_controls": [first_carry_control(n) for n in (3, 5, 11)],
        "valuation_controls": [valuation_regeneration(h) for h in (3, 5, 7, 9)],
    }, indent=2))
