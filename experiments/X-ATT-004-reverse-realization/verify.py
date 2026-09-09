#!/usr/bin/env python3
"""Independent-implementation bounded replay via actual positive orbit ancestors.

No generator or repository import. This does not independently peer-review
ATT-301--306. Only the supplied finite protocol and stated large-case premises
are checked. All checks remain active under -O and -OO.
"""
from __future__ import annotations
import argparse
from collections import Counter
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path

PARENT = '912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe'
N = 4096
LIMIT = 13


def check(ok, message):
    if not ok:
        raise RuntimeError(message)


def digest(x):
    return sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def step(x):
    return x//2 if x % 2 == 0 else (3*x+1)//2


def strip(z):
    z = abs(z)
    check(z > 0, 'zero valuation')
    e = 0
    while True:
        quotient, remainder = divmod(z, 3)
        if remainder:
            return e, z
        e, z = e+1, quotient


def rank_component(z):
    if not z:
        return 0
    e, unit = strip(z)
    return 3**e*unit**2


def trajectory(x, k):
    seq, word = [x], ''
    for _ in range(k):
        word += str(seq[-1] % 2)
        seq.append(step(seq[-1]))
    return seq, word


def replay():
    # Actual residue representatives reconstruct ALL finite parity words.
    counts = []
    for L in range(1, LIMIT+1):
        good = set()
        all_words = set()
        for seed in range(2**L):
            seq, w = trajectory(seed, L)
            all_words.add(w)
            q = w.count('1')
            P, D = 3**q, 2**L
            A = D*seq[-1]-P*seed
            if 4*P >= 5*D:
                check(A > 0 and 3*(P-D)**2 >= P, 'word constants')
                good.add(w)
        check(len(all_words) == 2**L, 'parity completeness')
        counts.append([L, len(good)])

    # This is deliberately NOT formal-word minimization at each endpoint.
    rows = []
    by_endpoint = {}
    for x in range(1, N):
        y, q, word = x, 0, ''
        for L in range(1, LIMIT+1):
            bit = y % 2
            word += str(bit)
            q += bit
            y = step(y)
            if not (2 <= y <= N and 2**L < 4*y and 4*3**q >= 5*2**L):
                continue
            check(y > x, 'expansion must increase ordinary source')
            gap = y-x
            value = 3**q*rank_component(gap)
            if value > y*y:
                continue
            e = q+strip(gap)[0]
            row = [y, word, x, q, e, value]
            check(5*x < 4*y, 'inverse contraction')
            rows.append(row)
            by_endpoint.setdefault(y, []).append(row)
    rows.sort(key=lambda r: (r[0], len(r[1]), r[1]))
    check(len({(r[0], r[1]) for r in rows}) == len(rows), 'duplicate inverse word')
    rank_rows, ranks = [], {}
    for n in range(2, N+1):
        pool = [('B0', rank_component(n)), ('B1', rank_component(n-1)), ('B2', rank_component(n+5))]
        pool += [('W:'+r[1], r[-1]) for r in by_endpoint.get(n, [])]
        low = min(v for _, v in pool)
        ranks[n] = low
        rank_rows.append([n, low, sorted(t for t, v in pool if v == low)])

    edges, outcomes = [], {1: (1, [])}
    freq = Counter()
    for n in range(2, N+1):
        if n % 2 == 0:
            item = (n//2, '0', 1, 'E')
        elif n % 4 == 1:
            seq, _ = trajectory(n, 2)
            item = (seq[-1], '10', 1, 'F10')
        elif n % 3 == 2:
            item = ((2*n-1)//3, '1', -1, 'I1')
        elif n % 9 == 4:
            item = ((8*n-5)//9, '110', -1, 'I110')
        elif by_endpoint.get(n):
            chosen = min(by_endpoint[n], key=lambda r: (len(r[1]), r[1]))
            item = (chosen[2], chosen[1], -1, 'IW')
        else:
            item = (n, '', 0, 'RESIDUAL')
        x, word, direction, typ = item
        freq[typ] += 1
        edges.append([n, typ, x, word, direction])
        if direction:
            a, b = (n, x) if direction > 0 else (x, n)
            seq, bits = trajectory(a, len(word))
            check(seq[-1] == b and bits == word and 9*x < 8*n, 'actual edge')
            terminal, tail = outcomes[x]
            outcomes[n] = (terminal, [(direction, len(word))]+tail)
        else:
            check(n % 36 in {3, 7, 15, 19, 27}, 'residual classes')
            check(ranks[n] == rank_component(n if n % 3 == 0 else n-1), 'residual rank form')
            outcomes[n] = (n, [])
    normalized = []
    for n in range(2, N+1):
        terminal, segments = outcomes[n]
        position, high, total = 0, 0, 0
        for direction, length in segments:
            position += direction*length
            high = max(high, position)
            total += length
        r, s = high, high-position
        left, _ = trajectory(n, r)
        right, _ = trajectory(terminal, s)
        check(left[-1] == right[-1] and r+s <= total, 'global merging diagram')
        check(9**len(segments) < n*8**len(segments), 'well-founded clock bound')
        normalized.append([n, terminal, r, s, left[-1], len(segments), total])

    balls = []
    for X in (64, 256, 1024, 4095):
        entries = [[n, ranks[n]] for n in range(2, X+2) if ranks[n] <= X]
        balls.append({'X': X, 'count': len(entries), 'max_source': max(t[0] for t in entries), 'sha256': digest(entries)})

    families = []
    for h in (21, 37, 53, 69, 85, 101):
        n = (3**h-73)//17
        # Rational inverse evaluation follows the word in reverse order.
        numerator, denominator = n, 1
        for bit in reversed('111010'):
            if bit == '0':
                numerator *= 2
            else:
                numerator = 2*numerator-denominator
                denominator *= 3
        check(numerator % denominator == 0, 'ordinary inverse family')
        x = numerator//denominator
        seq, word = trajectory(x, 6)
        check(word == '111010' and seq[-1] == n and n % 2 == 0 and 5*x < 4*n, 'large physical family')
        check(17*n+73 == 3**h and 3**h <= n*n, 'family candidate threshold')
        comparison = None
        if h >= 37:
            check(17*x+73 == 64*3**(h-4) and h-4 >= 13 and 2**(h-4) > 2176*64, 'large rank theorem premises')
            comparison = [3**h, 4096*3**(h-4)]
            check(comparison[1] > comparison[0], 'rho must not be claimed to decrease')
        families.append([h, n, x, comparison])

    odd_families = []
    for e in (25, 41, 57, 73, 89):
        n = (4*3**e-73)//17
        x = (256*3**(e-4)-73)//17
        seq, word = trajectory(x, 6)
        actual, actual_word = trajectory(n, 3)
        check(word == '111010' and seq[-1] == n and actual_word == '110', 'odd family physical mismatch')
        check(n % 36 == 19 and 5*x < 4*n, 'ordinary decrease in residual class')
        check(17*n+73 == 4*3**e and 17*x+73 == 256*3**(e-4), 'odd affine identities')
        check(e >= 13 and 2**e > 2176*4 and e-4 >= 13 and 2**(e-4) > 2176*256, 'odd family all-word premises')
        rn, rx = rank_component(17*n+73), rank_component(17*x+73)
        check(rx*81 == rn*4096 and rn <= n*n, 'rank cannot be substituted for size')
        odd_families.append([e, n, x, rn, rx])

    echoes = []
    for K in (1, 2, 4, 8, 16, 32, 64):
        modulus = 1 << (K+2)
        # Solve n=3t=-1 mod modulus, independently of the generator's rule.
        least = 3*((-pow(3, -1, modulus)) % modulus)
        for shift in range(3):
            n = least+shift*3*modulus
            seq, word = trajectory(n, K)
            check(word == '1'*K and n % 12 == 3, 'echo source')
            transcript = []
            for j, y in enumerate(seq[1:], 1):
                check(y % 12 == 11, 'inverse-one rule precedes other rules')
                z = y
                for _ in range(j):
                    check(z % 12 == 11, 'intermediate echo guard')
                    z = (2*z-1)//3
                check(z == n, 'normalizer cancels the observed forward prefix')
                transcript.append([j, y, z])
            echoes.append([K, shift, n, digest(transcript)])

    A, B = 1, 0
    for _ in range(10):
        A, B = 2*A+3*B, A+2*B
    constants = [(2**19-A)**2-3*B*B, 2*29**20-30**20,
                 2**19*3**20-5**20, 8**6-350*3**6]
    check(all(c > 0 for c in constants), 'analytic exact margins')
    check(rank_component(12) == 48 and (8*7-5) % 9 != 0, 'gapless extension is false')
    return {'schema': 'ATT-reverse-realization/v1', 'parent': PARENT, 'N': N, 'max_word_length': LIMIT,
            'scope': 'bounded exact replay; universal claims require the written proofs; no full Collatz proof',
            'word_counts': counts, 'constants': constants,
            'qualifying': {'count': len(rows), 'sha256': digest(rows)},
            'ranks': {'count': len(rank_rows), 'sha256': digest(rank_rows)},
            'edges': {'counts': dict(sorted(freq.items())), 'sha256': digest(edges)},
            'normalizer': {'count': len(normalized), 'to_core': sum(r[1] == 1 for r in normalized),
                           'max_edges': max(r[5] for r in normalized),
                           'max_clock_sum': max(r[2]+r[3] for r in normalized), 'sha256': digest(normalized)},
            'rank_balls': balls, 'exit_families': families, 'odd_illegal_families': odd_families,
            'large_rank_scope': 'rank comparison checks parent ATT-204 sufficient premises, not exhaustive large dictionary evaluation',
            'echoes': echoes,
            'controls': {'nearcritical': [7, '110', 9, 8, 5, 12, 48, 17, 3],
                         'generic_bridge': [1711, 1351, '111010'], 'administrative_loop': [7, 11, 7],
                         'scope': 'positive backward descent is not forward rho descent; residual coverage OPEN'}}


def validate(report, expected):
    check(isinstance(report, dict) and set(report) == {'payload', 'sha256'}, 'report shape')
    check(report['sha256'] == digest(report['payload']), 'digest mismatch')
    check(report['payload'] == expected, 'reconstructed payload mismatch')


def self_test(report, expected):
    mutations = [
        lambda p: p.update(N=p['N']-1),
        lambda p: p['qualifying'].update(count=p['qualifying']['count']+1),
        lambda p: p['edges']['counts'].update(RESIDUAL=0),
        lambda p: p['ranks'].update(sha256='0'*64),
        lambda p: p['rank_balls'][0].update(max_source=1),
        lambda p: p['exit_families'][0].__setitem__(1, 2),
        lambda p: p['echoes'][0].__setitem__(2, 1),
        lambda p: p['controls'].update(scope='all sources cleared'),
        lambda p: p.update(large_rank_scope='exhaustive large dictionary verification'),
        lambda p: p['normalizer'].update(max_clock_sum=0),
        lambda p: p.update(schema=p['schema']+'-wrong'),
        lambda p: p['word_counts'].pop(),
    ]
    for alter in mutations:
        bad = deepcopy(report)
        alter(bad['payload'])
        check(bad['payload'] != report['payload'], 'no-op mutation')
        bad['sha256'] = digest(bad['payload'])
        try:
            validate(bad, expected)
        except RuntimeError:
            continue
        raise RuntimeError('resealed corruption accepted')
    print('SELF-TEST PASS:', len(mutations), 'resealed corruptions rejected')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    report = json.loads(args.report.read_text(encoding='utf-8'))
    expected = replay()
    validate(report, expected)
    if args.self_test:
        self_test(report, expected)
    print('VERIFIER PASS', digest(expected))

if __name__ == '__main__':
    main()
