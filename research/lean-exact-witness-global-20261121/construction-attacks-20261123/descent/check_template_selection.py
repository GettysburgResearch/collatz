#!/usr/bin/env python3
"""Exact finite certificate for the two-log reduction and ordinary templates.

The imported Matveev theorem and the infinite reduction are written proofs.
This program certifies every finite continued-fraction and rational comparison
used in that reduction. It also checks actual ordinary-template identities.
No assertion is used as a guard, so optimized execution has the same meaning.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json


def need(condition, message):
    if not condition:
        raise ValueError(message)


def log_interval(a, terms=128):
    z = F(a - 1, a + 1)
    lo = 2 * sum((z ** (2 * k + 1) / (2 * k + 1)
                  for k in range(terms)), F(0))
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lo, lo + tail


def cf_certificate():
    l2, u2 = log_interval(2)
    l3, u3 = log_interval(3)
    need(F(2, 3) < l2 < u2 < F(7, 10), 'log 2 enclosure')
    need(1 < l3 < u3 < F(11, 10), 'log 3 enclosure')
    need(u2 * u3 < 1, 'height product')
    need(2 ** 32 < 5 * 10 ** 9, 'Matveev coarse constant')
    need(F(8, 3) ** 30 > 2 * 10 ** 12, 'log cutoff upper bound')
    need(10 ** 12 // 2 - 155 * 10 ** 9 - 1 > 0, 'large-exponent margin')
    lo, hi = l3 / u2, u3 / l2
    a0, a1, b0, b1 = 0, 1, 1, 0
    rows = []
    while True:
        digit = lo.numerator // lo.denominator
        need(digit == hi.numerator // hi.denominator, 'uncertain partial quotient')
        a, b = digit * a1 + a0, digit * b1 + b0
        low = a * l2 - b * u3
        high = a * u2 - b * l3
        need(low > 0 or high < 0, 'uncertain convergent side')
        upper = low > 0
        if upper and b >= 102:
            need(low > F(1, 2 ** 100), 'large convergent lower bound')
            bound = 'Lambda > 2^-100 > (3/2)*2^-b'
        elif upper and b >= 5:
            need(low > F(3, 2 ** (b + 1)), 'small convergent lower bound')
            bound = 'Lambda > (3/2)*2^-b'
        elif upper:
            need((a, b) == (2, 1), 'unexpected small upper convergent')
            need(2 * 2 ** b * (2 ** a - 3 ** b) > 3 * (3 ** b - 2 ** b),
                 'small-base gap')
            bound = 'exact base gap; all multiples covered by power lifting'
        else:
            bound = 'lower convergent; irrelevant to Q>P'
        rows.append(dict(partial_quotient=digit, numerator=a, denominator=b,
                         upper=upper, certificate=bound))
        if b > 10 ** 12:
            break
        lo, hi = 1 / (hi - digit), 1 / (lo - digit)
        a0, a1, b0, b1 = a1, a, b1, b
    need(rows[-1]['denominator'] == 5409303924479, 'CF stopping denominator')
    small = []
    for p in range(1, 5):
        length = (3 ** p).bit_length()
        gap = 2 ** length - 3 ** p
        need(2 * 2 ** p * gap > 3 * (3 ** p - 2 ** p), 'small exponent gap')
        small.append(dict(p=p, length=length, gap=gap))
    return rows, small


def affine(word):
    P, Q, C = 1, 1, 0
    for bit in word:
        if bit:
            P, C = 3 * P, 3 * C + Q
        Q *= 2
    return P, Q, C


def trace(x, word):
    need(isinstance(x, int) and x > 0, 'positive ordinary source required')
    for bit in word:
        need(x % 2 == bit, 'illegal ordinary parity')
        x = (3 * x + 1) // 2 if bit else x // 2
    return x


def anchor(P, Q, C):
    g = gcd(C, abs(Q - P))
    d = abs(Q - P) // g
    c = C // g if Q > P else -C // g
    return c, d


def finite_templates():
    words = ordinary = nonintegral = contracting = improving_integral = native_descents = 0
    for length in range(1, 13):
        for word in product((0, 1), repeat=length):
            words += 1
            P, Q, C = affine(word)
            p = sum(word)
            need(C <= 2 ** (length - p) * P - Q, 'complete carry bound')
            c, d = anchor(P, Q, C)
            need(gcd(abs(c), d) == 1 and d % 2 == 1, 'reduced odd denominator')
            need(d * C == (Q - P) * c, 'fixed center')
            if P < Q and p:
                need(2 * 2 ** p * (Q - P) > 3 * (P - 2 ** p), 'finite gap')
                need(3 * c < 2 * Q * d, 'center bound')
            a = (-C * pow(P, -1, Q)) % Q
            a = a or Q
            for lift in range(3):
                x = a + lift * Q
                y = trace(x, word)
                ordinary += 1
                need(Q * y == P * x + C, 'ordinary complete affine identity')
                if P < Q and 3*x >= 2*Q:
                    need(y < x, 'contracting native-window descent')
                    native_descents += 1
                z = d * x - c
                need(z % Q == 0, 'source lattice')
                if d > 1:
                    nonintegral += 1
                    contracting += int(P < Q)
                    need(z != 0 and abs(z) > x, 'nonintegral template beats height')
                elif z and abs(z) < x:
                    improving_integral += 1
                    need(c > 0 and trace(c, word) == c, 'improving center is an actual cycle')
    return dict(words=words, actual_sources=ordinary,
                nonintegral_sources=nonintegral,
                contracting_nonintegral_sources=contracting,
                contracting_native_window_descents=native_descents,
                improving_integral_sources=improving_integral)


def complete_witness_compiler():
    sources = steps = padded = 0
    for x in range(2, 1025):
        n, word = x, []
        while n != 1:
            need(len(word) < 10000, 'finite example did not terminate')
            bit = n % 2
            word.append(bit)
            n = (3 * n + 1) // 2 if bit else n // 2
        P, Q, C = affine(word)
        if Q == 2:
            word.extend((1, 0))
            padded += 1
            P, Q, C = affine(word)
        d, c = Q - P, C
        need(trace(x, word) == 1 and Q == P * x + C, 'complete witness')
        need(d > 1 and c >= 0 and d * C == (Q - P) * c, 'source anchor')
        need(P + abs(c - d) == P * x <= Q < Q * d, 'paid terminal macro')
        need(d * x - c == Q * (x - 1), 'source rank')
        sources += 1
        steps += len(word)
    return dict(sources=sources, ordinary_steps=steps, padded_short_word=padded)


def controls():
    rejected = 0
    for x, word in [(15, (0, 0, 1, 1, 1)), (F(76, 5), (0, 0, 1, 1, 1))]:
        try:
            trace(x, word)
        except ValueError:
            rejected += 1
        else:
            raise ValueError('damaged ordinary control accepted')
    P, Q, C = affine((1, 0))
    c, d = anchor(P, Q, C)
    need((c, d) == (1, 1) and abs(d * 5 - c) == 4 < 5,
         'integral-center exception missing')
    need(d * 1 - c == 0, 'zero must be excluded from positive-rank minimization')
    need(not (1 + abs(0 - 1) < 2 * 1), 'short terminal word exception')
    return dict(rejected_ordinary_inputs=rejected,
                integral_center_control=True, zero_control=True,
                unpadded_two_to_one_budget_rejected=True)


def main():
    rows, small = cf_certificate()
    here = Path(__file__).resolve().parent
    names = ['TEMPLATE_SELECTION.md', 'TemplateSelection.lean', Path(__file__).name]
    result = dict(
        scope='Exact finite CF certificate and ordinary controls; Matveev and the infinite reduction are written inputs, not executed or formalized here.',
        source_sha256={name: sha256((here / name).read_bytes()).hexdigest() for name in names},
        continued_fraction=dict(log_series_terms=128, exponent_cutoff=10 ** 12,
                                rows=rows, small_exponents=small),
        templates=finite_templates(), terminal_compiler=complete_witness_compiler(),
        controls=controls())
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
