"""Bounded physical-merger search inspired by the AL 27 (mod 128) branch.

No semigroup multiplier is treated as an ordinary edge. A successful row is
an affine source/partner progression; a failed search is only unresolved.
Run package_al27.py to serialize the certificate and verify_al27.py to check
it with a separate literal-forward implementation.
"""
from __future__ import annotations
import json

def step(n):return (3*n+1)//2 if n&1 else n//2

def advance(n,h):
 p=0
 for _ in range(h):p+=n&1;n=step(n)
 return n,p

def certificate(n,M,h,J,max_a=28,node_cap=100000):
 y,p=advance(n,h)
 # Binary source cylinder n+2^h*3^J*t, exact prefix slope 3^(p+J).
 S=3**(p+J)
 stack=[(y,S,0,0,'')];count=0
 while stack:
  u,A,a,q,w=stack.pop();count+=1
  if A<M:
   t0=max(0,(u-n)//(M-A)+1)
   if u<n:t0=0
   return dict(n=n,M=M,h=h,J=J,partner=u,slope=A,a=a,q=q,p=p,min_t=t0,reverse=w,nodes=count)
  if a>=max_a or count>=node_cap:continue
  # Need all remaining available odd divisions even ignoring legality to shrink slope.
  rem=p+J-q
  if A*2**rem>=M*3**rem:continue
  stack.append((2*u,2*A,a+1,q,w+'0'))
  if rem and u%3==2:
   stack.append(((2*u-1)//3,2*A//3,a+1,q+1,w+'1'))
 return None

def scan(k,s,H,J):
 M=2**H*3**J;rows=[];miss=[]
 for binary in range(s,2**H,2**k):
  for z in range(3**J):
   n=binary+2**H*z
   r=certificate(n,M,H,J,max_a=H+J*2+4)
   if r:rows.append(r)
   else:miss.append(n)
 return dict(k=k,s=s,H=H,J=J,total=len(rows)+len(miss),covered=len(rows),miss=miss[:1000],miss_total=len(miss),rows=rows)
if __name__=='__main__':
 r=scan(7,27,13,2)
 print(json.dumps({k:v for k,v in r.items() if k not in ('rows','miss')},indent=2))
