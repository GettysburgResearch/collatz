"""Exact higher-start carry control and chronological charges without a maximum clock gap."""
from collections import Counter
from fractions import Fraction as F
import json
from check_cycle_rotations import necklaces,rational_labels


def need(ok,label):
    if not ok:raise ValueError(label)


def run(y,e,q,lag,c):
    p=len(e)
    ends=[i for i in range(p) if e[i]!=e[(i+lag)%p]]
    s=len(ends)
    if not 2<=s<=6:return
    c['rotations']+=1
    if (1<<sum(e))>2*3**p:c['clock_gap_above_one_bit']+=1
    if any(i==p-1 or (i+lag)%p==p-1 for i in ends):c['true_minimum_is_a_cut']+=1
    times=[i+1 for i in ends]
    translated=[(i+lag)%p+1 for i in ends]
    u=[];v=[]
    for j,k in enumerate(ends):
        start=ends[j-1]+1
        L=(k+1-start)%p
        em=min(e[k],e[(k+lag)%p])
        us=e[k]-em;vs=e[(k+lag)%p]-em
        u.append(us);v.append(vs)
        C=0;A=0
        for j2 in range(L):
            C=3*C+(1<<A)
            A+=em if j2==L-1 else e[(start+j2)%p]
        Y,Z=y[start%p],y[(start+lag)%p]
        need(Y!=Z and (Y-Z)%(1<<A)==0,'actual native separation')
        need((1<<(A+us))*y[(k+1)%p]==3**L*Y+q*C,'left full carry')
        need((1<<(A+vs))*y[(k+lag+1)%p]==3**L*Z+q*C,'right full carry')
        H=max(Y,Z);low=min(Y,Z)
        need((1<<A)<=H and 2*C<3**L*H,'entire higher-side complete relative carry')
        trueC=F(3**L*H+q*C,3**L*H)
        need(F(1)<=trueC<F(2+q,2),'high side uniform correction')
        c['higher_side_clock_tests']+=1
        c['lower_side_exceeds_higher_correction_bound']+=2*C>3**L*low
    for dates,pays in ((times,u),(translated,v)):
        prev=0;paid=0
        for i,k in enumerate(sorted(range(s),key=dates.__getitem__)):
            date=dates[k];paid+=pays[k]
            need((1<<(paid+date))*y[date%p] <=
                 3**date*(q+1)**(i+1)*(y[0]+q),'nonasymptotic charged prefix')
            gap=date-prev
            need((1<<(gap+pays[k]))*y[date%p] <=
                 3**gap*(q+1)**2*y[prev%p],'nonasymptotic charged consecutive row')
            prev=date
            c['shifted_chronological_prefixes']+=1
    for y1,e1 in zip(y,e):
        yn=(3*y1+q)//(1<<e1)
        need(2*(yn+q)<=3*(y1+q),'unselected shifted physical step')
        need((1<<e1)*(yn+q)<=3*(1+q)*(y1+q),'charged shifted physical step')


def main():
    c=Counter()
    for h in range(4,15):
        for w in necklaces(h):
            src=rational_labels(w)
            if src is None:continue
            lab,q,_=src
            idx=[i for i,b in enumerate(w) if b];p=len(idx)
            if p<2:continue
            e=[(idx[(j+1)%p]-t)%h for j,t in enumerate(idx)];y=[lab[t] for t in idx]
            root=y.index(min(y));e=e[root:]+e[:root];y=y[root:]+y[:root]
            for lag in range(1,p//2+1):
                run(y,e,q,lag,c)
            c['primitive_rational_cycles']+=1
    print(json.dumps(c,sort_keys=True,indent=2))


if __name__=='__main__':main()
