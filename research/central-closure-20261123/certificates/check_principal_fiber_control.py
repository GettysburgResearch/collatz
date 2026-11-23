#!/usr/bin/env python3
"""Exact sample checks for the proved unbounded principal-fibre control.

The full family proof, including polynomial coprimality, is in
PRINCIPAL_FIBER_CONTROL.md. This script does not replace that proof.
"""

from fractions import Fraction
from math import gcd
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def correction(word):
    ds = [i for i, bit in enumerate(word) if bit]
    p = len(ds)
    return sum(2**d*3**(p-1-i) for i, d in enumerate(ds))


def check(g):
    require(isinstance(g, int) and g >= 4 and g % 5 == 4, "g must be 4 mod5 and >=4")
    word = (0, 1, 1, 1, 0) + (1, 1, 1, 0, 0)*(g-1)
    A, p = len(word), sum(word)
    require((A, p) == (5*g, 3*g), "word counts")
    require(all(word != word[k:]+word[:k] for k in range(1, A)), "primitivity")
    D = 32**g-27**g
    C = correction(word)
    require(D % 5 == 0 and D % 25 != 0, "exact denominator 5-valuation")
    require(C == 19*(D//5+27**(g-1)), "numerator formula")
    require(C % 5 == 0, "distinguished principal-fibre absorption")
    x = Fraction(C, D)
    start = x
    states = []
    for bit in word:
        require(x.denominator % 2 == 1, "rational odd denominator")
        require(x.numerator % 2 == bit, "actual branch parity")
        require(x > Fraction(19, 10), "uniform cyclic lower floor")
        states.append(x)
        x = (3*x+1)/2 if bit else x/2
    require(x == start, "closure")
    require(len(set(states)) == A, "least orbit period")
    if g == 4:
        require(4 < start < 5, "first member nonintegrality")
    else:
        require(Fraction(19, 5) < start < 4, "tail member nonintegrality")
    require(C % D != 0, "remaining denominator obstruction")
    return {
        "g": g,
        "A": A,
        "p": p,
        "D": str(D),
        "C": str(C),
        "minimum": str(min(states)),
        "actual_gcd": str(gcd(C, D)),
        "principal_factor_absorbed": 5,
        "polynomial_gcd": "1 (analytic root proof in note)",
    }


def run():
    require(32**9 > 122*27**8, "uniform tail comparison")
    cases = [check(g) for g in (4, 9, 14, 29, 49, 104)]
    # Invalid input rejection must survive Python's -O flag.
    rejected = 0
    for bad in (0, 3, 5, -1):
        try:
            check(bad)
        except ValueError:
            rejected += 1
    require(rejected == 4, "malformed family parameters not rejected")
    return {"status": "PASS", "scope": "finite controls for an independently proved infinite family", "cases": cases, "invalid_parameters_rejected": rejected}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
