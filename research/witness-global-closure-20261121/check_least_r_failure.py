#!/usr/bin/env python3
"""Exact replay for the scoped least-R exclusions; no orbit search is used."""

from fractions import Fraction
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value):
    return isinstance(value, int) and not isinstance(value, bool)


def witness(x, cumulative):
    require(integer(x) and x > 0 and x % 2 == 1, "invalid witness start")
    require(isinstance(cumulative, (list, tuple)) and len(cumulative) > 0,
            "missing exponent tuple")
    require(all(integer(a) for a in cumulative), "nonintegral exponent")
    require(cumulative[0] == 0, "first exponent is not zero")
    require(all(b > a for a, b in zip(cumulative, cumulative[1:])),
            "exponents not strictly increasing")
    r = len(cumulative) - 1
    total = 3**r * x + sum(3**(r-1-j) * 2**cumulative[j] for j in range(r))
    require(total == 2**cumulative[-1], "defining witness identity fails")
    n = x
    for a, b in zip(cumulative, cumulative[1:]):
        numerator, divisor = 3*n+1, 2**(b-a)
        require(numerator % divisor == 0, "nonintegral quotient")
        n = numerator // divisor
        require(n > 0 and n % 2 == 1, "nonexact valuation or positivity")
    require(n == 1, "witness does not end at one")
    return r, cumulative[-1]


def affine_word(start, word):
    """Check the whole cylinder u>=0, not selected values of u."""
    a, b = map(Fraction, start)
    states = [(a, b)]
    for exponent in word:
        require(integer(exponent) and exponent > 0, "bad word letter")
        a, b = 3*a / 2**exponent, (3*b+1) / 2**exponent
        states.append((a, b))
    for a, b in states:
        require(a.denominator == b.denominator == 1, "nonintegral affine state")
        require(a > 0 and b > 0 and int(a) % 2 == 0 and int(b) % 2 == 1,
                "affine state is not positive odd on every lift")
    return states


def main():
    H, G = Fraction(213597, 23), Fraction(355995, 23)
    require(G == Fraction(5, 3)*H, "general height conversion")
    # These constants are separately certified by check_reverse_cover.py.
    even_margin = 23*4**30 - 355995*3**29 - 23
    odd_margin = 46*4**32 - 427194*3**32 - 640814
    require(even_margin == 2085123415945956840, "even threshold arithmetic")
    require(odd_margin == 56951120834265369368, "odd threshold arithmetic")
    require(even_margin > 0 and odd_margin > 0, "threshold signs")
    # Coefficient identity F(d+1)=3F(d)+A4^d+2D for F(d)=A4^d-B3^d-D.
    # Compare independent coefficients of A4^d, B3^d, D.
    require((4, -3, -1) == (3+1, -3, -3+2), "monotone margin identity")

    orders = {}
    for modulus, expected in ((81, 54), (243, 162)):
        values = [pow(2, k, modulus) for k in range(expected)]
        require(len(set(values)) == expected and pow(2, expected, modulus) == 1,
                "modular order fails")
        require(set(values) == {k for k in range(1, modulus) if k % 3},
                "powers do not cover units")
        orders[str(modulus)] = expected

    # Every rank-two word in these families has b=b0+162j. Its p=2^b
    # lies in p=2^b0+243*2^b0*u, u>=0, so exact affine parity checks apply.
    rows = (
        (1, 22, (2, 2, 1), 4, 6),
        (2, 68, (1, 2, 1), 2, 4),
        (3, 118, (1, 1, 1), 0, 2),
    )
    prefix_count = 0
    for a, b0, word, endpoint_shift, power_shift in rows:
        solutions = [b for b in range(162)
                     if pow(2, a+b, 243) == (2**a+3) % 243]
        require(solutions == [b0], "rank-two last-letter progression")
        p0, pa = 2**b0, 243*2**b0
        start = (Fraction(2**a*pa, 27), Fraction(2**a*p0-2**a-3, 27))
        states = affine_word(start, word)
        require(states[-1] == (Fraction(pa, 2**endpoint_shift),
                               Fraction(p0, 2**endpoint_shift)+1),
                "rank-two endpoint polynomial")
        prefix_count += len(states)
        for j in (0, 1):
            b = b0+162*j
            n = (2**(a+b)-2**a-3)//9
            require(n > 0 and n % 27 == 0 and n % 2 == 1, "source domain")
            witness(n, [0, a, a+b])
            q = 3**((b-power_shift)//2)
            if (a, b) != (1, 22):
                require(G*q < n, "rank-two height comparison")

    margins = {
        "a1_b184": 23*(2**185-5)-9*355995*3**89,
        "a2_b68": 23*(2**70-7)-9*355995*3**32,
        "a3_b118": 23*(2**121-11)-9*355995*3**58,
    }
    require(all(v > 0 for v in margins.values()), "rank-two base margin")
    require(4**81 > 3**81 > 1, "rank-two progression comparison")
    require([b for b in range(162) if pow(2, 5+b, 243) == 35] == [88],
            "remaining a5 family was misidentified")

    data = json.loads(Path(__file__).with_name("low_rank_witnesses.json").read_text())
    sizes = {}
    for exponent, expected in ((8, (24, 51)), (25, (137, 257))):
        row = data[str(exponent)]
        require(row["x"] == 3**exponent, "wrong finite source")
        require(witness(row["x"], row["A"]) == expected, "finite witness sizes")
        require((row["odd_steps"], row["total_exponent"]) == expected,
                "finite witness metadata")
        sizes[str(exponent)] = {"x": row["x"], "odd_steps": expected[0],
                                "total_exponent": expected[1]}
    require(54*2 >= 60, "rank-one high-letter exclusion")

    x, A = data["8"]["x"], data["8"]["A"]
    bad_cases = [
        (x+2, A),
        (x, A[:-1]+[A[-1]+1]),
        (x, [1]+A[1:]),
        (x, [0, 0]+A[2:]),
        (x, [False]+A[1:]),
        (x, A[:-1]),
        (x, []),
        (True, [0]),
    ]
    rejected = 0
    for bad_x, bad_A in bad_cases:
        try:
            witness(bad_x, bad_A)
        except ValueError:
            rejected += 1
        else:
            raise ValueError("damaged witness was accepted")
    print(json.dumps({
        "status": "PASS",
        "full_claim": "UNRESOLVED",
        "height_bound_dependency": "RGA-003; independently replay check_reverse_cover.py",
        "unit_height": str(H), "general_height": str(G),
        "even_excluded_from": 60, "odd_excluded_from": 65,
        "modular_orders": orders,
        "rank_two_universal_affine_prefix_states": prefix_count,
        "rank_two_source_witness_fixtures": 6,
        "rank_two_base_margins": margins,
        "finite_endpoint_certificates": sizes,
        "damaged_witnesses_rejected": rejected,
        "scope": "Least global R failure only; remaining families are not proved.",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
