#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from functools import lru_cache
from pathlib import Path

P=(5,30,20,56)
B=(9,54,36,24)
BETA=(2,3,2,1)

@lru_cache(None)
def data(t:int):
    N=pow(3,7*(t+1))
    M=1<<(11*(t+17))
    r=pow(N,-1,M)
    c=(N*r-1)//M
    return N,M,r,c,M-r,N-c

def v2(x:int)->int:
    return (abs(x)&-abs(x)).bit_length()-1

def v3(x:int)->int:
    a=0
    while x%3==0:
        x//=3; a+=1
    return a

def rho_sigma(t:int,i:int,j:int):
    N,M,r,c,d,e=data(t)
    N1,M1,r1,c1,d1,e1=data(t+16)
    rho=((B[j]*d1-B[i]*e)*pow(N,-1,M1))%M1
    sigma=(B[i]*e+N*rho-B[j]*d1)//M1
    return rho,sigma

def add_int(h,x:int):
    sign=b'-' if x<0 else b'+'
    y=abs(x)
    raw=y.to_bytes(max(1,(y.bit_length()+7)//8),'big')
    h.update(sign); h.update(len(raw).to_bytes(8,'big')); h.update(raw)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    ap.add_argument('--summary',required=True)
    a=ap.parse_args()
    heights=(3744,3824)
    lifts=(0,1)
    h=hashlib.sha256(); chains=0; binary=0; ternary=0; coprime=0
    for t in heights:
        N,M,r,c,d,e=data(t)
        N1,M1,r1,c1,d1,e1=data(t+16)
        N2,M2,r2,c2,d2,e2=data(t+32)
        invN=pow(N,-1,M2)
        for i in range(4):
          for j in range(4):
            rho,sigma=rho_sigma(t,i,j)
            for ell in range(4):
              rho2,sigma2=rho_sigma(t+16,j,ell)
              L0=((rho2-sigma)*invN)%M2
              for q in lifts:
                L=L0+M2*q
                k=rho+M1*L
                kp=sigma+N*L
                assert (kp-rho2)%M2==0
                kpp=(B[j]*e1+N1*kp-B[ell]*d2)//M2
                U=B[i]*e+N*k
                V=B[j]*e1+N1*kp
                assert U==B[j]*d1+M1*kp
                assert V==B[ell]*d2+M2*kpp
                assert v2(U)==j and v2(V)==ell
                assert v3(U)==BETA[i] and v3(V)==BETA[j]
                CU=U//((1<<j)*pow(3,BETA[i]))
                CV=V//((1<<ell)*pow(3,BETA[j]))
                assert CU>1 and CV>1
                assert math.gcd(CU,6)==math.gcd(CV,6)==1
                assert math.gcd(CU,CV)==1
                for x in (t,i,j,ell,q,k,kp,kpp,U,V,CU,CV): add_int(h,x)
                chains+=1; binary+=2; ternary+=2; coprime+=1
    payload={
      'experiment':'X-8504',
      'heights':list(heights),
      'lifts':list(lifts),
      'two_step_chains':chains,
      'binary_signature_checks':binary,
      'ternary_signature_checks':ternary,
      'coprime_core_checks':coprime,
      'semantic_digest':h.hexdigest(),
      'limitations':[
        'finite arithmetic checks the local primitive-core statement only',
        'the Evertse theorem is not computationally proved',
        'no infinite ordinary seed is constructed'
      ]
    }
    Path(a.output).write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    summary=(
      'X-8504 primitive-core turnover summary\n'
      f'two-step chains:             {chains}\n'
      f'exact binary signatures:     {binary}\n'
      f'exact ternary signatures:    {ternary}\n'
      f'coprime adjacent cores:      {coprime}\n'
      f'semantic digest:\n{h.hexdigest()}\n'
      'all derivation checks passed\n'
    )
    Path(a.summary).write_text(summary)
    print(summary,end='')
if __name__=='__main__': main()
