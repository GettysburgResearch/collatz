#!/usr/bin/env python3
"""Independent exact crosswalk for PR #49 and PR #51 (standard library only)."""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from functools import lru_cache
from pathlib import Path
sys.set_int_max_str_digits(0)
P=(5,30,20,56); BETA=(2,3,2,1)

def shortcut(n): return n//2 if n%2==0 else (3*n+1)//2
def iterate(n,k):
    for _ in range(k): n=shortcut(n)
    return n

@lru_cache(None)
def d49(t,g,i):
    G=7*(t+1)+g-BETA[i]; D=11*(t+17)-i; A=3**G; Q=1<<D
    a=(-pow(A,-1,Q))%Q; h=(A*a+1)//Q
    return G,D,A,Q,a,h

@lru_cache(None)
def b49(t,g,i):
    G,D,A,Q,a,h=d49(t,g,i); out={}
    for j in range(4):
        kap=(pow(A,-1,64)*(pow(3**BETA[i],-1,64)*P[j]-h))%64
        R=a+Q*kap; S=(h+A*kap)//(1<<j)
        for nu in range(3):
            Rh=R+(1<<(D+6))*nu
            if Rh%3: out[j,nu]=(Rh,S+(1<<(6-j))*A*nu)
    assert len(out)==8
    return out

@lru_cache(None)
def inv49(t,g,i):
    A=d49(t,g,i)[2];H=11*(t+33);M=1<<H
    return A,H,M,pow(A,-1,M)

def tr49(t,g,i,j,nu,k):
    _,Sh=b49(t,g,i)[j,nu]; row=b49(t+16,BETA[i],j)
    cand=[(n,R) for (jj,n),(R,S) in row.items() if jj==k and R%3==Sh%3]
    assert len(cand)==1
    n,R2=cand[0]; diff=R2-Sh
    assert diff%(3*(1<<(6-j)))==0
    delta=diff//(3*(1<<(6-j))); A,H,M,inv=inv49(t,g,i)
    rho=inv*delta%M; sig=(A*rho-delta)//M
    D2=d49(t+16,BETA[i],j)[1]; SM=3*(1<<(D2+6))
    assert Sh+3*(1<<(6-j))*A*rho==R2+SM*sig and sig>=0
    for ell in (0,1,3):
        assert Sh+3*(1<<(6-j))*A*(rho+M*ell)==R2+SM*(sig+A*ell)
    return n,rho,sig,H

def review49():
    states=blocks=replays=cross=nonzero=0; t=3744
    for g in (1,2,3):
      for i in range(4):
        G,D,A,Q,a,h=d49(t,g,i); states+=1
        for (j,nu),(R,S) in b49(t,g,i).items():
          blocks+=1
          for m in (0,1,17):
            C=R+3*(1<<(D+6))*m; Cp=S+3*(1<<(6-j))*A*m; X=A*C+1
            assert math.gcd(C,6)==math.gcd(Cp,6)==1 and X%Q==0
            Y=X//Q
            assert (3**BETA[i]*Y)%64==P[j] and Cp==Y//(1<<j)
            assert Cp>(1<<170)*C and (2**i*3**g*C)%64==P[i]
            replays+=1
          for k in range(4):
            n,rho,sig,H=tr49(t,g,i,j,nu,k); cross+=1; nonzero+=rho!=0
            assert H==11*(t+33) and sig>=0
    assert 3**665>2**1054
    margin=lambda t:1054*(7*t+5)-665*(11*(t+49)+1)
    assert margin(5616)==-22 and margin(5632)==986
    assert 3**(7*5616+5)<2**(11*(5616+49)+1)
    for g in (1,2,3):
      for i in range(4): assert 3**(7*(5632+1)+g-BETA[i])>2**(11*(5632+49)+1)
    return {'frozen_head':'3357d36c7464e036363c6579d873f19f5674adad','critical_chain':['L-8504','L-8505','T-8507','L-8506','T-8506'],'local_states':states,'local_blocks':blocks,'local_replays':replays,'two_block_crosswalks':cross,'target_independent_H':'11*(t+33)','top_lift_first_multiple_of_16':5632,'margin_at_5616':margin(5616),'margin_at_5632':margin(5632),'top_lift_uniform_state_checks':12,'nonzero_two_block_corrections_at_3744':nonzero}

def chart(z):
    if z>0 and z%8==0:return 9*z//8,'A'
    if z>0 and z%16==1:return (9*z+7)//16,'B'

@lru_cache(None)
def a51(r,s,seven=False):
    M=1<<(4+3*s); L=16*M
    b=(7 if s%2==0 else 15) if seven else (1 if s%2==0 else 9)
    c=1 if seven else 7
    return (M*b-c)*pow(9**(r+1),-1,L)%L

@lru_cache(None)
def c51(r,s): return (9**(r+1)*a51(r,s)+7)//(1<<(4+3*s))
@lru_cache(None)
def tr51(r,s,t):
    M=1<<(4+3*t); L=16*M; aa=a51(s,t); cc=c51(r,s)
    assert (aa-cc)%16==0
    rho=pow(9**(r+1),-1,M)*((aa-cc)//16)%M
    sig=(cc+16*9**(r+1)*rho-aa)//L
    assert cc+16*9**(r+1)*rho==aa+L*sig and sig>=0
    return rho,sig,M

def review51():
    edges=0
    for q in range(1,5001):
        z=8*q; assert chart(z)==(9*q,'A') and iterate(6*z-5,3)==6*(9*q)-5; edges+=1
    for q in range(5001):
        z=1+16*q; assert chart(z)==(1+9*q,'B') and iterate(6*z-5,4)==6*(1+9*q)-5; edges+=1
    macros=ident=seven=0
    for r in range(16):
      u0=pow(9**r,-1,16)
      for q in range(13):
        u=u0+16*q; z=(1<<(3*r))*u; cur=z
        for _ in range(r): cur,l=chart(cur); assert l=='A'
        cur,l=chart(cur); assert l=='B' and cur==(9**(r+1)*u+7)//16; macros+=1
      for s in range(16):
        M=1<<(4+3*s); L=16*M; aa=a51(r,s); cc=c51(r,s)
        assert cc%16==(1 if s%2==0 else 9)
        for k in (0,1,17):
            u=aa+L*k; up=cc+16*9**(r+1)*k
            assert 9**(r+1)*u+7==M*up; ident+=1
        aa7=a51(r,s,True); vp=(9**(r+1)*aa7+1)//M
        assert vp%16==(7 if s%2==0 else 15); seven+=1
        for t in range(16):
          rho,sig,Mt=tr51(r,s,t)
          for ell in (0,1,3):
            k=rho+Mt*ell
            assert cc+16*9**(r+1)*k==a51(s,t)+16*Mt*(sig+9**(r+1)*ell); ident+=1
    for r in range(31): assert (9**(r+1)>2**(4+3*r))==(r>=5)
    seeds=redges=0
    for m in range(6,1201,6):
        z=((1<<(m+4))-7)//9; cur,l=chart(z); assert (cur,l)==(1<<m,'B')
        d=m//3
        for _ in range(d): cur,l=chart(cur); assert l=='A'; redges+=1
        assert cur==9**d; s2=(d&-d).bit_length()-1; k=(3+s2)//4
        for _ in range(k): cur,l=chart(cur); assert l=='B'; redges+=1
        assert cur==1+9**k*(9**d-1)//16**k
        assert (cur%8==0)==(s2%4==1 and (d>>s2)%8==3); seeds+=1
    cone=0
    for r in range(5,26):
      for s in range(5,10):
       for t in range(5,10):
        rho,sig,Mt=tr51(r,s,t)
        for u in range(5,26):
          rho2,_,Mu=tr51(s,t,u)
          if 9**(r+1)<=2*Mu: continue
          A=9**(r+1); theta=pow(A,-1,Mu)*(rho2-sig)%Mu
          for ell in ((theta if theta>=1 else Mu),theta+Mu):
            num=sig+A*ell-rho2; assert num%Mu==0 and num//Mu>=2*ell; cone+=1
    assert 3**53>2**84 and 3**12>2**19 and 3**65>2**103
    for n in range(501):
        r=64+n; assert 9**(r+1)>2**(5+3*(r+3))
    return {'frozen_head':'9c0753db8543a99247ed55beefbce75ca8f2b507','critical_chain':['O-8001','L-8002','L-8004','T-8002','L-8003'],'physical_chart_edges':edges,'maximal_run_macros':macros,'quotient_identities':ident,'divisible_seven_checks':seven,'reset_seeds':seeds,'reset_chart_edges':redges,'refund_cone_exact_doubling_checks':cone,'aperiodic_linear_schedule':'r_n=64+n','linear_schedule_checks':501}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path); ap.add_argument('--check-results',type=Path); a=ap.parse_args()
    p={'agent':'gpt56-refund-01','date':'2026-07-23','experiment_id':'X-8202','new_result':{'common_form':'q=rho+2^H*ell; q_next=sigma+P*ell; sigma>=0','counterexample_claimed':False,'pr49_top_lift_doubling_height':5632,'pr51_refund_cone':'9^(r_n+1)>2^(5+3*r_(n+3))'},'pr49':review49(),'pr51':review51()}
    p['semantic_digest']=hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    data=(json.dumps(p,indent=2,sort_keys=True)+'\n').encode()
    if a.output:a.output.write_bytes(data)
    if a.check_results and a.check_results.read_bytes()!=data: raise SystemExit('canonical result mismatch')
    print(data.decode(),end='')
if __name__=='__main__':main()
