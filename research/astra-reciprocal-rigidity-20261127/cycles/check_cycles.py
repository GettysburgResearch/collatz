"""Exact finite witnesses. Uses only the Python standard library."""
from collections import Counter
from csv import DictReader
from fractions import Fraction
from math import gcd, prod
from pathlib import Path


def require(condition, label):
    if not condition:
        raise ValueError(label)


def odd_step(x):
    z = 3 * x + 1
    return z // (z & -z)


def factors(n):
    p = 2
    while p * p <= n:
        while n % p == 0:
            yield p
            n //= p
        p += 1
    if n > 1:
        yield n


def counters():
    with Path(__file__).with_name("three_shifts.tsv").open() as stream:
        records = [(int(r["start"]), int(r["end"]), int(r["multiplicity"]))
                   for r in DictReader(stream, delimiter="\t")]
    require(len(set(x for x, y, w in records)) == len(records), "duplicate edge")
    delta = [Counter() for _ in range(4)]
    flow = Counter()
    for x, y, w in records:
        require(x % 2 == 1 and y % 2 == 1 and min(x, y) >= 5 and w > 0, "domain")
        require(odd_step(x) == y, "ordinary edge")
        flow[x] += w
        flow[y] -= w
        for h, diff in enumerate(delta):
            for z, sign in [(x, 1), (y, -1)]:
                for p in factors(z + h):
                    diff[p] += sign * w
    require(all(not any(c.values()) for c in delta[:3]), "shifted prime balance")
    require(any(delta[3].values()) and any(flow.values()), "failed distinction")
    print("three-shift support", len(records), "weight", sum(w for x, y, w in records))
    print("three-shift distinct open endpoints", sum(v != 0 for v in flow.values()))
    print("shift 3 first separating prime and signed valuation",
          next((p, v) for p, v in sorted(delta[3].items()) if v))


def small_paths():
    paths = [[7, 11], [65, 49, 37, 7, 11, 17, 13],
             [55, 83, 125, 47, 71, 107, 161, 121, 91, 137, 103, 155, 233, 175]]
    for path in paths:
        require(all(odd_step(x) == y for x, y in zip(path, path[1:])), "small path")
    for t in range(4):
        a = prod(path[0] + t for path in paths)
        b = prod(path[-1] + t for path in paths)
        require(a - b == -72*t*(t-1), "cubic difference")
    print("two-shift paths", len(paths), "ordinary steps", sum(len(p)-1 for p in paths))


def two_runs():
    # Test positive rational cycles and every rotation, including the trivial endpoint.
    checked = 0
    for s in range(1, 18):
        for z in range(1, 18):
            D = 2**(s+z) - 3**s
            if D <= 0:
                continue
            C = 3**s - 2**s
            g = gcd(C, D)
            require(g == gcd(C, 2**z-1), "two-run full gcd")
            x = Fraction(C, D)
            t = x
            require(x.denominator*(x+1) >= 2**s, "integer-grid bound")
            for bit in [1]*s + [0]*z:
                require(t.numerator % 2 == bit and t.denominator == x.denominator,
                        "rotated parity and reduced denominator")
                require((D*t).denominator == 1 and gcd(int(D*t), D) == g,
                        "rotated whole gcd")
                t = (3*t+1)/2 if bit else t/2
                require(t >= x, "minimum")
            require(t == x, "exact return")
            checked += 1
    print("positive two-run parameter pairs with all rotations", checked)


def finite_exits():
    require(3**17 < 2**27 and Fraction(440,1377) < Fraction(8,25), "count exponent")
    require(Fraction(8,25)*(1+Fraction(41,20)) == Fraction(122,125), "power saving")
    largest = 0
    for X in range(2, 20001):
        x, u, n = X, 0, 0
        seen = set()
        while True:
            require(x not in seen, "bounded repeat in control")
            seen.add(x)
            b = x % 2
            x = (3*x+1)//2 if b else x//2
            n += 1
            u += b
            p, q = 3**u, 2**n
            physical = -1 if x<X else 1 if 2*x>9*X else 0
            homogeneous = -1 if p<q else 1 if 2*p>9*q else 0
            require(physical == homogeneous, "first-exit control")
            if physical:
                largest = max(largest, n)
                break
    print("small starting integers replayed", 19999, "latest exit", largest)


if __name__ == "__main__":
    small_paths()
    counters()
    two_runs()
    finite_exits()
