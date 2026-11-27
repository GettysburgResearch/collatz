"""Independent full-denominator support and preceding-maximum excursion checks."""
from collections import Counter
from itertools import product
from math import gcd
from random import Random
import json
from check_residue_source_physical import orbit


def req(ok,msg):
    if not ok:raise ValueError(msg)


def unit_group(d):
    seq=[1%d]
    values=set(seq)
    for x in seq:
        for n in (2,3):
            z=x*n%d
            if z not in values:
                values.add(z);seq.append(z)
    return values


def analyze(w,stats,eg):
    o=orbit(w)
    if not o:return
    d,N=o;P=len(N);A=sum(w);g=gcd(A,P);q=P//g;a=A//g
    D=0;cuts=[]
    for e in w:cuts.append(D);D+=P*e-A
    ii=cuts.index(max(cuts))
    N=N[ii:]+N[:ii];w=w[ii:]+w[:ii]
    E=0;z=[]
    for j,e in enumerate(w):z.append(j*a//q-E);E+=e
    H=max(z)
    rho=lambda h: pow(3,h,d)*pow(2,-(h*a//q),d)%d
    om=rho(q);u=1%d
    omega={u};tmp=om
    while tmp not in omega:
        omega.add(tmp);tmp=tmp*om%d
    k=len(omega)
    req(g%k==0,'multiplicity above exact order')
    K=[n<<(H-j) for n,j in zip(N,z)]
    hist=Counter(n%d for n in K)
    req(all((n-K[0]*rho(i))%d==0 for i,n in enumerate(K)),'exact initial-coset law')
    if q==1:
        val=k;cap=g//k
    else:
        beta=rho(pow(a,-1,q))
        # Distinguish first quotient order below q versus no early coincidence.
        power=1%d;T=None
        for t in range(1,q+1):
            power=power*beta%d
            if power in omega:
                T=t;break
        val=k*(q if T is None else min(q,T))
        cap=(g//k)*(1 if T is None else (q+T-1)//T)
        if T is not None:
            req(all(v in [(g//k)*(q//T),cap] for v in hist.values()),'balanced positive atoms')
    req(len(hist)==val and max(hist.values())==cap,'exact support and largest atom')
    if d<=1500:
        S=len(unit_group(d));T=S//k
        req(S%k==0,'subgroup and exact order')
        req(len(hist)==min(q*k,S) and max(hist.values())==(g//k)*((q+T-1)//T),'explicit full-group formula')
        stats['true_cycles_full_subgroup_computed']+=1
    raw=Counter(n%d for n in N);R=len(raw)
    shift=len({pow(2,H-j,d) for j in z})
    req(len(hist)<=R*shift and max(raw.values())<=cap*shift,'raw populated-fibre inequalities')
    for Z in (0,1,2,3):
        kept=[i for i in range(P) if z[i]<=Z]
        shifts={pow(2,H-z[i],d) for i in kept}
        per=Counter(N[i]%d for i in kept)
        req(all(v<=cap*len(shifts) for v in per.values()),'localized grade mass')
        stats['low_grade_populations']+=1
    # Max-ending R-window, with indices distinguished even when it makes a full lap.
    end=N.index(max(N));indices=[(end-R+j)%P for j in range(R+1)]
    start=indices[0];xtop=N[end]
    if d>=4**R:
        req((xtop+d)*(2**R)<2*d*3**R,'uncapped maximum height tradeoff')
        req(P*2**R<2*R*3**R,'uncapped period tradeoff')
        stats['large_d_uncapped_cases']+=1
    if (xtop+d)*2**R>=2*d*3**R:
        req(all(N[i]>=d for i in indices),'all historical states at least one')
        total=sum(w[i] for i in indices[:-1])
        req(total<=2*R,'low total valuation in max-ending window')
        seen={};found=False
        for j,i in enumerate(indices):
            res=N[i]%d
            if res in seen:
                first=seen[res];length=j-first
                divisions=sum(w[v] for v in indices[first:j])
                D=abs((1<<divisions)-3**length)
                req(0<D<4**R and D%d==0,'integer returning-residue determinant')
                found=True;break
            seen[res]=j
        req(found,'residue pigeonhole at maximum')
        stats['large_X_return_determinants']+=1
    req(R!=1 or d==1 or P==1,'unit diversity classification')
    stats['true_primitive_cycles']+=1
    stats['proper_order_defect']+=int(k<g)
    stats['multiple_raw_occupancy']+=int(R<P)
    if k<g and len(eg)<6:
        eg.append(dict(P=P,d=d,R=R,g=g,k=k,q=q,H=H,K_support=val,max_K_atom=cap))


def modular_controls():
    c=Counter()
    for d in (1,5,7,11,13,17,19,25,31,35,55,65,77,91,101):
        S=len(unit_group(d))
        for q in range(1,33):
            for a in range(q+1,2*q+2):
                if gcd(q,a)!=1:continue
                om=pow(3,q,d)*pow(2,-a,d)%d;v=om;k=1
                while v!=1%d:v=v*om%d;k+=1
                T=S//k
                for m in (1,2,4):
                    g=m*k
                    freq=Counter(pow(3,i,d)*pow(2,-(i*a//q),d)%d for i in range(g*q))
                    low=m*(q//T);high=m*((q+T-1)//T)
                    req(len(freq)==min(k*q,S) and max(freq.values())==high,'finite clock support')
                    actual=Counter(freq.get(v,0) for v in unit_group(d))
                    expected=Counter()
                    expected[low]+=k*(T-q%T)
                    expected[high]+=k*(q%T)
                    expected=+expected
                    req(actual==expected,'full atom count including zeros')
                    c['finite_group_schedules']+=1
                    c['synthetic_order_defects']+=int(m>1)
                    c['heterogeneous_fibre_sizes']+=int(len(actual)>1)
    return dict(c)


def main():
    W={(1,1,2,4,3,4,1,2),(1,1,1,1,4,2,2,2),(1,3),(2,),(3,),(51,)}
    for p in range(2,8):
        for w in product((1,2,3),repeat=p):
            if w==min(w[i:]+w[:i] for i in range(p)):
                W.add(w)
    for p in range(3,23):
        W.add((1,)*(p-1)+(10*p,))
    rng=Random(17942)
    for p in (11,17,19,27):
        for _ in range(30):
            W.add(tuple(rng.randrange(1,6) for j in range(p)))
    st=Counter();examples=[]
    for w in sorted(W):analyze(w,st,examples)
    print(json.dumps(dict(real=dict(st),proper_order_examples=examples,modular=modular_controls()),sort_keys=True,indent=2))


if __name__=='__main__':main()
