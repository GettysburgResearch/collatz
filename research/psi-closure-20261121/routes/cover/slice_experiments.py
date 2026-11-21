#!/usr/bin/env python3
"""
Experiments on which points (x0, y0) with a non-stopping 2-adic coordinate are obstruction
points.  Uses deep_slice_search.deep (exhaustive for forward steps p <= pmax and backward steps
q <= D; see that file).

Evidence tier: EMPIRICAL.  "no descent" = none within the stated bounds.  "descent" = exact.

  [E0] controls: points of the fiber over -1 with known shortest certificates.
  [E1] the greedy non-stopping word (ratio 3^o/2^k kept minimal, never two consecutive
       even steps) with y0 = 0..45, compared with the fiber over -1.
  [E2] the greedy word with random 3-adic y0.
  [E3] random admissible (non-stopping) words with y0 = 0:
       (a) no two consecutive even steps, (b) unrestricted.
usage: python3 -X utf8 -B slice_experiments.py
"""
import random
import time
from fractions import Fraction as Fr

from deep_slice_search import deep, greedy_word, make_n, rational_residue


def residue_fast(bits):
    """residue x mod 2^K with parity word `bits`, in O(K) big-integer steps"""
    x, m, pow3 = 0, 0, 1          # m = T^k(x), pow3 = 3^(odd steps so far)
    for k, b in enumerate(bits):
        if m % 2 != b:
            x += 1 << k
            m += pow3
        if b:
            m = (3 * m + 1) // 2
            pow3 *= 3
        else:
            m //= 2
    return x


def random_admissible(K, rng, no_double_zero):
    bits, num, den = [], 1, 1
    for _ in range(K):
        can_zero = num > 2 * den and not (no_double_zero and bits and bits[-1] == 0)
        b = rng.randint(0, 1) if can_zero else 1
        bits.append(b)
        if b:
            num *= 3
        den *= 2
        assert num > den
    return bits


def main():
    K = J = 500
    PMAX, D, BUDGET = 300, 30, 20.0
    rng = random.Random(20261121)

    print("[E0] controls in the fiber over -1 (expected shortest certificates: y0=4: p=0,q=3; "
          "y0=10: p=0,q=6; y0=30: p=1,q=12)")
    r1 = rational_residue(-1, K)
    for y0 in (4, 10, 30):
        best, p_done, nodes, dt = deep(make_n(r1, K, y0, J), PMAX, D, BUDGET)
        print(f"     (-1,{y0}): found {best[:3] if best else None} (p, q, odd)")

    g = residue_fast(greedy_word(K))
    assert g == residue_fast(greedy_word(K))
    obst_minus_one = [1, 3, 6, 7, 9, 12, 15, 16, 18, 19, 21, 24, 25, 27, 28, 33, 36, 37, 39,
                      42, 43, 45]
    t0 = time.time()
    nodesc = []
    desc = {}
    for y0 in range(0, 46):
        best, p_done, nodes, dt = deep(make_n(g, K, y0, J), PMAX, D, BUDGET)
        if best is None:
            nodesc.append(y0)
        else:
            desc[y0] = best[:3]
    print(f"[E1] greedy word, y0 = 0..45, bounds p <= {PMAX}, q <= {D} ({time.time() - t0:.1f}s)")
    print(f"     no descent found for y0 in {nodesc}")
    print(f"     (fiber over -1: obstruction y0 in [0] + {obst_minus_one})")
    print(f"     descents (y0: p, q, odd): {desc}")

    t0 = time.time()
    cnt = 0
    for _ in range(60):
        y0 = rng.getrandbits(900) % 3 ** J
        best, p_done, nodes, dt = deep(make_n(g, K, y0, J), PMAX, D, BUDGET)
        cnt += best is not None
    print(f"[E2] greedy word, 60 random 3-adic y0: descent found for {cnt}/60 "
          f"({time.time() - t0:.1f}s)")
    cnt = 0
    for _ in range(60):
        y0 = 3 * (rng.getrandbits(900) % 3 ** (J - 1))
        best, p_done, nodes, dt = deep(make_n(g, K, y0, J), PMAX, D, BUDGET)
        cnt += best is not None
    print(f"     greedy word, 60 random y0 in 3 Z_3: descent found for {cnt}/60")
    cnt = 0
    for _ in range(60):
        y0 = 3 * (rng.getrandbits(900) % 3 ** (J - 1))
        best, p_done, nodes, dt = deep(make_n(r1, K, y0, J), PMAX, D, BUDGET)
        cnt += best is not None
    print(f"     word 1^inf (x0 = -1), 60 random y0 in 3 Z_3: descent found for {cnt}/60 "
          f"(compare 2.6% of integer multiples of 3 below 10^6)")

    for label, ndz in (("(a) no two consecutive even steps", True), ("(b) unrestricted", False)):
        t0 = time.time()
        found = []
        total = 100
        for _ in range(total):
            bits = random_admissible(K, rng, ndz)
            n = make_n(residue_fast(bits), K, 0, J)
            best, p_done, nodes, dt = deep(n, PMAX, D, BUDGET)
            if best is not None:
                found.append(best[:3])
        lens = sorted(p + q for (p, q, o) in found)
        print(f"[E3] {label}: {total} random admissible words, y0 = 0: descent found for "
              f"{len(found)}/{total}" + (f"; walk lengths min {lens[0]}, median "
              f"{lens[len(lens) // 2]}, max {lens[-1]}; one-backward-step descents: "
              f"{sum(1 for f in found if f[1] == 1)}" if found else "")
              + f" ({time.time() - t0:.1f}s)")


if __name__ == '__main__':
    main()
