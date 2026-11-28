#!/usr/bin/env python3
"""Exact signed gate, positive-cylinder, and stored-block tail controls."""

from fractions import Fraction as F
from itertools import product


def require(test, message):
    if not test:
        raise ValueError(message)


def residue(x, modulus):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def legal(s, e):
    return (2**e * s - 1) % 9 in (3, 6)


def inverse(x, e):
    return (2**e*x - 1)/3


def affine(x, e):
    return (1+3*x)/2**e


def small_gap(y, lo):
    return next(e for e in range(lo, lo+4) if legal(residue(y, 9), e))


def finite_policy(x, width):
    s = residue(x, 3**width)
    available = [e for e in range(1, 7) if legal(s, e)]
    return available[(s // 3) % len(available)]


def follow(start, n, width):
    x = F(start)
    total = 0
    for _ in range(n):
        e = finite_policy(x, width)
        x = inverse(x, e)
        total += e
    return total, residue(x, 3**width)


def reduced_shapes():
    count = 0
    for n in range(7):
        for w in product(range(1, 6), repeat=n):
            y = F(-1)
            for e in reversed(w):
                y = affine(y, e)
            if y < 0:
                require(y.numerator == -1 and y.denominator.bit_count() == 1,
                        'negative image outside signed list')
                k = y.denominator.bit_length()-1
                u = list(w)
                while u and u[-1] == 1:
                    u.pop()
                if k >= 2:
                    require(u in ([k+1], [k-1, 2]), 'reduced negative representation')
            count += 1
    return count


def gates():
    checked = 0
    positive = 0
    for W in range(2, 6):
        mod = 3**W
        N = 2*3**(W-1)
        R = 6
        B = 3*N
        M = R+6*W+1
        n = 6*M+3*B+7
        for s in range(1, mod):
            if s % 3 == 0:
                continue
            e0 = small_gap(F(s), R+4)
            y = inverse(F(s), e0)
            plan = [e0]
            for _ in range(W-1):
                e = small_gap(y, 3)
                plan.append(e)
                y = inverse(y, e)
            z = F(-1)
            for e in reversed(plan):
                z = affine(z, e)
            require(residue(z, mod) == s and 0 < z < F(1, 2**(R+2)), 'positive gate')
            y = z
            for e in plan:
                require(legal(residue(y, 9), e), 'route loses unit')
                y = inverse(y, e)
            require(y == -1, 'gate route endpoint')
            base, last = follow(z, n, W)
            require(base > sum(plan)+(n-W)+B+1, 'strict bias allowance')
            # The positive ordinary lift has the same n actions and terminal cell.
            modulus = 3**(n+W)
            lift = residue(z, modulus)
            if lift % 2 == 0:
                lift += modulus
            require(follow(lift, n, W) == (base, last), 'positive lift disagrees')
            win = F(lift)
            for e in plan: win = inverse(win, e)
            for _ in range(n-W): win = inverse(win, 1)
            require(win > 0 and win.denominator == 1 and residue(win, mod) == mod-1,
                    'positive lifted competitor')
            positive += 1
            if W <= 4:
                k = next(k for k in range(N+2,2*N+2) if residue(-F(1,2**k), mod) == s)
                n0 = 24*N+12
                base0, _ = follow(-F(1,2**k), n0, W)
                require(base0 > n0+k+B+1, 'single long edge saving')
            checked += 1
    return checked, positive


def reset_rows():
    fixtures = 0
    W = 2
    for n in range(1, 5):
        fine = 3**(W+n)
        for s in range(fine):
            if s % 3 == 0: continue
            y = F(s)
            plan = []
            # The plan explicitly uses the last observed trit.
            for i in range(n):
                a = small_gap(y, 1+2*((s//(fine//3)+i)%2))
                plan.append(a)
                y = inverse(y, a)
            out = []
            for j in range(3**n):
                v = F(s+fine*j)
                for e in plan: v = inverse(v,e)
                out.append(residue(v, fine))
            lo = residue(y, 3**W)
            require(sorted(out) == list(range(lo, fine, 3**W)), 'block Haar reset')
            fixtures += 1
    return fixtures


if __name__ == '__main__':
    shapes = reduced_shapes()
    states, positive = gates()
    rows = reset_rows()
    print(f'PASS {shapes} negative-word tests, {states} signed gate classes, '
          f'{positive} genuine positive lift comparisons, {rows} exhaustive Haar reset laws')
