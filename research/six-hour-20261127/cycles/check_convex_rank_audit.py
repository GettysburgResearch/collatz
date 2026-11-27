"""Independent exact local and physical controls for strict convex scaled ranks."""
from collections import Counter
from itertools import product
from math import gcd
from random import Random
import json


def require(v,label):
    if not v:raise ArithmeticError(label)


def low(a):
    return a & -a


def signs():
    regular={a-2*b+c for a,b,c in product((1,2),repeat=3)}
    early={a-2*b+4 for a,b in product((1,2),repeat=2)}
    late={a-8+2*b for a,b in product((1,2),repeat=2)}
    exits=set(); count=0
    for name,model in [('regular',regular),('P-2',early),('P-1',late)]:
        for H,t,m in product(range(-25,26),model,(1,2) if name=='regular' else (2,)):
            if (3*H+t)%2**m:continue
            new=(3*H+t)//2**m
            require(H*new>=0,'no direct reversal')
            if H and new==0:exits.add((name,H,t))
            count+=1
    require(exits=={('P-1',1,-3),('P-2',-1,3)},'only sign exits')
    # Check actual seam values on colliding neighboring representatives before
    # reducing any indices, including the doubled rank-zero and rank-one terms.
    vals=[x for x in range(1,41) if low(x)<=2];evens=[x for x in vals if low(x)==2]
    charts=0
    for x,y in product(vals,repeat=2):
        for zero,one in product(evens,vals):
            cluster=[x,y,2*zero,2*one]
            ls=[low(x),low(y),2*low(zero),2*low(one)]
            for k in (0,1):
                H=cluster[k+2]-2*cluster[k+1]+cluster[k]
                d=ls[k+2]-2*ls[k+1]+ls[k]
                out=[3*a+b for a,b in zip(cluster[k:k+3],ls[k:k+3])]
                require(3*H+d==out[-1]-2*out[1]+out[0],'true three-term raw chart')
                if all(v%4==0 for v in out):
                    new=(out[-1]-2*out[1]+out[0])//4
                    require(H*new>=0,'true two-seam sign')
                    charts+=1
    return dict(signed_integral_interfaces=count,admitted_true_seam_triples=charts,
                possible_nonzero_to_zero=sorted(exits))


def progressions():
    stats=Counter();cases=0
    for length in (3,4):
        for x,g in product(range(1,193),range(1,97)):
            values=tuple(x+j*g for j in range(length))
            if max(map(low,values))>2:continue
            ls=list(map(low,values))
            if g%2:
                require(length==3 and ls==[1,2,1],'only surviving odd progression')
                raw=[3*z+l for z,l in zip(values,ls)]
                require(raw[2]-2*raw[1]+raw[0]==-2,'forbidden negative curvature')
                stats['odd_triple_obstructions']+=1
            else:
                require(len(set(ls))==1,'even-spacing common lowbit')
            for m in (1,2):
                raw=[3*z+low(z) for z in values]
                if any(y%(1<<m) for y in raw):continue
                yy=[v>>m for v in raw]
                h=yy[2]-2*yy[1]+yy[0]
                if g%2:require(h<0,'actual excluded AP3 image')
                else:
                    require(h==0 and all((b-a)*2**m==3*g for a,b in zip(yy,yy[1:])),
                            'exact common-denominator AP transfer')
                    stats['exact_even_AP_transfers']+=1
            cases+=1
    stats['AP3_AP4_lowbit_configurations']=cases
    return dict(stats)


def rational_orbits():
    rng=Random(29991);stats=Counter()
    for P in (11,13,17,19,23,29,31,37,41):
        A=(3**P).bit_length()
        require(gcd(A,P)==1,'primitive rational clock')
        s=A-P
        rank=[(i*s)%P for i in range(P+1)]
        m=[1+int(r+s>=P) for r in rank[:-1]]
        for run in range(35):
            z=[0]
            for i in range(P-1):
                if z[-1]==0 and m[i]==1:z.append(0)
                else:z.append(rng.randrange(2))
            z.append(0)
            es=[m[i]+z[i]-z[i+1] for i in range(P)]
            require(min(es)>0,'true positive valuation')
            N=0;h=0
            for e in es:
                N=3*N+(1<<h);h+=e
            D=(1<<A)-3**P;g=gcd(N,D);den=D//g;x=N//g
            first=x;L={};ell={}
            for i,r in enumerate(rank[:-1]):
                ell[r]=2-z[i];L[r]=ell[r]*x
                a=3*x+den
                require(low(a)==1<<es[i],'true positive rational recurrence')
                x=a>>es[i]
            require(x==first and ell[0]==2,'complete physical orbit')
            def at(a,i):return a[i%P]<<(i//P)
            for r in range(P):
                rr=(r+s)%P
                mm=1+int(r+s>=P)
                for coeffs in ((-1,1),(1,-2,1)):
                    def op(a,j):return sum(v*at(a,j+k) for k,v in enumerate(coeffs))
                    require((1<<mm)*op(L,rr)==3*op(L,r)+den*op(ell,r),'both exact extended differences')
                    if r+len(coeffs)-1>=P:stats['physical_wrapped_charts']+=1
                    stats['physical_rank_difference_identities']+=1
            stats['true_rational_cycles']+=1
            stats['cycles_with_valuation_three']+=3 in es
    return dict(stats)


def seam_free_examples():
    stats=[]
    for P in (10007,30011,100003,200017,400009):
        A=(3**P).bit_length();s=A-P
        if gcd(A,P)!=1:continue
        T=10*(P+2).bit_length()+2
        distances=[min((s*j)%P,(-s*j)%P) for j in range(1,T+2)]
        require(min(distances)>4,'sample BLS-scale seam exclusion')
        for j in range(1,T+1):
            base=(j*s)%P
            nxt=((j+1)*s)%P
            cluster=range(base-2,base+2)
            ms={1+int(r+s>=P) for r in cluster}
            require(len(ms)==1 and {(r+s)%P for r in cluster}==set(range(nxt-2,nxt+2)),
                    'all four labels share the divisor including at a full wrap')
        stats.append({'P':P,'A':A,'horizon':T,'min_seam_distance':min(distances)})
    return stats


if __name__=='__main__':
    print(json.dumps(dict(signs=signs(),progressions=progressions(),
                          physical=rational_orbits(),seam_free_samples=seam_free_examples()),
                     sort_keys=True,indent=2))
