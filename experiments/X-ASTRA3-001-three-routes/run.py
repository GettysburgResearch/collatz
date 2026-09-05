#!/usr/bin/env python3
"""Exact, finite three-route certificates. No asymptotic inference is made.

Standard library only. Independent reconstruction is in verify.py.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

SCALE = 1 << 96
ZETA_CUTOFF = 1 << 16
MASS_CONFIG = ((1, 40), (64, 36))
ECHO_N = 256
ECHO_D = 128
CROSS_DEPTH = 21
CARRY_DEPTH = 6
MACRO_ODDS = 16384


def digest(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def T(n: int) -> int:
    return (3*n+1)//2 if n & 1 else n//2


def val(n: int, p: int = 2) -> int:
    if n == 0:
        raise ValueError("valuation of zero is not finite")
    n = abs(n)
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def floor_half_power(n: int, odd_exponent: int) -> int:
    """floor(SCALE * n**(-odd_exponent/2)), using integers only."""
    return math.isqrt((SCALE*SCALE)//(n**odd_exponent))


def ceildiv(a: int, b: int) -> int:
    return -(-a//b)


def base_mass_intervals() -> tuple[tuple[int,int],tuple[int,int]]:
    N, Q = ZETA_CUTOFF, SCALE
    root = math.isqrt(N)
    assert root*root == N
    S = sum(floor_half_power(n,3) for n in range(1,N+1))
    b = Fraction(2,root)-Fraction(1,2*N*root)
    error = Fraction(3,16*N*N*root)
    zlo = S + (Q*b.numerator)//b.denominator
    zhi = S+N+ceildiv(Q*(b+error).numerator,(b+error).denominator)
    Sp = sum(floor_half_power(n,3) for n in range(2,N+1,3))
    count = len(range(2,N+1,3))
    m = N+1
    while m%3 != 2:
        m += 1
    a,b0,c = (floor_half_power(m,k) for k in (1,3,5))
    # Sum_{j>=0}(m+3j)^(-3/2): integral + half endpoint + Peano remainder.
    plo = Sp + (4*a+3*b0)//6
    phi = Sp+count+ceildiv(4*(a+1)+3*(b0+1),6)+ceildiv(9*(c+1),16)
    return (zlo,zhi),(plo,phi)


def mass_rows(H: int, K: int, base: tuple) -> dict:
    (zl,zu),(pl,pu) = base
    seen = set(range(1,H+1))
    frontier = set(seen)
    hit_sum = sum(floor_half_power(n,3) for n in seen)
    eligible_min = (3*H+1)//2+1
    excluded = list(range(2,eligible_min,3))
    q_sum = sum(floor_half_power(n,3) for n in excluded)
    q_count = len(excluded)
    rows = []
    for k in range(K+1):
        ml,mh = zl-hit_sum-len(seen),zu-hit_sum
        ql,qh = pl-q_sum-q_count,pu-q_sum
        assert 0 < ml <= mh and 0 < ql <= qh
        rows.append({"k":k,"hit_count":len(seen),"new_hit_count":len(frontier),
                     "M_scaled":[ml,mh],"Q_scaled":[ql,qh]})
        if k == K:
            break
        nxt = set()
        for y in frontier:
            nxt.add(2*y)
            if y%3==2 and y>2:
                nxt.add((2*y-1)//3)
        frontier = nxt-seen
        seen.update(frontier)
        hit_sum += sum(floor_half_power(n,3) for n in frontier)
        elig = [n for n in frontier if n>=eligible_min and n%3==2]
        q_sum += sum(floor_half_power(n,3) for n in elig)
        q_count += len(elig)
    return {"H":H,"K":K,"eligible_min":next(n for n in range(eligible_min,eligible_min+3) if n%3==2),"rows":rows}


def echo_checks() -> dict:
    success=0
    transcript=hashlib.sha256()
    for n in range(1,ECHO_N+1):
        for d in range(1,ECHO_D+1):
            t=val(d)
            x,y=n,n+d
            P,Q,A=1,1,0
            for i in range(t):
                assert x%2 == y%2
                odd=x%2
                x,y=T(x),T(y)
                A=(3*A+P) if odd else A
                Q*=3 if odd else 1
                P*=2
            assert (x-y)%2
            assert y-x == Q*d//P
            z=T(y)
            predicted=(x+Q*d//P)//2 if x%2 else (3*(x+Q*d//P)+1)//2
            assert z == predicted
            flag=bool(x%2 and (2*P-Q)*n > Q*d+A)
            if x%2:
                assert flag == (z<n)
            success+=flag
            transcript.update(f"{n},{d},{t},{z},{int(flag)}\n".encode())
    return {"n_max":ECHO_N,"d_max":ECHO_D,"cases":ECHO_N*ECHO_D,
            "certified_descents":success,"sha256":transcript.hexdigest()}


def first_crossings() -> dict:
    # Stream every first coefficient-crossing word up to CROSS_DEPTH.
    levels={}
    examples=[]
    transcript=hashlib.sha256()
    def visit(bits:tuple[int,...],P:int,Q:int,A:int,prefix:tuple[tuple[int,int,int,int],...]):
        j=len(bits)
        if j and Q<P:
            cell=levels.setdefault(j,{"words":0,"positive_displacements":0,"echo_rejected":0,"integral_positive_displacements":0})
            cell['words']+=1
            D=P-Q
            for d in range(1,(A-1)//P+1):
                # Formal rational fixed-source pair, NOT an ordinary witness.
                rn=A-P*d
                assert rn>0
                t=val(d)
                assert t<j
                Pt,Qt,At,vt=prefix[t]
                reject=bool(vt and (2*Pt-Qt)*rn > D*(Qt*d+At))
                source=Fraction(rn,D)
                x=source
                for b in bits[:t]:
                    x=(3*x+1)/2 if b else x/2
                Ct=Fraction(Qt,Pt)
                z=(x+Ct*d)/2 if vt else (3*(x+Ct*d)+1)/2
                if vt:
                    assert reject == (z<source)
                # Integer numerator form of the shifted displacement threshold.
                if vt and Qt<2*Pt:
                    aa=(2*Pt-Qt)*A-D*At
                    bb=2*Pt*P-Q*Qt
                    assert bb>0
                    assert reject == (bb*d<aa)
                cell['positive_displacements']+=1
                cell['echo_rejected']+=reject
                cell['integral_positive_displacements']+=(rn%D==0)
                text=f"{''.join(map(str,bits))},{d},{rn},{D},{t},{int(reject)}\n"
                transcript.update(text.encode())
                if reject and len(examples)<8:
                    examples.append({"word":''.join(map(str,bits)),"d":d,
                                     "source":[source.numerator,source.denominator],
                                     "lookahead":t+1,"next":[z.numerator,z.denominator]})
            return
        if j==CROSS_DEPTH:
            return
        for v in (0,1):
            visit(bits+(v,),2*P,Q*(3 if v else 1),3*A+P if v else A,
                  prefix+((P,Q,A,v),))
    visit((),1,1,0,())
    return {"max_depth":CROSS_DEPTH,"levels":{str(k):v for k,v in sorted(levels.items())},
            "examples":examples,"sha256":transcript.hexdigest()}


DIGITS={'a':(2,0),'b':(2,1),'e':(3,0),'f':(3,1),'g':(3,2)}
RULES={'ae':'ea','af':'eb','ag':'fa','be':'fb','bf':'ga','bg':'gb'}


def value(word:str) -> int:
    c=0
    for ch in word:
        r,d=DIGITS[ch]
        c=r*c+d
    return c


def inversions(word:str) -> int:
    b=total=0
    for ch in word:
        if ch in 'ab':b+=1
        else:total+=b
    return total


def carry_checks() -> dict:
    total=swaps=0
    transcript=hashlib.sha256()
    for length in range(CARRY_DEPTH+1):
        for letters in itertools.product('abefg',repeat=length):
            w=''.join(letters); start=w; inv=inversions(w); steps=0
            while True:
                i=next((i for i in range(len(w)-1) if w[i:i+2] in RULES),None)
                if i is None:break
                nw=w[:i]+RULES[w[i:i+2]]+w[i+2:]
                assert value(nw)==value(w) and inversions(nw)==inversions(w)-1
                w=nw;steps+=1
            assert steps==inv
            total+=1;swaps+=steps
            transcript.update(f"{start}:{w}:{steps}\n".encode())
    return {"max_length":CARRY_DEPTH,"words":total,"swaps":swaps,"sha256":transcript.hexdigest()}


def macro_checks() -> dict:
    transcript=hashlib.sha256();longest=0
    for n in range(1,2*MACRO_ODDS,2):
        a=val(n+1);u=(n+1)//2**a;b=val(3**a*u-1)
        m=(3**a*u-1)//2**b
        x=n;steps=0
        while x%2:
            x=T(x);steps+=1
        while x%2==0:
            x=T(x);steps+=1
        assert x==m and steps==a+b
        longest=max(longest,steps)
        transcript.update(f"{n},{a},{u},{b},{m}\n".encode())
    return {"odd_sources":MACRO_ODDS,"max_source":2*MACRO_ODDS-1,
            "max_macro_steps":longest,"sha256":transcript.hexdigest()}


def rank_value(n:int,terms:list[tuple[int,Fraction,int]]) -> Fraction:
    # exp(R) for s=1 and integer valuation coefficients.
    result=Fraction(n)
    for p,alpha,c in terms:
        x=Fraction(n)-alpha
        v=val(x.numerator,p)-val(x.denominator,p)
        result*=Fraction(p)**(c*v)
    return result


def rank_witnesses() -> list[dict]:
    cases=[]
    examples=[('log',[], 'odd'),
              ('negative-dyadic-minus-one',[(2,Fraction(-1),-1)],'odd'),
              ('negative-dyadic-plus-one',[(2,Fraction(1),-1)],'odd'),
              ('positive-dyadic-minus-one',[(2,Fraction(-1),1)],'even2'),
              ('positive-ternary-minus-one',[(3,Fraction(-1),1)],'even3'),
              ('negative-ternary-minus-one',[(3,Fraction(-1),-1)],'even3inverse')]
    for name,terms,kind in examples:
        for ell in (1,2,4):
            if kind=='odd':
                L=24; b=6; x=2**L*b-1; endpoint=3**L*b-1
                assert rank_value(endpoint,terms)>rank_value(x,terms)
                found=None
                for i in range(0,L,ell):
                    y=x
                    for _ in range(ell):y=T(y)
                    if rank_value(y,terms)>rank_value(x,terms):found=(x,y);break
                    x=y
                assert found is not None
                x,y=found
            else:
                h=24
                if kind=='even2':target=2**h-1
                elif kind=='even3':target=3**h-1
                else:
                    target=(-pow(2**ell,-1,3**h))%(3**h)+3**h
                x=2**ell*target;y=target
            z=x
            for _ in range(ell):z=T(z)
            assert z==y and rank_value(y,terms)>rank_value(x,terms)
            cases.append({"candidate":name,"block":ell,"source":x,"endpoint":y,
                          "terms":[[p,a.numerator,a.denominator,c] for p,a,c in terms]})
    return cases



def macro_rank_witnesses() -> list[dict]:
    terms_by_name={
        'log':[],
        'negative-dyadic-minus-one':[(2,Fraction(-1),-1)],
        'negative-dyadic-plus-one':[(2,Fraction(1),-1)],
        'positive-dyadic-minus-one':[(2,Fraction(-1),1)],
        'positive-ternary-minus-one':[(3,Fraction(-1),1)],
        'negative-ternary-minus-one':[(3,Fraction(-1),-1)],
    }
    result=[]
    for name,terms in terms_by_name.items():
        if name=='positive-dyadic-minus-one':
            y=2**25-1;n=(4*y-1)//3
            assert 3*n==4*y-1
        elif name=='positive-ternary-minus-one':
            y=2*3**24-1;n=(8*y-1)//3
            assert 3*n==8*y-1
        elif name=='negative-ternary-minus-one':
            n=2*3**24-1
        else:n=3*2**25-1
        a=val(n+1);u=(n+1)//2**a;b=val(3**a*u-1);m=(3**a*u-1)//2**b
        assert n>1_000_000 and rank_value(m,terms)>rank_value(n,terms)
        result.append({'candidate':name,'source':n,'endpoint':m,'a':a,'b':b,
                       'terms':[[p,alpha.numerator,alpha.denominator,c] for p,alpha,c in terms]})
    return result


def generate() -> dict:
    base=base_mass_intervals()
    mass=[mass_rows(H,K,base) for H,K in MASS_CONFIG]
    h64=mass[1]
    assert all(200*r['Q_scaled'][1] <=69*r['M_scaled'][0] for r in h64['rows'])
    naive=next(r['k'] for r in h64['rows'] if 3*r['Q_scaled'][0]>r['M_scaled'][1])
    # Exact radicals sufficient for rho<0.993 at H=64,p=69/200.
    assert 8*177**2>500**2
    assert 463**2*65**3>250**2*98**3
    assert Fraction(177,500)+Fraction(69,200)*Fraction(463,250)<Fraction(993,1000)
    floor_times=[]
    for n in range(1,65):
        x=n;k=0
        while x!=1 and k<1000:x=T(x);k+=1
        assert x==1
        floor_times.append(k)
    # Rational enclosure of the critical ternary-bias constant; decimals only propose bounds.
    B=10**9
    a=int(B*2**(901/1000));b=int(B*3**(901/1000))
    assert a**1000 < 2**901*B**1000 < (a+1)**1000
    assert b**1000 < 3**901*B**1000 < (b+1)**1000
    kappa={"gamma":[901,1000],"scale":B,"two_power":[a,a+1],"three_power":[b,b+1],
           "bounds":[[a-B,b+1],[a+1-B,b]]}
    out={"schema":"astra-three-routes-v1","status":"FINITE_CERTIFICATE_NOT_COLLATZ_PROOF",
         "scope":{"all_positive_sources":True,"all_times":False,
                  "independent_mathematical_review":False},
         "scale":SCALE,"zeta_cutoff":ZETA_CUTOFF,"critical_bias":kappa,"base_mass_scaled":[list(b) for b in base],
         "mass":mass,"H64_naive_one_third_first_certified_failure":naive,
         "H64_69_over_200_checked_through":36,"floor64_max_hitting_time":max(floor_times),
         "echo":echo_checks(),"crossing_sieve":first_crossings(),
         "carry":carry_checks(),"macro":macro_checks(),"rank_witnesses":rank_witnesses(),"macro_rank_witnesses":macro_rank_witnesses()}
    return {"certificate":out,"sha256":digest(out)}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    report=generate()
    if args.check:
        old=json.loads(args.check.read_text())
        if report!=old:raise SystemExit('certificate differs from deterministic regeneration')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    print('PASS',report['sha256'])
    for data in report['certificate']['mass']:
        row=data['rows'][-1]
        print('H,K,count,M interval:',data['H'],data['K'],row['hit_count'],[float(Fraction(x,SCALE)) for x in row['M_scaled']])
    print('Crossing sieve:',report['certificate']['crossing_sieve']['levels'])

if __name__=='__main__':main()
