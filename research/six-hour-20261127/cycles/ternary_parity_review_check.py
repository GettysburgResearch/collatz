"""Independent parameter-square enumeration and uncollapsed six-state energy check."""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import hashlib,json

REGIONS=tuple(zip((Q(0),Q(1,4),Q(1,2)),(Q(1,4),Q(1,2),Q(3,4))))
TARGETS=((Q(9,20),Q(99,100)),(Q(7,10),Q(109,100)),(Q(87,100),Q(123,100)))
EXPECTED=('c462f7c334aeb5f9bc08f422306713f6ee7b0a109f138ed06e329d7f03520ba0','243c4370ce8239ff376801347df5ea3471efa556b7120ffa6016bf02f092da8a','ec07dc3cc112b42e2c4252a714ec886ccd1c556f322b6f386320961b197a700f')
SIX=[v for v in product((0,1),repeat=4) if v[0]+v[1]==v[2]+v[3]]
I=frozenset(((0,0),(1,1)))

def square_schedules(alpha,n):
    a,b=alpha.as_integer_ratio()
    cuts=sorted({(-j*a)%b for j in range(n+1)}|{b})
    regions=[set() for _ in REGIONS]
    def add(f,g,start,stop,single=False):
        out=bytearray()
        f%=6*b;g%=6*b
        for _ in range(n):
            c=g<f;ff=(f+6*a)%(6*b);gg=(g+6*a)%(6*b)
            out.append(8*(ff<f)+4*(gg<g)+2*c+(gg<ff))
            f,g=ff,gg
        for i,(l,h) in enumerate(REGIONS):
            if (single and l<=start<=h) or (not single and h>start and l<stop):
                regions[i].add(bytes(out))
    for i,(f0,f1) in enumerate(zip(cuts,cuts[1:])):
        for j,(g0,g1) in enumerate(zip(cuts,cuts[1:])):
            if i!=j:
                carry=int(g0<f0)
                add(3*(f0+f1),3*(g0+g1),Q(g0-f1,b)+carry,Q(g1-f0,b)+carry)
            else:
                w=g1-g0
                add(6*g0+2*w,6*g0+4*w,Q(0),Q(w,b))
                add(6*g0+4*w,6*g0+2*w,1-Q(w,b),Q(1))
                add(6*g0,6*g0,Q(0),Q(0),True)
    return regions

def relation(sym,k):
    m,mm,c,cc=1+(sym>>3),1+(sym>>2&1),sym>>1&1,sym&1
    return frozenset((x,y) for x,y in product((0,1),repeat=2)
          if m+x-y>=1 and mm+(x^k^c)-(y^k^cc)>=1)
def join(left,right):
    return frozenset((a,c) for a,b in left for b1,c in right if b==b1)
rels={(s,k):relation(s,k) for s in range(16) for k in range(2)}
from functools import lru_cache
join=lru_cache(None)(join)
@lru_cache(None)
def rate(B):
    return [(i,j) for i,p in enumerate(SIX) for j,q in enumerate(SIX) if all((x,y) in B for x,y in zip(p,q))]
def energy(word,k):
    state=None;R=I;factor=1
    for i,sym in enumerate(word):
        keep=bool(k or (sym&2))
        if not k and i==0 and keep:
            factor=16;keep=False
        if keep:
            if state is None: state=[1]*6
            else:
                nxt=[0]*6
                for x,y in rate(R):nxt[y]+=state[x]
                state=nxt
            R=I
        R=join(R,rels[(sym,k)])
    return factor*(sum(state) if state is not None else 1)

def brute(word,k):
    paths={(x,()) for x in (0,1)}
    for sym in word:
        c=(sym>>1)&1
        paths={(y,ds+((1<<c)*(2-(x^c^k))-(2-x),)) for x,ds in paths
               for xx,y in rels[(sym,k)] if xx==x}
    ds={seq for _,seq in paths}
    nums=[]
    for seq in ds:
        B=0;M=0
        for delta,sym in zip(seq,word):
            B=3*B+(1<<M)*delta
            M+=1+(sym>>3)
        nums.append(B)
    mod=3**len(word);pair=Counter((x+y)%mod for x in nums for y in nums)
    zero=sum(n*n for n in pair.values())
    assert zero<=energy(word,k)
    if len(word)<=4:
        assert all(sum(v*pair[(x+h)%mod] for x,v in pair.items())<=zero for h in range(mod))
    return zero

def main():
    a=[Q(584961,10**6),Q(5849625,10**7),Q(584964,10**6)]
    words=square_schedules(a[1],64)
    assert words==square_schedules(a[0],64)==square_schedules(a[2],64)
    # Between these slopes the cut order, lift labels, and pairwise cut differences
    # relative to every fixed u-sector boundary remain constant.
    for k in range(-64,65):
        for u in (Q(0),Q(1,4),Q(1,2),Q(3,4)):
            assert (k*a[0]-u).__floor__()==(k*a[2]-u).__floor__()
    maxima=[]
    for j,ws in enumerate(words):
        assert hashlib.sha256(b''.join(sorted(ws))).hexdigest()==EXPECTED[j]
        vals=[max(energy(w,k) for w in ws) for k in (0,1)]
        assert all(x**b.denominator<3**(64*b.numerator) for x,b in zip(vals,TARGETS[j]))
        maxima.append(vals)
    controls=0
    for n in (3,4,6):
        ws=set().union(*square_schedules(a[1],n))
        for w in ws:
            for k in (0,1):
                brute(w,k);controls+=1
    assert Q(5,9)+Q(1,200)+Q(1,120)==Q(128,225)<3/Q(5116201,10**6)
    print(json.dumps({'sector_schedule_counts':[len(ws) for ws in words],
       'independent_six_state_maxima':maxima,'literal_distinct_drift_checks':controls,
       '2018_plotkin_upper':'128/225'},indent=2))
if __name__=='__main__':main()
