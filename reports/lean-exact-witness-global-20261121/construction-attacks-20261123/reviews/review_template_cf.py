#!/usr/bin/env python3
"""Independent exact replay of TS-B's finite continued-fraction obligation.

This script does not import the author's checker, repeat the word census, or
claim to execute Matveev's theorem. Every guard survives python -O.
"""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


def require(value, label):
    if not value:
        raise ArithmeticError(label)


def enclosure(value):
    z = Fraction(value - 1, value + 1)
    current = z
    square = z * z
    partial = Fraction(0)
    for index in range(128):
        partial += current / (2 * index + 1)
        current *= square
    low = 2 * partial
    high = low + 2 * current / (257 * (1 - square))
    return low, high


def main():
    l2, u2 = enclosure(2)
    l3, u3 = enclosure(3)
    require(Fraction(2, 3) < l2 < u2 < Fraction(7, 10), 'log two')
    require(1 < l3 < u3 < Fraction(11, 10), 'log three')
    require(u2 * u3 < 1, 'height product')
    require(2**32 < 5 * 10**9, 'Matveev coarse coefficient')
    require(Fraction(8, 3)**30 > 2 * 10**12, 'cutoff logarithm')
    require(10**12 // 2 - 155 * 10**9 - 1 > 0, 'uniform large margin')
    require(2**5 > Fraction(9, 2) * 5, 'Legendre induction base')
    # If 2^p > (9/2)p and p>=1, doubling preserves the same inequality
    # at p+1 since 2p >= p+1. The manuscript uses p>=5.
    digits = [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1,
              1, 55, 1, 4, 3, 1, 1, 15, 1, 9, 2, 5, 7]
    lower, upper = l3 / u2, u3 / l2
    n_prevprev, n_prev = 0, 1
    d_prevprev, d_prev = 1, 0
    records = []
    for index, digit in enumerate(digits):
        require(digit < lower < upper < digit + 1, 'complete CF digit interval')
        numerator = digit * n_prev + n_prevprev
        denominator = digit * d_prev + d_prevprev
        require(abs(numerator * d_prev - n_prev * denominator) == 1,
                'primitive convergent determinant')
        gap_low = numerator * l2 - denominator * u3
        gap_high = numerator * u2 - denominator * l3
        require(gap_low > 0 or gap_high < 0, 'strict convergent sign')
        upper_convergent = gap_low > 0
        if upper_convergent:
            if denominator >= 102:
                require(gap_low > Fraction(1, 2**100), 'large upper lower bound')
                # Monotonicity reduces all denominator>=102 comparisons
                # to this one exact base comparison.
                require(Fraction(1, 2**100) > Fraction(3, 2**103),
                        'uniform exponential comparison')
                certificate = 'large_upper'
            elif denominator >= 5:
                require(gap_low > Fraction(3, 2**(denominator + 1)),
                        'small upper lower bound')
                certificate = 'small_upper'
            else:
                require((numerator, denominator) == (2, 1), 'only exceptional upper')
                require(Fraction(4 - 3) > Fraction(3, 2) * (Fraction(3, 2) - 1),
                        'exceptional upper base gap')
                certificate = 'power_lift_base'
        else:
            certificate = 'lower'
        if index < len(digits) - 1:
            require(denominator < 10**12, 'no earlier denominator reaches cutoff')
        else:
            require(d_prev == 753110839881 and denominator == 5409303924479,
                    'complete final cutoff bracket')
            require(d_prev < 10**12 < denominator, 'strict cutoff bracket')
        records.append({'index': index, 'digit': digit, 'numerator': numerator,
                        'denominator': denominator, 'upper': upper_convergent,
                        'certificate': certificate})
        lower, upper = 1 / (upper - digit), 1 / (lower - digit)
        n_prevprev, n_prev = n_prev, numerator
        d_prevprev, d_prev = d_prev, denominator
    small_uppers = [(row['numerator'], row['denominator']) for row in records
                    if row['upper'] and 5 <= row['denominator'] < 102]
    require(small_uppers == [(8, 5), (65, 41)], 'complete exceptional small uppers')
    for p, length, gap in [(1, 2, 1), (2, 4, 7), (3, 5, 5), (4, 7, 47)]:
        require(2**(length - 1) < 3**p < 2**length, 'minimal small length')
        require(2**length - 3**p == gap, 'small exact gap')
        require(gap > Fraction(3, 2) * (Fraction(3, 2)**p - 1), 'small target gap')
    root = Path(__file__).resolve().parents[4]
    source_dir = root / 'research/lean-exact-witness-global-20261121/construction-attacks-20261123/descent'
    hashes = {name: sha256((source_dir / name).read_bytes()).hexdigest()
              for name in ['TEMPLATE_SELECTION.md', 'check_template_selection.py',
                           'TemplateSelection.lean']}
    print(json.dumps({'scope': 'Independent exact finite CF replay only; no author checker imported, no word census repeated, no imported infinite theorem executed.',
                      'source_sha256': hashes, 'terms': 128, 'cutoff': 10**12,
                      'convergents': records, 'status': 'PASS'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
