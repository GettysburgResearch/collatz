#!/usr/bin/env python3
"""Independent direct ordinary source, inverse affine and integer shell controls."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb,gcd
import json


def shortcut(x):
    return (3*x+1)//2 if x%2 else x//2


def oddstep(x):
    v=3*x+1
    e=(v&-v).bit_length()-1
    return v>>e,e


def shadow():
    totals=Counter()
    largest_gcd=0
    for n in range(1,16):
        modulus=2**n
        for v in range(1,modulus,2):
            x,q,seen_word=v,0,[]
            for j in range(1,n+1):
                b=x%2
                q+=b
                if 3**q<=2**j:
                    break
                seen_word.append(b)
                x=shortcut(x)
            else:
                k=1+(3**q).bit_length()-n
                N=n+k
                intercept=modulus*x-3**q*v
                D=2**N-3**q
                scale=gcd(D,intercept)
                numerator,denominator=intercept//scale,D//scale
                assert gcd(denominator,6)==1
                assert 9*numerator>denominator and 3**q*numerator<=intercept*denominator
                closed=seen_word+[0]*k
                h=numerator
                for b in closed:
                    assert h%2==b
                    h=(3*h+denominator)//2 if b else h//2
                    assert h>0 and gcd(h,denominator)==1
                assert h==numerator
                if N<=2*n:
                    assert all(any(closed[i]!=closed[i%p] for i in range(p,N))
                               for p in range(1,N) if N%p==0)
                    totals["primitive_seam_tests"]+=1
                for lift in (v,v+modulus,v+5*modulus):
                    terminal=x+(lift-v)//modulus*3**q
                    assert gcd(D,terminal-2**k*lift)==scale
                    assert (numerator-denominator*lift)%modulus==0
                    totals["gcd_lifts"]+=1
                totals["prefixes"]+=1
                totals["reduced"]+=scale>1
                largest_gcd=max(largest_gcd,scale)
    return dict(totals,largest_gcd=largest_gcd)


def pressure():
    counts=Counter()
    layers=[]
    for n in range(1,7):
        mass=[Fraction(0) for _ in range(5)]
        for word in product(range(1,6),repeat=n):
            A=0
            offset=0
            for e in word:
                offset=3*offset+2**A
                A+=e
            m=((2**A-offset)*pow(3**n,-1,2**(A+1)))%2**(A+1)
            x, true, bottom=m,[],m
            path=[]
            for e in word:
                path.append(x)
                x,h=oddstep(x)
                true.append(h)
                bottom=min(x,bottom)
            y=x
            assert tuple(true)==word and m%2 and 0<m<2**(A+1) and y<2*3**n
            G=Fraction(offset,3**n)
            zp=Fraction(2**A,m+G)
            z0=Fraction(2**A,m)
            assert zp==Fraction(3**n,y)
            W=Fraction(1,2**A)
            for i,h in enumerate(path+[y]):
                assert z0>=Fraction(3**i*2**(n-i),h)
            assert z0<=4**n and zp>Fraction(1,2)
            for H,j in ((1,1),(7,2),(35,3)):
                if bottom<=H:
                    mass[j]+=W
                else:
                    assert z0 <= Fraction(3**n,H)*(1+Fraction(1,3*H))**n
                    counts["moving_floor_upper_tests"]+=1
            mass[0]+=W*z0
            mass[4]+=W*zp
            counts["physical_words"]+=1
        assert mass[0]<=n+1
        for H,j in ((1,1),(7,2),(35,3)):
            assert mass[j] <= Fraction(H*(n+1),2**n)
        layers.append([n]+[10**9*m//1 for m in mass])
    return dict(counts,layers_floored_billionths=layers)


def shell():
    totals=Counter()
    for a in (Fraction(3,2),Fraction(7,4),Fraction(15,8)):
        for n in range(1,10):
            cap=(a*n)//1
            by_shell=Counter()
            for m in range(1,2**(cap+1),2):
                x,A=m,0
                for i in range(1,n+1):
                    x,e=oddstep(x)
                    A+=e
                    if A>a*i:
                        break
                else:
                    if m>=2**(A+1):
                        continue
                    k=m.bit_length()-1
                    h,zeros=m,0
                    for _ in range(k):
                        zeros+=h%2==0
                        h=shortcut(h)
                    bound=min(((a-1)*k/a)//1,A-n)
                    assert zeros<=bound
                    by_shell[A,k]+=1
                    totals["principal_words"]+=1
            for (A,k),count in by_shell.items():
                h=min(((a-1)*k/a)//1,A-n)
                assert count<=sum(comb(k,j) for j in range(h+1))
                totals["nonempty_total_shell_pairs"]+=1
                totals["total_zero_constraint_strict"]+=(A-n)<((a-1)*k/a)//1
    return dict(totals)


if __name__=="__main__":
    print(json.dumps({"compact":shadow(),"pressure":pressure(),"joint":shell()},indent=2,sort_keys=True))
