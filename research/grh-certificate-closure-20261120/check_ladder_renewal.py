#!/usr/bin/env python3
"""Exact finite checks for complete-ladder energy renewal, not a full closure."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def odd_step(n: int) -> tuple[int, int]:
    need(type(n) is int and n > 0 and n % 2 == 1, 'positive odd input')
    y = 3*n+1
    power = (y & -y).bit_length()-1
    return y >> power, power


def block_end(n: int, exponents: list[int]) -> int:
    for expected in exponents:
        n, actual = odd_step(n)
        need(actual == expected, 'literal block exponent')
    return n


def run() -> dict:
    counts = {'inverse_progressions': 0, 'source_members': 0,
              'unit_members': 0, 'nonunit_members_dropped': 0,
              'positive_geometric_comparisons': 0,
              'nontrivial_endpoint_bounds': 0}
    for r in range(1, 9):
        modulus, period = 3**(r+1), 2*3**r
        logs, power = {}, 1
        for a in range(period):
            need(power not in logs, 'exact multiplicative order before period')
            logs[power] = a
            power = 2*power % modulus
        need(power == 1, 'complete multiplicative order')
        for q in range(1, 41, 2):
            if q % 3 == 0:
                continue
            b0 = 2+logs[pow(q, -1, modulus)]
            if b0 < 4:
                b0 += period
            need(4 <= b0 < 4+period, 'least allowed exponent in its progression')
            need(pow(2, b0-2, modulus)*q % modulus == 1, 'source congruence')
            correction = 4**(r+1)-3**(r+1)
            first = previous = None
            for k in range(3):
                b = b0+k*period
                numerator = (q << (2*r+b))-correction
                need(numerator % modulus == 0, 'whole inverse integrality')
                x = numerator//modulus
                need(x > 1 and x % 2, 'positive odd inverse source')
                need(block_end(x, [2]*r+[b]) == q, 'actual source endpoint')
                target = [5, b-3] if r == 1 else [4]+[2]*(r-2)+[3, b-3]
                need(block_end(5*x, target) == 5*q, 'actual paired endpoint')
                need(7*q <= x, 'finite cutoff endpoint lies below X/7')
                need(3**r*x >= 4**(r+1)*q, 'harmonic initial-height coefficient')
                if q >= 5:
                    need(15*3**r*x >= 76*4**r*q, 'subcritical initial-height coefficient')
                    counts['nontrivial_endpoint_bounds'] += 1
                if previous is not None:
                    need(x >= previous << period, 'positive geometric comparison')
                    need(3**(r+1)*(x-(previous << period)) == ((1 << period)-1)*correction,
                         'exact positive correction in the inverse fiber')
                    counts['positive_geometric_comparisons'] += 1
                first = x if first is None else first
                need(x >= first << (k*period), 'complete geometric comparison')
                if x % 3:
                    counts['unit_members'] += 1
                else:
                    counts['nonunit_members_dropped'] += 1
                previous = x
                counts['source_members'] += 1
            counts['inverse_progressions'] += 1

    harmonic = Fraction(1, 4)*Fraction(3, 4)/(1-Fraction(3, 4))/(1-Fraction(1, 64))
    need(harmonic == Fraction(16, 21), 'exact infinite geometric majorant')
    need(odd_step(5) == (1, 4), 'zero defect at endpoint one')
    need(15**21*50**25 < 76**21*13**25, 'first subcritical rational bound')
    need(3**21*500**25 < 4**21*393**25, 'second subcritical rational bound')
    need(6*21 > 5*25, 'dyadic subcritical bound')
    subcritical = Fraction(13, 50)*Fraction(393, 107)*Fraction(32, 31)
    need(subcritical == Fraction(81744, 82925) and subcritical < 1,
         'exact subcritical contraction')
    need(1/(1-subcritical) == Fraction(82925, 1181), 'truncated energy rearrangement')
    return {'status': 'PASS', 'counts': counts,
            'harmonic_coefficient_bound': str(harmonic),
            'subcritical_exponent': '21/25',
            'subcritical_coefficient_bound': str(subcritical),
            'scope': 'Exact inverse fibers, ordinary paired endpoints and rational bounds; universal renewal relies on the written proof; no bound on the uncovered energy.',
            'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    raw = json.dumps(run(), sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.write_text(raw, encoding='utf-8')
    print(raw, end='')
