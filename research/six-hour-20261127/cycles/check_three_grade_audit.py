"""Independent pair-state modular fourth-power and signed-orientation controls."""
from collections import Counter,defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, product
from math import gcd
import json

LOW=F(584961,10**6)
HIGH=F(584964,10**6)
CAP=F(21,50)
N=64


def check(truth,label):
    if not truth:
        raise ValueError(label)


def schedule(al,phase,n):
    lifted=[phase+i*al for i in range(n+1)]
    caps=tuple(2 if y-y//1 <= CAP else 1 for y in lifted)
    m=tuple(int(1+(lifted[i+1]//1)-(lifted[i]//1)) for i in range(n))
    return tuple(zip(caps,m)) + ((caps[-1],0),)


def phase_schedules(al,n):
    lines = [(j,b) for j in range(n+1) for b in (F(0),CAP)]
    cuts=sorted({(b-j*al)%1 for j,b in lines})
    faces=[a for i,a in enumerate(cuts)] + [(a+(cuts+[F(1)])[i+1])/2 for i,a in enumerate(cuts)]
    return cuts, {schedule(al,s,n) for s in faces}


def slope_critical(n):
    hits=[]
    for d in range(1,n+1):
        for z in (-CAP,F(0),CAP):
            lower=d*LOW-z
            upper=d*HIGH-z
            for m in range(-((-lower.numerator)//lower.denominator),upper//1+1):
                hits.append((d,m,z))
    return hits


def multiset(z):
    return 1 if z[0]==z[1] else 2


@lru_cache(None)
def pair_next(z,gap,cap):
    sign=1 if gap==2 else -1
    choices=[tuple(v for v in (a,a+sign) if 0<=v<=cap) for a in z]
    return tuple(Counter(tuple(sorted(p)) for p in product(*choices)).items())


def pair_mass_rows(first_cap):
    pairs=list(combinations_with_replacement(range(first_cap+1),2))
    return {(a,b,0):multiset(a)*multiset(b) for a in pairs for b in pairs}


@lru_cache(None)
def transition(a,b,m,h):
    outcomes=defaultdict(int)
    for aa,am in pair_next(a,m,h):
        for bb,bm in pair_next(b,m,h):
            outcomes[aa,bb]+=am*bm
    delta=(4 >> a[0])+(4 >> a[1])-(4 >> b[0])-(4 >> b[1])
    return delta,tuple((x,y,z) for (x,y),z in outcomes.items())


def advance(rows,m,cap):
    out=defaultdict(int)
    for (a,b,c),ways in rows.items():
        delta,edges=transition(a,b,m,cap)
        n=3*c+delta
        if n%(1 << m): continue
        carry=n//(1 << m)
        for aa,bb,multiplicity in edges:
            out[aa,bb,carry]+=ways*multiplicity
    return out


def energy(sig):
    rows=pair_mass_rows(sig[0][0])
    for i,(_,m) in enumerate(sig[:-1]):
        rows=advance(rows,m,sig[i+1][0])
    return sum(rows.values())


def direct_all_residues(sig):
    paths=[(z,0) for z in range(sig[0][0]+1)]
    exponent=0
    for i,(_,m) in enumerate(sig[:-1]):
        sign=1 if m==2 else -1
        paths=[(v,3*t+(4>>z)*(1<<exponent)) for z,t in paths for v in (z,z+sign)
               if 0<=v<=sig[i+1][0]]
        exponent+=m
    modulus=1 << exponent
    mu=Counter(t%modulus for _,t in paths)
    mu2=Counter()
    for a,ca in mu.items():
        for b,cb in mu.items():
            mu2[(a+b)%modulus]+=ca*cb
    four=Counter()
    for a,ca in mu2.items():
        for b,cb in mu2.items():
            four[(a-b)%modulus]+=ca*cb
    require_sum=len(paths)**4
    check(sum(four.values())==require_sum and max(four.values())==four[0],"Cauchy shift maximum")
    check(four[0]==energy(sig),"pair-state multiplicities")
    for c in [-17,-3,1,9,21]:
        start={(aa,bb,c):w for (aa,bb,_),w in pair_mass_rows(sig[0][0]).items()}
        for i,(_,m) in enumerate(sig[:-1]):
            start=advance(start,m,sig[i+1][0])
        check(sum(start.values())==four[-pow(3,len(sig)-1,modulus)*c%modulus],"incoming carry and all residues")
    return len(paths),len(four)


def max_energy():
    check(not slope_critical(N),"cut intersection inside the entire closed slope interval")
    mid=(LOW+HIGH)/2
    cuts,schedules=phase_schedules(mid,N)
    check(phase_schedules(LOW,N)[1]==schedules==phase_schedules(HIGH,N)[1],"endpoint faces")
    energy_table={sig:energy(sig) for sig in schedules}
    observed=max(energy_table.values())
    check(observed**5 < 3**(6*N),"modular exponent")
    checks=0; paths=0; residues=0
    for n in range(1,9):
        for sig in phase_schedules(mid,n)[1]:
            a,b=direct_all_residues(sig)
            paths+=a; residues+=b; checks+=1
    return {"closed_slope_interior_crossings":0,"full_intercept_faces":2*len(cuts),
            "full_distinct_schedules":len(energy_table),"maximum_modular_mass":observed,
            "minimum_modular_mass":min(energy_table.values()),"short_direct_schedules":checks,
            "short_single_paths":paths,"short_fourfold_residue_atoms":residues,
            "nonzero_inherited_carry_comparisons":5*checks}


def exact_admissible_count(f,u,w):
    L=F(121,50)
    return sum(0<=f+z<=L and 0<=f+z+u+w<=L for z in (0,1,2))


def orientation_checks():
    orientation_tests=interval_tests=0
    for p in range(3,13):
        for s in range(1,p):
            if gcd(s,p)!=1 or not F(1,2)<F(s,p)<F(2,3): continue
            caps=[2 if F(r,p)<=CAP else 1 for r in range(p)]
            seq=[(i*s)%p for i in range(p)]
            m=[1+int(r+s>=p) for r in seq]
            def walk(zs):
                nonlocal orientation_tests,interval_tests
                i=len(zs)-1; z=zs[-1]
                options=(z,z+(1 if m[i]==2 else -1))
                if i<p-1:
                    for v in options:
                        if 0<=v<=caps[seq[i+1]]:
                            walk(zs+(v,))
                    return
                if zs[0] not in options: return
                es=[m[i]+zs[i]-zs[(i+1)%p] for i in range(p)]
                for h in range(1,p):
                    t=(h*s)%p; u=F(t,p)
                    by_pair=[]; rev=[]
                    for i,r in enumerate(seq):
                        f=F(r,p); v=zs[(i+h)%p]-zs[i]; c=int(r+t>=p)
                        w=v-c
                        back=-v-(1-c)
                        check(back==-1-w,"reverse orientation")
                        l=1 << (2-zs[i])
                        drift=(1 << c)*(1 << (2-zs[(i+h)%p]))-l
                        check(drift==(F(2)**(-w)-1)*l,"signed grade drift")
                        check(exact_admissible_count(f,u,w)>=1,"nonempty actual interval")
                        by_pair.append(w); rev.append(back)
                        interval_tests+=1
                    check(all(es[(i+h)%p]-es[i]==by_pair[i]-by_pair[(i+1)%p] for i in range(p)),
                          "physical mismatch equals signed grade change")
                    orientation_tests+=1
            for z in range(caps[0]+1): walk((z,))
    # Rational margins for all transference assertions, using the manuscript's elementary bounds.
    check((1 << 1584961)<3**1000000<(1 << 1584964),"slope enclosed")
    check((1 << 79)<3**50,"physical band lies strictly below strip")
    check(max(abs(53*a-31)*53 for a in (LOW,HIGH))<F(1,5),"53-grid error")
    slack=F(1098,1000)/3-(F(10,1500)+(F(23,50)+F(7,265))*F(694,1000)+F(26,1500)*F(11,10))
    check(slack>0,"mismatch endpoint contradiction")
    return {"small_actual_oriented_words":orientation_tests,"rank_intersection_checks":interval_tests,
            "entropy_endpoint_rational_slack":str(slack)}


if __name__=="__main__":
    result=max_energy()
    result.update(orientation_checks())
    print(json.dumps(result,sort_keys=True,indent=2))
