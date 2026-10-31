#!/usr/bin/env python3
"""Rigorous dyadic enclosures of every ternary Syracuse cylinder density.

Standard library only. No floating point is used in a certified bound.
The two backward sweeps solve the complete geometric law, not a truncated
exponent sum. Run --max-level 14 --precision 50 for the published large census.
"""
from __future__ import annotations
import argparse
from array import array
from fractions import Fraction
import hashlib
import json
from pathlib import Path

MAX_I64 = (1 << 63) - 1

def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)

def inverse_double(r: int, modulus: int) -> int:
    return (r + (modulus if r & 1 else 0)) // 2

def sweep(lo: array, hi: array, start_lo: int, start_hi: int,
          store: bool) -> tuple[int, int, array | None, array | None]:
    m = len(lo)
    modulus, period = 3 * m, 2 * m
    out_lo = array('q', [0]) * modulus if store else None
    out_hi = array('q', [0]) * modulus if store else None
    r = (modulus + 1) // 2
    low, high = start_lo, start_hi
    for _ in range(period):
        if r % 3 == 2:
            index = ((2 * r - 1) // 3) % m
            low = (low + 3 * lo[index]) // 2
            high = (high + 3 * hi[index] + 1) // 2
        else:
            low //= 2
            high = (high + 1) // 2
        if store:
            out_lo[r], out_hi[r] = low, high
        r = inverse_double(r, modulus)
    require(r == (modulus + 1) // 2, 'complete doubling cycle')
    return low, high, out_lo, out_hi

def step(lo: array, hi: array) -> tuple[array, array]:
    require(len(lo) == len(hi), 'interval shape')
    require(max(hi) <= (MAX_I64 - 3) // 6, 'signed-64-bit storage headroom')
    period = 2 * len(lo)
    low, high, _, _ = sweep(lo, hi, 0, 0, False)
    if period < 64:
        power = 1 << period
        denominator = power - 1
        start_lo = low * power // denominator
        start_hi = (high * power + denominator - 1) // denominator
    else:
        # high <= 2^63-1 < 2^period-1, so the exact upper correction is <= 1.
        require(high <= MAX_I64, 'cyclic correction headroom')
        start_lo, start_hi = low, high + 1
    _, _, out_lo, out_hi = sweep(lo, hi, start_lo, start_hi, True)
    require(out_lo is not None and out_hi is not None, 'stored sweep')
    return out_lo, out_hi

def outward_decimal(x: Fraction, places: int, upward: bool = False) -> str:
    scale = 10 ** places
    numerator = x.numerator * scale
    v = (numerator + x.denominator - 1) // x.denominator if upward else numerator // x.denominator
    sign = '-' if v < 0 else ''
    v = abs(v)
    return f'{sign}{v // scale}.{v % scale:0{places}d}'

def interval_summary(low: Fraction, high: Fraction) -> dict:
    require(low <= high, 'ordered rational interval')
    return {'lower': str(low), 'upper': str(high),
            'outward_decimal_12': [outward_decimal(low, 12), outward_decimal(high, 12, True)]}

def hash_integers(values: array) -> str:
    # Portable canonical little-endian encoding, independent of host byte order.
    import sys
    view = values
    if sys.byteorder != 'little':
        view = array('q', values)
        view.byteswap()
    return hashlib.sha256(view.tobytes()).hexdigest()

def run(max_level: int, precision: int) -> tuple[dict, array, array]:
    require(1 <= max_level <= 15, 'supported finite level range')
    require(1 <= precision <= 50, 'supported fixed-point precision')
    scale = 1 << precision
    lo, hi = array('q', [scale]), array('q', [scale])
    previous_low = previous_high = Fraction(1)
    rows = []
    total_residues = 0
    for q in range(1, max_level + 1):
        lo, hi = step(lo, hi)
        size = len(lo)
        low_square = high_square = low_sum = high_sum = width = 0
        min_low = min_high = MAX_I64
        max_low = max_high = 0
        for r, (left, right) in enumerate(zip(lo, hi)):
            require(0 <= left <= right <= MAX_I64, 'valid stored interval')
            require(r % 3 != 0 or (left == 0 and right == 0), 'exact nonunit zero')
            low_sum += left
            high_sum += right
            low_square += left * left
            high_square += right * right
            width = max(width, right - left)
            if r % 3:
                min_low, min_high = min(min_low, left), min(min_high, right)
                max_low, max_high = max(max_low, left), max(max_high, right)
        require(low_sum <= size * scale <= high_sum, 'mean-one enclosure')
        lower = Fraction(low_square, size * scale * scale)
        upper = Fraction(high_square, size * scale * scale)
        increment_low, increment_high = lower - previous_high, upper - previous_low
        require(increment_low > 0, 'strictly positive certified finite increment')
        rows.append({'q': q, 'residues': size,
                     'energy': interval_summary(lower, upper),
                     'increment': interval_summary(increment_low, increment_high),
                     'unit_minimum': interval_summary(Fraction(min_low, scale), Fraction(min_high, scale)),
                     'maximum': interval_summary(Fraction(max_low, scale), Fraction(max_high, scale)),
                     'largest_interval_width_units': width,
                     'lower_array_sha256_le_i64': hash_integers(lo),
                     'upper_array_sha256_le_i64': hash_integers(hi)})
        previous_low, previous_high = lower, upper
        total_residues += size
    payload = {'status': 'PASS', 'max_level': max_level, 'precision_bits': precision,
               'total_residues_enclosed': total_residues, 'rows': rows,
               'arithmetic': 'Python integers; signed 64-bit array storage; rational outward bounds',
               'floating_point_used_for_bounds': False,
               'geometric_exponent_tail_truncated': False,
               'asymptotic_linear_energy_proved': False, 'Collatz_proved': False}
    canonical = json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()
    return {'payload': payload, 'semantic_sha256': hashlib.sha256(canonical).hexdigest()}, lo, hi

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-level', type=int, default=8)
    parser.add_argument('--precision', type=int, default=50)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report, _, _ = run(args.max_level, args.precision)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'semantic_sha256': report['semantic_sha256'],
                      'residues': report['payload']['total_residues_enclosed'],
                      'last_energy': report['payload']['rows'][-1]['energy']['outward_decimal_12']}))

if __name__ == '__main__':
    main()
