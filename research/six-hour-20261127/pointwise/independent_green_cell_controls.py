"""Independent finite rows for physical prebirth costs, Green boosts and spatial entropy."""
from collections import Counter,defaultdict
from fractions import Fraction as Q
from math import prod
import json

def test(x, tag):
    if not x: raise ValueError(tag)

def gap(x):
    z=3*x+1
    e=(z&-z).bit_length()-1
    return e,z>>e

def boost(r):
    d=max(13,r)
    return 1+Q(1,2*d)+Q(1,12*d*d)

def representative(x,mod):
    r=x%mod
    return r if r%2 else r+mod

def green():
    V=4095
    per=defaultdict(Counter)
    Ap=Counter()
    eq=Counter()
    for v in range(1,V+1,2):
        x=v
        mod=1; A=0; a=Q(1); depth=0
        while not (v<(1<<(A+1))):
            r=representative(x,mod)
            test(r!=x and r<=x,'prebirth ternary representative')
            per[depth][r]+=1
            a*=boost(r)
            e,x=gap(x); A+=e; mod*=3; depth+=1
        test(representative(x,mod)==x,'actual birth iff cutoff')
        for power in (1,2,4):
            Ap[power]+=a**power
        x=v; mod=1; A=0
        mode=Q(1); direct=Q(1,v**3); k=0
        while k<18:
            r=representative(x,mod)
            if r==x:
                eq['postbirth_vertex_rows']+=1
            w=boost(r)
            gain=Q(3**k,1<<A)
            test((gain/x)**3*mode**2==direct,'raw squared source contributions')
            rounded=Q(3**(3*k//2),1<<((3*A+1)//2))*mode
            test(rounded**2/x**3==direct/(3**(k%2)*2**(A%2)),'single parity rounding')
            if x>=13:
                test((w**2)*Q(3*x,3*x+1)**3>1,'strict increasing high contribution')
            eq['finite_green_phase_rows']+=1
            mode*=w; direct*=w**2*Q(3*x,3*x+1)**3
            e,x=gap(x); A+=e; mod*=3; k+=1
    for j,counts in per.items():
        total=sum(Q(c,r) for r,c in counts.items())
        test(total<=Q(V*(j+1),3**j),'uniform total prebirth reciprocal at each depth')
        eq['occupied_prebirth_depths']+=1
    B=boost(13)
    for power,S in Ap.items():
        cp=Q(7,12)*power*B**(power-1)
        upper=V*(1+cp/(1-B**power/3)**2)
        test(S<=upper,'uniform prebirth moment')
        eq['prebirth_power_rows']+=1
    # Compare clock differences at every common physical site along two fixed finite rays.
    ray=[];x=27;A=0
    while x!=1:
        ray.append((x,A));e,x=gap(x);A+=e
    lookup={x:(j,A) for j,(x,A) in enumerate(ray)}
    for v in range(1,V+1,2):
        x=v;k=A=0; offsets=None
        while x!=1:
            if x in lookup:
                t,T=lookup[x]
                delta=k-t,A-T
                if offsets is not None:
                    test(delta==offsets,'fixed clock shift on common continuation')
                    eq['merged_clock_and_phase_rows']+=1
                offsets=delta
            e,x=gap(x);A+=e;k+=1
    return dict(eq)

def powers(c):
    return prod(x**x for x in c if x)
def cells():
    stats=Counter()
    for x in range(3,380,2):
        xs=[];seen=set()
        while x not in seen and len(xs)<105:
            seen.add(x);xs.append(x);x=(3*x+1)//2 if x%2 else x//2
        P=len(xs); bits=[x%2 for x in xs]
        for m in (3,6,9):
            N=P-m+1
            if N<=0:continue
            windows=[tuple(bits[i:i+m]) for i in range(N)]
            labels=[x//(1<<(m-1)) for x in xs[:N]]
            W,K=Counter(windows),Counter(labels)
            test(len(set(zip(windows,labels)))==N,'cell and code determine physical index')
            test(N**N>=powers(K.values())*powers(W.values()),'cell entropy chain')
            for k in (1,2):
                joint=Counter((w[j-k:j],w[j]) for w in windows for j in range(k,m))
                cond=Counter()
                for (hist,_),nr in joint.items():cond[hist]+=nr
                test(N**N*powers(joint.values())<=powers(W.values())*(1<<(k*N))*powers(cond.values()),
                     'full physical block conditional law')
                stats['higher_conditional_rows']+=1
            for selected in ({0,2,3},{1,3,5,7}):
                hits=[w for c,w in zip(labels,windows) if c in selected]
                test(max(Counter(hits).values(),default=0)<=len(selected),'family covering multiplicity')
                stats['moving_interval_family_rows']+=1
            stats['coarse_cell_entropy_rows']+=1
    return dict(stats)

if __name__=='__main__':
    print(json.dumps(dict(green=green(),physical_cells=cells()),sort_keys=True,indent=2))
