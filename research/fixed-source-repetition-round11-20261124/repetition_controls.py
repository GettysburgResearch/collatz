"""Exact controls for the round-11 fixed-source repetition argument.
Finite arithmetic checks only; not a universal Collatz proof.
"""
from itertools import product
from fractions import Fraction
import json

L = (2, 1)
P = (1, 4)
W = (1,)*6 + (2,)*5 + (3,)
V = (1,)*7 + (5,) + (2,)*3 + (3,)


def need(ok, msg):
    if not ok:
        raise ArithmeticError(msg)


def affine(gaps):
    d, a, c = 1, 1, 0
    for g in gaps:
        c = 3*c+d
        a *= 3
        d <<= g
    return d, a, c


def charge(gaps):
    return sum((Fraction(g, 3**(i+1)) for i,g in enumerate(gaps)), Fraction(0))


def realize(gaps, b=1, negative=False):
    d,a,c=affine(gaps)
    x=((d-b*c)*pow(a,-1,2*d))%(2*d)
    if negative:
        x-=2*d
    return x


def step(a,b,g):
    z=3*a+b
    need(z%(1<<g)==0 and (z>>g)%2==1, 'literal exact valuation')
    return z>>g


def replay(script, words, a, b=1):
    out=[a]
    for bit in script:
        for g in words[bit]:
            a=step(a,b,g)
        out.append(a)
    return out


def cap(k,n):
    return int(n>0 and n.bit_count()<=k)


def next_pow2(x):
    return 1 << (x-1).bit_length()


def check():
    need(affine(L)==(8,9,7) and affine(P)==(32,9,5), 'LP maps')
    need(affine(W)==(524288,531441,700273) and affine(V)==(2097152,531441,1227505), 'WV maps')
    need(charge(L)==charge(P)==Fraction(7,9), 'LP charge')
    need(charge(W)==charge(V), 'WV charge')
    need(charge(W)/(1-Fraction(1,3**len(W)))==Fraction(729,1456), 'WV scalar')
    need(9**17 < 8**18 and 9**18 > 8**19, 'LP threshold')
    need(531441**971 < 524288**972 and 531441**972 > 524288**973, 'WV threshold')
    num_paths=num_edges=num_repeats=0
    for words, shift, limit in [((L,P),7,8),((W,V),98,5)]:
        d,a,_=affine(words[0]); lam=Fraction(a,d); amin=sum(words[0])
        for n in range(1,limit+1):
            for script in product((0,1),repeat=n):
                gaps=tuple(g for bit in script for g in words[bit])
                for b in (1,3,5):
                    for neg in (False,True):
                        src=realize(gaps,b,neg)
                        out=replay(script,words,src,b)
                        num_paths+=1
                        for x,y in zip(out,out[1:]):
                            need(d*(abs(y)+shift*b)<=a*(abs(x)+shift*b), 'height')
                            num_edges+=1
                        for m in range(1,n+1):
                            for i in range(n-m+1):
                                for j in range(i+1,n-m+1):
                                    if script[i:i+m]!=script[j:j+m]: continue
                                    g=tuple(v for bit in script[i:i+m] for v in words[bit])
                                    D,A,_=affine(g)
                                    diff=out[j]-out[i]
                                    need(D*(out[j+m]-out[i+m])==A*diff,'aligned carry')
                                    need(diff%(2*D)==0,'terminal odd divisor')
                                    if diff:
                                        need(abs(diff)>=2**(amin*m+1),'separation')
                                        need((1<<(amin*m))*d**j <= (abs(src)+shift*b)*a**j,'same-source bound')
                                    num_repeats+=1
    caps=0; cap_symbols=0; cap_replays=0
    for k in range(1,13):
        h=next_pow2(max(2**(k-1),8)); u=2**(k-1)-1
        script=[cap(k,n) for n in range(4*h)]
        need(script[h:2*h]==script[2*h:3*h], 'equal windows')
        need(script[2*h+u]==1 and script[3*h+u]==0, 'explicit mismatch')
        cap_symbols+=4*h; caps+=1
        gaps=tuple(g for bit in script for g in (L,P)[bit])
        for b in (1,5):
            for neg in (False,True):
                src=realize(gaps,b,neg); out=replay(script,(L,P),src,b)
                need(out[h]!=out[2*h], 'mismatching tails cannot share state')
                need((out[h]-out[2*h])%(2*8**h)==0,'large binary divisor')
                need(abs(src)+7*b>=4**h,'finite height obstruction')
                cap_replays+=1
    fixed_source_tests=0
    for q in range(1,258,2):
        for k in range(1,13):
            B=(q+7).bit_length(); h=next_pow2(max((B+1)//2,2**(k-1)))
            a=q; mismatch=False
            for n in range(4*h):
                for g in (L,P)[cap(k,n)]:
                    z=3*a+1
                    if z%(1<<g)!=0 or (z>>g)%2!=1:
                        mismatch=True; break
                    a=z>>g
                if mismatch: break
            need(mismatch,'fixed source finite budget')
            fixed_source_tests+=1
    # General near-critical construction with a=floor(p log_2 3), computed exactly.
    construction_tests=0
    for p in range(2,101):
        A=(3**p).bit_length()-1
        n2=A-p
        need(0<n2<p,'both binary gaps')
        w=(2,1)+(2,)*(n2-1)+(1,)*(p-n2-1)
        v=(1,4)+w[2:]
        need(len(w)==len(v)==p and sum(w)==A and sum(v)==A+2,'clock construction')
        need(charge(w)==charge(v),'common scalar')
        need(2**A < 3**p < 2**(A+1),'expanding slope below two')
        need((3**p)**p < 2**(A*(p+1)), 'automatic threshold at p')
        construction_tests+=1
    return dict(scope='finite exact arithmetic only',paths=num_paths,edges=num_edges,repeated_windows=num_repeats,bit_caps=caps,cap_symbols=cap_symbols,cap_replays=cap_replays,fixed_source_tests=fixed_source_tests,near_critical_constructions=construction_tests)

if __name__=='__main__':
    print(json.dumps(check(),sort_keys=True))
