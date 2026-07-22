from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from mechanical import (
    ACH, NCH, EXCESS, K, PR45_POSITIONS, chart_prefix_exp,
    disjoint_sites, mechanical_product,
)
PREC=145
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
    if y.lo<=0:raise ValueError
    lo=[];hi=[]
    for a in (x.lo,x.hi):
      for b in (y.lo,y.hi):
        lo.append(directed(a,b,lambda c,d:c/d,ROUND_FLOOR));hi.append(directed(a,b,lambda c,d:c/d,ROUND_CEILING))
    return Interval(min(lo),max(hi))
def frac_interval(num:int,den:int):
    with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=Decimal(num)/Decimal(den)
    with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=Decimal(num)/Decimal(den)
    return Interval(lo,hi)
@dataclass(frozen=True)
class AffI: ratio:Interval; translation:Interval
def aimul(left:AffI,right:AffI)->AffI:
    return AffI(imul(left.ratio,right.ratio),iadd(imul(right.ratio,left.translation),right.translation))
def aiid():return AffI(Interval(1),Interval(0))
def chart_aff_letter(bit:int)->AffI:
    return AffI(frac_interval(9,8 if bit else 16),frac_interval(3 if bit else 0,8 if bit else 16))
def accel_aff_letter(bit:int)->AffI:
    d=2**(1+bit);return AffI(frac_interval(3,d),frac_interval(1,d))
def fixed_interval_chart(selected_indices):
    base=mechanical_product(ACH,NCH,False,chart_aff_letter(0),chart_aff_letter(1),aiid(),aimul)
    delta=Interval(0);sites=disjoint_sites(ACH,NCH,80)
    for idx in selected_indices:
        pos,left,right=sites[idx];sign=-1 if (left,right)==(0,1) else 1
        factor=frac_interval(21*(1<<chart_prefix_exp(pos)),9**(pos+2));term=imul(base.ratio,factor)
        delta=iadd(delta,term if sign>0 else ineg(term))
    return idivpos(iadd(base.translation,delta),isub(Interval(1),base.ratio))
def fixed_interval_pr45():
    base=mechanical_product(EXCESS,K,False,accel_aff_letter(0),accel_aff_letter(1),aiid(),aimul)
    delta=Interval(0);sites=disjoint_sites(EXCESS,K,80);posmap={s[0]:i for i,s in enumerate(sites)}
    from mechanical import prefix_ones
    for pos in PR45_POSITIONS:
        _,left,right=sites[posmap[pos]];pref=(pos+1)+prefix_ones(EXCESS,K,pos+1)
        if (left,right)==(0,1):factor=frac_interval(1<<pref,3**(pos+2));term=imul(base.ratio,factor)
        else:factor=frac_interval(1<<(pref-1),3**(pos+2));term=ineg(imul(base.ratio,factor))
        delta=iadd(delta,term)
    return idivpos(iadd(base.translation,delta),isub(Interval(1),base.ratio))
