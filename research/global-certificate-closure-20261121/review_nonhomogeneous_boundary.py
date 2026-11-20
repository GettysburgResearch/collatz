#!/usr/bin/env python3
"""Independent review replay for NONHOMOGENEOUS_BOUNDARY.md.

Builds source words backwards and solves the finite exponent congruences
by direct cyclic enumeration, independently of the author's lifting code.
It never infers convergence of an unknown multiplied target.
"""

from fractions import Fraction
from pathlib import Path
import hashlib
import json


HERE = Path(__file__).resolve().parent
SOURCE = (HERE if (HERE / "NONHOMOGENEOUS_BOUNDARY.md").exists()
          else HERE.parent / "collatz-global" / "research" / "global-certificate-closure-20261121")


def need(ok, why):
    if not ok:
        raise ValueError(why)


def v2(n):
    need(n > 0, "valuation argument is not positive")
    return (n & -n).bit_length() - 1


def reverse_word(q, letters):
    need(q > 0 and q % 2, "endpoint is not positive odd")
    state = q
    states = [q]
    for gap in reversed(letters):
        numerator = 2 ** gap * state - 1
        need(numerator % 3 == 0, "nonintegral inverse step")
        state = numerator // 3
        need(state > 1 and state % 2, "inverse state is not positive odd preterminal")
        states.append(state)
    states.reverse()
    need(all(v2(3 * x + 1) == a and (3 * x + 1) // 2 ** a == y
             for x, a, y in zip(states, letters, states[1:])),
         "inverse construction failed exact forward replay")
    return states[0], states


def direct_exponent(p, c):
    modulus = 3 ** (p + 1)
    period = 2 * 3 ** p
    goal = (1 + c * 3 ** p) % modulus
    value = 5
    hits = []
    for s in range(period):
        if value == goal:
            hits.append(s)
        value = 2 * value % modulus
    need(len(hits) == 1 and hits[0] % 2 == 1, "exponent class is not unique odd")
    need(value == 5, "declared exponent period failed")
    return hits[0], period


def verify_target_prefix(m, b, q, x):
    p, h = m + 2, 3 * m + 4
    numerator = 5 * 2 ** (b - 3) * q - 1
    need(numerator % 3 ** p == 0, "target coefficient is nonintegral")
    k = numerator // 3 ** p
    need(k > 0 and k % 2 and 5 * x + 1 == 2 ** h * k, "wrong exact initial valuation")
    n = 5 * x
    first_odd_gaps = []
    for t in range(h):
        need(n == 2 ** (h - t) * 3 ** t * k - 1 and n > 1 and n % 2,
             "forced positive odd shortcut state failed")
        first_odd_gaps.append(v2(3 * n + 1))
        n = (3 * n + 1) // 2
    e = 3 ** (2 * m + 2) * numerator - 1
    need(n == e and e > 1 and e % 2 == 0, "wrong even debt endpoint")
    need(first_odd_gaps[:-1] == [1] * (h - 1), "early accelerated exponents are not one")
    need(first_odd_gaps[-1] == 1 + v2(e) > 1,
         "last forced odd input was confused with an exponent-one accelerated step")
    return e


def main():
    # The geometric expression B_m=(9*3^m+16*8^m)/5 obeys
    # B_0=5 and B_(m+1)=8*B_m-9*3^m; compare independent coefficients.
    need(Fraction(9 + 16, 5) == 5, "correction base failed")
    need((Fraction(27, 5), Fraction(128, 5))
         == (8 * Fraction(9, 5) - 9, 8 * Fraction(16, 5)),
         "geometric correction recurrence failed")
    need(Fraction(45, 16) < 4 and Fraction(9, 16) < 1,
         "universal grade majorant failed")
    arbitrary_prefixes = 0
    for m in (0, 1, 2, 3, 7, 15, 31):
        p, h = m + 2, 3 * m + 4
        for b in (4, 5, 6, 11):
            mod = 3 ** p
            q0 = pow(5 * 2 ** (b - 3), -1, mod)
            if q0 % 2 == 0:
                q0 += mod
            for q in (q0, q0 + 2 * mod):
                letters = [1] + [3] * m + [b]
                x, _ = reverse_word(q, letters)
                correction = 3 ** (m + 1) + 2 * sum(3 ** (m - j) * 8 ** j for j in range(m + 1))
                need(5 * correction == 3 ** p + 2 ** h, "correction closed form failed")
                need(3 ** p * x + correction == 2 ** sum(letters) * q,
                     "complete source numerator identity failed")
                verify_target_prefix(m, b, q, x)
                arbitrary_prefixes += 1
    complete_sources = 0
    ranks = []
    for p in (2, 3, 4, 5, 7, 10):
        m, h = p - 2, 3 * p - 2
        c = 2 if h % 2 == 0 else 1
        s0, period = direct_exponent(p, c)
        for s in (s0, s0 + period):
            b = s + 3
            letters = [1] + [3] * m + [b]
            x, states = reverse_word(1, letters)
            need(len(states) - 1 == p and states[-1] == 1, "wrong source first-hit rank")
            need(x % 3 == 2, "source misses physical-five domain")
            k = (5 * 2 ** s - 1) // 3 ** p
            need(k % 3 == c, "prescribed ternary residue failed")
            e = verify_target_prefix(m, b, 1, x)
            source_grade = sum(letters) - 2 * p
            need(source_grade == m + b - 3, "wrong source grade")
            majorant = Fraction(45, 16) * Fraction(9, 16) ** m
            need(Fraction(e, 2 ** (h + source_grade)) < majorant < 4,
                 "conditional grade obstruction failed")
            # Terminal source cycles have grade 0; the final 5->1 path has
            # four shortcut clocks and one odd input, hence grade 2.
            for padding in (0, 1, 7):
                padded_grade = sum(letters) + 2 * padding - 2 * (p + padding)
                need(padded_grade == source_grade, "terminal padding changed source grade")
                need((sum(letters) + 2 * padding + 4
                      - 2 * (p + padding + 1)) - source_grade == 2,
                     "homogeneous completion did not force grade difference two")
            complete_sources += 1
        ranks.append(p)
    files = ("NONHOMOGENEOUS_BOUNDARY.md", "check_nonhomogeneous_boundary.py")
    print(json.dumps({
        "status": "PASS",
        "scope": "NB1-NB3 architecture boundary only; no target convergence assertion",
        "arbitrary_positive_odd_endpoint_prefixes": arbitrary_prefixes,
        "independent_first_hit_sources": complete_sources,
        "source_ranks_replayed": ranks,
        "clock_distinction_checked": "first h-1 accelerated gaps are 1; h-th is 1+v2(E)>1",
        "input_sha256": {name: hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
                         for name in files},
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
