#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math, sys
from fractions import Fraction
from pathlib import Path
sys.set_int_max_str_digits(0)
NTERMS=230
C=748_000_000

class I:
    def __init__(self,a,b):
        if not a<b: raise ValueError
        self.a,self.b=a,b

def log_unit(y:Fraction)->I:
    z=(y-1)/(y+1); z2=z*z; p=z; s=Fraction(0)
    for j in range(NTERMS):
        s += 2*p/(2*j+1); p*=z2
    tail=2*p/((2*NTERMS+1)*(1-z2))
    return I(s,s+tail)

def logq(x:Fraction)->I:
    if x<=0: raise ValueError
    l2=log_unit(Fraction(2))
    if x==2: return l2
    e=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/(2**e) if e>=0 else x*2**(-e)
    while y<1:e-=1;y*=2
    while y>=2:e+=1;y/=2
    c=I(Fraction(0), Fraction(1,10**200)) if y==1 else log_unit(y)
    if e>=0:return I(e*l2.a+c.a,e*l2.b+c.b)
    return I(e*l2.b+c.a,e*l2.a+c.b)
L2=logq(Fraction(2));L3=logq(Fraction(3))
cache={2:L2,3:L3}
def lint(n):
    if n not in cache:cache[n]=logq(Fraction(n))
    return cache[n]

def semantic(x):
    y=dict(x);y.pop('semantic_sha256',None)
    return hashlib.sha256(json.dumps(y,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def eta(A,k):
    return I((k*L3.a-A*L2.b)/L2.b,(k*L3.b-A*L2.a)/L2.a)
def cf(x,stop):
    original=x;lo,hi=x.a,x.b;p2,p1=0,1;q2,q1=1,0;out=[]
    for idx in range(300):
        u=lo.numerator//lo.denominator;v=hi.numerator//hi.denominator
        if u!=v:raise AssertionError('cf unresolved')
        p=u*p1+p2;q=u*q1+q2;z=Fraction(p,q)
        side='below' if z<original.a else 'above' if z>original.b else None
        if side is None:raise AssertionError('cf inside')
        out.append({'index':idx,'a':u,'p':p,'q':q,'side':side})
        if q>stop:return out
        lo,hi=1/(hi-u),1/(lo-u);p2,p1=p1,p;q2,q1=q1,q
    raise AssertionError

def span(s,k,r):return ((s-1)*k*r)//s
def product(A,k,s,r):return 2**(A*r+s)*3**(k*r)>10**(k*r)
def floor_eta(E,r):
    x=E.a*r;y=E.b*r;a=x.numerator//x.denominator;b=y.numerator//y.denominator
    if a!=b:raise AssertionError('floor eta')
    return a
def direct(A,k,c,s,r,E):
    t=max(s,floor_eta(E,r)+1)
    return 2**(A*r+t)-3**(k*r)>=c*2**t*3**span(s,k,r),t

def verify_family(rec):
    A=int(rec['A']);k=int(rec['k']);c=int(rec['cmax']);lo,hi=map(int,rec['support_range'])
    E=eta(A,k); rows=cf(E,200_000_000_000)
    if rows!=rec['continued_fraction_rows']:raise AssertionError('cf rows')
    s=hi;rho=Fraction(s-1,s);rate=A*L2.a-rho*k*L3.b;K=C*L2.b*L3.b;R=200_000_000_000
    margin=R*rate-lint(2*c).b-K*(1+lint(k*R+1).b)
    deriv=rate-K*Fraction(k,k*R+1)
    if margin<=0 or deriv<=0:raise AssertionError('matveev')
    for sr in rec['supports']:
        s=int(sr['support']); R0=int(sr['legendre_start']); h=int(sr['floor_period']); delta=int(sr['period_span_increment'])
        if (R0+h)*3**delta>=R0*2**(A*h):raise AssertionError('period ratio')
        for r in range(R0,R0+h):
            if not 2**(A*r)>6*c*r*3**span(s,k,r):raise AssertionError('legendre base')
        got={int(x['r']):x for x in sr['finite_repetitions']}
        if set(got)!=set(range(1,R0)):raise AssertionError('finite coverage')
        for r,row in got.items():
            if row['gate']=='nontrivial-product':
                if not product(A,k,s,r):raise AssertionError('product')
            elif row['gate']=='minimal-positive-total-pulse':
                ok,t=direct(A,k,c,s,r,E)
                if not ok or t!=int(row['t0']):raise AssertionError('direct')
            else:raise AssertionError('gate label')
        ordmap={(int(x['p']),int(x['q'])):x for x in sr['ordinary_upper_convergents']}
        exmap={(int(x['p']),int(x['q'])):x for x in sr['exceptional_upper_convergents']}
        expected=[]
        for idx,row in enumerate(rows[:-1]):
            if row['side']=='above' and int(row['q'])<200_000_000_000:
                expected.append((int(row['p']),int(row['q']),int(rows[idx+1]['q'])))
        if set((p,q) for p,q,_ in expected)!=set(ordmap)|set(exmap):raise AssertionError('upper partition')
        for p,q,qn in expected:
            m=A*q*L2.a-span(s,k,q)*L3.b-lint(4*c*(q+qn)).b
            if (p,q) in ordmap:
                if m<=0:raise AssertionError('ordinary cf')
            else:
                x=exmap[(p,q)];m0=int(x['minimum_multiple']);hp=int(x['residue_period'])
                if m0!=max((s+p-1)//p,(s+k*q-1)//(k*q)):raise AssertionError('m0')
                d=((s-1)*k*q*hp)//s
                if 3**d>=2**(A*q*hp):raise AssertionError('exception period')
                if len(x['base_rows'])!=hp:raise AssertionError('exception rows')
                for br in x['base_rows']:
                    mm=int(br['m']);sp=span(s,k,q*mm)
                    mmargin=2**((A*q+p)*mm)-3**(k*q*mm)-c*2**(p*mm)*3**sp
                    if mmargin<=0 or hashlib.sha256(str(mmargin).encode()).hexdigest()!=br['margin_sha256']:
                        raise AssertionError('exception margin')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('result');args=ap.parse_args()
    x=json.loads(Path(args.result).read_text())
    if semantic(x)!=x['semantic_sha256']:raise SystemExit('semantic digest')
    for f in x['families']:verify_family(f)
    print('LIT-X-0065 INDEPENDENT VERIFICATION PASSED')
    print(x['semantic_sha256'])
if __name__=='__main__':main()
