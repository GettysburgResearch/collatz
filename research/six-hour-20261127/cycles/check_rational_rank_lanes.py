"""Independent exact modular, physical and positive-curvature controls.

Multi-sheet lane tests below are labeled artificial. They satisfy exact modular
transport and curvature inequalities but do not claim the affine cycle recurrence.
"""
from collections import Counter
from itertools import product
from math import gcd
from random import Random
import json


def check(ok, tag):
    if not ok:
        raise ArithmeticError(tag)


def subgroup(d):
    todo = [1 % d]
    seen = set(todo)
    for a in todo:
        for n in (2,3):
            y = n*a % d
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def order(v, d):
    x = v
    for k in range(1,d+1):
        if x == 1 % d:
            return k
        x = x*v % d
    raise ValueError('not unit')


def artificial_lanes():
    counts = Counter()
    samples = []
    for d in (1,5,7,11,13,17,19,23,35,55,65,77,85,91):
        U = subgroup(d)
        for q in (17,23,31,37,43,47):
            a = q+round(0.58*q)
            if gcd(a,q)>1:
                continue
            rho = lambda h: pow(3,h,d)*pow(2,-(h*a//q),d)%d
            g = order(rho(q),d)
            P = g*q
            check(len(U)%g==0,'group order divisibility')
            T = len(U)//g
            choices = {}
            for h in range(1,P):
                if rho(h)==1%d:
                    t = (h*a)%q
                    check(t not in choices and t>0,'unique compatible lift')
                    choices[t] = h
            check(sorted(choices)==list(range(T,q,T)),'exact offsets')
            counts['genuine_modular_clock_schedules']+=1
            counts['chronological_lags_enumerated']+=P-1
            if T>=q:
                continue
            h = choices[T]
            f = [(i*a)%q for i in range(P)]
            # A C1 convex quadratic between octave endpoints; the derivative
            # at q is twice that at 0. Round each rank to its true unit coset
            # and an odd positive integer. This introduces error below 2d.
            K = []
            for i,r in enumerate(f):
                center=100*d*(3*q*q+2*r*q+r*r)
                n=center+rho(i)
                if n%2==0:
                    n+=d
                K.append(n)
            check(len(set(K))==P,'distinct multicover ranks')
            def extended(i,j):
                return K[(i+j*h)%P]<<((f[i]+j*T)//q)
            J=[extended(i,2)-2*extended(i,1)+extended(i,0) for i in range(P)]
            check(min(J)>=d and all(v%d==0 for v in J),'artificial positive curvature')
            G=[extended(i,1)-extended(i,0) for i in range(P)]
            check(sum(J)==sum(G[(i+h)%P] for i,r in enumerate(f) if r+T>=q),'global wrap sum')
            lanes=[]
            for i in range(P):
                if f[i]>=T:
                    continue
                chain=[i]
                while f[chain[-1]]+T<q:
                    chain.append((chain[-1]+h)%P)
                lanes.append(chain)
            check(len(lanes)==g*T and sorted(i for chain in lanes for i in chain)==list(range(P)),'full lane partition')
            check(min(map(len,lanes))==q//T,'minimum lane length')
            for t,hh in choices.items():
                k=t//T
                check(hh==k*h%P,'compatible k-fold lift')
                vals=[extended(i,k)-extended(i,0) for i in range(P)]
                check(min(vals)>=d and all(v%d==0 for v in vals),'wide adjusted congruence')
                check(max(Counter(vals).values())<=g*T,'exact multiplicity upper bound')
                for i in range(P):
                    c=(f[i]+T)//q
                    rhs=sum(J[(i+j*h)%P]<<((f[i]+j*T)//q) for j in range(k))
                    lhs=(vals[(i+h)%P]<<c)-vals[i]
                    check(lhs==rhs and lhs>=k*d,'lifted wide curvature telescopes')
                    counts['wide_fibre_telescope_interfaces']+=1
                for chain in lanes:
                    check(all(vals[b]-vals[a]>=k*d for a,b in zip(chain,chain[1:])),'unadjusted within-lane monotonicity')
                counts['compatible_lags_on_artificial_convex_labels']+=1
            if g>1:
                counts['nonempty_multicover_schedules']+=1
                if len(samples)<8:
                    samples.append(dict(d=d,g=g,q=q,T=T,P=P,chains=len(lanes),h=h))
    return {'counts':dict(counts),'examples_of_modular_convex_chains_only':samples}


def genuine_drift():
    rng=Random(144983)
    cs=Counter()
    for q,a,g in ((11,18,1),(11,18,3),(13,21,1),(13,21,2),(17,27,3),(19,31,4),(23,37,2)):
        P=q*g
        for seed in range(15):
            r=[i*a%q for i in range(P)]
            m=[((i+1)*a)//q-(i*a)//q for i in range(P)]
            z=[0]
            for j in range(P-1):
                z.append(rng.randint(0,min(1,m[j]+z[j]-1)))
            z.append(0)
            e=[m[i]+z[i]-z[i+1] for i in range(P)]
            A=sum(e)
            n=0; E=0
            for v in e:
                n=3*n+(1<<E);E+=v
            den=(1<<A)-3**P
            divisor=gcd(den,n);d=den//divisor;x=n//divisor
            raw=[];low=[]
            for j in range(P):
                raw.append((2>>z[j])*x);low.append(2>>z[j])
                nxt=3*x+d
                check(nxt&-nxt==1<<e[j], 'true physical odd valuation')
                x=nxt>>e[j]
            if len(set(raw))<P:
                continue
            check(x==raw[0]//2 and gcd(6,d)==1,'periodic rational law')
            rho=lambda h: pow(3,h,d)*pow(2,-(h*a//q),d)%d
            check(order(rho(q),d)==g,'actual phase order')
            for h in range(1,P):
                t=h*a%q
                if t==0:
                    continue
                mult=rho(h)
                H=[];dH=[];G=[]
                for i in range(P):
                    tr=[(i+j*h)%P for j in range(3)]
                    B=[raw[idx]<<((r[i]+j*t)//q) for j,idx in enumerate(tr)]
                    L=[low[idx]<<((r[i]+j*t)//q) for j,idx in enumerate(tr)]
                    check(all((B[j]-pow(mult,j,d)*B[0])%d==0 for j in (1,2)),'real modular triple')
                    H.append(B[2]-2*B[1]+B[0]);dH.append(L[2]-2*L[1]+L[0]);G.append(B[1]-B[0])
                    cs['real_wrapped_triples']+=int(r[i]+2*t>=q)
                check(sum(H)==sum(G[(i+h)%P] for i in range(P) if r[i]+t>=q),'true full cyclic identity')
                for i in range(P):
                    check((H[(i+1)%P]<<m[i])==3*H[i]+d*dH[i],'genuine chronological motion')
                    cs['real_triple_interfaces']+=1
            cs['true_rational_orbits']+=1
            cs['true_multisheet_orbits']+=int(g>1)
    return dict(cs)


def seam_reset():
    types=[(1,-2,1),(1,-2,2),(1,-4,2)]
    cs=Counter();esc=set()
    for j,coeff in enumerate(types):
        for b in product((1,2),repeat=3):
            D=sum(x*y for x,y in zip(coeff,b))
            for h,m in product(range(-20,21),(1,2) if j==0 else (2,)):
                v=3*h+D
                if v%(1<<m):
                    continue
                nxt=v>>m
                check(h*nxt>=0,'direct sign flip')
                if h and not nxt:
                    esc.add((j,h,D))
                cs['integral_seam_transfers']+=1
    check(esc=={(1,-1,3),(2,1,-3)},'characterization of sign exits')
    for d in (1,5,7,11,25,35,11111):
        for A,b in product(range(1,84),range(1,65)):
            pts=[A+j*d*b for j in range(3)]
            low=[v&-v for v in pts]
            if max(low)>2:
                continue
            if b%2:
                check(low==[1,2,1],'odd normalized spacing')
            else:
                check(len(set(low))==1,'even normalized spacing')
            for m in (1,2):
                nxt=[3*w+d*l for w,l in zip(pts,low)]
                if any(v%(1<<m) for v in nxt):
                    continue
                X,Y,Z=[v>>m for v in nxt]
                if b%2:
                    check((Z-2*Y+X)*(1<<m)==-2*d,'strict return to negative')
                else:
                    check(Z-Y==Y-X and (Y-X)*(1<<m)==3*d*b,'normalized exact transfer')
                cs['explicit_physical_divisor_AP_steps']+=1
    return dict(cs)


if __name__=='__main__':
    print(json.dumps({'abstract_convex_multisheet_controls':artificial_lanes(),
                      'physical_nonasymptotic_controls':genuine_drift(),
                      'signed_seam_and_AP_controls':seam_reset()},indent=2,sort_keys=True))
