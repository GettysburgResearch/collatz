#!/usr/bin/env python3
"""Exact finite regressions for ATT-201..206; NOT a Collatz proof.

No repository imports. Only --write writes the report. Exceptions remain active
under optimized Python. Large-family rank identities use the written all-word
comparison theorem; a separately labeled subset is exhaustively enumerated.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

PARENT = '73572fddd9b8b3cbd8fc03c3a992eb0735d0f62c'
SCHEMA = 'ATT-expanding-word-rank/v1'
V = '111010'
PHASES = [73, 101, 143, 206, 103, 146]
ROTATIONS = [V[j:] + V[:j] for j in range(6)]
BASES = {'B0': '0', 'B1': '10', 'B2': '110'}


def require(ok: bool, text: str) -> None:
    if not ok:
        raise ValueError(text)


def digest(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def vp(x: int, p: int) -> int:
    x = abs(x)
    require(x > 0, 'valuation of zero')
    e = 0
    while x % p == 0:
        x //= p
        e += 1
    return e


def phi(x: int) -> int:
    return 0 if x == 0 else x*x // 3**vp(x, 3)


def step(n: int) -> int:
    return (3*n+1)//2 if n % 2 else n//2


def coefficients(w: str) -> tuple[int, int, int]:
    p, d, a = 1, 1, 0
    for b in w:
        if b == '1':
            p, a = 3*p, 3*a+d
        d *= 2
    return p, d, a


def physical(n: int, w: str) -> int:
    for b in w:
        require(n % 2 == int(b), 'wrong physical bit')
        n = step(n)
    return n


class Dictionary:
    def __init__(self):
        self.levels = {}
        self.front = [(1, 1, 0, '')]
        self.depth = 0

    def extend(self, target: int) -> None:
        while self.depth < target:
            nxt, admissible = [], []
            for p, d, a, w in self.front:
                for bit in (0, 1):
                    pp, dd = p * 3**bit, 2*d
                    aa, ww = a * 3**bit + bit*d, w+str(bit)
                    nxt.append((pp, dd, aa, ww))
                    if 4*pp >= 5*dd:
                        admissible.append((ww, pp, dd, aa))
            self.depth += 1
            self.front = nxt
            self.levels[self.depth] = admissible

    def rank(self, n: int, extra: tuple[str, ...] = ()) -> tuple[int, tuple[str, ...], int]:
        if n == 1:
            return 0, ('CORE',), 0
        require(n >= 2, 'positive non-core source required')
        pool = [(phi(n), 'B0'), (phi(n-1), 'B1'), (phi(n+5), 'B2')]
        for w in ('1', *ROTATIONS, *extra):
            p, d, a = coefficients(w)
            require(4*p >= 5*d, 'invalid seed word')
            pool.append((phi((p-d)*n+a), 'W:'+w))
        best = min(x[0] for x in pool)
        tags = {t for r, t in pool if r == best}
        limit = ((4*best-1)//n).bit_length()-1
        self.extend(limit)
        for length in range(1, limit+1):
            if n*2**length >= 4*best:
                break
            for w, p, d, a in self.levels[length]:
                z = (p-d)*n+a
                if z > best:
                    continue
                rr = phi(z)
                if rr < best:
                    best, tags = rr, {'W:'+w}
                elif rr == best:
                    tags.add('W:'+w)
        return best, tuple(sorted(tags)), limit


def old_rank(n: int) -> int:
    if n == 1:
        return 0
    h = vp(2*n+1, 3)
    inds = {0, 1, 2}
    if h >= 3:
        inds.add(h)
    return min(phi((3**a-2**(a+1))*n+3**a-2**a) for a in inds)


def old_accel(n: int) -> int:
    if n == 1:
        return 1
    a = vp(n+1, 2) if n % 2 else 0
    p, d, c = 3**a, 2**(a+1), 3**a-2**a
    z = (p-d)*n+c
    k = vp(z, 2)//(a+1)
    require(k >= 1, 'empty maximal module')
    zz = p**k*(z//d**k)
    require((zz-c) % (p-d) == 0, 'nonintegral module endpoint')
    return (zz-c)//(p-d)


def phase_lower_contract(n: int, a: int, e: int, u: int) -> int:
    """Check sufficient finite premises of ATT-204, not every word individually."""
    require(17*n+a == 3**e*u and u % 3 != 0, 'phase valuation identity')
    require(e >= 13 and 2**e > 2176*u, 'comparison hypotheses')
    m = 3**e*u*u
    require(1296*m < n*n, 'short-word comparison')
    require(64*m < 2**e*n, 'long-word comparison')
    require(min(phi(n), phi(n-1), phi(n+5)) > m, 'base comparison')
    return m


def build() -> dict:
    db = Dictionary()
    census, certificates, failures = [], [], []
    max_limit = 0
    for n in range(2, 4097):
        r, tags, limit = db.rank(n)
        max_limit = max(max_limit, limit)
        require(n-1 <= r <= old_rank(n) <= n*n, 'rank normalization')
        eligible = []
        for tag in tags:
            w = BASES[tag] if tag in BASES else tag[2:]
            p, d, a = coefficients(w)
            if (p*n+a) % d == 0:
                eligible.append(w)
        census.append([n, r, list(tags), sorted(eligible)])
        if eligible:
            w = min(eligible)
            y = physical(n, w)
            extras = (w,) if 4*coefficients(w)[0] >= 5*coefficients(w)[1] else ()
            rr, _, _ = db.rank(y, extras)
            q = w.count('1')
            require(rr * 4**len(w) <= 3**q*r and rr < r, 'physical descent')
            certificates.append([n, w, y, r, rr])
        else:
            failures.append(n)
    examples = []
    for n in (3, 7, 263, 380, 395, 593, 890, 4627, 11188):
        r, tags, _ = db.rank(n)
        examples.append([n, r, list(tags), old_rank(n)])

    a, b = 1, 0
    for _ in range(10):
        a, b = 2*a+3*b, a+2*b
    constants = [a, b, (2**19-a)**2-3*b*b,
                 2*29**20-30**20, 3**20*2**19-5**20,
                 3**13-34**2*1296,
                 4352*3**18-5992704*2**18]
    require(all(v > 0 for v in constants), 'rational constant check')
    db.extend(16)
    counts = [[l, len(db.levels[l])] for l in range(1, 17)]
    word_rows = [list(row) for l in range(1, 17) for row in sorted(db.levels[l])]

    phase_rows, endpoints, exact_rows = [], [], []
    unsafe_count = 0
    for k in range(1, 9):
        e0 = max(13, 6*k+12)
        e0 += (5-4*k-e0) % 16
        for lift in (0, 1, 2):
            e = e0+16*lift
            z = 3**e*64**k
            require((z-73) % 17 == 0, 'source congruence')
            n0 = n = (z-73)//17
            q, last_rank = 0, None
            initial = 3**e*4096**k
            for j in range(6*k+1):
                aa, ee, u = PHASES[j % 6], e+q, 2**(6*k-j)
                m = phase_lower_contract(n, aa, ee, u)
                if last_rank is not None:
                    bit = int(V[(j-1) % 6])
                    require(4*m == 3**bit*last_rank, 'per-shortcut rank identity')
                if k <= 2:
                    rr, tags, _ = db.rank(n)
                    require(rr == m and tags == ('W:'+ROTATIONS[j % 6],), 'exhaustive phase minimum')
                    exact_rows.append([k, e, j, n, rr])
                phase_rows.append([k, e, j, n, m, ee, u])
                if j < 6*k and j % 6 in (0, 4):
                    t = old_accel(n)
                    require(4*old_rank(t) > old_rank(n), 'old unsafe guard')
                    unsafe_count += 1
                if j < 6*k:
                    bit = int(V[j % 6])
                    require(n % 2 == bit, 'phase physical replay')
                    n = step(n)
                    q += bit
                last_rank = m
            s, h = n, e+4*k
            require(17*s+73 == 3**h and s % 8 == 2, 'exit phase')
            y = s//2
            require(h >= 18, 'exit lower bound range')
            low_num = 2**h*3**h
            require(y*y*4352 >= low_num*1296, 'exit short-word bound')
            require(2**(h-6)*y*4352 >= low_num, 'exit long-word bound')
            require(old_rank(s)*64**(2*k) > old_rank(n0)*81**(2*k), 'old rank growth')
            endpoints.append([k, e, n0, s, initial, 3**h, low_num, 4352])

    shadow_rows = []
    for k in range(1, 13):
        mod = 2**(k+1)
        for extra in (0, 7, 23):
            e = k+8+extra
            u = (-pow(3**e, -1, mod)) % mod
            if u % 3 == 0:
                u += mod
            n0 = n = 3**e*u
            require(u > 0 and u < 2**(k+2) and u % 3 != 0, 'small ordinary multiplier')
            require((n+1) % mod == 0, 'odd shadow')
            initial = n*n//3**e
            for j in range(1, k+1):
                require(n % 2 == 1, 'odd shadow replay')
                n = step(n)
                require(3**(e-k) > 16*16 and 2**(e-2) > 16*u, 'unbounded-delay lower ratio')
                require(all(vp(v,3)==0 for v in (n,n-1,n+5)), 'base valuations on positive shadow')
                shadow_rows.append([k,e,u,j,n0,n,initial])

    return {
        'schema': SCHEMA, 'parent': PARENT,
        'status': 'PROPOSED; no global selector or Collatz proof',
        'rank': 'three base forms and ALL words with 4*3^q >= 5*2^L',
        'census': {'sources': len(census), 'maximum_source': 4096,
                   'maximum_exhaustive_length': max_limit, 'sha256': digest(census),
                   'local_certificates': len(certificates), 'certificate_sha256': digest(certificates),
                   'unresolved': len(failures), 'first_unresolved': failures[:16]},
        'examples': examples,
        'word_census': {'through_length': 16, 'all_binary_words': 2**17-2,
                        'counts': counts, 'sha256': digest(word_rows)},
        'constants': constants,
        'phase_family': {'sources': len(endpoints), 'positions': len(phase_rows),
                         'old_unsafe_sources': unsafe_count, 'sha256': digest(phase_rows),
                         'exhaustive_positions': len(exact_rows), 'exhaustive_sha256': digest(exact_rows),
                         'examples': [endpoints[0], endpoints[3], endpoints[-1]],
                         'large_case_scope': 'all-word theorem premises plus physical replay; not exhaustive enumeration'},
        'fixed_clock_shadows': {'sources': 36, 'positions': len(shadow_rows),
                                 'sha256': digest(shadow_rows),
                                 'scope': 'finite substitutions in ATT-206; sources vary with the horizon'},
        'open': ['complete lower-rank selector', 'control after minimizer misalignment',
                 'uniform-time mass decay', 'nontrivial-cycle exclusion'],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--write', type=Path)
    group.add_argument('--check', type=Path)
    args = ap.parse_args()
    try:
        payload = build()
        report = {'payload': payload, 'sha256': digest(payload)}
        if args.write:
            args.write.parent.mkdir(parents=True, exist_ok=True)
            args.write.write_text(json.dumps(report, sort_keys=True, separators=(',', ':'))+'\n', encoding='utf-8')
        else:
            require(json.loads(args.check.read_text(encoding='utf-8')) == report, 'canonical report mismatch')
        print('PASS', report['sha256'])
        print(json.dumps(payload['census'], sort_keys=True))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print('ERROR:', exc)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
