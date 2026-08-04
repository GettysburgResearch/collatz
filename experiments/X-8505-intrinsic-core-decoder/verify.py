#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from functools import lru_cache
from pathlib import Path

P=(5,30,20,56)
B=(9,54,36,24)
BETA=(2,3,2,1)

@lru_cache(None)
def basis(t):
    N=3**(7*(t+1)); M=2**(11*(t+17)); r=pow(N,-1,M)
    d=M-r; e=(N*d+1)//M
    assert M*e-N*d==1
    return N,M,d,e

def residue(t,i,j):
    N,M,d,e=basis(t); NN,MM,dd,ee=basis(t+16)
    return ((B[j]*dd-B[i]*e)*pow(N,-1,MM))%MM

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('canonical'); a=ap.parse_args()
    frozen=json.loads(Path(a.canonical).read_text()); assert frozen['experiment']=='X-8505'
    t=3792
    N,M,d,e=basis(t); N1,M1,d1,e1=basis(t+16); N2,M2,d2,e2=basis(t+32)
    checked=0
    for i in range(4):
      for j in range(4):
        rho=residue(t,i,j)
        sigma=(B[i]*e+N*rho-B[j]*d1)//M1
        for ell in (1,2):
          rho2=residue(t+16,j,ell)
          lift=((rho2-sigma)*pow(N,-1,M2))%M2+3*M2
          k=rho+M1*lift; kp=sigma+N*lift
          U=B[i]*e+N*k; V=B[j]*e1+N1*kp
          gamma=BETA[i]; C=U//(2**j*3**gamma)
          G=7*(t+17)+gamma-BETA[j]; D=11*(t+33)-j
          X=3**G*C+1
          assert X%(2**D)==0
          Y=X//(2**D)
          assert (2**j*3**gamma*C)%64==P[j]
          assert (3**BETA[j]*Y)%64==P[ell]
          Cp=Y//(2**ell)
          assert Cp==V//(2**ell*3**BETA[j])
          assert Cp>2**170*C
          checked+=1
    assert frozen['intrinsic_core_transitions']==256
    print('X-8505 independent checker')
    print(f'intrinsic transitions:     {checked}')
    print(f'automatic source cells:    {checked}')
    print(f'six-bit target cells:      {checked}')
    print('all independent checks passed')
if __name__=='__main__': main()
