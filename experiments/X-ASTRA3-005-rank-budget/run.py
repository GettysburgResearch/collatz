#!/usr/bin/env python3
"""Exact finite tests for pass five. No convergence oracle or third-party module."""
from __future__ import annotations
import argparse, hashlib, json
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path

SCHEMA = 'X-ASTRA3-005/v1'
SCOPE = 'finite exact interfaces; universal statements require the written proofs; Collatz not proved'

def need(ok: bool, msg: str) -> None:
    if not ok:
        raise ValueError(msg)

def seal(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def v(n: int, p: int) -> int:
    n = abs(n)
    need(n != 0, 'valuation of zero')
    if p == 2:
        return (n & -n).bit_length() - 1
    k = 0
    while n % p == 0:
        n //= p; k += 1
    return k

def z(n: int, a: int) -> int:
    return 3**a * (n+1) - 2**a * (2*n+1)

@lru_cache(None)
def rank(n: int) -> int:
    need(n >= 1, 'nonpositive input')
    h = v(2*n+1, 3)
    values = []
    for a in set((0, 1, 2, h)):
        t = z(n, a)
        values.append(0 if t == 0 else t*t // 3**v(t, 3))
    return min(values)

@lru_cache(None)
def module(n: int) -> tuple[int, int, int]:
    if n == 1:
        return 1, 0, 0
    a = 0 if n % 2 == 0 else v(n+1, 2)
    k = v(z(n,a), 2) // (a+1)
    need(k >= 1, 'empty module')
    d, c = 3**a-2**(a+1), 3**a-2**a
    num = 3**(a*k) * (z(n,a) // 2**((a+1)*k)) - c
    need(num % d == 0, 'module divisibility')
    return num // d, a, k

def safe(n: int) -> bool:
    return n > 1 and 4*rank(module(n)[0]) <= rank(n)

def crt(a: int, m: int, b: int, q: int) -> int:
    return a + m * ((b-a)*pow(m,-1,q) % q)

def data_word(word: str) -> tuple[int, int, int]:
    P = Q = 1; A = 0
    for bit in word:
        if bit == '1':
            A = 3*A+P; Q *= 3
        P *= 2
    return P,Q,A

def lift_word(word: str, ternary: int, modulus: int) -> tuple[int,int]:
    P,Q,A = data_word(word)
    dy = (P-A)*pow(Q,-1,2*P) % (2*P)  # odd terminal bit
    base = crt(dy,2*P,ternary,modulus)
    step = 2*P*modulus
    while base < 11:
        base += step
    return base,step

def rank_ball(B: int) -> list[int]:
    out = set(); e = 0
    while 3**e <= B:
        for u in range(1,isqrt(B//3**e)+1):
            if u % 3 == 0:
                continue
            Z = 3**e*u; m = 3**e*u*u
            cand = [Z, Z+1, Z-5]
            for a in range(3,e+1):
                d,c = 3**a-2**(a+1),3**a-2**a
                if (Z-c) % d == 0:
                    cand.append((Z-c)//d)
            for n in cand:
                if n >= 2 and rank(n) == m:
                    out.add(n)
        e += 1
    return sorted(out)

def volume_report() -> dict:
    rows = []
    for B in (1,16,256,4096,65536,2**24):
        ball = rank_ball(B)
        need(len(ball)**2 <= 81*B, 'rank-volume upper bound')
        need(len(ball) >= max(0,isqrt(B)-1), 'rank-volume lower bound')
        rows.append(dict(B=B,count=len(ball),maximum=max(ball,default=0),digest=seal(ball)))
    need(3*7**2 > 12**2 and 36*60+343 < 2700, 'constant-nine certificate')
    need(Fraction(3,1)/(1-Fraction(1,3)) + Fraction(1,27)/(1-Fraction(1,3))**2 == Fraction(55,12), 'mass constant')
    return dict(rows=rows,integer_comparisons=3)

def operator_report() -> dict:
    # Arbitrary finite nonnegative mass, not a resampled power-law density.
    f = {n:1+n%7 for n in range(2,2049) if safe(n)}
    initial_count = len(f); rows = []
    for r in range(9):
        moment = sum(rank(n)*w for n,w in f.items())
        nxt = defaultdict(int); exit_moment = 0
        for n,w in f.items():
            y,_,_ = module(n)
            if y == 1:
                continue
            if safe(y):
                nxt[y] += w
            else:
                exit_moment += rank(y)*w
        next_moment = sum(rank(n)*w for n,w in nxt.items())
        need(4*(next_moment+exit_moment) <= moment, 'safe weighted contraction')
        rows.append([r,len(f),moment,next_moment,exit_moment])
        f = dict(nxt)
    spikes = []
    for e in range(4,117,16):
        x=3**e; y=(9*x+7)//16
        need(module(x)==(y,1,2), 'spike source module')
        need(rank(x)==x and rank(y)==9*(x-1)**2//256, 'spike ranks')
        need(not safe(x) and not safe(y), 'spike stays in unsafe section')
        need(module(y)==(y//2,0,1), 'spike destination module')
        need(rank(y//2)==(y//2-1)**2, 'spike next rank')
        need(32*rank(y)>x*x, 'uniform moment explosion contribution')
        spikes.append([e,x,y,rank(y)])
    return dict(seed_support=initial_count,safe_rows=rows,spikes=spikes)

def barrier_report() -> dict:
    rows=[]; positions=0; ancestor_checks=0
    for H in range(2,17):
        step=3**(H+1)*2**(2*H+1)
        n0=crt(3**H,3**(H+1),1+4**H,2**(2*H+1))
        for lift in (0,1,7):
            n=n0+step*lift; r=rank(n)
            need(v(n,3)==H and module(n)[1:]==(1,H), 'repayment guards')
            y,_,_=module(n)
            need(16**H*rank(y) < 9**H*r, 'rank repayment')
            peak=0; cur=n
            for i in range(2*H+1):
                peak=max(peak,rank(cur));positions+=1
                if i < 2*H:
                    cur=(3*cur+1)//2 if cur%2 else cur//2
            need(cur==y, 'literal repayment endpoint')
            low=((3*n-1)//2)**2; high=((3*n+1)//2)**2
            need(rank((3*n+1)//2)==low and low<=peak<=high,'barrier bracket')
            for j in range(9):
                x=2**j*n
                need(rank(x)==4**j*r and x%3==0, 'unique reverse ray')
                ancestor_checks+=1
            rows.append([H,lift,n,r,y,rank(y),peak,low,high])
    return dict(cases=len(rows),positions=positions,ancestor_checks=ancestor_checks,digest=seal(rows),examples=rows[:3])

def switch_report() -> dict:
    rows=[]; modules=0; unsafe_positions=0; examples=[]; witnesses=[]
    residue=-73*pow(17,-1,243)%243
    pairs=((0,1),(2,0),(4,-1),(3,1),(-1,2))
    for K in range(1,17):
        for extra in (0,2):
            L=K+4+extra
            base,step=lift_word('111010'*K+'0'*L,residue,243)
            for lift in (0,1,3):
                n=base+step*lift; cur=n; history=[n]
                need(v(17*n+73,2)==6*K,'intrinsic switch counter')
                for i in range(2*K):
                    out,a,k=module(cur)
                    need((a,k)==((3,1) if i%2==0 else (1,1)), 'switch modules')
                    need(not safe(cur),'source not unsafe')
                    need(rank(cur)==((cur-1)**2//9 if i%2==0 else (cur+5)**2//9), 'frozen rank')
                    unsafe_positions+=1;modules+=1;cur=out;history.append(cur)
                before=cur
                need(rank(before)*64**(2*K)>rank(n)*81**(2*K),'unbounded pre-repayment growth')
                out,a,k=module(before)
                need((a,k)==(0,L) and 4*rank(out)<rank(n),'terminal repayment')
                need(safe(before),'terminal halving not safe')
                modules+=1
                rows.append([K,L,lift,n,before,out,rank(n),rank(before),rank(out)])
                if lift==0 and extra==0 and K in (1,2,4,8):examples.append(rows[-1])
                if K==2 and lift==0 and extra==0:
                    for s,t in pairs:
                        def w(x):return Fraction(x)**(-s)*Fraction(rank(x))**(-t)
                        found=None
                        for x,y in zip(history[:-2],history[1:-1]):
                            if not safe(y) and w(x)>w(y):
                                found=[s,t,x,y];break
                        need(found is not None,'missing unsafe power-weight failure')
                        witnesses.append(found)
    # These familiar failures remain outside the guarded infinite families.
    residual=[[n,module(n)[0],rank(n),rank(module(n)[0])] for n in (3,7,9,81)]
    return dict(cases=len(rows),modules=modules,unsafe_sources=unsafe_positions,digest=seal(rows),examples=examples,power_weight_failures=witnesses,residual_controls=residual)

def build() -> dict:
    return dict(schema=SCHEMA,scope=SCOPE,volume=volume_report(),operator=operator_report(),barriers=barrier_report(),switches=switch_report())

def main() -> None:
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--check',type=Path);args=p.parse_args()
    payload=build(); report=dict(payload=payload,sha256=seal(payload))
    # JSON normalization is explicit: tuple/list differences cannot break replay.
    report=json.loads(json.dumps(report))
    if args.check:need(json.loads(args.check.read_text())==report,'canonical mismatch')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n')
    print(report['sha256']);print('pass-five finite checks passed')

if __name__=='__main__':main()
