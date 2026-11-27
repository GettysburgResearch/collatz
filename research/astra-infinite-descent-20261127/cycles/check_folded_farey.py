"""Exact finite controls for the sum across visits to each reduced clock rank."""
from collections import Counter
from itertools import combinations
from math import gcd
import json


def require(value, message):
    if not value:
        raise ArithmeticError(message)


def compositions(h, p):
    for places in combinations(range(1, h), p - 1):
        bounds = (0,) + places + (h,)
        word = tuple(y - x for x, y in zip(bounds, bounds[1:]))
        if all(word < word[i:] + word[:i] for i in range(1, p)):
            yield word


def orbit(word):
    h, p = sum(word), len(word)
    determinant = 2 ** h - 3 ** p
    carry = date = 0
    for step in word:
        carry = 3 * carry + 2 ** date
        date += step
    visited = []
    for step in word:
        visited.append(carry)
        numerator = 3 * carry + determinant
        require(numerator % 2 ** (step + 1) == 2 ** step, 'exact odd exponent')
        carry = numerator >> step
    require(carry == visited[0] and len(set(visited)) == p, 'least odd period')
    start = visited.index(min(visited))
    return word[start:] + word[:start], visited[start], determinant


def folded_data(word):
    h, p = sum(word), len(word)
    g = gcd(h, p)
    a, b = h // g, p // g
    offsets, dates = [], []
    elapsed = 0
    for i, step in enumerate(word):
        integer, rank = divmod(i * a, b)
        offsets.append(integer - elapsed)
        dates.append(rank)
        elapsed += step
    upper = max(offsets)
    columns = [[] for _ in range(b)]
    for rank, d in zip(dates, offsets):
        columns[rank].append(2 ** (upper - d))
    return a, b, g, upper - min(offsets), columns, dates[:b]


def coefficients(columns, step):
    b = len(columns)
    return [2 * columns[r] - (2 if r >= step else 1) * columns[(r - step) % b]
            for r in range(b)]


def lifts(coeffs, dates, a):
    """All chronological cuts, each cleared by the same 3**(b-1)."""
    b = len(dates)
    powers = [(1 << (t * a // b)) * 3 ** (b - 1 - t) for t in range(b)]
    result = []
    for cut, base_rank in enumerate(dates):
        total = 0
        for t, base in enumerate(powers):
            rank = dates[(cut + t) % b]
            # floor((at+r_cut)/b) contributes one more precisely on a wrap.
            total += coeffs[rank] * base * (2 if rank < dates[t] else 1)
        result.append(total)
    return result


def symbolic_mean(coeffs, dates, a, numerators):
    """Reduce both sides in Q[xi], xi**b=1/2, after clearing 3**(b-1)."""
    b = len(dates)
    actual = [0] * b
    expected = [0] * b
    for rank, numerator in zip(dates, numerators):
        actual[rank] += numerator
    for r, weight in enumerate(coeffs):
        for t in range(b):
            # xi**r * 2**(at/b) * 3**(-t) = xi**(r-at) * 3**(-t).
            quotient, rank = divmod(r - a * t, b)
            require(quotient <= 0, 'mean polynomial has integral coefficients')
            expected[rank] += weight * (1 << -quotient) * 3 ** (b - 1 - t)
    require(actual == expected, 'identity for the mean as an algebraic number')


def evaluate(word, stats, deep):
    word, carry, determinant = orbit(word)
    a, b, g, width, visits, dates = folded_data(word)
    columns = [sum(group) for group in visits]
    largest = max(columns)
    primary = coefficients(columns, 1)
    K = sum(x != 0 for x in primary)
    require(K >= 1 and largest <= g * 2 ** width, 'positive aggregate and size')
    require(width + 1 <= (K + 1) * ((g + 1) ** 2 // 4), 'binary carry width')
    merges = any(columns[r] == columns[r-1] and sorted(visits[r]) != sorted(visits[r-1])
                 for r in range(1, b))
    swaps = any(columns[r] == columns[r-1] and visits[r] != visits[r-1]
                for r in range(1, b))
    stats['distinct_native_cycles'] += 1
    stats['columns_hidden_by_equal_sums'] += swaps
    stats['different_multisets_hidden_by_equal_sums'] += merges
    stats['K_equal_to_one'] += K == 1
    A, B = 2 ** a, 3 ** b
    F = A - B
    q = determinant // gcd(determinant, carry)
    v = pow(a, -1, b)
    u = (1 - v * a) // b
    X = (pow(2, -u, F) * pow(3, -v, F)) % F
    require(gcd(F, carry) >= (F + q - 1) // q, 'complete denominator comparison')
    modulus = gcd(F, carry)
    primary_lifts = lifts(primary, dates, a)
    stats['cycles_with_zero_cut'] += 0 in primary_lifts
    stats['cycles_with_negative_cut'] += min(primary_lifts) < 0
    require(any(y > 0 for y in primary_lifts), 'strictly positive mean has a positive cut')
    if deep:
        symbolic_mean(primary, dates, a, primary_lifts)
        stats['symbolic_mean_checks'] += 1
    upper = 4 * q * K * largest * A
    lower = F
    cap = 0
    while 3 * lower <= upper:
        cap += 1
        lower *= 3
    require(b * g * B <= K * cap * (g * B + 2 * K * largest * (A - B)),
            'average support lower bound, integral version')
    for s in range(1, b):
        coeffs = coefficients(columns, s)
        observed = primary_lifts if s == 1 else lifts(coeffs, dates, a)
        support = [j for j, r in enumerate(dates) if coeffs[r]]
        require(1 <= len(support) <= min(b, s * K), 'telescoped support')
        positive = A ** (v * s % b) < B ** (v * s % b) * (1 << s)
        stats['signed_rank_steps'] += 1
        stats['Farey_positive_rank_steps'] += positive
        if positive:
            require(min(observed) > 0, 'positive summation by parts for every cut')
        if deep:
            # Direct derivation in the ring, independent of the lift loop.
            original = sum(c * pow(X, r, F) for r, c in enumerate(columns))
            residue = 2 * (1 - pow(X, s, F)) * original % F
            require(residue == sum(c * pow(X, r, F) for r, c in enumerate(coeffs)) % F,
                    'weighted seam')
        for j, integer in enumerate(observed):
            remaining = max((i - j) % b for i in support)
            gap = b - remaining
            require(integer % (3 ** (gap - 1) * modulus) == 0, 'actual reduced divisor')
            if integer:
                require(3 ** gap * F <= 4 * q * len(support) * largest * A,
                        'one-cut height and gap bound')
            if deep:
                expected = pow(3, b - 1, F) * pow(X, -dates[j], F) * residue % F
                require(integer % F == expected, 'literal full component at each cut')


def main():
    stats = Counter()
    for h in range(4, 23):
        for p in range(2, h):
            if gcd(h, p) == 1 or not 3 ** p < 2 ** h < 4 ** p:
                continue
            for word in compositions(h, p):
                evaluate(word, stats, deep=h <= 18 or stats['distinct_native_cycles'] % 127 == 0)
    print(json.dumps(dict(sorted(stats.items())), indent=2))


if __name__ == '__main__':
    main()
