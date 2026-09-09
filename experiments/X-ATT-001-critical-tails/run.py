#!/usr/bin/env python3
"""Exact finite regressions for ATT-001..006; no uniform-time certificate."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path

BASE='69b1ed57ce90fe8c9d6d7c80c69760a86eb0fd2a'
SCHEMA='X-ATT-001/v1'
SCOPE='finite arithmetic regressions and certified omitted-source mass; no all-time tightness or Collatz proof'
N=4096
SCALE=2**80
CLOCKS=(0,1,2,4,8,16,32,64,128)
THRESHOLDS=(1,16,256,4096,65536,16777216)

def need(p: bool, message: str)->None:
    if not p: raise ValueError(message)

def digest(x)->str:
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def frac(x: Fraction)->list[int]:return [x.numerator,x.denominator]

def vp(n:int,p:int)->int:
    n=abs(n);need(n>0,'valuation at zero');e=0
    while n%p==0:n//=p;e+=1
    return e

def step(n:int)->int:return (3*n+1)//2 if n&1 else n//2

def z(n:int,a:int)->int:return 3**a*(n+1)-2**a*(2*n+1)

def component(n:int,a:int)->int:
    v=z(n,a)
    return v*v//3**vp(v,3) if v else 0

@lru_cache(None)
def rank(n:int)->int:
    need(n>=1,'positive source')
    h=vp(2*n+1,3)
    return min(component(n,a) for a in ({0,1,2,h} if h>=3 else {0,1,2}))

@lru_cache(None)
def module(n:int)->tuple[int,int,int,int]:
    if n==1:return 1,-1,0,0
    a=vp(n+1,2) if n&1 else 0
    v=z(n,a);k=vp(v,2)//(a+1)
    need(k>=1,'empty active module')
    d,c=3**a-2**(a+1),3**a-2**a
    y=(3**(a*k)*(v//2**((a+1)*k))-c)//d
    need((y+5)**4<=(n+5)**9,'height ceiling')
    return y,a,k,(a+1)*k

def safe(n:int)->bool:return n>1 and 4*rank(module(n)[0])<=rank(n)

@lru_cache(None)
def unsafe_return(n:int)->tuple[int,int,int]:
    need(n>1 and not safe(n),'unsafe domain')
    y,_,_,clock=module(n);g=0
    while safe(y):
        old=rank(y);y,_,_,length=module(y);clock+=length;g+=1
        need(4*rank(y)<=old,'safe descent')
    need(rank(y)<=rank(module(n)[0]),'return rank bound')
    return y,g,clock

def interval(lo:int,terms:int)->list[list[int]]:
    return [frac(Fraction(lo,SCALE)),frac(Fraction(lo+terms,SCALE)+Fraction(43,N*N))]

def ordinary():
    rows=[]
    for cut in (2,8,32,128,512,1024):
        values=[SCALE//rank(n)**2 for n in range(cut+1,N+1)]
        v=interval(sum(values),len(values));e=0
        while 3**e<=cut:e+=1
        p=3**e
        need(rank(p)==p and p<=3*cut,'ordinary tail lower source')
        need(Fraction(*v[1])<=Fraction(43,cut*cut),'finite enclosure under global upper')
        rows.append({'cut':cut,'enclosure':v,'lower_source':p,'lower_weight':frac(Fraction(1,p*p))})
    return rows

def census():
    records=[];modes=Counter();unsafe=0;maxg=0;maxclock=0
    for n in range(2,N+1):
        r=rank(n);y,a,k,length=module(n);s=rank(y)
        need(n-1<=r<=n*n,'rank bounds')
        modes[a]+=1
        if not safe(n):
            endpoint,g,clock=unsafe_return(n);unsafe+=1;maxg=max(maxg,g);maxclock=max(maxclock,clock)
        else:endpoint,g,clock=None,None,None
        records.append([n,r,y,a,k,length,s,endpoint,g,clock])
    return {'sources':N-1,'unsafe_sources':unsafe,'active_modes':dict(sorted(modes.items())),
            'maximum_safe_modules_in_return':maxg,'maximum_observed_shortcut_clock':maxclock,
            'transcript_sha256':digest(records)}

def raw_tails():
    hist={(k,Y):[0,0] for k in CLOCKS for Y in THRESHOLDS}
    transcript=[]
    for n in range(2,N+1):
        x=n;wi=SCALE//rank(n)**2
        for k in range(max(CLOCKS)+1):
            if x==1:break
            if k in CLOCKS:
                r=rank(x);transcript.append([n,k,x,r])
                for Y in THRESHOLDS:
                    if r>Y:hist[k,Y][0]+=wi;hist[k,Y][1]+=1
            x=step(x)
    rows=[]
    for k in CLOCKS:
        for Y in THRESHOLDS:
            lo,count=hist[k,Y];v=interval(lo,count)
            bound=Fraction(77*9**k,4**k*Y)
            need(Fraction(*v[1])<=bound,'raw full-tail bound')
            rows.append({'clock':k,'rank_cut':Y,'enumerated_sources':count,'enclosure':v})
    return {'rows':rows,'transcript_sha256':digest(transcript)}

def induced_tails():
    hist={Y:[0,0] for Y in THRESHOLDS};records=[]
    for n in range(2,N+1):
        if safe(n):continue
        y,g,clock=unsafe_return(n)
        if y==1:continue
        r=rank(y);wi=SCALE//rank(n)**2;records.append([n,y,g,clock,r])
        for Y in THRESHOLDS:
            if r>Y:hist[Y][0]+=wi;hist[Y][1]+=1
    rows=[]
    for Y in THRESHOLDS:
        lo,count=hist[Y];v=interval(lo,count);upper=Fraction(*v[1])
        need(upper**9*Y**4<=200**9,'unsafe fractional-tail upper')
        rows.append({'rank_cut':Y,'enumerated_sources':count,'enclosure':v})
    return {'rows':rows,'transcript_sha256':digest(records)}

def fixed_clock_powers():
    rows=[]
    for k in (1,2,3,4,8,12,16):
        for extra in (0,1,3,8):
            e=2*k+2+extra;n=3**e;x=n;A=q=0;word=''
            for i in range(k):
                b=x&1;word+=str(b)
                if b:A=3*A+2**i;q+=1
                x=step(x)
            need(2**k*x==3**q*n+A and A&1,'affine/odd remainder')
            need(rank(n)==n and rank(x)*36**(k+1)>=n*n,'fixed-clock critical lower')
            need(n>2**k and x>1,'physical survival')
            rows.append({'clock':k,'e':e,'source':n,'endpoint':x,'word':word,'q':q,'A':A,
                         'endpoint_h':vp(2*x+1,3),'endpoint_rank':rank(x)})
    return rows

def clock_spikes():
    rows=[]
    for j in (2,4,6,8):
        t=2**j;M=3**t;n=4*M-5;a=j+4;m=(M-1)//2**(j+2)
        y=(3**a*m-1)//2
        need(module(n)==(y,a,1,a+1),'spike complete module')
        need(m%8==5 and vp(y,2)==1,'dyadic family')
        need(rank(n)==16*M and rank(y)==(y+5)**2//9,'family ranks')
        need(not safe(n) and not safe(y) and unsafe_return(n)[0]==y,'both unsafe')
        need(module(y)[0]==y//2 and rank(y//2)==(y//2-1)**2,'unsafe successor')
        need(1152*4**a*rank(y)>9**a*rank(n)**2,'growing weak moment')
        need((y+5)**4<=(n+5)**9,'all-mode bound in spike')
        u=2*y
        need(rank(u)==(u-1)**2,'even-clock endpoint rank')
        need(64*4**a*rank(u)>9**a*rank(n)**2,'even-clock weak lower')
        rows.append({'j':j,'t':t,'a':a,'source':n,'endpoint':y,'source_rank':rank(n),
                     'endpoint_rank':rank(y),'next_rank':rank(y//2),
                     'tail_cut':frac(Fraction(rank(y),2)),
                     'weak_moment_lower':frac(Fraction(rank(y),2*rank(n)**2)),
                     'even_clock':a,'even_endpoint':u,'even_rank':rank(u),
                     'even_weak_moment_lower':frac(Fraction(rank(u),2*rank(n)**2))})
    return rows

def limit_controls():
    # Shift on N>=1 with mass 2^-n: fixed clocks are tight; the entire family is not.
    shift=[]
    for cap in (2,8,32,128):
        for k in (0,1,cap,cap+1):
            mass=Fraction(1,2**max(0,cap-k))
            shift.append([cap,k,frac(mass)])
    return {'shift_tail_rows':shift,'shift_uniform_defect':[1,1],
            'two_cycle_escape_defect':[0,1],'two_cycle_cesaro_mass':[1,1],
            'model_scope':'separate deterministic models; not Collatz counterexamples'}

def build():
    need(3**17<2**27 and 3**2>2**3,'exact exponent bracket')
    return {'schema':SCHEMA,'scope':SCOPE,'base':BASE,'source_cutoff':N,'scale':SCALE,
            'ordinary_tail_constant':43,'raw_tail_constant':77,'unsafe_tail_constant':200,
            'ordinary_tails':ordinary(),'height_census':census(),'raw_tails':raw_tails(),
            'unsafe_tails':induced_tails(),'fixed_clock_powers':fixed_clock_powers(),
            'clock_change_spikes':clock_spikes(),'limit_controls':limit_controls()}

def main()->None:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);p.add_argument('--check',type=Path)
    args=p.parse_args();payload=json.loads(json.dumps(build()));report={'payload':payload,'sha256':digest(payload)}
    if args.check:need(json.loads(args.check.read_text())==report,'canonical report mismatch')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n')
    print(report['sha256']);print('GENERATOR PASS; finite checks, no uniform-time proof')
if __name__=='__main__':main()
