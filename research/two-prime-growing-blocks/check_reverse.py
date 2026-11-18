"""Exact finite checks for the reversed recurrence and its column operations."""
from fractions import Fraction
from itertools import permutations
from math import comb


def v3(value):
    value = Fraction(value)
    if not value:
        return float("inf")

    def power(n):
        count = 0
        while n % 3 == 0:
            count += 1
            n //= 3
        return count

    return power(value.numerator) - power(value.denominator)


def determinant(matrix):
    work = [row[:] for row in matrix]
    size = len(work)
    result = Fraction(1)
    for col in range(size):
        pivot = next((i for i in range(col, size) if work[i][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            result = -result
        diagonal = work[col][col]
        result *= diagonal
        for row in range(col + 1, size):
            ratio = work[row][col] / diagonal
            for k in range(col + 1, size):
                work[row][k] -= ratio * work[col][k]
    return result


def check(divisions, odds, nodes, weights, source, shift, size):
    q = Fraction(2**divisions, 3**odds)
    inverse = 1 / q
    count = len(nodes)

    def contribution(index):
        return sum(c * z**index for z, c in zip(nodes, weights))

    def triangular(index):
        return index * (index - 1) // 2

    def tail(index):
        partial = sum(contribution(k) * q**triangular(k)
                      for k in range(index + 1))
        if index < -1:
            partial = -sum(contribution(k) * q**triangular(k)
                           for k in range(index + 1, 0))
        return inverse**triangular(index + 1) * (source - partial)

    for start in range(-3, size + 1):
        for depth in range(1, size + 1):
            reverse = -sum(c * z**(1 - h) * inverse**(-comb(h, 2))
                           * (z * inverse**h)**start
                           for h in range(1, depth + 1)
                           for z, c in zip(nodes, weights))
            remainder = inverse**(depth * start - comb(depth, 2)) * tail(start - depth)
            assert tail(start) == reverse + remainder

    original = [[tail(shift + u + v) for v in range(size)] for u in range(size)]
    processed = [[] for _ in range(size)]
    costs = [[] for _ in range(size)]
    coeffs = [Fraction(1)]
    for v in range(size):
        depth = v // count
        for u in range(size):
            n = shift + u
            value = sum(c * tail(n + j) for j, c in enumerate(coeffs))
            remainder_terms = [
                c * inverse**(depth * (n + j) - comb(depth, 2)) * tail(n + j - depth)
                for j, c in enumerate(coeffs)
            ]
            assert value == sum(remainder_terms)
            cost = min(map(v3, remainder_terms))
            assert v3(value) >= cost
            processed[u].append(value)
            costs[u].append(cost)
        root = nodes[v % count] * inverse**(depth + 1)
        coeffs = [a - root * b for a, b in zip([0] + coeffs, coeffs + [0])]

    det = determinant(original)
    assert det == determinant(processed)
    lower_bound = min(sum(costs[u][v] for u, v in enumerate(order))
                      for order in permutations(range(size)))
    assert v3(det) >= lower_bound
    return size * (size + 4), size * size


def main():
    cases = [
        (7, 6, [Fraction(2**5, 3**5), Fraction(2**7, 3**6)], [1, -1]),
        (9, 6, [Fraction(2, 3), Fraction(2**3, 3**2), Fraction(2**9, 3**6)], [1, 2, -3]),
        (12, 5, [Fraction(4, 3), Fraction(32, 9), Fraction(256, 27), Fraction(4096, 243)],
         [3, -2, 4, -5]),
    ]
    total = [0, 0]
    for divisions, odds, nodes, weights in cases:
        for source in (Fraction(0), Fraction(-11, 81), Fraction(23, 7)):
            for shift in (0, 3):
                counts = check(divisions, odds, nodes, weights, source, shift, 6)
                total = [a + b for a, b in zip(total, counts)]
    print(f"Verified {total[0]} signed tail identities, {total[1]} transformed entries, "
          "and 18 rational determinants.")


if __name__ == "__main__":
    main()
