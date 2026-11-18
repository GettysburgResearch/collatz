"""Exact controls for the marked terminal construction; no asymptotic inputs."""
from collections import Counter
from fractions import Fraction
from math import comb
import json


def transition_counts(steps, total_limit):
    levels = [{0: Counter({0: 1})}]
    for depth in range(1, steps + 1):
        modulus = 3**depth
        inverses = [pow(2, -e, modulus) for e in range(total_limit + 1)]
        current = {}
        for total, counts in levels[-1].items():
            for exponent in range(1, total_limit - total + 1):
                row = current.setdefault(total + exponent, Counter())
                for residue, count in counts.items():
                    target = (3*residue + 1)*inverses[exponent] % modulus
                    row[target] += count
        levels.append(current)
    return levels


def inverse_sources(root, depth, total):
    if depth == 0:
        if not total:
            yield root
        return
    for e in range(1, total - depth + 2):
        numerator = (root << e) - 1
        if numerator % 3 == 0:
            yield from inverse_sources(numerator // 3, depth - 1, total - e)


def depth_range(b):
    return range((b + 2)//3, (5*b)//3 + 1)


def exponent(depth, m):
    return (3**depth).bit_length() + m + 2


def physical_check():
    b = 6
    ell = b//4
    m = 2
    depths = depth_range(b)
    limit = exponent(depths[-1], m)
    distributions = transition_counts(depths[-1], limit)
    # These distinct odd roots all have odd successor 1 and have no return.
    roots = [(4**v - 1)//3 for v in range(14, 28)]
    checks = 0
    for d in depths:
        total = exponent(d, m)
        counts = distributions[d][total]
        if sum(counts.values()) != comb(total - 1, d - 1):
            raise ValueError("marked total marginal")
        coarse = Counter()
        for value, count in counts.items():
            coarse[value % (3**ell)] += count
        independent = Counter()
        for s, row in distributions[ell].items():
            remaining = total - s
            if remaining < d - ell:
                continue
            suffixes = comb(remaining - 1, d - ell - 1)
            for residue, count in row.items():
                independent[residue] += count*suffixes
        if coarse != independent:
            raise ValueError("coarse projection of marked law")
        for root in roots:
            sources = list(inverse_sources(root, d, total))
            if len(sources) != counts[root % (3**d)]:
                raise ValueError("actual inverse count")
            for source in sources:
                if not (root << m) <= source <= 8*(root << m):
                    raise ValueError("terminal physical window")
            checks += len(sources)
    # Distinct-source claim also compares different terminal depths.
    for root in roots:
        merged = [s for d in depths for s in inverse_sources(root, d, exponent(d, m))]
        if len(merged) != len(set(merged)):
            raise ValueError("repeated source at nonperiodic target")
    return {"base": b, "roots": len(roots), "depths": list(depths),
            "distinct_integral_sources": checks}


def first_crossing_mass(b, m, s):
    ell = b//4
    depths = depth_range(b)
    start, stop = depths[0] - ell, depths[-1] - ell
    denominator_exponent = exponent(depths[-1], m) - s
    previous = [1]
    first_total = 0
    occupation_total = 0
    for j in range(1, stop + 1):
        threshold = exponent(j + ell, m) - s
        if threshold <= 0 or threshold <= len(previous) - 1:
            raise ValueError("crossing threshold must advance")
        total = sum(previous)
        if j >= start:
            first_total += total << (denominator_exponent - threshold)
            ordinary_count = comb(threshold - 1, j - 1) if threshold >= j else 0
            occupation_total += ordinary_count << (denominator_exponent - threshold)
        current = []
        prefix = 0
        for a in range(threshold):
            current.append(prefix)
            if a < len(previous):
                prefix += previous[a]
        previous = current
    if not 0 <= first_total <= occupation_total:
        raise ValueError("first crossing versus total occupation")
    denominator = 1 << denominator_exponent
    return Fraction(first_total, denominator), Fraction(occupation_total, denominator)


def renewal_checks():
    rows = []
    for b in (32, 64, 128, 256, 512):
        possible_m = [m for m in range(b + 1)
                      if (1 << (20*m))*3**(9*b) >= 4**(9*b)
                      and (1 << (20*m))*3**(31*b) <= 4**(31*b)]
        ell = b//4
        possible_s = [s for s in range(ell, 3*ell + 1)
                      if (1 << (100*abs(s - 2*ell)))*3**b <= 4**b]
        # The limiting argument handles the entire interval. These finite
        # controls sample both boundaries and the middle at each scale.
        settings = {(m, s) for m in (possible_m[0], possible_m[len(possible_m)//2], possible_m[-1])
                    for s in (possible_s[0], possible_s[-1])}
        pairs = [first_crossing_mass(b, m, s) for m, s in sorted(settings)]
        first = min(x for x, _ in pairs)
        occupation = min(y for _, y in pairs)
        rows.append({"base": b, "cases": len(settings),
                     "min_first_crossing_floor_1e9": int(10**9*first),
                     "min_occupation_floor_1e9": int(10**9*occupation)})
    return rows


if __name__ == "__main__":
    print(json.dumps({"physical": physical_check(), "renewal": renewal_checks()},
                     indent=2, sort_keys=True))
