#!/usr/bin/env python3
"""Independent implementation: literal inverse stepping, no generator imports."""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path

BASE='b9a7b7ed0dd0cdf36d9dee578b1c75144ec9266d'
SCOPE='finite exact replay; all-parameter proofs PROPOSED; Collatz and total merging cover OPEN'

def check(ok: bool, why: str) -> None:
    if not ok: raise ValueError(why)

def code(x: object) -> bytes: return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def seal(x: object) -> str: return hashlib.sha256(code(x)).hexdigest()
def nu(x: int) -> int:
    check(x!=0,'undefined valuation');p=3; k=0
    while x%p==0:k+=1;p*=3
    return k

def P(x: int) -> int:
    check(x>0,'rank sign');m=2*x+1;d=1
    while m%(3*d)==0:d*=3
    return m*m//d

def T(x: int) -> int:
    if x&1:return (3*x+1)>>1
    return x//2

def walk(x: int, bits: str) -> int:
    for b in bits:
        check(str(x&1)==b,'wrong physical bit');x=T(x)
    return x

def undo(y: int, bits: str) -> int:
    x=Fraction(y)
    for b in reversed(bits):
        x=2*x if b=='0' else (2*x-1)/3
        check(x.denominator==1,'nonintegral reverse branch')
        check(int(x)%2==int(b),'wrong inverse parity')
    return int(x)

def predecessors(y: int) -> list[tuple[int,str,int]]:
    check(y%3==1 and y!=1,'section domain')
    h=nu(2*y+1);cur=2*y; suffix='0';out=[]
    while True:
        check(cur%3==2,'inverse continuation left class two')
        bits='0'+suffix
        out.append((2*cur,bits,h-bits.count('1')))
        if (2*cur-1)%3: break
        nxt=(2*cur-1)//3; suffix='1'+suffix
        if nxt%3==1:
            out.append((nxt,suffix,0));break
        if nxt%3==0:break
        check(abs(nxt)<abs(cur),'inverse odd chain failed to shorten')
        cur=nxt
    for x,w,_ in out:check(walk(x,w)==y,'inverse fan endpoint')
    return out

@lru_cache(None)
def negrows(r: int) -> tuple[tuple[int,int,int,str], ...]:
    pending=[(-2,0,'')];out={}
    at=0
    while at<len(pending):
        v,d,w=pending[at];at+=1
        check(v not in out,'negative cone duplicate')
        out[v]=(v,d,w.count('1'),w)
        if d<r:
            pending.extend((x,d+1,bits+w) for x,bits,_ in predecessors(v))
    return tuple(out[x] for x in sorted(out))

@lru_cache(None)
def threshold(r: int) -> int:
    return max(row[2]+nu(2*row[0]+1)+1 for row in negrows(r))

def cone(root: int, r: int, reduced: bool) -> tuple[dict[int,str],int,int]:
    # Physical fan enumeration; reductions based on explicit negative cones.
    words={root:''};levels=[root];kept=deleted=0
    for t in range(r):
        new=[]
        for v in levels:
            if v==1:continue
            for x,w,d in predecessors(v):
                if reduced and d>=threshold(r-t-1):deleted+=1;continue
                kept+=1
                if x not in words:words[x]=w+words[v];new.append(x)
        levels=new
    return words,kept,deleted

def minimum(nodes: dict[int,str]) -> int: return min(nodes,key=P)

def record(v: int, w: str) -> bool:
    # Recover every proper section prefix backwards from -2, independently
    # of the generator's forward test.
    end=w.count('1')+nu(2*v+1)
    if end<2:return False
    y=-2;q=0
    if nu(2*y+1)>=end:return False
    for i,b in enumerate(reversed(w)):
        y=2*y if b=='0' else (2*y-1)//3;q+=int(b)
        if i+1<len(w) and y%3==1 and q+nu(2*y+1)>=end:return False
    check(y==v,'record reconstruction')
    return True

def inverse(a: int,m: int) -> int:
    r0,r1=a,m;s0,s1=1,0
    while r1:
        q=r0//r1;r0,r1=r1,r0-q*r1;s0,s1=s1,s0-q*s1
    check(r0==1,'CRT inverse gcd');return s0%m

def unit(A: int,c: int,K: int,eps: int,lift: int) -> int:
    m=3**(K+1);r=((eps*3**K-c)*inverse(A,m))%m
    odd=r if r%2 else r+m
    return odd+2*m*lift

def make_family(v: int,w: str,j: int,extra: int,eps: int,lift: int) -> list[object]:
    k=len(w);q=w.count('1');hv=nu(2*v+1);d=q+hv
    K=1
    while 3**(j+q+K)<=4**(k+j+3):K+=1
    K+=extra
    u=unit(2**(k+j+2),(2*v+1)//3**hv,K,eps,lift)
    check(u>0 and u%2 and u%3,'CRT source unit')
    y=(3**(j+d)*u-1)//2
    x=undo(y,w+'0'+'1'*j+'0')
    check(x>0 and walk(x,w+'0'+'1'*j+'0')==y,'positive frontier path')
    check(nu(2*x+1)==hv+K and nu(2*y+1)==j+d,'frontier exact valuations')
    check(P(x)*4<P(y),'frontier decrease')
    check(Fraction(P(x),P(y))<Fraction(4**(k+j+2),3**(j+q+K)),'frontier bound')
    return [v,w,j,K,eps,lift,u,y,x,j+d,hv+K]

def reconstruct() -> tuple[dict,dict]:
    full={};table=[]
    for r in range(11):
        rows=negrows(r)
        for v,t,q,w in rows:
            check(walk(v,w)==-2,'negative actual path')
            check(abs(v)<=2*4**t and q<=t*t and nu(2*v+1)<=2*t+1,'symbolic bound control')
            check(abs(v)<=2**(len(w)-q+1),'negative height bound')
        check(threshold(r)<=(r+1)**2+1,'precision envelope')
        table.append([r,len(rows),threshold(r),max(row[2] for row in rows)])
    full['table']=table;full['shadow10']=[list(row) for row in negrows(10)]
    cases=[(n,r) for n in range(4,194,3) for r in range(1,7)]
    cases.extend(((3**h*u-1)//2,r) for h in (8,16,32,64,128,256) for u in (1,5,17) for r in (1,2,3,4,5))
    cases.extend([(208363,3),(29371,2),(121,8),(859,6)])
    comp=[]
    for n,r in cases:
        f,ef,_=cone(n,r,False);p,ep,deleted=cone(n,r,True)
        a,b=minimum(f),minimum(p)
        check(a==b,'full/reduced minimum mismatch')
        check(walk(a,f[a])==n and walk(b,p[b])==n,'minimizing certificates')
        comp.append([n,r,a,P(a),len(f),len(p),ef,ep,deleted,p[b]])
    full['comparisons']=comp
    guards=[]
    for r in range(6):
        for j in (0,2):
            for u in (1,5):
                for plus in (0,2):
                    d=threshold(r)+plus;y=(3**(j+d)*u-1)//2;s=4*y if j==0 else 2**(j+1)*3**d*u-2
                    actual,_,_=cone(s,r,False);mapped={}
                    for v,t,q,w in negrows(r):
                        x=undo(s,w)
                        check(x==v+2**(len(w)+j+1)*3**(d-q)*u,'shadow affine transport')
                        check(nu(2*x+1)==nu(2*v+1),'shadow precision threshold')
                        check(Fraction(P(x),P(y))>Fraction(64,3),'rank shield margin')
                        mapped[x]=w
                    check(set(actual)==set(mapped),'entire inverse ball isomorphism')
                    guards.append([r,j,u,d,y,len(actual),seal(sorted(mapped))])
    full['guard']=guards
    records=[(v,w) for v,t,q,w in negrows(8) if w and record(v,w)]
    fam=[make_family(v,w,j,e,eps,lift) for v,w in records for j in (0,2) for e in (0,2) for eps in (1,2) for lift in (0,1)]
    full['records']=[[v,w] for v,w in records];full['frontier']=fam
    delays=[]
    for d in range(2,7):
        N=3**(d-1);C=(4**N-1)//3**d
        check(nu(4**N-1)==d and C%3!=0,'4-power LTE certificate')
        K=1
        while 3**(K+1)<=4*16**N:K+=1
        for eps in (1,2):
            u=unit(4**N,-C,K,eps,0);y=(3**d*u-1)//2
            x=undo(y,'1'+'0'*(2*N-1))
            check(nu(2*x+1)==d+K-1 and P(x)*4<P(y),'delayed crossing')
            cur=y
            for i in range(1,N):
                cur*=4
                check(nu(2*cur+1)==1+nu(i) and P(cur)>P(y),'early even chain')
            delays.append([d,N,K,eps,y,x,2*N])
    full['delayed']=delays
    old={208363};layer={208363}
    for _ in range(3):
        layer={x for y in layer for x,w,d in predecessors(y) if d<=1};old.update(layer)
    f,_,_=cone(208363,3,False);p,_,_=cone(208363,3,True)
    check(min(old,key=P)==208363 and minimum(f)==4445077 and minimum(p)==4445077,'old/new pruning distinction')
    full['control']=[208363,len(old),len(f),len(p),4445077,p[4445077]]

    low=[];orbits=[];U=set()
    # Finite sublevel bound P(x)>=2x+1 proves this enumeration exhaustive.
    for x in range(1,122):
        if P(x)>=243:continue
        low.append(x);v=x;history=[];seen=set()
        while v not in seen:
            check(len(history)<128,'finite control bound');seen.add(v);history.append(v);v=T(v)
        check(v in (1,2),'nontrivial sublevel loop');U.update(history);orbits.append([x,P(x),history])
    v=121;prefix=[]
    while v not in U:
        check(len(prefix)<128,'first meeting bound');prefix.append(v);v=T(v)
    check(len(prefix)==54 and v==40 and 121 not in U,'all possible witnesses tested')
    full['all_witness_121']={'lower_rank_sources':low,'orbits':orbits,'union':sorted(U),'prefix':prefix,'first_meeting':[54,40]}
    b={'schema':'X-AS7-001-v1','base':BASE,'scope':SCOPE,'precision_table':table,'negative_nodes':len(negrows(10)),
       'comparisons':len(comp),'comparison_rows_sha256':seal(comp),'complete_nodes_sum':sum(row[4] for row in comp),
       'pruned_nodes_sum':sum(row[5] for row in comp),'omitted_fan_edges_sum':sum(row[8] for row in comp),
       'guard_cases':len(guards),'guard_rows_sha256':seal(guards),'record_nodes':len(records),
       'frontier_cases':len(fam),'frontier_rows_sha256':seal(fam),'delayed_cases':len(delays),
       'delayed_bridge_steps':sum(row[-1] for row in delays),'control':full['control'],
       'all_witness_121':{'lower_rank_sources':low,'forward_union':sorted(U),'first_meeting':[54,40],'rows_sha256':seal(full['all_witness_121'])},
       'full_payload_sha256':seal(full)}
    return {'body':b,'sha256':seal(b)},full

def validate(report: dict, expected: dict) -> None:
    check(set(report)=={'body','sha256'},'report keys')
    check(report['sha256']==seal(report['body']),'report digest')
    check(report==expected,'mathematics or coverage differs from reconstruction')

def selftest(expected: dict) -> int:
    mutations=[lambda b:b.update(scope='Collatz proved'),lambda b:b.update(comparisons=1),
        lambda b:b['precision_table'][2].__setitem__(2,2),lambda b:b.update(record_nodes=1),
        lambda b:b['control'].__setitem__(4,208363),lambda b:b.update(omitted_fan_edges_sum=0),
        lambda b:b['all_witness_121']['lower_rank_sources'].remove(40),
        lambda b:b['all_witness_121'].__setitem__('first_meeting',[53,40])]
    for mutate in mutations:
        bad=copy.deepcopy(expected);mutate(bad['body']);bad['sha256']=seal(bad['body'])
        try:validate(bad,expected)
        except ValueError:continue
        raise ValueError('resealed false report accepted')
    return len(mutations)

def main() -> None:
    ap=argparse.ArgumentParser();ap.add_argument('report',type=Path);ap.add_argument('--self-test',action='store_true');ap.add_argument('--full-output',type=Path)
    args=ap.parse_args();expected,full=reconstruct();validate(json.loads(args.report.read_text()),expected)
    if args.full_output:args.full_output.write_bytes(code(full)+b'\n')
    print('INDEPENDENT IMPLEMENTATION REPLAY PASS',expected['sha256'])
    if args.self_test:print('RESEALED CORRUPT REPORTS REJECTED',selftest(expected))

if __name__=='__main__':main()
