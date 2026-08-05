#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from pathlib import Path
from typing import Callable

K=3_149_971_404_836
A=4_992_586_555_009
CHART_BLOCKS=K//2
EXPANDING=2*K-A
RUN_LENGTH=CHART_BLOCKS-EXPANDING
RUN_WEIGHT=EXPANDING-4*RUN_LENGTH
FACTORS=(7,191,281,28_591,136_398_329)
MODULUS=math.prod(FACTORS)
OMEGA=7*(2**16)*(3**9)
SELECTED_INDICES=(1,4,5,7,9,12,13,14,15,17,18,19,21,22,24,25,26,27,28,30,32,33,34,35,36,39,40,42,43,46,47,52,55,56,58,59,62,63,64,65,66,68,70,71,74,76)
EXPECTED_POSITIONS=(7,33,42,59,77,103,111,120,129,146,155,164,181,190,207,216,224,233,242,259,277,285,294,303,311,337,346,364,372,398,407,450,477,485,503,511,537,546,555,563,572,590,607,616,642,659)
PREC=170

@dataclass(frozen=True)
class Summary:
    length:int; exponent:int; odd:int; dyadic:int; constant:int; modulus:int
    def __mul__(self,other:'Summary')->'Summary':
        if self.modulus!=other.modulus: raise ValueError('modulus mismatch')
        m=self.modulus
        return Summary(self.length+other.length,self.exponent+other.exponent,
            self.odd*other.odd%m,self.dyadic*other.dyadic%m,
            (other.odd*self.constant+self.dyadic*other.constant)%m,m)

def identity(m:int)->Summary:return Summary(0,0,1%m,1%m,0,m)
def run_letter(bit:int,m:int)->Summary:
    r=4+bit; e=16+3*bit
    return Summary(1,e,pow(9,5+bit,m),pow(2,e,m),48*(pow(9,r,m)-pow(8,r,m))%m,m)
def power(v,n,ident,mul):
    out=ident
    while n:
        if n&1:out=mul(out,v)
        v=mul(v,v);n//=2
    return out
def mechanical_product(ones,length,upper,zero,one,ident,mul:Callable):
    if ones==0:return power(zero,length,ident,mul)
    if ones==length:return power(one,length,ident,mul)
    q,r=divmod(length,ones)
    if upper:
        z=mul(one,power(zero,q-1,ident,mul));o=mul(one,power(zero,q,ident,mul))
        return mechanical_product(r,ones,False,z,o,ident,mul)
    z=mul(power(zero,q-1,ident,mul),one);o=mul(power(zero,q,ident,mul),one)
    return mechanical_product(r,ones,True,z,o,ident,mul)
def bit(pos:int)->int:return ((pos+1)*RUN_WEIGHT)//RUN_LENGTH-(pos*RUN_WEIGHT)//RUN_LENGTH
def prefix_ones(count:int)->int:return count*RUN_WEIGHT//RUN_LENGTH
def sites(count=80):
    out=[];prev=-2;pos=0
    while len(out)<count:
        l,r=bit(pos),bit(pos+1)
        if l!=r and pos>prev+1:out.append((pos,l,r));prev=pos
        pos+=1
    return out
def delta(site,mod:int)->int:
    pos,l,r=site; sign=-1 if (l,r)==(0,1) else 1
    pref_e=16*pos+3*prefix_ones(pos)
    pref_blocks=5*pos+prefix_ones(pos)
    return sign*(OMEGA%mod)*pow(2,pref_e,mod)*pow(9,CHART_BLOCKS-pref_blocks-11,mod)%mod

def prime64(n:int)->bool:
    if n<2:return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%p==0:return n==p
    d=n-1;s=0
    while d%2==0:s+=1;d//=2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a%n==0:continue
        x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True
def order2(p:int)->int:
    assert prime64(p); n=p-1;fs=[];d=2
    while d*d<=n:
        if n%d==0:
            fs.append(d)
            while n%d==0:n//=d
        d+=1 if d==2 else 2
    if n>1:fs.append(n)
    o=p-1
    for f in fs:
        while o%f==0 and pow(2,o//f,p)==1:o//=f
    return o
def crt(moduli,residues):
    M=math.prod(moduli);x=0
    for m,r in zip(moduli,residues):
        q=M//m;x=(x+r*q*pow(q,-1,m))%M
    return x

class Interval:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):self.lo=Decimal(lo);self.hi=Decimal(lo if hi is None else hi)
def directed(a,b,op,rounding):
    with localcontext() as c:c.prec=PREC;c.rounding=rounding;return op(a,b)
def iadd(x,y):return Interval(directed(x.lo,y.lo,lambda a,b:a+b,ROUND_FLOOR),directed(x.hi,y.hi,lambda a,b:a+b,ROUND_CEILING))
def ineg(x):return Interval(x.hi.copy_negate(),x.lo.copy_negate())
def isub(x,y):return iadd(x,ineg(y))
def imul(x,y):
    lo=[];hi=[]
    for a in (x.lo,x.hi):
      for b in (y.lo,y.hi):
        lo.append(directed(a,b,lambda c,d:c*d,ROUND_FLOOR));hi.append(directed(a,b,lambda c,d:c*d,ROUND_CEILING))
    return Interval(min(lo),max(hi))
def idivpos(x,y):
    if y.lo<=0:raise ValueError('positive denominator required')
    lo=[];hi=[]
    for a in (x.lo,x.hi):
      for b in (y.lo,y.hi):
        lo.append(directed(a,b,lambda c,d:c/d,ROUND_FLOOR));hi.append(directed(a,b,lambda c,d:c/d,ROUND_CEILING))
    return Interval(min(lo),max(hi))
def frac(n,d):
    with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=Decimal(n)/Decimal(d)
    with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=Decimal(n)/Decimal(d)
    return Interval(lo,hi)
@dataclass(frozen=True)
class AffI:ratio:Interval;translation:Interval
def aimul(a,b):return AffI(imul(a.ratio,b.ratio),iadd(imul(b.ratio,a.translation),b.translation))
def aiid():return AffI(Interval(1),Interval(0))
def run_aff(bit:int)->AffI:
    r=4+bit;q=2**(16+3*bit)
    return AffI(frac(9**(5+bit),q),frac(48*(9**r-8**r),q))
def fixed_interval(chosen,all_sites):
    base=mechanical_product(RUN_WEIGHT,RUN_LENGTH,False,run_aff(0),run_aff(1),aiid(),aimul)
    corr=Interval(0)
    for idx in chosen:
        pos,l,r=all_sites[idx];sign=-1 if (l,r)==(0,1) else 1
        pe=16*pos+3*prefix_ones(pos);pb=5*pos+prefix_ones(pos)
        term=imul(base.ratio,frac(OMEGA*(1<<pe),9**(pb+11)))
        corr=iadd(corr,term if sign>0 else ineg(term))
    return idivpos(iadd(base.translation,corr),isub(Interval(1),base.ratio))

def payload():
    assert CHART_BLOCKS==5*RUN_LENGTH+RUN_WEIGHT
    assert EXPANDING==4*RUN_LENGTH+RUN_WEIGHT
    assert EXPANDING%3==0
    ss=sites();positions=tuple(ss[i][0] for i in SELECTED_INDICES);assert positions==EXPECTED_POSITIONS
    base=mechanical_product(RUN_WEIGHT,RUN_LENGTH,False,run_letter(0,MODULUS),run_letter(1,MODULUS),identity(MODULUS),lambda x,y:x*y)
    assert base.exponent==A and base.odd==pow(3,K,MODULUS) and base.dyadic==pow(2,A,MODULUS)
    modified=(base.constant+sum(delta(ss[i],MODULUS) for i in SELECTED_INDICES))%MODULUS;assert modified==0
    canonical7=(3*pow(2,4*(CHART_BLOCKS-EXPANDING),7)*(pow(2,EXPANDING,7)-1))%7
    d7=(pow(2,4*CHART_BLOCKS-EXPANDING,7)-pow(9,CHART_BLOCKS,7))%7
    assert canonical7==d7==0
    rows=[];qs=[]
    for p in FACTORS:
        mod=p*p
        b=mechanical_product(RUN_WEIGHT,RUN_LENGTH,False,run_letter(0,mod),run_letter(1,mod),identity(mod),lambda x,y:x*y).constant
        c=(b+sum(delta(ss[i],mod) for i in SELECTED_INDICES))%mod
        d=(pow(2,A,mod)-pow(3,K,mod))%mod
        assert c%p==d%p==0 and (d//p)%p
        q=(c//p)*pow(d//p,-1,p)%p;qs.append(q)
        rows.append({'prime':p,'C_mod_p2':c,'D_mod_p2':d,'C_over_p_mod_p':c//p,'D_over_p_mod_p':d//p,'quotient_mod_p':q})
    qcrt=crt(FACTORS,qs)
    iv=fixed_interval(SELECTED_INDICES,ss);floor=int(iv.lo);assert floor==int(iv.hi)
    near=min(iv.lo-Decimal(floor),Decimal(floor+1)-iv.hi)
    orders=[order2(p) for p in FACTORS]
    return {
      'schema_version':1,'experiment_id':'X-8303',
      'critical_run_compression':{
        'chart_blocks':CHART_BLOCKS,'expanding_blocks':EXPANDING,
        'run_word_length':RUN_LENGTH,'run_word_weight':RUN_WEIGHT,
        'substitution':{'0':'01111','1':'011111'},
        'run_zero_summary':{'chart_length':5,'dyadic_exponent':16,'odd_exponent':10,'constant':48*(9**4-8**4)},
        'run_one_summary':{'chart_length':6,'dyadic_exponent':19,'odd_exponent':12,'constant':48*(9**5-8**5)},
        'commutator':{'sign_convention':'C_01-C_10','value':OMEGA,'factorization':'7*2^16*3^9'}},
      'automatic_factor_7':{'expanding_weight_mod_3':EXPANDING%3,'canonical_numerator_mod_7':canonical7,'denominator_mod_7':d7,'all_adjacent_run_deltas_divisible_by_7':all(delta(s,MODULUS)%7==0 for s in ss)},
      'run_repair':{
        'factor_product':MODULUS,'base_numerator_mod_product':base.constant,
        'selected_site_indices':list(SELECTED_INDICES),'selected_run_positions':list(positions),
        'selected_swap_count':len(SELECTED_INDICES),'modified_numerator_mod_product':modified,
        'fixed_point_lower':str(iv.lo),'fixed_point_upper':str(iv.hi),'interval_width':str(iv.hi-iv.lo),
        'unique_floor':floor,'distance_to_nearest_integer_lower_bound':str(near),
        'quotient_rows':rows,'crt_quotient_residue':qcrt,'floor_mod_product':floor%MODULUS,'ceil_mod_product':(floor+1)%MODULUS,
        'modular_nonintegrality':qcrt not in (floor%MODULUS,(floor+1)%MODULUS),
        'conclusion':'the frozen 46-run-swap word is not an integral cycle'},
      'order_cover':{'orders':orders,'lcm':math.lcm(*orders),'excess_window':A-K,'covers_word':math.lcm(*orders)>A-K},
      'boundaries':{'proved':['exact second Euclidean run compression','run-letter monomial commutator','automatic factor 7','46-run proper-factor repair','directed real and quotient-cylinder rejection'],'not_proved':['complete denominator factorization','prime-square-compatible repair','positive cycle','infinite ordinary chart path','Collatz counterexample']}}

def canonical_bytes(p):return (json.dumps(p,indent=2,sort_keys=True)+'\n').encode()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write-results',type=Path);ap.add_argument('--check-results',type=Path);a=ap.parse_args()
    data=canonical_bytes(payload());digest=hashlib.sha256(data).hexdigest()
    if a.write_results:a.write_results.parent.mkdir(parents=True,exist_ok=True);a.write_results.write_bytes(data)
    if a.check_results and a.check_results.read_bytes()!=data:raise SystemExit('canonical mismatch')
    print(data.decode(),end='');print('SHA256',digest)
if __name__=='__main__':main()
