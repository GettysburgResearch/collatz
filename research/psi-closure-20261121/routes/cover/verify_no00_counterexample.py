#!/usr/bin/env python3
"""
Independent replay of the counterexample to "Conjecture N" found by no00_exhaustive.py.

Claim (exact certificate): let u = 11101101101101010101101101101 (29 steps; 3^o > 2^k on every
prefix; never two consecutive even steps).  Every point (x0, 0) of Z_2 x Z_3 whose 2-adic
coordinate has a parity word beginning with u has a DESCENDING ordinary path.  So a non-stopping
word without the factor 00 does not guarantee an obstruction point at y0 = 0.

The script
  1. finds the shortest backward word hanging off T^29(n) on an actual integer n,
  2. replays the whole path with exact rational shadows from the rational point (x0, 0),
     x0 = the 2-adic rational with parity word u 1^infinity, checking every legality condition,
  3. replays it on several actual integers and checks w = alpha*n + beta < n.
usage: python3 -X utf8 -B verify_no00_counterexample.py [word]
"""
import sys
from fractions import Fraction as Fr

from shadow_bfs import par2, res3
from deep_slice_search import make_n
from slice_experiments import residue_fast


def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def find_path(n, u, prev, Dmax):
    """shortest backward word (letters D, S) from u to an integer below n, edge to prev excluded"""
    for D in range(1, Dmax + 1):
        stack = []
        if 2 * u != prev:
            stack.append((2 * u, 'D'))
        if u % 3 == 2 and (2 * u - 1) // 3 != prev:
            stack.append(((2 * u - 1) // 3, 'S'))
        while stack:
            w, path = stack.pop()
            if w < n:
                return path
            if len(path) == D:
                continue
            # exact pruning: every remaining step multiplies by at least 2/3
            if w * 2 ** (D - len(path)) >= n * 3 ** (D - len(path)) + 3 ** (D - len(path)):
                continue
            stack.append((2 * w, path + 'D'))
            if w % 3 == 2:
                stack.append(((2 * w - 1) // 3, path + 'S'))
    return None


def main():
    word = sys.argv[1] if len(sys.argv) > 1 else '11101101101101010101101101101'
    bits = [int(c) for c in word]
    K = len(bits)
    # admissibility and the no-00 property
    num, den = 1, 1
    for i, b in enumerate(bits):
        num, den = num * (3 if b else 1), den * 2
        assert num > den, "word is not non-stopping"
        assert not (b == 0 and i > 0 and bits[i - 1] == 0), "word contains 00"
    J = 140
    n = make_n(residue_fast(bits), K, 0, J)
    u, prev = n, None
    for b in bits:
        assert u % 2 == b
        prev, u = u, T(u)
    path = find_path(n, u, prev, 34)
    assert path is not None, "no descent found"
    print(f"word u ({K} steps, {sum(bits)} odd): {word}")
    print(f"backward word ({len(path)} steps, {path.count('S')} odd): {path}")

    # exact shadow replay from the rational point with parity word u 1^infinity
    x0 = Fr(-1)
    for b in reversed(bits):
        x0 = 2 * x0 if b == 0 else (2 * x0 - 1) / 3
    X, Y, alpha = x0, Fr(0), Fr(1)
    for b in bits:
        assert par2(X) == b
        if b:
            X, Y, alpha = (3 * X + 1) / 2, (3 * Y + 1) / 2, alpha * Fr(3, 2)
        else:
            X, Y, alpha = X / 2, Y / 2, alpha / 2
    assert X == -1
    fwd_alpha = alpha
    for ch in path:
        if ch == 'D':
            X, Y, alpha = 2 * X, 2 * Y, alpha * 2
        else:
            assert res3(Y) == 2
            X, Y, alpha = (2 * X - 1) / 3, (2 * Y - 1) / 3, alpha * Fr(2, 3)
    beta = Y
    print(f"rational point: x0 = {x0}  (parity word u 1^inf), y0 = 0")
    print(f"multiplier after the forward part: {fwd_alpha} = {float(fwd_alpha):.4f}")
    print(f"alpha = {alpha} = {float(alpha):.6f},  beta = 3-adic shadow = {beta}")
    assert alpha < 1
    assert Y == alpha * 0 + beta and X == alpha * x0 + beta

    # replay on actual integers
    M = 2 ** K * 3 ** J
    for t in (0, 1, 2, 12345):
        nn = n + t * M
        w = nn
        for b in bits:
            assert w % 2 == b
            w = T(w)
        for ch in path:
            if ch == 'D':
                w = 2 * w
            else:
                assert w % 3 == 2
                w = (2 * w - 1) // 3
        assert Fr(w) == alpha * nn + beta and 0 < w < nn
    print("replayed on 4 integers n = x0 (mod 2^29), n = 0 (mod 3^140): every move legal, "
          "w = alpha*n + beta < n")
    # least 3-adic precision for which the path is legal on the whole class
    need = None
    for Jtry in range(0, 60):
        ok = True
        for t in range(0, 60):
            nn = make_n(residue_fast(bits), K, 0, Jtry) + t * 2 ** K * 3 ** Jtry
            w = nn
            for b in bits:
                w = T(w)
            for ch in path:
                if ch == 'D':
                    w = 2 * w
                elif w % 3 == 2:
                    w = (2 * w - 1) // 3
                else:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            need = Jtry
            break
    print(f"least J such that the path is legal on 60 consecutive members of the class "
          f"n = r (mod 2^{K}), n = 0 (mod 3^J): J = {need}"
          + ("  (no 3-adic condition: a purely 2-adic certificate)" if need == 0 else ""))
    print(f"odd steps: forward {sum(bits)}, backward {path.count('S')} "
          f"(backward <= forward means validity cannot depend on the 3-adic coordinate)")
    print("RESULT: PASS  (Conjecture N refuted)")


if __name__ == '__main__':
    main()
