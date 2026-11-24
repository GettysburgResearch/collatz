"""Exact finite checks for the companion determinant, its content and leading valuation."""

from fractions import Fraction
from itertools import combinations
import json
from math import comb, factorial, gcd, prod
from random import Random


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def shortcut(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def order(value, prime):
    value = abs(value)
    require(value > 0, "valuation needs a nonzero input")
    if prime == 2:
        return (value & -value).bit_length() - 1
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def matching_valuation(x, y):
    """Exact companion difference valuation, using genuine physical inputs."""
    length = order(x - y, 2)
    result = length
    for _ in range(length):
        require(x % 2 == y % 2, "mismatched shared physical branch")
        result += x % 2
        x, y = shortcut(x), shortcut(y)
    require(x % 2 != y % 2, "first unequal bit")
    return result


def path(source, length):
    x, q, a, c = source, 1, 1, 0
    points = [(x, q, a, c)]
    for _ in range(length):
        bit = x % 2
        y = shortcut(x)
        if x >= 6:
            require((2 * y) ** 3 <= 32**bit * x**3, "physical one-step bound")
        c, q, a, x = 3 * c + bit * a, q * 3, a * (2**(1 + bit)), y
        points.append((x, q, a, c))
    return points


def literal_source(bits):
    """Take the least positive residue for this finite physical parity prefix."""
    carry, multiplier = 0, 1
    for j, bit in enumerate(bits):
        if bit:
            carry = 3 * carry + (1 << j)
            multiplier *= 3
    modulus = 1 << len(bits)
    return -carry * pow(multiplier, -1, modulus) % modulus or modulus


def row(q, a, c, degree):
    return [q**(degree - j - k) * (a - q)**j * c**k
            for j in range(degree + 1) for k in range(degree + 1 - j) if j + k]


def determinant(matrix):
    """Bareiss elimination with row swaps and checked exact divisions."""
    data = [list(values) for values in matrix]
    previous, sign, size = 1, 1, len(data)
    for j in range(size - 1):
        swap = next((k for k in range(j, size) if data[k][j]), None)
        if swap is None:
            return 0
        if swap != j:
            data[swap], data[j] = data[j], data[swap]
            sign = -sign
        pivot = data[j][j]
        for k in range(j + 1, size):
            for l in range(j + 1, size):
                numerator = pivot * data[k][l] - data[k][j] * data[j][l]
                result, remainder = divmod(numerator, previous)
                require(remainder == 0, "Bareiss division")
                data[k][l] = result
        previous = pivot
    return sign * data[-1][-1]


def check_matrix(points, clocks, degree, counts):
    block = [degree] + list(range(degree, 0, -1))
    degrees = list(range(degree, -1, -1))
    size = sum(block)
    require(len(clocks) == size and list(clocks) == sorted(set(clocks)), "clock order")
    chosen = [points[i] for i in clocks]
    matrix = [row(q, a, c, degree) for _, q, a, c in chosen]
    reductions = [gcd(a - q, c) for _, q, a, c in chosen]
    require(all(gcd(*v) == g for v, g in zip(matrix, reductions)), "projected row content")
    result = determinant(matrix)
    counts["determinants"] += 1
    if result == 0:
        counts["zero_determinants"] += 1
    else:
        counts["nonzero_determinants"] += 1
        outside = abs(result) // (2**order(result, 2) * 3**order(result, 3))
        require(outside % prod(reductions) == 0, "full factored matrix content")
        n, end = clocks[0], clocks[-1]
        _, q0, a0, _ = points[n]
        _, q1, a1, _ = points[end]
        if a1 >= q1:
            trial = max([Fraction(1)] + [Fraction(c, a) for _, _, a, c in chosen])
            total = comb(degree + 2, 3)
            bound = (2**size * factorial(size) * a0**degree *
                     Fraction(q0, q1)**degree *
                     (Fraction(q1, q0) * Fraction(a1, a0)**2 * trial)**total)
            require(outside <= bound, "simultaneous real, dyadic and triadic determinant bound")
            counts["three_place_bounds"] += 1
    marked = [points[0][0]] + [x for x, _, _, _ in chosen]
    if len(set(marked)) != len(marked):
        counts["repeated_physical_state"] += 1
        return
    gap = min(clocks[0], *[b - a for a, b in zip(clocks, clocks[1:])])
    r = max(order(a - b, 2) for a, b in combinations(marked, 2))
    budget = 2 * (degree + sum(comb(m, 2) for m in block))
    start, weight, extra = 0, 0, 0
    for k, m in zip(degrees, block):
        group = chosen[start:start + m]
        weight += k * sum(order(a, 2) for _, _, a, _ in group)
        xs = [x for x, _, _, _ in group]
        extra += sum(matching_valuation(x, y) for x, y in combinations(xs, 2))
        if k == degree:
            extra += sum(matching_valuation(x, marked[0]) for x in xs)
        start += m
    require(extra <= budget * r, "Vandermonde valuation cap")
    if result:
        require(order(result, 2) >= weight + min(gap, extra), "valuation lower bound")
    if gap > extra:
        require(result != 0 and order(result, 2) == weight + extra, "strict leading valuation")
        counts["exact_leading_valuations"] += 1
    if gap > budget * r:
        require(result != 0, "spacing theorem")
        counts["spacing_certificates_by_degree"][degree - 1] += 1


def main():
    counts = dict(determinants=0, nonzero_determinants=0, zero_determinants=0,
                  three_place_bounds=0, repeated_physical_state=0,
                  exact_leading_valuations=0, spacing_certificates_by_degree=[0] * 3)
    content_tests = 0
    for length in range(1, 9):
        for source in range(1, 2**length + 1):
            _, q, a, c = path(source, length)[-1]
            for d in range(1, 5):
                require(gcd(*row(q, a, c, d)) == gcd(a - q, c), "all-word content")
                content_tests += 1
    counts["all_word_degree_content"] = content_tests
    _, q, a, c = path(2**20 - 1, 20)[-1]
    require(c == a - q and gcd(*row(q, a, c, 4)) % 25 == 0, "repeated prime factor")
    counts["repeated_prime_control"] = 25
    for first, second in [(2, 4), (4, 12), (18, 50)]:
        p = path(1, second)
        matrix = [row(*p[i][1:], 1) for i in (first, second)]
        require(determinant(matrix) == 0, "ordinary whole-lap obstruction")
        check_matrix(p, [first, second], 1, counts)
    rng = Random(20261124)
    for n in (3, 7, 27, 871, 6171, 77031, 837799):
        p = path(n, 120)
        for d in (1, 2):
            m = comb(d + 2, 2) - 1
            for _ in range(16):
                clocks = sorted(rng.sample(range(2, 120), m))
                check_matrix(p, clocks, d, counts)
    # Changing finite lifts exercise all three degree groups with large
    # separations. Their original source stays fixed throughout each matrix.
    for d, spacing in [(1, 31), (2, 80), (3, 220)]:
        m = comb(d + 2, 2) - 1
        clocks = [spacing * j for j in range(1, m + 1)]
        bits = [int(rng.randrange(10) < 7) for _ in range(clocks[-1])]
        n = literal_source(bits)
        p = path(n, len(bits))
        require([x % 2 for x, *_ in p[:-1]] == bits, "literal prescribed finite orbit")
        check_matrix(p, clocks, d, counts)
    require(all(counts["spacing_certificates_by_degree"]), "nonvacuous spacing for every degree")
    require(counts["exact_leading_valuations"] and counts["three_place_bounds"], "valuation coverage")
    print(json.dumps(counts, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
