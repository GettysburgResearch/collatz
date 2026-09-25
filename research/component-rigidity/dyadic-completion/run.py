#!/usr/bin/env python3
"""Lossless dyadic completion with finitely many actual odd Collatz edges.

Standard library. The infinite-horizon optimum is certified as A*zeta(2)+B,
using rational enclosures, not floating point. This is not a Collatz solver
with an all-input termination guarantee. Finite full-graph refinement has an
explicit height cap. All omitted odd edges remain omitted until added.
"""
from __future__ import annotations
import argparse
from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys


def require(test, message):
    if not test:
        raise ValueError(message)


def odd(n):
    require(type(n) is int and n > 0, 'positive integer required')
    return n // (n & -n)


def step(n, p):
    return n // 2 if n % 2 == 0 else (p*n+1)//2


def pack_q(x):
    return [str(x.numerator), str(x.denominator)]


class Enclosure:
    """zeta(2)=sum_(j>=0) 2^-j H_(j+1)/(j+1); tail <= 2^(1-J)."""
    def __init__(self, count=64, maximum=2048):
        self.count = 0
        self.maximum = maximum
        self.total = Q(0)
        self.harmonic = Q(0)
        self.refine(count)

    def refine(self, count):
        require(count <= self.maximum, 'UNRESOLVED_SYMBOLIC_PRECISION_CAP')
        for j in range(self.count, count):
            self.harmonic += Q(1, j+1)
            self.total += self.harmonic / ((j+1) * (1 << j))
        self.count = count
        self.lo = self.total
        self.hi = self.total + Q(1, 1 << (count-1))


ENC = Enclosure()


@dataclass(frozen=True)
class Z:
    a: int = 0
    b: Q = Q(0)

    def __add__(self, other):
        return Z(self.a+other.a, self.b+other.b)

    def __sub__(self, other):
        return Z(self.a-other.a, self.b-other.b)

    def __neg__(self):
        return Z(-self.a, -self.b)

    def sign(self):
        if not self.a:
            return (self.b > 0)-(self.b < 0)
        while True:
            left = self.a * (ENC.lo if self.a > 0 else ENC.hi) + self.b
            right = self.a * (ENC.hi if self.a > 0 else ENC.lo) + self.b
            if left > 0:
                return 1
            if right < 0:
                return -1
            ENC.refine(ENC.count * 2)

    def __lt__(self, other):
        return (self-other).sign() < 0

    def pack(self):
        return [self.a, *pack_q(self.b)]


ZERO = Z()


class Flow:
    """Dinic over the ordered additive group Q+Z*zeta(2)."""
    def __init__(self, vertices):
        self.g = {v: [] for v in vertices}
        self.original = []

    def edge(self, u, v, cap):
        require(u != v and cap.sign() > 0, 'invalid network edge')
        iu, iv = len(self.g[u]), len(self.g[v])
        self.g[u].append([v, iv, cap])
        self.g[v].append([u, iu, cap])
        self.original.append((u, v, cap, iu))

    def solve(self, source, sink):
        require(source != sink, 'incompatible pins')
        sys.setrecursionlimit(max(sys.getrecursionlimit(), 3*len(self.g)+100))
        infinity = Z(0, Q(1))
        for _, _, c, _ in self.original:
            infinity += c
        value = ZERO
        while True:
            level = {source: 0}
            todo = deque([source])
            while todo:
                u = todo.popleft()
                for v, _, c in self.g[u]:
                    if c.sign() > 0 and v not in level:
                        level[v] = level[u]+1
                        todo.append(v)
            if sink not in level:
                break
            cursor = {u: 0 for u in self.g}
            def send(u, budget):
                if u == sink:
                    return budget
                while cursor[u] < len(self.g[u]):
                    edge = self.g[u][cursor[u]]
                    v, back, c = edge
                    if c.sign() > 0 and level.get(v, -1) == level[u]+1:
                        amount = send(v, c if c < budget else budget)
                        if amount.sign() > 0:
                            edge[2] = edge[2]-amount
                            self.g[v][back][2] = self.g[v][back][2]+amount
                            return amount
                    cursor[u] += 1
                return ZERO
            while True:
                amount = send(source, infinity)
                if amount.sign() == 0:
                    break
                value += amount
        reached = {source}
        todo = deque([source])
        while todo:
            u = todo.popleft()
            for v, _, c in self.g[u]:
                if c.sign() > 0 and v not in reached:
                    reached.add(v)
                    todo.append(v)
        flows = [[u,v,(c-self.g[u][i][2]).pack()]
                 for u,v,c,i in self.original if c != self.g[u][i][2]]
        return value, reached, flows


class Model:
    def __init__(self, source, p, selected, horizon=None):
        require(type(source) is int and source > 1, 'source must exceed one')
        require(type(p) is int and p in (3,5), 'unsupported multiplier')
        require(horizon is None or type(horizon) is int and horizon >= 0,
                'invalid horizon')
        require(type(selected) is list and selected == sorted(set(selected)),
                'odd-edge list must be sorted and unique')
        require(all(type(n) is int and n > 0 and n % 2 for n in selected),
                'odd positive edge sources required')
        require(1 in selected and (p != 5 or 3 in selected), 'missing core edges')
        if horizon is not None:
            h = 1 << (horizon+1)
            require(source <= h and all(max(n,step(n,p)) <= h for n in selected),
                    'source or physical edge outside horizon')
        self.source, self.p, self.selected, self.horizon = source,p,selected,horizon
        self.marks = {1, odd(source)}
        for n in selected:
            self.marks.update((n, odd(step(n,p))))
        self.expanded = set()
        for n in self.marks:
            h = n.bit_length()-1
            q = n-(1 << h)
            for d in range(h):
                self.expanded.add((d, q >> (h-d)))
        self.depth = max((d+1 for d,_ in self.expanded), default=0)
        limit = self.depth if horizon is None else horizon+1
        harmonic = [Q(0)]
        for j in range(1, limit+1):
            harmonic.append(harmonic[-1]+Q(1,j*j))
        self.raw = defaultdict(lambda: ZERO)
        self.vertices = {1}
        self.leaves = []
        todo = [(0,0)]
        while todo:
            d,i = todo.pop()
            lo,hi = odd((1 << d)+i),odd((1 << d)+i+1)
            self.vertices.update((lo,hi))
            if (d,i) in self.expanded:
                weight = Z(0,Q(1,(d+1)**2))
                todo.extend(((d+1,2*i),(d+1,2*i+1)))
            else:
                self.leaves.append((d,i,lo,hi))
                weight = Z(1,-harmonic[d]) if horizon is None else Z(0,harmonic[horizon+1]-harmonic[d])
            if lo != hi and weight.sign() > 0:
                key = tuple(sorted((lo,hi)))
                self.raw[key] = self.raw[key]+weight
        parent = {v:v for v in self.vertices}
        def find(n):
            while parent[n] != n:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n
        for n in selected:
            u,v = find(n),find(odd(step(n,p)))
            if u != v:
                parent[max(u,v)] = min(u,v)
        self.component = {v:find(v) for v in self.vertices}
        self.quotient = defaultdict(lambda: ZERO)
        for (u,v),cap in self.raw.items():
            u,v = self.component[u],self.component[v]
            if u != v:
                key = tuple(sorted((u,v)))
                self.quotient[key] = self.quotient[key]+cap
        self.ones = set()

    def color(self, n):
        r = odd(n)
        if r in self.vertices:
            return int(self.component[r] in self.ones)
        h = r.bit_length()-1
        q = r-(1 << h)
        d=i=0
        while (d,i) in self.expanded:
            d += 1
            i = q >> (h-d)
        lo = odd((1 << d)+i)
        return int(self.component[lo] in self.ones)

    def solve(self):
        common = dict(schema='dyadic-completion-v1', multiplier=self.p,
                      source=self.source, horizon=self.horizon, odd_edges=self.selected,
                      compressed_vertices=len(self.vertices),
                      compressed_edges=len(self.raw), quotient_vertices=len(set(self.component.values())))
        if self.component[odd(self.source)] == self.component[1]:
            n=self.source
            path=[n]
            used=set()
            selected=set(self.selected)
            while n != 1:
                require(n not in used, 'unexpected noncore cycle in pin component')
                require(n % 2 == 0 or n in selected, 'missing directed merger edge')
                used.add(n)
                n=step(n,self.p)
                path.append(n)
            return dict(common, status='CONVERGENCE', path=path)
        graph = Flow(set(self.component.values()))
        for (u,v),cap in sorted(self.quotient.items()):
            graph.edge(u,v,cap)
        value,self.ones,flow=graph.solve(self.component[odd(self.source)],self.component[1])
        cut=ZERO
        for (u,v),cap in self.quotient.items():
            if (u in self.ones) != (v in self.ones):
                cut += cap
        require(cut == value, 'formal cut-flow equality failed')
        require(self.color(1) == 0 and self.color(self.source) == 1, 'pin loss')
        require(all(self.color(n) == self.color(step(n,self.p)) for n in self.selected), 'odd equality loss')
        return dict(common,status='OPTIMAL_COMPLETION',value=value.pack(),
                    ones=sorted(self.ones),flow=flow,zeta_terms=ENC.count,
                    zeta_interval=[pack_q(ENC.lo),pack_q(ENC.hi)])


def full_edges(p, k):
    h=1 << (k+1)
    return [n for n in range(1,h+1,2) if step(n,p) <= h]


def refine(source,p,k,round_cap=256):
    """An exhaustive finite-height oracle; never call it an infinite solver."""
    require(type(round_cap) is int and round_cap >= 1, 'positive round cap required')
    require(type(k) is int and k >= 0 and type(p) is int and p in (3,5), 'invalid finite oracle')
    require(type(source) is int and 1 < source <= (1 << (k+1)), 'invalid finite source')
    selected={1} if p==3 else {1,3}
    all_edges=full_edges(p,k)
    history=[]
    for iteration in range(round_cap):
        model=Model(source,p,sorted(selected),k)
        cert=model.solve()
        if cert['status']=='CONVERGENCE':
            history.append(dict(round=iteration,retained=len(selected),status='CONVERGENCE',certificate=cert))
            return dict(source=source,multiplier=p,horizon=k,status='CONVERGENCE',history=history,certificate=cert)
        defects=[n for n in all_edges if model.color(n) != model.color(step(n,p))]
        history.append(dict(round=iteration,retained=len(selected),status='OPTIMAL_RELAXATION',
                            value=cert['value'],violations=len(defects),certificate=cert))
        if not defects:
            return dict(source=source,multiplier=p,horizon=k,status='FULL_FINITE_OPTIMUM',history=history,certificate=cert)
        selected.update(defects)
    return dict(source=source,multiplier=p,horizon=k,status='UNRESOLVED_AT_ROUND_CAP',history=history,certificate=cert)


def selected_ladders(source,p,depth):
    require(type(depth) is int and depth >= 0 and type(p) is int and p in (3,5), 'invalid ladder request')
    selected={1} if p==3 else {1,3}
    for root in (1,source):
        y=odd(root)
        if y % p == 0:
            selected.add(y)
            y=odd(step(y,p))
        if y==1:
            y=5 if p==3 else 3
            selected.add(y)
        for _ in range(depth):
            k=2 if p==3 else 3
            while ((1 << k)*y-1)%p or (((1 << k)*y-1)//p)%p==0:
                k+=1
            y=((1 << k)*y-1)//p
            selected.add(y)
    return sorted(selected)


def corpus():
    cases=[]
    for p,n in ((3,27),(3,97),(5,13)):
        for depth in (0,2,4,8):
            edges=selected_ladders(n,p,depth)
            minimum=max([n]+[max(a,step(a,p)) for a in edges]).bit_length()-1
            for horizon in (minimum+2,None):
                cases.append(Model(n,p,edges,horizon).solve())
    for p,n in ((3,27),(5,13)):
        for k in (4,5,6,7,8,9,10):
            cases.append(Model(n,p,full_edges(p,k),None).solve())
    # Same finite odd constraints, literal ambient height 2^1025; no interval scan.
    cases.append(Model(27,3,selected_ladders(27,3,4),1024).solve())
    # All odd edges on the actual path of 27 are sufficient; neither ladder meeting nor regularity is assumed.
    n=27;edges={1}
    while n!=1:
        if n%2:
            edges.add(n)
        n=step(n,3)
    cases.append(Model(27,3,sorted(edges),None).solve())
    cases.append(Model(27,3,[1,5],None).solve())
    for horizon in (3,28,29,128,None):
        cases.append(Model(7,3,[1,7],horizon).solve())
    refinements=[refine(n,p,k) for p,n,k in ((3,27,7),(3,27,12),(3,97,12),(5,13,8),(5,13,10))]
    refinements.append(refine(27,3,12,round_cap=1))
    return dict(schema='dyadic-completion-corpus-v1',certificates=cases,refinements=refinements)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    data=corpus()
    text=json.dumps(data,sort_keys=True,separators=(',',':'))+'\n'
    args.output.write_text(text)
    print(json.dumps(dict(certificates=len(data['certificates']),refinements=len(data['refinements']),
                          sha256=sha256(text.encode()).hexdigest(),zeta_terms=ENC.count),sort_keys=True))


if __name__=='__main__':
    main()
