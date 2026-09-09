#!/usr/bin/env python3
"""ATT-301--306 finite exact regressions. No repository imports; not Collatz closure."""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

PARENT = '912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe'
SCHEMA = 'ATT-reverse-realization/v1'
N = 4096
MAX_L = (4*N-1).bit_length()-1


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sha(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def valuation(z):
    z = abs(z)
    need(z > 0, 'zero valuation')
    e = 0
    while z % 3 == 0:
        e += 1
        z //= 3
    return e


def g(z):
    return 0 if z == 0 else z*z // 3**valuation(z)


def T(n):
    return (3*n+1)//2 if n & 1 else n//2


def path(n, w):
    for b in w:
        need(n % 2 == int(b), 'illegal word')
        n = T(n)
    return n


def words():
    front = [(1, 1, 0, '')]
    out, counts = [], []
    for L in range(1, MAX_L+1):
        nxt, level = [], []
        for P, D, A, w in front:
            for b in (0, 1):
                p, d, a, v = P*3**b, D*2, A*3**b+b*D, w+str(b)
                nxt.append((p, d, a, v))
                if 4*p >= 5*d:
                    need(3*(p-d)**2 >= p, 'spacing inequality')
                    level.append((v, p, d, a))
        out.extend(sorted(level))
        counts.append([L, len(level)])
        front = nxt
    return out, counts


def base(n):
    return [('B0', g(n)), ('B1', g(n-1)), ('B2', g(n+5))]


def build():
    table, counts = words()
    qualifying, rank_rows = [], []
    by_end = {}
    for n in range(2, N+1):
        vals = base(n)
        for w, P, D, A in table:
            if D >= 4*n:
                break
            z = (P-D)*n+A
            if z > n*n:
                continue
            value = g(z)
            if value <= n*n:
                e = valuation(z)
                q = w.count('1')
                need(e >= q and (D*n-A) % P == 0, 'integrality gate')
                x = (D*n-A)//P
                need(0 < x < n and 5*x < 4*n, 'inverse decrease')
                need(path(x, w) == n, 'inverse physical replay')
                row = [n, w, x, q, e, value]
                qualifying.append(row)
                by_end.setdefault(n, []).append(row)
                vals.append(('W:'+w, value))
        best = min(v for _, v in vals)
        tags = sorted(t for t, v in vals if v == best)
        need(n-1 <= best <= n*n, 'proper rank')
        rank_rows.append([n, best, tags])
    qualifying.sort(key=lambda r: (r[0], len(r[1]), r[1]))
    rank_map = {r[0]: r[1] for r in rank_rows}

    def edge(n):
        if n == 1:
            return ('CORE', 1, '', 0)
        if n % 2 == 0:
            return ('E', n//2, '0', 1)
        if n % 4 == 1:
            return ('F10', (3*n+1)//4, '10', 1)
        if n % 3 == 2:
            return ('I1', (2*n-1)//3, '1', -1)
        if (n+5) % 9 == 0:
            return ('I110', (8*n-5)//9, '110', -1)
        if n in by_end:
            row = min(by_end[n], key=lambda r: (len(r[1]), r[1]))
            return ('IW', row[2], row[1], -1)
        return ('RESIDUAL', n, '', 0)

    edge_rows, normalized, histogram = [], [], Counter()
    for n in range(2, N+1):
        typ, x, w, direction = edge(n)
        histogram[typ] += 1
        edge_rows.append([n, typ, x, w, direction])
        if direction:
            need(9*x < 8*n, 'uniform size contraction')
            need(path(n if direction == 1 else x, w) == (x if direction == 1 else n), 'edge replay')
        else:
            need(n % 36 in (3, 7, 15, 19, 27), 'residual residue')
            need(rank_map[n] == (g(n) if n % 3 == 0 else g(n-1)), 'residual rank')
        cur, clock, peak_clock, budget, steps = n, 0, 0, 0, 0
        while True:
            kind, nxt, word, sign = edge(cur)
            if not sign:
                break
            clock += sign*len(word)
            peak_clock = max(peak_clock, clock)
            budget += len(word)
            steps += 1
            cur = nxt
        r, s = peak_clock, peak_clock-clock
        a, b = n, cur
        for _ in range(r): a = T(a)
        for _ in range(s): b = T(b)
        need(a == b and r+s <= budget, 'composed physical merging')
        need(9**steps < n*8**steps, 'normalizer length bound')
        normalized.append([n, cur, r, s, a, steps, budget])

    # These are complete rank balls: rho(n)>=n-1 bounds all possible sources.
    balls = []
    for X in (64, 256, 1024, 4095):
        rows = [[n, r] for n, r, _ in rank_rows if r <= X]
        need(all(n <= X+1 for n, _ in rows), 'rank-ball completeness')
        balls.append({'X': X, 'count': len(rows), 'max_source': max(n for n, _ in rows), 'sha256': sha(rows)})

    families = []
    for h in (21, 37, 53, 69, 85, 101):
        n = (3**h-73)//17
        x = (64*n-73)//81
        need(17*n+73 == 3**h and 81*x+73 == 64*n, 'exit family identities')
        need(n % 2 == 0 and path(x, '111010') == n and 5*x < 4*n, 'exit family inverse')
        need(g(17*n+73) <= n*n, 'low component')
        comparison = None
        if h >= 37:
            e, u = h-4, 64
            need(e >= 13 and 2**e > 2176*u, 'parent all-word minimum premises')
            comparison = [3**h, 4096*3**(h-4)]
            need(comparison[1] > comparison[0], 'orders must differ')
        families.append([h, n, x, comparison])

    odd_families = []
    for e in (25, 41, 57, 73, 89):
        n = (4*3**e-73)//17
        x = (64*n-73)//81
        need(17*n+73 == 4*3**e and 17*x+73 == 256*3**(e-4), 'odd family identity')
        need(n % 36 == 19 and n % 8 == 3 and path(x, '111010') == n, 'odd illegal-minimum bridge')
        need(2**e > 2176*4 and e-4 >= 13 and 2**(e-4) > 2176*256, 'both exact minimum premises')
        rn, rx = 16*3**e, 65536*3**(e-4)
        need(rn <= n*n and rx*81 == rn*4096 and 5*x < 4*n, 'different orders')
        odd_families.append([e, n, x, rn, rx])

    echoes = []
    for K in (1, 2, 4, 8, 16, 32, 64):
        modulus = 2**(K+2)
        seed = next(mult*modulus-1 for mult in (1, 2, 3) if (mult*modulus-1) % 3 == 0)
        for shift in range(3):
            n = seed + shift*3*modulus
            cur = n
            transcript = []
            for j in range(1, K+1):
                cur = T(cur)
                need(cur % 4 == 3 and cur % 3 == 2, 'echo priority guards')
                z = cur
                for _ in range(j):
                    need(z % 4 == 3 and z % 3 == 2, 'inverse echo guards')
                    z = (2*z-1)//3
                need(z == n and n % 3 == 0 and n % 4 == 3, 'echo residual')
                transcript.append([j, cur, z])
            echoes.append([K, shift, n, sha(transcript)])

    # 110 is too close to coefficient 1 to satisfy the spacing hypothesis.
    controls = {'nearcritical': [7, '110', 9, 8, 5, 12, 48, 17, 3],
                'generic_bridge': [1711, 1351, '111010'],
                'administrative_loop': [7, 11, 7],
                'scope': 'positive backward descent is not forward rho descent; residual coverage OPEN'}
    need(g(12) == 48 <= 49 and 8*7-5 == 51, 'nearcritical control')
    need(path(1351, '111010') == 1711, 'generic bridge')

    constants = [59768833, 2*29**20-30**20, 2**19*3**20-5**20,
                 8**6-350*3**6]
    need(all(v > 0 for v in constants), 'analytic constants')
    return {'schema': SCHEMA, 'parent': PARENT, 'N': N, 'max_word_length': MAX_L,
            'scope': 'bounded exact replay; universal claims require the written proofs; no full Collatz proof',
            'word_counts': counts, 'constants': constants,
            'qualifying': {'count': len(qualifying), 'sha256': sha(qualifying)},
            'ranks': {'count': len(rank_rows), 'sha256': sha(rank_rows)},
            'edges': {'counts': dict(sorted(histogram.items())), 'sha256': sha(edge_rows)},
            'normalizer': {'count': len(normalized), 'to_core': sum(r[1] == 1 for r in normalized),
                           'max_edges': max(r[5] for r in normalized),
                           'max_clock_sum': max(r[2]+r[3] for r in normalized),
                           'sha256': sha(normalized)},
            'rank_balls': balls, 'exit_families': families, 'odd_illegal_families': odd_families,
            'large_rank_scope': 'rank comparison checks parent ATT-204 sufficient premises, not exhaustive large dictionary evaluation',
            'echoes': echoes, 'controls': controls}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write', type=Path)
    ap.add_argument('--check', type=Path)
    args = ap.parse_args()
    payload = build()
    report = {'payload': payload, 'sha256': sha(payload)}
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(report, sort_keys=True, separators=(',', ':'))+'\n', encoding='utf-8')
    if args.check:
        need(json.loads(args.check.read_text(encoding='utf-8')) == report, 'canonical payload mismatch')
    print('GENERATOR PASS', report['sha256'])
    print(json.dumps({k: payload[k] for k in ('qualifying', 'edges', 'normalizer', 'rank_balls')}, sort_keys=True))

if __name__ == '__main__':
    main()
