#!/usr/bin/env python3
"""Exact independent checks of HP-001--005 and the Route 4 audit.

Standard library only. Uses explicit exceptions, so optimized Python retains
every check. Does not import the supplied Gemini verifier or repository code.
Bounded checks support the written general proofs; they do not prove Collatz.
"""

from fractions import Fraction as Q
from itertools import product
from math import comb, factorial, gcd, lcm, prod
import json


def need(ok, message):
    if not ok:
        raise ValueError(message)


def add(a, b):
    c = [Q(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return c


def mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def power(a, n):
    out = [Q(1)]
    for _ in range(n):
        out = mul(out, a)
    return out


def basis_vector_from_polynomial(coeffs, m):
    """R(Y)=sum P_i(z)Y^i with Y^m=1-z; exact change of basis."""
    result = [[] for _ in range(m)]
    for s, value in enumerate(coeffs):
        if not value:
            continue
        i, k = s % m, s // m
        term = [value * comb(k, h) * (-1)**h for h in range(k+1)]
        result[i] = add(result[i], term)
    return result


def substitute_basis(polynomials, m, sign=-1):
    """Return R(Y) after z=1-Y^m (sign=-1), or z=Y^m-1 (+1)."""
    z = [Q(-sign)] + [Q(0)]*(m-1) + [Q(sign)]
    result = []
    for i, p in enumerate(polynomials):
        for k, coefficient in enumerate(p):
            term = [Q(0)]*i + [coefficient*c for c in power(z, k)]
            result = add(result, term)
    return result


def binomial_series(exponent, order, sign):
    result = [Q(1)]
    for k in range(1, order+1):
        result.append(result[-1]*(exponent-k+1)*sign/k)
    return result


def series_form(polynomials, m, order, sign):
    result = []
    for i, p in enumerate(polynomials):
        result = add(result, mul(p, binomial_series(Q(i,m), order, sign)))
    return result[:order+1]


def determinant(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    result = Q(1)
    for c in range(len(a)):
        pivot = next((r for r in range(c, len(a)) if a[r][c]), None)
        if pivot is None:
            return Q(0)
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            result = -result
        p = a[c][c]
        result *= p
        for r in range(c+1, len(a)):
            factor = a[r][c]/p
            for s in range(c+1, len(a)):
                a[r][s] -= factor*a[c][s]
    return result


def norm(coeffs, m, r):
    matrix = [[Q(0)]*m for _ in range(m)]
    for column in range(m):
        for s, value in enumerate(coeffs):
            exponent = s+column
            matrix[exponent % m][column] += value*r**(exponent//m)
    return determinant(matrix)


def divide_one_root(coeffs):
    """Divide polynomial by Y-1 and fail if remainder is nonzero."""
    out = [Q(0)]*(len(coeffs)-1)
    out[-1] = coeffs[-1]
    for i in range(len(out)-2, -1, -1):
        out[i] = coeffs[i+1] + out[i+1]
    need(coeffs[0] == -out[0], "nonzero division remainder")
    return out


def primitive_normalize(coeffs):
    denominator = lcm(*(v.denominator for v in coeffs))
    integers = [int(v*denominator) for v in coeffs]
    common = gcd(*integers)
    return [Q(v//common) for v in integers]


def maximal_sparse(support):
    coeffs = [Q(0)]*(max(support)+1)
    for s in support:
        coeffs[s] = Q(1,prod(s-t for t in support if t != s))
    return coeffs


def alternant_at_ones(support):
    size = len(support)
    return Q(prod(support[j]-support[i] for i in range(size) for j in range(i+1,size)),
             prod(factorial(i) for i in range(size)))


def confluent_alternant(support):
    """Branching formula (13) at all variables except the last equal to one."""
    k = len(support)-1
    if not k:
        return [Q(0)]*support[0]+[Q(1)]
    result = [Q(0)]*(support[-1]-k+1)
    for r in product(*(range(support[i],support[i+1]) for i in range(k))):
        degree = sum(support)-sum(r)-k
        result[degree] += alternant_at_ones(r)
    return result


def odd_step(x):
    return (3*x+1)//2 if x % 2 else x//2


def word_data(word):
    q, c = 0, 0
    for j, b in enumerate(word):
        if b == "1":
            q += 1
            c = 3*c + 2**j
    return len(word), q, c


def main():
    prototype = [[Q(-27),Q(0),Q(28)], [Q(54),Q(54),Q(-8)],
                 [Q(-27),Q(-54),Q(1)]]
    binomial8 = power([Q(-1),Q(1)], 8)
    need(substitute_basis(prototype, 3, sign=1) == binomial8,
         "prototype is not the advertised exact binomial power")
    plus = series_form(prototype, 3, 8, 1)
    minus = series_form(prototype, 3, 8, -1)
    need(plus[:8] == [0]*8 and plus[8] == Q(1,6561), "plus-series order")
    need(minus[:2] == [0,0] and minus[2] == 36, "minus-series countercontrol")

    equal_count = 0
    norm_count = 0
    for m in range(2,8):
        for d in range(6):
            n = m*(d+1)-1
            coeffs = power([Q(-1),Q(1)], n)
            polynomials = basis_vector_from_polynomial(coeffs, m)
            need(all(len(p) <= d+1 for p in polynomials), "degree budget")
            need(substitute_basis(polynomials, m) == coeffs, "basis reconstruction")
            series = series_form(polynomials, m, n, -1)
            need(series[:n] == [0]*n and series[n] == Q(-1,m)**n,
                 "equal-budget series contact")
            equal_count += 1
            for r in [Q(3,2), Q(9,16), Q(27,32), Q(1), Q(0)]:
                need(norm(coeffs,m,r) == (((-1)**m)*(1-r))**n, "equal norm")
                norm_count += 1

    sparse_count = 0
    for m in range(2,5):
        for budgets in product(range(3), repeat=m):
            support = sorted(i+m*k for i,d in enumerate(budgets) for k in range(d+1))
            size = len(support)
            coeffs = maximal_sparse(support)
            for k in range(size):
                derivative = sum(coeffs[s]*prod(range(s-k+1,s+1)) for s in support)
                need(derivative == (1 if k == size-1 else 0), "sparse contact")
            quotient = coeffs[:]
            for _ in range(size-1):
                quotient = divide_one_root(quotient)
            need(sum(quotient) == Q(1,factorial(size-1)), "sparse leading coefficient")
            polynomials = basis_vector_from_polynomial(coeffs,m)
            need(all(len(p) <= budgets[i]+1 for i,p in enumerate(polynomials)),
                 "unequal degree budget")
            need(substitute_basis(polynomials,m) == coeffs, "unequal basis reconstruction")
            for r in [Q(9,16),Q(27,32)]:
                expected = (((-1)**m)*(1-r))**(size-1)*norm(quotient,m,r)
                need(norm(coeffs,m,r) == expected, "sparse norm factorization")
                norm_count += 1
            sparse_count += 1

    positivity_count = 0
    for mask in range(1,512):
        support = [0]+[i+1 for i in range(9) if (mask >> i)&1]
        k = len(support)-1
        coeffs = maximal_sparse(support)
        quotient = coeffs[:]
        for _ in range(k):
            quotient = divide_one_root(quotient)
        factor = alternant_at_ones(support)*factorial(k)
        need(confluent_alternant(support) == [factor*x for x in quotient],
             "confluent determinant identity")
        primitive = primitive_normalize(coeffs)
        for _ in range(k):
            primitive = divide_one_root(primitive)
        need(all(v.denominator == 1 and v >= 0 for v in primitive),
             "primitive residual is not a nonnegative integer polynomial")
        need(primitive[0] >= 1, "primitive residual constant")
        for y in [Q(0),Q(1,100),Q(1,2),Q(1),Q(7,3)]:
            need(sum(v*y**i for i,v in enumerate(primitive)) >= 1,
                 "no residual smallness")
        positivity_count += 1

    upper = [(8,5),(65,41),(485,306)]
    lower = [(1,1),(3,2),(19,12),(84,53),(1054,665)]
    need(all(2**p > 3**q for p,q in upper), "upper sides")
    need(all(2**p < 3**q for p,q in lower), "lower sides")
    first_crossing_count = 0
    for n in range(2,2001):
        x, q, c = n, 0, 0
        for j in range(1,1000):
            odd = x % 2
            if odd:
                q += 1
                c = 3*c + 2**(j-1)
            x = odd_step(x)
            need(2**j*x == 3**q*n+c, "forward affine identity")
            if 2**j > 3**q:
                need(x < n, "bounded first-crossing descent counterexample")
                first_crossing_count += 1
                break
        else:
            raise ValueError("finite first-crossing horizon exhausted")

    x, q, trace = 7, 0, [7]
    for _ in range(8):
        q += x % 2
        x = odd_step(x)
        trace.append(x)
    need(trace == [7,11,17,26,13,20,10,5,8], "paradoxical example replay")
    need(q == 5 and x > 7 and 3**q < 2**8, "paradoxical example coefficient")

    for length in range(1,101):
        x = 2**length-1
        for j in range(length):
            need(x % 2 == 1, "all-odd-prefix parity")
            need(x == 3**j*2**(length-j)-1, "all-odd-prefix identity")
            x = odd_step(x)

    need(word_data("1010") == (4,2,7), "integer cycle word")
    need(word_data("1100") == (4,2,5), "rational cycle word")
    print(json.dumps({
        "status":"PASS",
        "equal_budget_cases":equal_count,
        "unequal_budget_cases":sparse_count,
        "arbitrary_support_positivity_cases":positivity_count,
        "exact_norm_checks":norm_count,
        "first_crossing_descent_checked_range":"2..2000",
        "first_crossing_cases":first_crossing_count,
        "advertised_minus_prototype_first_nonzero_coefficient":{"degree":2,"coefficient":36},
        "true_plus_prototype":"((1+z)^(1/3)-1)^8",
        "all_odd_positive_prefix_lengths_checked":"1..100",
        "negative_controls":["unchanged prototype fails documented minus-series order", "arbitrary subcritical endpoint at n=7,j=8 does not descend", "three printed lower convergents have positive D"],
        "scope":"Exact bounded arithmetic checks; general classification is proved in the companion note. No universal Collatz or CST verification."
    },sort_keys=True,indent=2))


if __name__ == "__main__":
    main()
