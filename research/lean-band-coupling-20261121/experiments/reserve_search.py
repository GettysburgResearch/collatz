#!/usr/bin/env python3
"""Exact, bounded discovery of ordinary merger witnesses.

This is an experiment, not a coverage theorem. A successful witness is replayed
on both ordinary forward orbits. An exhausted inverse tree is exhaustive only
for its stated (r,h,s,v) decomposition and odd-step allowance. The outer search
tries a finite menu of decompositions; failure does not refute convergence.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def step(n: int) -> int:
    return (3 * n + 1) // 2 if n % 2 else n // 2


def advance(n: int, t: int) -> tuple[int, int]:
    odds = 0
    for _ in range(t):
        odds += n % 2
        n = step(n)
    return n, odds


def reverse_search(n: int, r: int, h: int, s: int, v: int,
                   cap: int = 100_000, partner_bound: int | None = None) -> dict:
    """Find x<partner_bound with T^t(x)=T^h(n), using the splice theorem.

    By default partner_bound=n. If n is a later marked endpoint of an earlier
    source n0, pass partner_bound=n0 and separately retain the actual n0->n
    visit certificate. A bound x<n alone does not close induction at n0.

    With y=T^h(r), p=oddCount(h,r), P=p+s, an ancestor T^t(u)=y
    with a<=P yields x=2^t*3^(P-a)*v+u. Since v>=1, a successful
    node has 2^t<partner_bound. This gives a finite depth bound.

    If R=P-a odd inverse steps remain, even the smallest conceivable
    continuation is >= (2/3)^R*(x+1)-1. This follows by allowing every
    remaining step to be (2*x-1)/3, even when that branch is illegal.
    Thus (x+1)*2^R >= (partner_bound+1)*3^R is a sound prune.
    """
    assert n == (1 << h) * 3**s * v + r and v > 0 and r >= 0
    bound = n if partner_bound is None else partner_bound
    assert 1 < bound
    y, p = advance(r, h)
    P = p + s
    depth = (bound - 1).bit_length() - 1
    powers3 = [3**j for j in range(P + 1)]
    stack = [(y, 0, 0)]
    seen = set()
    visited = 0
    while stack:
        u, t, a = stack.pop()
        if (u, t, a) in seen:
            continue
        seen.add((u, t, a))
        visited += 1
        if visited > cap:
            return {"status": "node_cap", "visited": visited, "cap": cap,
                    "n": n, "r": r, "h": h, "s": s, "v": v,
                    "partner_bound": bound}
        x = (1 << t) * powers3[P - a] * v + u
        if 0 < x < bound:
            uy, ua = advance(u, t)
            q, _ = advance(n, h)
            xq, _ = advance(x, t)
            assert (uy, ua) == (y, a)
            assert xq == q == powers3[P] * v + y
            assert (1 << t) * powers3[P] * v + 3**a * u < 3**a * bound
            return {
                "status": "witness", "n": n, "r": r, "h": h, "s": s,
                "v": v, "p": p, "y": y, "u": u, "t": t, "a": a,
                "x": x, "partner_bound": bound,
                "common_endpoint": q, "visited": visited,
                "independent_forward_replay": True,
            }
        R = P - a
        if t >= depth or (x + 1) * (1 << R) >= (bound + 1) * powers3[R]:
            continue
        stack.append((2 * u, t + 1, a))
        if a < P and u % 3 == 2:
            stack.append(((2 * u - 1) // 3, t + 1, a + 1))
    return {"status": "exhausted_fixed_decomposition", "visited": visited,
            "n": n, "r": r, "h": h, "s": s, "v": v, "p": p,
            "partner_bound": bound,
            "max_ordinary_clock": depth, "max_odd_count": P}


def find_reserved(n: int, cap: int, partner_bound: int | None = None) -> dict:
    d = n.bit_length() - 1
    trials = 0
    caps = 0
    for h in range(d, -1, -1):
        quotient = n >> h
        power = 1
        s = 0
        while power <= quotient:
            v = quotient // power
            r = n - (1 << h) * power * v
            result = reverse_search(n, r, h, s, v, cap, partner_bound)
            trials += 1
            caps += result["status"] == "node_cap"
            if result["status"] == "witness":
                return {"trials": trials, "capped_trials": caps, **result}
            power *= 3
            s += 1
    return {"status": "finite_menu_unresolved", "n": n, "trials": trials,
            "partner_bound": n if partner_bound is None else partner_bound,
            "capped_trials": caps, "cap_per_decomposition": cap}


def run(cap: int) -> dict:
    cases = []
    for d in [6, 8, 10, 12, 16, 20, 24, 28, 32, 40, 48, 56, 64, 128, 256]:
        n = (1 << d) + 27
        native = reverse_search(n, 27, d, 0, 1, cap)
        reserved = find_reserved(n, cap)
        marked = n % 2 == 1 and (d + 1) * (n - (1 << d)) <= 70 * (1 << d)
        cases.append({"label": f"2^{d}+27", "marked": marked,
                      "section_automatic_on_entire_octave": d <= 69,
                      "native": native,
                      "reserved_menu": reserved})
    return {
        "status": "EXACT_FINITE_EXPERIMENT",
        "map": "T(n)=n/2 if even, (3*n+1)/2 if odd",
        "scope": "No universal coverage or universal convergence assertion.",
        "cases": cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cap", type=int, default=100_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.cap < 1:
        parser.error("--cap must be positive")
    result = run(args.cap)
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
