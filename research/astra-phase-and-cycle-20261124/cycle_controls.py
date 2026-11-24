"""Exact finite controls for CYCLE_FACTORS.md, using only the standard library."""

from fractions import Fraction
from functools import cache, reduce
from itertools import combinations
from math import gcd, lcm, prod


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def trim(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def primitive_part(poly):
    trim(poly)
    if not poly:
        return []
    content = reduce(gcd, poly)
    return [v // content for v in poly]


def polynomial_gcd(left, right):
    left, right = list(left), list(right)
    while right:
        while len(left) >= len(right):
            shift = len(left) - len(right)
            lc = left[-1]
            left = [v * right[-1] for v in left]
            for i, v in enumerate(right):
                left[i + shift] -= lc * v
            left = primitive_part(left)
        left, right = right, left
    left = primitive_part(left)
    return [-v for v in left] if left[-1] < 0 else left


def monic_quotient(poly, divisor):
    remainder = list(poly)
    quotient = [0] * (len(poly) - len(divisor) + 1)
    require(divisor[-1] == 1, "expected monic divisor")
    while len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        c = remainder[-1]
        quotient[shift] = c
        for i, v in enumerate(divisor):
            remainder[i + shift] -= c * v
        trim(remainder)
    require(not remainder, "non-exact polynomial division")
    return quotient


def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


@cache
def components(a, b, g):
    result = {}
    for h in divisors(g):
        poly = [-2 ** (a * h)] + [0] * (b * h - 1) + [1]
        for d in divisors(h)[:-1]:
            poly = monic_quotient(poly, result[d])
        result[h] = poly
    return result


def prime_powers(n):
    result = []
    for p in range(2, n + 1):
        if n % p == 0:
            q = 1
            while n % p == 0:
                n //= p
                q *= p
            result.append((p, q))
    return result


def primitive(length, positions):
    odd = set(positions)
    return all(any((d + k) % length not in odd for d in odd)
               for k in divisors(length)[:-1])


def polynomials(length, positions):
    p = len(positions)
    return [-2**length] + [0] * (p - 1) + [1], [2**d for d in reversed(positions)]


def finite_words(limit):
    totals = [0, 0, 0]
    for length in range(1, limit + 1):
        for p in range(1, length + 1):
            g = gcd(length, p)
            a, b = length // g, p // g
            t = b // gcd(b, 2)
            factors = components(a, b, g)
            for positions in combinations(range(length), p):
                if not primitive(length, positions):
                    continue
                f, qpoly = polynomials(length, positions)
                residual = monic_quotient(f, polynomial_gcd(f, qpoly))
                n = len(residual) - 1
                retained = []
                for h, factor in factors.items():
                    degree = len(polynomial_gcd(residual, factor)) - 1
                    if degree:
                        retained.append(h)
                        size = len(factor) - 1
                        allowed = {size}
                        if b % 2 == 0 and h % 8 == 4:
                            allowed.add(size // 2)
                        require(degree in allowed, "incorrect projected occupancy")
                    totals[1] += 1
                phi_sum = sum((len(factors[h]) - 1) // b for h in retained if h > 1)
                cost = sum(q - q // prime for prime, q in prime_powers(g))
                require(lcm(*retained) == g, "projected lcm")
                require(n >= b + t * phi_sum and cost <= 1 + (n - b) // t,
                        "fibre or maximal-prime-power bound")
                if len(prime_powers(g)) == 1 and 2**length > 3**p:
                    prime = prime_powers(g)[0][0]
                    if g == 4 and b % 2 == 0:
                        lower = 2 ** (a - 1)
                    else:
                        lower = 2 ** (length - length // prime) + 1
                    value = abs(sum(v * 3**i for i, v in enumerate(residual)))
                    require(value >= lower, "prime-power distinguished evaluation")
                    totals[2] += 1
                totals[0] += 1
    return totals


def check_rational_cycle(length, positions, expected, expected_minimum=None):
    f, q = polynomials(length, positions)
    c = sum(v * 3**i for i, v in enumerate(q))
    d = abs(2**length - 3**len(positions))
    start = Fraction(c, d)
    require(primitive(length, positions) and start == expected, "rational source")
    x, den = start.numerator, start.denominator
    minimum = x
    for i in range(length):
        bit = int(i in positions)
        require(x % 2 == bit, "illegal rational parity")
        x = (3 * x + den) // 2 if bit else x // 2
        minimum = min(minimum, x)
    require(x == start.numerator, "rational closure")
    if expected_minimum is not None:
        require(Fraction(minimum, den) == expected_minimum, "minimum cyclic state")
    return f, q


def determinant(matrix):
    n = len(matrix)
    result = Fraction(1)
    for j in range(n):
        pivot = next((k for k in range(j, n) if matrix[k][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            matrix[pivot], matrix[j] = matrix[j], matrix[pivot]
            result = -result
        pivot_value = matrix[j][j]
        result *= pivot_value
        for k in range(j + 1, n):
            scale = matrix[k][j] / pivot_value
            for i in range(j + 1, n):
                matrix[k][i] -= scale * matrix[j][i]
    return result


def example_norm(h, positions):
    degree, binomial_constant = {1: (4, 2), 2: (4, -2), 4: (8, -4)}[h]
    matrix = [[Fraction(0) for _ in range(degree)] for _ in range(degree)]
    for i, d in enumerate(positions):
        e = 4 * d - 7 * i
        w = (2 * i - d) % h
        require(e >= 0, "minimum-discrepancy rotation required")
        for column in range(degree):
            for offset, sign in ((0, -1), (1, 1)):
                power, row = divmod(column + e + 4*w + offset, degree)
                matrix[row][column] += Fraction(sign * binomial_constant**power, 2**w)
    return determinant(matrix)


def main():
    totals = finite_words(12)
    check_rational_cycle(12, (0, 1, 2, 4), Fraction(1, 55))
    check_rational_cycle(20, (0, 1, 2, 3, 4, 5, 6, 8, 13, 14, 15, 16), Fraction(601, 295))
    positions = (0, 2, 3, 4, 5, 8, 9, 10, 11, 12, 14, 16, 17, 18, 19, 22)
    f, q = check_rational_cycle(28, positions, Fraction(577703, 1078415))
    require(polynomial_gcd(f, q) == [1], "full polynomial survival")
    k = min(range(16), key=lambda i: 4*positions[i] - 7*i)
    rotated = sorted((d - positions[k]) % 28 for d in positions)
    cases = ((1, 47, 2157911), (2, 209, 9937323), (4, 22945, 87054402105125))
    for h, component, expected in cases:
        j = example_norm(h, rotated)
        factor = components(7, 4, 4)[h]
        require(abs(sum(c * 3**i for i, c in enumerate(factor))) == component,
                "component distinguished value")
        require(j == expected and j % component == 0, "whole norm absorption")
    require(prod(row[1] for row in cases) == 2**28 - 3**16, "whole denominator")
    higher = (0, 1, 4, 6, 7, 10, 12, 13, 14, 15, 16, 17, 18, 22, 23, 24)
    f, q = check_rational_cycle(28, higher, Fraction(174449, 82955),
                                Fraction(88181, 82955))
    require(polynomial_gcd(f, q) == [1], "higher-floor full survival")
    k = min(range(16), key=lambda i: 4*higher[i] - 7*i)
    rotated = sorted((d - higher[k]) % 28 for d in higher)
    for (h, component, _), expected in zip(cases, (-29281, 411939, 16950045125)):
        j = example_norm(h, rotated)
        require(j == expected and j % component == 0, "higher-floor norm saturation")
    print(f"primitive words={totals[0]}, components={totals[1]}, "
          f"positive prime-power controls={totals[2]}, exact rational cycles=4, "
          "simultaneously saturated nonzero norms=6")


if __name__ == "__main__":
    main()
