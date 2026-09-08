#!/usr/bin/env python3
"""Exact finite support for APR; no universal Collatz conclusion. Stdlib only."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import itertools
import json
from math import isqrt
from pathlib import Path

BASE = 'ca55b248722fd9bdeb713c6f05fdda5cbdc91f38'
WORDS = ['1', '110', '1110', '111010', '1110110', '11101110110', '1110'*4+'110', '1110'*8+'110']
LEVELS = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536]
SCAN = 8192

def need(ok: bool, why: str) -> None:
    if not ok: raise ValueError(why)

def raw(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()

def sha(obj: object) -> str: return hashlib.sha256(raw(obj)).hexdigest()

def val(n: int) -> int:
    need(n != 0, 'zero valuation')
    n = abs(n); e = 0
    while n % 3 == 0: n //= 3; e += 1
    return e

def g(n: int) -> int:
    need(n != 0, 'zero displacement must be omitted')
    return n*n//3**val(n)

def T(n: int) -> int: return (3*n+1)//2 if n & 1 else n//2

@lru_cache(None)
def gamma(n: int) -> tuple[int, tuple[int, ...]]:
    need(n >= 1, 'positive rank source')
    if n == 1: return 0, (0,)
    best, indices = g(n), [0]
    x, four, k = n, 4, 1
    while four <= best:
        x = T(x); d = x-n
        if d:
            candidate = four*g(d)
            if candidate < best: best, indices = candidate, [k]
            elif candidate == best: indices.append(k)
        four *= 4; k += 1
    need(n <= best <= n*n, 'properness')
    return best, tuple(indices)

def data(w: str) -> tuple[int, int]:
    q = A = 0
    for i, b in enumerate(w):
        if b == '1': q += 1; A = 3*A+2**i
    return q, A

def primitive(w: str) -> bool:
    return all(w != w[:d]*(len(w)//d) for d in range(1, len(w)) if len(w)%d == 0)

def profile(w: str) -> dict:
    m = len(w); q, A = data(w); P, Q = 2**m, 3**q; D = Q-P
    need(D > 0 and primitive(w), 'expanding primitive word required')
    rotations = [w[r:]+w[:r] for r in range(m)]
    As = [data(v)[1] for v in rotations]
    hs = []
    for v, av in zip(rotations, As):
        for r in range(1, m):
            qr, ar = data(v[:r]); C = D*ar-(3**qr-2**r)*av
            need(C != 0, 'nonprimitive phase equality')
            hs.append(val(C))
    b = max([0]+hs); j0 = 1
    while Q**j0 < 2**(m+1)*P**j0: j0 += 1
    K0 = (j0+1)*m; M = 2*3**K0+max(As)+1; H0 = b+1
    while 3**H0 <= 4*(D+1)**2*3**b: H0 += 1
    return dict(word=w, m=m, q=q, A=A, P=P, Q=Q, D=D, b=b, j0=j0, K0=K0,
                M=M, Amax=max(As), H0=H0, U=6*P*D, phase_values_sha256=sha(hs))

def old_rank(n: int) -> int:
    h = val(2*n+1); indices = {0, 1, 2}
    if h >= 3: indices.add(h)
    vals = []
    for a in indices:
        z = 3**a*(n+1)-2**a*(2*n+1)
        vals.append(g(z) if z else 0)
    return min(vals)

def family(p: dict, extra: int, L: int, which: int) -> dict:
    m,q,A,P,Q,D = [p[k] for k in ('m','q','A','P','Q','D')]
    H = p['H0']+extra; U=p['U']; c=0
    while 4**c < 3**(H+q*(L+1))*U*U: c += 1
    N0=1
    while not (P**N0 > 2*D*U+2*D*p['M']+2*p['Amax'] and Q**N0 >= 2**(c+1)*P**N0): N0 += 1
    N=N0+L+1
    residue=A*pow(P**N*3**H, -1, D)%D if D>1 else 0
    units=sorted({residue+t*D for t in range(7) if 0<residue+t*D<=6*D and (residue+t*D)%2 and (residue+t*D)%3})
    need(len(units)==2, 'six-class unit coverage')
    u=units[which]; n=(P**N*3**H*u-A)//D
    need(n>=p['M'] and D*n+A==P**N*3**H*u, 'source guard')
    x=n; odd=0; states=[]; ranks=[]; gamma0=P**(2*N)*3**H*u*u
    for r in range(m*L+1):
        z, indices=gamma(x)
        need(indices==(m,), 'global minimum is not unique at the period length')
        need(z*4**r==3**odd*gamma0, 'exact all-phase common-rank scaling')
        states.append(x); ranks.append(z)
        if r<m*L:
            bit=int(p['word'][r%m]); need(x%2==bit, 'physical phase')
            odd+=bit; x=T(x)
    check_x=n
    for bit in p['word']*N:
        need(check_x%2==int(bit), 'complete prescribed ordinary word')
        check_x=T(check_x)
    need(states[-1]>n and ranks[-1]*P**(2*L)==Q**L*ranks[0], 'opposite growth directions')
    old=[]
    if p['word']=='111010':
        for i in range(L):
            s,t,end=states[6*i],states[6*i+4],states[6*i+6]
            ps,pt,pe=old_rank(s),old_rank(t),old_rank(end)
            need(ps==(s-1)**2//9 and pt==(t+5)**2//9, 'old rank formulas')
            need(pt>ps and 4*pe>pt and 16*pe<9*pt, 'old unsafe classification')
            need((s+1)&15==8 and (t+1)&3==2, 'maximal modes three/one')
            old.append([ps,pt,pe])
        need(old_rank(states[-1])*64**(2*L)>old_rank(n)*81**(2*L), 'old cycle-rank growth')
        need(27*ranks[0] < 4*old_rank(n), 'new initial rank is genuinely smaller')
    return dict(word=p['word'], H=H, L=L, which=which, N0=N0, N=N, c=c, u=u,
                source_bits=n.bit_length(), source_sha256=sha(n), first_rank_sha256=sha(ranks[0]),
                phases=len(states), winning_length=m, states_sha256=sha(states), ranks_sha256=sha(ranks),
                old_unsafe_edges=2*L if old else 0, old_comparison_sha256=sha(old))

def sublevel(M: int) -> set[int]:
    def ds(Y: int):
        e=0
        while 3**e<=Y:
            for u in range(1,isqrt(Y//3**e)+1):
                if u%3: yield 3**e*u
            e+=1
    candidates=set(ds(M)); k=1
    while 4**k<=M:
        displacements=list(ds(M//4**k))
        for bits in itertools.product('01', repeat=k):
            w=''.join(bits);q,A=data(w);D=3**q-2**k
            for d0 in displacements:
                for d in (d0,-d0):
                    num=2**k*d-A
                    if num%D==0:
                        n=num//D
                        if n>=2:
                            x=n
                            for bit in w:
                                need(x%2==int(bit), 'sublevel physical word');x=T(x)
                            need(x-n==d, 'sublevel displacement')
                            candidates.add(n)
        k+=1
    return {n for n in candidates if n>=2 and gamma(n)[0]<=M}

def parity() -> dict:
    counts=[]
    for k in range(1,13):
        seen=set()
        for bits in itertools.product('01', repeat=k):
            w=''.join(bits);q,A=data(w);P=2**k
            residue=(-A*pow(3**q,-1,P))%P; n=residue+P; x=n
            for bit in w:
                need(x%2==int(bit),'parity residue');x=T(x)
            need(P*(x-n)==(3**q-P)*n+A and 0<=A<=3**k-P,'prefix affine identity')
            seen.add(residue)
        need(len(seen)==2**k,'complete parity classes'); counts.append([k,len(seen)])
    return dict(rows=counts, words=sum(x[1] for x in counts))

def build() -> dict:
    profiles=[profile(w) for w in WORDS]
    family_rows=[family(p,e,L,i) for p in profiles for e in (0,2) for L in (1,3) for i in (0,1)]
    core=[]; types=Counter(); guards=0; old_long=0; safe=[]
    for n in range(2,SCAN+1):
        a,ks=gamma(n);x=n; ds={}
        for k in range(1,max(ks)+1): x=T(x);ds[k]=x-n
        guard=(0 in ks and n%2==0) or any(k and ds[k]%2==0 for k in ks)
        nxt=gamma(T(n))[0]
        if guard: need(nxt<a,'rotation guard failed');guards+=1
        types[min(ks)]+=1;old_long+=min(ks)>=4
        core.append([n,a,list(ks),nxt,guard])
        x=n;length=0
        while x!=1 and gamma(T(x))[0]<gamma(x)[0]: x=T(x);length+=1
        K=(a.bit_length()-1)//2
        need(length*length<25*(K+1)**2*a,'safe residence bound')
        safe.append([n,length,x])
    balls=[];tails=[];scale=2**80
    for M in LEVELS:
        ns=sorted(sublevel(M)); K=(M.bit_length()-1)//2
        need(isqrt(M)-1<=len(ns) and len(ns)**2<25*(K+1)**2*M,'rank count bounds')
        balls.append(dict(M=M,count=len(ns),maximum=max(ns,default=0),sources_sha256=sha(ns)))
        J=K;tail=F(80*(7*J+15),49*8**J)
        total=sum(scale//gamma(n)[0]**2 for n in ns)
        tails.append(dict(J=J,cutoff=M,safe_clock=5*(J+1)*2**J,tail=str(tail),
                          finite_lower_units=total,finite_upper_units=total+len(ns),rounding_bits=80))
    spikes=[]
    for H in (1,2,3,4,8,16,32,64):
        n=3**H;y=T(n);a,ks=gamma(n);b,_=gamma(y)
        need(a==n and ks==(0,) and b**10>n**11,'all-word spike control')
        rays=[]
        for r in range(6):
            x=2**r*n;need(gamma(x)[0]>=n,'lower-rank inverse-ray failure');rays.append([r,gamma(x)[0]])
        spikes.append(dict(H=H,n=n,y=y,source_rank=a,endpoint_rank=b,ray_sha256=sha(rays)))
    x=1932103;boundary=[]
    for i in range(8): boundary.append([i,x,*[gamma(x)[0]],list(gamma(x)[1])]);x=T(x)
    need(boundary[0][2]==1479901446144 and boundary[6][2]==29265629184 and boundary[7][2]==4484692426800,'finite-window countertest')
    need(boundary[7][2]>boundary[6][2],'boundary spike missing')
    need(T(T(2))==2 and gamma(2)[0]==4,'zero displacement convention')
    payload=dict(schema='APR-v1',base=BASE,scope=dict(collatz_proved=False,universal_selector=False,
                 all_parameter_proofs_by_finite_computation=False,rank_candidates='actual nonzero prefix displacements',
                 zero_displacements='omitted',rank_domain='positive integers; 1 absorbed'),
                 profiles=profiles,families=family_rows,parity=parity(),
                 core=dict(cutoff=SCAN,sources=len(core),rotation_guards=guards,
                           one_step_decreases=sum(row[3]<row[1] for row in core),long_winners=old_long,
                           winner_counts={str(k):v for k,v in sorted(types.items())},rows_sha256=sha(core)),
                 safe=dict(sources=len(safe),maximum_steps=max(r[1] for r in safe),
                           reaches_one=sum(r[2]==1 for r in safe),rows_sha256=sha(safe)),
                 balls=balls,rank_tails=tails,spikes=spikes,boundary_counterexample=boundary,
                 exact_constants=dict(four9_gt_three11=4**9>3**11,safe_occupation='21200/27',global_rank_reciprocal_bound=60))
    return dict(payload=payload,sha256=sha(payload))

def compact(report: dict) -> dict:
    p=dict(report['payload']); families=p['families']
    p['full_reconstruction_sha256']=report['sha256']
    p['family_corpus']=dict(cases=len(families), phases=sum(r['phases'] for r in families),
        old_unsafe_edges=sum(r['old_unsafe_edges'] for r in families),
        rows_sha256=sha(families), retained_indices=[0,24,31,63])
    p['families']=[families[i] for i in p['family_corpus']['retained_indices']]
    p['schema']='APR-compact-v1'
    return dict(payload=p,sha256=sha(p))

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);ap.add_argument('--check',type=Path)
    ap.add_argument('--full-output',type=Path)
    args=ap.parse_args(); full=build(); report=compact(full)
    if args.check: need(raw(json.loads(args.check.read_text()))==raw(report),'canonical report mismatch')
    if args.output: args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(raw(report)+b'\n')
    if args.full_output: args.full_output.parent.mkdir(parents=True,exist_ok=True);args.full_output.write_bytes(raw(full)+b'\n')
    print('PASS',report['sha256']);print('family corpus',report['payload']['family_corpus'])
    print('core',report['payload']['core']);print('safe',report['payload']['safe'])

if __name__=='__main__': main()
