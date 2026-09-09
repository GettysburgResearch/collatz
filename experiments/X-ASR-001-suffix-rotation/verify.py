#!/usr/bin/env python3
"""Separate affine-rank and literal reverse-word reconstruction. No run import."""
from __future__ import annotations
import argparse
import copy
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from math import isqrt
from pathlib import Path

BASE = 'ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a'
APR = '7b7471ea0e7b359a2ac46fb1e6aff269331509c3'


def check(condition: bool, reason: str) -> None:
    if not condition:
        raise ValueError(reason)


def code(x: object) -> bytes:
    return json.dumps(x, separators=(',', ':'), sort_keys=True, allow_nan=False).encode()


def seal(x: object) -> str:
    return hashlib.sha256(code(x)).hexdigest()


def order3(x: int) -> int:
    check(x != 0, 'undefined valuation')
    power, e = 3, 0
    while x % power == 0:
        power *= 3
        e += 1
    return e


def weight(x: int) -> int:
    return x*x//3**order3(x)


def step(x: int) -> int:
    check(x > 0, 'positive physical source')
    return (x+(x % 2)*(2*x+1))//2


@lru_cache(None)
def gamma(n: int) -> tuple[int, tuple]:
    check(type(n) is int and n > 0, 'rank domain')
    if n == 1:
        return 0, ()
    baseline = weight(n)
    candidates = [(baseline, (0, '', n, order3(n)))]
    # Full baseline window, not a current-minimum stopping condition.
    kmax, power = 0, 4
    while power <= baseline:
        kmax += 1
        power *= 4
    q = A = 0
    x, word = n, ''
    for i in range(kmax):
        bit = x % 2
        word += str(bit)
        A = (3 if bit else 1)*A + bit*2**i
        q += bit
        x = step(x)
        Z = (3**q-2**(i+1))*n+A
        check(2**(i+1)*x == 3**q*n+A, 'affine prefix reconstruction')
        if Z:
            d = x-n
            candidates.append((weight(Z), (i+1, word, d, order3(d))))
    best = min(v for v, _ in candidates)
    check(n <= best <= n*n, 'properness control')
    return best, tuple(t for v, t in candidates if v == best)


def p(n: int) -> int:
    return (n+1)*gamma(n)[0]


def follow(n: int, word: str) -> int:
    for b in word:
        check(str(n % 2) == b, 'wrong actual bit')
        n = step(n)
    return n


def backwards(n: int, word: str) -> int:
    x = F(n)
    for b in reversed(word):
        x = 2*x if b == '0' else (2*x-1)/3
        check(x.denominator == 1 and x > 0, 'nonordinary reverse source')
        check(int(x) % 2 == int(b), 'reverse parity')
    return int(x)


def parameters(word: str) -> tuple[int, int, int, int]:
    slope, offset = F(1), F(0)
    for b in word:
        if b == '0':
            slope, offset = slope/2, offset/2
        else:
            slope, offset = 3*slope/2, (3*offset+1)/2
    P = 2**len(word)
    Q, A = slope*P, offset*P
    check(Q.denominator == A.denominator == 1, 'affine denominator')
    return P, int(Q), int(A), word.count('1')


def possibilities(n: int) -> tuple[list, list, int]:
    G, winners = gamma(n)
    fs, bs, checked = [], [], 0
    K = 1
    while 4**(K+1) <= weight(n):
        K += 1
    x, word = n, ''
    for j in range(1, K+1):
        word += str(x % 2)
        x = step(x)
        if p(x) < p(n):
            fs.append([x, j, word])
    for k, w, d, h in winners:
        for r in range(1, k+1):
            u, v = w[:k-r], w[k-r:]
            P, Q, A, a = parameters(v)
            if a > h:
                continue
            x = backwards(n, v)
            check(Q*x+A == P*n and x <= n*n, 'inverse source formula')
            z = follow(n, u)
            check(follow(x, v+u) == z and Q*(z-x) == P*d, 'physical rotation')
            check(Q*4**k*weight(z-x) == P*P*G, 'rank transport')
            check(Q*gamma(x)[0] <= P*P*G, 'candidate upper bound')
            E = A+P-Q
            check(E >= 0 and Q*(x+1)+E == P*(n+1), 'shifted affine identity')
            check(Q*Q*p(x) <= P**3*p(n), 'common-rank inequality')
            analytic = 9**a > 8**r
            if analytic:
                check(x < n and p(x) < p(n), 'analytic strictness')
            if p(x) < p(n):
                bs.append([x, r, v, k, analytic])
            checked += 1
    return fs, bs, checked


def modular_inverse(a: int, m: int) -> int:
    r0, r1, s0, s1 = a, m, 1, 0
    while r1:
        q = r0//r1
        r0, r1, s0, s1 = r1, r0-q*r1, s1, s0-q*s1
    check(r0 == 1, 'non-coprime fixture congruence')
    return s0 % m


def long_fixture(a: int, H: int) -> list:
    w = '1'*a+'0'
    P, Q, A = 2**(a+1), 3**a, 3**a-2**a
    D = Q-P
    for N in range(2, 33):
        C = P**N*3**H
        residue = A*modular_inverse(C, D) % D
        choices = [residue+t*D for t in range(7)]
        u = min(z for z in choices if z > 0 and z % 6 in (1, 5))
        n, rem = divmod(C*u-A, D)
        check(rem == 0 and follow(n, w*N) > 0, 'finite source construction')
        G, winners = gamma(n)
        if any(row[1] == w for row in winners):
            x = backwards(n, w)
            check(Q*Q > P**3 and Q*Q*p(x) <= P**3*p(n), 'long suffix certificate')
            return [a, H, N, u, n, x, G, p(x)]
    raise ValueError('finite long fixture budget exhausted')


def reconstruct() -> tuple[dict, dict]:
    rows, counts, residual = [], Counter(), []
    checked = singles = 0
    for n in range(2, 8193):
        G, wins = gamma(n)
        fs, bs, c = possibilities(n)
        checked += c
        tag = 'forward' if fs else 'backward_only' if bs else 'unresolved'
        counts[tag] += 1
        if tag == 'unresolved':
            residual.append(n)
        if any(t[0] == 1 for t in wins):
            check(bool(fs or bs), 'all one-letter minima covered')
            singles += 1
        choices = [[p(x), x, j, 'forward', w] for x, j, w in fs]
        choices += [[p(x), x, r, 'backward', v] for x, r, v, _, _ in bs]
        if choices:
            _, x, clock, direction, word = sorted(choices)[0]
            chosen = dict(status='REDUCED', x=x, clock=clock, direction=direction, word=word)
            check(p(x) < p(n), 'selected decrease')
        else:
            chosen = {'status': 'UNRESOLVED'}
        rows.append([n, G, [list(t) for t in wins], fs, bs, chosen])
    units = []
    for H in range(1, 41):
        n = 2*3**H-1
        y, x = step(n), backwards(n, '1')
        G, wins = gamma(n)
        check(G == 4*3**H and len(wins) == 1 and wins[0][0] == 1, 'unit source rank')
        check(gamma(y)[0]**10 > n**11 and 9*p(x) <= 8*p(n), 'spike and bypass')
        units.append([H, n, y, x, G, gamma(y)[0], p(n), p(x)])
    mersenne, phases_total = [], 0
    for L in range(2, 65):
        n = 2**L-1
        G, wins = gamma(n)
        check(G == weight(n) and len(wins) == 1 and wins[0][0] == 0, 'baseline unique')
        fs, bs, _ = possibilities(n)
        check(not fs and not bs, 'normalizer unexpectedly succeeds')
        phases = []
        for j in range(1, L):
            x = follow(n, '1'*j)
            check(x == 3**j*2**(L-j)-1 and p(x) > p(n), 'every early rank is higher')
            phases.append([j, x, p(x)])
        phases_total += len(phases)
        mersenne.append([L, n, G, phases])
    longs = [long_fixture(a, H) for a in (18, 19, 24, 32) for H in (2*a+4, 2*a+10)]
    balls = []
    for J in range(9):
        M = 8**J
        cap = isqrt(M)
        if cap*(cap+1) > M:
            cap -= 1
        check(cap*(cap+1) <= M < (cap+1)*(cap+2), 'complete cap')
        values = [[n, p(n)] for n in range(2, cap+1) if p(n) <= M]
        check(len(values) < 5*(J+1)*2**J, 'spectrum inequality')
        # Infinite arithmetic-geometric series: sum x^r and sum r*x^r.
        tail = 10*F(1, 4**J)*((J+2)*F(4, 3)+F(4, 9))
        balls.append([J, M, cap, values, [tail.numerator, tail.denominator]])
    control = dict(mixed_rank_cycle=[11, 17, gamma(11)[0], gamma(17)[0], p(11), p(17)],
                   missing_ternary_guard=[3, '1', 2, 5, 3])
    check(step(11) == 17 and gamma(11)[0] > gamma(17)[0] and p(11) < p(17), 'incompatible ranks')
    check(F(2*3-1, 3).denominator == 3, 'missing guard is nonintegral')
    full = dict(core=rows, unit_spikes=units, mersenne=mersenne, long_suffixes=longs,
                balls=balls, controls=control)
    b = dict(schema='X-ASR-001-v1', base=BASE, apr_source=APR,
             scope=dict(collatz_proved=False, universal_normalizer=False, all_parameter_proofs='PROPOSED',
                        raw_T_after_one=True, zero_displacements='omitted', common_rank='(n+1)*Gamma(n)'),
             core=dict(cutoff=8192, sources=8191, counts=dict(sorted(counts.items())),
                       suffix_checks=checked, length_one_sources=singles,
                       first_unresolved=residual[:24], rows_sha256=seal(rows)),
             unit_spikes=dict(heights=list(range(1, 41)), rows_sha256=seal(units), examples=units[:3]),
             mersenne=dict(exponents=list(range(2, 65)), phases=phases_total, rows_sha256=seal(mersenne)),
             long_suffixes=dict(cases=len(longs), rows_sha256=seal(longs), examples=longs[:1]),
             balls=[dict(J=z[0], M=z[1], complete_source_cap=z[2], sources=len(z[3]),
                         rows_sha256=seal(z[3]), reciprocal_tail=z[4]) for z in balls],
             controls=control, full_sha256=seal(full))
    return dict(body=b, sha256=seal(b)), full


def validate(actual: dict, expected: dict) -> None:
    check(set(actual) == {'body', 'sha256'}, 'invalid top-level keys')
    check(actual['sha256'] == seal(actual['body']), 'invalid digest')
    check(code(actual) == code(expected), 'typed mathematical or coverage reconstruction mismatch')


def self_test(expected: dict) -> int:
    mutations = [
        lambda b: b['scope'].update(collatz_proved=True),
        lambda b: b['scope'].update(universal_normalizer=True),
        lambda b: b['core'].update(cutoff=8192.0),
        lambda b: b['balls'][0].update(J=False),
        lambda b: b['scope'].update(raw_T_after_one=1),
        lambda b: b['core']['counts'].update(unresolved=0),
        lambda b: b['unit_spikes']['examples'][1].__setitem__(3, 17),
        lambda b: b['mersenne']['exponents'].pop(),
        lambda b: b['long_suffixes'].update(cases=7),
        lambda b: b['balls'][3].__setitem__('reciprocal_tail', [0, 1]),
        lambda b: b['controls']['mixed_rank_cycle'].__setitem__(2, 47),
        lambda b: b['core'].update(suffix_checks=b['core']['suffix_checks']-1),
    ]
    for mutate in mutations:
        altered = copy.deepcopy(expected)
        mutate(altered['body'])
        check(code(altered['body']) != code(expected['body']), 'no-op mutation')
        altered['sha256'] = seal(altered['body'])
        try:
            validate(altered, expected)
        except ValueError as error:
            check('reconstruction' in str(error), 'rejected by digest alone')
        else:
            raise ValueError('resealed corruption accepted')
    return len(mutations)


def main() -> None:
    a = argparse.ArgumentParser(description=__doc__)
    a.add_argument('report', type=Path)
    a.add_argument('--self-test', action='store_true')
    a.add_argument('--output', type=Path)
    a.add_argument('--full-output', type=Path)
    args = a.parse_args()
    expected, full = reconstruct()
    validate(json.loads(args.report.read_text()), expected)
    for path, obj in ((args.output, expected), (args.full_output, full)):
        if path:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(code(obj)+b'\n')
    print('SEPARATE RECONSTRUCTION PASS', expected['sha256'])
    if args.self_test:
        print('RESEALED CORRUPTIONS REJECTED', self_test(expected))


if __name__ == '__main__':
    main()
