"""Bounded exact checks of literal cuts, offset composition and clock windows."""

from fractions import Fraction
from functools import cache
from math import isqrt
import json


def require(predicate, message):
    if not predicate:
        raise ValueError(message)


def unit(x):
    return x > 0 and x % 2 == 1 and x % 3 != 0


def walk(x, n):
    total = 0
    for _ in range(n):
        y = 3 * x + 1
        gap = (y & -y).bit_length() - 1
        total += gap
        x = y >> gap
    return x, total


@cache
def sources(q, n, total):
    if n == 0:
        return frozenset({q}) if total == 0 else frozenset()
    result = set()
    for gap in range(1, total - n + 2):
        num = (q << gap) - 1
        if num % 3 or not unit(num // 3):
            continue
        parents = sources(num // 3, n - 1, total - gap)
        require(result.isdisjoint(parents), ("final gap collision", q, n, total))
        result.update(parents)
    return frozenset(result)


def offset(x, q, n, t):
    return Fraction(q) - Fraction(3**n * x, 2**t)


def check_banks():
    checked = glue = carries = 0
    for q in (1, 5, 7, 11, 17, 31):
        for n in range(2, 7):
            for t in range(n, 2 * n + 5):
                row = sources(q, n, t)
                # Direct forward comparison over the complete bound from beta >= 0.
                maximum = (q << t) // 3**n
                direct = {x for x in range(1, maximum + 1, 2)
                          if unit(x) and walk(x, n) == (q, t)}
                require(row == direct, ("forward inverse mismatch", q, n, t))
                checked += 1
                for cut in range(1, n):
                    result = set()
                    for s in range(cut, t - (n - cut) + 1):
                        for g in sources(q, n - cut, t - s):
                            bank = sources(g, cut, s)
                            require(result.isdisjoint(bank), ("cut collision", q, cut, s))
                            result.update(bank)
                            for x in bank:
                                beta = offset(x, g, cut, s)
                                tail = offset(g, q, n - cut, t - s)
                                combined = tail + Fraction(3**(n-cut), 2**(t-s)) * beta
                                require(combined == offset(x, q, n, t), ("offset", x, g, q))
                                carries += 1
                    require(result == row, ("missing cut sources", q, n, t, cut))
                    glue += 1
    return {"direct_forward_rows": checked, "literal_cut_unions": glue,
            "exact_offset_compositions": carries}


def check_schedules():
    tested = 0
    for n in (1024, 4096, 65537, 1000000, 100000003):
        for d in (0, 1, -1, isqrt(n)//2, -isqrt(n)//2, n//2048, -n//2048):
            m = max(1, (256*d*d + n-1)//n)
            h, large = divmod(n, m)
            if h < 1024:
                continue
            jump = isqrt(h)//16
            for j in range(1, m+1):
                length = h + (j <= large)
                drift = (j*d)//m - ((j-1)*d)//m
                for left in ({0} if j == 1 else {0, jump}):
                    for right in ({0} if j == m else {0, jump}):
                        excess = drift + right-left
                        require(4*excess**2 <= length, ("central slice", n, d, j))
                        require(4*(2*length+excess) >= 7*length, ("slope", n, d, j))
                        tested += 1
    return tested


if __name__ == "__main__":
    counts = check_banks()
    counts["schedule_corner_checks"] = check_schedules()
    print(json.dumps(counts, indent=2))
