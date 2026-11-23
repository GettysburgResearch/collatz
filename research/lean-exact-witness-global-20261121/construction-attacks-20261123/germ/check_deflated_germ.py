#!/usr/bin/env python3
"""Exact finite controls for the density-free deflated-germ criterion.

The external analytic theorem, actual infinite germ, and universal
construction are not simulated by this checker. Guards remain active under -O.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import comb
from pathlib import Path
import json


def need(condition, message):
    if not condition:
        raise ValueError(message)


def trim(a):
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def add(a, b):
    c = [Q(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return trim(c)


def mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def shift_two(a):
    c = [Q(0)] * len(a)
    for i, x in enumerate(a):
        for j in range(i + 1):
            c[j] += x * comb(i, j) * 2 ** (i - j)
    return trim(c)


def actual_word(n):
    need(isinstance(n, int) and n > 0, 'positive ordinary source required')
    x, word = n, []
    while x != 1:
        need(len(word) < 10000, 'selected finite control did not terminate')
        e = x % 2
        word.append(e)
        x = (3 * x + 1) // 2 if e else x // 2
    return word


def backward_germ(word):
    k = [Q(-1)]
    for e in reversed(word):
        k = add(mul([Q(2), Q(1)], k), [Q(e), Q(4 * e), Q(e)])
        if e:
            k = [c / 3 for c in k]
    return trim(k)


def prefix_germ(word):
    s = sum(word)
    p = 0
    c = [Q(0)] * max(1, len(word))
    for i, e in enumerate(word):
        p += e
        if e:
            c[i] = Q(3 ** (s - p))
    z_tau = [Q(0)] * len(word) + [Q(-1)]
    f = add(mul([Q(-3), Q(0), Q(1)], c), z_tau)
    return trim([v / 3 ** s for v in shift_two(f)])


def log_interval(a, terms=96):
    a = Q(a)
    need(a > 1, 'log enclosure needs argument greater than one')
    z = (a - 1) / (a + 1)
    lo = 2 * sum((z ** (2 * i + 1) / (2 * i + 1)
                  for i in range(terms)), Q(0))
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lo, lo + tail


def capacity_controls():
    lo2, hi2 = log_interval(2)
    lo32, hi32 = log_interval(Q(3, 2))
    left_lower = (3 * lo2 - 4 * hi32) / 5
    right_lower = (2 * lo2 - 3 * hi32) / 5
    need(left_lower > 0 and right_lower > 0, 'strict strategy margin')
    need(left_lower > Q(9, 100) and right_lower > Q(3, 100), 'rational margin floors')
    need(Q(4, 3) ** 2 < 3 and Q(4, 3) + Q(2, 3) == 2, 'complex geometry')
    for b in [Q(51, 100), Q(11, 20), Q(2, 3), Q(9, 10)]:
        a_hi = log_interval(3 / (2 - b))[1]
        b_hi = log_interval(1 / b)[1]
        need(a_hi * b_hi < lo2 * lo2, 'finite radius-threshold control')
    b = Q(49, 100)
    a_lo = log_interval(3 / (2 - b))[0]
    b_lo = log_interval(1 / b)[0]
    need(a_lo * b_lo > hi2 * hi2, 'below-threshold matrix control')
    return dict(log_series_terms=96, explicit_strategy=['2/5', '3/5'],
                certified_payoff_floors=['9/100', '3/100'],
                strict_radius_controls=4, below_threshold_control=True)


def main():
    seeds = sorted(set(range(1, 129)) | {129, 257, 385, 3 ** 27 + 1}
                   | {2 ** j for j in range(1, 21)}
                   | {3 ** j + 1 for j in range(1, 13)})
    coefficient_checks = ordinary_steps = 0
    max_degree = 0
    for n in seeds:
        word = actual_word(n)
        k = backward_germ(word)
        need(k == prefix_germ(word), 'independent deflated polynomial mismatch')
        need(k[0] == -n, 'actual binary constant')
        s = sum(word)
        need(all((3 ** s * c).denominator == 1 for c in k), 'common ternary denominator')
        x = n
        p = 0
        for j, e in enumerate(word, 1):
            need(x % 2 == e, 'literal parity')
            x = (3 * x + 1) // 2 if e else x // 2
            p += e
            need(1 <= x and 2 ** j * x <= n * 4 ** p, 'positive-source radius bound')
        coefficient_checks += len(k)
        ordinary_steps += len(word)
        max_degree = max(max_degree, len(k) - 1)
    inverse = [1, -4]
    for j in range(62):
        inverse.append(-4 * inverse[-1] - inverse[-2])
    product = mul([Q(1), Q(4), Q(1)], list(map(Q, inverse)))
    need(product[0] == 1 and all(c == 0 for c in product[1:64]), 'integer inverse')
    actual85 = backward_germ(actual_word(85))
    need(actual85[0] == -85 and actual85[1] == -340, 'retained derivative-zero control')
    need(actual85 != [Q(-85)], 'constant-only fitted germ falsely accepted')
    need(Q(1, 5).denominator % 3 != 0 and Q(1, 5).denominator != 1,
         'foreign-prime coefficient control')
    here = Path(__file__).resolve().parent
    files = ['DENSITY_FREE_DEFLATED_GERM.md', 'GermCapacity.lean', Path(__file__).name]
    result = dict(
        scope='Exact finite capacity and known-convergent actual-germ controls; not the analytic rationality theorem or a universal germ construction.',
        source_sha256={f: sha256((here / f).read_bytes()).hexdigest() for f in files},
        capacity=capacity_controls(),
        actual_germs=dict(sources=len(seeds), ordinary_steps=ordinary_steps,
                          coefficient_equalities=coefficient_checks, maximum_degree=max_degree,
                          inverse_coefficients=64),
        controls=dict(fitted_constant_rejected=True, foreign_prime_rejected=True,
                      old_derivative_zero_fixture_retained=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
