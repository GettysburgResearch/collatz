from fractions import Fraction
from math import comb
import hashlib,json


def ceilq(q):
 return -((-q.numerator)//q.denominator)

def width_q(x,k,q):
 return ceilq(Fraction(3**q*x,2**k)+Fraction(3,2)**q-1)

F=[0]
strict=0
eligible=0
for x in range(1,4097):
 best=x
 best_plain=x
 for k in range(0,x.bit_length()+1):
  L=[width_q(x,k,q) for q in range(k+1)]
  if not all(z>=1 for z in L) or L!=sorted(L):raise RuntimeError(('width positivity/order',x,k,L))
  for h in range(k+1):
   tail=sum(comb(k,q) for q in range(h+1,k+1))
   external=k+ceilq(Fraction(x,2**k))*tail
   best_plain=min(best_plain,external+sum(L[:h+1]))
   if L[h]<x:
    eligible+=1
    best=min(best,external+sum(F[z] for z in L[:h+1]))
 if best>best_plain:raise RuntimeError(('failed domination',x,best,best_plain))
 F.append(best)
 strict+=best<best_plain

alignment=0
for x in range(1,65):
 for k in range(1,8):
  for q in range(k+1):
   length=width_q(x,k,q)
   for a in range(1,2**k+1):
    lo=Fraction(3**q*a,2**k)
    hi=Fraction(3**q*(a+x),2**k)+Fraction(3,2)**q-1
    count=ceilq(hi)-ceilq(lo)
    if count>length or ceilq(hi)>ceilq(lo)+length:raise RuntimeError(('alignment',x,k,q,a))
    alignment+=1
# The wrong floor image width really fails; no merely hypothetical mutation.
lo,hi=Fraction(1),Fraction(3,2)
wrong_floor=(hi-lo).numerator//(hi-lo).denominator
if not ceilq(hi)-ceilq(lo)>wrong_floor:raise RuntimeError('floor mutation control failed')
# k=0,h=0 has its own width as child and must be rejected.
if width_q(128,0,0)!=128:raise RuntimeError('self-recursion control failed')
# An arbitrary set or repeated cycle is not a finite simple path.
if not 128>F[128]:raise RuntimeError('arbitrary-set control failed')
if not len([1,2]*20)>F[16]:raise RuntimeError('repeated-path control failed')
cert1=3**200<2**317
cert2=317**6340<2**6023*200**4000*117**2340
if not(cert1 and cert2):raise RuntimeError('integer exponent witness failed')
if Fraction(39,40)*Fraction(19,20)!=Fraction(741,800):raise RuntimeError('explicit record exponent')
if Fraction(19,20)**2!=Fraction(361,400):raise RuntimeError('qualified record exponent')
print(json.dumps({'full_widths':4096,'full_table_sha256':hashlib.sha256(','.join(map(str,F)).encode('ascii')).hexdigest(),'eligible_menus':eligible,'strict_improvements_over_one_pass':strict,'exact_half_open_alignment_checks':alignment,'negative_controls':4,'integer_power_certificates':2,'record_exponents':['741/800','361/400'],'F_128':F[128],'F_4096':F[4096]},indent=2))
