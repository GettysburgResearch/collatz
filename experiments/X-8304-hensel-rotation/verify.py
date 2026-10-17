#!/usr/bin/env python3
from __future__ import annotations
import json, math, sys
from dataclasses import dataclass
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec=220
K=3_149_971_404_836;A=4_992_586_555_009;CBL=K//2;EXP=2*K-A
RLEN=CBL-EXP;RWT=EXP-4*RLEN
FACTORS=(7,191,281,28_591,136_398_329);OMEGA=7*2**16*3**9
SEL=(0,1,2,3,11,13,14,15,16,17,18,20,22,23,24,27,28,29,32,35,36,38,40,41,43,44,47,49,50,52,53,54,55,59,60,62,64,68,69,71,73,75,79,80,83,89,92,93,94,96,97,100,101,102,105,108,109,120,121,123,125,129,130,132,134)
ROT=928_986

def pref(n):return n*RWT//RLEN
def bit(n):return pref(n+1)-pref(n)
def sites(n=136):
    out=[];p=0;last=-2
    while len(out)<n:
        a,b=bit(p),bit(p+1)
        if a!=b and p>last+1:out.append((p,a,b));last=p
        p+=1
    return out
@dataclass(frozen=True)
class S:
    p:int;q:int;c:int;m:int
    def mul(self,o):
        m=self.m;return S(self.p*o.p%m,self.q*o.q%m,(o.p*self.c+self.q*o.c)%m,m)
def one(m):return S(1%m,1%m,0,m)
def letter(b,m):
    r=4+b;e=16+3*b;return S(pow(9,5+b,m),pow(2,e,m),48*(pow(9,r,m)-pow(8,r,m))%m,m)
def power(x,n):
    y=one(x.m)
    while n:
        if n&1:y=y.mul(x)
        x=x.mul(x);n//=2
    return y
def mech(o,l,u,z,a):
    if o==0:return power(z,l)
    if o==l:return power(a,l)
    q,r=divmod(l,o)
    if u:return mech(r,o,False,a.mul(power(z,q-1)),a.mul(power(z,q)))
    return mech(r,o,True,power(z,q-1).mul(a),power(z,q).mul(a))
def delta(site,m):
    p,l,r=site;sg=-1 if (l,r)==(0,1) else 1
    return sg*OMEGA*pow(2,16*p+3*pref(p),m)*pow(9,CBL-(5*p+pref(p))-11,m)%m

@dataclass(frozen=True)
class Aff:
    r:Decimal;t:Decimal
    def mul(self,o):return Aff(self.r*o.r,o.r*self.t+o.t)
def aone():return Aff(Decimal(1),Decimal(0))
def aletter(b):
    rr=4+b;q=Decimal(2)**(16+3*b)
    return Aff((Decimal(9)**(5+b))/q,(Decimal(48)*(Decimal(9)**rr-Decimal(8)**rr))/q)
def apower(x,n):
    y=aone()
    while n:
        if n&1:y=y.mul(x)
        x=x.mul(x);n//=2
    return y
def amech(o,l,u,z,a):
    if o==0:return apower(z,l)
    if o==l:return apower(a,l)
    q,r=divmod(l,o)
    if u:return amech(r,o,False,a.mul(apower(z,q-1)),a.mul(apower(z,q)))
    return amech(r,o,True,apower(z,q-1).mul(a),apower(z,q).mul(a))

def verify(data):
    ss=sites();assert [ss[i][0] for i in SEL]==data['word']['selected_positions']
    qv={}
    for p in FACTORS:
        m=p*p;base=mech(RWT,RLEN,False,letter(0,m),letter(1,m)).c
        C=(base+sum(delta(ss[i],m) for i in SEL))%m;D=(pow(2,A,m)-pow(3,K,m))%m
        assert C%p==D%p==0 and (D//p)%p
        qv[p]=(C//p)*pow(D//p,-1,p)%p
    assert qv=={r['prime']:r['quotient_mod_p'] for r in data['initial']['quotient_rows']}
    base=amech(RWT,RLEN,False,aletter(0),aletter(1));Dreal=Decimal(1)-base.r
    C=base.t
    for i in SEL:
        p,l,r=ss[i];sg=-1 if (l,r)==(0,1) else 1
        C += Decimal(sg)*base.r*Decimal(OMEGA)*(Decimal(2)**(16*p+3*pref(p)))/(Decimal(9)**(5*p+pref(p)+11))
    x=C/Dreal;lo=Decimal(data['initial']['fixed_point_lower']);hi=Decimal(data['initial']['fixed_point_upper'])
    assert lo<=x<=hi;N=int(x);assert N==data['initial']['floor']
    changed={}
    for i in SEL:
        p,l,r=ss[i];changed[p]=r;changed[p+1]=l
    for pos in range(ROT):
        b=changed.get(pos,bit(pos));P=9**(5+b);Q=2**(16+3*b);cc=48*(9**(4+b)-8**(4+b))
        x=(Decimal(P)*x+Decimal(cc))/Decimal(Q)
        for p in FACTORS:qv[p]=((P*qv[p]+cc)*pow(Q,-1,p))%p
    assert int(x)==data['rotated']['floor']
    assert qv=={int(p):v for p,v in data['rotated']['quotient_residues'].items()}
    assert [p for p in FACTORS if int(x)%p==qv[p]]==data['rotated']['matched_primes']
    assert Decimal(data['rotated']['fixed_point_lower'])<=x<=Decimal(data['rotated']['fixed_point_upper'])
    return {'verified':True,'modular_primes':len(FACTORS),'rotation_steps':ROT,'selected_sites':len(SEL),'initial_matches':data['initial']['matched_primes'],'rotated_matches':data['rotated']['matched_primes']}
if __name__=='__main__':
    path=Path(sys.argv[1] if len(sys.argv)>1 else 'results/canonical.json');data=json.loads(path.read_text());print(json.dumps(verify(data),sort_keys=True,indent=2))
