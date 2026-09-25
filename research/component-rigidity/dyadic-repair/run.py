#!/usr/bin/env python3
"""Exact dyadic elimination, certified tail bounds, and actual odd-edge repair.

Standard library only. This is a finite-constraint research solver, not a
universal Collatz termination algorithm. A resource cap is an unresolved case.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from collections import defaultdict, deque
from fractions import Fraction as Q
from math import lcm
from pathlib import Path
import json
import sys


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def pos(n: int) -> int:
    require(type(n) is int and n > 0, 'expected a positive integer')
    return n


def odd(n: int) -> int:
    pos(n)
    return n // (n & -n)


def step(n: int, p: int) -> int:
    return n // 2 if n % 2 == 0 else (p*n+1)//2


def phase(n: int) -> Q:
    return Q(n, 1 << (pos(n).bit_length()-1))-1


def enc(x: Q) -> list[int]:
    return [x.numerator, x.denominator]


class DSU:
    def __init__(self, nodes):
        self.p = {x:x for x in nodes}
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.p[max(a,b)] = min(a,b)


def skeleton(marked: set[int]):
    """Dyadic interval ancestors; an unsplit subtree becomes ONE tail edge."""
    splits = set()
    for n in marked:
        h = n.bit_length()-1
        a = n-(1 << h)
        for d in range(h):
            splits.add((d, a >> (h-d)))
    nodes = {1}
    pieces = []
    leaves = []
    todo = [(0,0)]
    while todo:
        d,j = todo.pop()
        left, right = odd((1 << d)+j), odd((1 << d)+j+1)
        nodes.update((left,right))
        split = (d,j) in splits
        pieces.append((d,j,left,right,split))
        if split:
            todo.extend(((d+1,2*j+1),(d+1,2*j)))
        else:
            leaves.append((d,j,left,right))
    return sorted(nodes), sorted(pieces), sorted(leaves, key=lambda z: Q(z[1],1 << z[0]))


def flow_cut(nodes, edges, source, sink):
    """Integer-scaled undirected Dinic, with net edge flows retained."""
    nodes = sorted(nodes)
    ix = {n:i for i,n in enumerate(nodes)}
    D = 1
    for _,_,lo,_ in edges:
        D = lcm(D, lo.denominator)
    adj = [[] for _ in nodes]
    pointers = []
    for u,v,lo,_ in edges:
        a,b = ix[u],ix[v]
        c = int(lo*D)
        forward = [b, len(adj[b]), c]
        backward = [a, len(adj[a]), c]
        pointers.append((forward,c))
        adj[a].append(forward); adj[b].append(backward)
    s,t = ix[source],ix[sink]
    value = 0
    sys.setrecursionlimit(max(sys.getrecursionlimit(),len(nodes)*2+200))
    while True:
        level = [-1]*len(nodes); level[s] = 0; todo = deque([s])
        while todo:
            u = todo.popleft()
            for v,rev,c in adj[u]:
                if c and level[v] < 0:
                    level[v] = level[u]+1; todo.append(v)
        if level[t] < 0:
            break
        at = [0]*len(nodes)
        def dfs(u, amount):
            if u == t:
                return amount
            while at[u] < len(adj[u]):
                e = adj[u][at[u]]; v,rev,c = e
                if c and level[v] == level[u]+1:
                    take = dfs(v,min(amount,c))
                    if take:
                        e[2] -= take; adj[v][rev][2] += take
                        return take
                at[u] += 1
            return 0
        upper = sum(e[2] for e in adj[s])
        while True:
            take = dfs(s,upper)
            if not take:
                break
            value += take
    colors = {n:int(level[ix[n]] >= 0) for n in nodes}
    flows = [Q(c-forward[2],D) for forward,c in pointers]
    return Q(value,D), colors, flows


def solve(problem: dict, horizon: int | None = None, tail_terms: int = 64) -> dict:
    p = problem['p']; N = pos(problem['N'])
    require(type(p) is int and p in (3,5),'p must be 3 or 5')
    sources = problem['odd_sources']
    require(type(sources) is list and sources == sorted(set(sources)), 'odd sources must be sorted and unique')
    require(all(type(n) is int and n > 0 and n%2 for n in sources),'invalid odd source')
    pins = problem.get('pins',[[1,0],[N,1]])
    require(type(pins) is list and all(type(v) is list and len(v)==2 and type(v[0]) is int and v[0]>0 and type(v[1]) is int and v[1] in (0,1) for v in pins),'invalid pins')
    require([1,0] in pins and [N,1] in pins,'original pins must be retained')
    relations = [(n,odd(p*n+1)) for n in sources]
    marked = {1} | {odd(n) for n,_ in pins} | {x for ab in relations for x in ab}
    raw_nodes,pieces,leaves = skeleton(marked)
    K = max(n.bit_length()-1 for n in raw_nodes)
    require(horizon is None or (type(horizon) is int and horizon >= K),'horizon below a marked phase')
    require(type(tail_terms) is int and tail_terms >= 1,'invalid tail precision')
    L = max(tail_terms,K+2) if horizon is None else horizon+1
    weights = [Q(1,(d+1)**2) for d in range(L)]
    heads = [Q(0)]*(L+1)
    for d in range(L-1,-1,-1):
        heads[d] = heads[d+1]+weights[d]
    dsu = DSU(raw_nodes)
    for a,b in relations:
        dsu.union(a,b)
    grouped = {0:[],1:[]}
    for n,b in pins:
        grouped[b].append(odd(n))
    for group in grouped.values():
        for n in group[1:]:
            dsu.union(group[0],n)
    zero,one = dsu.find(1),dsu.find(odd(N))
    base = {'schema':'dyadic-repair-cut-v1','problem':problem,'horizon':horizon,'tail_terms':L,'max_phase_depth':K}
    if zero == one:
        return dict(base,status='PINS_INFEASIBLE')
    capacities = defaultdict(lambda:[Q(0),Q(0)])
    for d,j,a,b,split in pieces:
        a,b = sorted((dsu.find(a),dsu.find(b)))
        if a == b:
            continue
        if split:
            lo = hi = weights[d]
        elif horizon is None:
            lo,hi = heads[d]+Q(1,L+1),heads[d]+Q(1,L)
        else:
            lo = hi = heads[d]
        capacities[(a,b)][0] += lo; capacities[(a,b)][1] += hi
    edges = [(a,b,*v) for (a,b),v in sorted(capacities.items())]
    nodes = {dsu.find(n) for n in raw_nodes}
    lower,colors,flows = flow_cut(nodes,edges,one,zero)
    upper = sum((hi for a,b,lo,hi in edges if colors[a]!=colors[b]),Q(0))
    raw_colors = {n:colors[dsu.find(n)] for n in raw_nodes}
    ranges = [[enc(Q(j,1 << d)),enc(Q(j+1,1 << d)),raw_colors[a]] for d,j,a,b in leaves]
    result = dict(base,status='SEPARATOR',source_vertex=one,sink_vertex=zero,
        classes=[[n,dsu.find(n)] for n in raw_nodes],
        colors=sorted(colors.items()),ranges=ranges,
        edges=[[a,b,enc(lo),enc(hi),enc(f)] for (a,b,lo,hi),f in zip(edges,flows)],
        lower=enc(lower),upper=enc(upper),
        stats={'marked_phases':len(marked),'raw_vertices':len(raw_nodes),'quotient_vertices':len(nodes),'terminal_intervals':len(leaves),'compressed_edges':len(edges)})
    return result


def coloring(certificate):
    ranges = certificate['ranges']
    starts = [Q(*row[0]) for row in ranges]
    labels = [row[2] for row in ranges]
    def g(x):
        return labels[bisect_right(starts,x)-1]
    def b(n):
        return g(phase(n))
    return g,b,starts


def normalize(x: Q) -> Q:
    while x >= 2:
        x /= 2
    while x < 1:
        x *= 2
    return x


def defect(certificate: dict, prefer_marked: bool = True) -> dict:
    require(certificate['status']=='SEPARATOR','a feasible cut is required')
    p = certificate['problem']['p']; K = certificate['max_phase_depth']
    g,b,starts = coloring(certificate)
    if prefer_marked:
        for n,_ in sorted(certificate['classes'], key=lambda row:(row[1] != certificate['source_vertex'],row[0])):
            t = step(n,p)
            if b(n) != b(t):
                return {'kind':'MARKED_ODD_EDGE','n':n,'target':t,'colors':[b(n),b(t)]}
    breaks = {Q(1),Q(2)} | {1+x for x in starts}
    overlay = set(breaks)
    r = p.bit_length()-1
    for z in breaks:
        for a in (r,r+1):
            y = z*(1 << a)/p
            if 1 < y < 2:
                overlay.add(y)
    points = sorted(overlay)
    for a,z in zip(points,points[1:]):
        mid = (a+z)/2
        if g(mid-1) == g(normalize(p*mid)-1):
            continue
        c = (2*p+1).bit_length(); h = K+c; scale = 1 << h
        n = (a*scale).numerator//(a*scale).denominator+1
        if n%2 == 0:
            n += 1
        require(Q(n)+Q(1,p) < z*scale,'oracle width bound failed')
        t = step(n,p)
        require(b(n)!=b(t),'oracle returned a satisfied edge')
        return {'kind':'ROTATION_INTERVAL','n':n,'target':t,'colors':[b(n),b(t)],'interval':[enc(a),enc(z)],'shell':h}
    raise ValueError('nonconstant finite-step coloring unexpectedly rotation invariant')


def original_path(N: int,p: int, sources: list[int]) -> list[int]:
    have = set(sources); seen = set(); path = [N]
    while path[-1] != 1:
        n = path[-1]
        require(n not in seen,'retained graph cycles away from 1')
        seen.add(n)
        require(n%2==0 or n in have,'path uses an unrecorded odd edge')
        path.append(step(n,p))
    return path


def initial_sources(N: int, p: int, ladder_depth: int = 0) -> list[int]:
    require(type(ladder_depth) is int and ladder_depth >= 0,'invalid ladder depth')
    sources = {1} if p==3 else {1,3}
    if not ladder_depth:
        return sorted(sources)
    for M in (1,N):
        y = odd(M)
        if y%p == 0:
            sources.add(y); y = step(y,p)
        if y==1:
            y = 5 if p==3 else 3
            sources.add(y)
        for _ in range(ladder_depth):
            k = 2 if p==3 else 3
            while ((1 << k)*y-1)%p or (((1 << k)*y-1)//p)%p==0:
                k += 1
            z = ((1 << k)*y-1)//p
            sources.add(z); y = z
    return sorted(sources)


def root_frontier(N: int,p: int,sources: list[int]):
    """Retain the same original source; never reset an actual root clock."""
    have = set(sources); seen = set(); n = odd(N)
    while n != 1 and n in have:
        if n in seen:
            return None,True
        seen.add(n); n = odd(p*n+1)
    return (None if n==1 else n),False


def cycle_path(N: int,p: int,sources: list[int]):
    have=set(sources); first={}; path=[]; n=N
    while n not in first:
        require(n%2==0 or n in have,'cycle uses unrecorded odd edge')
        first[n]=len(path); path.append(n); n=step(n,p)
    path.append(n)
    return path,first[n]


def refine(N: int,p: int,round_cap: int = 64,ladder_depth: int = 0,tail_terms: int = 64,policy: str = 'root-fair') -> dict:
    require(type(round_cap) is int and round_cap>=0,'invalid round cap')
    require(policy in ('root-fair','cuts-only'),'unknown repair policy')
    sources = initial_sources(N,p,ladder_depth)
    initial = sources[:]; records = []
    common = {'schema':'dyadic-repair-refinement-v1','p':p,'N':N,'initial_sources':initial,'round_cap':round_cap,'policy':policy}
    for k in range(round_cap+1):
        problem = {'p':p,'N':N,'odd_sources':sources[:]}
        cert = solve(problem,tail_terms=tail_terms)
        if cert['status']=='PINS_INFEASIBLE':
            path = original_path(N,p,sources)
            return dict(common,records=records,status='CONVERGENCE',path=path,final_sources=sources)
        if policy=='root-fair':
            frontier,is_cycle = root_frontier(N,p,sources)
            if is_cycle:
                path,start=cycle_path(N,p,sources)
                return dict(common,records=records,status='VERIFIED_OTHER_CYCLE',path=path,cycle_start=start,final_sources=sources)
        if k==round_cap:
            return dict(common,records=records,status='UNRESOLVED_AT_RESOURCE_CAP',last_cut=cert,final_sources=sources)
        if policy=='root-fair' and k%2:
            require(frontier is not None,'root path closed without pin merger')
            _,color,_=coloring(cert)
            t=step(frontier,p)
            witness={'kind':'ROOT_FAIR_EDGE','n':frontier,'target':t,'colors':[color(frontier),color(t)]}
        else:
            witness=defect(cert)
        records.append({'cut':cert,'edge':witness})
        require(witness['n'] not in sources,'duplicate repair edge')
        sources = sorted(sources+[witness['n']])
    raise RuntimeError('unreachable')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=int,default=27)
    parser.add_argument('--multiplier',type=int,choices=(3,5),default=3)
    parser.add_argument('--rounds',type=int,default=64)
    parser.add_argument('--ladder-depth',type=int,default=0)
    parser.add_argument('--tail-terms',type=int,default=64)
    parser.add_argument('--policy',choices=('root-fair','cuts-only'),default='root-fair')
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    record = refine(args.source,args.multiplier,args.rounds,args.ladder_depth,args.tail_terms,args.policy)
    args.output.write_text(json.dumps(record,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'status':record['status'],'source':args.source,'p':args.multiplier,'repairs':len(record['final_sources'])-len(record['initial_sources']), 'retained_odd_sources':len(record['final_sources']),'largest_phase_depth':max((r['cut']['max_phase_depth'] for r in record['records']),default=0),'path_steps':len(record.get('path',[]))-1 if 'path' in record else None},sort_keys=True))

if __name__=='__main__':
    main()
