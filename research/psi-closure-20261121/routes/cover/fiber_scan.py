#!/usr/bin/env python3
"""
Which points (-1, y0), y0 a positive integer, are obstruction points?

Evidence tier: for each y0 <= N the answer printed here is an exact finite decision, GIVEN the
criterion of Theorem B in NOTES.md (written proof).  Nothing here is a statement about y0 > N.

Theorem B (fiber criterion).  Let y0 >= 1 be an integer.  The point (-1, y0) of Z_2 x Z_3 has a
descending ordinary path  iff  there are integers y'' >= 1, t >= 1 and a node B of the backward
tree of 1 under S(c) = c/2 | (3c-1)/2, with j = number of even S-steps from B down to 1, with
        T^t(y'') = 2^j (y0 + 1) - B      and      3^o > 2^(j+t),
where o is the number of odd steps among the first t steps of y''.  Any such y'' is < y0, so
for fixed y0 the search is finite.

Checks performed:
  [scan]    all y0 <= N decided; statistics.
  [replay]  every certificate is replayed on actual integers n = -1 (mod 2^K), n = y0 (mod 3^J)
            as a legal ordinary walk ending at w < n   (independent of the criterion).
  [cross]   for small y0 the verdict is compared with the exhaustive shadow search.
usage: python3 -X utf8 -B fiber_scan.py [N]
"""
import sys
import time
from fractions import Fraction as Fr


def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def S(c):
    return c // 2 if c % 2 == 0 else (3 * c - 1) // 2


class Tree:
    """backward S-tree of 1, stored by number j of doublings; odd[B] = number of odd S-steps"""

    def __init__(self):
        self.levels = [[1]]
        self.odd = {1: 0}

    def level(self, j):
        while len(self.levels) <= j:
            jj = len(self.levels)
            cur = []
            stack = [(2 * b, self.odd[b]) for b in self.levels[-1]]
            while stack:
                b, p = stack.pop()
                assert 1 <= b <= 2 ** jj          # Lemma: B <= 2^j
                cur.append(b)
                self.odd[b] = p
                if b % 3 == 1:
                    stack.append(((2 * b + 1) // 3, p + 1))
            self.levels.append(cur)
        return self.levels[j]


def scan(N):
    tree = Tree()
    cert = {}
    max_j = 0
    for ypp in range(1, N):
        m, t, o, num, den = ypp, 0, 0, 1, 1          # num = 3^o, den = 2^t
        while True:
            if m % 2:
                m = (3 * m + 1) // 2
                num *= 3
                o += 1
            else:
                m //= 2
            den *= 2
            t += 1
            if num > den:
                j = 0
                while (den << j) < num:
                    pw = 1 << j
                    for B in tree.level(j):
                        if (m + B) & (pw - 1) == 0:
                            y0 = (m + B) // pw - 1
                            assert y0 >= 1              # y0 = 0 would contradict Theorem A
                            assert ypp < y0             # predicted by the theory
                            if y0 <= N:
                                length = 2 * tree.odd[B] + j + t
                                if y0 not in cert or length < cert[y0][0]:
                                    cert[y0] = (length, ypp, t, o, j, B)
                    j += 1
                    max_j = max(max_j, j)
            if m == 1:
                break
    return cert, tree, max_j


def crt(K, J, y0, shift=0):
    """an n with n = -1 (mod 2^K), n = y0 (mod 3^J), n > 6^... large"""
    M2, M3 = 2 ** K, 3 ** J
    # n = -1 + M2 * s,  M2*s = y0 + 1 (mod M3)
    s = ((y0 + 1) * pow(M2, -1, M3)) % M3
    n = -1 + M2 * (s + M3 * (1 + shift))
    assert (n + 1) % M2 == 0 and (n - y0) % M3 == 0 and n > 0
    return n


def replay(y0, c, tree):
    """replay the certificate as an ordinary walk on an actual integer; return walk length"""
    length, ypp, t, o, j, B = c
    pB = tree.odd[B]
    for shift in (0, 1, 7):
        n = crt(pB + 3, o + 3, y0, shift)
        w = n
        steps = 0
        for _ in range(pB):                     # forward part: all odd steps
            assert w % 2 == 1
            w = T(w)
            steps += 1
        traj = [B]                              # S-trajectory of B down to 1
        while traj[-1] != 1:
            traj.append(S(traj[-1]))
        assert sum(1 for b in traj[:-1] if b % 2) == pB
        assert sum(1 for b in traj[:-1] if b % 2 == 0) == j
        for b in reversed(traj[:-1]):           # climb the tree of -1 from -1 to -B
            if b % 2 == 0:
                w = 2 * w
            else:
                assert w % 3 == 2
                w = (2 * w - 1) // 3
            steps += 1
        assert w == 2 ** j * (n + 1) - B        # level node
        z = [ypp]
        for _ in range(t):
            z.append(T(z[-1]))
        assert z[-1] == 2 ** j * (y0 + 1) - B
        for a in reversed(z[:-1]):              # climb the 3-adic shadow from y' down to y''
            if a % 2 == 0:
                w = 2 * w
            else:
                assert w % 3 == 2
                w = (2 * w - 1) // 3
            steps += 1
        assert 3 ** o * (w - ypp) == 2 ** (j + t) * (n - y0)    # w = alpha (n - y0) + y''
        assert 0 < w < n
        assert steps == length
    return length


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 60000
    t0 = time.time()
    cert, tree, max_j = scan(N)
    obst = [y for y in range(1, N + 1) if y not in cert]
    print(f"[scan] N = {N}: {len(obst)} obstruction points (-1, y0) with 1 <= y0 <= N, "
          f"{len(cert)} points with a descending path; tree levels used j < {max_j}; "
          f"{time.time() - t0:.1f}s")
    for r in range(3):
        tot = len([y for y in range(1, N + 1) if y % 3 == r])
        ob = len([y for y in obst if y % 3 == r])
        print(f"       y0 = {r} mod 3: obstruction fraction {ob}/{tot} = {ob / tot:.4f}")
    print("       by 3-adic valuation (y0 divisible by 3^M): obstruction fraction")
    M = 1
    while 3 ** M * 20 <= N:
        tot = N // 3 ** M
        ob = len([y for y in obst if y % 3 ** M == 0])
        print(f"         M={M}: {ob}/{tot} = {ob / tot:.4f}")
        M += 1
    print("       first obstruction y0:", obst[:40])
    non3 = sorted(y for y in cert if y % 3 == 0)[:12]
    print("       first multiples of 3 WITH a descending path (y0: length, y'', t, o, j, B):")
    for y in non3:
        print(f"         {y}: {cert[y]}")
    lens = sorted(c[0] for c in cert.values())
    print(f"       certificate lengths: min {lens[0]}, median {lens[len(lens) // 2]}, "
          f"max {lens[-1]}")

    t0 = time.time()
    for y0, c in cert.items():
        replay(y0, c, tree)
    print(f"[replay] all {len(cert)} certificates replayed on actual integers as legal "
          f"ordinary walks with w < n ({time.time() - t0:.1f}s)  PASS")

    try:
        from shadow_bfs import explore
    except ImportError:
        print("[cross] shadow_bfs.py not importable; skipped")
        return
    depth = 22
    agree = 0
    for y0 in range(1, 46):
        seen, best, descents, d = explore(Fr(-1), Fr(y0), depth, stop_at_descent=True)
        found = bool(descents)
        if found:
            assert y0 in cert, y0                       # BFS descent => criterion descent
            shortest = min(len(r[2]) for r in descents)
            assert shortest <= cert[y0][0], (y0, shortest, cert[y0])
        else:
            assert y0 not in cert or cert[y0][0] > depth, (y0, cert.get(y0))
        agree += 1
    print(f"[cross] criterion and exhaustive shadow search (depth {depth}) agree on "
          f"{agree} values y0 = 1..45  PASS")
    print("RESULT: PASS")


if __name__ == '__main__':
    main()
