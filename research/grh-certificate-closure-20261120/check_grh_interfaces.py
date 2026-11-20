#!/usr/bin/env python3
"""Exact finite interface checks, not a GRH proof or Collatz proof."""
from __future__ import annotations
import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path


def need(ok: bool, why: str) -> None:
    if not ok:
        raise ValueError(why)


def step(n: int) -> int:
    need(type(n) is int and n > 0, 'ordinary positive input')
    return (3*n+1)//2 if n & 1 else n//2


def prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n)+1, 2))


def word(n: int, h: int) -> tuple[int, ...]:
    result = []
    for _ in range(h):
        result.append(n & 1)
        n = step(n)
    return tuple(result)


def validate_prime(h: int, b: int, p: int) -> None:
    need(type(h) is int and h >= 2, 'word length')
    q = 1 << h
    need(type(b) is int and 0 < b < q and b & 1, 'odd cylinder')
    need(type(p) is int and prime(p), 'prime source')
    need(p % q == b, 'prescribed residue')
    need(p < 2*q*q*h*h, 'coarse GRH consequence envelope')
    need(word(p, h) == word(b, h), 'literal word equality')


def components(q: int, use_odd: bool = True) -> int:
    parent = list(range(q))
    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for n in range(1, 2*q+1):
        if n & 1 and not use_odd:
            continue
        a, b = find(n % q), find(step(n) % q)
        parent[a] = b
    return len({find(a) for a in range(q)})


def run() -> dict:
    counts = {'prime_cylinders': 0, 'growth_prefix_states': 0,
              'unit_residues': 0, 'certified_sources': 0,
              'blocked_source_levels': 0, 'periodic_quotients': 0}
    sample, first = [], None
    for h in range(2, 9):
        q = 1 << h
        for b in range(1, q, 2):
            p = b
            while not prime(p):
                p += q
            validate_prime(h, b, p)
            counts['prime_cylinders'] += 1
            first = first or (h, b, p)
    for h in range(2, 19):
        q, p = 1 << h, (1 << h)-1
        while not prime(p):
            p += q
        validate_prime(h, q-1, p)
        a, y = (p+1)//q, p
        for j in range(h+1):
            need(y == 3**j * (1 << (h-j))*a-1, 'growing prime formula')
            if j:
                need(y > p, 'prime prefix strict growth')
            y = step(y)
            counts['growth_prefix_states'] += 1
        sample.append({'H': h, 'prime': p})

    for e in range(1, 10):
        q, period = 3**e, 2*3**(e-1)
        powers, x = [], 1
        for _ in range(period):
            powers.append(x)
            x = 2*x % q
        need(x == 1 and len(set(powers)) == period, 'full exact order')
        need(set(powers) == {a for a in range(q) if a % 3}, 'all units')
        need(pow(2, period//2, q) == q-1, 'minus-one exponent')
        h = q.bit_length()-1
        good = {pow(pow(2, a, q), -1, q) for a in range(1, h+1)}
        need(len(good) == h, 'exact short-inverse class count')
        if e >= 3:
            need(q-1 not in good and period//2 > h, 'prescribed-level obstruction')
        counts['unit_residues'] += period

    for E in range(3, 11):
        b = 3**E+1
        n = ((1 << b)-1)//3
        need(n & 1 and 3*n+1 == 1 << b, 'complete depth-one certificate')
        need((n+1) % 3**E == 0 and (n+1) % 3**(E+1) != 0,
             'exact source ternary valuation')
        for e in range(3, E+1):
            q, a = 3**e, 3**(e-1)
            need(n % q == q-1 and pow(2, a, q)*(n % q) % q == 1,
                 'certified source prescribed inverse')
            h = q.bit_length()-1
            need(all((pow(2, j, q)*(n % q)-1) % q for j in range(1, h+1)),
                 'no decreasing exponent at prescribed level')
            counts['blocked_source_levels'] += 1
        counts['certified_sources'] += 1

    for q in range(1, 257):
        need(components(q) == 1, 'periodic invariant quotient connected')
        counts['periodic_quotients'] += 1
    need(components(7, use_odd=False) == 3, 'odd-law deletion negative control')

    h, b, p = first
    bad = [(h, b, p*(1+(1 << h))), (h, b+2, p), (1, 1, 3)]
    rejected = 0
    for row in bad:
        try:
            validate_prime(*row)
        except ValueError:
            rejected += 1
        else:
            raise ValueError('damaged prime certificate accepted')
    return {'status': 'PASS', 'counts': counts, 'growth_prime_examples': sample,
            'damaged_certificates_rejected': rejected,
            'omitting_odd_edges_components_mod7': 3,
            'scope': 'Exact bounded arithmetic; cited GRH least-prime theorem not verified by these examples; no full Collatz proof.',
            'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    raw = json.dumps(run(), indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(raw, encoding='utf-8')
    print(raw, end='')
