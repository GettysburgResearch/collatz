#!/usr/bin/env python3
"""Exact finite interfaces for pass 5. No claim of full Collatz convergence."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from math import isqrt
from pathlib import Path

SCHEMA = 'X-ASTRA3-005/v1'
SCOPE = 'finite exact interfaces; universal statements require written proofs; Collatz not proved'
N = 16384
SCALE = 10**24


def need(test, msg):
    if not test:
        raise ValueError(msg)


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def vp(n, p):
    n = abs(n)
    need(n > 0, 'valuation at zero')
    t = 0
    while n % p == 0:
        n //= p
        t += 1
    return t


def step(n):
    return (3*n+1)//2 if n & 1 else n//2


def z(n, a):
    return 3**a*(n+1) - 2**a*(2*n+1)


def ra(n, a):
    d = z(n, a)
    return d*d // 3**vp(d, 3) if d else 0


@lru_cache(None)
def rank(n):
    need(n >= 1, 'positive source')
    h = vp(2*n+1, 3)
    return min(ra(n, a) for a in ({0, 1, 2, h} if h >= 3 else {0, 1, 2}))


def phi(n):
    r = rank(n)
    return r*r+r+1-n


@lru_cache(None)
def module(n):
    if n == 1:
        return (1, -1, 0, 0)
    a = vp(n+1, 2) if n & 1 else 0
    k = vp(z(n, a), 2)//(a+1)
    need(k >= 1, 'positive module length')
    endpoint = (3**(a*k)*(z(n, a)//2**((a+1)*k))-(3**a-2**a))//(3**a-2**(a+1))
    return endpoint, a, k, (a+1)*k


def safe(n):
    return n > 1 and rank(module(n)[0]) <= rank(n)


@lru_cache(None)
def safe_exit(n):
    y = n
    count = clock = 0
    while safe(y):
        v, a, k, length = module(y)
        need(phi(v) < phi(y), 'nonincreasing step fails refined rank')
        clock += length
        count += 1
        y = v
        need(count*count <= 81*rank(n), 'rank-count clock violated')
    return y, count, clock


def jump(n):
    """Induced return on unsafe sources; 1 is absorbing."""
    if n == 1:
        return 1
    need(not safe(n), 'jump domain is unsafe')
    return safe_exit(module(n)[0])[0]


def sublevel(M):
    """Complete rank <= M list, without scanning all n <= M+1."""
    out = set()
    pe = 1
    e = 0
    while pe <= M:
        for u in range(1, isqrt(M//pe)+1):
            if u % 3 == 0:
                continue
            Z = pe*u
            cand = [Z, Z+1, Z-5]
            for a in range(3, e+1):
                d = 3**a-2**(a+1)
                num = Z-(3**a-2**a)
                if num % d == 0:
                    cand.append(num//d)
            for n in cand:
                if n >= 2:
                    need(rank(n) <= M, 'candidate outside rank sublevel')
                    out.add(n)
        e += 1
        pe *= 3
    return sorted(out)


def spectrum():
    rows = []
    for j in range(9):
        M = 4**j
        values = sublevel(M)
        need(len(values)**2 <= 81*M, 'square-root count')
        need(len(values) >= max(0, isqrt(M)-1), 'lower count')
        rows.append({'M': M, 'count': len(values), 'values_sha256': digest(values),
                     'largest_source': max(values, default=0)})
    return rows


def census():
    flat = []
    unsafe = []
    hist = Counter()
    exits = Counter()
    quarters = 0
    transcript = []
    for n in range(2, N+1):
        y, a, k, length = module(n)
        r, s = rank(n), rank(y)
        quarters += int(4*s <= r)
        if s == r:
            need(y > n, 'equal-rank direction')
            flat.append([n, y, r])
        if s <= r:
            need(phi(y) < phi(n), 'refined-rank decrease')
        else:
            unsafe.append(n)
        target, count, clock = safe_exit(n)
        hist[count] += 1
        exits['one' if target == 1 else 'unsafe'] += 1
        transcript.append([n, y, r, s, target, count, clock])
    return {'N': N, 'safe': N-1-len(unsafe), 'quarter_safe': quarters,
            'unsafe': len(unsafe), 'flat_edges': flat,
            'safe_run_histogram': dict(sorted(hist.items())),
            'exits': dict(exits), 'max_safe_modules': max(hist),
            'transcript_sha256': digest(transcript)}


def frac(x):
    return [x.numerator, x.denominator]


def mass():
    # Outward fixed-point arithmetic; all n>N covered by rank >= N and the analytic tail.
    tail = Fraction(12, N*isqrt(N))
    rows = []
    for r in [0, 1, 2, 4, 8, 16]:
        lo = terms = 0
        for n in range(2, N+1):
            if safe_exit(n)[1] > r:
                lo += SCALE//rank(n)**2
                terms += 1
        lower = Fraction(lo, SCALE)
        upper = Fraction(lo+terms, SCALE)+tail
        rows.append({'r': r, 'enumerated_survivors': terms,
                     'lower': frac(lower), 'upper': frac(upper)})
    # Actual ordinary failure after safe-state induction, not an arbitrary model.
    spikes = []
    for j in range(13):
        e = 4+16*j
        x = 3**e
        y = (9*x+7)//16
        need(module(x)[0] == y, 'power-family module')
        need(vp(y, 2) == 1, 'power-family unsafe parity')
        need(rank(x) == x and rank(y) == 9*(x-1)**2//256, 'power-family ranks')
        need(not safe(x) and not safe(y) and jump(x) == y, 'induced kernel witness')
        spikes.append({'e': e, 'source': x, 'endpoint': y,
                       'rank_source': rank(x), 'rank_endpoint': rank(y),
                       'inverse_weight_ratio_lower_p2': frac(Fraction(rank(y), rank(x))**2)})
    return {'scale': SCALE, 'source_cutoff': N, 'omitted_source_tail': frac(tail),
            'safe_mass_intervals': rows, 'induced_spikes': spikes,
            'global_rank_counterexample': [9, jump(9), rank(9), rank(jump(9))]}


def cylinder(word):
    P = Q = 1
    c = 0
    for bit in word:
        if bit == '1':
            c = 3*c+P
            Q *= 3
        P *= 2
    return (-c*pow(Q, -1, P)) % P, P


def crt(r, m, s, d):
    return (r+m*((s-r)*pow(m, -1, d) % d)) % (m*d)


def source_for(word, b, t, lift=0):
    r, m = cylinder(word)
    modulus = 3**(t+1)
    db, cb = 3**b-2**(b+1), 3**b-2**b
    v = ((3**t-cb)*pow(db, -1, modulus)) % modulus
    n = crt(r, m, v, modulus)
    if n < 2:
        n += m*modulus
    return n+lift*m*modulus


def repayment():
    special = []
    for t in range(3, 25):
        word = '1110'+'110'*t+'0'
        for lift in [0, 1]:
            n = source_for(word, 2, t, lift)
            y, a, k, _ = module(n)
            m, b, ell, _ = module(y)
            need((a,k,b,ell) == (3,1,2,t), 'special maximal counts')
            need(rank(n) == (n+5)**2//3**t, 'special initial minimum')
            need(rank(y) == (y+5)**2//9, 'special spike minimum')
            need(rank(y) > 2*3**(t-2)*rank(n), 'special spike bound')
            need(256*64**t*rank(m) < 81*27**t*rank(n), 'special repayment bound')
            need(m > y > n, 'special numerical growth')
            special.append({'t':t,'lift':lift,'n':n,'spike':y,'endpoint':m,
                            'ranks':[rank(n),rank(y),rank(m)]})
    general = []
    for a in [2,3,4]:
        for b in [2,3,5]:
            if a == b:
                continue
            for k in [1,2]:
                for extra in [0,2]:
                    t = 2*b+4+extra
                    ell = t+a*k+4
                    word = ('1'*a+'0')*k+('1'*b+'0')*ell+'0'
                    n = source_for(word,b,t)
                    y, aa, kk, _ = module(n)
                    m, bb, ll, _ = module(y)
                    need((aa,kk,bb,ll)==(a,k,b,ell), 'general maximal counts')
                    need(vp(z(n,b),3)==t and rank(n)==ra(n,b), 'general input resonance')
                    need(vp(z(y,b),3)==min(a,b), 'destroyed resonance valuation')
                    need(vp(z(m,b),3)==min(a,b)+b*ell, 'recreated resonance valuation')
                    need(16*rank(m) < rank(n), 'general repayment')
                    need(m>y>n, 'general numerical growth')
                    general.append({'a':a,'b':b,'k':k,'t':t,'ell':ell,
                                    'n':n,'spike':y,'endpoint':m,
                                    'ranks':[rank(n),rank(y),rank(m)]})
    alternative = {'n':103, 'ternary_depth':vp(108,3), 'endpoint':module(103)[0],
                   'next_mode':module(module(103)[0])[1]}
    need(alternative == {'n':103,'ternary_depth':3,'endpoint':175,'next_mode':4},
         'unforced repayment countermodel')
    return {'special':special,'general':general,'alternative_mode':alternative}


def merging():
    clock = 6
    rows = []
    for n in [3,7,9,13,27,46,81,121,703,2223]:
        candidates = [x for x in [1]+sublevel(rank(n)) if phi(x)<phi(n)]
        end = [n]
        for _ in range(clock): end.append(step(end[-1]))
        diagrams = []
        for x in candidates:
            y = x
            for s in range(clock+1):
                for r in range(clock+1):
                    if y == end[r]: diagrams.append([r,s,x,y])
                y = step(y)
        diagrams.sort(key=lambda q:(q[0]+q[1],max(q[0],q[1]),q[0],q[1],q[2]))
        rows.append({'n':n, 'rank':rank(n),'candidate_count':len(candidates),
                     'candidate_sha256':digest(candidates),'diagram_count':len(diagrams),
                     'diagram_sha256':digest(diagrams),'best':diagrams[0] if diagrams else None})
    return {'clock_cap':clock,'rows':rows}


def build():
    return {'schema':SCHEMA,'scope':SCOPE,'spectrum':spectrum(),'census':census(),
            'mass':mass(),'repayment':repayment(),'merging':merging()}


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--check',type=Path)
    args=p.parse_args()
    payload=json.loads(json.dumps(build(),sort_keys=True))
    report={'payload':payload,'sha256':digest(payload)}
    if args.check:
        need(json.loads(args.check.read_text())==report,'canonical report mismatch')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n')
    print(report['sha256']); print('finite interfaces passed; no global coverage claim')

if __name__=='__main__':main()
