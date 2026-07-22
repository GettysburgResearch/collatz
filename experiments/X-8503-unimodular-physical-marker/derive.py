#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path

P=(5,30,20,56)
B=(9,54,36,24)

def v2(x:int)->int:
    assert x
    return (abs(x)&-abs(x)).bit_length()-1

def inverse_data(t:int):
    N=pow(3,7*(t+1))
    M=1<<(11*(t+17))
    r=pow(N,-1,M)
    c=(N*r-1)//M
    d=M-r
    e=N-c
    assert M*e-N*d==1
    return N,M,r,c,d,e

def add_int(h, x:int):
    sign=b'-' if x<0 else b'+'
    y=abs(x)
    z=y.to_bytes(max(1,(y.bit_length()+7)//8),'big')
    h.update(sign); h.update(len(z).to_bytes(8,'big')); h.update(z)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    ap.add_argument('--summary',required=True)
    a=ap.parse_args()
    heights=(3744,3760,3840,4000)
    lifts=(0,1,17)
    h=hashlib.sha256()
    cases=0; determinant_rows=0; gcd_rows=0; marker_rows=0; projective_rows=0
    for t in heights:
        N,M,r,c,d,e=inverse_data(t)
        Np,Mp,rp,cp,dp,ep=inverse_data(t+16)
        assert v2(M)==11*(t+17)
        determinant_rows+=1
        for i in range(4):
            assert (-B[i]*r-P[i])%64==0
            for j in range(4):
                rhs=B[j]*dp-B[i]*e
                rho=(rhs*pow(N,-1,Mp))%Mp
                sigma=(B[i]*e+N*rho-B[j]*dp)//Mp
                assert B[i]*e+N*rho==B[j]*dp+Mp*sigma
                pv=11*(t+17)+j-i
                assert 11*(t+17)-3 <= pv <= 11*(t+17)+3
                projective_rows+=1
                for lift in lifts:
                    k=rho+Mp*lift
                    kp=sigma+N*lift
                    W=B[i]*d+M*k
                    U=B[i]*e+N*k
                    assert M*U==N*W+B[i]
                    assert U==B[j]*dp+Mp*kp
                    assert W%64==P[i] and U%64==P[j]
                    assert e*W-d*U==k
                    assert M*U-N*W==B[i]
                    x=(1<<(11*(t+1)-6))*W
                    xp=(1<<(11*(t+17)-6))*U
                    assert v2(x)==11*t+5+i
                    assert v2(xp)==11*(t+16)+5+j
                    assert v2(xp)-v2(x)==176+j-i
                    g=math.gcd(W,U)
                    assert B[i]%g==0
                    for z in (t,i,j,lift,k,kp,W,U,x,xp,g,pv):
                        add_int(h,z)
                    cases+=1; gcd_rows+=1; marker_rows+=1
    for t0,t1 in zip(heights,heights[1:]):
        assert 11*(t1+17)-3 > 11*(t0+17)+3
    targets=((64,5),(32,15),(16,5),(8,7))
    smooth=[]
    for mod,target in targets:
        seen=set(); x=1
        while x not in seen:
            seen.add(x); x=(3*x)%mod
        assert target not in seen
        smooth.append({'modulus':mod,'target':target,'powers':sorted(seen)})
    payload={
      'experiment':'X-8503',
      'heights':list(heights),
      'lifts':list(lifts),
      'unimodular_rows':determinant_rows,
      'exact_connector_cases':cases,
      'intrinsic_marker_cases':marker_rows,
      'adjacent_gcd_cases':gcd_rows,
      'projective_valuation_rows':projective_rows,
      'smooth_residue_rows':smooth,
      'semantic_digest':h.hexdigest(),
      'limitations':[
        'finite arithmetic validates the native gates only',
        'Evertse finiteness is an external theorem, not computationally proved',
        'no forever-defined ordinary seed is constructed'
      ]
    }
    Path(a.output).write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    summary=(
      'X-8503 unimodular physical-marker summary\n'
      f'unimodular rows:              {determinant_rows}\n'
      f'exact connector cases:        {cases}\n'
      f'intrinsic marker cases:       {marker_rows}\n'
      f'adjacent gcd cases:           {gcd_rows}\n'
      f'projective valuation rows:    {projective_rows}\n'
      f'smooth residue obstructions:  {len(smooth)}\n'
      f'semantic digest:\n{h.hexdigest()}\n'
      'all derivation checks passed\n'
    )
    Path(a.summary).write_text(summary)
    print(summary,end='')
if __name__=='__main__':
    main()
