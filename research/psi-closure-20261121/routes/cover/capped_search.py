#!/usr/bin/env python3
"""
Long-range search for descending ordinary paths, capped by multiplier instead of by depth.

Evidence tier: EMPIRICAL.  For p = 0..pmax the side tree of backward moves hanging off T^p(n)
is searched completely among the nodes whose multiplier (relative to n) never exceeds 2^cap and
whose backward depth is <= depth_cap.  "none found" means: no descending path with
p <= pmax forward steps whose backward part keeps the multiplier <= 2^cap.  A found descent is
an exact certificate on the integer used (n agrees with the point to 2^K, 3^J, K and J far
beyond every walk considered).

The file exists because depth-capped searches (deep_slice_search.py) cannot see descents whose
backward part is about as long as the forward part; the counterexample replayed by
verify_no00_counterexample.py is of that kind.
usage: python3 -X utf8 -B capped_search.py [seconds_per_target]
"""
import math
import random
import sys
import time
from fractions import Fraction as Fr

from deep_slice_search import greedy_word, make_n, rational_residue
from slice_experiments import random_admissible, residue_fast

LN2, LN3 = math.log(2), math.log(3)
GAIN = LN3 - LN2


def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def capped(n, pmax, cap_bits, depth_cap, budget):
    lam_cap = cap_bits * LN2
    t0 = time.time()
    u, prev, lamA, odd_fwd = n, None, 0.0, 0
    nodes = 0
    p_done = -1
    for p in range(0, pmax + 1):
        if time.time() - t0 > budget:
            break
        stack = []
        c = 2 * u
        if c != prev and lamA + LN2 <= lam_cap:
            stack.append((c, 1, 0, lamA + LN2))
        if u % 3 == 2:
            c = (2 * u - 1) // 3
            if c != prev:
                stack.append((c, 1, 1, lamA - GAIN))
        while stack:
            w, q, o, lam = stack.pop()
            nodes += 1
            if w < n:
                return (p, q, odd_fwd, o, w / n), p, nodes, time.time() - t0
            if q >= depth_cap:
                continue
            if lam + LN2 <= lam_cap:
                stack.append((2 * w, q + 1, o, lam + LN2))
            if w % 3 == 2:
                stack.append(((2 * w - 1) // 3, q + 1, o + 1, lam - GAIN))
        p_done = p
        prev = u
        if u % 2:
            lamA += GAIN
            odd_fwd += 1
        else:
            lamA -= LN2
        u = T(u)
    return None, p_done, nodes, time.time() - t0


def show(label, n, pmax, cap_bits, depth_cap, budget):
    best, p_done, nodes, dt = capped(n, pmax, cap_bits, depth_cap, budget)
    if best is None:
        print(f"  {label}: none with p <= {p_done}, multiplier cap 2^{cap_bits}, backward depth "
              f"<= {depth_cap} ({nodes} nodes, {dt:.1f}s)  EMPIRICAL")
    else:
        p, q, of, ob, ratio = best
        kind = "purely 2-adic (valid for every 3-adic coordinate)" if ob <= of else \
            "uses the 3-adic coordinate"
        print(f"  {label}: DESCENT p = {p} forward ({of} odd), q = {q} backward ({ob} odd), "
              f"w/n = {ratio:.6f}; {kind}  ({nodes} nodes, {dt:.1f}s)")
    return best


if __name__ == '__main__':
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 30.0
    K = J = 700
    print(f"precision 2^{K}, 3^{J}")
    show("(-1, 0)  [control, proved obstruction]",
         make_n(rational_residue(-1, K), K, 0, J), 400, 16, 400, budget)
    show("(-5, 0)  [control, proved obstruction]",
         make_n(rational_residue(-5, K), K, 0, J), 400, 16, 400, budget)
    w29 = [int(c) for c in '11101101101101010101101101101'] + [1] * (K - 29)
    show("(word 11101101101101010101101101101 1^inf, 0)  [control, descent expected at p = 29]",
         make_n(residue_fast(w29), K, 0, J), 60, 16, 400, budget)
    show("(-17, 0)", make_n(rational_residue(-17, K), K, 0, J), 400, 16, 400, budget)
    show("(-19/11, 0)", make_n(rational_residue(Fr(-19, 11), K), K, 0, J), 400, 16, 400, budget)
    show("(greedy word, 0)", make_n(residue_fast(greedy_word(K)), K, 0, J), 400, 16, 400, budget)

    rng = random.Random(20261121)
    Kw, pm = 360, 300
    for label, ndz in (("no two consecutive even steps", True), ("unrestricted", False)):
        t0 = time.time()
        found = []
        total = 30
        pure = 0
        for _ in range(total):
            bits = random_admissible(Kw, rng, ndz)
            n = make_n(residue_fast(bits), Kw, 0, Kw)
            best, p_done, nodes, dt = capped(n, pm, 12, 400, budget / 6)
            if best is not None:
                found.append(best)
                pure += best[3] <= best[2]
        ps = sorted(b[0] for b in found)
        print(f"  {total} random admissible words ({label}), y0 = 0, p <= {pm}, cap 2^12: "
              f"descent for {len(found)}/{total}"
              + (f" (purely 2-adic: {pure}); forward lengths p: min {ps[0]}, median "
                 f"{ps[len(ps) // 2]}, max {ps[-1]}" if found else "")
              + f"  ({time.time() - t0:.1f}s)")
