#!/usr/bin/env python3
"""Exact open-boundary Collatz cuts. Standard library; no network or assertions.
Only T-edges inside 1..H are contracted. Exterior components remain free.
All max-flow arithmetic is integer after exact rational scaling.
"""
from __future__ import annotations
import argparse
from collections import defaultdict, deque
from fractions import Fraction
import hashlib
import json
from math import lcm
from pathlib import Path
import sys


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def step(n: int, multiplier: int = 3) -> int:
    require(n > 0 and multiplier in (3, 5), 'invalid map input')
    return n // 2 if n % 2 == 0 else (multiplier * n + 1) // 2


def components(height: int, multiplier: int = 3) -> list[int]:
    require(height >= 2, 'height must be >= 2')
    parent = list(range(height + 1))
    size = [1] * (height + 1)
    def find(n: int) -> int:
        while parent[n] != n:
            parent[n] = parent[parent[n]]
            n = parent[n]
        return n
    for n in range(1, height + 1):
        m = step(n, multiplier)
        if m <= height:
            a, b = find(n), find(m)
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
    minimum: dict[int, int] = {}
    for n in range(1, height + 1):
        root = find(n)
        minimum[root] = min(n, minimum.get(root, n))
    return [0] + [minimum[find(n)] for n in range(1, height + 1)]


def check_coloring(bits: list[int], multiplier: int = 3) -> None:
    h = len(bits) - 1
    require(bits[1] == 0 and all(x in (0, 1) for x in bits[1:]), 'not Boolean/core pinned')
    for n in range(1, h + 1):
        t = step(n, multiplier)
        if t <= h:
            require(bits[n] == bits[t], f'invariant edge failed at {n}')


def variation(bits: list[int], k: int) -> int:
    require(1 << (k + 1) < len(bits), 'incomplete shell')
    return sum(abs(bits[n + 1] - bits[n]) for n in range(1 << k, 1 << (k + 1)))


def corridor(k: int, r: int) -> dict:
    require(1 <= r <= k - 2, 'corridor requires 1<=r<=k-2')
    a = 1 << (k - r)
    height = 4 * 3 ** (r - 1) * a
    ts = range((4 * a) // 3 + 2, 2 * a + 1)
    seeds = [(1 << r) * t - 1 for t in ts]
    exits = []
    edges = 0
    for t, n in zip(ts, seeds):
        require((1 << k) <= n < (1 << (k + 1)), 'seed outside shell')
        for j in range(r + 1):
            expected = 3 ** j * (1 << (r - j)) * t - 1
            require(n == expected, 'corridor affine replay failed')
            if j < r:
                require(n % 2 == 1 and n <= height, 'premature exit/parity failure')
                if j == r - 1:
                    exits.append(n)
                n = step(n)
                edges += 1
            else:
                require(n > height, 'missing terminal exit')
    comp = components(height)
    labels = [comp[n] for n in seeds]
    require(len(set(labels)) == len(labels), 'distinct exits merged inside cutoff')
    require(comp[1] not in labels, 'exit connected to core')
    chosen = {label for i, label in enumerate(labels) if i % 2}
    bits = [int(label in chosen) for label in comp]
    check_coloring(bits)
    v = variation(bits, k)
    require(v >= len(seeds) - 1, 'alternating-seed bound failed')
    d = [0] + [bits[n + 1] - bits[n] for n in range(1, height)]
    d2 = d3 = births = 0
    for n in range(1, (height - 2) // 2 + 1):
        require(d[n] == d[2*n] + d[2*n+1], 'D2 failure')
        d2 += 1
    for n in range((height - 5) // 3 + 1):
        require(d[2*n+1] + d[2*n+2] == d[3*n+2]+d[3*n+3]+d[3*n+4], 'D3 failure')
        d3 += 1
    for j in range(height.bit_length() - 2):
        b = sum(bits[n] == bits[n+1] != bits[2*n+1]
                for n in range(1 << j, 1 << (j+1)))
        require(variation(bits, j+1) == variation(bits, j) + 2*b, 'birth identity failed')
        births += 1
    digest = hashlib.sha256(bytes(bits[1:])).hexdigest()
    return dict(k=k, r=r, height=height, seeds=len(seeds), first_seed=seeds[0],
                last_seed=seeds[-1], minimum_variation=len(seeds)-1,
                observed_variation=v, literal_edges=edges,
                D2_checks=d2, D3_checks=d3, birth_checks=births,
                coloring_sha256=digest)


class MaxFlow:
    """Integer Dinic algorithm; each capacity pair carries antisymmetric flow."""
    def __init__(self, count: int) -> None:
        self.g: list[list[list[int]]] = [[] for _ in range(count)]
        self.original: list[tuple[int, int, int, int]] = []

    def edge(self, u: int, v: int, capacity: int) -> None:
        require(u != v and capacity > 0, 'invalid quotient edge')
        iu, iv = len(self.g[u]), len(self.g[v])
        self.g[u].append([v, iv, capacity])
        self.g[v].append([u, iu, capacity])
        self.original.append((u, v, capacity, iu))

    def solve(self, source: int, sink: int) -> tuple[int, set[int], list[tuple[int,int,int]]]:
        require(source != sink, 'infeasible anchor separation')
        sys.setrecursionlimit(max(sys.getrecursionlimit(), 2*len(self.g)+100))
        total = 0
        infinity = sum(c for _, _, c, _ in self.original) + 1
        while True:
            level = [-1] * len(self.g)
            level[source] = 0
            q = deque([source])
            while q:
                u = q.popleft()
                for v, _, capacity in self.g[u]:
                    if capacity > 0 and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            if level[sink] < 0:
                break
            cursor = [0] * len(self.g)
            def send(u: int, budget: int) -> int:
                if u == sink:
                    return budget
                while cursor[u] < len(self.g[u]):
                    e = self.g[u][cursor[u]]
                    v, back, cap = e
                    if cap > 0 and level[v] == level[u] + 1:
                        flow = send(v, min(budget, cap))
                        if flow:
                            e[2] -= flow
                            self.g[v][back][2] += flow
                            return flow
                    cursor[u] += 1
                return 0
            while True:
                sent = send(source, infinity)
                if not sent:
                    break
                total += sent
        reached = {source}
        q = deque([source])
        while q:
            u = q.popleft()
            for v, _, cap in self.g[u]:
                if cap > 0 and v not in reached:
                    reached.add(v)
                    q.append(v)
        flow = [(u,v,c-self.g[u][i][2]) for u,v,c,i in self.original]
        return total, reached, flow


def cut_certificate(height: int, anchor: int, multiplier: int = 3,
                    brute_force: bool = False) -> dict:
    require(1 < anchor <= height, 'invalid anchor')
    comp = components(height, multiplier)
    labels = sorted(set(comp[1:]))
    ids = {c: i for i, c in enumerate(labels)}
    common = dict(height=height, anchor=anchor, multiplier=multiplier,
                  quotient_vertices=len(labels))
    if comp[anchor] == comp[1]:
        return dict(common, status='MERGED_WITHIN_CUTOFF')
    scale = lcm(*(n*n for n in range(1, (height-1).bit_length()+1)))
    weights: dict[tuple[int,int], int] = defaultdict(int)
    for n in range(1, height):
        u, v = comp[n], comp[n+1]
        if u != v:
            if u > v:
                u, v = v, u
            weights[u,v] += scale // (n.bit_length() ** 2)
    network = MaxFlow(len(labels))
    for (u,v), capacity in sorted(weights.items()):
        network.edge(ids[u], ids[v], capacity)
    value, reached, flow = network.solve(ids[comp[anchor]], ids[comp[1]])
    ones = {labels[i] for i in reached}
    bits = [int(label in ones) for label in comp]
    check_coloring(bits, multiplier)
    require(bits[anchor] == 1, 'anchor lost')
    cut = sum(cap for (u,v),cap in weights.items() if (u in ones) != (v in ones))
    require(cut == value, 'cut-flow mismatch')
    if brute_force:
        free = [u for u in labels if u not in (comp[1], comp[anchor])]
        require(len(free) <= 18, 'bruteforce request too large')
        brute = None
        for mask in range(1 << len(free)):
            side = {comp[anchor]} | {u for i,u in enumerate(free) if mask >> i & 1}
            cost = sum(cap for (u,v),cap in weights.items() if (u in side) != (v in side))
            brute = cost if brute is None else min(brute, cost)
        require(brute == value, 'exhaustive optimum mismatch')
    energy = Fraction(value, scale)
    return dict(common, status='FINITE_SEPARATOR', scale=scale,
                scaled_capacity=value, capacity=[energy.numerator, energy.denominator],
                ones=sorted(ones),
                flow=[[labels[u],labels[v],f] for u,v,f in flow if f],
                shell_variation=[variation(bits,k) for k in range(height.bit_length()-1)],
                coloring_sha256=hashlib.sha256(bytes(bits[1:])).hexdigest(),
                quotient_edges=len(weights))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('results.json'))
    args = parser.parse_args()
    corridors = [corridor(k,r) for k,r in ((8,1),(10,1),(10,3),(12,4),(14,6),(16,8))]
    cases = []
    for multiplier, anchor, exponents in (
        (3,27,range(5,14)), (3,97,range(7,15)),
        (3,871,range(10,17)), (5,13,range(4,17)), (5,17,range(5,16))):
        for power in exponents:
            cases.append(cut_certificate(1 << power, anchor, multiplier))
    exhaustive_cases = exhaustive_assignments = 0
    for multiplier in (3,5):
        for height in range(4,65):
            comp = components(height,multiplier)
            labels = sorted(set(comp[1:]))
            anchors = [c for c in labels if c != comp[1]][:2]
            for anchor in anchors:
                if len(labels) - 2 <= 12:
                    cut_certificate(height,anchor,multiplier,brute_force=True)
                    exhaustive_cases += 1
                    exhaustive_assignments += 1 << (len(labels)-2)
    coarea_checks = 0
    for multiplier in (3,5):
        for height in range(4,65):
            comp = components(height,multiplier)
            values = {c: Fraction((c*c+3*c+1) % 8,7) for c in set(comp[1:])}
            energy = sum((abs(values[comp[n+1]]-values[comp[n]])/n.bit_length()**2
                          for n in range(1,height)),Fraction(0))
            integrated = sum((sum((Fraction(int((values[comp[n]]>Fraction(i,7)) !=
                                                (values[comp[n+1]]>Fraction(i,7))), n.bit_length()**2)
                                   for n in range(1,height)),Fraction(0)) for i in range(7)),Fraction(0))/7
            require(energy == integrated, 'coarea identity failed')
            coarea_checks += 1
    previous: dict[tuple[int,int], Fraction | None] = {}
    for c in cases:
        key = c['multiplier'], c['anchor']
        current = None if c['status'] != 'FINITE_SEPARATOR' else Fraction(*c['capacity'])
        if key in previous:
            old = previous[key]
            require(old is not None or current is None, 'merged anchor resurrected')
            require(old is None or current is None or current >= old, 'capacity decreased')
        previous[key] = current
    output = dict(status='PROPOSED; bounded exact experiments, not a Collatz proof',
                  corridors=corridors, cut_certificates=cases,
                  exhaustive_cut_cases=exhaustive_cases,
                  exhaustive_cut_assignments=exhaustive_assignments,
                  exact_coarea_checks=coarea_checks)
    args.output.write_text(json.dumps(output,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(dict(corridor_cases=len(corridors), cut_cases=len(cases),
                         finite_cut_certificates=sum(c['status']=='FINITE_SEPARATOR' for c in cases),
                         exhaustive_cut_cases=exhaustive_cases,
                         exhaustive_cut_assignments=exhaustive_assignments,
                         exact_coarea_checks=coarea_checks,
                         output_sha256=hashlib.sha256(args.output.read_bytes()).hexdigest()),indent=2))

if __name__ == '__main__':
    main()
