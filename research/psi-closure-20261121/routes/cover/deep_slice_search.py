#!/usr/bin/env python3
"""
Deeper targeted search for descending ordinary paths at points (x0, y0) whose 2-adic
coordinate has a non-stopping parity word.

Evidence tier: EMPIRICAL (bounded search).  "none found" proves nothing beyond the bounds
printed; "descent found" is an exact certificate (the walk is replayed on an actual integer).

Method.  Take an actual integer n agreeing with x0 to 2^K and with y0 to 3^J, K and J far
larger than every walk considered.  For p = 0..pmax walk forward to T^p(n) and explore the
side tree of backward moves of depth <= D hanging off T^p(n) (the edge back to T^(p-1)(n)
excluded).  A branch is pruned only when even D - q further odd backward steps (factor 2/3
each) could not bring its multiplier below 1, so the search is exhaustive for
  { forward steps p <= pmax,  backward steps q <= D }.
usage: python3 -X utf8 -B deep_slice_search.py [seconds_per_target]
"""
import math
import sys
import time
from fractions import Fraction as Fr

LN2, LN3 = math.log(2), math.log(3)
GAIN = LN3 - LN2            # best possible decrease of log(multiplier) per backward step


def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def greedy_word(K):
    bits, num, den = [], 1, 1
    for _ in range(K):
        if num > 2 * den:
            bits.append(0)
            den *= 2
        else:
            bits.append(1)
            num *= 3
            den *= 2
    return bits


def residue_of_word(bits):
    x = 0
    for k, b in enumerate(bits):
        m = x
        for _ in range(k):
            m = T(m)
        if m % 2 != b:
            x += 1 << k
    return x


def make_n(r, K, y0, J):
    """n = r (mod 2^K), n = y0 (mod 3^J), n > 2^K 3^J"""
    M2, M3 = 2 ** K, 3 ** J
    s = ((y0 - r) * pow(M2, -1, M3)) % M3
    n = r + M2 * (s + M3)
    assert n % M2 == r % M2 and (n - y0) % M3 == 0
    return n


def rational_residue(x0, K):
    x0 = Fr(x0)
    return (x0.numerator * pow(x0.denominator, -1, 2 ** K)) % 2 ** K


def deep(n, pmax, D, budget):
    t0 = time.time()
    u, prev, lamA = n, None, 0.0
    nodes = 0
    best = None
    p_done = -1
    for p in range(0, pmax + 1):
        if time.time() - t0 > budget:
            break
        stack = []
        c = 2 * u
        if c != prev and lamA + LN2 - (D - 1) * GAIN < 0:
            stack.append((c, 1, 0, lamA + LN2))
        if u % 3 == 2:
            c = (2 * u - 1) // 3
            if c != prev:
                stack.append((c, 1, 1, lamA - GAIN))
        while stack:
            w, q, o, lam = stack.pop()
            nodes += 1
            if w < n:
                if best is None or p + q < best[0] + best[1]:
                    best = (p, q, o, w)
                continue
            if q == D:
                continue
            rem = D - q - 1
            if lam + LN2 - rem * GAIN < 0:
                stack.append((2 * w, q + 1, o, lam + LN2))
            if w % 3 == 2 and lam - GAIN - rem * GAIN < 0:
                stack.append(((2 * w - 1) // 3, q + 1, o + 1, lam - GAIN))
        p_done = p
        if best is not None:
            break
        prev = u
        if u % 2:
            lamA += GAIN
        else:
            lamA -= LN2
        u = T(u)
    return best, p_done, nodes, time.time() - t0


def report(label, n, pmax, D, budget):
    best, p_done, nodes, dt = deep(n, pmax, D, budget)
    if best is None:
        print(f"  {label}: no descending path with p <= {p_done} forward and q <= {D} "
              f"backward steps ({nodes} nodes, {dt:.1f}s)  EMPIRICAL")
    else:
        p, q, o, w = best
        num, den = 3 ** 0, 1
        print(f"  {label}: DESCENT with p = {p} forward, q = {q} backward steps "
              f"({o} odd): w/n = {w / n:.6f}  ({nodes} nodes, {dt:.1f}s)  "
              f"=> not an obstruction point")


if __name__ == '__main__':
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 30.0
    K = J = 700
    print(f"precision 2^{K}, 3^{J}")
    # controls: proved obstruction points
    report("(-1, 0)   [control, proved]", make_n(rational_residue(-1, K), K, 0, J), 300, 30,
           budget)
    report("(-5, 0)   [control, proved]", make_n(rational_residue(-5, K), K, 0, J), 300, 30,
           budget)
    # control: a non-stopping word with an explicit descent (word 111100 then 1^infinity)
    report("(-43/27, 0) [control, descent expected]",
           make_n(rational_residue(Fr(-43, 27), K), K, 0, J), 300, 30, budget)
    report("(-17, 0)", make_n(rational_residue(-17, K), K, 0, J), 300, 30, budget)
    report("(-19/11, 0)", make_n(rational_residue(Fr(-19, 11), K), K, 0, J), 300, 30, budget)
    g = residue_of_word(greedy_word(K))
    for y0 in (0, 1, 3, 7):
        report(f"(greedy word, {y0})", make_n(g, K, y0, J), 400, 30, budget)
