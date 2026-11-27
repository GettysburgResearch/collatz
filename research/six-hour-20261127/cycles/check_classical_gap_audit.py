"""Independent primal orientation and exact signed-word physical controls."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations,product
from math import gcd
from random import Random
import json


def require(value,message):
    if not value:
        raise ArithmeticError(message)


W=tuple(range(-3,3))
L=Q(121,50)


def solve(eq):
    m=len(eq)
    B=[list(map(Q,row)) for row in eq]
    for j in range(m):
        pivot=next((i for i in range(j,m) if B[i][j]),None)
        if pivot is None: return None
        B[pivot],B[j]=B[j],B[pivot]
        a=B[j][j];B[j]=[v/a for v in B[j]]
        for i in range(m):
            if i==j:continue
            a=B[i][j]
            B[i]=[v-a*u for v,u in zip(B[i],B[j])]
    return tuple(row[-1] for row in B)


def primal():
    result=[]
    for j in range(8):
        left,right=Q(j,16),Q(j+1,16)
        def g(w):
            D=max(Q(0),L-min(abs(w+left),abs(w+right)))
            if D>Q(99,50):return Q(6,5)
            return min(Q(1),Q(5,3)*max(Q(0),D-1))
        # Vertex dimensions permit <=3 positive probabilities. The mean slab
        # and orientation switch are the only potential interior equalities.
        best=Q(-1); total=0
        for k in (1,2,3):
            for support in combinations(W,k):
                a=[g(w)*int(w!=0) for w in support]
                b=[g(w)*int(w!=-1) for w in support]
                extra=[list(support)+[-left],list(support)+[-right],
                       [x-y for x,y in zip(a,b)]+[0]]
                for chosen in combinations(extra,k-1):
                    p=solve([[1]*k+[1],*chosen])
                    if p is None or min(p)<0:continue
                    u=-sum(x*w for x,w in zip(p,support))
                    if not left<=u<=right:continue
                    cost=min(sum(x*y for x,y in zip(p,a)),sum(x*y for x,y in zip(p,b)))
                    best=max(best,cost);total+=1
        require(0<=best<Q(23,40),'independent primal bound')
        result.append({'bin':j,'feasible_vertices_including_ties':total,'max_charge':str(best)})
    worst=max(Q(r['max_charge']) for r in result)
    M=Q(5116201,10**6)
    require(worst*M<3,'2018 Diophantine margin')
    return {'vertices':result,'worst_optimum':str(worst),'margin':str(3-M*worst)}


def physical_cycles():
    rng=Random(406);stats=Counter();profiles=set()
    for P in (5,7,11,13,17,19,23,29,31):
        A=next(n for n in range(P+1,2*P) if (1<<n)>3**P and gcd(n,P)==1)
        s=A-P
        rank=[(i*s)%P for i in range(P)]+[0]
        m=[1+int(r+s>=P) for r in rank[:-1]]
        caps=[1+int(Q(r,P)<=L-2) for r in rank]
        options=[{0}]
        for i in reversed(range(P)):
            options.append({a for a in range(caps[i]+1)
                            if any(m[i]+a-b in (1,2) for b in options[-1])})
        options.reverse()
        for _ in range(7):
            z=[0]
            for i in range(P):
                z.append(rng.choice(sorted(b for b in options[i+1] if m[i]+z[-1]-b in (1,2))))
            es=[m[i]+z[i]-z[i+1] for i in range(P)]
            val,h=0,0
            for e in es:
                val=3*val+(1<<h);h+=e
            det=(1<<h)-3**P; g=gcd(det,val); den=det//g; source=val//g
            require(den>0 and sum(es)==A and z[-1]==0,'positive physical cycle')
            x=[source]
            for e in es:
                v=3*x[-1]+den
                require((v & -v).bit_length()-1==e,'actual valuation')
                x.append(v>>e)
            require(x[-1]==source and len(set(x[:-1]))==P,'least positive cycle')
            K={r:(1<<(2-k))*y for r,k,y in zip(rank[:-1],z,x)}
            grade=dict(zip(rank[:-1],z))
            def lifted(r):
                return K[r%P] << (r//P)
            for t in range(1,P):
                u=Q(t,P)
                w={r:grade[(r+t)%P]-grade[r]-int(r+t>=P) for r in range(P)}
                G={r:lifted(r+t)-lifted(r) for r in range(P)}
                delta={r:((1<<int(r+t>=P))*(1<<(2-grade[(r+t)%P]))-(1<<(2-grade[r])))
                       for r in range(P)}
                require(sum(w.values())==-t,'exact mean gap profile')
                for i,r in enumerate(rank[:-1]):
                    y=(r+t)%P
                    opp=grade[(y+P-t)%P]-grade[y]-int(y+P-t>=P)
                    require(opp==-1-w[r],'pointwise opposite profile')
                    profiles.add(w[r])
                    require((1<<m[i])*G[rank[i+1]]==3*G[r]+den*delta[r],'physical signed difference')
                    require((Q(2)**(-w[r])-1)*(1<<(2-grade[r]))==delta[r],'true drift')
                    j=(i+t*pow(s,-1,P))%P
                    require(es[j]-es[i]==w[r]-w[rank[i+1]],'original mismatch')
                    stats['rank_pair_identities']+=1
                # Reconstruct each signed gap from its genuine whole-cycle word.
                running=0;M=0
                for i,r in enumerate(rank[:-1]):
                    running=3*running+(delta[r]<<M);M+=m[i]
                require((G[0]+den*running*pow(3**P,-1,1<<M))%(1<<M)==0,'signed source residue')
                stats['signed_cycle_source_residues']+=1
            stats['positive_primitive_physical_cycles']+=1
    return dict(stats,observed_profiles=sorted(profiles))


def word_tests():
    stats=Counter()
    alpha=Q(31,53);n=6
    for u in (Q(1,29),Q(2,13),Q(1,3),Q(1,2),Q(17,29)):
        for w in W:
            bottom=max(Q(0),-u-w);top=min(L,L-u-w)
            if bottom>top:continue
            for start in (Q(0),Q(1,25),Q(11,19),Q(4,5),bottom%1,top%1):
                phase=[(start+i*alpha)%1 for i in range(n+1)]
                M=[i+(start+i*alpha)//1 for i in range(n+1)]
                M0=(start-bottom)//1
                Mp=[i+(start+i*alpha-bottom)//1-M0 for i in range(n+1)]
                zp=[int((f-bottom)//1) for f in phase]
                grades=[[z for z in range(3) if bottom<=f+z<=top]
                        for f in phase]
                words=set()
                for z in product(*grades):
                    r=[v+h for v,h in zip(z,zp)]
                    e=[M[i+1]-M[i]+z[i]-z[i+1] for i in range(n)]
                    if any(k not in (1,2) for k in e): continue
                    if any(M[i]-z[i]!=Mp[i]-r[i]+M0 for i in range(n+1)):
                        raise ValueError('recentered chart')
                    ds=tuple((Q(2)**(-w)-1)*(1<<(2-k)) for k in z[:-1])
                    if any(x.denominator!=1 for x in ds):continue
                    ds=tuple(map(int,ds));words.add(ds)
                    D=sum(3**(n-1-i)*2**M[i]*ds[i] for i in range(n))
                    v=sum(3**(n-1-i)*2**Mp[i]*Q(2)**(2-r[i]) for i in range(n))
                    require(D==(Q(2)**(-w)-1)*Q(2)**M0*v,'ordinary rescaled signed sum')
                    stats['exact_grade_paths']+=1
                if not words: continue
                if w==0:require(len(words)==1,'zero word multiplicity')
                polys=[]
                for ds in words:
                    polys.append(sum(3**(n-1-i)*2**M[i]*ds[i] for i in range(n)))
                pair=Counter(x+y for x,y in product(polys,repeat=2))
                diff=Counter()
                for x,nx in pair.items():
                    for y,ny in pair.items():diff[x-y]+=nx*ny
                modulus=1<<M[-1]
                atoms=Counter()
                for z,c in diff.items():atoms[z%modulus]+=c
                require(diff[0]==max(diff.values()) and atoms[0]==max(atoms.values()),'shifted atoms')
                require(atoms[0]<=sum(z%modulus==0 for z in diff)*diff[0],'modular to ordinary')
                for incoming in range(-9,10):
                    avg=atoms[(-3**n*incoming)%modulus]
                    require(avg<=atoms[0],'arbitrary signed initial carry')
                    stats['signed_carry_targets']+=1
                stats['nonempty_pointed_languages']+=1
                stats['actual_distinct_drifts']+=len(words)
    return dict(stats)


if __name__=='__main__':
    print(json.dumps({'orientation_primal':primal(),'physical_cycles':physical_cycles(),
                      'signed_words':word_tests()},sort_keys=True,indent=2))
