"""Independent integer controls for fractional-part sources and clean-record translations."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import gcd
from random import Random
import json


def demand(ok, tag):
    if not ok:
        raise ArithmeticError(tag)


def parameters(word):
    K=B=0
    for e in word:
        B=3*B+(1<<K)
        K+=e
    return K,B


def orbit(word):
    P=len(word);A,B=parameters(word)
    D=(1<<A)-3**P
    if D<=0:
        return None
    k=gcd(B,D)
    d=D//k;x=B//k;first=x;N=[]
    for e in word:
        raw=3*x+d
        demand(gcd(x,d)==1 and raw&-raw==1<<e,'physical odd valuation')
        N.append(x);x=raw>>e
    demand(x==first,'closed actual rational cycle')
    return (d,N) if len(set(N))==P else None


def tests():
    rng=Random(234917)
    words={(1,2,3,1,4,3,1),(1,3),(2,), (3,), (15,)}
    for p, cap in ((3,3),(5,3),(7,2),(9,2),(11,2),(15,3),(19,4),(31,2),(47,3),(53,4)):
        for j in range(20):
            w=tuple(rng.randrange(1,cap+1) for i in range(p))
            words.add(min(w[i:]+w[:i] for i in range(p)))
    count=Counter();examples=[];all_fibres=0
    for w in sorted(words):
        o=orbit(w)
        if o is None:
            continue
        d,N=o;P=len(w)
        xs=defaultdict(set)
        for x in N:
            r=x%d;J=x//d
            demand(J not in xs[r],'same-residue localization injective')
            xs[r].add(J)
        all_fibres+=len(xs)
        if max(map(len,xs.values()))>1 and len(examples)<5:
            examples.append(dict(P=P,d=d,fibres=len(xs),max_fibre=max(map(len,xs.values()))))
        count['true_primitive_cycles']+=1
        for i in range(P):
            for b in sorted({1,2,5,P+2,2*P+1}):
                word=[w[(i+j)%P] for j in range(b)]
                t,B=parameters(word);nn=1<<t;th=3**b
                end=N[(i+b)%P];begin=N[i]
                demand(nn*end==th*begin+d*B,'physical affine identity')
                r=begin%d;end_r=end%d;J=begin//d;end_J=end//d
                u=-r*pow(d,-1,nn)%nn
                v=-end_r*pow(d,-1,th)%th
                demand(J%nn==(-B*pow(th,-1,nn)+u)%nn,'start J source')
                demand(end_J%th==(B*pow(nn,-1,th)+v)%th,'terminal J source')
                # The inhomogeneous offset in exact integer coordinates is integral.
                carry=th*r-nn*end_r
                demand(carry%d==0 and nn*end_J==th*J+B+carry//d,'integer fibre bridge')
                count['two_prime_power_windows']+=1
                count['winding_windows']+=int(b>P)
                count['start_J_zero']+=int(J==0)
                count['both_centres_nonzero']+=int(u!=0 and v!=0)
                for j in (0,b//3,b//2):
                    if j+1>=b or word[j]==word[j+1]:continue
                    patched=word.copy()
                    patched[j],patched[j+1]=patched[j+1],patched[j]
                    T,C=parameters(patched)
                    demand(T==t,'unchanged endpoints and modulus')
                    # Exactly one cumulative date changed. Its global signed
                    # low-place correction is placed before any source counting.
                    A=sum(word[:j])
                    expected=3**(b-j-2)*((1<<(A+word[j]))-(1<<(A+patched[j])))
                    demand(B-C==expected,'scalar correction for one changed date')
                    delta=-pow(th,-1,nn)*expected
                    demand(J%nn==(-pow(th,-1,nn)*C+u+delta)%nn,'actual translated repaired circle')
                    count['single_record_repairs']+=1
                    count['omitting_repair_changes_located_point']+=int(delta%nn!=0)
                    break
    return {'counts':dict(count),'populated_actual_fibres_total':all_fibres,'multiply_populated_actual_examples':examples}


def parity():
    counts=Counter()
    for d in (1,5,7,11,25,35,175,1009):
        for r in sorted({0 if d==1 else 1, (d-1)%d,(d//2)%d}):
            if gcd(d,r)>1:continue
            for n in (3,6,9):
                M=1<<n
                table={}
                for J in range(M):
                    x=d*J+r
                    parity_bits=0
                    for j in range(n):
                        parity_bits|=(x&1)<<j
                        x=((3*x+d) if x&1 else x)//2
                    demand(parity_bits not in table,'fixed-fibre parity permutation')
                    table[parity_bits]=J
                demand(len(table)==M,'all shortcut words represented once')
                counts['complete_fixed_fibre_parity_tables']+=1
                counts['parity_cylinders']+=M
    return dict(counts)


def margins():
    Q=Fraction
    settings=[
        ('global canonical',Q(3),Q(1,10**8),Q(2666577000221,8000002000000)),
        ('12/5',Q(5116201,10**6),Q(1,5000),Q(1827,9500)),
        ('5/2',Q(5116201,10**6),Q(1,10000),Q(349919,1800600)),
        ('3',Q(3),Q(1,100000),Q(123461,375125)),
        ('31/10',Q(3),Q(1,10**7),Q(9499713500517,28500009500000)),
        ('mixed',Q(3),Q(1,10**10),Q(6666505000263,20000005000000))]
    out={}
    for key,M,delta,C in settings:
        margin=1-delta-M*C
        demand(margin>0 and 25*delta<1,'fractional-part consumer margins')
        out[key]=str(margin)
    return out


if __name__=='__main__':
    print(json.dumps(dict(physical_source=tests(),parity=parity(),margins=margins()),sort_keys=True,indent=2))
