"""All three real two-phase regions for stable valuation parity. Integer-only."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import hashlib,json

N=64
BASE=2000000
ALPHAS=(1169922,1169925,1169928)
REGIONS=((Q(0),Q(1,4)),(Q(1,4),Q(1,2)),(Q(1,2),Q(3,4)))
CAPS=((Q(9,20),Q(99,100)),(Q(7,10),Q(109,100)),(Q(87,100),Q(123,100)))
pairs=[p for p in product(range(2),repeat=4) if p[0]+p[1]==p[2]+p[3]]
classes=[0 if p==(0,0,0,0) else 1 if p==(1,1,1,1) else 2 for p in pairs]
def compose(a,b):
    return sum(int(any((a>>(2*i+k)&1) and (b>>(2*k+j)&1) for k in (0,1)))<<(2*i+j) for i in (0,1) for j in (0,1))
comp=[[compose(a,b) for b in range(16)] for a in range(16)]
lift=[]
for B in range(16):
    rows=[]
    for q in ((0,0,0,0),(1,1,1,1),(0,1,0,1)):
        r=[0,0,0]
        for p,cl in zip(pairs,classes):
            if all(B>>(2*x+y)&1 for x,y in zip(p,q)):r[cl]+=1
        rows.append(r)
    lift.append(rows)

def transition(sym,k):
    m=1+(sym>>3);mm=1+((sym>>2)&1);c=(sym>>1)&1;c1=sym&1
    return sum(int(m+x-y>=1 and mm+(x^(c^k))-(y^(c1^k))>=1)<<(2*x+y) for x in (0,1) for y in (0,1))
trans=[[transition(s,k) for s in range(16)] for k in (0,1)]
def energy(word,k):
    x=y=z=1;flag=False;A=9;factor=1
    for i,s in enumerate(word):
        active=k or (s&2)
        if not k and i==0 and active:active=False;factor=16
        if active:
            if flag:
                r,b,c=lift[A]
                x,y,z=r[0]*x+r[1]*y+r[2]*z,b[0]*x+b[1]*y+b[2]*z,c[0]*x+c[1]*y+c[2]*z
            flag=True;A=9
        A=comp[A][trans[k][s]]
    return factor*(x+y+4*z if flag else 1)

def faces(cuts,mod):
    cuts=sorted(set(cuts));assert cuts[0]==0
    end=cuts[1:]+[mod]
    return [v for x,y in zip(cuts,end) for v in (2*x,x+y)]

def allregions(a):
    # Rank-parameter breakpoints are u=k alpha (mod one), plus region edges.
    ulabels=defaultdict(list)
    for k in range(-N,N+1):
        z=k*a;ulabels[z%BASE].append(('r',k,z//BASE))
    for k in range(4):ulabels[BASE*k//4].append(('b',k,0))
    sig=[sorted(ulabels[u]) for u in sorted(ulabels)]
    regions=[set() for _ in REGIONS];nuf=nfaces=0
    for u in faces(ulabels,BASE):
        hit=[i for i,(lo,hi) in enumerate(REGIONS) if lo*(2*BASE)<=u<=hi*(2*BASE)]
        if not hit:continue
        nuf+=1
        fc=[(-j*2*a-t)%(2*BASE) for j in range(N+1) for t in (0,u)]
        for f in faces(fc,2*BASE):
            nfaces+=1;w=bytearray();den=4*BASE;z=f
            for _ in range(N):
                c=z+2*u>=den;m=z+4*a>=den;mm=(z+2*u)%den+4*a>=den;z=(z+4*a)%den;c1=z+2*u>=den
                w.append(8*m+4*mm+2*c+c1)
            words=bytes(w)
            for i in hit:regions[i].add(words)
    return sig,regions,nuf,nfaces

def direct(word,k):
    # Brute-force distinct signed drift strings and their ternary modular energy.
    m=[1+(s>>3) for s in word];paths={(x,()) for x in (0,1)}
    for s in word:
        c=(s>>1)&1;A=trans[k][s];out=set()
        for x,ds in paths:
            y=x^(k^c);dr=(1<<c)*(2-y)-(2-x)
            for xp in (0,1):
                if A>>(2*x+xp)&1:out.add((xp,ds+(dr,)))
        paths=out
    vals=[]
    for ds in {ds for x,ds in paths}:
        t=0;v=0
        for e,j in zip(m,ds):v=3*v+(1<<t)*j;t+=e
        vals.append(v%3**len(word))
    f=defaultdict(int)
    for x in vals:
        for y in vals:f[(x+y)%3**len(word)]+=1
    return sum(v*v for v in f.values())

def run():
    # Exact corner controls also pin the irrational limiting rotation.
    assert 1<<1584961<3**1000000<1<<1584964
    sig,sets,nu,nf=allregions(ALPHAS[1])
    for aa in (ALPHAS[0],ALPHAS[2]):
        s,r,n1,n2=allregions(aa);assert s==sig and r==sets and n1==nu and n2==nf
    result=[];short=set()
    for j,words in enumerate(sets):
        for w in words:short.add(w[:5])
        vals=[max(energy(w,k) for w in words) for k in (0,1)]
        for v,e in zip(vals,CAPS[j]):assert v**e.denominator<3**(N*e.numerator)
        result.append(dict(region=[str(v) for v in REGIONS[j]],schedules=len(words),max_energy=vals,strict_exponent_bounds=[str(c) for c in CAPS[j]],schedule_digest=hashlib.sha256(b''.join(sorted(words))).hexdigest()))
    for w in short:
        for k in (0,1):assert direct(w,k)<=energy(w,k)
    upper=max(CAPS[0]+((CAPS[1][0]+CAPS[2][1])/2,(CAPS[1][1]+CAPS[2][0])/2))
    assert upper==Q(99,100)
    return dict(length=N,slope_endpoints=[str(Q(a,BASE)) for a in ALPHAS],u_faces=nu,parameter_phase_faces=nf,distinct_five_site_exact_controls=2*len(short),sector_bounds=result,orientation_bound=str(upper))
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
