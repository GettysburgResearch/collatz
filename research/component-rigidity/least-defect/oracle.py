#!/usr/bin/env python3
"""Exact odd-equation defect counts for finite dyadic step colorings.

All counts include the +1 in p*n+1, strict half-open endpoints, odd parity and
physical cutoff. No ambient integer interval is enumerated by this module.
"""
from __future__ import annotations
from bisect import bisect_right
from fractions import Fraction as Q


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def integer(n: int, minimum: int = 0) -> int:
    need(type(n) is int and n >= minimum, 'integer domain')
    return n


def encode(q: Q) -> list[int]:
    return [q.numerator, q.denominator]


def rational(pair: list[int]) -> Q:
    need(type(pair) is list and len(pair) == 2, 'rational pair')
    need(type(pair[0]) is int and type(pair[1]) is int and pair[1] > 0, 'rational types')
    out = Q(*pair)
    need(encode(out) == pair, 'noncanonical rational')
    return out


def ceilq(q: Q) -> int:
    return -((-q.numerator)//q.denominator)


def checked(steps: list) -> tuple[list, int]:
    need(type(steps) is list and steps, 'empty step partition')
    rows = []
    end = Q(1)
    D = 0
    for row in steps:
        need(type(row) is list and len(row) == 3, 'step row')
        a, b = rational(row[0]), rational(row[1])
        c = integer(row[2])
        need(c in (0, 1) and a == end and a < b <= 2, 'step partition or color')
        for x in (a, b):
            d = x.denominator
            need(d & (d-1) == 0, 'nondyadic endpoint')
            D = max(D, d.bit_length()-1)
        rows.append((a, b, c)); end = b
    need(end == 2, 'incomplete step partition')
    return rows, D


def from_cut(certificate: dict) -> list:
    need(certificate['status'] == 'SEPARATOR', 'a separator is required')
    rows = []
    for a, b, c in certificate['ranges']:
        left, right = rational(a)+1, rational(b)+1
        if rows and rows[-1][2] == c:
            rows[-1][1] = encode(right)
        else:
            rows.append([encode(left), encode(right), c])
    checked(rows)
    return rows


def evaluator(steps: list):
    rows, _ = checked(steps)
    starts = [a for a, _, _ in rows]
    labels = [c for _, _, c in rows]
    def value(n: int) -> int:
        integer(n, 1)
        x = Q(n, 1 << (n.bit_length()-1))
        return labels[bisect_right(starts, x)-1]
    return value


def overlaps(rows: list, p: int, scale: int, offset: int):
    """Two monotone partitions; yields ALL rational intersection intervals."""
    integer(p, 3); need(p in (3, 5), 'multiplier')
    source = [(a*scale, b*scale, c) for a, b, c in rows]
    r = p.bit_length()-1
    target = [((a*scale*(1 << t)-offset)/p,
               (b*scale*(1 << t)-offset)/p, c)
              for t in (r, r+1) for a, b, c in rows]
    i = j = 0
    while i < len(source) and j < len(target):
        a, b, c = source[i]; u, v, d = target[j]
        left, right = max(a, u), min(b, v)
        if left < right:
            yield left, right, c, d
        if b <= v:
            i += 1
        if v <= b:
            j += 1


def shell(steps: list, p: int, h: int, last_source: int | None = None) -> dict:
    rows, _ = checked(steps)
    integer(h)
    scale = 1 << h
    stop = 2*scale-1 if last_source is None else integer(last_source)
    need(scale <= stop < 2*scale, 'shell cutoff')
    blocks = []
    for left, right, a, b in overlaps(rows, p, scale, 1):
        lo = max(scale, ceilq(left)); hi = min(stop, ceilq(right)-1)
        lo += int(lo % 2 == 0); hi -= int(hi % 2 == 0)
        if lo > hi:
            continue
        if blocks and blocks[-1][1]+2 == lo and blocks[-1][2:] == [a, b]:
            blocks[-1][1] = hi
        else:
            blocks.append([lo, hi, a, b])
    bad = [z for z in blocks if z[2] != z[3]]
    return {'h': h, 'last_source': stop, 'blocks': blocks,
            'defects': sum((b-a)//2+1 for a, b, _, _ in bad),
            'least': bad[0][0] if bad else None}


def model(steps: list, p: int) -> dict:
    rows, D = checked(steps)
    integer(p, 3); need(p in (3, 5), 'multiplier')
    P = 2 if p == 3 else 4
    ideal = [[encode(a), encode(b), c, d] for a, b, c, d in overlaps(rows, p, 1, 0)]
    delta = sum((rational(b)-rational(a) for a, b, c, d in ideal if c != d), Q(0))
    start = D+1
    base = [shell(steps, p, h) for h in range(start+P)]
    beta = [Q(base[start+r]['defects'])-delta*(1 << (start+r-1)) for r in range(P)]
    # This is the stated finite-step theorem, not a search stopping assumption.
    nonconstant = len({c for _, _, c in rows}) > 1
    need((delta > 0) == nonconstant, 'finite-step rotation test')
    return {'schema': 'least-defect-model-v1', 'p': p, 'steps': steps, 'D': D,
            'period': P, 'start': start, 'ideal': ideal, 'delta': encode(delta),
            'base': base, 'beta': [encode(x) for x in beta]}


def predicted_count(m: dict, h: int) -> int:
    integer(h)
    if h < m['start']:
        return m['base'][h]['defects']
    z = rational(m['delta'])*(1 << (h-1))+rational(m['beta'][(h-m['start']) % m['period']])
    need(z.denominator == 1 and z >= 0, 'nonintegral tail count')
    return z.numerator


def least(m: dict) -> dict:
    """Globally least violated actual odd source, not just some violated edge."""
    for row in m['base']:
        if row['least'] is not None:
            return {'n': row['least'], 'shell': row['h'], 'extra': None}
    if rational(m['delta']) == 0:
        return {'n': None, 'shell': None, 'extra': None}
    h = m['start']+m['period']
    row = shell(m['steps'], m['p'], h)
    need(row['defects'] == predicted_count(m, h) and row['least'] is not None,
         'finite-step least-defect bound')
    return {'n': row['least'], 'shell': h, 'extra': row}


def cutoff(m: dict, H: int) -> dict:
    """Count every violated physical odd edge with BOTH endpoints <= H."""
    integer(H, 1)
    p, start, P = m['p'], m['start'], m['period']
    L = min(H, (2*H-1)//p)
    if L == 0:
        return {'H': H, 'last_eligible': L, 'full_shells': 0, 'prefix': 0,
                'tail': [0, 1], 'last_shell': None, 'defects': 0, 'least': None}
    a = L.bit_length()-1
    prefix = sum(m['base'][h]['defects'] for h in range(min(start, a)))
    tail = Q(0)
    if a > start:
        tail = rational(m['delta'])*((1 << (a-1))-(1 << (start-1)))
        length = a-start
        for r, b in enumerate(m['beta']):
            times = 0 if length <= r else 1+(length-1-r)//P
            tail += times*rational(b)
    last = shell(m['steps'], p, a, L)
    total = Q(prefix)+tail+last['defects']
    need(total.denominator == 1 and total >= 0, 'cutoff count')
    candidate = least(m)['n']
    witness = candidate if candidate is not None and candidate <= L else None
    need((total > 0) == (witness is not None), 'cutoff witness')
    return {'H': H, 'last_eligible': L, 'full_shells': a, 'prefix': prefix,
            'tail': encode(tail), 'last_shell': last, 'defects': total.numerator,
            'least': witness}


def first_defects(steps: list, p: int, lo: int, hi: int, limit: int) -> list[int]:
    """Enumerate only the requested repair batch, never all ambient sources."""
    integer(lo, 1); integer(hi, lo); integer(limit, 1)
    out = []
    for h in range(lo.bit_length()-1, hi.bit_length()):
        row = shell(steps, p, h, min(hi, (1 << (h+1))-1))
        for a, b, c, d in row['blocks']:
            if c == d or b < lo:
                continue
            start = max(a, lo)
            start += int(start % 2 == 0)
            count = min((b-start)//2+1, limit-len(out))
            out.extend(start+2*i for i in range(max(0, count)))
            if len(out) == limit:
                return out
    return out
