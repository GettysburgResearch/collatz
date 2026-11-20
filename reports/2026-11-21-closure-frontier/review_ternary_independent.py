#!/usr/bin/env python3
"""Independent rational linear-system check of the ternary stationary note.

Does not import the author's recursion/checker. This is a finite algebra audit.
"""
from fractions import Fraction as F
from math import comb
import hashlib
import json
from pathlib import Path


def need(test, message):
    if not test:
        raise ValueError(message)


def stationary_by_linear_system(s):
    q = 3 ** s
    inv2 = pow(2, -1, q)
    units = [a for a in range(q) if a % 3]
    index = {a: i for i, a in enumerate(units)}
    size = len(units)
    matrix = [[F(0) for _ in range(size + 1)] for _ in range(size)]
    for row in range(size):
        matrix[row][row] = F(-1)
    for a in units:
        for b in (a * inv2 % q, (3 * a + 1) * inv2 % q):
            matrix[index[b]][index[a]] += F(1, 2)
    matrix[-1] = [F(1)] * size + [F(1)]
    for col in range(size):
        pivot = next((row for row in range(col, size) if matrix[row][col]), None)
        need(pivot is not None, "singular stationary system")
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        scale = matrix[col][col]
        matrix[col] = [v / scale for v in matrix[col]]
        for row in range(size):
            if row == col or not matrix[row][col]:
                continue
            scale = matrix[row][col]
            matrix[row] = [a - scale * b for a, b in zip(matrix[row], matrix[col])]
    pi = [F(0)] * q
    for i, a in enumerate(units):
        pi[a] = matrix[i][-1]
    need(sum(pi) == 1 and all(pi[a] > 0 for a in units), "stationary support or mass")
    for b in range(q):
        incoming = sum(pi[a] * F(1, 2)
                       for a in range(q)
                       for target in (a * inv2 % q, (3 * a + 1) * inv2 % q)
                       if target == b)
        need(pi[b] == incoming, "stationarity equation")
    return pi


def main():
    previous = [F(1)]
    previous_r = F(1)
    rows = []
    cut_count = 0
    for s in range(1, 5):
        q = 3 ** s
        pi = stationary_by_linear_system(s)
        inv2 = pow(2, -1, q)
        for a in range(q // 3):
            need(sum(pi[a + j * (q // 3)] for j in range(3)) == previous[a],
                 "projective consistency")
        r = q * sum(p * p for p in pi)
        cross = sum(F(q, 3) * pi[(2 * x) % q] * previous[((2 * x - 1) // 3) % (q // 3)]
                    for x in range(q) if x % 3 == 2)
        need(r - previous_r == 2 * cross and cross > 0, "critical square identity")
        need(pi[-1] >= F(1, 2 ** s), "all-one atom lower bound")
        need(max(pi) <= F(2, 3) ** s, "atom upper bound")
        tail = F(sum(comb(4 * s, j) for j in range(s)), 2 ** (4 * s))
        need(tail <= F(1, 3) * F(16, 27) ** s, "coupling binomial estimate")
        # Exhaust every cut at the two smallest full moduli. Zero-mass
        # multiples are included, so no division by a stationary zero occurs.
        if q <= 9:
            for mask in range(1 << q):
                mass = sum(pi[x] for x in range(q) if (mask >> x) & 1)
                flow = sum(pi[x] * F(1, 2)
                           for x in range(q) if (mask >> x) & 1
                           for y in (x * inv2 % q, (3 * x + 1) * inv2 % q)
                           if not ((mask >> y) & 1))
                need(flow >= F(49, 648 * s) * min(mass, 1 - mass), "conductance bound")
                cut_count += 1
        if s == 2:
            need(pi == list(map(F, [0, F(8, 63), F(16, 63), 0, F(11, 63), F(4, 63), 0, F(2, 63), F(22, 63)])),
                 "published modulo-nine normalization")
        rows.append({"s": s, "q": q, "R": str(r), "I": str(cross), "binomial_tail": str(tail)})
        previous, previous_r = pi, r
    report = {"status": "PASS", "method": "independent rational Gaussian elimination",
              "levels": rows, "all_cuts_checked": cut_count,
              "scope": "Finite algebra only; no finite check proves the infinite L2 or imported L1 theorems."}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
