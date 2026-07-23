#!/usr/bin/env python3
"""Separately written verifier for X-8202; does not import run.py."""
from __future__ import annotations
import hashlib,json,math,sys
from functools import lru_cache
from pathlib import Path
sys.set_int_max_str_digits(0)
P=(5,30,20,56); BETA=(2,3,2,1)
def S(n):return n//2 if n%2==0 else (3*n+1)//2
def it(n,k):
 for _ in range(k):n=S(n)
 return n
def chart(z):
 if z>0 and z%8==0:return 9*z//8,'A'
 if z>0 and z%16==1:return (9*z+7)//16,'B'
@lru_cache(None)
def aa(r,s):
 M=1<<(4+3*s);L=16*M;b=1 if s%2==0 else 9
 return (M*b-7)*pow(9**(r+1),-1,L)%L
@lru_cache(None)
def cc(r,s):return (9**(r+1)*aa(r,s)+7)//(1<<(4+3*s))
@lru_cache(None)
def tr(r,s,t):
 M=1<<(4+3*t);L=16*M;x=aa(s,t);c=cc(r,s)
 rho=pow(9**(r+1),-1,M)*((x-c)//16)%M;sig=(c+16*9**(r+1)*rho-x)//L
 assert sig>=0
 return rho,sig,M

def check49(R):
 t=3744;states=blocks=replays=cross=nonzero=0;cache={}
 def B(tt,g,i):
  key=tt,g,i
  if key in cache:return cache[key]
  G=7*(tt+1)+g-BETA[i];D=11*(tt+17)-i;A=3**G;Q=1<<D;a=(-pow(A,-1,Q))%Q;h=(A*a+1)//Q;row=[]
  for j in range(4):
   ks=[k for k in range(64) if (3**BETA[i]*(h+A*k))%64==P[j]];assert len(ks)==1
   k=ks[0];r=a+Q*k;s=(h+A*k)//(1<<j)
   for nu in range(3):
    rh=r+(1<<(D+6))*nu
    if rh%3:row.append((j,nu,rh,s+(1<<(6-j))*A*nu))
  assert len(row)==8;cache[key]=(G,D,A,Q,a,h,row);return cache[key]
 for g in (1,2,3):
  for i in range(4):
   G,D,A,Q,a,h,row=B(t,g,i);states+=1;blocks+=8
   for j,nu,rh,sh in row:
    for m in (0,1,17):
     C=rh+3*(1<<(D+6))*m;Cp=sh+3*(1<<(6-j))*A*m;X=A*C+1
     assert X%Q==0 and math.gcd(C,6)==math.gcd(Cp,6)==1
     Y=X//Q;assert (3**BETA[i]*Y)%64==P[j] and Cp==Y//(1<<j);replays+=1
    for k in range(4):
     row2=B(t+16,BETA[i],j)[6];mch=[z for z in row2 if z[0]==k and z[2]%3==sh%3];assert len(mch)==1
     _,n,r2,s2=mch[0];d=r2-sh;assert d%(3*(1<<(6-j)))==0;delta=d//(3*(1<<(6-j)))
     H=11*(t+33);M=1<<H;rho=pow(A,-1,M)*delta%M;sig=(A*rho-delta)//M;assert sig>=0
     if rho:nonzero+=1
     cross+=1
 assert (states,blocks,replays,cross,nonzero)==(R['local_states'],R['local_blocks'],R['local_replays'],R['two_block_crosswalks'],R['nonzero_two_block_corrections_at_3744'])
 assert 3**665>2**1054 and 1054*(7*5616+5)-665*(11*(5616+49)+1)==-22 and 1054*(7*5632+5)-665*(11*(5632+49)+1)==986
 for g in (1,2,3):
  for i in range(4):assert 3**(7*5633+g-BETA[i])>2**(11*(5632+49)+1)

def check51(R):
 e=0
 for q in range(1,5001):z=8*q;assert chart(z)==(9*q,'A') and it(6*z-5,3)==54*q-5;e+=1
 for q in range(5001):z=1+16*q;assert chart(z)==(1+9*q,'B') and it(6*z-5,4)==6*(1+9*q)-5;e+=1
 assert e==R['physical_chart_edges'];mac=ident=seven=0
 for r in range(16):
  u0=pow(9**r,-1,16)
  for q in range(13):
   u=u0+16*q;z=(1<<(3*r))*u;cur=z
   for _ in range(r):cur,l=chart(cur);assert l=='A'
   cur,l=chart(cur);assert l=='B' and cur==(9**(r+1)*u+7)//16;mac+=1
  for s in range(16):
   M=1<<(4+3*s);L=16*M;a=aa(r,s);c=cc(r,s)
   for k in (0,1,17):assert 9**(r+1)*(a+L*k)+7==M*(c+16*9**(r+1)*k);ident+=1
   ee=7 if s%2==0 else 15;a7=(M*ee-1)*pow(9**(r+1),-1,L)%L;assert ((9**(r+1)*a7+1)//M)%16==ee;seven+=1
   for t in range(16):
    rho,sig,Mt=tr(r,s,t)
    for ell in (0,1,3):assert c+16*9**(r+1)*(rho+Mt*ell)==aa(s,t)+16*Mt*(sig+9**(r+1)*ell);ident+=1
 assert (mac,ident,seven)==(R['maximal_run_macros'],R['quotient_identities'],R['divisible_seven_checks'])
 seeds=edges=0
 for m in range(6,1201,6):
  z=((1<<(m+4))-7)//9;cur,l=chart(z);assert (cur,l)==(1<<m,'B');d=m//3
  for _ in range(d):cur,l=chart(cur);assert l=='A';edges+=1
  s2=(d&-d).bit_length()-1;k=(3+s2)//4
  for _ in range(k):cur,l=chart(cur);assert l=='B';edges+=1
  assert cur==1+9**k*(9**d-1)//16**k and (cur%8==0)==(s2%4==1 and (d>>s2)%8==3);seeds+=1
 assert (seeds,edges)==(R['reset_seeds'],R['reset_chart_edges'])
 cone=0
 for r in range(5,26):
  for s in range(5,10):
   for t in range(5,10):
    rho,sig,Mt=tr(r,s,t)
    for u in range(5,26):
     rho2,_,Mu=tr(s,t,u)
     if 9**(r+1)<=2*Mu:continue
     A=9**(r+1);theta=pow(A,-1,Mu)*(rho2-sig)%Mu
     for ell in ((theta if theta else Mu),theta+Mu):
      n=sig+A*ell-rho2;assert n%Mu==0 and n//Mu>=2*ell;cone+=1
 assert cone==R['refund_cone_exact_doubling_checks']
 for n in range(501):r=64+n;assert 9**(r+1)>2**(5+3*(r+3))

def main():
 if len(sys.argv)!=2:raise SystemExit('usage: verify.py canonical.json')
 p=json.loads(Path(sys.argv[1]).read_text());d=p.pop('semantic_digest');assert hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest()==d;p['semantic_digest']=d
 check49(p['pr49']);check51(p['pr51']);assert not p['new_result']['counterexample_claimed'];print('all independent X-8202 critical-path checks passed')
if __name__=='__main__':main()
