"""Exhaust the four coupled ordinary parity trees at upper odd budget fifteen."""

import argparse
from collections import Counter
from functools import cache
import json
from pathlib import Path


SMALL_FLOOR = 2**18
DEPTH_LIMIT = 256
BUDGET = 15
MARKS = ((3, 0), (1, -1), (1, 1), (2, -1))


def shortcut(x):
    return (3*x + 1)//2 if x % 2 else x//2


def hit(x, max_clock=100000):
    """Return first hit and odd departures; failure to certify raises."""
    if x < 1:
        raise ValueError("first-hit check requires a positive source")
    n, odds = x, 0
    for clock in range(max_clock + 1):
        if n == 1:
            return clock, odds
        odds += n % 2
        n = shortcut(n)
    raise RuntimeError(f"unresolved ordinary first hit at {x}")


def small_floor():
    """Inductively certify every small source by a genuine strict descent."""
    worst = 0
    for x in range(2, SMALL_FLOOR + 1):
        n = x
        for clock in range(1, 10001):
            n = shortcut(n)
            if n < x:
                worst = max(worst, clock)
                break
        else:
            raise RuntimeError(f"missing small descent at {x}")
    return {"through_inclusive": SMALL_FLOOR, "maximum_first_descent_clock": worst}


@cache
def compare(time, odds):
    """Compare the coefficient 3^odds/2^time with 1 and the strip endpoints."""
    num, den = 3**odds, 2**time
    return (num > den) - (num < den), 50*num > 267*den, 50*den > 267*num


def mark_tree(A, B):
    # Each node holds a canonical residue x modulo 2^t, its two actual
    # endpoints and odd counts, the last lower bit, and both ratio extrema.
    initial_upper = A+B
    stack = [(1, 1, 2, shortcut(initial_upper), 1, initial_upper % 2,
              True, 0, 0, 0, 0)]
    powers = [3**i for i in range(DEPTH_LIMIT + 1)]
    counts = Counter()
    hits = {}
    max_depth = 0
    while stack:
        t, x, lower, upper, p, q, previous_odd, lt, lp, ht, hp = stack.pop()
        counts["nodes"] += 1
        max_depth = max(max_depth, t)
        if t >= DEPTH_LIMIT:
            raise RuntimeError("depth limit reached before full exhaustion")

        # The upper endpoint for a nonnegative lift x+2^t*z is exactly
        # upper+A*3^q*z. An upper first hit at this clock must be this lift.
        z, remainder = divmod(1-upper, A*powers[q])
        if z >= 0 and remainder == 0:
            candidate = x + (z << t)
            if candidate not in hits:
                first = hit(A*candidate+B)
                if first[0] > t or first[1] > q:
                    raise RuntimeError("upper endpoint disagrees with its physical first hit")
                hits[candidate] = {"upper_first_hit": first, "lower_first_hit": hit(candidate)}

        # Both lifts have the same actual endpoint for every remaining z.
        if lower == upper and powers[p] == A*powers[q]:
            counts["merged_cylinders"] += 1
            continue

        for bit in (0, 1):
            low = lower + bit*powers[p]
            up = upper + bit*A*powers[q]
            low_bit, up_bit = low % 2, up % 2
            next_q = q + up_bit
            if next_q > BUDGET:
                counts["upper_budget"] += 1
                continue
            if not (previous_odd or low_bit):
                counts["two_even_lower_departures"] += 1
                continue
            low_t, low_p, high_t, high_p = lt, lp, ht, hp
            if low_bit:
                low_cmp = compare(t-lt, p-lp)
                high_cmp = compare(t-ht, p-hp)
                if low_cmp[1] or high_cmp[2]:
                    counts["lower_strip"] += 1
                    continue
                if low_cmp[0] < 0:
                    low_t, low_p = t, p
                if high_cmp[0] > 0:
                    high_t, high_p = t, p
            stack.append((t+1, x+(bit << t), shortcut(low), shortcut(up),
                          p+low_bit, next_q, low_bit, low_t, low_p, high_t, high_p))

    return {"upper_affine": [A, B], "max_depth": max_depth, "counts": dict(counts),
            "number_of_candidate_sources": len(hits), "max_candidate": max(hits),
            "candidates": [{"x": x, **hits[x]} for x in sorted(hits)]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path, help="Compare with a saved JSON receipt")
    args = parser.parse_args()
    # The geometric bound (1+1/(3s))^t <= 3s/(3s-t) and the physical
    # ceiling give largest/smallest slope <= (16s+7)/(3s-t).
    if 50*(16*SMALL_FLOOR+7) > 267*(3*SMALL_FLOOR-DEPTH_LIMIT):
        raise RuntimeError("small floor does not cover the requested strip depth")
    receipt = {"upper_odd_budget": BUDGET, "depth_failure_limit": DEPTH_LIMIT,
               "strip_ratio": [267, 50], "small_floor": small_floor(),
               "profiles": [mark_tree(*mark) for mark in MARKS]}
    data = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.verify:
        if data != args.verify.read_text(encoding="utf-8"):
            raise RuntimeError("replay differs from the stored receipt")
        print("All four parity trees, ordinary first hits and the small floor agree.")
    else:
        print(data, end="")


if __name__ == "__main__":
    main()
