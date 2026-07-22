#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from functools import lru_cache
from pathlib import Path

P=(5,30,20,56)
B=(9,54,36,24)
BETA=(2,3,2,1)

@lru_cache(None)
def basis(t):
    odd=3**(7*(t+1))
    radix=2**(11*(t+17))
    inv=pow(odd,-1,radix)
    right=radix-inv
    upper=(odd*right+1)//radix
    assert radix*upper-odd*right==1
    return odd,radix,right,upper

def ordp(x,p):
    a=0
    while x%p==0:
        x//=p; a+=1
    return a

def source_residue(t,i,j):
    n,m,d,e=basis(t)
    nn,mm,dd,ee=basis(t+16)
    return ((B[j]*dd-B[i]*e)*pow(n,-1,mm))%mm

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('canonical'); a=ap.parse_args()
    frozen=json.loads(Path(a.canonical).read_text())
    assert frozen['experiment']=='X-8504'
    t=3792
    n,m,d,e=basis(t)
    nn,mm,dd,ee=basis(t+16)
    n2,m2,d2,e2=basis(t+32)
    checked=0
    for i in range(4):
      for j in range(4):
        rho=source_residue(t,i,j)
        sigma=(B[i]*e+n*rho-B[j]*dd)//mm
        for ell in (0,3):
          rho2=source_residue(t+16,j,ell)
          lift=((rho2-sigma)*pow(n,-1,m2))%m2 + 2*m2
          k=rho+mm*lift
          kp=sigma+n*lift
          assert (kp-rho2)%m2==0
          U=B[i]*e+n*k
          V=B[j]*ee+nn*kp
          assert U==B[j]*dd+mm*kp
          assert (V-B[ell]*d2)%m2==0
          assert ordp(U,2)==j and ordp(V,2)==ell
          assert ordp(U,3)==BETA[i] and ordp(V,3)==BETA[j]
          CU=U//(2**j*3**BETA[i])
          CV=V//(2**ell*3**BETA[j])
          assert CU>1 and CV>1
          assert math.gcd(CU,6)==math.gcd(CV,6)==1
          assert math.gcd(CU,CV)==1
          checked+=1
    assert frozen['two_step_chains']==256
    assert frozen['coprime_core_checks']==256
    print('X-8504 independent checker')
    print(f'two-step chains:          {checked}')
    print(f'coprime core checks:      {checked}')
    print('all independent checks passed')
if __name__=='__main__': main()
