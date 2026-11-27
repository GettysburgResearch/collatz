"""Independent unordered-pair energy and multicover rational-rank checks."""
from collections import Counter,defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, product
from math import gcd
import json

LOW=F(584961,10**6)
HIGH=F(584964,10**6)
CAP=F(1,10)
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
    choices=[tuple(v for v in range(cap+1) if gap+a-v>=1) for a in z]
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
        paths=[(v,3*t+(4>>z)*(1<<exponent)) for z,t in paths for v in range(sig[i+1][0]+1)
               if m+z-v>=1]
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
    check(observed**20 < 3**(29*N),"modular exponent")
    checks=0; paths=0; residues=0
    for n in range(1,7):
        for sig in phase_schedules(mid,n)[1]:
            a,b=direct_all_residues(sig)
            paths+=a; residues+=b; checks+=1
    return {"closed_slope_interior_crossings":0,"full_intercept_faces":2*len(cuts),
            "full_distinct_schedules":len(energy_table),"maximum_modular_mass":observed,
            "minimum_modular_mass":min(energy_table.values()),"short_direct_schedules":checks,
            "short_single_paths":paths,"short_fourfold_residue_atoms":residues,
            "nonzero_inherited_carry_comparisons":5*checks}


def actual_repeated_ranks():
    from random import Random
    rng=Random(2006)
    stats=Counter()
    seen_g=set()
    for q in (5,7,11,13,17,19):
        a=(3**q).bit_length()
        s=a-q
        check(gcd(s,q)==1,'primitive mechanical base')
        for g in (2,3,4,5):
            P=g*q
            rank=[(i*s)%q for i in range(P+1)]
            m=[1+int(r+s>=q) for r in rank[:-1]]
            caps=[1+int(F(r,q)<=CAP) for r in rank]
            for _ in range(16):
                z=[0]
                for i in range(P-1):z.append(rng.randrange(1+min(caps[i+1],z[-1]+m[i]-1)))
                z.append(0)
                es=[m[i]+z[i]-z[i+1] for i in range(P)]
                N=0;h=0
                for e in es:N=3*N+(1<<h);h+=e
                det=(1<<h)-3**P
                if det<=0:continue
                v=gcd(N,det);d=det//v;x=N//v
                Ns=[];K=[];l=[]
                for i in range(P):
                    Ns.append(x)
                    l.append(1<<(2-z[i]));K.append(l[-1]*x)
                    h=3*x+d
                    check((h&-h)==1<<es[i],'physical total exponent');x=h>>es[i]
                check(x==Ns[0],'exact physical return')
                if len(set(Ns))!=P:continue
                check(gcd(sum(es),P)==g,'genuine repeated rank')
                omega=pow(3,q,d)*pow(1<<a,-1,d)%d if d!=1 else 0
                order=next(k for k in range(1,g+1) if pow(omega,k,d)==1%d)
                check(order==g and g<=d,'denominator order')
                seen_g.add(g)
                stats['true_primitive_rational_cycles_with_multiple_rank_copies']+=1
                stats['cycles_with_a_nonbinary_valuation']+=max(es)>=3
                stats['cycles_with_grade_two']+=max(z)>=2
                for h in range(1,P):
                    t=h*s%q
                    if not t:
                        stats['resonant_excluded_lags']+=1
                        continue
                    w=[];G=[];delta=[]
                    for i,r in enumerate(rank[:-1]):
                        c=int(r+t>=q);j=(i+h)%P
                        w.append(z[j]-z[i]-c)
                        G.append((K[j]<<c)-K[i])
                        delta.append((l[j]<<c)-l[i])
                    check(sum(w)==-t*g,'full physical population mean including copies')
                    for i in range(P):
                        j=(i+1)%P
                        check(2**m[i]*G[j]==3*G[i]+d*delta[i],'signed dynamics')
                        check(es[(i+h)%P]-es[i]==w[i]-w[j],'mismatch equality')
                    stats['nonresonant_signed_rank_lags']+=1
                    stats['physical_signed_copy_interfaces']+=P
    return dict(stats,actual_clock_gcds=sorted(seen_g))


def branch_margins():
    M=F(5116201,10**6);g=F(29,20);L=F(21,10)
    point=F(1)+3*g/5
    check(point==F(187,100),'linear active widths below two')
    check(F(60,29)>2 and 3/M>F(1,2),'macroscopic margin')
    check((F(60,29)-2)/(F(60,29)-1)==F(2,31)>F(1,18),'microscopic margin')
    size=0
    for j in range(501):
        u=F(j,1000)
        c0=F(5,3)*(L-1-u);c1=F(5,3)*(L-2+u)
        check(c0+c1==2 and c0*c1/(c0+c1)<=F(1,2),'two central posts')
        for w in (-3,-2,1,2):
            width=max(F(0),L-abs(u+w));cost=min(g,F(5,3)*max(F(0),width-1))
            check(cost<=F(1,6),'peripheral charge')
            size+=1
    return {'macroscopic_surplus':str(3/M-F(1,2)),'microscopic_surplus':str(F(2,31)-F(1,18)),
            'exact_peripheral_samples':size}


if __name__=='__main__':
    print(json.dumps({'energy':max_energy(),'rational_ranks':actual_repeated_ranks(),
                      'budgets':branch_margins()},sort_keys=True,indent=2))
