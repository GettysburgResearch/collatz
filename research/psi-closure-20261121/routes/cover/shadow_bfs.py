#!/usr/bin/env python3
"""
Exact exploration of ordinary paths from a RATIONAL point (x0, y0) of X = Z_2 x Z_3.

Evidence tier: exhaustive bounded search with exact rational arithmetic (fractions.Fraction).
A bounded search proves nothing beyond its depth; the proof for (-1, 0) is in NOTES.md and in
CoverObstruction.lean.  This script is the independent replay of the invariants used there.

State = pair of rationals (x, y):
    x = 2-adic shadow (odd denominator), y = 3-adic shadow (denominator prime to 3).
A path acts on the integers n of a small neighbourhood of (x0, y0) as n -> alpha*n + beta, and
    (x, y) = (alpha*x0 + beta, alpha*y0 + beta),   so   y - x = alpha*(y0 - x0).
Moves (letters used in printed paths):
    o / e : forward T, odd / even branch, chosen by the 2-adic parity of x
    D     : backward doubling z -> 2z                       (always legal)
    S     : backward odd branch z -> (2z-1)/3               (legal iff y = 2 mod 3 in Z_3)
A path is DESCENDING iff alpha < 1, or alpha = 1 and beta < 0.

usage:  python3 -X utf8 -B shadow_bfs.py [depth_main] [depth_other]
"""
from fractions import Fraction as Fr
import sys
import time


def par2(x):
    assert x.denominator % 2 == 1, x
    return x.numerator % 2


def res3(y):
    assert y.denominator % 3 != 0, y
    return (y.numerator * y.denominator) % 3      # d^-1 = d (mod 3) when 3 does not divide d


def moves(x, y):
    if par2(x) == 0:
        yield 'e', x / 2, y / 2, Fr(1, 2)
    else:
        yield 'o', (3 * x + 1) / 2, (3 * y + 1) / 2, Fr(3, 2)
    yield 'D', 2 * x, 2 * y, Fr(2)
    if res3(y) == 2:
        yield 'S', (2 * x - 1) / 3, (2 * y - 1) / 3, Fr(2, 3)


def explore(x0, y0, depth, stop_at_descent=False, max_nodes=4_000_000):
    """Breadth-first search over all ordinary walks of length <= depth from (x0, y0).
    Returns (seen, best, descents, reached_depth); seen maps node -> (alpha, path)."""
    x0, y0 = Fr(x0), Fr(y0)
    start = (x0, y0)
    seen = {start: (Fr(1), '')}
    frontier = [start]
    best = None
    descents = []
    d = 0
    for d in range(1, depth + 1):
        nxt = []
        for (x, y) in frontier:
            a, path = seen[(x, y)]
            for name, x2, y2, m in moves(x, y):
                key = (x2, y2)
                if key in seen:
                    continue
                a2 = a * m
                p2 = path + name
                seen[key] = (a2, p2)
                beta = x2 - a2 * x0
                assert y2 == a2 * y0 + beta          # both shadows follow the same affine map
                nxt.append(key)
                if best is None or a2 < best[0]:
                    best = (a2, beta, p2, key)
                if a2 < 1 or (a2 == 1 and beta < 0):
                    descents.append((a2, beta, p2, key))
        frontier = nxt
        if (stop_at_descent and descents) or len(seen) > max_nodes:
            break
    return seen, best, descents, d


def main_point(depth):
    """(-1, 0): replay the invariants of the written proof on every node within `depth`."""
    t0 = time.time()
    seen, best, descents, d = explore(-1, 0, depth)
    start = (Fr(-1), Fr(0))
    bad = 0
    n_phase2 = 0
    alphas = {}
    for (x, y), (a, path) in seen.items():
        ok = (x <= -1) and (y >= 0) and (a == y - x) and (a >= 1) and (a > 1 or (x, y) == start)
        # reduced form: p forward steps then backward steps; phase 2 <=> more S than o
        p, s = path.count('o'), path.count('S')
        if s > p:
            n_phase2 += 1
            ok = ok and y.denominator == 1 and y >= 1      # 3-adic shadow is a positive integer
        else:
            ok = ok and x.denominator == 1                 # 2-adic shadow is a negative integer
        if not ok:
            bad += 1
        alphas[a] = alphas.get(a, 0) + 1
    print(f"[A] point (-1,0): depth {d}, nodes {len(seen)}, phase-2 nodes {n_phase2}, "
          f"invariant violations {bad}, descending paths {len(descents)}, "
          f"time {time.time() - t0:.1f}s")
    small = sorted(alphas)[:6]
    print("    smallest multipliers alpha (count):",
          ", ".join(f"{a} ({alphas[a]})" for a in small))
    print(f"    smallest non-trivial alpha: {best[0]} via path '{best[2]}' at node {best[3]}")
    return bad == 0 and not descents


def other_points(depth):
    pts = [(Fr(-1), Fr(y0)) for y0 in range(-12, 64, 3)]
    pts += [(Fr(-5), Fr(0)), (Fr(-17), Fr(0)), (Fr(-19, 11), Fr(0)),
            (Fr(-5), Fr(3)), (Fr(-5), Fr(9)), (Fr(-17), Fr(3)), (Fr(-19, 11), Fr(3)),
            (Fr(-7), Fr(0)), (Fr(-1), Fr(1)), (Fr(-1), Fr(4)), (Fr(-1), Fr(7))]
    print(f"[B] other rational points, exhaustive to depth {depth} (EMPIRICAL beyond that):")
    for (x0, y0) in pts:
        t0 = time.time()
        seen, best, descents, d = explore(x0, y0, depth, stop_at_descent=True)
        if descents:
            a, beta, path, node = min(descents, key=lambda r: (len(r[2]), r[0]))
            print(f"    ({x0},{y0}): DESCENT at length {len(path)}: alpha={a} beta={beta} "
                  f"path={path}")
        else:
            print(f"    ({x0},{y0}): no descending path of length <= {d} "
                  f"({len(seen)} nodes, min alpha {best[0]}, {time.time() - t0:.1f}s)")


if __name__ == '__main__':
    d_main = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    d_other = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    ok = main_point(d_main)
    other_points(d_other)
    print("RESULT:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
