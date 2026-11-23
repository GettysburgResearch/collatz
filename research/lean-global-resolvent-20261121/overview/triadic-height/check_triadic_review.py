#!/usr/bin/env python3
"""Independent exact controls for the weighted triadic paired-state proof.

This is a bounded arithmetic check, not a proof of universal certificate
existence.  It deliberately uses Fraction for the rational interpretation
and explicit exceptions rather than optimization-removable assertions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import prod
from pathlib import Path


def weight(r: int) -> int:
    return prod(1 + 3**j for j in range(r))


def step(x: int, w: int, r: int):
    if (x + w) % 2 != 1:
        return None
    if x % 2:
        return ((3 * x + 1) // 2, w // 2, r)
    if r:
        return (x // 2, (w + 3 ** (r - 1)) // 2, r - 1)
    return (x // 2, (3 * w + 1) // 2, 0)


def potential(state) -> int:
    x, w, r = state
    return x * abs(w) * weight(r)


def require(condition: bool, label: str, *states) -> None:
    if not condition:
        raise RuntimeError((label, *states))


def run() -> dict:
    counts = dict(compatible=0, positive_drop=0, zero_entry=0, tie=0,
                  two_step=0)
    for x in range(2, 101):
        for r in range(8):
            numerators = set(range(-120, 121)) | {
                -(3**r), 3**r, -(3 ** max(0, r - 1)),
                3 ** max(0, r - 1),
            }
            for w in sorted(numerators):
                state = (x, w, r)
                after = step(*state)
                if after is None or w == 0:
                    continue
                counts['compatible'] += 1
                xp, wp, rp = after
                y = Fraction(w, 3**r)
                yp = Fraction(wp, 3**rp)
                expected = y / 2 if x % 2 else (3 * y + 1) / 2
                require(yp == expected, 'rational', state, after)
                require(potential(after) <= potential(state), 'monotone',
                        state, after)
                if x % 2 == 0 and r > 0:
                    counts['positive_drop'] += 1
                    require(4 * potential(after) <= potential(state),
                            'quarter', state, after)
                if wp == 0:
                    counts['zero_entry'] += 1
                    require(r > 0 and x % 2 == 0
                            and w == -(3 ** (r - 1))
                            and xp + 1 <= potential(state),
                            'zero', state, after)
                if x % 2 == 0 and r == 0 and w == 1:
                    counts['tie'] += 1
                    require(potential(after) == potential(state), 'tie',
                            state, after)
                else:
                    require(6 * potential(after) <= 5 * potential(state),
                            'contraction', state, after)
                if xp > 1 and wp != 0:
                    second = step(*after)
                    if second is not None:
                        counts['two_step'] += 1
                        require(6 * potential(second) <= 5 * potential(state),
                                'two', state, after, second)
    return counts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True, type=Path)
    parser.add_argument('--receipt', type=Path)
    args = parser.parse_args()
    result = {
        'scope': ('Independent bounded arithmetic check of written one/two-step '
                  'inequalities and rational state meaning; not a universal '
                  'certificate construction or formal proof.'),
        'range': ('2<=x<=100; 0<=r<=7; w in [-120,120] plus signed 3^r and '
                  '3^max(0,r-1); compatible nonzero starts only.'),
        'counts': run(),
        'reviewed_source_name': args.source.name,
        'reviewed_source_sha256': hashlib.sha256(args.source.read_bytes()).hexdigest(),
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.receipt:
        args.receipt.write_text(rendered)
    print(rendered, end='')


if __name__ == '__main__':
    main()
