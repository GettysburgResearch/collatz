#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math
from dataclasses import dataclass
from decimal import Decimal,ROUND_FLOOR,ROUND_CEILING,localcontext
from pathlib import Path
K=3_149_971_404_836;A=4_992_586_555_009;CB=K//2;S=2*K-A;B=CB-S;R=S-4*B
F=(7,191,281,28591,136398329);M=math.prod(F);W=7*2**16*3**9;PREC=170
SEL=(1,4,5,7,9,12,13,14,15,17,18,19,21,22,24,25,26,27,28,30,32,33,34,35,36,39,40,42,43,46,47,52,55,56,58,59,62,63,64,65,66,68,70,71,74,76)
@dataclass(frozen=True)
class S0:p:int;q:int;c:int

def mul(a,b,m):return S0(a.p*b.p%m,a.q*b.q%m,(b.p*a.c+a.q*b.c)%m)
def pw(x,n,m):
 o=S0(1%m,1%m,0)
 while n:
  if n&1:o=mul(o,x,m)
  x=mul(x,x,m);n//=2
 return o
def mech(p,q,up,z,o,m):
 if p==0:return pw(z,q,m)
 if p==q:return pw(o,q,m)
 a,r=divmod(q,p)
 if up:return mech(r,p,False,mul(o,pw(z,a-1,m),m),mul(o,pw(z,a,m),m),m)
 return mech(r,p,True,mul(pw(z,a-1,m),o,m),mul(pw(z,a,m),o,m),m)
def chart(b,m):return S0(9%m,pow(2,4-b,m),3*b%m)
def run(d,m):
 o=chart(0,m)
 for _ in range(4+d):o=mul(o,chart(1,m),m)
 return o
def po(n):return n*R//B
def bit(n):return po(n+1)-po(n)
def sites():
 a=[];p=-2;n=0
 while len(a)<80:
  x,y=bit(n),bit(n+1)
  if x!=y and n>p+1:a.append((n,x,y));p=n
  n+=1
 return a
def delt(site,m):
 n,x,y=site;sg=-1 if (x,y)==(0,1) else 1;pe=16*n+3*po(n);pb=5*n+po(n)
 return sg*(W%m)*pow(2,pe,m)*pow(9,CB-pb-11,m)%m
class I:
 def __init__(self,a,b=None):self.lo=Decimal(a);self.hi=Decimal(a if b is None else b)
def dr(a,b,f,r):
 with localcontext() as c:c.prec=PREC;c.rounding=r;return f(a,b)
def add(x,y):return I(dr(x.lo,y.lo,lambda a,b:a+b,ROUND_FLOOR),dr(x.hi,y.hi,lambda a,b:a+b,ROUND_CEILING))
def neg(x):return I(x.hi.copy_negate(),x.lo.copy_negate())
def mulI(x,y):
 lo=[];hi=[]
 for a in (x.lo,x.hi):
  for b in (y.lo,y.hi):lo.append(dr(a,b,lambda c,d:c*d,ROUND_FLOOR));hi.append(dr(a,b,lambda c,d:c*d,ROUND_CEILING))
 return I(min(lo),max(hi))
def frac(a,b):
 with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=Decimal(a)/Decimal(b)
 with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=Decimal(a)/Decimal(b)
 return I(lo,hi)
@dataclass(frozen=True)
class A0:r:I;t:I
def amul(a,b):return A0(mulI(a.r,b.r),add(mulI(b.r,a.t),b.t))
def apw(x,n):
 o=A0(I(1),I(0))
 while n:
  if n&1:o=amul(o,x)
  x=amul(x,x);n//=2
 return o
def ame(p,q,up,z,o):
 if p==0:return apw(z,q)
 if p==q:return apw(o,q)
 a,r=divmod(q,p)
 if up:return ame(r,p,False,amul(o,apw(z,a-1)),amul(o,apw(z,a)))
 return ame(r,p,True,amul(apw(z,a-1),o),amul(apw(z,a),o))
def cair(b):return A0(frac(9,2**(4-b)),frac(3*b,2**(4-b)))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('canonical',type=Path);a=ap.parse_args();p=json.loads(a.canonical.read_text());ss=sites();assert [ss[i][0] for i in SEL]==p['run_repair']['selected_run_positions']
 cbase=mech(S,CB,False,chart(0,M),chart(1,M),M);rbase=mech(R,B,False,run(0,M),run(1,M),M);assert cbase==rbase
 assert (rbase.c+sum(delt(ss[i],M) for i in SEL))%M==0
 for row,prime in zip(p['run_repair']['quotient_rows'],F):
  m=prime*prime;base=mech(R,B,False,run(0,m),run(1,m),m).c;c=(base+sum(delt(ss[i],m) for i in SEL))%m;d=(pow(2,A,m)-pow(3,K,m))%m
  assert (c,d,c//prime,d//prime,(c//prime)*pow(d//prime,-1,prime)%prime)==(row['C_mod_p2'],row['D_mod_p2'],row['C_over_p_mod_p'],row['D_over_p_mod_p'],row['quotient_mod_p'])
 base=ame(S,CB,False,cair(0),cair(1));corr=I(0)
 for i in SEL:
  n,x,y=ss[i];sg=-1 if (x,y)==(0,1) else 1;pe=16*n+3*po(n);pb=5*n+po(n);z=mulI(base.r,frac(W*(1<<pe),9**(pb+11)));corr=add(corr,z if sg>0 else neg(z))
 num=add(base.t,corr);den=add(I(1),neg(base.r));lo=dr(num.lo,den.hi,lambda x,y:x/y,ROUND_FLOOR);hi=dr(num.hi,den.lo,lambda x,y:x/y,ROUND_CEILING)
 assert str(lo)==p['run_repair']['fixed_point_lower'] and str(hi)==p['run_repair']['fixed_point_upper'];assert int(lo)==p['run_repair']['unique_floor']
 checks=0
 for q in range(2,40):
  for r in range(1,q):
   if math.gcd(r,q)>1:continue
   bits=[((j+1)*r)//q-(j*r)//q for j in range(q)];chartbits=[z for d in bits for z in ([0]+[1]*(4+d))]
   sm=S0(1,1,0)
   for d in bits:sm=mul(sm,run(d,1_000_000_007),1_000_000_007)
   sc=S0(1,1,0)
   for d in chartbits:sc=mul(sc,chart(d,1_000_000_007),1_000_000_007)
   assert sm==sc;checks+=1
 assert checks==473
 print(json.dumps({'verified':True,'small_compressions':checks,'selected_swaps':len(SEL),'prime_rows':len(F)},sort_keys=True))
if __name__=='__main__':main()
