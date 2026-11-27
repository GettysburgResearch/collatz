#!/usr/bin/env python3
"""Exact finite cross-checks for the written staircase proofs."""
from fractions import Fraction as F
from itertools import product
from math import comb
import json


def tri(n):
    return n * (n - 1) // 2


def integer_order(x):
    assert x != 0
    return (x & -x).bit_length() - 1


def order(x):
    return integer_order(x.numerator) - integer_order(x.denominator)


def size(x):
    return max(abs(x.numerator), x.denominator)


def residue(x, modulus):
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def affine(word):
    carry = 0
    for clock, bit in enumerate(word):
        if bit == "1":
            carry = 3 * carry + 2**clock
    odds = word.count("1")
    return F(2**len(word), 3**odds), F(-carry, 3**odds)


def root(word):
    slope, offset = affine(word)
    return offset / (1 - slope)


def prefix(x, length):
    bits = []
    for _ in range(length):
        bit = x % 2
        bits.append(str(bit))
        x = ((3 * x + 1) if bit else x) // 2
    return "".join(bits), x


def polynomial_product(factors):
    coeff = [1]
    for constant, linear in factors:
        coeff = [constant * coeff[0],
                 *(constant * coeff[i] + linear * coeff[i - 1] for i in range(1, len(coeff))),
                 linear * coeff[-1]]
    return coeff


def polynomial_value(coeff, x):
    y = 0
    for c in reversed(coeff):
        y = y * x + c
    return y


def tau(q, z, N):
    return sum((z**j / q**tri(j) for j in range(N)), F(0))


def native_tests():
    words = ["".join(bits) for n in range(5) for bits in product("01", repeat=n)]
    noncommuting = commuting = 0
    for v in words[1:]:
        a, _ = affine(v)
        b = root(v)
        q = 1 / a
        for u in words:
            e, f = affine(u)
            d, z = e * b + f - b, a * e
            assert (d == 0) == (u + v == v + u)
            noncommuting += bool(d)
            commuting += not d
            for K in (2, 5, 9):
                directive = "".join(v * j + u for j in range(K))
                H = len(directive)
                expected = residue(b + d * tau(q, z, K), 2**H)
                # A positive cylinder lift and actual integer endpoints.
                x = expected + 2**H
                bits, y = prefix(x, H)
                assert bits == directive
                assert x == b + d * tau(q, z, K) + e**K * a**tri(K) * (y - b)
    return {"noncommuting_pairs": noncommuting, "commuting_pairs": commuting,
            "positive_cylinder_tests": 3 * (noncommuting + commuting)}


def pade_tests():
    tests = 0
    for v, p in ((1, 0), (1, 1), (3, 2), (5, 1), (5, 5)):
        q = F(3**p, 2**v)
        for z in (F(2**(v+1), 3**(p+1)), F(-6, 5), F(7, 2)):
            w = order(z)
            for n in range(2, 8):
                coeff = polynomial_product([(1, -q**j) for j in range(1, n + 1)])
                for m in sorted({n, (2 * n) // 3, 0}):
                    if v * (n + m) + w <= 0:
                        continue
                    B = sum(c / z**k * q**(tri(k)+k*m) for k, c in enumerate(coeff))
                    A = sum(c / z**k * q**(tri(k)+k*m) * tau(q, z, m+k+1)
                            for k, c in enumerate(coeff))
                    assert order(B) == -v*n*(m+n) - n*w
                    expected = v*(n*(n+m) + tri(n+m+1)) + (2*n+m+1)*w
                    t = tau(q, z, 3*n+2*m+10)
                    assert order(t-A/B) == expected
                    bound = ((m+n+1)*2**n*max(q.numerator,q.denominator)**(tri(m)+n*(n+m))
                             * size(z)**(2*n))
                    assert size(A/B) <= bound
                    # Check the finite blockwise identity independently of the first-term valuation.
                    for s in (1, n, n+1, n+3):
                        term = lambda k: z**k / q**tri(k)
                        folded = sum(c / z**k * q**(tri(k)+k*m) * term(m+s+k)
                                     for k, c in enumerate(coeff))
                        assert folded == polynomial_value(coeff, q**(-s)) * term(m+s)
                    tests += 1
    assert 3**80 < 2**127
    assert 3**340 < 2**539
    return {"pade_parameter_tests": tests, "matching_term_checks": 4 * tests,
            "integer_threshold_checks": 2}


def multiphase_tests():
    tests = active_counts = 0
    for growing, separators in [
        (["1", "10"], ["", ""]),
        (["1", "0", "11"], ["1", "01", "0"]),
        (["11", "1", "101"], ["01", "00", "10"]),
        (["00", "11", "10", "1"], ["01", "11", "0", "101"]),
        (["1011", "00"], ["1", "11"]),
    ]:
        vs, us = [affine(w)[0] for w in growing], [affine(w)[0] for w in separators]
        roots = [root(w) for w in growing]
        A, q = F(1), F(1)
        for v, u in zip(vs, us, strict=True):
            A *= u
            q /= v
        c, z = [], []
        prod_u, prod_v = F(1), F(1)
        for i, (v, u, word) in enumerate(zip(vs, us, separators, strict=True)):
            delta = u * roots[(i + 1) % len(roots)] + affine(word)[1] - roots[i]
            prod_v *= v
            if delta:
                c.append(prod_u * delta)
                z.append(A * prod_v)
            prod_u *= u
        H = -order(q)
        assert c and all(order(a)<order(b) for a,b in zip(z,z[1:]))
        assert order(z[-1])-order(z[0]) < H
        active_counts += len(c)
        for K in (3, 8):
            directive = "".join("".join(w*j + u for w, u in zip(growing, separators, strict=True))
                                for j in range(K))
            value = roots[0] + sum(h*tau(q, point, K) for h, point in zip(c,z,strict=True))
            x = residue(value, 2**len(directive)) + 2**len(directive)
            bits, _ = prefix(x, len(directive))
            assert bits == directive
        for n in range(3, 8):
            ell = len(c)
            poly = polynomial_product([(-point.numerator * q.denominator**j,
                                        point.denominator * q.numerator**j)
                                       for point in z for j in range(n)])
            for m in (0, n, 2*n):
                if any(order(c[i]) + (m+n)*order(z[i]) <= order(c[0])+(m+n)*order(z[0])
                       for i in range(1,ell)):
                    continue
                # A long rational truncation determines every valuation being tested.
                Q = 3 * (m + ell*n + n + 6)
                sample = sum(h*tau(q, point, Q) for h,point in zip(c,z,strict=True))
                def Y(j):
                    return q**tri(j) * (sample-sum(h*tau(q, point, j)
                                                  for h,point in zip(c,z,strict=True)))
                observed = sum(b*Y(m+j) for j,b in enumerate(poly))
                expected = (H*((ell+1)*tri(n)+m*n) + n*sum(integer_order(k.numerator) for k in z)
                            + (m+n)*order(z[0]) + order(c[0]))
                assert order(observed) == expected
                tests += 1
    return {"multiphase_template_count": 5, "total_active_phases": active_counts,
            "exact_leading_order_checks": tests, "positive_multiphase_prefix_tests": 10}


if __name__ == "__main__":
    print(json.dumps({"status": "PASS", "scope": "finite exact arithmetic checks",
                      **native_tests(), **pade_tests(), **multiphase_tests()},
                     indent=2))
