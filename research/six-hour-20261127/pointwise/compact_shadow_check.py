"""Exhaust all short strict-supercritical prefixes and separately their integer lifts."""

from fractions import Fraction
from math import gcd
import json


def shortcut(v):
    return (3 * v + 1) / 2 if v.numerator % 2 else v / 2


def critical_words(maximum):
    layer = [((), 0, 0)]
    for n in range(1, maximum + 1):
        children = []
        for bits, q, offset in layer:
            for b in (0, 1):
                if 3 ** (q + b) <= 1 << n:
                    continue
                new_offset = 3 * offset + (1 << (n - 1)) if b else offset
                children.append((bits + (b,), q + b, new_offset))
        layer = children
        yield n, layer


def run():
    periods = {}
    cycles = tests = 0
    reduced = 0
    largest_cancel = (1, None)
    for n, words in critical_words(15):
        counts = 0
        for bits, q, offset in words:
            raw_num = 3 ** q
            k = raw_num.bit_length() - n + 1
            N = n + k
            D = (1 << N) - raw_num
            start = Fraction(offset, D)
            d = start.denominator
            assert gcd(d, 6) == 1
            intercept = Fraction(offset, raw_num)
            assert Fraction(1, 9) < start <= intercept
            z = start
            path = set()
            for b in bits + (0,) * k:
                assert z.denominator == d and z > 0 and z.numerator % 2 == b
                path.add(z)
                z = shortcut(z)
            assert z == start
            if k <= n:
                assert len(path) == N
                counts += 1
            cycles += 1
            reduced += d < D
            factor = D // d
            if factor > largest_cancel[0]:
                largest_cancel = factor, ''.join(map(str, bits))
            # Two independent ordinary lifts, including the least lift.
            modulus = 1 << n
            m = (-offset * pow(raw_num, -1, modulus)) % modulus or modulus
            for x in (m, m + modulus):
                y = Fraction(x)
                for bit in bits:
                    assert y.denominator == 1 and y.numerator % 2 == bit
                    y = shortcut(y)
                assert y.denominator == 1
                assert D // gcd(D, y.numerator - (x << k)) == d
                diff = start.numerator - x * d
                assert diff % modulus == 0
                if diff:
                    assert d * (x + start) >= modulus
                tests += 1
        periods[n] = counts
    return dict(critical_prefixes=cycles, certified_primitive_by_horizon=periods,
                ordinary_lift_checks=tests, nontrivial_reductions=reduced,
                largest_removed_factor=largest_cancel[0],
                prefix_at_largest=largest_cancel[1])


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
