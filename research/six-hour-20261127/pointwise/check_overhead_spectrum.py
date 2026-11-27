"""Exhaustive fixed-pool spectra over all source valuations, with ordinary CRT witnesses."""
from functools import lru_cache
import json
from check_positive_anchors import odd_step
from check_extra_budget import PHASES,need

@lru_cache(None)
def cutoff(D):
    left=right=1
    lap=0
    while 17*(1<<D)*(7*lap+1)*left>=right or (7*lap+8)*2048>=(7*lap+1)*2187:
        left*=2048;right*=2187;lap+=1
    return lap

@lru_cache(None)
def matching_first_17(m,D):
    x=m;d=0;seen=set()
    for q in range(7*cutoff(D)):
        if x==17:
            return (q,d) if q%7==0 and d==11*(q//7)+D else None
        if x in seen:return None
        seen.add(x)
        x,e=odd_step(x,-1);d+=e
    return None

def orbit_after(n,steps):
    for _ in range(steps):n,_=odd_step(n)
    return n

def witness(h,s,item,t,a,h0):
    w,c,D,E,m,q,d=item
    k=max(q//7,1);R=7*k+a;H=11*k+h0
    mod=3**(s+h)
    Nrem=(-(w+1)*pow(2**(D+E),-1,3**h))%3**h
    z=(3**s*Nrem+17)*pow(2**(H+1),-1,mod)%mod or mod
    while True:
        n=(1<<(H+1))*z-17
        v=(1<<(D+E))*(n//3**s)+w
        need((v+1)%3**h==0 and n%3**s==0,('CRT',h,s,item,t))
        y=((v+1)<<h)//3**h-1
        if 0<y<n:break
        z+=mod
    target=2*3**R*z-t
    need(z%3!=0 and orbit_after(n,R)==target and orbit_after(y,R+s+h)==target,
         ('actual positive paths',h,s,t,n,y))
    return {'R':R,'z':z,'n':n,'visitor':y,'rank':s,'physical_signed_clock':d,
            'odd_signed_clock':q,'w':w,'c':c,'D':D,'E':E,'m':m}

def row(h):
    hits={};max_s=0;total=0;upper=(17*3**h-1)//2**h
    for w in range(1,upper+1,2):
        c=w;E=0;s=0;seen=set()
        while True:
            if c==1 and (1<<(E+1+h))>=3**(s+h):break
            need(c==1 or c not in seen,('unexpected nontrivial positive cycle',h,w,c))
            seen.add(c);c,e=odd_step(c);s+=1;E+=e
            max_s=max(max_s,s);total+=1;D=1
            while (1<<(D+E+h))<3**(s+h):
                m=(17<<D)-c
                if m>0:
                    sig=matching_first_17(m,D)
                    if sig is not None:hits.setdefault(s,[]).append((w,c,D,E,m,*sig))
                D+=1
    verified=0
    for s,items in hits.items():
        for t,a,h0 in PHASES:
            witness(h,s,items[0],t,a,h0);verified+=1
    res={'source_rank_set':sorted(hits),'last_inspected_rank':max_s,'ordinary_prefixes':total,
         'actual_CRT_witnesses_replayed':verified,'ordinary_pool_cutoff':upper}
    if hits:
        s=max(hits);res['last_rank_example_at_17']=witness(h,s,hits[s][0],17,0,0)
    return res

if __name__=='__main__':
    expected=[[],[],[],[1],[1,2,3],[1,2,3,4,7,9],list(range(1,10))+[25,27]]
    rows=[]
    for h,ss in enumerate(expected):
        r=row(h);need(r['source_rank_set']==ss,('spectrum',h,r));rows.append(r)
    print(json.dumps({'h_range':[0,6],'rows_in_h_order':rows},sort_keys=True,indent=2))
