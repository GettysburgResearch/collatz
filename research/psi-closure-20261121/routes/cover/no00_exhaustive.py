#!/usr/bin/env python3
"""
Exhaustive bounded test of Conjecture N (NOTES.md):

    if the parity word u of x0 is non-stopping (3^o > 2^k on every prefix) and never has two
    consecutive even steps, then (x0, 0) is an obstruction point.

Evidence tier: EMPIRICAL / exhaustive within bounds.  For EVERY admissible word u of length
k <= L with no factor 00 the side tree hanging off the orbit point T^k(n) is searched to depth
D (pruned only when a descent within depth D is impossible), where n is an actual integer with
parity word u and n = 0 (mod 3^J).  Whether the side tree contains an integer below n depends
only on u, so the result is a statement about all 2-adic x0 with such a prefix:

    no descending path with p <= L forward steps and q <= D backward steps.

usage: python3 -X utf8 -B no00_exhaustive.py [L] [D] [seconds]
"""
import math
import sys
import time

LN2, LN3 = math.log(2), math.log(3)
GAIN = LN3 - LN2


def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def side_tree(n, u, prev, lamA, D):
    """search the backward tree hanging off u (edge to prev excluded) for an integer < n"""
    nodes = 0
    stack = []
    c = 2 * u
    if c != prev and lamA + LN2 - (D - 1) * GAIN < 0:
        stack.append((c, 1, lamA + LN2))
    if u % 3 == 2:
        c = (2 * u - 1) // 3
        if c != prev:
            stack.append((c, 1, lamA - GAIN))
    while stack:
        w, q, lam = stack.pop()
        nodes += 1
        if w < n:
            return q, nodes
        if q == D:
            continue
        rem = D - q - 1
        if lam + LN2 - rem * GAIN < 0:
            stack.append((2 * w, q + 1, lam + LN2))
        if w % 3 == 2 and lam - GAIN - rem * GAIN < 0:
            stack.append(((2 * w - 1) // 3, q + 1, lam - GAIN))
    return None, nodes


def main():
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 26
    D = int(sys.argv[2]) if len(sys.argv) > 2 else 34
    budget = float(sys.argv[3]) if len(sys.argv) > 3 else 200.0
    J = D + 60
    M3 = 3 ** J
    t0 = time.time()
    # state: (x, m, pow3, num, den, last, bits) with m = T^k(x), pow3 = 3^(odd steps)
    frontier = [(0, 0, 1, 1, 1, 1, '')]
    total_words = total_nodes = 0
    descents = []
    done = 0
    for k in range(0, L):
        nxt = []
        for (x, m, pow3, num, den, last, bits) in frontier:
            for b in (1, 0):
                if b == 0 and (last == 0 or not num > 2 * den):
                    continue                     # no 00, and the ratio must stay > 1
                if m % 2 != b:
                    x2, mk = x + (1 << k), m + pow3
                else:
                    x2, mk = x, m
                if b:
                    m2, p3 = (3 * mk + 1) // 2, pow3 * 3
                    num2 = num * 3
                else:
                    m2, p3 = mk // 2, pow3
                    num2 = num
                den2 = den * 2
                word = bits + str(b)
                # actual integer n = x2 (mod 2^(k+1)), n = 0 (mod 3^J)
                s = (-x2 * pow(1 << (k + 1), -1, M3)) % M3 + M3
                n = x2 + (s << (k + 1))
                u = m2 + p3 * s
                prev = mk + pow3 * 2 * s
                assert n % M3 == 0 and T(prev) == u
                lamA = math.log(num2) - math.log(den2)
                q, nodes = side_tree(n, u, prev, lamA, D)
                total_words += 1
                total_nodes += nodes
                if q is not None:
                    descents.append((word, q))
                nxt.append((x2, m2, p3, num2, den2, b, word))
        frontier = nxt
        done = k + 1
        if time.time() - t0 > budget:
            break
    print(f"admissible words without 00, all lengths <= {done}: {total_words} words "
          f"({len(frontier)} of length {done}), side trees to depth {D}: {total_nodes} nodes, "
          f"{time.time() - t0:.1f}s")
    if descents:
        print(f"DESCENTS FOUND ({len(descents)}); first: {descents[:5]}  "
              f"=> Conjecture N is FALSE")
    else:
        print(f"no descending path with p <= {done} forward and q <= {D} backward steps "
              f"for any such word  (EMPIRICAL support for Conjecture N)")


if __name__ == '__main__':
    main()
