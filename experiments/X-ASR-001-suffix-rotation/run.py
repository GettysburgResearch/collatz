#!/usr/bin/env python3
"""Exact finite evidence for ASR; not a universal Collatz certificate."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from math import isqrt
from pathlib import Path

BASE = 'ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a'
APR = '7b7471ea0e7b359a2ac46fb1e6aff269331509c3'
LIMIT = 8192


def need(ok: bool, why: str) -> None:
    if not ok:
        raise ValueError(why)


def encoded(x: object) -> bytes:
    return json.dumps(x, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def sha(x: object) -> str:
    return hashlib.sha256(encoded(x)).hexdigest()


def v3(x: int) -> int:
    x = abs(x)
    need(x > 0, 'zero valuation')
    h = 0
    while x % 3 == 0:
        x //= 3
        h += 1
    return h


def g(x: int) -> int:
    return x*x // 3**v3(x)


def T(x: int) -> int:
    need(x > 0, 'positive source')
    return (3*x+1)//2 if x & 1 else x//2


@lru_cache(None)
def rank(n: int) -> tuple[int, tuple]:
    need(type(n) is int and n >= 1, 'rank domain')
    if n == 1:
        return 0, ()
    best = g(n)
    winners = [(0, '', n, v3(n))]
    x, word, power = n, '', 4
    for k in range(1, n.bit_length()):
        if power > best:
            break
        word += str(x & 1)
        x = T(x)
        d = x-n
        if d:
            value = power*g(d)
            if value < best:
                best, winners = value, []
            if value == best:
                winners.append((k, word, d, v3(d)))
        power *= 4
    need(n <= best <= n*n, 'rank properness')
    return best, tuple(winners)


def psi(n: int) -> int:
    return (n+1)*rank(n)[0]


def data(word: str) -> tuple[int, int, int, int]:
    A = q = 0
    for i, bit in enumerate(word):
        if bit == '1':
            A = 3*A + 2**i
            q += 1
    return 2**len(word), 3**q, A, q


def walk(n: int, word: str) -> int:
    for bit in word:
        need(n & 1 == int(bit), 'physical parity')
        n = T(n)
    return n


def options(n: int) -> tuple[list, list, int]:
    G, winners = rank(n)
    if n == 1:
        return [], [], 0
    K = max(1, (g(n).bit_length()-1)//2)
    forward, backward = [], []
    x, word = n, ''
    for j in range(1, K+1):
        word += str(x & 1)
        x = T(x)
        if psi(x) < (n+1)*G:
            forward.append([x, j, word])
    checked = 0
    for k, w, d, h in winners:
        if not k:
            continue
        for r in range(1, k+1):
            u, v = w[:-r], w[-r:]
            P, Q, A, a = data(v)
            if h < a:
                continue
            x, rem = divmod(P*n-A, Q)
            need(not rem and 0 < x <= n*n, 'suffix source')
            need(walk(x, v) == n, 'inverse certificate')
            z = walk(x, v+u)
            need(Q*(z-x) == P*d and z != x, 'rotated displacement')
            need(Q*4**k*g(z-x) == P*P*G, 'candidate identity')
            need(Q*rank(x)[0] <= P*P*G, 'new candidate bound')
            E = A+P-Q
            need(E >= 0 and Q*(x+1)+E == P*(n+1), 'n+1 shift')
            need(Q*Q*psi(x) <= P**3*psi(n), 'common-rank bound')
            analytic = Q*Q > P**3
            if analytic:
                need(x < n and psi(x) < psi(n), 'strict analytic reduction')
            if psi(x) < psi(n):
                backward.append([x, r, v, k, analytic])
            checked += 1
    return forward, backward, checked



def select(n: int) -> dict:
    """One total call: return a physical reduction, CORE, or UNRESOLVED."""
    if n == 1:
        return {'status': 'CORE'}
    fs, bs, _ = options(n)
    choices = [(psi(x), x, j, 'forward', w) for x, j, w in fs]
    choices += [(psi(x), x, r, 'backward', v) for x, r, v, _, _ in bs]
    if not choices:
        return {'status': 'UNRESOLVED'}
    target_rank, x, clock, direction, word = min(choices)
    need(target_rank < psi(n), 'selected common rank')
    return dict(status='REDUCED', x=x, clock=clock, direction=direction, word=word)



def long_case(a: int, H: int) -> list:
    w = '1'*a+'0'
    P, Q, A, _ = data(w)
    D = Q-P
    for N in range(2, 33):
        multiplier = P**N*3**H
        residue = A*pow(multiplier, -1, D) % D
        u = min(residue+t*D for t in range(7)
                if residue+t*D > 0 and (residue+t*D) % 6 in (1, 5))
        n = (multiplier*u-A)//D
        G, winners = rank(n)
        if any(row[1] == w for row in winners):
            x = (P*n-A)//Q
            need(Q*Q > P**3 and walk(x, w) == n, 'long suffix physical')
            need(Q*Q*psi(x) <= P**3*psi(n) and psi(x) < psi(n), 'long bound')
            return [a, H, N, u, n, x, G, psi(x)]
    raise ValueError('finite fixture construction did not find a selected word')


def reconstruct() -> tuple[dict, dict]:
    rows, counts, residual = [], Counter(), []
    checks = length_one = 0
    for n in range(2, LIMIT+1):
        G, winners = rank(n)
        fs, bs, c = options(n)
        checks += c
        tag = 'forward' if fs else 'backward_only' if bs else 'unresolved'
        counts[tag] += 1
        if tag == 'unresolved':
            residual.append(n)
        if any(row[0] == 1 for row in winners):
            need(bool(fs or bs), 'length-one coverage')
            length_one += 1
        chosen = select(n)
        need((chosen['status'] == 'UNRESOLVED') == (tag == 'unresolved'), 'selector status')
        rows.append([n, G, [list(t) for t in winners], fs, bs, chosen])
    units = []
    for H in range(1, 41):
        n, y, x = 2*3**H-1, 3**(H+1)-1, 4*3**(H-1)-1
        G, winners = rank(n)
        need(G == 4*3**H and len(winners) == 1 and winners[0][0] == 1, 'unit winner')
        need(rank(y)[0]**10 > n**11 and T(x) == n, 'unit spike/edge')
        need(9*psi(x) <= 8*psi(n) and psi(x) < psi(n), 'unit bypass')
        units.append([H, n, y, x, G, rank(y)[0], psi(n), psi(x)])
    mersenne = []
    phase_count = 0
    for L in range(2, 65):
        n = 2**L-1
        G, winners = rank(n)
        need(G == g(n) and len(winners) == 1 and winners[0][0] == 0, 'Mersenne baseline')
        fs, bs, _ = options(n)
        need(not fs and not bs, 'false universal coverage')
        x, phases = n, []
        for j in range(1, L):
            x = T(x)
            need(x == 3**j*2**(L-j)-1 and psi(x) > psi(n), 'Mersenne phase')
            phases.append([j, x, psi(x)])
        phase_count += len(phases)
        mersenne.append([L, n, G, phases])
    longs = [long_case(a, H) for a in (18, 19, 24, 32) for H in (2*a+4, 2*a+10)]
    balls = []
    for J in range(9):
        M = 8**J
        cap = (isqrt(1+4*M)-1)//2
        values = [[n, psi(n)] for n in range(2, cap+1) if psi(n) <= M]
        need(len(values) < 5*(J+1)*2**J, 'sublevel bound')
        tail = Fraction(40*(3*J+7), 9*4**J)
        partial = sum((Fraction(10*(i+2), 4**i) for i in range(J, J+32)), Fraction())
        remainder = Fraction(40*(3*(J+32)+7), 9*4**(J+32))
        need(partial+remainder == tail, 'entire tail identity')
        balls.append([J, M, cap, values, [tail.numerator, tail.denominator]])
    control = dict(mixed_rank_cycle=[11, 17, rank(11)[0], rank(17)[0], psi(11), psi(17)],
                   missing_ternary_guard=[3, '1', 2, 5, 3])
    need(T(11) == 17 and rank(11)[0] > rank(17)[0] and psi(11) < psi(17), 'mixed-rank control')
    need((2*3-1) % 3 != 0, 'invalid inverse guard control')
    full = dict(core=rows, unit_spikes=units, mersenne=mersenne, long_suffixes=longs,
                balls=balls, controls=control)
    body = dict(schema='X-ASR-001-v1', base=BASE, apr_source=APR,
                scope=dict(collatz_proved=False, universal_normalizer=False,
                           all_parameter_proofs='PROPOSED', raw_T_after_one=True,
                           zero_displacements='omitted', common_rank='(n+1)*Gamma(n)'),
                core=dict(cutoff=LIMIT, sources=LIMIT-1, counts=dict(sorted(counts.items())),
                          suffix_checks=checks, length_one_sources=length_one,
                          first_unresolved=residual[:24], rows_sha256=sha(rows)),
                unit_spikes=dict(heights=list(range(1, 41)), rows_sha256=sha(units), examples=units[:3]),
                mersenne=dict(exponents=list(range(2, 65)), phases=phase_count,
                              rows_sha256=sha(mersenne)),
                long_suffixes=dict(cases=len(longs), rows_sha256=sha(longs), examples=longs[:1]),
                balls=[dict(J=z[0], M=z[1], complete_source_cap=z[2], sources=len(z[3]),
                            rows_sha256=sha(z[3]), reciprocal_tail=z[4]) for z in balls],
                controls=control, full_sha256=sha(full))
    return dict(body=body, sha256=sha(body)), full


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check', type=Path)
    p.add_argument('--output', type=Path)
    p.add_argument('--full-output', type=Path)
    a = p.parse_args()
    report, full = reconstruct()
    if a.check:
        need(encoded(json.loads(a.check.read_text())) == encoded(report), 'canonical typed mismatch')
    for path, obj in ((a.output, report), (a.full_output, full)):
        if path:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(encoded(obj)+b'\n')
    print('PASS', report['sha256'])
    print(json.dumps(report['body']['core'], sort_keys=True))


if __name__ == '__main__':
    main()
