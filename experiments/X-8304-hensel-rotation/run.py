#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext, getcontext
from pathlib import Path
from typing import Callable

K=3_149_971_404_836
A=4_992_586_555_009
CBL=K//2
EXP=2*K-A
RUN_LENGTH=CBL-EXP
RUN_WEIGHT=EXP-4*RUN_LENGTH
FACTORS=(7,191,281,28_591,136_398_329)
MODULUS=math.prod(FACTORS)
OMEGA=7*(2**16)*(3**9)
PREC=180
getcontext().prec=PREC
ROTATION=928_986
SELECTED_INDICES=(
0,1,2,3,11,13,14,15,16,17,18,20,22,23,24,27,28,29,32,35,36,
38,40,41,43,44,47,49,50,52,53,54,55,59,60,62,64,68,69,71,73,
75,79,80,83,89,92,93,94,96,97,100,101,102,105,108,109,120,
121,123,125,129,130,132,134,
)
EXPECTED_POSITIONS=(
0,7,16,25,94,111,120,129,138,146,155,172,190,198,207,233,242,
251,277,303,311,329,346,355,372,381,407,424,433,450,459,468,
477,511,520,537,555,590,598,616,633,650,685,694,720,772,798,
807,816,833,842,868,876,885,911,937,946,1042,1050,1068,1085,
1120,1128,1146,1163,
)

@dataclass(frozen=True)
class Summary:
    p:int;q:int;c:int;m:int
    def __mul__(self,o:'Summary')->'Summary':
        m=self.m
        if m!=o.m: raise ValueError('modulus mismatch')
        return Summary(self.p*o.p%m,self.q*o.q%m,(o.p*self.c+self.q*o.c)%m,m)

def ident(m:int)->Summary:return Summary(1%m,1%m,0,m)
def run_letter(bit:int,m:int)->Summary:
    r=4+bit;e=16+3*bit
    return Summary(pow(9,5+bit,m),pow(2,e,m),48*(pow(9,r,m)-pow(8,r,m))%m,m)
def monoid_power(v,n:int,one,mul:Callable):
    out=one
    while n:
        if n&1:out=mul(out,v)
        v=mul(v,v);n//=2
    return out
def mechanical_product(ones:int,length:int,upper:bool,zero,one,identity,mul:Callable):
    if ones==0:return monoid_power(zero,length,identity,mul)
    if ones==length:return monoid_power(one,length,identity,mul)
    q,r=divmod(length,ones)
    if upper:
        z=mul(one,monoid_power(zero,q-1,identity,mul))
        o=mul(one,monoid_power(zero,q,identity,mul))
        return mechanical_product(r,ones,False,z,o,identity,mul)
    z=mul(monoid_power(zero,q-1,identity,mul),one)
    o=mul(monoid_power(zero,q,identity,mul),one)
    return mechanical_product(r,ones,True,z,o,identity,mul)
def prefix_ones(n:int)->int:return n*RUN_WEIGHT//RUN_LENGTH
def run_bit(n:int)->int:return prefix_ones(n+1)-prefix_ones(n)
def sites(count:int=136):
    out=[];prev=-2;pos=0
    while len(out)<count:
        l,r=run_bit(pos),run_bit(pos+1)
        if l!=r and pos>prev+1:
            out.append((pos,l,r));prev=pos
        pos+=1
    return out
def run_delta(site,mod:int)->int:
    pos,l,r=site;sgn=-1 if (l,r)==(0,1) else 1
    pe=16*pos+3*prefix_ones(pos);pb=5*pos+prefix_ones(pos)
    return sgn*OMEGA*pow(2,pe,mod)*pow(9,CBL-pb-11,mod)%mod

class Interval:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=Decimal(lo);self.hi=Decimal(lo if hi is None else hi)
def directed(a,b,op,rounding):
    with localcontext() as c:c.prec=PREC;c.rounding=rounding;return op(a,b)
def iadd(x,y):return Interval(directed(x.lo,y.lo,lambda a,b:a+b,ROUND_FLOOR),directed(x.hi,y.hi,lambda a,b:a+b,ROUND_CEILING))
def ineg(x):return Interval(x.hi.copy_negate(),x.lo.copy_negate())
def isub(x,y):return iadd(x,ineg(y))
def imul(x,y):
    lo=[];hi=[]
    for a in (x.lo,x.hi):
        for b in (y.lo,y.hi):
            lo.append(directed(a,b,lambda c,d:c*d,ROUND_FLOOR))
            hi.append(directed(a,b,lambda c,d:c*d,ROUND_CEILING))
    return Interval(min(lo),max(hi))
def idivpos(x,y):
    if y.lo<=0:raise ValueError('positive divisor required')
    lo=[];hi=[]
    for a in (x.lo,x.hi):
        for b in (y.lo,y.hi):
            lo.append(directed(a,b,lambda c,d:c/d,ROUND_FLOOR))
            hi.append(directed(a,b,lambda c,d:c/d,ROUND_CEILING))
    return Interval(min(lo),max(hi))
def frac(n:int,d:int):
    with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=Decimal(n)/Decimal(d)
    with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=Decimal(n)/Decimal(d)
    return Interval(lo,hi)
@dataclass(frozen=True)
class AffI:
    ratio:Interval;translation:Interval
def aimul(a:AffI,b:AffI)->AffI:return AffI(imul(a.ratio,b.ratio),iadd(imul(b.ratio,a.translation),b.translation))
def aiid():return AffI(Interval(1),Interval(0))
def run_aff(bit:int)->AffI:
    r=4+bit;q=2**(16+3*bit)
    return AffI(frac(9**(5+bit),q),frac(48*(9**r-8**r),q))
def initial_interval(ss):
    base=mechanical_product(RUN_WEIGHT,RUN_LENGTH,False,run_aff(0),run_aff(1),aiid(),aimul)
    den=isub(Interval(1),base.ratio);corr=Interval(0)
    for idx in SELECTED_INDICES:
        pos,l,r=ss[idx];sgn=-1 if (l,r)==(0,1) else 1
        pe=16*pos+3*prefix_ones(pos);pb=5*pos+prefix_ones(pos)
        term=idivpos(imul(base.ratio,frac(OMEGA*(1<<pe),9**(pb+11))),den)
        corr=iadd(corr,term if sgn>0 else ineg(term))
    return iadd(idivpos(base.translation,den),corr)
def quotient_rows(ss):
    rows=[];q={}
    for p in FACTORS:
        mod=p*p
        base=mechanical_product(RUN_WEIGHT,RUN_LENGTH,False,run_letter(0,mod),run_letter(1,mod),ident(mod),lambda x,y:x*y).c
        C=(base+sum(run_delta(ss[i],mod) for i in SELECTED_INDICES))%mod
        D=(pow(2,A,mod)-pow(3,K,mod))%mod
        if C%p or D%p or (D//p)%p==0:raise AssertionError('bad valuation')
        qp=(C//p)*pow(D//p,-1,p)%p;q[p]=qp
        rows.append({'prime':p,'C_mod_p2':C,'D_mod_p2':D,'quotient_mod_p':qp})
    return rows,q
def rotate(iv:Interval,q:dict[int,int],ss):
    changed={}
    for idx in SELECTED_INDICES:
        pos,l,r=ss[idx];changed[pos]=r;changed[pos+1]=l
    N=int(iv.lo)
    if int(iv.hi)!=N:raise AssertionError('initial interval crosses integer')
    flo=iv.lo-Decimal(N);fhi=iv.hi-Decimal(N)
    for pos in range(ROTATION):
        bit=changed.get(pos,run_bit(pos))
        P=9**(5+bit);Q=2**(16+3*bit);C=48*(9**(4+bit)-8**(4+bit))
        base,rem=divmod(P*N+C,Q)
        lo=directed(Decimal(rem),Decimal(P)*flo,lambda a,b:(a+b)/Decimal(Q),ROUND_FLOOR)
        hi=directed(Decimal(rem),Decimal(P)*fhi,lambda a,b:(a+b)/Decimal(Q),ROUND_CEILING)
        cl,ch=int(lo),int(hi)
        if cl!=ch:raise AssertionError(f'rounding ambiguity at {pos}')
        N=base+cl;flo=lo-cl;fhi=hi-ch
        for p in FACTORS:q[p]=((P*q[p]+C)*pow(Q,-1,p))%p
    return Interval(Decimal(N)+flo,Decimal(N)+fhi),N,q

def generate():
    if not (K%2==0 and EXP==2*K-A and 4*CBL-EXP==A):raise AssertionError
    ss=sites();positions=tuple(ss[i][0] for i in SELECTED_INDICES)
    if positions!=EXPECTED_POSITIONS:raise AssertionError('site mismatch')
    rows,q=quotient_rows(ss);iv=initial_interval(ss);floor0=int(iv.lo)
    if int(iv.hi)!=floor0:raise AssertionError
    matched0=[p for p in FACTORS if floor0%p==q[p]]
    riv,rfloor,rq=rotate(iv,dict(q),ss)
    if int(riv.hi)!=rfloor:raise AssertionError
    matched=[p for p in FACTORS if rfloor%p==rq[p]]
    if matched0!=[7,191] or matched!=[7,191,281]:raise AssertionError((matched0,matched))
    return {
      'schema_version':1,'experiment_id':'X-8304','rotation':ROTATION,
      'word':{'run_length':RUN_LENGTH,'run_weight':RUN_WEIGHT,'selected_count':len(SELECTED_INDICES),'selected_indices':list(SELECTED_INDICES),'selected_positions':list(positions)},
      'initial':{'fixed_point_lower':str(iv.lo),'fixed_point_upper':str(iv.hi),'width':str(iv.hi-iv.lo),'floor':floor0,'fraction_lower':str(iv.lo-floor0),'quotient_rows':rows,'matched_primes':matched0},
      'rotated':{'fixed_point_lower':str(riv.lo),'fixed_point_upper':str(riv.hi),'width':str(riv.hi-riv.lo),'floor':rfloor,'fraction_lower':str(riv.lo-rfloor),'quotient_residues':{str(p):rq[p] for p in FACTORS},'floor_residues':{str(p):rfloor%p for p in FACTORS},'matched_primes':matched,'remaining_mismatches':[p for p in FACTORS if p not in matched]},
      'interpretation':{'proved':['all five first-level factor divisibilities','real-floor/Hensel agreement at primes 7 and 191 before rotation','exact quotient transport under 928986 cyclic run shifts','real-floor/Hensel agreement at primes 7, 191, and 281 after rotation'],'not_proved':['integrality','the 28591 or 136398329 quotient digits','complete denominator divisibility','a positive Collatz cycle or counterexample']}}
def canonical_bytes(x):return (json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write-results',type=Path);ap.add_argument('--check-results',type=Path);a=ap.parse_args();data=canonical_bytes(generate());digest=hashlib.sha256(data).hexdigest()
    if a.write_results:a.write_results.parent.mkdir(parents=True,exist_ok=True);a.write_results.write_bytes(data)
    if a.check_results and a.check_results.read_bytes()!=data:raise SystemExit('canonical mismatch')
    print(data.decode(),end='');print('SHA256',digest)
if __name__=='__main__':main()
