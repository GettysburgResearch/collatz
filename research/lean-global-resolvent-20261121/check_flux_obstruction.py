#!/usr/bin/env python3
"""Replay the one q=20 finite witness in FLUX_ATTEMPT.md, using exact integers.

The all-source tail 1/(3*N**3) is justified analytically in the note.
This program does not estimate an asymptotic loss rate.
"""
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def step(n):
    y = 3 * n + 1
    return y // (y & -y)


def main():
    bound = 512
    states = {n: n for n in range(1, bound + 1, 2)}
    for _ in range(20):
        states = {n: step(x) for n, x in states.items()}
    following = {n: step(x) for n, x in states.items()}
    hits = [n for n, x in states.items() if x != 1 and following[n] == 1]
    require(hits == [377], "wrong complete finite first-hit set")
    require((states[27], following[27]) == (377, 283), "wrong source 27")
    require((states[31], following[31]) == (425, 319), "wrong source 31")
    require((states[377], following[377]) == (5, 1), "wrong source 377")
    flux_upper = Fraction(1, 377**4) + Fraction(1, 3 * bound**3)
    mass_lower = Fraction(1, 27**4) + Fraction(1, 31**4)
    margin = mass_lower - 1000 * flux_upper
    require(margin > 0, "claimed 1/1000 flux obstruction failed")
    print(json.dumps({
        "q": 20,
        "all_positive_odd_sources_through": bound,
        "first_hits_at_21": hits,
        "source_27_values_at_20_21": [states[27], following[27]],
        "source_31_values_at_20_21": [states[31], following[31]],
        "tail_envelope": str(Fraction(1, 3 * bound**3)),
        "positive_margin": str(margin),
        "claim": "F_20 < A_20 / 1000",
        "scope": "finite exact witness plus the analytic all-source tail in the note",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
