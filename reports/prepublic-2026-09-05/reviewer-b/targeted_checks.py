#!/usr/bin/env python3
"""Reviewer B's bounded regressions; not a Collatz or asymptotic certificate.

No author checker or repository module is imported. All-source mass coverage
is only for H=64 at finite times 0 and 19. The analytic tail is the audited
trapezoidal/convexity bound in PR92 ROUTE1_MELLIN.md, not an orbit heuristic.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib
import json

S=1<<96

def need(ok, why):
    if not ok: raise ValueError(why)

def step(n):
    return n//2 if n%2==0 else (3*n+1)//2

def vp(n,p):
    need(n!=0,'valuation zero')
    n=abs(n);e=0
    while n%p==0:n//=p;e+=1
    return e

def ceil(x):return -(-x.numerator//x.denominator)

def weight(n):return isqrt(S*S//(n**3))

def mass_check():
    # Tail from m in progression step d: integral+half endpoint,
    # with convex trapezoidal error <= (3d/16) m^(-5/2).
    def ap(a,d,N):
        vals=[weight(a+d*i) for i in range(N)]
        m=a+d*N
        root1=isqrt(S*S//m);root3=weight(m);root5=isqrt(S*S//m**5)
        lo=sum(vals)+ (F(2*root1,d)+F(root3,2)).__floor__()
        hi=sum(vals)+N+ceil(F(2*(root1+1),d)+F(root3+1,2)+F(3*d*(root5+1),16))
        return lo,hi
    total=ap(1,1,65536)
    # H64 odd-source eligibility is first y==2 mod3 with (2y-1)/3>64: 98.
    elig=ap(98,3,21846)
    known=set(range(1,65));fringe=known.copy();rows=[]
    for k in range(20):
        if k in (0,19):
            w=sum(weight(n) for n in known)
            en=[n for n in known if n>=98 and n%3==2]
            ew=sum(weight(n) for n in en)
            m=[total[0]-w-len(known),total[1]-w]
            q=[elig[0]-ew-len(en),elig[1]-ew]
            need(m[0]>0 and q[0]>0,'nonpositive enclosure')
            need(200*q[1]<69*m[0],'69/200 not certified at selected time')
            if k==19:need(3*q[0]>m[1],'one-third failure not certified')
            rows.append(dict(k=k,vertices=len(known),M_scaled=m,Q_scaled=q))
        if k<19:
            nxt=set()
            for y in fringe:
                nxt.add(2*y)
                if y%3==2:nxt.add((2*y-1)//3)
            nxt.discard(0)
            fringe=nxt-known;known.update(fringe)
    return dict(H=64,times=[0,19],scale=S,rows=rows,
                all_sources=True,all_times=False)

def small_checks():
    # 61/295 is rational; all numerator states are kept over the same odd denominator.
    seen=[];v=61
    while v not in seen:
        need(len(seen)<100,'unexpected rational period')
        seen.append(v);v=v//2 if v%2==0 else (3*v+295)//2
    need(seen.index(v)==13 and len(seen)-13==30 and min(seen)==61,'rational control')
    need(seen[10]==356 and 61%295!=0,'rational/ordinary boundary')
    def comp(n,a):
        z=3**a*(n+1)-2**a*(2*n+1)
        return 0 if z==0 else z*z//3**vp(z,3)
    def rank(n):return min(comp(n,a) for a in {0,1,2,vp(2*n+1,3)})
    def A(n):
        if n==1:return 1
        mode=0 if n%2==0 else vp(n+1,2)
        x=n
        for _ in range(100):
            y=x
            for bit in [1]*mode+[0]:
                if y%2!=bit:return x
                y=step(y)
            x=y
        raise ValueError('bounded regression cap exceeded')
    controls=[]
    for n in [3,7,9,81,103]:
        y=A(n)
        controls.append(dict(n=n,y=y,R=rank(n),Ry=rank(y),quarter_safe=4*rank(y)<=rank(n),nonincreasing_safe=rank(y)<=rank(n)))
    need(controls[0]['quarter_safe'] is False and controls[0]['nonincreasing_safe'] is True,'safe sets collapsed')
    need(controls[1]['Ry']>controls[1]['R'],'global rank counterexample')
    need(A(103)==175 and vp(176,2)==4,'future mode not forced')
    # Exact constants used in distinct contracts.
    need(F(1,20)+F(64,147)<F(1,2),'PR91 charged constant')
    need(8*3125**24<3456**24,'orbit cylinder Chernoff constant')
    need(F(177,500)+F(69,200)*F(463,250)<F(993,1000),'Mellin contraction constant')
    return dict(rational_preperiod=13,rational_period=30,rank_controls=controls,
                constants_checked=3,A0_first_crossing_interval='empty: 0<=d<0; log cutoff undefined')

def main():
    payload=dict(scope='reviewer-authored finite regressions; no global termination inference',mass=mass_check(),small=small_checks())
    text=json.dumps(payload,sort_keys=True,separators=(',',':'))
    report=dict(payload=payload,sha256=hashlib.sha256(text.encode()).hexdigest())
    out=Path(__file__).with_name('targeted-checks.json')
    if out.exists():need(json.loads(out.read_text())==report,'review regression changed')
    else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print('PASS reviewer-targeted checks',report['sha256'])
    print('H64 k19 inverse vertices:',payload['mass']['rows'][-1]['vertices'])

if __name__=='__main__':main()
