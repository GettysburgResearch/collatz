"""Independent inverse-terminal enumeration and exact original/tilted law tests."""

from fractions import Fraction as F
from itertools import combinations
from math import comb
import json


def check(a, n):
    cap = int(a * n)
    b = a / (2 * (a - 1))
    original = F(0)
    tilted = F(0)
    weighted = [F(0) for _ in range(cap + 1)]
    small = {}
    seeds = set()
    max_terminal = 0
    tests = 0
    for h in range(n, cap + 1):
        for cuts in combinations(range(1, h), n - 1):
            levels = (0,) + cuts + (h,)
            if any(levels[i] > a * i for i in range(1, n + 1)):
                continue
            e = [levels[i + 1] - levels[i] for i in range(n)]
            N = sum((1 << levels[i]) * 3 ** (n - 1 - i) for i in range(n))
            residue = N * pow(1 << h, -1, 3 ** n) % (3 ** n)
            terminal = residue if residue % 2 else residue + 3 ** n
            z = terminal
            for v in reversed(e):
                z, rem = divmod((z << v) - 1, 3)
                assert rem == 0 and z > 0 and z % 2
            m = z
            assert m < 1 << (h + 1) and m not in seeds
            seeds.add(m)
            G = F(0)
            for i, v in enumerate(e):
                assert z == F(3 ** i, 1 << levels[i]) * (m + G)
                assert G < (1 << (levels[i] - i)) or i == 0
                G += F(1 << levels[i], 3 ** (i + 1))
                z, rem = divmod(3 * z + 1, 1 << v)
                assert rem == 0 and z % 2
            assert z == terminal and terminal < 2 * 3 ** n
            po = F(1, 1 << h)
            pt = (a - 1) ** (-n) * ((a - 1) / a) ** h
            assert po == pt * (a - 1) ** n * b ** h
            original += po
            tilted += pt
            weighted[h] += po
            small[m] = (h, po)
            for zeta in (F(0), F(2, 3), F(9, 4)):
                Z = (1 << h) / (m + zeta * G)
                assert Z == F(3 ** n, terminal) * (m + G) / (m + zeta * G)
                assert F(1, 2) / max(1, zeta) <= Z <= F(1 << cap, m)
                tests += 1
            max_terminal = max(terminal, max_terminal)
    assert original >= F(comb(cap - 1, n - 1), n << cap)
    assert original <= (a - 1) ** n * b ** cap * tilted
    for j in range(cap + 1):
        cutoff = 1 << j
        shell_bound = sum(sum(comb(l, v) for v in range(l + 1) if a * v >= l)
                          for l in range(j + 1))
        exact_event = sum((prob for m, (_, prob) in small.items() if m <= cutoff), F(0))
        assert sum(m <= cutoff for m in seeds) <= shell_bound
        for h0 in range(n, cap + 1):
            low = sum(weighted[:h0])
            assert low <= (a - 1) ** n * b ** (h0 - 1)
            assert exact_event <= low + F(shell_bound, 1 << h0)
    return dict(depth=n, words=len(seeds), probability=str(original),
                auxiliary_gate=str(tilted), individual_Z_tests=tests,
                largest_terminal=max_terminal)


if __name__ == '__main__':
    print(json.dumps({str(a): [check(a, n) for n in (4, 6, 8, 9)]
                      for a in (F(5, 4), F(3, 2), F(7, 4), F(19, 10))}, indent=2))
