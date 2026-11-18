"""Independent finite expansion of the unblocked Padé numerator, in Z[T]."""
from collections import Counter
from itertools import product
from math import comb


def flag(j):
    return j % 10 in (1, 2)


def test_parameters(n, m, d):
    M, D = 37*n//2, 9*n
    A, B = 9*d, 9*m+1+9*d
    assert n % 2 == 0 and n >= 2
    context, exponent = m, 0
    for j in range(1, 101):
        context += d + flag(j) - 2*flag(j-1) + flag(j-2)
        exponent += 9*context + 1
        assert exponent == A*comb(j, 2) + B*j + 9*flag(j)

    # Expand every original factor choice, grouping only identical monomials.
    denominators = [Counter() for _ in range(D+1)]
    for indices in product(range(10), repeat=n):
        k = sum(indices)
        q_exp = sum((M+i)*power for i, power in enumerate(indices)) - comb(k+1, 2)
        denominators[k][A*q_exp+B*k] += (-1)**k

    K = A*(comb(M, 2)+9*comb(n, 2)) + B*M+9

    def coefficient(j, weight):
        result = Counter()
        for k, poly in enumerate(denominators[:j+1]):
            u = j-k
            term = B*u + A*comb(u, 2) + 9*weight(u)
            for index, value in poly.items():
                result[index+term] += value
                if j < M:
                    assert 0 <= index+term <= K
        return {power: v for power, v in result.items() if v}

    for j in range(M):
        coefficient(j, flag)
    for j in range(M, M+n):
        assert not coefficient(j, flag)
    for j in range(M+n, M+n+5):
        poly = coefficient(j, flag)
        predicted = A*(comb(j, 2) - D*(j-M) + 9*comb(n, 2)) + B*j + 9*flag(j-D)
        assert min(poly) == predicted and abs(poly[predicted]) == 1
        assert all(index >= 0 for index in poly)
    assert any(coefficient(j, lambda u: u % 10 == 1) for j in range(M, M+n))
    return M+n


def main():
    assert 64**93 > 81**88 and 88*297-93*281 == 3
    for n in (2, 4):
        for m, d in ((0, 2), (3, 5)):
            test_parameters(n, m, d)
    print("4 exact formal expansions; 12 zero coefficients; 20 first-tail coefficients; 4 rejected weight mutations")


if __name__ == "__main__":
    main()
