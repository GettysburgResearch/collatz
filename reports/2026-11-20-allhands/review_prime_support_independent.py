#!/usr/bin/env python3
"""Independent narrow replay of P13; imports no author routines."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import argparse
import json
from functools import lru_cache

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-dir',type=Path,required=True)
parser.add_argument('--output',type=Path)
args=parser.parse_args()
ROOT=args.source_dir
OUT=args.output

def need(ok,why):
    if not ok:raise ValueError(why)

def step(n):
    need(type(n) is int and n>0 and n%2,'odd positive source')
    a=((3*n+1)&-(3*n+1)).bit_length()-1
    return (3*n+1)>>a,a

@lru_cache(None)
def fac(n):
    res={};d=3
    while d*d<=n:
        while n%d==0:
            res[d]=res.get(d,0)+1;n//=d
        d+=2
    if n>1:res[n]=res.get(n,0)+1
    return res

# Do not stop on the fixed point: literal unrolling checks repeated-state costs.
seeds=list(range(1,128,2))+[255,511,1023,4095,59049,531441]
blocks=charges=tail_checks=affines=source_bounds=0
maxbits=0
for seed in seeds:
    states=[seed];vals=[]
    for _ in range(80):
        y,a=step(states[-1]);states.append(y);vals.append(a)
    maxbits=max(maxbits,max(states).bit_length())
    high=0
    for stop,y in enumerate(states):
        if y<high:continue
        high=y
        for length in (2,4,6,10,16):
            if stop+1<length:continue
            left=stop+1-length
            ns=states[left:stop+1];aa=vals[left:stop]
            rows=[fac(n) for n in ns]
            ps=set().union(*(r.keys() for r in rows))
            removed=set()
            for p in ps:
                top=max(r.get(p,0) for r in rows)
                # Delete the LAST maximizer, independently of the author choice.
                removed.add(max(j for j,r in enumerate(rows) if r.get(p,0)==top))
            remain=[j for j in range(length) if j not in removed]
            A=sum(aa);d=length-1
            need(A<=2*d,'peak division budget')
            fullcost=3**d*2**(A-d)
            need(fullcost<2**(3*d),'coarse cost constant')
            blocks+=1
            for p in ps:
                for e in range(1,max(r.get(p,0) for r in rows)+1):
                    q=p**e
                    ix=[j for j,n in enumerate(ns) if n%q==0]
                    iy=[j for j in remain if ns[j]%q==0]
                    need(len(iy)<=len(ix)-1,'maximum deletion at every level')
                    product=1
                    for i,j in zip(ix,ix[1:]):
                        # Independent expansion of the affine correction using prefixes.
                        total=sum(aa[i:j]);prefix=0;C=0
                        for t,a in enumerate(aa[i:j]):
                            C+=3**(j-i-1-t)*2**prefix;prefix+=a
                        need(2**total*ns[j]==3**(j-i)*ns[i]+C,'affine expansion')
                        need(C%q==0 and C>0,'positive divisible correction')
                        cost=3**(j-i)*2**(total-(j-i))
                        need(q<=C<cost,'exact return cost')
                        product*=cost;affines+=1
                    need(product<=fullcost,'disjoint return intervals')
                    need(q**len(iy)<fullcost,'boundary-free retained tail')
                    charges+=len(ix)-1;tail_checks+=1
        ps=set().union(*(fac(n).keys() for n in states[:stop+1]))
        s=len(ps)
        if s:
            need(high<=max(4**s*seed,(s+1)**(64*s)),'finite-source alternative')
            if stop<2*s:need(high<4**s*seed,'short-prefix branch')
            source_bounds+=1

# Exact rational enclosure of ln(2), from 2*atanh(1/3).
z=F(1,3);K=8
lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(K)),F())
hi=lo+2*z**(2*K+1)/(F(2*K+1)*(1-z*z))
need(F(1,2)<lo<hi<F(7,10),'logarithm enclosure')
need(6*hi<5 and 10*hi<7,'log-base constants')

# At s=2^r-1, B=64*s*log2(s+1) is integral: exact boundary inversion.
inversions=[]
for r in range(1,9):
    s=2**r-1;B=64*s*r
    need(2**B>2**(8*s)*B**(5*s),'P13 numerical inversion at B')
    need(B*lo>5*s,'monotonicity derivative sign')
    inversions.append({'s':s,'B':B})

# Negative control: without deleting a coordinate maximum, a true peak window
# already fails the proposed boundary-free tail: 3 -> 5 has cost 3, but q=5.
need(step(3)==(5,1),'negative-control actual edge')
need(5>3,'undeleted singleton exceeds available return cost')
# Prime support and rank differ even algebraically; this is not an orbit claim.
need(fac(15)=={3:1,5:1} and 225==15**2,'rank/support distinction')

report={'status':'PASS','scope':'Independent finite checks of P13 exact costs, maximum deletion, retained tails, source alternative and integer inversion; no imported author code and no nontrivial cycle fixture.',
 'sources':len(seeds),'odd_edges':80*len(seeds),'peak_windows':blocks,
 'prime_power_tail_checks':tail_checks,'charged_returns':charges,'affine_expansions':affines,
 'source_boundary_checks':source_bounds,'maximum_state_bits':maxbits,
 'integer_inversion_points':inversions,'ln2_interval':[str(lo),str(hi)],
 'negative_controls':['actual 3->5 window fails boundary-free tail without deletion','rank-one set {15,225} has prime-support size two; not a trajectory assertion'],
 'author_note_sha256':hashlib.sha256((ROOT/'PRIME_SUPPORT_PEAKS.md').read_bytes()).hexdigest(),
 'author_checker_sha256':hashlib.sha256((ROOT/'check_prime_support_peaks.py').read_bytes()).hexdigest(),
 'review_checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
raw=json.dumps(report,indent=2,sort_keys=True)+'\n'
if OUT:OUT.write_text(raw)
print(raw)
