#!/usr/bin/env python3
"""Exact, total Collatz rank regularization; no convergence oracle is used.

Gamma is the actual-prefix rank from GettysburgResearch/collatz PR106,
7b7471ea0e7b359a2ac46fb1e6aff269331509c3.  Phi is the new least integer
majorant with one-step growth at most three.  Standard library only.
"""
from __future__ import annotations

from functools import lru_cache


def shortcut(n: int) -> int:
    if n < 1:
        raise ValueError("positive ordinary integer required")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def absorbed(n: int) -> int:
    return 1 if n == 1 else shortcut(n)


def v3(n: int) -> int:
    if n == 0:
        raise ValueError("valuation of zero is not a finite rank input")
    n = abs(n)
    e = 0
    while n % 3 == 0:
        n //= 3
        e += 1
    return e


def displacement_rank(d: int) -> int:
    d = abs(d)
    if d == 0:
        raise ValueError("zero displacements must be omitted")
    return d * d // (3 ** v3(d))


@lru_cache(maxsize=None)
def gamma(n: int) -> int:
    if n < 1:
        raise ValueError("positive ordinary integer required")
    if n == 1:
        return 0
    best = displacement_rank(n)
    m = n
    four_power = 1
    # Every unexamined candidate is at least 4**k; the baseline is <= n**2.
    for _k in range(1, n.bit_length()):
        four_power *= 4
        if four_power > best:
            break
        m = shortcut(m)
        d = m - n
        if d:
            best = min(best, four_power * displacement_rank(d))
    return best


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


@lru_cache(maxsize=None)
def envelope(n: int) -> tuple[int, int, int]:
    """Return (Phi(n), first maximizing j, last evaluated j).

    The tail inequality is integer-exact.  Once it holds at j, every future
    rounded candidate is bounded by the current best value.
    """
    if n < 1:
        raise ValueError("positive ordinary integer required")
    if n == 1:
        return (0, 0, 0)
    m, j, three_power, four_power = n, 0, 1, 1
    best, witness = gamma(n), 0
    height = (n + 1) ** 2
    while True:
        candidate = ceil_div(gamma(m), three_power)
        if candidate > best:
            best, witness = candidate, j
        if m == 1 or three_power * height <= four_power * best:
            return best, witness, j
        m = absorbed(m)
        j += 1
        three_power *= 3
        four_power *= 4


def phi(n: int) -> int:
    return envelope(n)[0]


def is_contact(n: int) -> bool:
    return n >= 2 and phi(n) == gamma(n)


def contact_return(n: int) -> tuple[int, int]:
    """First positive-time return to the contact set, killed at 1.

    Return (endpoint, shortcut clock); endpoint 1 means killed.  The stopping
    limit is the proved contact bound, not a user-selected search cutoff.
    """
    if not is_contact(n):
        raise ValueError("a contact source is required")
    x = absorbed(n)
    if x == 1 or is_contact(x):
        return x, 1
    limit, three, four = 0, 1, 1
    while four * (phi(x) - 1) <= three * (x + 1) ** 2:
        limit, three, four = limit + 1, three * 3, four * 4
    for j in range(limit + 1):
        if x == 1 or is_contact(x):
            return x, j + 1
        x = absorbed(x)
    raise RuntimeError("proved contact-hitting bound violated")


def inverse_contact_fan(y: int) -> dict:
    """All contact sources first-returning to y, with exact clocks.

    Completeness: a return of clock r has 3**(r-1) < Phi(y), since each
    noncontact predecessor divides the envelope rank by three, rounded up.
    """
    if not is_contact(y):
        raise ValueError("a contact endpoint is required")
    depth_bound, three = 0, 1
    while three < phi(y):
        depth_bound, three = depth_bound + 1, three * 3
    stack = [(y, 0)]
    sources: dict[int, int] = {}
    interior_nodes = 0
    widths: dict[int, int] = {}
    while stack:
        current, depth = stack.pop()
        predecessors = [2 * current]
        if current % 3 == 2:
            odd = (2 * current - 1) // 3
            if odd >= 2:
                predecessors.append(odd)
        for n in predecessors:
            next_depth = depth + 1
            widths[next_depth] = widths.get(next_depth, 0) + 1
            if n > 2 * ceil_div(phi(y), 3 ** (next_depth - 1)):
                raise RuntimeError("proved inverse-source height bound violated")
            if is_contact(n):
                if n in sources and sources[n] != next_depth:
                    raise RuntimeError("one source has two distinct first-return clocks")
                sources[n] = next_depth
                continue
            if not (phi(n) == ceil_div(phi(current), 3) < phi(current)):
                raise RuntimeError("noncontact inverse rank identity violated")
            if next_depth >= depth_bound:
                raise RuntimeError("proved inverse-depth bound violated")
            interior_nodes += 1
            stack.append((n, next_depth))
    fibonacci = [0, 1]
    while len(fibonacci) <= depth_bound + 2:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    node_bound = 0
    for d in range(1, depth_bound + 1):
        width_bound = min(fibonacci[d + 2], 2 * ceil_div(phi(y), 3 ** (d - 1)))
        if widths.get(d, 0) > width_bound:
            raise RuntimeError("proved inverse width bound violated")
        node_bound += width_bound
    return {"endpoint": y, "phi": phi(y), "depth_bound": depth_bound,
            "interior_nodes": interior_nodes,
            "tested_nodes": sum(widths.values()), "node_bound": node_bound,
            "depth_widths": widths,
            "sources": [{"n": n, "clock": r} for n, r in sorted(sources.items())]}


def critical_real_envelope(n: int) -> tuple[int, int, int]:
    """Exact rational max_j (4/9)**j Gamma(S**j n).

    Returns reduced numerator, denominator, and evaluated horizon.  Unlike
    envelope(), the totality proof does not promise logarithmic bit complexity.
    At each even step the normalized height bound improves by 16/81.
    """
    from fractions import Fraction

    if n < 1:
        raise ValueError("positive ordinary integer required")
    if n == 1:
        return (0, 1, 0)
    m, j, evens = n, 0, 0
    factor = Fraction(1)
    best = Fraction(gamma(n))
    even_height_factor = Fraction(1)
    while True:
        best = max(best, factor * gamma(m))
        if m == 1 or even_height_factor * (n + 1) ** 2 <= best:
            return best.numerator, best.denominator, j
        if m % 2 == 0:
            evens += 1
            even_height_factor *= Fraction(16, 81)
        m = absorbed(m)
        factor *= Fraction(4, 9)
        j += 1


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int, nargs="+", help="positive sources")
    args = parser.parse_args()
    print(json.dumps([
        {"n": n, "gamma": gamma(n), "phi": phi(n),
         "maximizing_time": envelope(n)[1], "evaluated_horizon": envelope(n)[2],
         "next_n": absorbed(n), "next_phi": phi(absorbed(n))}
        for n in args.n
    ], indent=2))
