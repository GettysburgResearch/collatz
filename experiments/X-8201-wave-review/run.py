#!/usr/bin/env python3
from __future__ import annotations
import hashlib, itertools, json, math
from dataclasses import dataclass
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING

A=4_992_586_555_009
K=3_149_971_404_836
ONES=A-K
FACTORS=(7,191,281,28_591,136_398_329)
M=math.prod(FACTORS)
MASK0=679_923_852_302
MASK1=1_092_615_932_587
EXPECTED=(2,4,6,23,30,35,39,42,44,47,54,59,61,64,71,78,80,83,85,92,95,97,102,107,112,117,121,138,141,143,145,148,150,158,165,167,174,177,179,182,184,186,189)
SOURCE_LO=Decimal("1791361447298439130709020.99752835390985101078597115625463997678316699077019108974634764751200085257269769107803891195190")
SOURCE_HI=Decimal("1791361447298439130709020.99752835390985101078597115625463997678316699077019108974634764751200085455151399874064825798230")
PREC=170

def sha(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

@dataclass(frozen=True)
class S:
    k:int; A:int; p:int; q:int; c:int; m:int

def mul(x:S,y:S)->S:
    assert x.m==y.m
    m=x.m
    return S(x.k+y.k,x.A+y.A,x.p*y.p%m,x.q*y.q%m,(y.p*x.c+x.q*y.c)%m,m)

def oneS(m): return S(0,0,1%m,1%m,0,m)
def bitS(b,m): return S(1,1+b,3%m,pow(2,1+b,m),1%m,m)

def power(x,n,identity,mulfn):
    out=identity
    while n:
        if n&1: out=mulfn(out,x)
        x=mulfn(x,x); n//=2
    return out

def mech(p,q,upper,x0,x1,identity,mulfn):
    if p==0:return power(x0,q,identity,mulfn)
    if p==q:return power(x1,q,identity,mulfn)
    a,s=divmod(q,p)
    if upper:
        z0=mulfn(x1,power(x0,a-1,identity,mulfn))
        z1=mulfn(x1,power(x0,a,identity,mulfn))
        return mech(s,p,False,z0,z1,identity,mulfn)
    z0=mulfn(power(x0,a-1,identity,mulfn),x1)
    z1=mulfn(power(x0,a,identity,mulfn),x1)
    return mech(s,p,True,z0,z1,identity,mulfn)

def mech_bit(i): return ((i+1)*ONES)//K-(i*ONES)//K
def prefixA(n): return n+(n*ONES)//K

def sites(n):
    out=[]; last=-2; i=0
    while len(out)<n:
        l,r=mech_bit(i),mech_bit(i+1)
        if l!=r and i>last+1:
            out.append((i,l,r,prefixA(i+1))); last=i
        i+=1
    return out

def delta(site,mod):
    i,l,r,p=site; coeff=pow(3,K-i-2,mod)
    if (l,r)==(0,1): return coeff*pow(2,p,mod)%mod
    return (-coeff*pow(2,p-1,mod))%mod

class I:
    def __init__(self,lo,hi=None):
        self.lo=Decimal(lo); self.hi=Decimal(lo if hi is None else hi)

def op(a,b,fn,rounding):
    with localcontext() as c:
        c.prec=PREC;c.rounding=rounding
        return fn(a,b)
def add(x,y):return I(op(x.lo,y.lo,lambda a,b:a+b,ROUND_FLOOR),op(x.hi,y.hi,lambda a,b:a+b,ROUND_CEILING))
def neg(x):return I(x.hi.copy_negate(),x.lo.copy_negate())
def sub(x,y):return add(x,neg(y))
def prod(x,y):
    lo=[];hi=[]
    for a in (x.lo,x.hi):
      for b in (y.lo,y.hi):
        lo.append(op(a,b,lambda c,d:c*d,ROUND_FLOOR));hi.append(op(a,b,lambda c,d:c*d,ROUND_CEILING))
    return I(min(lo),max(hi))
def divpos(x,y):
    assert y.lo>0
    lo=[];hi=[]
    for a in (x.lo,x.hi):
      for b in (y.lo,y.hi):
        lo.append(op(a,b,lambda c,d:c/d,ROUND_FLOOR));hi.append(op(a,b,lambda c,d:c/d,ROUND_CEILING))
    return I(min(lo),max(hi))
def fracI(a,b):
    with localcontext() as c:c.prec=PREC;c.rounding=ROUND_FLOOR;lo=Decimal(a)/Decimal(b)
    with localcontext() as c:c.prec=PREC;c.rounding=ROUND_CEILING;hi=Decimal(a)/Decimal(b)
    return I(lo,hi)
@dataclass(frozen=True)
class AF:
    r:I;t:I

def afmul(x,y): return AF(prod(y.r,x.r),add(prod(y.r,x.t),y.t))
def afbit(b):return AF(fracI(3,1<<(1+b)),fracI(1,1<<(1+b)))
def afone():return AF(I(1),I(0))
def selected():return [i for i in range(40) if (MASK0>>i)&1]+[40+i for i in range(40) if (MASK1>>i)&1]

def interval_fixed(st,sel):
    base=mech(ONES,K,False,afbit(0),afbit(1),afone(),afmul)
    dc=I(0)
    for ix in sel:
        pos,l,r,p=st[ix]
        term=prod(base.r,fracI(1<<(p if (l,r)==(0,1) else p-1),3**(pos+2)))
        dc=add(dc,term if (l,r)==(0,1) else neg(term))
    return divpos(add(base.t,dc),sub(I(1),base.r))

def minima(st,sel):
    changes={}
    for ix in sel:
        pos,l,r,_=st[ix];changes[pos]=r;changes[pos+1]=l
    affected=set()
    for p in changes: affected|={p,p+1}
    def b(i):return mech_bit(i%K)
    def f(i):return changes.get(i%K,b(i))
    before=sum(b(i-1)==1 and b(i)==0 for i in affected)
    after=sum(f(i-1)==1 and f(i)==0 for i in affected)
    return K-ONES+after-before

def isprime(n):
    if n<2:return False
    for p in range(2,math.isqrt(n)+1):
        if n%p==0:return n==p
    return True

def pr45():
    assert math.gcd(ONES,K)==1
    assert all(isprime(p) for p in FACTORS)
    assert all(pow(2,A,p)==pow(3,K,p) for p in FACTORS)
    base=mech(ONES,K,False,bitS(0,M),bitS(1,M),oneS(M),mul)
    assert (base.k,base.A)==(K,A)
    st=sites(80);sel=selected();positions=tuple(st[i][0] for i in sel)
    assert positions==EXPECTED
    residue=base.c
    for ix in sel:residue=(residue+delta(st[ix],M))%M
    assert residue==0
    fixed=interval_fixed(st,sel)
    n=int(fixed.lo)
    assert n==int(fixed.hi) and fixed.lo>n and fixed.hi<n+1
    minc=minima(st,sel)
    small=0
    for q in range(1,80):
      for p in range(q+1):
        lo=[((j+1)*p)//q-(j*p)//q for j in range(q)]
        up=[math.ceil((j+1)*p/q)-math.ceil(j*p/q) for j in range(q)]
        mlo=mech(p,q,False,"0","1","",lambda x,y:x+y)
        mup=mech(p,q,True,"0","1","",lambda x,y:x+y)
        assert mlo==''.join(map(str,lo)) and mup==''.join(map(str,up));small+=2
    with localcontext() as c:
        c.prec=80
        err=Decimal(A)/Decimal(K)-(Decimal(3).ln()/Decimal(2).ln())
        threshold=Decimal(1)/(Decimal(3)*Decimal(2).ln()*err)
    overlap=not(fixed.lo>SOURCE_HI or SOURCE_LO>fixed.hi)
    assert overlap and n==int(SOURCE_LO)
    return {"target":{"k":K,"A":A,"gcd_extra_length":math.gcd(ONES,K),"critical_error":str(err),"elementary_implied_X":str(threshold)},"factors":{"all_prime":True,"product":M,"all_divide_D":True},"mechanical":{"base_residue":base.c,"small_lower_upper_words":small},"repairs":{"sites":80,"swaps":len(sel),"positions":list(positions),"modified_residue":residue,"local_minima":minc},"real_filter":{"recomputed_lo":str(fixed.lo),"recomputed_hi":str(fixed.hi),"recomputed_width":str(fixed.hi-fixed.lo),"recomputed_floor":n,"recomputed_distance_next":str(Decimal(n+1)-fixed.hi),"source_lo":str(SOURCE_LO),"source_hi":str(SOURCE_HI),"source_floor":int(SOURCE_LO),"source_and_recomputed_overlap":overlap,"verdict":"frozen numeric interval independently reproduced and excludes integrality"}}

def shortcut(n):return n//2 if n%2==0 else (3*n+1)//2
def targets(r,m):
    n=r if r>0 else m
    return {shortcut(n+t*m)%m for t in (0,1)}
def sanctuary(maxm=220):
    total=0
    for m in range(1,maxm+1):
      adj=[targets(r,m) for r in range(m)]
      for s in range(m):
        seen={s};stack=[s]
        while stack:
          v=stack.pop()
          for w in adj[v]:
            if w not in seen:seen.add(w);stack.append(w)
        assert 1%m in seen;total+=1
    for b in range(1,20):
        mod=3**b;u=1+3**(b-1)
        assert pow(2,3**(b-1),mod)==mod-1
        for x in range(min(mod,100)):
            cn=(pow(3,b,mod)*x+(pow(3,b)-1)//2)%mod
            assert pow(2,u,mod)*cn%mod==1%mod
    return {"moduli":maxm,"starting_residues":total,"all_reach_one":True,"reset_levels":19}

def Aof(B):return 1792*B+3_657_472
def Eof(B):return 2816*B+5_792_512
def threshold(r):return 16*((611_319_808*r-224_512+53)//20_480+1)
def refund():
    rows=[]
    for r in range(1,33):
        B=threshold(r);margin=84*Aof(B)-53*(Eof(B+4096*r)+1)
        assert B%16==0 and margin>0
        assert 84*Aof(B-16)<=53*(Eof(B-16+4096*r)+1)
        rows.append({"lookahead":r,"threshold":B,"strict_margin":margin})
    assert rows[0]["threshold"]==477_424 and rows[1]["threshold"]==955_024
    import random
    rr=random.Random(0x820043);cases=0
    for _ in range(50000):
        q1=rr.randrange(2,500);q2=rr.randrange(2,500);p=rr.randrange(2*q2+1,6*q2+2)|1
        while math.gcd(p,q1)!=1:p+=2
        s=rr.randrange(q1);r0=rr.randrange(q1)
        y=(-s+r0)*pow(p,-1,q1)%q1;c=(s+p*y-r0)//q1
        assert c>=0
        k=rr.randrange(1,1000);yn=c+p*k;k2=yn//q2
        assert k2>=2*k;cases+=1
    b2=rows[1]["threshold"]
    return {"thresholds":rows,"two_stage":{"B":b2,"A":Aof(b2),"next2_E":Eof(b2+8192),"certificate":"3^A > 2^(E_next2+1) via 3^53>2^84","consequence":"k_next >= 2*k for every coherent path with k>=1"},"abstract_exact_cases":cases,"stage_word_residue_capacity_bits":512,"pair_capacity_bits":1024,"next_modulus_bits_at_first_threshold":Eof(477_424+4096)}

def main():
    payload={"reviewer":"gpt56-refund-01","frozen":{"pr45":"5d17926b48e29f94a935f1d433559b0c417cef55","pr42":"94fcd99fe7fb71e0f5a15915ba40e9d74b167a13","pr34":"86fa0aeb35a8b8c3dc405c4507877c3792194608"},"pr45":pr45(),"t8601":sanctuary(),"refund":refund()}
    payload["semantic_digest"]=sha(payload)
    print(json.dumps(payload,indent=2,sort_keys=True))
if __name__=='__main__':main()
