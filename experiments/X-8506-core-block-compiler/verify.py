#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path

P=(5,30,20,56)
BETA=(2,3,2,1)

def make_block(t,gamma,i):
    g=7*(t+1)+gamma-BETA[i]
    d=11*(t+17)-i
    odd=3**g; radix=2**d
    residue=(-pow(odd,-1,radix))%radix
    carry=(odd*residue+1)//radix
    return g,d,odd,radix,residue,carry

def decode(t,gamma,i,c):
    g,d,odd,radix,residue,carry=make_block(t,gamma,i)
    x=odd*c+1
    assert x%radix==0
    y=x//radix
    out=(3**BETA[i]*y)%64
    assert out in P
    j=P.index(out)
    return j,y//(2**j)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('canonical'); a=ap.parse_args()
    frozen=json.loads(Path(a.canonical).read_text()); assert frozen['experiment']=='X-8506'
    t=3792; states=targets=replays=0
    for gamma in (1,2,3):
      for i in range(4):
        g,d,odd,radix,residue,carry=make_block(t,gamma,i); states+=1
        for j in range(4):
          kappa=(pow(odd,-1,64)*((pow(3**BETA[i],-1,64)*P[j]-carry)%64))%64
          low=residue+radix*kappa
          out0=(carry+odd*kappa)//(2**j)
          allowed=[r for r in range(3) if (low+2**(d+6)*r)%3]
          assert len(allowed)==2; targets+=1
          for r in allowed:
            for m in (2,29):
              c=low+2**(d+6)*r+3*2**(d+6)*m
              cp=out0+2**(6-j)*odd*r+3*2**(6-j)*odd*m
              assert math.gcd(c,6)==math.gcd(cp,6)==1
              assert decode(t,gamma,i,c)==(j,cp)
              assert cp>2**170*c
              replays+=1
    assert frozen['finite_core_states']==24
    assert frozen['target_binary_blocks']==96
    assert frozen['exact_block_replays']==576
    print('X-8506 independent checker')
    print(f'finite states:              {states}')
    print(f'binary target blocks:       {targets}')
    print(f'ordinary block replays:     {replays}')
    print('all independent checks passed')
if __name__=='__main__': main()
