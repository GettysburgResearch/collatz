#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from functools import lru_cache
from pathlib import Path

P=(5,30,20,56)
B=(9,54,36,24)
BETA=(2,3,2,1)

@lru_cache(None)
def data(t):
    N=3**(7*(t+1)); M=2**(11*(t+17)); r=pow(N,-1,M); c=(N*r-1)//M
    return N,M,r,c,M-r,N-c

def rho_sigma(t,i,j):
    N,M,r,c,d,e=data(t); N1,M1,r1,c1,d1,e1=data(t+16)
    rho=((B[j]*d1-B[i]*e)*pow(N,-1,M1))%M1
    sigma=(B[i]*e+N*rho-B[j]*d1)//M1
    return rho,sigma

def add_int(h,x):
    sign=b'-' if x<0 else b'+'
    y=abs(x); raw=y.to_bytes(max(1,(y.bit_length()+7)//8),'big')
    h.update(sign); h.update(len(raw).to_bytes(8,'big')); h.update(raw)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--summary',required=True); a=ap.parse_args()
    heights=(3744,3824); lifts=(0,1)
    h=hashlib.sha256(); cases=source=divisibility=targets=growth=0
    for t in heights:
        N,M,r,c,d,e=data(t); N1,M1,r1,c1,d1,e1=data(t+16); N2,M2,r2,c2,d2,e2=data(t+32)
        invN=pow(N,-1,M2)
        for i in range(4):
          for j in range(4):
            rho,sigma=rho_sigma(t,i,j)
            for ell in range(4):
              rho2,sigma2=rho_sigma(t+16,j,ell)
              lift0=((rho2-sigma)*invN)%M2
              for q in lifts:
                lift=lift0+M2*q
                k=rho+M1*lift; kp=sigma+N*lift
                U=B[i]*e+N*k; V=B[j]*e1+N1*kp
                gamma=BETA[i]
                C=U//(2**j*3**gamma)
                G=7*(t+17)+gamma-BETA[j]
                D=11*(t+33)-j
                X=3**G*C+1
                assert (2**j*3**gamma*C)%64==P[j]
                source+=1
                assert X%(2**D)==0
                divisibility+=1
                Y=X//(2**D)
                out=(3**BETA[j]*Y)%64
                assert out==P[ell]
                targets+=1
                Cp=Y//(2**ell)
                assert Cp==V//(2**ell*3**BETA[j])
                assert Cp>2**170*C
                growth+=1
                n=2**(11*(t+16)+5+j)*3**gamma*C-34
                np=2**(11*(t+32)+5+ell)*3**BETA[j]*Cp-34
                assert n+34==2**(11*(t+16)+5)*U
                assert np+34==2**(11*(t+32)+5)*V
                for z in (t,i,j,ell,q,C,Cp,G,D,X,Y,n,np): add_int(h,z)
                cases+=1
    payload={
      'experiment':'X-8505','heights':list(heights),'lifts':list(lifts),
      'intrinsic_core_transitions':cases,'automatic_source_cells':source,
      'high_block_divisibility':divisibility,'six_bit_output_decodes':targets,
      'growth_checks':growth,'semantic_digest':h.hexdigest(),
      'limitations':['finite reconstruction only','no forever-defined core is supplied']
    }
    Path(a.output).write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    summary=(
      'X-8505 intrinsic core decoder summary\n'
      f'intrinsic core transitions:       {cases}\n'
      f'automatic source-cell checks:     {source}\n'
      f'high-block divisibility checks:   {divisibility}\n'
      f'six-bit output decodes:           {targets}\n'
      f'170-bit growth checks:            {growth}\n'
      f'semantic digest:\n{h.hexdigest()}\n'
      'all derivation checks passed\n')
    Path(a.summary).write_text(summary); print(summary,end='')
if __name__=='__main__': main()
