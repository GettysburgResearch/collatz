#!/usr/bin/env python3
"""Finite exact regression evidence; the universal claims are written proofs."""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path

SCHEMA = 'X-ASTRA3-002/v1'
SCOPE = 'finite exact checks only; no Collatz proof or independent mathematical review'


def digest(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def vp(n: int, p: int) -> int:
    if n == 0:
        raise ValueError('valuation at zero')
    n = abs(n)
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def T(n: int) -> int:
    return (3*n+1)//2 if n % 2 else n//2


def F(n: int) -> int:
    a = vp(n+1, 2)
    z = 3**a * ((n+1)//2**a)-1
    return z//2**vp(z, 2)


def compositions(total: int, length: int, prefix: tuple[int, ...] = ()):
    if length == 1:
        yield prefix+(total,)
    else:
        for a in range(1, total-length+2):
            yield from compositions(total-a, length-1, prefix+(a,))


def cylinder_checks() -> dict:
    rows = []
    replays = 0
    for A in range(1, 12):
        for q in range(1, min(A, 5)+1):
            for word in compositions(A, q):
                B = used = 0
                for a in word:
                    B = 3*B+2**used
                    used += a
                modulus = 2**(A+1)
                root = ((2**A-B)*pow(3**q, -1, modulus)) % modulus
                assert root % 2 == 1
                assert B*2**q <= (3**q-2**q)*2**A
                endpoints = []
                for lift in (0, 1, 3):
                    n = root+modulus*lift
                    x = n
                    actual = []
                    for _ in word:
                        y = 3*x+1
                        a = vp(y, 2)
                        actual.append(a)
                        x = y//2**a
                    assert tuple(actual) == word
                    assert x*2**A == 3**q*n+B
                    endpoints.append(x)
                    replays += 1
                rows.append([list(word), B, root, endpoints])
    tail_rows = []
    for q in range(1, 65):
        m = 5*q//3
        tail = sum((Fraction(comb(A-1, q-1), 2**A) for A in range(q, m+1)), Fraction())
        assert tail**3 <= Fraction(3125, 3456)**q
        tail_rows.append([q, m, tail.numerator, tail.denominator])
    assert 8*3125**24 < 3456**24
    assert 3**200 < 2**317
    assert 317**6340 < 2**6023*117**2340*200**4000
    # Exact parent margin, without evaluating irrational powers.
    assert Fraction(177, 500)**2 > Fraction(1, 8)
    assert Fraction(463, 250)**2 > Fraction(98, 65)**3
    assert Fraction(177, 500)+Fraction(463, 250)*Fraction(69, 200) < Fraction(993, 1000)
    return dict(words=len(rows), ordinary_replays=replays, max_total=11, max_odd_depth=5,
                cylinder_digest=digest(rows), tail_cases=len(tail_rows), tail_digest=digest(tail_rows),
                integer_certificates=6)


def correction_checks() -> dict:
    rows = []
    positions = 0
    for n in range(3, 516, 2):
        x = n
        C = P = Fraction(1)
        seen = set()
        minimum = x
        odd = 0
        for k in range(129):
            assert Fraction(x) == n*C*P
            if x in seen or k == 128:
                rows.append([n, k, minimum, odd, C.numerator, C.denominator, P.numerator, P.denominator])
                break
            seen.add(x)
            minimum = min(minimum, x)
            if x % 2:
                P *= Fraction(3*x+1, 3*x)
                C *= Fraction(3, 2)
                odd += 1
            else:
                C /= 2
            x = T(x)
            positions += 1
    core = []
    for n in range(1, 65):
        x, k = n, 0
        while x != 1:
            x = T(x)
            k += 1
            assert k <= 1000
        core.append(k)
    return dict(sources=len(rows), positions=positions, max_horizon=128, digest=digest(rows),
                core_hitting_times=core)


def first_crossings(limit: int):
    def walk(word, P, Q, A, prefixes):
        if word and Q < P:
            yield word, P, Q, A, prefixes
            return
        if len(word) >= limit:
            return
        for bit in (0, 1):
            p, q, a = 2*P, (3 if bit else 1)*Q, (3 if bit else 1)*A+bit*P
            yield from walk(word+(bit,), p, q, a, prefixes+[(p, q, a)])
    yield from walk((), 1, 1, 0, [])


def echo_checks() -> dict:
    rows = []
    hist = Counter()
    signs = Counter()
    total_words = integer = old = cycles = integer_cycles = steps = 0
    for word, P, Q, A, prefixes in first_crossings(21):
        total_words += 1
        D = P-Q
        if A > 0:
            cycles += 1
            integer_cycles += int(A % D == 0)
            x = A
            for bit in word:
                assert x % 2 == bit
                x = (3*x+D)//2 if bit else x//2
                assert x >= A
            assert x == A
        for d in range(1, (A+P-1)//P):
            R, Y = A-P*d, A-Q*d
            assert R > 0
            integral = R % D == 0
            assert integral == (D == 1 or d % D == (A*pow(P, -1, D)) % D)
            integer += int(integral)
            t = vp(d, 2)
            first_echo = False
            if t < len(word) and word[t] == 1:
                pt, qt, at = (1, 1, 0) if t == 0 else prefixes[t-1]
                first_echo = (2*pt-qt)*R > D*(qt*d+at)
            old += int(first_echo)
            pu = qu = 1
            au = 0
            exit_time = 0
            for k in range(1, 2*len(word)+1):
                bit = Y % 2
                Y = (3*Y+D)//2 if bit else Y//2
                au = (3 if bit else 1)*au+bit*pu
                qu *= 3 if bit else 1
                pu *= 2
                residue = (-au*pow(qu, -1, pu)) % pu
                assert d % pu == (pow(Q, -1, pu)*(A-D*residue)) % pu
                coefficient = P*pu-Q*qu
                signs['positive' if coefficient > 0 else 'negative' if coefficient < 0 else 'zero'] += 1
                gap = coefficient*d-((pu-qu)*A-D*au)
                assert gap == pu*(Y-R)
                steps += 1
                if Y < R:
                    exit_time = k
                    break
            if first_echo:
                assert exit_time and exit_time <= t+1
            hist[exit_time] += 1
            rows.append([''.join(map(str, word)), d, int(first_echo), exit_time])
    pre = [61,239,506,253,527,938,469,851,1424,712,356,178,89]
    cyc = [281,569,1001,1649,2621,4079,6266,3133,4847,7418,3709,5711,8714,4357,6683,
           10172,5086,2543,3962,1981,3119,4826,2413,3767,5798,2899,4496,2248,1124,562]
    seq = pre+cyc
    for x, y in zip(seq, seq[1:]+[cyc[0]]):
        assert y == ((3*x+295)//2 if x % 2 else x//2)
    assert len(set(seq)) == len(seq) and min(seq) == 61
    assert seq[10]-seq[0] == 295
    return dict(limit=21, words=total_words, positive_pairs=len(rows), integer_sources=integer,
                old_rejections=old, continuation_rejections=len(rows)-hist[0], remaining=hist[0],
                steps=steps, coefficient_signs=dict(sorted(signs.items())), histogram={str(k): v for k, v in sorted(hist.items())}, digest=digest(rows),
                rational_cycles=cycles, integer_cycles=integer_cycles,
                rational_countermodel=dict(denominator=295, preperiod=pre, period=cyc))


PROFILES = [
    [[2, -1, 2, 1]], [[2, -1, 2, -1]], [[3, -1, 2, 1]], [[3, -1, 2, -1]],
    [[2, -1, 3, 1]], [[2, -1, 3, -1]],
    [[2, -1, 2, 0]], [[3, -1, 2, 0]],
    [[2, -1, 2, -1], [3, -1, 3, 1]],
]


def rank_increases(n: int, y: int, profile: list) -> bool:
    top, bottom = y, n
    for p, root, power, sign in profile:
        a, b = vp(n-root, p), vp(y-root, p)
        fa = (sign if sign else (-1)**a)*a**power
        fb = (sign if sign else (-1)**b)*b**power
        e = fb-fa
        if e >= 0:
            top *= p**e
        else:
            bottom *= p**(-e)
    return top > bottom


def candidates():
    for k in range(8, 65):
        for c in range(1, 9):
            for p in (2, 3, 5):
                x = c*p**k-1
                yield x
                for ell in (1, 2, 4):
                    yield 2**ell*x
                    if x % 2**ell == 0:
                        yield x//2**ell
            yield c*8*3**(k-1)-3
            if (4*(c*2**k-1)-1) % 3 == 0:
                yield (4*(c*2**k-1)-1)//3


def rank_checks() -> dict:
    pending = {(i, mode) for i in range(len(PROFILES)) for mode in (1, 2, 4, 'macro')}
    rows = []
    for n in candidates():
        if n <= 10**6:
            continue
        for i, mode in sorted(pending.copy(), key=lambda x: (x[0], str(x[1]))):
            if mode == 'macro':
                if n % 2 == 0:
                    continue
                y = F(n)
            else:
                y = n
                for _ in range(mode):
                    y = T(y)
            if y <= 10**6:
                continue
            if rank_increases(n, y, PROFILES[i]):
                rows.append(dict(profile=i, mode=mode, source=n, endpoint=y))
                pending.remove((i, mode))
        if not pending:
            break
    if pending:
        raise AssertionError(('missing rank controls', pending))
    rows.sort(key=lambda x: (x['profile'], str(x['mode'])))
    return dict(profiles=PROFILES, floor=10**6, witnesses=rows, count=len(rows))


def build() -> dict:
    payload = dict(schema=SCHEMA, scope=SCOPE, cylinders=cylinder_checks(),
                   corrections=correction_checks(), echoes=echo_checks(), ranks=rank_checks())
    return dict(payload=payload, sha256=digest(payload))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--check', type=Path)
    args = parser.parse_args()
    report = build()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    if args.check and report != json.loads(args.check.read_text()):
        raise SystemExit('certificate mismatch')
    print('PASS', report['sha256'])
    print(json.dumps({k: v for k, v in report['payload'].items() if k not in ('ranks', 'echoes')}, sort_keys=True))
    print('echoes', report['payload']['echoes']['continuation_rejections'], 'rank witnesses', report['payload']['ranks']['count'])


if __name__ == '__main__':
    main()
