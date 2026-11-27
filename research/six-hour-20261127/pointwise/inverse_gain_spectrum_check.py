"""Exact positive odd inverse-gain superlevel census using two forward methods."""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json


def odd_step(x):
    y = 3 * x + 1
    e = (y & -y).bit_length() - 1
    return y >> e, e


def improved(rows, target, numerator, denominator, source):
    current = rows.get(target)
    if current is None or numerator * current[1] > current[0] * denominator:
        rows[target] = (numerator, denominator, source)


def stopped_search(bound):
    rows = {}
    reasons = Counter()
    largest_clock = 0
    for source in range(1, bound + 1, 2):
        numerator = denominator = 1
        x = source
        seen = set()
        while x not in seen and numerator * bound >= x * denominator:
            improved(rows, x, numerator, denominator, source)
            seen.add(x)
            x, e = odd_step(x)
            numerator *= 3
            denominator <<= e
        reasons['repetition' if x in seen else 'below_threshold'] += 1
        largest_clock = max(largest_clock, len(seen))
    return rows, dict(reasons), largest_clock


def complete_search(bound):
    rows = {}
    steps = 0
    greatest_height = 1
    for source in range(1, bound + 1, 2):
        odd_part = source
        affine_numerator = source
        forward_numerator = divisor = 1
        seen = set()
        while True:
            assert odd_part not in seen
            seen.add(odd_part)
            steps += 1
            greatest_height = max(greatest_height, odd_part)
            assert affine_numerator == odd_part * divisor
            if affine_numerator <= bound * forward_numerator:
                improved(rows, odd_part, forward_numerator, divisor, source)
            if odd_part == 1:
                break
            affine_numerator = 3 * affine_numerator + divisor
            forward_numerator *= 3
            odd_part = 3 * odd_part + 1
            while odd_part % 2 == 0:
                odd_part //= 2
                divisor *= 2
    return rows, steps, greatest_height


def report(bound):
    first, reasons, longest = stopped_search(bound)
    second, visits, greatest = complete_search(bound)
    assert first == second
    assert all(z in first for z in range(1, bound + 1, 2))
    assert all(0 < n <= z * d and v * n <= z * d <= bound * n
               for z, (n, d, v) in first.items())
    # Every nonempty path ends at an odd unit modulo three.
    assert all(n == d == 1 and v == z for z, (n, d, v) in first.items() if z % 3 == 0)
    digest = sha256()
    for z, (n, d, v) in sorted(first.items()):
        digest.update(f'{z} {n} {d} {v}\n'.encode())
    z = max(first)
    n, d, v = first[z]
    return {
        'B': bound,
        'odd_sources': (bound + 1) // 2,
        'distinct_global_superlevel_targets': len(first),
        'targets_above_B': sum(z > bound for z in first),
        'true_largest_superlevel_target': z,
        'maximizing_source_at_largest': v,
        'exact_G_at_largest': str(Fraction(n, d)),
        'threshold_search_final_causes': reasons,
        'longest_stopped_seed_search': longest,
        'complete_search_visits_including_endpoints': visits,
        'complete_search_largest_odd_height': greatest,
        'table_sha256': digest.hexdigest(),
    }


if __name__ == '__main__':
    print(json.dumps([report(b) for b in (1, 31, 511, 4095, 65535)], indent=2))
