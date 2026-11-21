#!/usr/bin/env python3
"""
Other candidate obstruction points: 2-adic coordinate on an expanding negative cycle or on a
non-stopping parity word, 3-adic coordinate 0.

Evidence tiers:
  [C1] (-5, 0): replay of the invariants used in the WRITTEN proof of Theorem C (NOTES.md) on
       every node within the search depth (exact rationals).
  [C2] integer balls for the classes n = x0 (mod 2^L), n = 0 (mod 3^L), x0 in {-5, -17, -19/11}:
       exhaustive for the listed L.  For x0 = -5 this replays Theorem C; for the others it is
       EMPIRICAL (no proof here).
  [C3] shadow search at (-17, 0) and (-19/11, 0): EMPIRICAL.
  [C4] the "greedy" non-stopping parity word (smallest admissible ratio 3^o/2^k > 1), 3-adic
       coordinate 0: EMPIRICAL search for a descending walk.
usage: python3 -X utf8 -B cycle_points.py [depth]
"""
import sys
import time
from fractions import Fraction as Fr

from shadow_bfs import explore


def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def ball_min(n, L):
    seen = {n}
    frontier = [n]
    mn = n
    for _ in range(L):
        nxt = []
        for w in frontier:
            cand = [T(w), 2 * w]
            if w % 3 == 2:
                cand.append((2 * w - 1) // 3)
            for c in cand:
                if c not in seen:
                    seen.add(c)
                    nxt.append(c)
                    if c < mn:
                        mn = c
        frontier = nxt
    return mn, len(seen)


def first_descent_radius(n, Lmax):
    seen = {n}
    frontier = [n]
    for d in range(1, Lmax + 1):
        nxt = []
        for w in frontier:
            cand = [T(w), 2 * w]
            if w % 3 == 2:
                cand.append((2 * w - 1) // 3)
            for c in cand:
                if c not in seen:
                    if c < n:
                        return d, c, len(seen)
                    seen.add(c)
                    nxt.append(c)
        frontier = nxt
    return None, None, len(seen)


def class_rep(x0, L, J=None):
    """least n > 0 with n = x0 in Z/2^L (x0 rational with odd denominator), n = 0 (mod 3^J)"""
    J = L if J is None else J
    x0 = Fr(x0)
    M2, M3 = 2 ** L, 3 ** J
    r = (x0.numerator * pow(x0.denominator, -1, M2)) % M2 if L > 0 else 0
    # n = M3 * s, M3 * s = r (mod M2)
    s = (r * pow(M3, -1, M2)) % M2 if L > 0 else 1
    n = M3 * s
    if n == 0:
        n = M2 * M3
    assert (n - r) % M2 == 0 and n % M3 == 0 and n > 0
    return n


def c1(depth):
    t0 = time.time()
    seen, best, descents, d = explore(-5, 0, depth)
    start = (Fr(-5), Fr(0))
    bad = 0
    small_y = {}
    for (x, y), (a, path) in seen.items():
        p_odd, s = path.count('o'), path.count('S')
        ok = (a == (y - x) / 5) and (a >= 1) and (a > 1 or (x, y) == start) and x < 0
        if s <= p_odd:                       # phase 1 (and level nodes): x integer <= -5, y >= 0
            ok = ok and x.denominator == 1 and x <= -5 and y >= 0
            if s == p_odd:
                ok = ok and y.denominator == 1
        else:                                # phase 2: y positive integer, |x| > 1
            ok = ok and y.denominator == 1 and y >= 1 and x < -1
            if y <= 3:
                small_y[y] = min(small_y.get(y, a), a)
        if not ok:
            bad += 1
    print(f"[C1] point (-5,0): depth {d}, nodes {len(seen)}, invariant violations {bad}, "
          f"descending paths {len(descents)}, smallest non-trivial alpha {best[0]} "
          f"('{best[2]}'), {time.time() - t0:.1f}s")
    print("     smallest alpha at phase-2 nodes with 3-adic shadow y'' in {1,2,3}: "
          + ", ".join(f"y''={k}: {v}" for k, v in sorted(small_y.items())))
    return bad == 0 and not descents


def c2(Lmax):
    ok = True
    for x0, label in ((-5, "proved (Theorem C)"), (-17, "EMPIRICAL"), (Fr(-19, 11), "EMPIRICAL")):
        t0 = time.time()
        total = 0
        fails = []
        for L in range(1, Lmax + 1):
            n = class_rep(x0, L)
            mn, size = ball_min(n, L)
            total += size
            if mn != n:
                fails.append((L, n, mn))
        print(f"[C2] x0 = {x0}: balls of radius L around the least n = x0 (2^L), 0 (3^L), "
              f"L = 1..{Lmax}: {'minimum is always n' if not fails else 'FAILS ' + str(fails[:3])}"
              f"  ({total} nodes, {time.time() - t0:.1f}s)  [{label}]")
        if fails and x0 == -5:
            ok = False
    return ok


def c3(depth):
    for x0 in (Fr(-17), Fr(-19, 11)):
        t0 = time.time()
        seen, best, descents, d = explore(x0, 0, depth, stop_at_descent=True)
        if descents:
            a, beta, path, node = min(descents, key=lambda r: len(r[2]))
            print(f"[C3] ({x0},0): DESCENT length {len(path)} alpha={a} path={path}")
        else:
            print(f"[C3] ({x0},0): no descending path of length <= {d} ({len(seen)} nodes, "
                  f"min alpha {best[0]}, {time.time() - t0:.1f}s)  EMPIRICAL")


def greedy_word(K):
    """parity word with 3^o > 2^k for every prefix and the ratio kept as small as possible"""
    bits, num, den = [], 1, 1
    for _ in range(K):
        if num > 2 * den:            # a 0 keeps the ratio above 1
            bits.append(0)
            den *= 2
        else:
            bits.append(1)
            num *= 3
            den *= 2
        assert num > den
    return bits


def residue_of_word(bits):
    """the residue x mod 2^K whose first K parities are `bits`"""
    x = 0
    for k, b in enumerate(bits):
        m = x
        for _ in range(k):
            m = T(m)
        if m % 2 != b:
            x += 1 << k
    m = x
    for b in bits:
        assert m % 2 == b
        m = T(m)
    return x


def c4(K, J, Lmax):
    bits = greedy_word(K)
    r = residue_of_word(bits)
    M2, M3 = 2 ** K, 3 ** J
    print(f"[C4] greedy non-stopping word, first 24 bits {''.join(map(str, bits[:24]))}")
    for y0 in (0, 3, 6, 9, 27, 81):
        # n = r (mod 2^K), n = y0 (mod 3^J)
        s = ((y0 - r) * pow(M2, -1, M3)) % M3
        n = r + M2 * (s + M3)
        assert n % M2 == r and (n - y0) % M3 == 0
        t0 = time.time()
        d, w, size = first_descent_radius(n, Lmax)
        if d is None:
            print(f"     y0={y0}: no descending walk of length <= {Lmax} ({size} nodes, "
                  f"{time.time() - t0:.1f}s)  EMPIRICAL")
        else:
            print(f"     y0={y0}: descending walk of length {d} exists  "
                  f"(so this point is NOT an obstruction point)")


if __name__ == '__main__':
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 38
    ok = c1(depth)
    ok = c2(34) and ok
    c3(depth)
    c4(70, 70, 34)
    print("RESULT:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
