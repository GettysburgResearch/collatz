"""Exact finite controls for PRESSURE_WIENER_ATTACK.md; no infinite proof."""

from fractions import Fraction
import json
from math import gcd


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def odd_step(n):
    value = 3 * n + 1
    exponent = 0
    while value % 2 == 0:
        exponent += 1
        value //= 2
    return value, exponent


def unit(n):
    return n > 0 and gcd(n, 6) == 1


def trajectory_controls():
    rows = []
    for k in range(1, 7):
        exponent = 3 ** (k + 1) + 1
        q = (2**exponent - 1) // 3
        require((q + 1) % (2 * 3 ** (k + 1)) == 0, "divisibility")
        p = 2**k * ((q + 1) // 3**k) - 1
        current = p
        for j in range(k):
            expected = 2 ** (k - j) * 3**j * ((q + 1) // 3**k) - 1
            require(current == expected and unit(current), "actual unit state")
            current, gap = odd_step(current)
            require(gap == 1, "exact gap one")
        require(current == q and unit(q), "actual root")
        require(odd_step(q) == (1, exponent), "literal hit of one")
        require(q * 2**k <= 2 * 3**k * p, "q/p norm bound")
        weight = Fraction(3, 2) ** (2 * k)
        require(weight.denominator == 2 ** (2 * k), "source coefficient")
        rows.append({"k": k, "root_final_gap": exponent,
                     "root_bits": q.bit_length(), "source_bits": p.bit_length(),
                     "gap_one_source_weight_s2": str(weight)})
    return rows


FILTERS = {1: (2, 8), 2: (1, 4), 3: (2, 5),
           4: (1, 7), 5: (5, 8), 6: (4, 7)}


def filter_controls():
    checked = 0
    for e in range(1, 43):
        for q in range(1, 200):
            if not unit(q):
                continue
            numerator = 2**e * q - 1
            legal = numerator % 3 == 0 and unit(numerator // 3)
            expected = q % 9 in FILTERS[1 + (e - 1) % 6]
            require(legal == expected, "period-six exact branch filter")
            checked += 1
    return checked


def equation_controls():
    # For arbitrary H, let K(z)=z*(A_2 H)(z^3).
    # Then 4096 K(z)-K(z^64) equals the right side of (W17).
    degree = 6001
    count = 0
    for family in range(4):
        h = {n: Fraction(((family + 2) * n + 3) % 13 - 6, n + family + 1)
             for n in range(1, 80) if unit(n)}
        K = {}
        for n in range(1, (degree - 1) // 3 + 1):
            if not unit(n):
                continue
            q, e = odd_step(n)
            if q in h:
                K[3 * n + 1] = Fraction(3, 2**e) ** 2 * h[q]
        lhs = {d: 4096 * c for d, c in K.items()}
        for d, c in K.items():
            if 64 * d <= degree:
                lhs[64 * d] = lhs.get(64 * d, Fraction(0)) - c
        rhs = {}
        for e in range(1, 7):
            factor = Fraction(9 * 4096, 2 ** (2 * e))
            for n, c in h.items():
                d = 2**e * n
                if n % 9 in FILTERS[e] and d <= degree:
                    rhs[d] = rhs.get(d, Fraction(0)) + factor * c
        for d in range(degree + 1):
            require(lhs.get(d, 0) == rhs.get(d, 0), "finite operator equation")
            count += 1
    return count


def main():
    result = {
        "scope": "exact finite controls only; infinite spectral claims are written proofs",
        "trajectory_family": trajectory_controls(),
        "filter_cases": filter_controls(),
        "operator_coefficients_compared": equation_controls(),
        "success": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
