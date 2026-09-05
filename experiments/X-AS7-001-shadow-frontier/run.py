#!/usr/bin/env python3
"""Finite exact checks for INVERSE_SHADOW_FRONTIER.md; no all-time conclusion."""
from __future__ import annotations
import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path

BASE = 'b9a7b7ed0dd0cdf36d9dee578b1c75144ec9266d'
SCOPE = 'finite exact replay; all-parameter proofs PROPOSED; Collatz and total merging cover OPEN'

def require(ok: bool, why: str) -> None:
    if not ok: raise ValueError(why)

def enc(x: object) -> bytes:
    return json.dumps(x, sort_keys=True, separators=(',', ':')).encode()

def sha(x: object) -> str: return hashlib.sha256(enc(x)).hexdigest()

def val(n: int) -> int:
    n = abs(n); require(n != 0, 'zero valuation')
    h=0
    while n%3 == 0: n//=3; h+=1
    return h

def rank(n: int) -> int:
    require(n > 0, 'rank requires positive integer')
    z=2*n+1
    return z*z//3**val(z)

def step(n: int) -> int: return (3*n+1)//2 if n%2 else n//2

def replay(n: int, w: str) -> int:
    for c in w:
        require(n%2 == int(c), 'physical word mismatch')
        n=step(n)
    return n

def fan(n: int) -> list[tuple[int,str,int]]:
    require(n%3 == 1 and n != 1, 'signed section input')
    h=val(2*n+1); u=(2*n+1)//3**h
    out=[(2**(j+1)*3**(h-j)*u-2, '0'+'1'*j+'0', h-j) for j in range(h)]
    z=2**h*u-1
    if z%3==1: out.append((z,'1'*h+'0',0))
    return out

@lru_cache(None)
def shadow(r: int) -> tuple[tuple[int,int,int,str], ...]:
    # Store source-to-root words, including the negative root at depth zero.
    data={-2:(0,'')}; layer=[-2]
    for d in range(1,r+1):
        nxt=[]
        for n in layer:
            suffix=data[n][1]
            for x,w,_ in fan(n):
                require(x <= -2, 'negative cone left negative integers')
                require(x not in data, 'negative cone repeated a state')
                data[x]=(d,w+suffix); nxt.append(x)
        layer=nxt
    return tuple(sorted((x,d,w.count('1'),w) for x,(d,w) in data.items()))

@lru_cache(None)
def cap(r: int) -> int:
    return 1+max(q+val(2*v+1) for v,d,q,w in shadow(r))

def ball(root: int, radius: int, prune: bool) -> tuple[dict[int,str],int,int]:
    # BFS: an earlier arrival leaves at least as much remaining radius.
    found={root:''}; layer=[root]; edges=omitted=0
    for level in range(radius):
        nxt=[]; B=cap(radius-level-1) if prune else 0
        for y in layer:
            if y==1: continue
            for x,w,gap in fan(y):
                if prune and gap>=B:
                    omitted+=1; continue
                edges+=1
                if x not in found:
                    found[x]=w+found[y]; nxt.append(x)
        layer=nxt
    return found,edges,omitted

def argmin(nodes: dict[int,str]) -> int: return min(nodes,key=rank)

def is_record(v: int, w: str) -> bool:
    final=w.count('1')+val(2*v+1)
    x=v; oddleft=w.count('1')
    # Proper ancestors in the shadow path viewed root-to-leaf are the later
    # section states in forward replay of v -> -2.
    for c in w:
        oddleft-=int(c); x=step(x)
        if x%3==1:
            if oddleft+val(2*x+1)>=final: return False
    return final>=2

def positive_unit(A: int, c: int, K: int, eps: int, lift: int) -> int:
    m=3**(K+1)
    u=((eps*3**K-c)*pow(A,-1,m))%m
    if u%2==0: u+=m
    u+=2*m*lift
    require(u>0 and u%2==1 and u%3!=0,'ordinary unit')
    return u

def frontier_case(v: int, w: str, j: int, Kextra: int, eps: int, lift: int) -> list[object]:
    k=len(w); q=w.count('1'); hv=val(2*v+1); d=q+hv
    c=(2*v+1)//3**hv; A=2**(k+j+2)
    K=1
    while 4*4**(k+j+2)>=3**(j+q+K): K+=1
    K+=Kextra
    u=positive_unit(A,c,K,eps,lift)
    y=(3**(j+d)*u-1)//2
    s=2**(j+1)*3**d*u-2
    x=2**(k+j+1)*3**hv*u+v
    require(x>0 and replay(x,w)==s,'frontier bridge to interior')
    tail='0'+'1'*j+'0'
    require(replay(s,tail)==y,'interior bridge')
    require(val(2*y+1)==j+d and val(2*x+1)==hv+K,'frontier depths')
    require(4*rank(x)<rank(y),'frontier rank drop')
    require(rank(x)*3**(j+q+K)<rank(y)*4**(k+j+2),'strict slope bound')
    return [v,w,j,K,eps,lift,u,y,x,j+d,hv+K]

def build() -> tuple[dict,dict]:
    full: dict[str,object]={}
    table=[]
    for r in range(11):
        rows=shadow(r)
        for v,t,q,w in rows:
            require(replay(v,w)==-2,'negative word')
            require(abs(v)<=2*4**t and q<=t*t and val(2*v+1)<=2*t+1,'universal shadow bounds')
            require(abs(v)<=2**(len(w)-q+1),'negative inverse height')
        require(cap(r)<=(r+1)**2+1,'quadratic precision bound')
        table.append([r,len(rows),cap(r),max(q for v,t,q,w in rows)])
    full['table']=table
    full['shadow10']=[list(row) for row in shadow(10)]

    root_cases=[(n,r) for n in range(4,194,3) for r in range(1,7)]
    root_cases += [((3**h*u-1)//2,r) for h in (8,16,32,64,128,256)
                   for u in (1,5,17) for r in (1,2,3,4,5)]
    root_cases += [(208363,3),(29371,2),(121,8),(859,6)]
    comparisons=[]
    for n,r in root_cases:
        f,ef,_=ball(n,r,False); p,ep,skip=ball(n,r,True)
        a,b=argmin(f),argmin(p)
        require(a==b,'pruning changed exact minimum')
        require(replay(a,f[a])==n and replay(b,p[b])==n,'minimum path')
        comparisons.append([n,r,a,rank(a),len(f),len(p),ef,ep,skip,p[b]])
    full['comparisons']=comparisons

    guard=[]
    for r in range(6):
        for j in (0,2):
            for u in (1,5):
                for plus in (0,2):
                    d=cap(r)+plus; y=(3**(j+d)*u-1)//2; s=2**(j+1)*3**d*u-2
                    nodes,_,_=ball(s,r,False); mapped={}
                    for v,t,q,w in shadow(r):
                        x=2**(len(w)+j+1)*3**(d-q)*u+v
                        require(replay(x,w)==s,'shadow map physical')
                        require(val(2*x+1)==val(2*v+1),'shadow precision')
                        require(3*rank(x)>64*rank(y),'shadow rank shield')
                        mapped[x]=w
                    require(set(mapped)==set(nodes),'shadow bijection coverage')
                    guard.append([r,j,u,d,y,len(nodes),sha(sorted(mapped))])
    full['guard']=guard

    records=[(v,w) for v,t,q,w in shadow(8) if w and is_record(v,w)]
    families=[frontier_case(v,w,j,extra,eps,lift) for v,w in records
              for j in (0,2) for extra in (0,2) for eps in (1,2) for lift in (0,1)]
    full['records']=[[v,w] for v,w in records]; full['frontier']=families

    delayed=[]
    for d in range(2,7):
        N=3**(d-1); C=(4**N-1)//3**d
        require(val(4**N-1)==d and C%3!=0,'elementary 4-power valuation')
        K=1
        while 4*16**N>=3**(K+1): K+=1
        for eps in (1,2):
            u=positive_unit(4**N,-C,K,eps,0); y=(3**d*u-1)//2; x=(4**N*y-1)//3
            require(replay(x,'1'+'0'*(2*N-1))==y,'delayed bridge')
            require(val(2*x+1)==d+K-1 and 4*rank(x)<rank(y),'delayed rank')
            for i in range(1,N):
                require(val(2*4**i*y+1)==1+val(i),'exact early depth')
                require(rank(4**i*y)>rank(y),'early inverse rank')
            delayed.append([d,N,K,eps,y,x,2*N])
    full['delayed']=delayed

    # Old all-depth boundary pruning fails; new depth-aware cap retains it.
    n=208363
    old={n};layer={n}
    for _ in range(3):
        layer={x for y in layer for x,w,gap in fan(y) if gap<=1}
        old.update(layer)
    complete,_,_=ball(n,3,False);new,_,_=ball(n,3,True)
    require(min(old,key=rank)==n,'old false pruning control')
    require(argmin(complete)==4445077 and argmin(new)==4445077,'restored witness')
    full['control']=[n,len(old),len(complete),len(new),4445077,new[4445077]]

    low=[x for x in range(1,122) if rank(x)<243]
    union=set(); lowpaths=[]
    for x in low:
        y=x; path=[]
        while y not in path:
            require(len(path)<128, 'finite sublevel control cap')
            path.append(y); y=step(y)
        require(y in (1,2), 'sublevel path did not end in trivial cycle')
        union.update(path); lowpaths.append([x,rank(x),path])
    y=121; path=[]
    while y not in union:
        require(len(path)<128, 'finite first-meeting cap')
        path.append(y); y=step(y)
    require(len(path)==54 and y==40 and 121 not in union, 'all-witness barrier')
    full['all_witness_121']={'lower_rank_sources':low,'orbits':lowpaths,
                             'union':sorted(union),'prefix':path,'first_meeting':[54,40]}

    body={'schema':'X-AS7-001-v1','base':BASE,'scope':SCOPE,
          'precision_table':table,'negative_nodes':len(shadow(10)),
          'comparisons':len(comparisons),'comparison_rows_sha256':sha(comparisons),
          'complete_nodes_sum':sum(row[4] for row in comparisons),
          'pruned_nodes_sum':sum(row[5] for row in comparisons),
          'omitted_fan_edges_sum':sum(row[8] for row in comparisons),
          'guard_cases':len(guard),'guard_rows_sha256':sha(guard),
          'record_nodes':len(records),'frontier_cases':len(families),'frontier_rows_sha256':sha(families),
          'delayed_cases':len(delayed),'delayed_bridge_steps':sum(row[-1] for row in delayed),
          'control':full['control'],'all_witness_121':{'lower_rank_sources':low,'forward_union':sorted(union),'first_meeting':[54,40],'rows_sha256':sha(full['all_witness_121'])},'full_payload_sha256':sha(full)}
    return {'body':body,'sha256':sha(body)},full

def main() -> None:
    p=argparse.ArgumentParser();p.add_argument('--check',type=Path);p.add_argument('--output',type=Path);p.add_argument('--full-output',type=Path)
    a=p.parse_args();report,full=build()
    if a.check: require(json.loads(a.check.read_text())==report,'canonical report mismatch')
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_bytes(enc(report)+b'\n')
    if a.full_output: a.full_output.write_bytes(enc(full)+b'\n')
    print('PASS',report['sha256']); print(json.dumps(report['body'],indent=2))

if __name__=='__main__': main()
