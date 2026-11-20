#!/usr/bin/env python3
"""Reviewer replay: reuse path producer, independently check edges and sources."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def step(n):
    need(type(n) is int and n > 0, "ordinary input")
    return n // 2 if n % 2 == 0 else (3*n + 1)//2


def high_expected(x):
    need(x > 0 and x % 243 == 0 and x % 2, "high input")
    v = x // 243
    lower = min(k for k in range(2, 6) if pow(3, k, 16)*(v % 16) % 16 in (3, 5))
    upper = min(k for k in range(6, 10) if pow(3, k, 16)*(v % 16) % 16 in (3, 5))
    rows = [(('power', k), 3**k*v) for k in range(6, upper)]
    rows += [(('offset', k-3), 8*3**(k-3)*v-1) for k in range(upper, lower, -1)]
    rows += [(('power', k), 3**k*v) for k in range(lower, 5)]
    need(len({label for label, _ in rows}) == len(rows), "high label multiplicity")
    return rows


def expected(x):
    if x % 243 == 0:
        return high_expected(x)
    j, u = 0, x
    while u % 3 == 0:
        j += 1
        u //= 3
    need(j <= 4, "low exponent")
    a0 = min(a for a in range(j+1, j+487) if pow(2, a, 729)*u % 729 == 1)
    def target(a):
        z = pow(3, a, 512)*(u % 512) % 512
        return z == 369 or z % 16 == 3 or z % 8 == 5 or z % 32 == 23
    a = min(a0+486*r for r in range(64) if target(a0+486*r))
    need(j < a <= 31110, "universal exponent bound")
    z = (2**a*u-1)//3
    need(3*z == 2**a*u-1 and z > 0 and z % 243 == 0, "ordinary high splice")
    rows = [(('low-power', j, k), 3**k*u) for k in range(j+1, a)]
    rows += [(('embedded-high', j, a, *label), y) for label, y in high_expected(z)]
    rows += [(('low-power', j, k), 3**k*u) for k in range(j)]
    need(len({label for label, _ in rows}) == len(rows), "low label multiplicity")
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--author-path', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--extra-sources', action='store_true', help='also replay 1,3,9,27,81; these have much longer generated returns')
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('circulation_author', args.author_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # The producer and its fixture list are reused; every acceptance check
    # below, including the independent affine label reconstruction, is ours.
    sources, _ = mod.fixtures()
    sources = sorted(set(sources))
    if args.extra_sources:
        sources = sorted(set(sources) | {1, 3, 9, 27, 81})
    paths = []
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        a, b = find(x), find(y)
        if a != b:
            parent[max(a,b)] = min(a,b)
    edge_count = triple_count = 0
    for x in sources:
        p = mod.return_path(x)
        need(p.vertices[0] == 3*x and p.vertices[-1] == x, "endpoints")
        need(len(p.vertices) == len(p.kinds)+1 <= 93451, "encoding and length")
        triple_sources = []
        for v, w, kind in zip(p.vertices, p.vertices[1:], p.kinds):
            need(type(v) is int and type(w) is int and min(v, w) > 0, "ordinary positive vertices")
            need(v <= 3*w and w <= 3*v, "height ratio")
            find(v); find(w)
            if kind == 'O':
                need(step(v) == w or step(w) == v, "ordinary undirected edge")
                union(v, w)
            elif kind == 'V':
                need(v % 2 == 1 and w == 3*v, "directed odd tripling")
                triple_sources.append(v)
            else:
                raise ValueError("unknown edge type")
        need(triple_sources == [y for _, y in expected(x)], "independent affine-source list")
        edge_count += len(p.kinds)
        triple_count += len(triple_sources)
        paths.append((x, p, triple_sources))
    balances = []
    for s in (0, 1, 2):
        divergence = defaultdict(Fraction)
        for x, _, tripling in paths:
            weight = Fraction(1, x**s)
            for y in [x] + tripling:
                divergence[find(y)] -= weight
                divergence[find(3*y)] += weight
        need(all(v == 0 for v in divergence.values()), "finite quotient circulation")
        balances.append({'power': s, 'vertices': len(divergence), 'balanced': True})
    clipping_checks = 0
    grid = [Fraction(k, 2) for k in range(-8, 9)]
    for a in grid:
        for b in grid:
            if a > b:
                continue
            def clip(x):
                return min(b, max(a, x))
            for x in grid:
                for y in grid:
                    g = y-x
                    h = clip(y)-clip(x)
                    need(max(h, 0) <= max(g, 0), "positive clipping orientation")
                    need(max(-h, 0) <= max(-g, 0), "negative clipping orientation")
                    clipping_checks += 1
    need(17+5*(31110+1)+5*31110*17 == 2799922, "source label total")
    report = {
        'status': 'PASS',
        'scope': 'Reused author path producer; independent literal edge, affine-source multiplicity, quotient-flow and scalar clipping checks. No independent external KL reproof.',
        'author_sha256': hashlib.sha256(args.author_path.read_bytes()).hexdigest(),
        'sources': len(sources), 'literal_edges': edge_count,
        'return_tripling_edges': triple_count, 'balances': balances,
        'rational_clipping_cases': clipping_checks,
    }
    raw = json.dumps(report, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(raw)
    print(raw, end='')


if __name__ == '__main__':
    main()
