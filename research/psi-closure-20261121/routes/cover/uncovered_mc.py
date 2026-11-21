#!/usr/bin/env python3
"""
How fast does the set of points with no descending path of length <= L shrink?

Evidence tier: EMPIRICAL (Monte Carlo with a fixed seed).  Each sample is a random 180-bit
integer n, i.e. an (almost) Haar-random point of Z_2 x Z_3 to precision far beyond the walk
lengths used.  For walks of length <= 34 from such n, "the endpoint is < n" is the same as
"the multiplier alpha is < 1".

  sigma_f(n) = least k with T^k(n) < n                      (forward-only certificate)
  sigma_o(n) = least L such that some ordinary walk of length L from n ends below n
               (forward and backward moves in any order)

Prints the tails P(sigma > L) and the per-step decay factor over the last ten steps.
usage: python3 -X utf8 -B uncovered_mc.py [samples] [Lmax] [seed]
"""
import random
import sys
import time


def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def sigma_forward(n, cap):
    m = n
    for k in range(1, cap + 1):
        m = T(m)
        if m < n:
            return k
    return cap + 1


def sigma_ordinary(n, cap):
    seen = {n}
    frontier = [n]
    for d in range(1, cap + 1):
        nxt = []
        for w in frontier:
            c = T(w)
            if c not in seen:
                if c < n:
                    return d
                seen.add(c)
                nxt.append(c)
            c = 2 * w
            if c not in seen:
                seen.add(c)
                nxt.append(c)
            if w % 3 == 2:
                c = (2 * w - 1) // 3
                if c not in seen:
                    if c < n:
                        return d
                    seen.add(c)
                    nxt.append(c)
        frontier = nxt
    return cap + 1


def main():
    samples = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    Lmax = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 20261121
    rng = random.Random(seed)
    t0 = time.time()
    hf = [0] * (Lmax + 2)
    ho = [0] * (Lmax + 2)
    for _ in range(samples):
        n = rng.getrandbits(180) | (1 << 180)
        sf = sigma_forward(n, Lmax)
        so = sigma_ordinary(n, min(sf, Lmax)) if sf <= Lmax else sigma_ordinary(n, Lmax)
        assert so <= sf
        hf[sf] += 1
        ho[so] += 1
    print(f"samples {samples}, seed {seed}, Lmax {Lmax}, time {time.time() - t0:.1f}s")
    print("  L   P(sigma_f > L)   P(sigma_o > L)   ratio")
    tf = to = samples
    tails = {}
    for L in range(1, Lmax + 1):
        tf -= hf[L]
        to -= ho[L]
        tails[L] = (tf / samples, to / samples)
        if L <= 12 or L % 2 == 0:
            ratio = (to / tf) if tf else float('nan')
            print(f" {L:2d}   {tf / samples:10.5f}      {to / samples:10.5f}     {ratio:6.3f}")
    a, b = Lmax - 10, Lmax
    for name, idx in (("forward-only", 0), ("ordinary", 1)):
        if tails[b][idx] > 0 and tails[a][idx] > 0:
            f = (tails[b][idx] / tails[a][idx]) ** (1 / (b - a))
            print(f"  {name}: mean per-step decay factor over L = {a}..{b}: {f:.4f}")
    print("  reference: 2^-(1 - H(log 2 / log 3)) = 0.9659 is the exponential rate of the "
          "forward-only tail (large deviations of the parity word)")


if __name__ == '__main__':
    main()
