#!/usr/bin/env python3
"""One exact Hankel control; this is not a cycle search or universal proof."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from math import gcd
from pathlib import Path


def determinant(rows: list[list[Fraction]]) -> Fraction:
    a = [[Fraction(x) for x in row] for row in rows]
    value = Fraction(1)
    for k in range(len(a)):
        pivot = next((j for j in range(k, len(a)) if a[j][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[pivot], a[k] = a[k], a[pivot]
            value = -value
        diagonal = a[k][k]
        value *= diagonal
        for i in range(k + 1, len(a)):
            scale = a[i][k] / diagonal
            for j in range(k + 1, len(a)):
                a[i][j] -= scale * a[k][j]
            a[i][k] = Fraction(0)
    return value


def hankel(values: list[Fraction], size: int, shift: int = 0) -> Fraction:
    return determinant([[values[shift + i + j] for j in range(size)]
                        for i in range(size)])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--receipt', required=True, type=Path)
    args = parser.parse_args()
    source = Path(__file__).resolve()
    receipt = args.receipt.resolve()
    if receipt.is_relative_to(source.parent.parents[3]):
        parser.error('the execution receipt must be outside the checkout')
    started = datetime.now(timezone.utc).isoformat()
    positions = (0, 1, 2, 3, 4, 6, 8, 9)
    p, total = 8, 13
    u = [Fraction(2 ** (total * (j // p) + positions[j % p]))
         for j in range(18)]
    denominator = 2 ** total - 3 ** p
    numerator = sum(2 ** positions[i] * 3 ** (p - 1 - i) for i in range(p))
    closing = Fraction(numerator, denominator)
    checks = []

    def check(label: str, actual, expected) -> None:
        checks.append({'label': label, 'actual': str(actual),
                       'expected': str(expected), 'passed': actual == expected})

    def states(t: Fraction) -> list[Fraction]:
        result = [Fraction(t)]
        for forcing in u:
            result.append(3 * result[-1] + forcing)
        return result

    def polynomial(x: int) -> int:
        return sum(2 ** positions[i] * x ** (p - 1 - i) for i in range(p))

    delta_u = hankel(u, p)
    check('D', denominator, 1631)
    check('C', numerator, 7553)
    check('gcd(C,D)', gcd(numerator, denominator), 7)
    check('nonintegral closing value', closing, Fraction(1079, 233))
    check('Q(3) modulo 7', polynomial(3) % 7, 0)
    check('Q(-3) modulo 233', polynomial(-3) % 233, 0)
    check('Q(3) modulo 233', polynomial(3) % 233, 97)
    check('full-rank forcing determinant', delta_u, -2 ** 71 * 7 * 233 ** 2)
    for shift in (0, 1):
        actual = hankel(states(closing), p, shift)
        check(f'weighted-state determinant at shift {shift}', actual,
              Fraction((-8192) ** shift * 2 ** 71 * 233))
        check(f'filtered determinant identity at shift {shift}',
              hankel(u, p, shift), -1631 * actual)
    for t in (Fraction(0), Fraction(1), closing):
        check(f'border at t={t}', hankel(states(t), p + 1),
              delta_u * (-1631 * t + 7553))
    result = {
        'schema': 'collatz-risk24-hankel-control/v1',
        'scope': 'one prescribed rational cycle; shifts 0 and 1; three border values; no census or universal proof',
        'started_utc': started,
        'driver_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'checks': checks,
        'success': all(row['passed'] for row in checks),
        'finished_utc': datetime.now(timezone.utc).isoformat(),
    }
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'success': result['success'], 'checks': len(checks),
                      'receipt_sha256': hashlib.sha256(receipt.read_bytes()).hexdigest()}, indent=2))
    return 0 if result['success'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
