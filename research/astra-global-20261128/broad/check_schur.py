"""Exact replay of sparse alternants on separated greedy rows, and a wrong real branch."""
from fractions import Fraction
from itertools import combinations
from math import prod
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valuation(n, p):
    x = abs(n)
    if x == 0:
        raise ValueError("zero valuation argument")
    k = 0
    while x % p == 0:
        x //= p
        k += 1
    return k


def vp(x, p):
    return valuation(x.numerator, p) - valuation(x.denominator, p)


def determinant(values, powers):
    matrix = [[x**m for m in powers] for x in values]
    result = Fraction(1)
    for k in range(len(values)):
        pivot = matrix[k][k]
        require(pivot != 0, ("nonzero leading minor", k))
        result *= pivot
        for i in range(k+1, len(values)):
            multiple = matrix[i][k] / pivot
            for j in range(k+1, len(values)):
                matrix[i][j] -= multiple * matrix[k][j]
    return result


def rows(n, target):
    total = 0
    c = Fraction(n+1)
    accepted = []
    e = 0
    while len(accepted) < target:
        u = vp(c, 2) - e
        old = total
        c += 2**e * Fraction(2, 3)**u
        total = u
        e += 1
        if total > old:
            require(-vp(c, 3) == u, ("selected row denominator", n, e))
            accepted.append(c)
    return accepted


def check_schur():
    tests = 0
    for n in range(1, 17):
        points = rows(n, 4)
        for k in (2, 3, 4):
            xs = points[:k]
            v = prod(xs[j]-xs[i] for i in range(k) for j in range(i+1, k))
            for ms in combinations(range(6), k):
                s = determinant(xs, ms) / v
                lam = [ms[k-1-i] - (k-i-1) for i in range(k)]
                z = prod(x**l for x,l in zip(xs, lam))
                b = [-vp(x, 3) for x in xs]
                dim = prod(Fraction(ms[j]-ms[i], j-i) for i in range(k) for j in range(i+1, k))
                require(dim.denominator == 1 and dim > 0, ("Weyl dimension", ms))
                require(s >= dim*z, ("positive tableau bound", n, ms))
                require(vp(s, 2) == vp(z, 2), ("dyadic determinant valuation", n, ms))
                require(-vp(s, 3) == sum(l*x for l,x in zip(lam,reversed(b))), ("triadic valuation", n, ms))
                gap = vp(z,3)-vp(s,3)
                lower = sum((lam[i-1]-lam[i])*i*(k-i) for i in range(1, k))
                require(gap >= lower, ("cubic denominator loss", n, ms))
                tests += 1
    return tests


def check_real_path(length):
    x = Fraction(-5)
    ones = b = 0
    next_denom = 1
    last_zero = None
    for i in range(length):
        r = -x-1
        bit = (1,1,0,1,1,0,0)[i] if i<7 else int(r < 1)
        if i in (0,3,6):
            require(x == -5, ("repeated real state", i))
        if i >= 7 and not bit:
            if last_zero is not None:
                require(i-last_zero >= 5, ("spacing of real branch bits", i))
            last_zero = i
        if bit:
            b = 3*b + 2**i
            x = (3*x+1)/2
            ones += 1
        else:
            x /= 2
        require(x == Fraction(3**ones*(-5)+b, 2**(i+1)), ("real affine identity", i))
        if i >= 6:
            next_denom *= 2
            require(x.denominator == next_denom and -Fraction(5,2) <= x < -1, ("bounded growing-denominator real state", i))
    return {"steps": length, "ones": ones, "terminal_denominator_exponent": length-6}


if __name__ == "__main__":
    print(json.dumps({"schur_cases": check_schur(), "real_path": check_real_path(1200)}, sort_keys=True))
