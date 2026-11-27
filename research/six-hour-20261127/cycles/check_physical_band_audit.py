"""Independent exact physical-window and sparse grade repair controls."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb, factorial
from random import Random
import json


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def step(x):
    w = 3*x+1
    e = (w & -w).bit_length()-1
    return w >> e,e


@lru_cache(maxsize=20000)
def greatest_feasible(gaps,clip):
    # Prefix/suffix feasibility on the layered graph, independent of distances.
    left = [set(range(clip[0]+1))]
    for i,m in enumerate(gaps):
        left.append({y for y in range(clip[i+1]+1)
                     if any(m+x-y in (1,2) for x in left[-1])})
    right = [set(range(clip[-1]+1))]
    for i in reversed(range(len(gaps))):
        right.append({x for x in range(clip[i]+1)
                      if any(gaps[i]+x-y in (1,2) for y in right[-1])})
    right.reverse()
    return tuple(max(a & b) for a,b in zip(left,right))


def checkpath(gaps,caps,z,stats,d=7,x0=None):
    e = tuple(m+x-y for m,x,y in zip(gaps,z,z[1:]))
    require(min(e)>=1,'raw positive valuations')
    v = tuple(min(h,x) for h,x in zip(caps,z))
    u = greatest_feasible(gaps,v)
    # Recover the greatest cap-feasible lift by an independent relaxation of
    # edge inequalities until stationary. Count support distance on each side.
    trial = list(v)
    while True:
        prior = trial.copy()
        for i,m in enumerate(gaps):
            trial[i] = min(trial[i],prior[i+1]+2-m)
            trial[i+1] = min(trial[i+1],prior[i]+m-1)
        if trial==prior:
            break
    require(list(u)==trial,'maximal projection via divergent constructions')
    pred = tuple(m+x-y for m,x,y in zip(gaps,u,u[1:]))
    require(set(pred)<={1,2},'binary lifted path')
    defects={i for i,k in enumerate(e) if k>=3}
    high={i for i,(raw,h) in enumerate(zip(z,caps)) if raw>h}
    for j,(k,l) in enumerate(zip(v,u)):
        if k!=l:
            radius=min(abs(j-i) for i in defects)
            require(radius<=5,'locality of repairs')
            stats['maximum_observed_repair_radius']=max(stats['maximum_observed_repair_radius'],radius)
    changed={j for j,(a,b) in enumerate(zip(z,u)) if a!=b}
    require(all(any(abs(j-i)<=6 for i in defects|high) for j in changed),'global mask support')
    stats['path_windows'] += 1
    stats['changed_windows'] += bool(changed)
    stats['raw_maximum_grade']=max(stats['raw_maximum_grade'],max(z))
    if z[0]!=u[0] or z[-1]!=u[-1]:
        return
    raw_time=[0]
    repaired_time=[0]
    for a,b in zip(e,pred):
        raw_time.append(raw_time[-1]+a)
        repaired_time.append(repaired_time[-1]+b)
    require(raw_time[-1]==repaired_time[-1],'true/repaired terminal binary time')
    K=raw_time[-1]
    modulus=1<<K
    n=len(e)
    B=C=delta=0
    for i in range(n):
        coeff=3**(n-1-i)
        B += coeff*(1<<raw_time[i])
        C += coeff*(1<<repaired_time[i])
        if i in changed:
            delta += coeff*((1<<raw_time[i])-(1<<repaired_time[i]))
        else:
            require(raw_time[i]==repaired_time[i],'unrecorded dates coincide')
    require(B-C==delta,'ordinary integer polynomial translation')
    inv=pow(3**n,-1,modulus)
    source=(-d*inv*B)%modulus
    moved=(-d*inv*C-d*inv*delta)%modulus
    require(source==moved,'true modulo and translated relaxed source')
    if x0 is not None:
        require(source==x0%modulus,'physical starting numerator')
        stats['actual_fixed_endpoint_translations']+=1
    if changed:
        stats['nontrivial_matched_translations']+=1
    # Validate support profile reconstruction without knowing the outside raw word.
    reconstructed=list(u)
    for j in changed: reconstructed[j]=z[j]
    require(tuple(reconstructed)==z,'profile injection')
    stats['matched_endpoint_windows']+=1


def exact_lift(X):
    n,d=X.numerator,X.denominator
    k=n.bit_length()-d.bit_length()
    if k>=0:
        if n < d << k:
            k-=1
    else:
        if n << (-k) < d:
            k-=1
    return k


def cap_ratio(r,bits):
    # True cap is r<=2**(1/bits). Rational bracketing is proved by
    # (1+.6/bits)^bits <= exp(.6)<2 and log(1+.75/bits)*bits>log(2).
    # If the input is too close, fall back to the exact powered integers.
    if r <= 1+F(3,5*bits):
        return True
    if r >= 1+F(3,4*bits):
        return False
    return r.numerator**bits <= 2*r.denominator**bits


def real_windows():
    rng=Random(270226)
    stats=Counter()
    runs=0
    for _ in range(750):
        x0=(rng.randrange(1<<29,1<<31)//2)*2+1
        n=rng.choice((8,11,17,23,31))
        path=[x0]
        E=[0]
        for j in range(n):
            x,e=step(path[-1]);path.append(x);E.append(E[-1]+e)
        s=min(path)
        if s<10000000:
            continue
        # A rational lift t0 with exact exponential bound for the physical drift.
        ratio=F(x0,s)*F(3*s+1,3*s)**n
        clock=[];caps=[]
        for i in range(n+1):
            M=exact_lift(ratio)
            require(M>=0,'positive correction')
            f=ratio/(1<<M)
            require(1<=f<2,'exact lifted physical intercept')
            clock.append(M);caps.append(1+cap_ratio(f,100000))
            ratio*=3
        if not cap_ratio(F(3*s+1,3*s)**n,200000):
            continue
        z=tuple(m-t for m,t in zip(clock,E))
        require(min(z)>=0,'physical clock lower bound')
        high={i for i,x in enumerate(path) if not cap_ratio(F(x,4*s),200000)}
        require(all(raw<=h or i in high for i,(raw,h) in enumerate(zip(z,caps))),
                'raw cap violations only physically high')
        gaps=tuple(b-a for a,b in zip(clock,clock[1:]))
        checkpath(gaps,tuple(caps),z,stats,d=1,x0=x0)
        runs+=1
    require(runs>=100,'physical sample coverage')
    return dict(stats,retained_physical_windows=runs)


def abstract_windows():
    stats=Counter()
    rng=Random(901)
    alpha=F(58496250072,10**11)
    c=F(1,100000)
    for n in (5,8,13,25,40):
        # Exact cap and wrap point faces as well as actual intervening cells.
        breakpoints=sorted({(h-j*alpha)%1 for j in range(n+1) for h in (0,c)})
        faces=breakpoints+[(a+b)/2 for a,b in zip(breakpoints,breakpoints[1:]+[1])]
        for f in faces:
            g=tuple(1+((f+(j+1)*alpha)//1)-((f+j*alpha)//1) for j in range(n))
            caps=tuple(1+int((f+j*alpha)%1<=c) for j in range(n+1))
            require(all(g[i]+caps[i]-caps[i+1] in (1,2) for i in range(n)),'cap admissible')
            if n==5:
                frontier=[(z,) for z in range(3)]
                for m in g:
                    frontier=[a+(d,) for a in frontier for d in range(a[-1]+m)]
                for z in frontier:checkpath(g,caps,z,stats)
            else:
                for i in range(18):
                    z=[rng.randrange(3)]
                    for j,m in enumerate(g):
                        bound=z[-1]+m
                        if i==0:
                            nxt=bound-1 if j < n-2 else 0
                        elif i%2==0:
                            nxt=bound-1 if rng.random()<.75 else rng.randrange(bound)
                        else:
                            nxt=rng.randrange(bound)
                        z.append(nxt)
                    checkpath(g,caps,tuple(z),stats,d=(1,7,25,1009)[i%4])
    return dict(stats)


def constants():
    c,eta,tau=F(1,10**10),F(1,10**6),F(1,10**7)
    gamma=F(4,3)-F(1,20000)
    cap=(6*eta+gamma*(1-eta)+(5+eta)*26*tau)/(4+eta)
    slack=1-(3+c)*cap
    require(c*(4+eta)<eta/2 and slack>0,'separation and occupation margins')
    require(1-26*c-13*c/tau>F(98,100),'cyclic good-start fraction')
    # log(10^7)<17 since e>8/3 and (8/3)^17>10^7; ln2<1.
    require(F(8,3)**17>10**7,'entropy envelope')
    # Analytic regional inequalities used as accelerated cap comparisons.
    require(2**4<3**3<2**5,'mechanical three-letter test')
    require(sum(F(3,5)**j/factorial(j) for j in range(8))+
            F(3,5)**8/factorial(8)/(1-F(3,5)/9)<2,'exp upper bound')
    require(sum(F(7,10)**j/factorial(j) for j in range(4))>2,'log 2 < .7')
    for bits in (100000,200000):
        require(F(3,4)-F(9,32*bits)>F(7,10),'upper root bracket')
    for l in range(1,1001):
        require(3**(l+1)*comb(2*l+2,l) <= 2**(8*l),'raw-run profile budget')
    return dict(source_exponent=str(cap),positive_slack=str(slack))


if __name__=='__main__':
    print(json.dumps(dict(constants=constants(),abstract=abstract_windows(),physical=real_windows()),
                     sort_keys=True,indent=2))
