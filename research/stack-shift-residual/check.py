"""Exact finite checks for period cutoff, minor divisors and shift residual."""

from fractions import Fraction
from functools import reduce
from itertools import combinations, permutations
from math import factorial, gcd, lcm


T = Fraction(64, 81)


def margins():
    rho = Fraction(94639, 100000)
    delta = Fraction(31, 30)
    height = (delta / 4 - Fraction(1, 12)) / (delta - 1)
    assert height == Fraction(21, 4)
    lo, hi = Fraction(683, 100), Fraction(2641, 100)
    values = [
        rho * ((s + delta + 1) ** 2 / 2 - delta / 2)
        - (s + delta) ** 2 / 2 - delta / 2 - height
        for s in (lo, hi)
    ]
    assert 64**100000 > 81**94639
    assert values == [Fraction(11598853, 6000000000), Fraction(10987957, 6000000000)]
    assert (hi - lo) / (delta - 1) == Fraction(2937, 5) > 587


def determinant(rows):
    if len(rows) == 1:
        return rows[0][0]
    return sum(
        (-1) ** i * entry * determinant([row[:i] + row[i + 1:] for row in rows[1:]])
        for i, entry in enumerate(rows[0])
    )


def multiply(left, right):
    output = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] += x * y
    return output


def scaled_argument(coefficients, q):
    return [value * q**i for i, value in enumerate(coefficients)]


def numerical_polynomials(increments, n, D, start):
    r = len(increments)
    a = Fraction(9 * sum(increments), r)
    E = [0]
    current = start
    for j in range(1, 3 * D + 2 * r + n + 1):
        current += increments[(j - 1) % r]
        E.append(E[-1] + 9 * current + 1)
    Q = T ** (a * r).__floor__()
    base = [T**e for e in E]
    for j in range(r, len(base)):
        assert base[j] == base[r] * Q ** (j - r) * base[j - r]
    g = [(a * ((D + Fraction(n, 2)) * k - Fraction(k * k, 2))).__floor__() for k in range(D + 1)]
    costs = [[g[k] + E[D + i - k] for k in range(D + 1)] for i in range(n)]
    minimum = [min(row) for row in costs]
    maximum = [max(row) for row in costs]
    scaled = [[64 ** (e - minimum[i]) * 81 ** (maximum[i] - e) for e in row]
              for i, row in enumerate(costs)]
    all_cols = list(range(D + 1))
    bound = min(
        min(sum(costs[i][k] - minimum[i] for i, k in enumerate(injection)),
            sum(maximum[i] - costs[i][k] for i, k in enumerate(injection)))
        for injection in permutations(all_cols, n)
    )
    divisors = 64**bound * 81**bound
    minors = {}
    for columns in combinations(all_cols, n):
        submatrix = [[row[k] for k in columns] for row in scaled]
        value = determinant(submatrix)
        assert value and value % divisors == 0
        diagonal_cost = sum(costs[i][k] for i, k in enumerate(columns))
        assert all(diagonal_cost < sum(costs[i][k] for i, k in enumerate(perm))
                   for perm in permutations(columns) if perm != columns)
        minors[columns] = value
    common = reduce(gcd, minors.values())
    max_minor = max(map(abs, minors.values()))
    span = sum(h - l for h, l in zip(maximum, minimum))
    assert Fraction(max_minor, common) <= factorial(n) * 81 ** (span - 2 * bound)
    support = list(range(n)) + [D]
    c = [0] * (D + 1)
    for position, k in enumerate(support):
        cols = tuple(j for j in support if j != k)
        c[k] = (-1) ** position * minors[cols]
    common = reduce(gcd, c)
    c = [x // common for x in c]
    V = [x * T**e for x, e in zip(c, g)]
    VF = multiply(V, base)
    U = VF[:D]
    assert not any(VF[D:D + n])
    first = multiply(U, scaled_argument(V, Q))
    second = multiply(base[:r], multiply(V, scaled_argument(V, Q)))
    third = [0] * r + [base[r] * z for z in multiply(V, scaled_argument(U, Q))]
    length = max(map(len, (first, second, third)))
    def at(poly, i):
        return poly[i] if i < len(poly) else 0
    residual = [at(first, i) - at(second, i) - at(third, i) for i in range(length)]
    assert not any(residual[:D + n]) and any(residual)
    reduced_degree = max(i for i, x in enumerate(residual) if x) - D - n
    assert reduced_degree <= D - n + r - 1
    return len(minors), reduced_degree


if __name__ == "__main__":
    margins()
    answers = [numerical_polynomials(w, n, D, m) for w, n, D, m in
               [((1, 2, 1), 2, 3, 0), ((2, 1), 3, 4, 1), ((1,), 3, 5, 0)]]
    print(f"Verified period-587 margins, {sum(x for x, _ in answers)} full minors and three residuals.")
    print(f"Residual degrees after removing the certified origin factor: {[y for _, y in answers]}")
