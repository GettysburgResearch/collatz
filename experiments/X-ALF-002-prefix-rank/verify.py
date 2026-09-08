#!/usr/bin/env python3
"""Separate reconstruction: full fixed rank horizon, physical residues, all-component comparison.
Imports neither run.py nor repository modules. Same author; not peer review.
"""
from __future__ import annotations
import argparse
from collections import Counter
import copy
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from math import isqrt
from pathlib import Path

BASE='ca55b248722fd9bdeb713c6f05fdda5cbdc91f38'
WORDS=['1','110','1110','111010','1110110','11101110110','1110'*4+'110','1110'*8+'110']
LEVELS=[1,4,16,64,256,1024,4096,16384,65536]
SCAN=8192

def check(ok: bool, why: str) -> None:
    if not ok: raise ValueError(why)

def encode(obj: object) -> bytes:
    return json.dumps(obj,sort_keys=True,separators=(',',':')).encode()

def seal(obj: object) -> str: return hashlib.sha256(encode(obj)).hexdigest()

def v3(z: int) -> int:
    check(z!=0,'zero valuation'); z=abs(z);power=3; count=0
    while z%power==0: power*=3;count+=1
    return count

def score(z: int) -> int:
    check(z!=0,'omit zero return'); z=abs(z);unit=z
    while unit%3==0:unit//=3
    return z*unit

def advance(x: int) -> int: return (x+(2*x+1)*(x%2))>>1

@lru_cache(None)
def rank(n: int) -> tuple[int,tuple[int,...]]:
    check(n>=1,'positive input')
    if n==1:return 0,(0,)
    original=score(n);limit=(original.bit_length()-1)//2
    values=[(original,0)];x=n;p2=p3=1;A=0
    # No early stopping: enumerate the entire proved baseline horizon.
    for k in range(1,limit+1):
        bit=x%2
        if bit:A=3*A+p2;p3*=3
        p2*=2;x=advance(x)
        z=p3*n+A-p2*n
        check(z==p2*(x-n),'physical raw numerator')
        if z:values.append((score(z),k))
    best=min(a for a,k in values)
    check(n<=best<=n*n,'proper rank')
    return best,tuple(k for a,k in values if a==best)

def word_data(w: str) -> tuple[int,int]:
    # Reverse rational branch maps recover the forward affine offset.
    mul,add=Fraction(1),Fraction(0)
    for b in reversed(w):
        if b=='0':mul*=2;add*=2
        else:mul*=Fraction(2,3);add=(2*add-1)/3
    q=w.count('1'); A=-add*3**q
    check(A.denominator==1 and mul==Fraction(2**len(w),3**q),'word affine data')
    return q,int(A)

def params(w: str) -> dict:
    m=len(w);q,A=word_data(w);P=2**m;Q=3**q;D=Q-P
    check(D>0,'positive expansion')
    check(not any(m%d==0 and all(w[i]==w[i%d] for i in range(m)) for d in range(1,m)), 'primitive period')
    As=[];depths=[]
    for r in range(m):
        v=w[r:]+w[:r];av=word_data(v)[1];As.append(av)
        center=Fraction(-av,D);x=center
        for s,bit in enumerate(v[:-1],1):
            check(x.denominator%2==1 and x.numerator%2==int(bit),'rational phase parity')
            x=(3*x+1)/2 if bit=='1' else x/2
            z=2**s*(x-center)
            check(z!=0,'shorter period found')
            depths.append(v3(z.numerator)-v3(z.denominator))
    b=max([0]+depths); j=1;mult=Fraction(Q,P)
    while mult<2**(m+1):j+=1;mult*=Fraction(Q,P)
    K=(j+1)*m;M=2*3**K+max(As)+1;H=b+1
    while Fraction(3**H,3**b)<=4*(D+1)**2:H+=1
    return dict(word=w,m=m,q=q,A=A,P=P,Q=Q,D=D,b=b,j0=j,K0=K,M=M,Amax=max(As),H0=H,U=6*P*D,phase_values_sha256=seal(depths))

def inverse(a: int,mod: int) -> int:
    if mod==1:return 0
    a%=mod;r0,r1=a,mod;s0,s1=1,0
    while r1:
        q=r0//r1;r0,r1=r1,r0-q*r1;s0,s1=s1,s0-q*s1
    check(r0==1,'unit inverse');return s0%mod

def whole_old_rank(n: int) -> int:
    check(n>1,'old comparison is noncore')
    best=min(score(n),score(n-1));a=2;z=n+5;power=4
    # z_a grows strictly for a>=2; each subsequent component is at least z_a.
    while z<=best:
        best=min(best,score(z));z=3*z+power*(2*n+1);power*=2;a+=1
    return best

def trial(p: dict,extra: int,L: int,which: int) -> dict:
    w=p['word'];m=len(w);q=p['q'];P=p['P'];Q=p['Q'];D=p['D'];A=p['A']
    H=p['H0']+extra;U=p['U'];threshold=3**(H+q*(L+1))*U**2;c=0
    while 2**(2*c)<threshold:c+=1
    N0=1
    while P**N0<=2*D*U+2*D*p['M']+2*p['Amax'] or Q**N0<2**(c+1)*P**N0:N0+=1
    N=N0+L+1;residue=A*inverse(P**N*3**H,D)%D if D>1 else 0
    units=[residue+t*D for t in range(7) if 0<residue+t*D<=6*D and (residue+t*D)%6 in (1,5)]
    check(len(units)==2,'ordinary unit lifts');u=units[which]
    n,rem=divmod(P**N*3**H*u-A,D);check(rem==0 and n>=p['M'],'ordinary source')
    states=[];ranks=[];x=n;odd=0;first=P**(2*N)*3**H*u*u
    for r in range(m*L+1):
        a,ks=rank(x);check(ks==(m,),'all candidate lengths checked')
        check(a*2**(2*r)==first*3**odd,'phase rank transport')
        states.append(x);ranks.append(a)
        if r<m*L:
            check(str(x%2)==w[r%m],'physical switch word');odd+=x%2;x=advance(x)
    y=n
    for i in range(m*N):
        check(y%2==int(w[i%m]),'full finite period guard');y=advance(y)
    check(states[-1]>n and Fraction(ranks[-1],ranks[0])==Fraction(Q,P*P)**L,'growth versus rank')
    old=[]
    if w=='111010':
        for i in range(L):
            s,t,y=states[6*i],states[6*i+4],states[6*i+6]
            a,b,cost=whole_old_rank(s),whole_old_rank(t),whole_old_rank(y)
            check(a*9==(s-1)**2 and b*9==(t+5)**2,'complete old dictionary minima')
            check(b>a and 4*cost>b and 16*cost<9*b,'old quarter-unsafe endpoints')
            # Literal maximal odd runs, without an affine mode formula.
            z=s;as_=0
            while z%2:z=advance(z);as_+=1
            check(as_==3 and advance(z)==t,'first whole odd run')
            z=t;at=0
            while z%2:z=advance(z);at+=1
            check(at==1 and advance(z)==y,'second whole odd run')
            old.append([a,b,cost])
        check(Fraction(whole_old_rank(states[-1]),whole_old_rank(n))>Fraction(81,64)**(2*L),'old rank growth')
        check(Fraction(ranks[0],whole_old_rank(n)) < Fraction(4,27),'initial rank comparison')
    return dict(word=w,H=H,L=L,which=which,N0=N0,N=N,c=c,u=u,source_bits=n.bit_length(),
                source_sha256=seal(n),first_rank_sha256=seal(ranks[0]),phases=len(states),winning_length=m,
                states_sha256=seal(states),ranks_sha256=seal(ranks),old_unsafe_edges=2*L if old else 0,old_comparison_sha256=seal(old))

def parity_rows() -> dict:
    out=[]
    for k in range(1,13):
        seen=set();P=2**k
        for n in range(P,2*P):
            x=n;bits=[]
            for _ in range(k):bits.append(x%2);x=advance(x)
            q=sum(bits);A=P*x-3**q*n
            check(0<=A<=3**k-P and P*(x-n)==(3**q-P)*n+A,'actual affine bounds')
            seen.add(tuple(bits))
        check(len(seen)==P,'all physical parity words');out.append([k,len(seen)])
    return dict(rows=out,words=sum(r[1] for r in out))

def reconstruct() -> dict:
    profiles=[params(w) for w in WORDS]
    families=[trial(p,e,L,i) for p in profiles for e in (0,2) for L in (1,3) for i in (0,1)]
    core=[];safe=[];counts=Counter();guards=0;long=0
    for n in range(2,SCAN+1):
        a,ks=rank(n);x=n;d={}
        for k in range(1,max(ks)+1):x=advance(x);d[k]=x-n
        guard=(0 in ks and n%2==0) or any(k>0 and d[k]%2==0 for k in ks)
        nxt=rank(advance(n))[0]
        check(not guard or nxt<a,'rotation conclusion');guards+=guard
        counts[min(ks)]+=1;long+=min(ks)>=4
        core.append([n,a,list(ks),nxt,guard])
        x=n;length=0
        while x!=1:
            y=advance(x)
            if rank(y)[0]>=rank(x)[0]:break
            length+=1;check(length<=a,'strict integer descent');x=y
        K=(a.bit_length()-1)//2
        check(length**2<25*(K+1)**2*a,'safe count bound');safe.append([n,length,x])
    # Full source scan is complete by Gamma(n)>=n; it shares no word-displacement enumerator.
    ranks_by_source={n:rank(n)[0] for n in range(2,max(LEVELS)+1)}
    balls=[];tails=[];scale=2**80
    for M in LEVELS:
        ns=[n for n in range(2,M+1) if ranks_by_source[n]<=M];K=(M.bit_length()-1)//2
        check(isqrt(M)-1<=len(ns) and len(ns)**2<25*(K+1)**2*M,'sublevel spectrum')
        balls.append(dict(M=M,count=len(ns),maximum=max(ns,default=0),sources_sha256=seal(ns)))
        total=sum(scale//ranks_by_source[n]**2 for n in ns)
        tails.append(dict(J=K,cutoff=M,safe_clock=5*(K+1)*2**K,tail=str(Fraction(80*(7*K+15),49*8**K)),
                          finite_lower_units=total,finite_upper_units=total+len(ns),rounding_bits=80))
    spikes=[]
    for H in (1,2,3,4,8,16,32,64):
        n=3**H;y=advance(n);a,ks=rank(n);b,_=rank(y)
        check((a,ks)==(n,(0,)) and b**10>3**(11*H),'all-prefix spike')
        rays=[]
        for r in range(6):
            x=n<<r;check(rank(x)[0]>=n,'ray rank');rays.append([r,rank(x)[0]])
        spikes.append(dict(H=H,n=n,y=y,source_rank=a,endpoint_rank=b,ray_sha256=seal(rays)))
    boundary=[];x=1932103
    for i in range(8):a,ks=rank(x);boundary.append([i,x,a,list(ks)]);x=advance(x)
    check([boundary[i][2] for i in (0,6,7)]==[1479901446144,29265629184,4484692426800],'boundary numbers')
    check(boundary[7][2]>boundary[6][2],'no unlimited guard renewal')
    check(advance(advance(2))==2 and rank(2)[0]==4,'no false zero rank from return')
    p=dict(schema='APR-v1',base=BASE,scope=dict(collatz_proved=False,universal_selector=False,
               all_parameter_proofs_by_finite_computation=False,rank_candidates='actual nonzero prefix displacements',
               zero_displacements='omitted',rank_domain='positive integers; 1 absorbed'),
           profiles=profiles,families=families,parity=parity_rows(),
           core=dict(cutoff=SCAN,sources=len(core),rotation_guards=guards,one_step_decreases=sum(r[3]<r[1] for r in core),
                     long_winners=long,winner_counts={str(k):v for k,v in sorted(counts.items())},rows_sha256=seal(core)),
           safe=dict(sources=len(safe),maximum_steps=max(r[1] for r in safe),reaches_one=sum(r[2]==1 for r in safe),rows_sha256=seal(safe)),
           balls=balls,rank_tails=tails,spikes=spikes,boundary_counterexample=boundary,
           exact_constants=dict(four9_gt_three11=4**9>3**11,safe_occupation='21200/27',global_rank_reciprocal_bound=60))
    return dict(payload=p,sha256=seal(p))

def compact_expected(full: dict) -> dict:
    p={k:v for k,v in full['payload'].items() if k!='families'}
    rows=full['payload']['families']; retained=[0,24,31,63]
    p['family_corpus']={'retained_indices':retained,'rows_sha256':seal(rows),
        'cases':len(rows),'phases':sum(r['phases'] for r in rows),
        'old_unsafe_edges':sum(r['old_unsafe_edges'] for r in rows)}
    p['families']=[r for i,r in enumerate(rows) if i in retained]
    p['full_reconstruction_sha256']=seal(full['payload'])
    p['schema']='APR-compact-v1'
    return {'payload':p,'sha256':seal(p)}

def validate(given: dict,expected: dict) -> None:
    check(set(given)=={'payload','sha256'},'report shape')
    check(given['sha256']==seal(given['payload']),'seal mismatch')
    check(encode(given)==encode(expected),'mathematics, scope or coverage differs')

def self_test(expected: dict) -> int:
    mutations=[lambda p:p['scope'].update(collatz_proved=True),
               lambda p:p['scope'].update(zero_displacements='rank zero'),
               lambda p:p['core'].update(cutoff=8191),
               lambda p:p['families'][0].update(N0=p['families'][0]['N0']+1),
               lambda p:p['families'][-1].update(winning_length=3),
               lambda p:p['families'][0].update(phases=p['families'][0]['phases']-1),
               lambda p:p['rank_tails'][-1].update(tail='0'),
               lambda p:p['balls'][-1].update(sources_sha256='0'*64),
               lambda p:p['balls'][-1].update(count=p['balls'][-1]['count']-1),
               lambda p:p['spikes'][0].update(endpoint_rank=p['spikes'][0]['endpoint_rank']-1),
               lambda p:p['boundary_counterexample'][7].__setitem__(2,p['boundary_counterexample'][6][2]),
               lambda p:p['profiles'][0].update(H0=p['profiles'][0]['H0']-1)]
    seen=set()
    for change in mutations:
        bad=copy.deepcopy(expected);change(bad['payload']);bad['sha256']=seal(bad['payload'])
        check(bad['sha256']!=expected['sha256'] and bad['sha256'] not in seen,'genuine distinct mutation');seen.add(bad['sha256'])
        try:validate(bad,expected)
        except ValueError as error:check('mathematics' in str(error),'must reject beyond hash')
        else:raise ValueError('resealed false report accepted')
    return len(mutations)

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('report',type=Path);ap.add_argument('--self-test',action='store_true');ap.add_argument('--output',type=Path)
    ap.add_argument('--full-output',type=Path)
    args=ap.parse_args();full=reconstruct();expected=compact_expected(full);validate(json.loads(args.report.read_text()),expected)
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(encode(expected)+b'\n')
    if args.full_output:args.full_output.parent.mkdir(parents=True,exist_ok=True);args.full_output.write_bytes(encode(full)+b'\n')
    print('SEPARATE REPLAY PASS',expected['sha256'])
    if args.self_test:print('RESEALED CORRUPT REPORTS REJECTED',self_test(expected))

if __name__=='__main__':main()
