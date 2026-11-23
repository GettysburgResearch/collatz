#!/usr/bin/env python3
"""Exact shared-tail and boundary controls for HARDY_INVERSE_TREE.md.

Finite truncations are not eigenvectors: their explicit leaf defects tend to
zero in coefficient l2. The infinite theorem is the written geometric-series
argument, not a claim inferred from these finite checks.
"""

from collections import defaultdict
from fractions import Fraction
from math import gcd
import json


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def exponents(n):
    assert n > 0 and gcd(n, 6) == 1
    es = [e for e in range(3, 9) if (2 ** e * n) % 9 in (4, 7)]
    assert len(es) == 2
    return es


def child(n, e):
    r = (2 ** e * n - 1) // 3
    assert r > n and gcd(r, 6) == 1
    assert 3 * r + 1 == 2 ** e * n
    x = r
    for _ in range(e):
        x = shortcut(x)
    assert x == n
    return r


def clean(d):
    return {n: c for n, c in d.items() if c}


def defect(f, lam):
    out = defaultdict(Fraction)
    for n, c in f.items():
        out[shortcut(n)] += c
        out[n] -= lam * c
    return clean(out)


def norm_sq(f):
    return sum((c * c for c in f.values()), Fraction(0))


def incoming(root, lam, depth):
    """Odd leaves through depth; even blocks for parents below depth."""
    out = {}
    level = {root: Fraction(1)}
    seen_odds = {root}
    for _ in range(depth):
        nxt = {}
        for n, c in level.items():
            es = exponents(n)
            for j in range(1, 8):
                value = c * lam ** j * sum(e > j for e in es) / 2
                if value:
                    even = 2 ** j * n
                    assert even not in out
                    out[even] = value
            for e in es:
                r = child(n, e)
                assert r not in seen_odds
                seen_odds.add(r)
                value = c * lam ** e / 2
                nxt[r] = value
                assert r not in out
                out[r] = value
        level = nxt
    expected = {root: lam}
    expected.update({n: -lam * c for n, c in level.items()})
    assert defect(out, lam) == clean(expected)
    assert root not in out

    rho = abs(lam)
    B = 1 + sum(rho ** (2 * j) for j in range(1, 8))
    q = max(Fraction(1), rho ** 16) / 2
    assert q < 1
    assert norm_sq(out) <= B / (1 - q)
    assert norm_sq({n: lam * c for n, c in level.items()}) <= rho ** 2 * q ** depth
    return out, level


def channel(root, e, lam, depth):
    r = child(root, e)
    incoming_flow, leaves = incoming(r, lam, depth)
    out = {2 ** j * root: lam ** j for j in range(1, e)}
    assert r not in out
    out[r] = lam ** e
    for n, c in incoming_flow.items():
        assert n not in out
        out[n] = lam ** e * c
    expected = {root: lam}
    expected.update({n: -lam ** (e + 1) * c for n, c in leaves.items()})
    assert defect(out, lam) == clean(expected)
    return out


def difference(root, lam, depth):
    e, f = exponents(root)
    first = channel(root, e, lam, depth)
    second = channel(root, f, lam, depth)
    out = defaultdict(Fraction, first)
    for n, c in second.items():
        out[n] -= c
    out = clean(out)
    delta = defect(out, lam)
    assert root not in delta  # The common root boundary cancels exactly.
    assert out[child(root, e)] == lam ** e
    if lam == 1:
        assert norm_sq(delta) == Fraction(2, 2 ** depth)
    return out, delta


def antichain_root(k):
    n = 1
    for _ in range(k):
        n = child(n, exponents(n)[0])
    return child(n, exponents(n)[1])


def main():
    cases = []
    for root in [1, 5]:
        for lam in [Fraction(1), Fraction(-1), Fraction(33, 32)]:
            for depth in [1, 3, 7]:
                flow, delta = difference(root, lam, depth)
                cases.append({
                    "root": root, "lambda": str(lam), "depth": depth,
                    "nonzero_coefficients": len(flow),
                    "boundary_coefficients": len(delta),
                    "boundary_l2_squared_approx": float(norm_sq(delta)),
                    "exact_assertions_passed": True,
                })
    roots = [antichain_root(k) for k in range(4)]
    supports = [set(difference(n, Fraction(1), 5)[0]) for n in roots]
    assert all(not (supports[i] & supports[j])
               for i in range(len(supports)) for j in range(i))
    print(json.dumps({
        "status": "finite_exact_flow_controls_passed",
        "infinite_theorem_scope": "written_proof_not_finite_inference",
        "cases": cases,
        "antichain_roots": roots,
        "antichain_truncation_supports_disjoint": True,
    }, indent=2))


if __name__ == "__main__":
    main()
