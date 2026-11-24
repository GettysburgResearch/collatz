"""Finite exact controls for the complete fixed-source prefix denominators."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json
from math import gcd, isqrt, lcm, prod


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def row(word, companion):
    """The ordered branch composition is (b*s + c)/a."""
    a, b, c = 1, 1, 0
    for bit in word:
        mult = 3 if bit or companion else 1
        c = mult * c + bit * a
        b *= mult
        a *= 2 ** (1 + bit) if companion else 2
    return a, b, c


def literal_cycle(word, companion, counts):
    a, b, c = row(word, companion)
    base = Fraction(c, a - b)
    y = base
    for bit in word:
        residue = y.numerator * pow(y.denominator, -1, 4) % 4
        require(residue % 2 == bit, "wrong physical or companion branch")
        if companion:
            require(not bit or residue == 1, "forbidden companion residue")
            y = (3 * y + bit) / 2 ** (1 + bit)
        else:
            y = (3 ** bit * y + bit) / 2
        require(y.denominator == base.denominator, "full reduced denominator")
        counts["literal_rational_steps"] += 1
    require(y == base, "signed lap failed")


def interpolate(targets):
    """Exact null vector for the rectangular monomial evaluation matrix."""
    k = isqrt(len(targets))
    monomials = list(product(range(k + 1), repeat=2))
    matrix = [[u ** i * y ** j for i, j in monomials] for u, y in targets]
    pivots = []
    for col in range(len(monomials)):
        pos = len(pivots)
        pivot = next((r for r in range(pos, len(matrix)) if matrix[r][col]), None)
        if pivot is None:
            continue
        matrix[pos], matrix[pivot] = matrix[pivot], matrix[pos]
        scale = matrix[pos][col]
        matrix[pos] = [z / scale for z in matrix[pos]]
        for r, values in enumerate(matrix):
            if r != pos and values[col]:
                coeff = values[col]
                matrix[r] = [v - coeff * p for v, p in zip(values, matrix[pos])]
        pivots.append(col)
    free = next(i for i in range(len(monomials)) if i not in pivots)
    coeffs = [Fraction(0)] * len(monomials)
    coeffs[free] = Fraction(1)
    for values, col in zip(matrix, pivots):
        coeffs[col] = -values[free]
    scale = prod(z.denominator for z in coeffs)
    coeffs = [int(z * scale) for z in coeffs]
    divisor = gcd(*coeffs)
    return k, [(i, j, z // divisor) for (i, j), z in zip(monomials, coeffs) if z]


def evaluate(polynomial, u, y):
    return sum(z * u ** i * y ** j for i, j, z in polynomial)


def finite_words(counts):
    for L in range(1, 11):
        for word in product((0, 1), repeat=L):
            counts["all_marked_words"] += 1
            for companion in (False, True):
                literal_cycle(word, companion, counts)
                a, b, c = row(word, companion)
                ones = 0
                direct = 0
                for i, bit in enumerate(word):
                    if bit:
                        direct += (2 ** (i + ones) * 3 ** (L - 1 - i)
                                   if companion else 2 ** i * 3 ** (sum(word) - ones - 1))
                        ones += 1
                require(c == direct, "explicit chronological carry")
                counts["closed_form_carries"] += 1


def windows(n, horizon, counts):
    states = [n]
    for _ in range(horizon + 7):
        states.append(step(states[-1]))
    bits = [x % 2 for x in states]
    choices = ((0, 1, 2), (0, 2, 3, 5), (1, 2, 4, 5, 6))
    for companion in (False, True):
        s = 0 if companion else n
        for L in range(1, horizon, 3):
            prefix = bits[:L]
            if sum(prefix) == 0:
                continue
            a0, b0, c0 = row(prefix, companion)
            u = Fraction(a0, b0)
            y = Fraction(b0 * s + c0, a0)
            if not companion:
                require(y == states[L], "ordinary endpoint")
            for offsets in choices:
                targets = []
                divisors = []
                for h in offsets:
                    a, b, c = row(bits[L:L + h], companion)
                    A, B, C = row(bits[:L + h], companion)
                    require((A, B, C) == (a * a0, b * b0, b * c0 + a0 * c),
                            "chronological concatenation")
                    g = gcd(abs(A - B), C)
                    alpha, beta = Fraction(b, a), Fraction(a * s - c, b)
                    require((u - alpha).numerator % g == 0
                            and (y - beta).numerator % g == 0, "complete residue")
                    if not companion:
                        require(g == gcd(abs(A - B), states[L + h] - n),
                                "physical displacement gcd")
                    targets.append((alpha, beta))
                    divisors.append(g)
                    counts["target_moduli_above_one"] += int(g > 1)
                    counts["complete_modulus_targets"] += 1
                overlap = 1
                for i, j in combinations(range(len(offsets)), 2):
                    a, b, _ = row(bits[L + offsets[i]:L + offsets[j]], companion)
                    d = gcd(divisors[i], divisors[j])
                    require((a - b) % d == 0, "pairwise overlap")
                    overlap *= d
                    counts["clock_overlaps"] += 1
                k, polynomial = interpolate(targets)
                require(polynomial and all(evaluate(polynomial, x, z) == 0
                                           for x, z in targets), "interpolation")
                z = u.denominator ** k * y.denominator ** k * evaluate(polynomial, u, y)
                require(z.denominator == 1, "uncleared interpolant")
                require(abs(z.numerator) * overlap % prod(divisors) == 0,
                        "entire product divides cleared value times overlap")
                counts["integer_interpolants"] += 1
                counts["nonzero_integer_interpolants"] += int(z != 0)
                counts["zero_integer_interpolants"] += int(z == 0)


def v2(value):
    require(value != 0, "zero dyadic distance")
    value = Fraction(value)
    a, b = abs(value.numerator), value.denominator
    return (a & -a).bit_length() - (b & -b).bit_length()


def scalar_agreement(n, counts):
    states = [n]
    while states[-1] != 1:
        require(len(states) <= 2000, "fixed finite input did not reach one")
        states.append(step(states[-1]))
    bits = [x % 2 for x in states[:-1]]
    value = Fraction(9)
    at = {1: Fraction(9), 2: Fraction(6)}
    for x, bit in zip(reversed(states[:-1]), reversed(bits)):
        value = bit + Fraction(2 ** (1 + bit), 3) * value
        at[x] = value
    Q = lcm(*(z.denominator for z in at.values()))
    for L in range(1, len(bits) + 1):
        k = v2(states[L] - n)
        if k >= L:
            continue
        a, b, c = row(bits[:L], True)
        candidate = Fraction(-3 * c, a - b)
        require(candidate != value and candidate.denominator == abs(a - b) // gcd(abs(a - b), c),
                "candidate and full denominator")
        require(v2(value - candidate) == L + sum(bits[:L]) + k + sum(bits[:k]),
                "exact dyadic scalar agreement")
        counts["exact_genuine_scalar_agreements"] += 1
        counts["agreements_with_additional_physical_bits"] += int(k > 0)
    final = states + [2, 1] * 8
    word = [x % 2 for x in final[:-1]]
    for L, x in enumerate(final[1:], 1):
        a, b, c = row(word[:L], False)
        require((x - n) % gcd(abs(a - b), c) == 0, "transient physical bound")
        a, b, c = row(word[:L], True)
        diff = Q * (value - at[x])
        require(diff and diff.denominator == 1 and diff.numerator % gcd(abs(a - b), c) == 0,
                "transient genuine companion difference")
        counts["transient_double_cancellation_bounds"] += 1
    counts["convergent_scalar_sources"] += 1


def periodic_curve_control():
    for lap in range(1, 33):
        word = (1, 0) * lap
        a, b, c = row(word, True)
        require(Fraction(c, a) == -3 + 3 / Fraction(a, b), "periodic curve")
        require(gcd(abs(a - b), c) == abs(a - b), "full companion cancellation")
        a, b, c = row(word, False)
        require(gcd(abs(a - b), c) == abs(a - b), "full physical cancellation")
    for n in (1, 2):
        x = n
        bits = []
        for L in range(1, 65):
            bits.append(x % 2)
            x = step(x)
            for companion in (False, True):
                a, b, c = row(bits, companion)
                g = gcd(abs(a - b), c)
                if x == n:
                    require(g == abs(a - b), "return orbit cancellation")
                else:
                    require((3 if companion else 1) % g == 0, "off-return cancellation")


def main():
    counts = Counter()
    finite_words(counts)
    for n in (1, 7, 27, 97, 871, 6171, 77031, 837799):
        windows(n, 65, counts)
    for n in (7, 27, 97, 871, 6171, 77031, 837799):
        scalar_agreement(n, counts)
    periodic_curve_control()
    require(counts["zero_integer_interpolants"] > 0
            and counts["nonzero_integer_interpolants"] > 0, "degeneracy controls")
    print(json.dumps({"status": "PASS", "word_lengths": [1, 10],
                      "distinct_standard_laps_checked": 32, "counts": dict(counts)},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
