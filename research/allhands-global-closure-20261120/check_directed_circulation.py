#!/usr/bin/env python3
"""Literal positive paths and quotient circulations; no convergence premise."""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import argparse
import json

PIN = '6863d298187af8b2619efbf78cc4b0aa8e627393'
A = 31110
L = 3*A+120
M = 90*A+22

def require(ok, why):
    if not ok:
        raise ValueError(why)

def T(n):
    require(type(n) is int and n>0, 'positive integer input')
    return n//2 if n%2==0 else (3*n+1)//2

def target(y):
    return y%512==369 or y%16==3 or y%8==5 or y%32==23

def clock(y):
    if y%512==369: return 9
    if y%16==3: return 4
    if y%8==5: return 3
    if y%32==23: return 5
    raise ValueError('missing neighbor class')

class PathBuilder:
    def __init__(self, start):
        self.vertices=[start]
        self.kinds=[]
    def append(self, value, kind='O'):
        self.kinds.append(kind)
        self.vertices.append(value)
    def extend(self, other):
        require(self.vertices[-1]==other.vertices[0], 'path splice')
        self.kinds.extend(other.kinds)
        self.vertices.extend(other.vertices[1:])
    def bridge(self, y, reverse=False):
        c=clock(y)
        left=[y];right=[y-1]
        for _ in range(c):
            left.append(T(left[-1]));right.append(T(right[-1]))
        require(left[-1]==right[-1], 'neighbor merger endpoint')
        seq=left+list(reversed(right[:-1]))
        if reverse: seq.reverse()
        require(self.vertices[-1]==seq[0], 'neighbor bridge start')
        for z in seq[1:]:self.append(z)
    def validate(self, source):
        require(type(source) is int and source>0 and source%2==1, 'odd source')
        require(self.vertices[0]==3*source and self.vertices[-1]==source,'return endpoints')
        require(len(self.kinds)<=L, 'uniform return length')
        require(len(self.vertices)==len(self.kinds)+1, 'path encoding')
        triples=[]
        for x,y,k in zip(self.vertices,self.vertices[1:],self.kinds):
            require(type(x) is int and type(y) is int and x>0 and y>0,'positive vertices')
            require(x<=3*y and y<=3*x,'per-edge height ratio')
            if k=='V':
                require(x%2==1 and y==3*x, 'forward odd tripling')
                triples.append(x)
            else:
                require(k=='O' and (T(x)==y or T(y)==x), 'literal ordinary edge')
        return triples

def high_return(x):
    require(x%243==0 and x%2==1 and x>0,'high domain')
    u=x//243
    b=next(i for i in range(2,6) if (3**i*u)%16 in (3,5))
    a=next(i for i in range(6,10) if (3**i*u)%16 in (3,5))
    p=PathBuilder(3*x)
    for _ in range(6,a):p.append(3*p.vertices[-1],'V')
    p.bridge(3**a*u)
    for i in range(a,b,-1):
        h=3**(i-3)*u
        require(p.vertices[-1]==27*h-1,'high descent start')
        for z in (18*h-1,12*h-1,8*h-1):p.append(z)
        p.append(3*(8*h-1),'V')
        for z in (4*(9*h-1),2*(9*h-1),9*h-1,6*h-1,4*h-1,6*h-1,9*h-1):p.append(z)
    p.bridge(3**b*u,reverse=True)
    for _ in range(b,5):p.append(3*p.vertices[-1],'V')
    p.validate(x)
    return p

def choose_a(u,j):
    a0=next(a for a in range(j+1,j+487) if pow(2,a,729)*u%729==1)
    return next(a0+486*r for r in range(64) if target(pow(3,a0+486*r,512)*(u%512)%512))

def return_path(x):
    require(x>0 and x%2==1,'source domain')
    if x%243==0:return high_return(x)
    u=x;j=0
    while u%3==0:u//=3;j+=1
    require(j<=4,'low valuation')
    a=choose_a(u,j)
    require(j<a<=A,'bounded exponent')
    p=PathBuilder(3*x)
    for _ in range(j+1,a):p.append(3*p.vertices[-1],'V')
    p.bridge(3**a*u)
    for i in range(a):p.append(2**(i+1)*3**(a-i-1)*u-1)
    z=(2**a*u-1)//3
    require(3*z==p.vertices[-1] and z%243==0,'high splice')
    p.extend(high_return(z))
    for _ in range(a):p.append(T(p.vertices[-1]))
    require(p.vertices[-1]==u,'ordinary target')
    for _ in range(j):p.append(3*p.vertices[-1],'V')
    p.validate(x)
    return p

def congruence_facts():
    powers=[pow(2,a,729) for a in range(486)]
    units=[u for u in range(729) if u%3]
    require(len(set(powers))==486 and set(powers)==set(units),'primitive root mod 729')
    g=pow(3,486,512)
    groups=[]
    for r in (1,3,5,7):
        orbit=[r*pow(g,j,512)%512 for j in range(64)]
        require(len(set(orbit))==64,'binary orbit length')
        require(set(orbit)==set(range(r,512,8)),'full binary coset')
        require(any(target(y) for y in orbit),'neighbor class in every coset')
        groups.append({'class_mod8':r,'first_hit':next(j for j,y in enumerate(orbit) if target(y))})
    for u in range(1,16,2):
        require(any(3**j*u%16 in (3,5) for j in range(2,6)),'low high-case exponent')
        require(any(3**j*u%16 in (3,5) for j in range(6,10)),'upper high-case exponent')
    return {'ternary_units':486,'binary_cosets':groups,'high_cases':8}

def crt(a,m,b,n):
    return (a+m*((b-a)*pow(m,-1,n)%n))%(m*n)

def fixtures():
    sources={243*u for u in range(1,64,2)} | {5,7,13,17,19,23}
    cells=[(369,512),(3,16),(5,8),(23,32)]
    designed=0
    for a in list(range(1,9))+[12,16,24]:
        for r,mod in cells:
            u=crt(pow(2,-a,729),729,r*pow(3,-a,mod)%mod,mod)
            require(u>0 and u%2 and u%3,'designed unit source')
            require(target(pow(3,a,512)*u%512),'designed binary target')
            for j in range(min(a,5)):
                require(choose_a(u,j)<=a,'controlled fixture exponent')
                sources.add(3**j*u);designed+=1
    return sorted(sources),designed

class DSU:
    def __init__(self):self.p={}
    def find(self,x):
        if x not in self.p:self.p[x]=x
        p=self.p[x]
        if p!=x:self.p[x]=self.find(p)
        return self.p[x]
    def join(self,a,b):
        a=self.find(a);b=self.find(b)
        if a!=b:self.p[a]=b

def flow_check(paths,s):
    dsu=DSU()
    for source,p in paths:
        dsu.find(source);dsu.find(3*source)
        for x,y,k in zip(p.vertices,p.vertices[1:],p.kinds):
            dsu.find(x);dsu.find(y)
            if k=='O':dsu.join(x,y)
    flow=defaultdict(Fraction)
    for source,p in paths:
        w=Fraction(1,source**s)
        flow[dsu.find(source)]-=w;flow[dsu.find(3*source)]+=w
        for x,y,k in zip(p.vertices,p.vertices[1:],p.kinds):
            if k=='V':flow[dsu.find(x)]-=w;flow[dsu.find(y)]+=w
    require(all(v==0 for v in flow.values()),'component-quotient circulation')
    return {'exponent':s,'ordinary_quotient_vertices':len(flow),'all_divergences_zero':True}

def mutations(paths):
    source,p=paths[0]
    import copy
    rejected=0
    for mode in ('edge','endpoint','even_tripling'):
        bad=copy.deepcopy(p)
        if mode=='edge':bad.vertices[1]+=2
        elif mode=='endpoint':bad.vertices[-1]+=2
        else:
            bad.vertices=[3*source,6*source,source];bad.kinds=['O','V']
        try:bad.validate(source)
        except ValueError:rejected+=1
        else:raise ValueError('mutation unexpectedly accepted')
    return rejected

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
    facts=congruence_facts();sources,designed=fixtures();paths=[]
    edges=triples=maxlen=0
    for x in sources:
        p=return_path(x);vs=p.validate(x);paths.append((x,p))
        edges+=len(p.kinds);triples+=len(vs);maxlen=max(maxlen,len(p.kinds))
    rows=[flow_check(paths,s) for s in (0,1,2)]
    report={'status':'PASS','scope':'Finite literal positive paths and exact quotient circulations; universal statements use the accompanying proof and pinned source. No full Collatz proof.',
        'source_pr':146,'source_revision':PIN,'uniform_return_length':L,'affine_form_bound':M,
        'congruence_facts':facts,'designed_low_source_cases':designed,'distinct_sources':len(paths),
        'ordinary_or_tripling_edges':edges,'return_tripling_edges':triples,'maximum_fixture_return_length':maxlen,
        'quotient_flows':rows,'damaged_paths_rejected':mutations(paths),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    raw=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(raw)
    print(raw)

if __name__=='__main__':main()
