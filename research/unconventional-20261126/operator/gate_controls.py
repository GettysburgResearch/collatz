"""Exact arithmetic on finite first-exit gates at exponent two."""

from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
import json


def check(ok, reason):
    if not ok:
        raise ValueError(reason)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def slope(n):
    return F(3 if n % 2 else 1, 2)


def gates(cutoff):
    # cache[n] stores its finite exit gate and slope from n, or None for a cycle.
    cache = {}
    masses = defaultdict(F)
    counts = defaultdict(int)
    for x in range(1, cutoff):
        path = []
        seen = set()
        n = x
        while n < cutoff and n not in cache and n not in seen:
            path.append(n)
            seen.add(n)
            n = step(n)
        if n >= cutoff:
            result = n, F(1)
        else:
            result = cache.get(n)
        for z in reversed(path):
            if result is not None:
                y, product = result
                result = y, slope(z) * product
            cache[z] = result
        result = cache[x]
        if result is not None:
            y, product = result
            check(cutoff <= y <= 3 * cutoff // 2 and y % 3 == 2, "gate location")
            check(product * x <= y, "positive distortion")
            masses[y] += (product / y) ** 2
            counts[y] += 1
    return dict(masses), dict(counts)


def advance(mass, lower, upper):
    result = defaultdict(F)
    sources = list(mass.items())
    sources.extend((x, F(1, x * x)) for x in range(lower, upper))
    for x, weight in sources:
        n, c, seen = x, F(1), set()
        while n < upper and n not in seen:
            seen.add(n)
            c *= slope(n)
            n = step(n)
        if n >= upper:
            result[n] += weight * (c * x / n) ** 2
    return dict(result)


def direct(cutoff):
    total = defaultdict(F)
    for x in range(1, cutoff):
        seen, n, c = set(), x, F(1)
        while n < cutoff and n not in seen:
            seen.add(n)
            c *= slope(n)
            n = step(n)
        if n >= cutoff:
            total[n] += (c / n) ** 2
    return dict(total)


def floor_scaled(x):
    return x.numerator * 10**15 // x.denominator


def digest(values):
    h = sha256()
    for y, w in sorted(values.items()):
        h.update(f"{y}:".encode())
        for value in (w.numerator, w.denominator):
            data = value.to_bytes((value.bit_length() + 7) // 8, "big")
            h.update(len(data).to_bytes(8, "big") + data)
    return h.hexdigest()


def main():
    outputs = []
    previous = None
    for n in (10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000):
        mass, count = gates(n)
        if n <= 1000:
            check(mass == direct(n), "independent path replay")
        total = sum(mass.values(), F())
        if previous:
            prior_n, prior_total, prior_mass = previous
            # Integral lower bound on the fresh source weights proves monotonicity
            # for these particular comparisons without evaluating zeta(2).
            new_source_lower_bound = F(1, prior_n) - F(1, n)
            check(total <= prior_total + new_source_lower_bound, "monotone augmented flux")
            if n <= 1000:
                check(advance(prior_mass, prior_n, n) == mass, "exact gate transport")
        expected_gates = {step(z) for z in range(1, n, 2) if step(z) >= n}
        check(set(mass) == expected_gates, "gate support equality")
        previous = n, total, mass
        best = sorted(mass, key=lambda y: -mass[y])[:3]
        outputs.append({
            "cutoff": n, "number_of_gates": len(mass),
            "exiting_starts": sum(count.values()),
            "total_flux_floor_1e15": floor_scaled(total),
            "largest": [{"gate": y, "flux_floor_1e15": floor_scaled(mass[y]),
                         "exiting_starts": count[y]} for y in best],
            "all_exact_gate_weights_sha256": digest(mass),
        })
    print(json.dumps(outputs, indent=2))


if __name__ == "__main__":
    main()
