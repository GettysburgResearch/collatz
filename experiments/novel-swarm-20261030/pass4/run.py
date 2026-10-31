#!/usr/bin/env python3
"""Exact finite tests for pass 4; four CPU workers, not independent agents.
Standard library only. No assertions: checks remain active under -OO.
The all-width theorems are written proofs, not consequences of this census.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction as Q
from math import comb
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def sha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def pair(x: Q) -> list[int]:
    return [x.numerator, x.denominator]


def step(n: int) -> int:
    return (3*n+1)//2 if n & 1 else n//2


def word_data(k: int, bits: int) -> tuple[int, int, int]:
    q = C = 0
    for i in range(k):
        if (bits >> i) & 1:
            C = 3*C + (1 << i)
            q += 1
    r = (-C * pow(3**q, -1, 1 << k)) % (1 << k)
    return q, C, r


def child(K: int, k: int, q: int) -> int:
    return 1 + (3**q*(K-1)+(3**q-2**q)*(2**(k-q)-1))//2**k


def log_floor(base: int, bound: int) -> int:
    a, p = 0, 1
    while p*base <= bound:
        p *= base
        a += 1
    return a


def geometry_track() -> dict:
    words = []
    lifts = 0
    for k in range(1, 13):
        residues = set()
        for bits in range(1 << k):
            q, C, r = word_data(k, bits)
            need(3**q-2**q <= C <= (3**q-2**q)*2**(k-q), 'affine extrema')
            residues.add(r)
            for h in (1, 2, (1 << 128)+1):
                x = r + (1 << k)*h
                y, actual = x, 0
                for j in range(k):
                    actual |= (y & 1) << j
                    y = step(y)
                need(actual == bits and (1 << k)*y == 3**q*x+C, 'whole-cylinder lift')
                lifts += 1
            words.append([k, bits, q, C, r])
        need(len(residues) == 1 << k, 'residue bijection')
    windows, samples = [], []
    offsets = [1, 2, 27, (1 << 64)+13, (1 << 256)+123]
    group_checks = 0
    for k in range(1, 11):
        m = max(0, log_floor(3, 1 << k)-2)
        H = sum(comb(k, q) for q in range(m+1, k+1))
        for K in range(1, 65):
            for a in offsets:
                groups = {}
                for n in range(a, a+K):
                    y, q = n, 0
                    for _ in range(k):
                        q += y & 1
                        y = step(y)
                    groups.setdefault(q, []).append(y)
                high = sum(len(ys) for q, ys in groups.items() if q > m)
                need(high <= ((K+(1 << k)-1)//(1 << k))*H, 'high-lane source count')
                row = [a, K, k, []]
                for q, ys in sorted(groups.items()):
                    L = child(K, k, q)
                    need(max(ys)-min(ys)+1 <= L, 'translated image interval')
                    row[3].append([q, len(ys), min(ys), max(ys), L])
                    group_checks += 1
                windows.append(row)
                if k in (1, 5, 10) and K in (1, 7, 32, 64):
                    samples.append(row)
    return {'words': words, 'positive_lifts': lifts, 'window_count': len(windows),
            'group_checks': group_checks, 'window_sha256': sha(windows), 'window_samples': samples}


def product_powers(spec: list[list[int]]) -> int:
    z = 1
    for b, e in spec:
        z *= b**e
    return z


def constants_track() -> dict:
    inequalities = [
        ['critical_ratio', [[3,147]], [[2,233]]],
        ['chernoff_rate', [[19,4660]], [[7,1720],[3,2940],[2,10307]]],
        ['geometric_sum', [[2,60]], [[3,39]]],
        ['remainder_exponent', [[3,5]], [[2,8]]],
        ['tail_at_32', [[2640,50]], [[2,608]]],
        ['tail_monotonicity', [[5,50]], [[2,119]]],
        ['high_constant', [[3456,1]], [[11,1],[343,1]]],
        ['terminal_monotonicity', [[25,1]], [[32,1]]],
        ['induction_base', [[2,32]], [[16,20]]],
    ]
    for name, left, right in inequalities:
        need(product_powers(left) < product_powers(right), name)
    clocks = []
    for k in list(range(32,257))+[512,1024,2048,4096]:
        m = log_floor(3, 1 << k)-2
        H = sum(comb(k, q) for q in range(m+1, k+1))
        need(H**20 * 7**60 <= 12**60 * (1 << (19*k)), 'finite Chernoff check')
        need(3**m*9 <= 1 << k, 'low-lane shrink')
        clocks.append([k, m, H])
    five = []
    for k in (8,16,32,64,128):
        m = log_floor(5, 1 << k)
        H = sum(comb(k,q) for q in range(m+1,k+1))
        need(2*m < k and H >= 1 << (k-1), '5x+1 right-tail control')
        five.append([k,m,H])
    return {'inequalities': inequalities, 'clock_rows': clocks, 'five_control': five}


def no_descent(n: int, cap: int = 4096) -> tuple[list[int], str]:
    states, seen, x = [n], {n}, n
    for _ in range(cap):
        y = step(x)
        if y < n:
            return states, 'descent'
        if y in seen:
            return states, 'repeat'
        states.append(y)
        seen.add(y)
        x = y
    raise ValueError('no-descent clock cap exhausted')


def records_track() -> dict:
    rows, samples = [], []
    raw_steps = max_records = 0
    for n in range(2,8193):
        states, outcome = no_descent(n)
        L, q = len(states)-1, 0
        records = [0]
        best_q = best_i = 0
        for i in range(1,L+1):
            q += states[i-1] & 1
            if 3**q * (1 << best_i) < 3**best_q * (1 << i):
                records.append(i)
                best_q, best_i = q, i
        distortion = Q(states[-1]*(1 << L), n*3**q)
        need(distortion >= 1, 'distortion sign')
        W = (n*distortion.numerator)//distortion.denominator-n+1
        need(all(n <= states[i] <= n+W-1 for i in records), 'record location')
        R = len(records)
        need(R**20 <= 16**20 * W**19, 'translated record packing')
        ends = records[1:]+[L]
        idx = max(range(R), key=lambda j: ends[j]-records[j])
        start, length = records[idx], max(0, ends[idx]-records[idx]-1)
        qq = 0
        for j in range(1,length+1):
            qq += states[start+j-1] & 1
            need(3**qq >= 1 << j, 'supercritical extraction')
        need(length >= max(0,(L+R-1)//R-1), 'extraction clock bound')
        row = [n,L,q,records,W,pair(distortion),start,length,outcome]
        rows.append(row)
        if R > max_records or n in (3,27,31,97,871,6171):
            samples.append({'row': row, 'states': states})
        max_records = max(max_records,R)
        raw_steps += L+1
    # Exercise multiple records on complete SIMPLE prefixes. These may descend
    # below their initial source, so they are not nontrivial no-descent tests.
    full_rows = []
    for n in range(2,513):
        states, seen, x = [n], {n}, n
        while True:
            y = step(x)
            if y in seen:
                break
            need(len(states) < 4096, 'full simple prefix cap')
            states.append(y); seen.add(y); x = y
        L = len(states)-1
        q = best_q = best_i = 0
        records = [0]
        for i in range(1,L+1):
            q += states[i-1] & 1
            if 3**q * (1 << best_i) < 3**best_q * (1 << i):
                records.append(i); best_q,best_i=q,i
        D = Q(states[-1]*(1 << L), n*3**q)
        lower = min(states)
        width = (n*D.numerator)//D.denominator-lower+1
        need(all(lower <= states[i] < lower+width for i in records), 'general record window')
        need(len(records)**20 <= 16**20*width**19, 'general record packing')
        ends = records[1:]+[L]
        j = max(range(len(records)),key=lambda j:ends[j]-records[j])
        start,length=records[j],max(0,ends[j]-records[j]-1)
        qq=0
        for h in range(1,length+1):
            qq += states[start+h-1] & 1
            need(3**qq >= 1 << h, 'general record extraction')
        full_rows.append([n,L,records,lower,width,pair(D),start,length])
    # The terminal correction cannot be discarded for an arbitrary simple prefix.
    # 1 and 5 merge synchronously at time 4 despite being distinct states of
    # the simple prefix 5,8,4,2,1. The last k points must be removed.
    x,y=1,5
    for _ in range(4):
        x,y=step(x),step(y)
    need(x==y==1, 'terminal-boundary negative control')
    return {'rows': rows, 'raw_steps_including_exit': raw_steps, 'max_records': max_records,
            'samples': samples, 'full_simple_rows': full_rows, 'terminal_control': {'path':[5,8,4,2,1], 'k':4, 'sources':[1,5], 'endpoint':1}}


def pressure_track() -> dict:
    targets = (251,263,377,395)
    sums = {t:Q(0) for t in targets}
    digest_rows, steps = [], 0
    for source in range(1,65536,2):
        n, q, A, peak = source, 0, 0, source
        while True:
            if n in sums:
                sums[n] += Q(9**q, (1 << (2*A))*n*n)
            if n == 1:
                break
            need(q < 4096, 'pressure bank clock exhausted')
            z=3*n+1
            a=(z & -z).bit_length()-1
            n=z >> a
            q += 1
            A += a
            peak=max(peak,n)
        steps += q
        digest_rows.append([source,q,A,peak])
    delta=Q(1,131072)
    drops=[]
    for x,y,den in ((263,395,3000000),(251,377,1500000)):
        need((3*x+1)//2==y, 'claimed ordinary edge')
        margin=sums[x]-sums[y]-delta
        need(margin>Q(1,den), 'full-pressure decrease certificate')
        drops.append([x,y,den,pair(margin)])
    toy=[]
    for t in range(1,8192,2):
        x=t; p=Q(0); r=0
        while True:
            p += Q(1,x*x)
            if x%3:
                break
            x//=3
            r+=1
        formula=Q(1,x*x)*sum((Q(1,9)**j for j in range(r+1)),Q(0))
        need(p==formula, 'ordinary expanding-map pressure')
        toy.append([t,pair(p)])
    return {'source_bound':65535, 'sources':len(digest_rows), 'odd_steps':steps,
            'bank_sha256':sha(digest_rows), 'values':[[t,pair(sums[t])] for t in targets],
            'tail':pair(delta), 'drops':drops, 'toy_count':len(toy), 'toy_sha256':sha(toy)}


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--serial',action='store_true')
    a=p.parse_args()
    jobs=[geometry_track,constants_track,records_track,pressure_track]
    if a.serial:
        results=[job() for job in jobs]
    else:
        with ProcessPoolExecutor(max_workers=4) as pool:
            results=list(pool.map(call_job,jobs))
    data={'schema':'collatz-pass4-v1', **dict(zip(('geometry','constants','records','pressure'),results))}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'status':'passed','output_sha256':hashlib.sha256(a.output.read_bytes()).hexdigest(),
                      'words':len(data['geometry']['words']), 'translated_windows':data['geometry']['window_count'],
                      'record_sources':len(data['records']['rows']), 'pressure_sources':data['pressure']['sources']},sort_keys=True))


def call_job(job):
    return job()


if __name__=='__main__':
    main()
