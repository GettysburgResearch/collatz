"""Exact regression of C2/C3, including rotations and ordinary lifts."""
from fractions import Fraction
from math import gcd
from itertools import product

def affine(word):
    v, b, u = (1, 0, 1)
    for exponent in word:
        v, b, u = (3 * v, 3 * b + u, (1 << exponent) * u)
    return (v, b, u)

def check_case(i, b, modulus):
    word = [1] * i + [b]
    p = i + 1
    v, numerator, u = affine(word)
    d = u - v
    if not (d > 0 and gcd(2 * modulus, d) == 1):
        raise RuntimeError('Check failed at source line 19: d > 0 and gcd(2 * modulus, d) == 1')
    if not numerator == v - 2 ** p:
        raise RuntimeError('Check failed at source line 20: numerator == v - 2 ** p')
    root = Fraction(numerator, d)
    if not root > 1:
        raise RuntimeError('Check failed at source line 22: root > 1')
    if not root.denominator * u > d * 2 ** p:
        raise RuntimeError('Check failed at source line 23: root.denominator * u > d * 2 ** p')
    if not gcd(root.denominator, modulus) == 1:
        raise RuntimeError('Check failed at source line 24: gcd(root.denominator, modulus) == 1')
    if p <= 30:
        cyclic = word + word
        for start in range(p):
            for length in range(1, p):
                wv, wb, wu = affine(cyclic[start:start + length])
                if not wv != wu:
                    raise RuntimeError('Check failed at source line 32: wv != wu')
                candidate = Fraction(wb, wu - wv)
                if not (candidate < 0 or candidate.denominator > 1):
                    raise RuntimeError('Check failed at source line 34: candidate < 0 or candidate.denominator > 1')
    period = 2 * u * modulus
    start = numerator * pow(d, -1, period) % period + period
    x = start
    for exponent in word:
        product = 3 * x + 1
        if not product & -product == 2 ** exponent:
            raise RuntimeError('Check failed at source line 41: product & -product == 2 ** exponent')
        if exponent == 1:
            if not product // 2 > x:
                raise RuntimeError('Check failed at source line 43: product // 2 > x')
        x = product >> exponent
    if not (1 < x < start and x % modulus == start % modulus):
        raise RuntimeError('Check failed at source line 45: 1 < x < start and x % modulus == start % modulus')
    if not Fraction(v, u) < Fraction(x, start) < 1:
        raise RuntimeError('Check failed at source line 46: Fraction(v, u) < Fraction(x, start) < 1')
    return root

def check_complexity(max_period=10):
    count = 0
    comparisons = 0
    for period in range(2, max_period + 1):
        for bits in product((0, 1), repeat=period):
            rotations = {bits[i:] + bits[:i] for i in range(period)}
            if bits != min(rotations) or len(rotations) < period:
                continue
            power = 3 ** sum(bits)
            denominator = 2 ** period - power
            if denominator <= 0:
                continue
            offset = 0
            for i, odd in enumerate(bits):
                if odd:
                    offset = 3 * offset + 2 ** i
            value = Fraction(offset, denominator)
            phases = []
            for odd in bits:
                phases.append(value)
                if not value.numerator % 2 == odd:
                    raise RuntimeError('Check failed at source line 70: value.numerator % 2 == odd')
                value = (3 * value + 1) / 2 if odd else value / 2
            if not value == phases[0]:
                raise RuntimeError('Check failed at source line 72: value == phases[0]')
            minimum = min(phases)
            e, d = (minimum.numerator, minimum.denominator)
            count += 1
            for k in range(1, period):
                h = len({word[:k] for word in rotations})
                if h == period:
                    continue
                for s in range(h + 1):
                    t = h - s
                    if not 2 ** (k + t) <= max(2 ** t * (2 ** s - 1) * e, (3 ** t - 2 ** t) * (e + d)):
                        raise RuntimeError('Check failed at source line 82: 2 ** (k + t) <= max(2 ** t * (2 ** s - 1) * e, (3 ** t - 2 ** t) * (e + d))')
                    comparisons += 1
    return (count, comparisons)
if __name__ == '__main__':
    cases = [(4, 4, 25), (16, 11, 2 ** 5 * 3 ** 4), (40, 25, 2 ** 9 * 3 ** 5)]
    for i, b, modulus in cases:
        root = check_case(i, b, modulus)
        print(f'i={i} b={b} M={modulus} exact_root={root}')
    words, splits = check_complexity()
    print(f'C5.1 checked on {words} primitive positive cycles and {splits} splits')
