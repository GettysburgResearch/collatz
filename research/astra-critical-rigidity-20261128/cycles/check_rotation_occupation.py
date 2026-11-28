"""Exact odd-numerator controls for rotation occupation, including unequal final edges."""
from fractions import Fraction
from itertools import combinations, product
from math import factorial, gcd, prod
import json


def require(ok, msg):
    if not ok:
        raise ArithmeticError(msg)


def primitive_necklace(w):
    return all(w < w[k:]+w[:k] for k in range(1,len(w)))


def lifted(w):
    p = len(w)
    D = 2**sum(w)-3**p
    if D <= 0:
        return None
    E = 0
    C = 0
    for i,a in enumerate(w):
        C += (2**E)*3**(p-1-i)
        E += a
    g = gcd(D,C)
    q, seed = D//g,C//g
    y = []
    x = seed
    for a in w:
        require(x%2 and gcd(x,q)==1, "positive reduced odd numerator")
        y.append(x)
        x,remainder = divmod(3*x+q,2**a)
        require(remainder==0, "physical division")
    require(x==seed and len(set(y))==p, "primitive physical replay")
    return q,y


def blocks(bad,period):
    for j,last in enumerate(bad):
        prev = bad[j-1]
        L = (last-prev)%period or period
        yield (prev+1)%period,L


def block_check(w,y,q,starts,L,stats):
    p = len(w)
    exps = [[w[(t+k)%p] for t in starts] for k in range(L)]
    require(all(len(set(a))==1 for a in exps[:-1]), "common strict prefix")
    smallest = min(exps[-1])
    E = sum(a[0] for a in exps[:-1])+smallest
    v = [2**(e-smallest)*y[(t+L)%p] for t,e in zip(starts,exps[-1])]
    for j,k in combinations(range(len(starts)),2):
        # Two tracks may have the same last exponent above a third track's minimum.
        a,b=starts[j],starts[k]
        S=0
        g0=y[a]-y[b]
        correction=Fraction()
        for t in range(L):
            g=y[(a+t)%p]-y[(b+t)%p]
            lattice=3**t*2**(E-S)
            require(g and g%lattice==0 and abs(g)>=2**L, "complete mixed interior divisor")
            require(2**S*g==3**t*g0, "past at the same physical date")
            require(2**(E-S)*(v[j]-v[k])==3**(L-t)*g,
                    "future to actual possibly even intermediate states")
            correction += Fraction(q,3*max(y[(a+t)%p],y[(b+t)%p]))
            S += exps[t][0] if t+1<L else smallest
            stats["interior_lattices"] += 1
        require(correction <= Fraction(q,2**L)*(1-Fraction(2,3)**L),
                "high-track relative-error sum")
        stats["high_track_corrections"] += 1
        stats["unequal_final_pairs"] += exps[-1][j]!=exps[-1][k]
        stats["both_final_excesses_positive"] += min(exps[-1][j],exps[-1][k])>smallest


def case(w,stats):
    source=lifted(w)
    if source is None:
        return
    q,y=source
    p=len(w)
    P=prod(y)
    caps=sorted(set([0,1,q]+[y[i] for i in (0,p//2,p-1)]
                    +[2**(Y.bit_length()-1) for Y in (min(y),max(y))]))
    stats["primitive_rational_cycles"] += 1
    stats["proper_cancelled_denominators"] += 1<q<2**sum(w)-3**p
    for ell in range(1,p):
        bad=[i for i in range(p) if w[i]!=w[(i+ell)%p]]
        s=len(bad)
        d=gcd(ell,p)
        M=p//d
        changes=[r for r in range(d) if len({w[r+j*d] for j in range(M)})>1]
        K=len(changes)
        require(0<2*K<=s, "nonconstant residue-circle changes")
        for t,L in blocks(bad,p):
            block_check(w,y,q,[t,(t+ell)%p],L,stats)
        for t,L in blocks(changes,d):
            block_check(w,y,q,[(t+j*d)%p for j in range(M)],L,stats)
        require(P**(4*s) >= 2**(p*p+p*s)*3**(p*p-p*s), "geometric mean (8)")
        require(P**(2*K) >= factorial(M-1)**(2*K*d) *
                2**((M-1)*(d*d+d*K))*3**((M-1)*(d*d-d*K)), "geometric mean (7)")
        stats["geometric_mean_pairs"] += 1
        for cap in caps:
            T=max(0,cap.bit_length()-1)
            low=[x<=cap for x in y]
            D=sum(low)
            E=sum(low[i] and low[(i+ell)%p] for i in range(p))
            require(E<=s*T, "paired low dates (6)")
            require(D<=d+(M-1)*K*T, "complete-fiber occupation (2)")
            for J in range(2,M+1):
                require(6*J*D<=6*p+J*(J*J-1)*s*T, "all translate orders (1)")
                stats["translated_quantiles"] += 1


def main():
    stats={k:0 for k in ("primitive_rational_cycles","proper_cancelled_denominators",
                         "interior_lattices","high_track_corrections","unequal_final_pairs",
                         "both_final_excesses_positive","geometric_mean_pairs",
                         "translated_quantiles")}
    for p in range(2,7):
        for w in product((1,2,3),repeat=p):
            if primitive_necklace(w):
                case(w,stats)
    # Even intermediate targets, unequal extreme roofs, nearly repeated cells,
    # a very short final block and a wrapping long common block are all retained.
    for w in [(1,2,1,3,1,2,1,12),(2,1,3,2,1,3,2,1,29),
              (1,1,2,2,1,2,1,1,2,2,1,51),(1,2,1,3,2,61,1,3,1,2)]:
        require(len({w[i:]+w[:i] for i in range(len(w))})==len(w),"control necklace primitive")
        case(w,stats)
    require(all(stats.values()),"all advertised physical regimes covered")
    return stats


if __name__=="__main__":
    print(json.dumps(main(),indent=2,sort_keys=True))
