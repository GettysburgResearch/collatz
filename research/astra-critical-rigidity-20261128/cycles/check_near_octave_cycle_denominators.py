"""Complete rational closures, chronological annihilator ranks, and true multi-lap codes."""

import hashlib
import json
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement, product
from math import gcd
from pathlib import Path

from sympy import Poly, Symbol, factorint, totient

from check_native_return_curvature import binary_floor, require, two_power


def primitive(word):
    p=len(word)
    return min(word[i:]+word[:i] for i in range(p))==word and all(
        word[i:]+word[:i]!=word for i in range(1,p))


def orbit(word):
    p=len(word)
    grade,carry=0,0
    for a in word:
        carry=3*carry+(1<<grade)
        grade+=a
    x=Fraction(carry,(1<<grade)-3**p)
    q=x.denominator
    ys,grades=[x.numerator],[0]
    for a in word:
        v=3*ys[-1]+q
        require((v & -v)==1<<a, 'true exact exponents of the unmodified rational map')
        ys.append(v>>a)
        grades.append(grades[-1]+a)
    require(ys[-1]==ys[0] and gcd(q,6)==1 and all(gcd(y,q)==1 and y%2 for y in ys),
            'closed orbit and full reduced odd denominator')
    require(len(set(ys[:-1]))==p,'primitive odd states')
    return q,ys[:-1],grades[:-1]


@lru_cache(None)
def factors(p,A):
    x=Symbol('x')
    pieces=Poly(x**p-2**A,x).factor_list()[1]
    require(all(m==1 for _,m in pieces),'separable chronological binomial')
    return tuple(tuple(map(int,v.all_coeffs())) for v,_ in pieces)


def remainder(poly, divisor):
    # Descending coefficients, with monic divisor.
    temp=list(poly)
    for k in range(len(temp)-len(divisor)+1):
        z=temp[k]
        for j,b in enumerate(divisor):
            temp[k+j]-=z*b
    return temp[len(temp)-len(divisor)+1:]


def enumerate_ranks():
    counts=Counter()
    examples={}
    for p in range(2,10):
        for word in product((1,2,3),repeat=p):
            if (1<<sum(word))<=3**p or not primitive(word):
                continue
            q,ys,E=orbit(word)
            A=sum(word);g=gcd(A,p);P=p//g
            # sum V_i X^(p−1−i) is zero at the inactive roots of X^p−2^A.
            # The common numerator denominator q is immaterial to this exact gcd.
            v=[y<<e for y,e in zip(ys,E)]
            fs=factors(p,A)
            degree=sum(len(f)-1 for f in fs if any(remainder(v,f)))
            require(P<=degree<=p,'reduced clock degree lower bound')
            if g==1:
                require(degree==p,'all modes retained on the coprime clock')
            for prime,a in factorint(g).items():
                require(2*degree>=P*int(totient(prime**a)),'abelian active-character degree')
            if g>1 and len(factorint(g))==1:
                require(4*degree>=p,'prime-power sheet consequence')
            key='full' if degree==p else 'proper'
            counts[key]+=1
            counts['gcd_'+str(g)]+=1
            if key=='proper' and len(examples)<6:
                examples[str((p,A,degree))]={'word':list(word),'complete_q':q,'P':P}
    require(counts['proper']>0 and counts['gcd_6']>0,'nontrivial lost modes and mixed prime sheets')
    return {'counts':dict(sorted(counts.items())),'proper_rank_examples':examples}


def native_code(p,A):
    word=tuple((i+1)*A//p-i*A//p for i in range(p))
    q,ys,E=orbit(word)
    m=min(ys)
    require(max(ys)<Fraction(21,10)*m, 'actual near-octave rational cycle')
    U=[1<<e for e in E];V=[y*u for y,u in zip(ys,U)]
    def lifted(arr,i):
        laps,r=divmod(i,p)
        return two_power(laps*A)*arr[r]
    # Include actual spatially close phases from several distinct chronological offsets.
    # Homogeneous powers below record 3^s folded at the genuine degree-one dyadic chart.
    candidates=[]
    for s in range(p//2):
        k=binary_floor(Fraction(3**s))
        if Fraction(3**s,1<<k)<Fraction(109,100):
            candidates.append((s,k))
    cols=candidates[:7]
    require(len(cols)>=3 and len(cols)==len(set(s for s,_ in cols)),'nontrivial actual offsets')
    alltags=[]; labels=[]
    for i in range(p):
        f=binary_floor(Fraction(2*V[i],3*m))
        tags=[two_power(-f-k)*lifted(U,i+s) for s,k in cols]
        require(set(tags)<={1,2},'actual synchronized complete-denominator binary chart')
        alltags.append(tuple(int(t-1) for t in tags))
        values=[two_power(-f-k)*lifted(V,i+s) for s,k in cols]
        require(all(v.denominator==1 for v in values),'scaled physical numerator integral')
        labels.append(tuple(map(int,values)))
    variable=[i for i in range(p) if len(set(alltags[i]))>1]
    require(variable,'code has a genuine variable row')
    gaps=[(b-a)%p or p for a,b in zip(variable,variable[1:]+variable[:1])]
    L=min(gaps)
    h=min(5,3**L-1)
    require(h>=2,'guard admits the tested order')
    tuples=list(combinations_with_replacement(range(len(cols)),h))
    for row in labels:
        require(len({sum(row[i] for i in entry) for entry in tuples})==len(tuples),
                'all actual h sums are multiset-injective at EVERY true base')
    n=3*p+7
    f0=binary_floor(Fraction(2*V[0],3*m))
    fn=binary_floor(Fraction(2*lifted(V,n),3*m))
    require(1<<(fn-f0)>4*h*max(ys),'true coded cutoff across multiple laps')
    encoded=[sum(alltags[t%p][i]*(h+1)**t for t in range(n))
             for i in range(len(cols))]
    require(len({sum(encoded[i] for i in entry) for entry in tuples})==len(tuples),
            'coordinatewise sum decoder with no base-(h+1) carries')
    return {'odd_period':p,'A':A,'complete_q_bits':q.bit_length(),
            'true_offsets':[s for s,_ in cols],'tested_h':h,'anchor_multisets_per_date':len(tuples),
            'active_rows_per_lap':len(variable),'shortest_actual_gap':L,
            'coding_edges':n,'real_minimum_approx':round(m/q,4),
            'real_width_approx':round(max(ys)/m,7)}


if __name__=='__main__':
    src=Path(__file__).with_name('NEAR_OCTAVE_CYCLE_DENOMINATORS.md')
    result={'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
            'genuine_annihilator_ranks':enumerate_ranks(),
            'actual_lap_codes':[native_code(41,65),native_code(306,485)]}
    print(json.dumps(result,sort_keys=True,indent=2))
