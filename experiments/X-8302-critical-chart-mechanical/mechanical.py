from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Callable

K = 3_149_971_404_836
A = 4_992_586_555_009
EXCESS = A-K
FACTORS = (7,191,281,28_591,136_398_329)
MODULUS = math.prod(FACTORS)
P_LO, Q_LO = 440_541_600_217, 753_110_839_881
P_HI, Q_HI = 80_448_749_305, 137_528_045_312
PR45_POSITIONS = (
 2,4,6,23,30,35,39,42,44,47,54,59,61,64,71,78,80,83,85,92,95,97,
 102,107,112,117,121,138,141,143,145,148,150,158,165,167,174,177,
 179,182,184,186,189,
)
PR45_FLOOR = 1_791_361_447_298_439_130_709_020
CHART_MASK_HI = 46_478
CHART_MASK_LO = 8_732_882_846_915_751_955
CHART_POSITIONS = (
 0,4,22,69,75,81,87,93,99,134,140,146,163,169,193,199,204,216,228,
 240,246,252,263,269,281,305,310,328,346,352,357,363,381,387,393,
 416,422,434,446,452,463,
)
CHART_FLOOR = 1_567_441_266_425_753_353_472_608
NCH=K//2
ACH=2*K-A
ECH=4*NCH-ACH
assert ECH==A and 2*NCH==K

@dataclass(frozen=True)
class Summary:
    length:int; valuation:int; odd:int; dyadic:int; constant:int; modulus:int
    def __mul__(self, other:'Summary')->'Summary':
        if self.modulus!=other.modulus: raise ValueError('modulus mismatch')
        m=self.modulus
        return Summary(self.length+other.length,self.valuation+other.valuation,
            self.odd*other.odd%m,self.dyadic*other.dyadic%m,
            (other.odd*self.constant+self.dyadic*other.constant)%m,m)

def identity(m:int)->Summary:return Summary(0,0,1%m,1%m,0,m)
def accel_letter(bit:int,m:int)->Summary:
    v=1+bit;return Summary(1,v,3%m,pow(2,v,m),1%m,m)
def chart_letter(bit:int,m:int)->Summary:
    e=4-bit;c=3*bit
    return Summary(1,e,9%m,pow(2,e,m),c%m,m)

def monoid_power(value, exponent:int, ident, multiply:Callable):
    result=ident;base=value
    while exponent:
        if exponent&1:result=multiply(result,base)
        base=multiply(base,base);exponent//=2
    return result

def mechanical_product(ones:int,length:int,upper:bool,zero,one,ident,multiply:Callable):
    if ones==0:return monoid_power(zero,length,ident,multiply)
    if ones==length:return monoid_power(one,length,ident,multiply)
    q,r=divmod(length,ones)
    if upper:
        z=multiply(one,monoid_power(zero,q-1,ident,multiply))
        o=multiply(one,monoid_power(zero,q,ident,multiply))
        return mechanical_product(r,ones,False,z,o,ident,multiply)
    z=multiply(monoid_power(zero,q-1,ident,multiply),one)
    o=multiply(monoid_power(zero,q,ident,multiply),one)
    return mechanical_product(r,ones,True,z,o,ident,multiply)

def mech_bit(ones:int,length:int,pos:int)->int:
    return ((pos+1)*ones)//length-(pos*ones)//length
def prefix_ones(ones:int,length:int,count:int)->int:
    return count*ones//length
def disjoint_sites(ones:int,length:int,count:int):
    out=[];prev=-2;pos=0
    while len(out)<count:
        left=mech_bit(ones,length,pos);right=mech_bit(ones,length,pos+1)
        if left!=right and pos>prev+1:
            out.append((pos,left,right));prev=pos
        pos+=1
    return out

def accel_delta(site,mod:int)->int:
    pos,left,right=site
    pref=(pos+1)+prefix_ones(EXCESS,K,pos+1)
    coeff=pow(3,K-pos-2,mod)
    if (left,right)==(0,1):return coeff*pow(2,pref,mod)%mod
    if (left,right)==(1,0):return -coeff*pow(2,pref-1,mod)%mod
    raise ValueError

def chart_prefix_exp(count:int)->int:return 4*count-prefix_ones(ACH,NCH,count)
def chart_delta(site,mod:int)->int:
    pos,left,right=site
    sign=-1 if (left,right)==(0,1) else 1
    return sign*21*pow(9,NCH-pos-2,mod)*pow(2,chart_prefix_exp(pos),mod)%mod
