"""Exact controls for the two positive-quadrant congruence heights."""
from fractions import Fraction
from math import gcd
import json


SCALE = 2**62


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def heights(Q, r):
    h1 = Q
    twice_h2 = 2*Q
    for q in range(1, Q+1):
        if q >= h1 and 2*q >= twice_h2:
            break
        p = (-q*r) % Q or Q
        h1 = min(h1, max(q, p))
        twice_h2 = min(twice_h2, max(2*q, p))
    return h1, twice_h2


def passes(Q, H1, twoH2):
    numerator = 2*Q*H1-Q*twoH2
    denominator = H1*twoH2
    return 2*denominator < 3*numerator < 4*denominator


def rational_cycle(steps, odds):
    x = Fraction(3**odds-2**odds, 2**steps-3**odds)
    now = x
    minimum = x
    total = 0
    for i in range(steps):
        parity = now.numerator % 2
        require(parity == int(i < odds), "prescribed rational phase")
        total += parity
        require(5*(i+1) <= 8*total, "qualifying rational prefix")
        now = (3*now+1)/2 if parity else now/2
        minimum = min(minimum, now)
    require(now == x and minimum == x, "rational closure and minimum")
    return {"bits": steps, "ones": odds, "minimum": str(x),
            "above_33": x>33, "reduced_denominator": x.denominator}


def rational_and_alias(Q, a, b, d):
    main = (a*pow(b, -1, Q)) % Q
    residues = [main] if d == 1 else [
        (main+(Q//d)*j) % Q for j in range(1, d, 2)]
    rows = []
    for r in sorted(residues):
        require(Q//gcd(Q, b*r-a) == d, "precision-loss factor")
        H1, twoH2 = heights(Q, r)
        for c, value in [(1, Fraction(H1)), (2, Fraction(twoH2, 2))]:
            T = Fraction(Q, d*(a+c*b))
            error_cap = Fraction(d, 2)*max(b, Fraction(a, c))
            require(T <= value, "determinant lower bound")
            if T > error_cap:
                require(value <= T+error_cap, "rounded complement")
        rows.append({"residue": r, "height_one": H1, "twice_height_two": twoH2,
                     "denominator_test": passes(Q, H1, twoH2)})
    return {"slope": f"{a}/{b}", "loss": d, "cells": rows}


def main():
    rows = []
    for n in range(1, 16):
        Q = 2**n
        total_error_lo = selected_lo = native_lo = 0
        selected = 0
        high = {k: 0 for k in [1, 2, 4, 8, 16, 32]}
        for r in range(1, Q, 2):
            H1, twoH2 = heights(Q, r)
            require((r+1)*H1 >= Q, "integer determinant lower bound")
            decision = passes(Q, H1, twoH2)
            selected += decision
            den = Q**3
            numer = H1**3 if decision else 0
            ordinary_den = (r+1)**3
            total_error_lo += SCALE*abs(numer*ordinary_den-den)//(den*ordinary_den)
            selected_lo += SCALE*numer//den
            native_lo += SCALE//ordinary_den
            for k in high:
                high[k] += int(k*H1>Q)
        for k, count in high.items():
            require(count <= 9*k*k, "large-height population")
        rows.append({"bits": n, "selected": selected, "large_height_counts": high,
                     "total_error_enclosure": [total_error_lo, total_error_lo+Q//2],
                     "filtered_mass_enclosure": [selected_lo, selected_lo+selected],
                     "integer_mass_enclosure": [native_lo, native_lo+Q//2]})
    samples = [rational_and_alias(2**14, a, b, d) for a, b, d in
               [(3, 1, 1), (3, 1, 2), (3, 1, 4), (5, 3, 1), (7, 9, 1)]]
    print(json.dumps({"scope": "finite congruence rows and exact rational cycle checks",
                      "enclosure_denominator": SCALE, "rows": rows, "samples": samples,
                      "cycles": [rational_cycle(8, 5), rational_cycle(27, 17),
                                 rational_cycle(46, 29)]}, indent=2))


if __name__ == "__main__":
    main()

