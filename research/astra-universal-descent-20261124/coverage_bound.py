"""Exact constants for the infinite ordinary-source count in SHADOW_COVERAGE_LIMIT.md."""
from fractions import Fraction
from math import comb

def prefix_sum(last_clock):
    numerator = 0
    for s in range(1, last_clock + 1):
        first_d = 1
        while first_d <= s and 3 ** first_d <= 3 * 2 ** s:
            first_d += 1
        eligible = sum((comb(s - 1, d - 1) for d in range(first_d, s + 1)))
        numerator += eligible << last_clock - s
    return Fraction(numerator, 2 ** last_clock)

def check():
    finite = prefix_sum(400)
    if not finite < Fraction(1931, 1000):
        raise RuntimeError('Failed exact coverage-bound check at original line 21')
    q = Fraction(3, 2) ** 8 / 2 ** 5
    if not q == Fraction(6561, 8192):
        raise RuntimeError('Failed exact coverage-bound check at original line 23')
    tail = 8 * q ** 50 / (1 - q)
    if not tail < Fraction(1, 1000):
        raise RuntimeError('Failed exact coverage-bound check at original line 25')
    if not finite + tail < Fraction(1932, 1000):
        raise RuntimeError('Failed exact coverage-bound check at original line 26')
    print('finite exact:', finite)
    print('finite < 1931/1000; tail < 1/1000; total < 1932/1000')
    print('relative lower density > 17/500')
if __name__ == '__main__':
    check()
