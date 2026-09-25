#!/usr/bin/env python3
"""Exact two-ladder ray capacities; never enumerate the ambient interval.
Standard library, integer/rational arithmetic. Certificates are PROPOSED evidence,
not claims of nonconvergence. All original-source paths are retained.
"""
from __future__ import annotations
import argparse
from bisect import bisect_left
from fractions import Fraction
import hashlib
import json
from math import lcm
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def step(n: int, p: int) -> int:
    return n // 2 if n % 2 == 0 else (p*n+1)//2


def hx(n: int) -> str:
    return format(n, 'x')


def ladder(source: int, p: int, depth: int) -> tuple[dict, list[int], dict[int,int]]:
    need(type(source) is int and source > 0 and p in (3,5), 'map/source domain')
    need(type(depth) is int and depth >= 0, 'depth domain')
    forward = [source]
    if source % p == 0:
        while forward[-1] % 2 == 0:
            forward.append(step(forward[-1],p))
        forward.append(step(forward[-1],p))
    y = forward[-1]
    seed_path = [y]
    if y == 1:
        seed_path = [5,8,4,2,1] if p == 3 else [3,8,4,2,1]
        y = seed_path[0]
    edges: dict[int,int] = {}
    for path in (forward,seed_path):
        for a,b in zip(path,path[1:]):
            edges[a] = b
    nodes = [source,y]
    clocks = []
    for _ in range(depth):
        k = 2 if p == 3 else 3
        while ((1 << k)*y-1) % p or (((1 << k)*y-1)//p) % p == 0:
            k += 1
        need(k <= (5 if p == 3 else 10), 'proved inverse-clock bound')
        z = ((1 << k)*y-1)//p
        need(4*z >= 5*y and z & 1, 'inverse growth/parity')
        n = z
        for _ in range(k):
            t = step(n,p)
            edges[n] = t
            n = t
        need(n == y, 'physical inverse clock')
        y = z
        nodes.append(y)
        clocks.append(k)
    return dict(source=hx(source), forward=[hx(n) for n in forward],
                seed_path=[hx(n) for n in seed_path], clocks=clocks), nodes, edges


def profile(ray_nodes: list[tuple[int,int]], last_shell: int) -> tuple[list[list[int]], Fraction]:
    """Sorted-list insertion; records only nonzero circular alternation births."""
    events = sorted((n.bit_length()-1, Fraction(n,1 << (n.bit_length()-1)), color)
                    for n,color in ray_nodes)
    phases: list[Fraction] = []
    colors: list[int] = []
    births: dict[int,int] = {}
    for h,u,b in events:
        need(h <= last_shell, 'inactive supplied ray')
        i = bisect_left(phases,u)
        if i < len(phases) and phases[i] == u:
            need(colors[i] == b, 'oppositely colored identical ray')
            continue
        delta = 0
        if phases:
            left,right = colors[i-1],colors[i % len(colors)]
            delta = int(left != b)+int(b != right)-int(left != right)
        need(delta in (0,2), 'Boolean circle insertion law')
        if delta:
            births[h] = births.get(h,0)+delta//2
        phases.insert(i,u)
        colors.insert(i,b)
    denominator = lcm(*range(1,last_shell+2))**2
    numerator = current = 0
    for k in range(last_shell+1):
        current += 2*births.get(k,0)
        numerator += current*(denominator//((k+1)**2))
    return [[h,births[h]] for h in sorted(births)], Fraction(numerator,denominator)


def certificate(source: int, p: int, depth: int, last_shell: int | None = None) -> dict:
    a,nodes0,edges0 = ladder(1,p,depth)
    b,nodes1,edges1 = ladder(source,p,depth)
    edges = dict(edges0)
    for n,t in edges1.items():
        need(n not in edges or edges[n] == t, 'functional path conflict')
        edges[n] = t
    core = [1,2,1] if p == 3 else [1,3,8,4,2,1]
    for n,t in zip(core,core[1:]):
        edges[n] = t
    by_odd: dict[int,tuple[int,int]] = {}
    collision = None
    for color,nodes in enumerate((nodes0,nodes1)):
        for n in nodes:
            m = n
            while not m & 1:
                edges[m] = m//2
                m //= 2
            if m in by_odd and by_odd[m][0] != color:
                collision = [by_odd[m][1],n]
            else:
                by_odd[m] = (color,n)
    common = dict(schema='two-ladder-capacity-v1', multiplier=p, source=hx(source),
                  depth=depth, ladders=[a,b])
    if collision is not None:
        n = source
        path = [n]
        while n != 1:
            need(n in edges, 'connected functional certificate is missing an edge')
            n = edges[n]
            need(n not in path or n == 1, 'unexpected noncore cycle')
            path.append(n)
        return dict(common, status='CONVERGENCE', collision=[hx(n) for n in collision],
                    path=[hx(n) for n in path])
    rays = [(n,0) for n in nodes0]+[(n,1) for n in nodes1]
    top = max(n.bit_length()-1 for n,_ in rays)
    k = 2*(top+1) if last_shell is None else last_shell
    need(type(k) is int and k >= top, 'last_shell smaller than a ray activation')
    births,value = profile(rays,k)
    peak = max([1,source]+list(edges)+list(edges.values()))
    height_exponent = max(k+1,(peak-1).bit_length())
    return dict(common, status='CAPACITY_LOWER_CERTIFICATE', last_shell=k,
                ambient_height_exponent=height_exponent, physical_peak=hx(peak),
                births=births, capacity=[hx(value.numerator),hx(value.denominator)],
                last_alternations=2*sum(v for _,v in births))


def corpus() -> list[dict]:
    requests = [(p,n,d) for p,n in ((3,7),(3,27),(3,97),(3,871),(3,2**61-1),(5,13),(5,17))
                for d in (0,4,16,64,256,1024)]
    requests += [(3,1,0),(3,2,0),(3,5,4),(5,3,4),(5,8,0)]
    return [certificate(n,p,d) for p,n,d in requests]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--source', type=int)
    parser.add_argument('--multiplier', type=int, choices=(3,5), default=3)
    parser.add_argument('--depth', type=int, default=256)
    parser.add_argument('--last-shell', type=int)
    args = parser.parse_args()
    rows = corpus() if args.source is None else [certificate(args.source,args.multiplier,args.depth,args.last_shell)]
    args.output.write_text(json.dumps(rows,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(status='PASS', cases=len(rows),
                         capacity_cases=sum(r['status']=='CAPACITY_LOWER_CERTIFICATE' for r in rows),
                         convergence_cases=sum(r['status']=='CONVERGENCE' for r in rows),
                         sha256=hashlib.sha256(args.output.read_bytes()).hexdigest()),sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
