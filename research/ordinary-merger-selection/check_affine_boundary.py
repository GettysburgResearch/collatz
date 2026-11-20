#!/usr/bin/env python3
"""Exact bounded checks for AC1/AC2; not a Collatz proof."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

if not __debug__:
    raise RuntimeError("Run this exact checker without -O; assertions are required.")


def step(n: int) -> int:
    return (3 * n + 1) // 2 if n % 2 else n // 2


def valuation(n: int, p: int) -> int:
    assert n > 0
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def first_hit(n: int) -> tuple[int, int]:
    assert n > 0
    odd = 0
    for clock in range(10000):
        if n == 1:
            return clock, odd
        odd += n % 2
        n = step(n)
    raise AssertionError("finite fixture did not terminate within its safety cap")


def word(n: int, length: int) -> tuple[tuple[int, ...], int]:
    bits = []
    for _ in range(length):
        bits.append(n % 2)
        n = step(n)
    return tuple(bits), n


def affine(bits: tuple[int, ...]) -> tuple[int, int, int]:
    """Return numerator multiplier, offset, denominator."""
    mul, off, den = 1, 0, 1
    for bit in bits:
        assert bit in (0, 1)
        if bit:
            mul, off = 3 * mul, 3 * off + den
        den *= 2
    return mul, off, den


def valid_affine_identity(a, b, c, d, left, right) -> bool:
    lm, lo, ld = affine(left)
    rm, ro, rd = affine(right)
    return a * lm * rd == c * rm * ld and (b * lm + lo) * rd == (
        d * rm + ro
    ) * ld


def run() -> dict:
    counts = {
        "convergent_affine_instances": 0,
        "criterion_positive_instances": 0,
        "criterion_negative_instances": 0,
        "positive_cylinder_lifts": 0,
        "negative_forced_clock_checks": 0,
        "dyadic_exception_instances": 0,
        "signed_fixed_point_checks": 0,
        "ordinary_prefix_checks": 0,
        "mutation_rejections": 0,
    }
    digest = hashlib.sha256()
    slopes = (1, 2, 3, 4, 6, 9, 12, 18)
    for a in slopes:
        for c in slopes:
            for b, d in ((0, 0), (1, -1), (-2, 3), (4, 1)):
                for t in (1, 2, 3, 5, 8, 13, 21):
                    x, y = a * t + b, c * t + d
                    if min(x, y) <= 0:
                        continue
                    dx, ax = first_hit(x)
                    dy, ay = first_hit(y)
                    kx, ky = dx - 2 * ax, dy - 2 * ay
                    A = valuation(a, 2) - valuation(c, 2)
                    C = valuation(c, 3) - valuation(a, 3)
                    counts["convergent_affine_instances"] += 1
                    expected = kx - ky == A - 2 * C
                    j = max(dy, dx - A, valuation(c, 2), 0) + 2
                    i = j + A
                    left, end_left = word(x, i)
                    right, end_right = word(y, j)
                    actual = end_left == end_right and valid_affine_identity(
                        a, b, c, d, left, right
                    )
                    assert actual == expected
                    digest.update(f"{a},{b},{c},{d},{t},{expected};".encode())
                    if expected:
                        counts["criterion_positive_instances"] += 1
                        assert sum(left) - sum(right) == C
                        h = i - valuation(a, 2)
                        assert h == j - valuation(c, 2) and h >= 0
                        for lift in (0, 1, 2, 7):
                            tl = t + lift * 2**h
                            wl, el = word(a * tl + b, i)
                            wr, er = word(c * tl + d, j)
                            assert wl == left and wr == right and el == er
                            counts["positive_cylinder_lifts"] += 1
                    else:
                        counts["criterion_negative_instances"] += 1
                        for jj in range(max(0, -A), max(dx, dy) + abs(A) + 8):
                            ii = jj + A
                            wl, el = word(x, ii)
                            wr, er = word(y, jj)
                            assert not (
                                el == er
                                and valid_affine_identity(a, b, c, d, wl, wr)
                            )
                            counts["negative_forced_clock_checks"] += 1

    for r in range(65):
        for n, delta in ((2**r, 1), (3 * 2**r, 0)):
            dn, an = first_hit(n)
            d3, a3 = first_hit(3 * n)
            assert d3 - 2 * a3 - dn + 2 * an == delta != 2
            counts["dyadic_exception_instances"] += 1

    for h in range(129):
        wl, el = word(-1, h)
        wr, er = word(-3, h)
        assert not (el == er and sum(wl) - sum(wr) == 1)
        if h >= 3:
            assert el == er == -1 and sum(wl) - sum(wr) == 2
        counts["signed_fixed_point_checks"] += 1

    for h in range(3, 49):
        for lift in (1, 2, 3, 7):
            n = 2**h * lift - 1
            for i in range(h + 1):
                wl, el = word(n, i)
                wr, er = word(3 * n, i)
                assert el != er
                if i >= 3:
                    assert el == 3**i * (n + 1) // 2**i - 1
                    assert er == 3 ** (i - 1) * (n + 1) // 2**i - 1
                    assert sum(wl) - sum(wr) == 2
                counts["ordinary_prefix_checks"] += 1

    # Equal actual endpoints alone do not make a parameter identity.
    wl, el = word(3, 13)
    wr, er = word(9, 13)
    assert el == er == 1 and sum(wl) == sum(wr)
    assert not valid_affine_identity(1, 0, 3, 0, wl, wr)
    counts["mutation_rejections"] += 1

    # The sign in the three-ray defect criterion is +2, not -2.
    d23, a23 = first_hit(23)
    d69, a69 = first_hit(69)
    assert (d69 - 2 * a69) - (d23 - 2 * a23) == 2
    assert (d69 - 2 * a69) - (d23 - 2 * a23) != -2
    counts["mutation_rejections"] += 1

    # Neither a one-bit perturbation of a word nor endpoint matching at
    # one parameter is silently accepted as a lifted identity.
    wl, _ = word(23, 30)
    wr, _ = word(69, 30)
    assert valid_affine_identity(1, 0, 3, 0, wl, wr)
    changed = (1 - wl[0],) + wl[1:]
    assert not valid_affine_identity(1, 0, 3, 0, changed, wr)
    counts["mutation_rejections"] += 1

    return {
        "schema": "ordinary-merger-affine-boundary/v1",
        "status": "PASS",
        "map": "shortcut T: even n/2; odd (3n+1)/2",
        "claim_ids": ["AC1", "AC2"],
        "counts": counts,
        "fixture_digest_sha256": digest.hexdigest(),
        "scope": "Bounded exact replay; unbounded statements require the written proofs.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
