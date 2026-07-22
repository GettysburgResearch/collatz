#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from functools import lru_cache
from pathlib import Path

P=(5,30,20,56)
BETA=(2,3,2,1)

@lru_cache(None)
def inverse_block(t,gamma,i):
    G=7*(t+1)+gamma-BETA[i]
    D=11*(t+17)-i
    A=3**G; Q=2**D
    a=(-pow(A,-1,Q))%Q
    h=(A*a+1)//Q
    return G,D,A,Q,a,h

def step(t,gamma,i,C):
    G,D,A,Q,a,h=inverse_block(t,gamma,i)
    X=A*C+1
    if X%Q: return None
    Y=X//Q
    out=(3**BETA[i]*Y)%64
    if out not in P: return None
    j=P.index(out)
    return BETA[i],j,Y//(2**j)

def add_int(h,x):
    sign=b'-' if x<0 else b'+'
    y=abs(x); raw=y.to_bytes(max(1,(y.bit_length()+7)//8),'big')
    h.update(sign); h.update(len(raw).to_bytes(8,'big')); h.update(raw)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--summary',required=True); a=ap.parse_args()
    heights=(3744,3824); tails=(0,1,17)
    digest=hashlib.sha256(); states=targets=lifts=replays=growth=0
    for t in heights:
      for gamma in (1,2,3):
        for i in range(4):
          G,D,A,Q,ainv,h=inverse_block(t,gamma,i)
          states+=1
          for j in range(4):
            kappa=(pow(A,-1,64)*((pow(3**BETA[i],-1,64)*P[j]-h)%64))%64
            R=ainv+Q*kappa
            assert (h+A*kappa)%(2**j)==0
            S=(h+A*kappa)//(2**j)
            allowed=[nu for nu in range(3) if (R+2**(D+6)*nu)%3]
            assert len(allowed)==2
            targets+=1; lifts+=2
            for nu in allowed:
              Rh=R+2**(D+6)*nu
              Sh=S+2**(6-j)*A*nu
              for m in tails:
                C=Rh+3*2**(D+6)*m
                Cp=Sh+3*2**(6-j)*A*m
                assert math.gcd(C,6)==math.gcd(Cp,6)==1
                assert step(t,gamma,i,C)==(BETA[i],j,Cp)
                assert Cp>2**170*C
                for x in (t,gamma,i,j,nu,m,G,D,ainv,h,kappa,R,S,Rh,Sh,C,Cp): add_int(digest,x)
                replays+=1; growth+=1
    payload={
      'experiment':'X-8506','heights':list(heights),'tails':list(tails),
      'finite_core_states':states,'target_binary_blocks':targets,
      'admissible_ternary_lifts':lifts,'exact_block_replays':replays,
      'growth_checks':growth,'semantic_digest':digest.hexdigest(),
      'limitations':['local compiler only','no infinite compatible block path is proved']
    }
    Path(a.output).write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    summary=(
      'X-8506 core block compiler summary\n'
      f'finite core states:          {states}\n'
      f'target binary blocks:        {targets}\n'
      f'admissible ternary lifts:    {lifts}\n'
      f'exact block replays:         {replays}\n'
      f'170-bit growth checks:       {growth}\n'
      f'semantic digest:\n{digest.hexdigest()}\n'
      'all derivation checks passed\n')
    Path(a.summary).write_text(summary); print(summary,end='')
if __name__=='__main__': main()
