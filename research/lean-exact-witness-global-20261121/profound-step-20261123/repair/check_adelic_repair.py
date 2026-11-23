#!/usr/bin/env python3
"""Exact finite controls for canonical pullbacks, not an escaping-orbit census."""
from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def valuation(n: int, p: int) -> int:
    require(n != 0, 'valuation at zero')
    n = abs(n)
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def padic(x: F, p: int) -> F:
    if x == 0:
        return F(0)
    v = valuation(x.numerator, p) - valuation(x.denominator, p)
    return F(p) ** (-v)


def orbit(start: int, steps: int) -> tuple[list[int], list[int], list[int]]:
    require(start > 0 and start % 2 == 1 and start % 3 != 0, 'unit odd source')
    q, gaps, clocks = [start], [], [0]
    for _ in range(steps):
        value = 3 * q[-1] + 1
        a = valuation(value, 2)
        q.append(value >> a)
        gaps.append(a)
        clocks.append(clocks[-1] + a)
    return q, gaps, clocks


def leaf(q: list[int], clocks: list[int], j: int, b: int) -> F:
    h = (64 ** b - 1) // 3
    z = F(2 ** clocks[j], 3 ** j)
    return q[0] + h * z * (3 * q[j] + 1)


def verify_primitive(q0: int, qnext: int, next_clock: int, j: int,
                     b: int, P: int, Q: int) -> None:
    h = (64 ** b - 1) // 3
    nu = valuation(h, 3)
    require(j > nu, 'not in the nonintegral primitive range')
    c = h // 3 ** nu
    require(Q == 3 ** (j - nu), 'wrong primitive denominator')
    require(P == Q * q0 + c * 2 ** next_clock * qnext, 'wrong primitive numerator')
    require(math.gcd(P, Q) == 1, 'pair is not primitive')
    require(padic(F(P - q0 * Q), 2) == F(2) ** -next_clock,
            'wrong exact binary precision')


def main() -> None:
    counts = dict(pullbacks=0, primitive_pairs=0, literal_rational_edges=0,
                  finite_products=0, block_extrapolants=0,
                  real_contracting_tail_blocks=0, rejected_controls=0)
    seeds = [1, 5, 7, 11, 13, 17, 25, 31, 41, 65, 193, 385, 837799]
    sibling_powers = [1, 2, 3, 4, 9, 27]
    example = None
    smallest_product = None
    for start in seeds:
        q, gaps, A = orbit(start, 64)
        for b in sibling_powers:
            h = (64 ** b - 1) // 3
            nu, c = valuation(h, 3), h // 3 ** valuation(h, 3)
            require(nu == 1 + valuation(b, 3), 'LTE identity')
            require(c >= 7 and c % 2 == 1 and c % 3 != 0, 'primitive sibling factor')
            for j in range(0, 59):
                y, yp = leaf(q, A, j, b), leaf(q, A, j + 1, b)
                z, zn = F(2 ** A[j], 3 ** j), F(2 ** A[j + 1], 3 ** (j + 1))
                D = z * q[j] - start
                require(y == 64 ** b * start + 3 * h * D + h * z, 'complete pullback')
                require(yp - y == h * zn, 'successive leaf increment')
                require(y.denominator == 3 ** max(0, j - nu), 'exact reduced denominator')
                counts['pullbacks'] += 1
                if j <= 12 and b <= 3:
                    current = y
                    for a in gaps[:j]:
                        v = 3 * current + 1
                        require(v.denominator % 2 == 1 and
                                valuation(v.numerator, 2) == a,
                                'literal rational parity/gap mismatch')
                        current = v / 2 ** a
                        require(current > 0, 'lost positive rational source')
                        counts['literal_rational_edges'] += 1
                    target = 64 ** b * q[j] + h
                    require(current == target, 'changed the sibling root')
                    require((3 * target + 1) // 2 ** (gaps[j] + 6 * b) == q[j + 1],
                            'wrong unchanged forward ray')
                if j > nu:
                    P, Q = y.numerator, y.denominator
                    verify_primitive(start, q[j + 1], A[j + 1], j, b, P, Q)
                    counts['primitive_pairs'] += 1
                    if example is None:
                        example = (start, q[j + 1], A[j + 1], j, b, P, Q)
                    for J in (j + 1, j + 3, j + 5):
                        L = leaf(q, A, J, b)
                        product = abs(F(P) - L * Q) * Q
                        product *= padic(F(P - start * Q), 2) * padic(F(Q), 2)
                        product *= padic(F(P), 3) * padic(F(Q), 3)
                        require(product == Q * (L - y) / 2 ** A[j + 1], 'full adelic product')
                        require(product >= F(c, 3) >= F(7, 3), 'claimed product saving')
                        if J == j + 1:
                            require(product == F(c, 3), 'sharp one-tail-term constant')
                        smallest_product = product if smallest_product is None else min(product, smallest_product)
                        counts['finite_products'] += 1
        for j in range(18):
            z = F(2 ** A[j], 3 ** j)
            D = z * q[j] - start
            for r in range(1, 7):
                P, Q = 3 ** r, 2 ** (A[j + r] - A[j])
                C = Q * q[j + r] - P * q[j]
                Dnext = F(2 ** A[j + r], 3 ** (j + r)) * q[j + r] - start
                require(C > 0 and Dnext - D == z * C / P, 'complete block carry')
                H = D + z * C / (P - Q)
                delta = (Q - P) * q[j] - C
                require(H + start == z * delta / (Q - P), 'signed extrapolation error')
                require(delta == Q * (q[j] - q[j + r]), 'actual endpoint displacement')
                counts['block_extrapolants'] += 1
                if Q < P:
                    counts['real_contracting_tail_blocks'] += 1

    require(example is not None, 'missing primitive example')
    for index, increment in [(2, 1), (3, 1), (5, 1), (6, 1)]:
        bad = list(example)
        bad[index] += increment
        try:
            verify_primitive(*bad)
        except ValueError:
            counts['rejected_controls'] += 1
        else:
            raise ValueError('damaged primitive certificate was accepted')

    q, gaps, A = orbit(65, 10)
    require(q[8] == 1, 'control prefix')
    y = leaf(q, A, 8, 1)
    require(y.denominator == 3 ** 7, 'control canonical denominator')
    require((3 * 75 + 1) // 2 == 113 and (3 * 113 + 1) // 4 == 85,
            'ordinary same-root alternative repair')
    here = Path(__file__).resolve().parent
    hashes = {name: hashlib.sha256((here / name).read_bytes()).hexdigest()
              for name in ['ADELIC_INTEGER_REPAIR.md', 'AdelicRepair.lean', Path(__file__).name]}
    print(json.dumps(dict(status='PASS', counts=counts, seeds=seeds,
                         sibling_powers=sibling_powers,
                         sharp_finite_product=str(smallest_product),
                         ordinary_alternative=dict(source=75, odd_path=[75, 113, 85],
                             fixed_root=85, original_source=65, original_prefix=8,
                             canonical_leaf=str(y)),
                         source_sha256=hashes,
                         scope='exact finite rational and ordinary controls; no escaping-orbit example or universal integer repair'),
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
