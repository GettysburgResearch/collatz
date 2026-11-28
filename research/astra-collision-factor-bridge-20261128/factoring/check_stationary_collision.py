#!/usr/bin/env python3
"""Independent exact finite consumer for the joint stationary collision formula.

No stationary simulation or asymptotic claim is made. Arbitrary rational real
seeds and integer ternary seeds test the deterministic interface: native words,
the full-conductor selector, complete shifted laws, and the two-copy cell.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def native(n: int, h: int):
    tape = []
    for _ in range(h):
        odd = n % 2
        tape.append(odd)
        n = (3 * n + 1) // 2 if odd else n // 2
    return tuple(tape), n


def floor(q: Fraction) -> int:
    return q.numerator // q.denominator


def endpoint_law(h: int, size: int, shift: int):
    result = Counter()
    for n in range(shift + 1, shift + size + 1):
        tape, y = native(n, h)
        result[sum(tape), y] += 1
    return result


def cells(h: int, size: int, seed: Fraction, zseed: int, words):
    modulus = 3 ** h
    inv2 = pow(2, -1, modulus) if modulus > 1 else 0
    result, law = [], Counter()
    for tape in words:
        real, ternary = seed, zseed % modulus
        for odd in tape:
            real = (3 * real + 1) / 2 if odd else real / 2
            ternary = ((3 * ternary + 1) if odd else ternary) * inv2 % modulus
        grade = sum(tape)
        q = 3 ** grade
        residue = ternary % q
        length = Fraction(q * size, 2 ** h)
        first = floor((real - residue) / q) + 1
        last = floor((real + length - residue) / q)
        endpoints = tuple(residue + q * j for j in range(first, last + 1))
        for y in endpoints:
            require(y > 0, 'Selected endpoint is not positive')
            law[grade, y] += 1
        result.append((q, residue, real, real + length, endpoints))
    require(law == endpoint_law(h, size, floor(seed)),
            'Full joint selector differs from native shifted source law')
    require(sum(law.values()) == size, 'One-copy selector mass differs from X')
    return result, law


def common_cell(left, right):
    q, r, lo, hi, ys = left
    qq, rr, llo, hhi, yys = right
    if (r - rr) % min(q, qq):
        count = 0
    else:
        modulus, residue = (q, r) if q >= qq else (qq, rr)
        lower, upper = max(lo, llo), min(hi, hhi)
        count = max(0, floor((upper - residue) / modulus)
                    - floor((lower - residue) / modulus))
    require(count == len(set(ys).intersection(yys)),
            'Arithmetic intersection differs from explicit endpoint intersection')
    return count


def marginal(law):
    result = Counter()
    for (_, y), count in law.items():
        result[y] += count
    return result


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    seeds = [Fraction(0), Fraction(1, 2), Fraction(1),
             Fraction(11, 3), Fraction(898, 7)]
    law_checks = pair_checks = intersections = indicator_checks = 0
    rows = []
    for h in range(7):
        words = [native(n, h)[0] for n in range(2 ** h)]
        require(len(set(words)) == 2 ** h, 'Native words are not a full census')
        for size in sorted({1, 3, 2 ** h, 2 ** h + 1}):
            base = endpoint_law(h, size, 0)
            data = []
            for index, seed in enumerate(seeds):
                cell, law = cells(h, size, seed, 17 - 31 * index, words)
                keys = set(base) | set(law)
                tv = Fraction(sum(abs(law[k] - base[k]) for k in keys), 2 * size)
                require(tv <= Fraction(min(floor(seed), size), size),
                        'Joint-law TV exceeds the source-window bound')
                data.append((cell, marginal(law)))
                law_checks += 1
            for i, (left, law) in enumerate(data):
                for j, (right, other) in enumerate(data):
                    total = 0
                    for l in left:
                        for r in right:
                            count = common_cell(l, r)
                            total += count
                            intersections += 1
                            if size <= 2 ** h:
                                require(count in (0, 1), 'Small cell is not an indicator')
                                indicator_checks += 1
                    direct = sum(count * other.get(y, 0) for y, count in law.items())
                    require(total == direct, 'Two-copy trace differs from native collisions')
                    pair_checks += 1
            mixed = Counter()
            for _, law in data:
                for y, count in law.items():
                    mixed[y] += Fraction(count, len(seeds) * size)
            original = marginal(base)
            actual_energy = sum(Fraction(count, size) ** 2 for count in original.values())
            mixed_energy = sum(mass ** 2 for mass in mixed.values())
            truncated_mean = sum(min(seed, size) for seed in seeds) / len(seeds)
            require(abs(mixed_energy - actual_energy) <= 2 * truncated_mean / size,
                    'Mixture collision error exceeds twice the TV bound')
            rows.append({'h': h, 'X': size,
                         'actual_energy': str(actual_energy),
                         'mixed_energy': str(mixed_energy)})
    report = {
        'schema': 'collatz-stationary-collision-independent-check/v1',
        'success': True,
        'recorded_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'joint_shifted_law_checks': law_checks,
        'complete_two_copy_checks': pair_checks,
        'arithmetic_cell_intersections': intersections,
        'indicator_regime_checks': indicator_checks,
        'real_seeds': [str(seed) for seed in seeds],
        'rows': rows,
        'scope': 'Exact rational finite checks at clocks 0..6, including grade 0, '
                 'integer and noninteger source shifts, shifted windows beyond X, '
                 'negative ternary seeds, and X both below and above 2^h. '
                 'No stationary sampler, rare-event estimate, or Collatz proof.'
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['success', 'joint_shifted_law_checks',
          'complete_two_copy_checks', 'arithmetic_cell_intersections',
          'indicator_regime_checks']}))


if __name__ == '__main__':
    main()
