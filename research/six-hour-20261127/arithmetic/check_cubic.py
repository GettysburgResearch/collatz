"""Exact finite controls for cubic rotations, an ordinary trace denominator, and tower orders."""
import json
from fractions import Fraction
from itertools import product
from math import gcd


def require(condition, message):
    if not condition:
        raise ValueError(message)


def odd_step(x):
    n = 3 * x + 1
    return n // (n & -n)


def squarefree_part(n):
    p = 2
    value = 1
    while p * p <= n:
        odd = False
        while n % p == 0:
            n //= p
            odd = not odd
        if odd:
            value *= p
        p = 3 if p == 2 else p + 2
    return value * n


def dickson(e, b):
    prev, curr = 2, b
    for _ in range(e):
        prev, curr = curr, b * curr - prev
    return prev


def trace_control():
    x = 43681
    departures = []
    labels = {}
    while x not in departures:
        departures.append(x)
        key = squarefree_part(3 * x * (3 * x + 1))
        labels.setdefault(key, []).append(x)
        x = odd_step(x)
    repeated = {p: values for p, values in labels.items() if len(values) > 1}
    require(x == 1 and departures[-1] == 1 and len(departures) == 58, "ordinary simple interval")
    require(repeated == {3: [43681, 1]}, "field repetitions")
    require(dickson(5, 14) == 12 * 43681 + 2, "Pell exponent five")
    trace = 1 + Fraction(4 * 14, dickson(3, 14) + dickson(2, 14))
    require(trace == Fraction(369, 362), "exact trace")
    require(181**2 == departures[1] and gcd(181, departures[0] * x) == 1, "internal prime")
    return {"start": departures[0], "terminal": x, "distinct_departures": len(departures),
            "pell_labels": len(labels), "repeated_labels": repeated, "normalized_trace": str(trace),
            "interior_vertex": departures[1], "interior_prime": 181}


def rotation_control():
    weights = (2, -1, -1)
    table = []
    for a, b in product(range(3), repeat=2):
        total = sum(abs(weights[i] - weights[(i + a) % 3] - weights[j] + weights[(j + b) % 3])
                    for i, j in product(range(3), repeat=2))
        expected = 24 if a and b else 18 if a or b else 0
        require(total == expected, "rotation cost")
        table.append(total)
    return table


def mobius(n):
    value = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            value *= -1
            if n % p == 0:
                return 0
        p += 1
    return -value if n > 1 else value


def ramanujan(n, j):
    return sum(a * mobius(n // a) for a in range(1, n + 1) if gcd(n, j) % a == 0)


def divide_monic(poly, divisor):
    coeff = poly[:]
    quotient = [0] * (len(poly) - len(divisor) + 1)
    for offset in range(len(quotient) - 1, -1, -1):
        multiplier = coeff[offset + len(divisor) - 1]
        quotient[offset] = multiplier
        for j, entry in enumerate(divisor):
            coeff[offset + j] -= multiplier * entry
    require(not any(coeff), "monic exact division")
    return quotient


def cyclotomics(limit):
    result = {}
    for n in range(1, limit + 1):
        poly = [-1] + [0] * (n - 1) + [1]
        for a in range(1, n):
            if n % a == 0:
                poly = divide_monic(poly, result[a])
        result[n] = poly
    return result


def remainder(poly, divisor):
    coeff = poly[:]
    for k in range(len(poly) - 1, len(divisor) - 2, -1):
        multiplier = coeff[k]
        offset = k - len(divisor) + 1
        for j, entry in enumerate(divisor):
            coeff[offset + j] -= multiplier * entry
    return coeff[:len(divisor) - 1]


def tower_control():
    limit = 30
    polys = cyclotomics(2 * limit)
    checked = 0
    for d in range(1, limit + 1):
        n = 2 * d
        for q in range(2, n + 1):
            if n % q:
                continue
            weights = [ramanujan(q, j) * (1 if j in (0, d) else 2) for j in range(d + 1)]
            require(sum(weights) == 0, "normalization at infinity")
            for k in range(d + 1):
                poly = [0] * n
                for j, weight in enumerate(weights):
                    poly[k * j % n] += weight
                    poly[-k * j % n] += weight
                reduced = remainder(poly, polys[n])
                expected = 2 * n if gcd(k, n) == n // q else 0
                require(reduced == [expected] + [0] * (len(reduced) - 1), "Fourier orbit")
            checked += 1
    return {"levels": limit, "divisor_rules_checked": checked,
            "degree_five_first_nonzero_frequencies": [1, 2, 5]}


if __name__ == "__main__":
    print(json.dumps({"trace": trace_control(), "rotation_cost_times_two_summed_over_nine": rotation_control(),
                      "tower": tower_control()}, sort_keys=True, indent=2))

