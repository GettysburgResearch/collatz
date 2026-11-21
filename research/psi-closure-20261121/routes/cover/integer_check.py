#!/usr/bin/env python3
"""
Integer-level replay of the obstruction theorem at the point (-1, 0) of Z_2 x Z_3.

Evidence tier: exhaustive bounded computation with Python big integers on ACTUAL positive
integers (no shadows, no rationals).  Independent of shadow_bfs.py.

Theorem Z (proved in NOTES.md; Lean: CoverObstruction.no_descent / no_short_walk_descent):
    Let n >= 1, 2^K | n+1, 3^J | n.  If T^q(w) = T^p(n) with p <= K and the first q steps of w
    contain at most p + J odd steps, then w >= n.
    In particular every integer reachable from n by an ordinary walk of length <= min(K, J)
    (forward T-steps and backward T-steps in any order) is >= n.

Checks:
  [1] walk balls: for L = 0..Lmax and several n with 2^L | n+1, 3^L | n, the whole ball of
      radius L around n in the Collatz graph has minimum n.
  [2] meet form with K != J, including the bound "at most p + J odd backward steps".
  [3] sharpness / illustration: the shortest ordinary descending walk from the least n of each
      class K = J = k (it must be longer than k).
"""
import sys
import time


def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def class_rep(K, J, t=0):
    """least positive n with n = -1 (mod 2^K), n = 0 (mod 3^J), plus t*2^K*3^J."""
    M2, M3 = 2 ** K, 3 ** J
    s = (-pow(M3, -1, M2)) % M2 if K > 0 else 0
    n = M3 * s
    if n == 0:
        n = M2 * M3
    assert (n + 1) % M2 == 0 and n % M3 == 0 and n > 0
    return n + t * M2 * M3


def ball(n, L, stop_below=None):
    """all integers reachable from n by ordinary walks of length <= L; value -> (dist, parent)"""
    dist = {n: (0, None)}
    frontier = [n]
    for d in range(1, L + 1):
        nxt = []
        for w in frontier:
            cand = [T(w), 2 * w]
            if w % 3 == 2:
                cand.append((2 * w - 1) // 3)
            for c in cand:
                if c not in dist:
                    dist[c] = (d, w)
                    nxt.append(c)
                    if stop_below is not None and c < stop_below:
                        return dist, c
        frontier = nxt
    return dist, None


def check1(Lmax):
    t0 = time.time()
    total = 0
    for L in range(0, Lmax + 1):
        ts = range(0, 4) if L <= 24 else range(0, 1)
        for t in ts:
            n = class_rep(L, L, t)
            b, _ = ball(n, L)
            total += len(b)
            assert min(b) == n, (L, t, n, min(b))
    print(f"[1] walk balls radius L around n = -1 (2^L), 0 (3^L), L = 0..{Lmax}: "
          f"minimum is always n  ({total} nodes, {time.time() - t0:.1f}s)  PASS")


def check2(Q):
    t0 = time.time()
    total = 0
    pairs = [(0, 20), (1, 20), (2, 20), (3, 12), (12, 3), (20, 0), (20, 1), (20, 2), (6, 6),
             (9, 4), (4, 9)]
    for (K, J) in pairs:
        for t in (0, 1, 5):
            n = class_rep(K, J, t)
            u = n
            for p in range(0, K + 1):
                if p > 0:
                    assert u % 2 == 1
                    u = T(u)
                # backward tree from u = T^p(n): at most p + J odd steps, depth <= Q
                stack = [(u, 0, 0)]
                while stack:
                    w, q, o = stack.pop()
                    total += 1
                    assert w >= n, (K, J, t, p, q, o, w, n)
                    if w == n:
                        assert (q, o) == (p, p)
                    if q == Q:
                        continue
                    stack.append((2 * w, q + 1, o))
                    if w % 3 == 2 and o + 1 <= p + J:
                        stack.append(((2 * w - 1) // 3, q + 1, o + 1))
    print(f"[2] meet form T^q(w) = T^p(n), p <= K, odd steps <= p + J, q <= {Q}: "
          f"w >= n on {total} nodes ({time.time() - t0:.1f}s)  PASS")


def walk_shape(b, n, w):
    """(forward steps p, backward steps q, odd backward steps o) of the BFS walk n -> w"""
    path = []
    cur = w
    while cur != n:
        par = b[cur][1]
        path.append((par, cur))
        cur = par
    path.reverse()
    p = q = o = 0
    for (a, c) in path:
        if c == T(a):
            p += 1            # forward step a -> T(a)
        else:                 # backward step: T(c) == a
            assert T(c) == a
            q += 1
            if c % 2 == 1:
                o += 1
    return p, q, o, len(path)


def check3(kmax, Lcap):
    print(f"[3] shortest ordinary descending walk from the least n with n = -1 (2^k), "
          f"n = 0 (3^k)  (search radius <= {Lcap}):")
    for k in range(1, kmax + 1):
        t0 = time.time()
        n = class_rep(k, k)
        b, hit = ball(n, Lcap, stop_below=n)
        if hit is None:
            print(f"    k={k}: n={n}: no smaller integer within radius {Lcap} "
                  f"({len(b)} nodes, {time.time() - t0:.1f}s)")
            continue
        p, q, o, length = walk_shape(b, n, hit)
        assert length > k
        # forward stopping time for comparison
        m, st = n, 0
        while m >= n and st < 10 ** 6:
            m = T(m)
            st += 1
        print(f"    k={k}: n={n}: w={hit} at walk length {length} (> k) "
              f"[p={p} forward, q={q} backward of which {o} odd]; "
              f"forward-only stopping time {st}")


if __name__ == '__main__':
    Lmax = int(sys.argv[1]) if len(sys.argv) > 1 else 36
    check1(Lmax)
    check2(24)
    check3(9, 40)
    print("RESULT: PASS")
