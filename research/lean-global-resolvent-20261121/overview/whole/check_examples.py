#!/usr/bin/env python3
"""Replay the one-pass failure and its credited independent-clock affine repair."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def step(n: int) -> int:
    return (3 * n + 1) // 2 if n % 2 else n // 2


def iterate(n: int, clock: int) -> int:
    for _ in range(clock):
        n = step(n)
    return n


def affine_path(slope: int, offset: int, clock: int) -> tuple[int, int, int]:
    """Exact on every nonnegative parameter: check constant parity at each step."""
    odds = 0
    for _ in range(clock):
        require(slope % 2 == 0, "Parity may depend on the affine parameter")
        if offset % 2:
            slope, offset = 3 * slope // 2, (3 * offset + 1) // 2
            odds += 1
        else:
            slope, offset = slope // 2, offset // 2
    return slope, offset, odds


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    q, e, target, word = 17, 1, 63, [2, 3, 4]
    source, degree, offset = q, 3, target - 27 * q
    clock, boost, envelope = 0, e, 2 ** (e - 1) * q
    rows = []
    for gap in word:
        numerator = 3 * source + 1
        require(numerator % 2 ** gap == 0, "Nonintegral supplied source edge")
        endpoint = numerator // 2 ** gap
        require(endpoint > 0 and endpoint % 2 == 1, "Wrong exact source valuation")
        require(degree > 0, "This example unexpectedly stopped at degree zero")
        signed = offset - 3 ** (degree - 1)
        odds = 0
        for _ in range(gap):
            odds += signed % 2
            signed = step(signed)
        degree, offset = degree - 1 + odds, signed
        source, clock, boost = endpoint, clock + gap, max(boost, gap - 1)
        paid = 2 ** boost * source
        envelope = max(envelope, paid)
        actual = iterate(target, clock)
        require(actual == 3 ** degree * source + offset, "Affine target pin failed")
        require(offset < 0, "Negative carry invariant failed")
        require(actual > 2 * paid + 1, "One-pass noncapture example failed")
        rows.append(dict(source=source,clock=clock,boost=boost,
                         paid_ceiling=2*paid+1,target=actual,degree=degree,offset=offset))
    require(source == 1 and envelope == 26, "Complete source or maximal envelope failed")
    require(2 ** e*q+1 < target <= 2 ** (e+1)*q+1, "Target is not a low residual")
    require(target > 2*envelope+1, "Target is already inside the source envelope")
    require([row['target'] for row in rows] == [143,485,91], "Target clocks changed")
    upper = affine_path(256,63,8)
    lower = affine_path(128,31,7)
    require(upper == lower == (729,182,6), "Credited all-parameter merger failed")
    require(2*128 == 256 and 2*31 == 63-1, "Partner is not below half the target")
    require(31 <= rows[0]['paid_ceiling'], "Base partner is not rank paid")
    wrong = affine_path(768,63,8)
    require(wrong[0] == 2187 and wrong[0] != lower[0], "Wrong-slope diagnostic changed")
    result = dict(schema='collatz-checkpoint9-examples/v1',success=True,
                  scope='Exact finite counterexample and symbolic affine ray; no universal coverage claim',
                  checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  source=q,exponent=e,target=target,certificate=word,envelope=envelope,
                  cuts=rows,ray=dict(upper_input=[256,63],upper_clock=8,
                                    lower_input=[128,31],lower_clock=7,
                                    common_endpoint=list(upper[:2]),odd_count=upper[2]),
                  ray_source=dict(pr=185,commit='276be8154f4e867acc0230466b34d9cb224aacf5',
                                  path='research/literature-orbit-closure-20261121/certificates/prefix_language_rules.json',
                                  row=[1,8,63,31,1]),
                  wrong_slope_endpoint=list(wrong[:2]))
    args.receipt.parent.mkdir(parents=True,exist_ok=True)
    args.receipt.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: exact one-pass failure and credited all-parameter merger')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
