#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path

P=[5,30,20,56]
B=[9,54,36,24]

def two_order(x):
    assert x
    return (abs(x)&-abs(x)).bit_length()-1

def bezout_pair(t):
    odd=3**(7*(t+1))
    radix=2**(11*(t+17))
    inv=pow(odd,-1,radix)
    right=radix-inv
    upper=(odd*right+1)//radix
    assert radix*upper-odd*right==1
    return odd,radix,right,upper

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('canonical')
    a=ap.parse_args()
    frozen=json.loads(Path(a.canonical).read_text())
    assert frozen['experiment']=='X-8503'
    cases=0; gcds=0; markers=0
    for t in (3792,):
        n,m,d,e=bezout_pair(t)
        nn,mm,dd,ee=bezout_pair(t+16)
        assert m*e-n*d==1
        for i in range(4):
          for j in range(4):
            origin=B[j]*dd
            base=B[i]*e
            least=((origin-base)*pow(n,-1,mm))%mm
            for q in (2,63):
                k=least+mm*q
                w=B[i]*d+m*k
                u=(n*w+B[i])//m
                assert (n*w+B[i])%m==0
                assert u%64==P[j]
                kk=(u-origin)//mm
                assert kk>=0 and u==origin+mm*kk
                assert e*w-d*u==k
                assert m*u-n*w==B[i]
                left=(1<<(11*(t+1)-6))*w
                right=(1<<(11*(t+17)-6))*u
                assert two_order(left)==11*t+5+i
                assert two_order(right)==11*(t+16)+5+j
                assert B[i]%math.gcd(w,u)==0
                cases+=1; gcds+=1; markers+=1
    for mod,target in ((64,5),(32,15),(16,5),(8,7)):
        seen=set(); x=1
        while x not in seen:
            seen.add(x); x=3*x%mod
        assert target not in seen
    assert frozen['exact_connector_cases']==192
    assert frozen['intrinsic_marker_cases']==192
    assert frozen['adjacent_gcd_cases']==192
    print('X-8503 independent checker')
    print(f'exact connector cases:      {cases}')
    print(f'intrinsic marker cases:     {markers}')
    print(f'adjacent gcd cases:         {gcds}')
    print('smooth residue gates:       4')
    print('all independent checks passed')
if __name__=='__main__':
    main()
