"""Exact controls for full denominators, physical cuts and product packing."""
from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, isqrt, lcm, prod
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def carry(bits):
    value = 0
    for i, bit in enumerate(bits):
        if bit:
            value = 3 * value + (1 << i)
    return value


def marked_walk(bits):
    length = len(bits)
    gap = 2**length - 3**sum(bits)
    if not any(bits) or gap <= 0:
        return None
    start = Fraction(carry(bits), gap)
    n = start.numerator
    d = start.denominator
    nodes = []
    for bit in bits:
        require(n % 2 == bit, "literal parity")
        require(gcd(n, d) == 1, "reduced denominator")
        nodes.append(n)
        n = (3 * n + d) // 2 if bit else n // 2
    require(n == start.numerator, "literal closure")
    require(3 * gap * min(nodes) <= d * sum(bits) * 2**length,
            "rational minimum floor")
    return nodes, d


def prime_orders(n):
    result = Counter()
    trial = 2
    while trial * trial <= n:
        while n % trial == 0:
            result[trial] += 1
            n //= trial
        trial += 1 if trial == 2 else 2
    if n > 1:
        result[n] += 1
    return result


def independent_modulo_sign(centers):
    basis = {}
    for center in centers:
        row = prime_orders(abs(center.numerator))
        row.subtract(prime_orders(center.denominator))
        row = {p: Fraction(v) for p, v in row.items() if v}
        while row:
            prime = min(row)
            coefficient = row[prime]
            if prime not in basis:
                basis[prime] = {p: v / coefficient for p, v in row.items()}
                break
            for p, v in basis[prime].items():
                row[p] = row.get(p, 0) - coefficient * v
                if not row[p]:
                    del row[p]
        else:
            return False
    return True


def check_cuts(bits, nodes, d, counts):
    length = len(bits)
    index = nodes.index(min(nodes))
    bits = bits[index:] + bits[:index]
    nodes = nodes[index:] + nodes[:index]
    m = nodes[0]
    weights = [sum(bits[:j]) for j in range(length)]
    gaps = [0]
    centers = [Fraction()]
    for j in range(1, length):
        suffix = bits[j:]
        u, v = 2**len(suffix), 3**sum(suffix)
        gap = u - v
        physical = carry(suffix)
        center = Fraction(physical, gap)
        require(d * physical == u * m - v * nodes[j], "endpoints")
        require(gcd(gap, d * physical) == gcd(gap, m - nodes[j]),
                "exact endpoint gcd")
        require(center.denominator * abs(m - nodes[j]) >= abs(gap),
                "reduced center lower bound")
        gaps.append(gap)
        centers.append(center)
        counts["proper_centers"] += 1
    for i in range(1, length):
        for j in range(i + 1, length):
            u, v = 2**(j - i), 3**(weights[j] - weights[i])
            a, b = centers[i], centers[j]
            require((u - v) % gcd(gaps[i], gaps[j]) == 0, "nested gaps")
            earlier = u * m - v * nodes[i]
            later = v * m - u * nodes[j]
            require(earlier != 0 and later != 0, "nonzero cross terms")
            require(earlier % gcd(b.denominator, a.numerator) == 0,
                    "earlier carry against later center")
            require(later % gcd(a.denominator, b.numerator) == 0,
                    "later carry against earlier center")
            counts["unordered_cut_pairs"] += 1
    t = min(isqrt(length), length - 1)
    bs = [x.denominator for x in centers[1 : t + 1]]
    pair_gcds = (gcd(x, y) for j, x in enumerate(bs) for y in bs[:j])
    require(prod(bs) <= lcm(*bs) * prod(pair_gcds), "lcm overlap")
    family = centers[1 : t + 1]
    if family and all(family):
        counts["nonzero_center_families"] += 1
        independent = independent_modulo_sign(family)
        counts["independent_center_families"] += int(independent)
        dominant = all(
            x.denominator > prod(gcd(x.denominator, abs(y.numerator)*y.denominator)
                                 for i, y in enumerate(family) if i != j)
            for j, x in enumerate(family))
        if dominant:
            require(independent, "maximal coefficient valuation rank certificate")
            counts["rank_families_certified_by_overlap"] += 1


def verify(last_length=13):
    counts = Counter()
    clocks = defaultdict(Counter)
    known_periods = set()
    packed = defaultdict(list)
    for length in range(1, last_length + 1):
        for raw in range(2**length):
            bits = [(raw >> j) & 1 for j in range(length)]
            counts["all_marked_words"] += 1
            result = marked_walk(bits)
            if result is None:
                continue
            nodes, d = result
            p = sum(bits)
            clocks[length, p][d] += 1
            counts["positive_marked_words"] += 1
            if len(set(nodes)) < length or (d, min(nodes)) in known_periods:
                continue
            known_periods.add((d, min(nodes)))
            counts["primitive_necklaces"] += 1
            odd = [n for n in nodes if n % 2]
            require(all(gcd(n, 6 * d) == 1 for n in odd), "coprime odd nodes")
            require(2**length * prod(odd) == prod(3*n + d for n in odd),
                    "exact lap product")
            packed[d].append((length, odd))
            check_cuts(bits, nodes, d, counts)
    for (length, p), histogram in clocks.items():
        gap = 2**length - 3**p
        q = Fraction(p * 2**length, 3 * gap)
        for d, number in histogram.items():
            require(gap % d == 0 and number <= length * int(d * q),
                    "per-denominator marked-word count")
        divisors = sum(2 - (k*k == gap) for k in range(1, isqrt(gap)+1)
                       if gap % k == 0)
        require(sum(Fraction(number, d) for d, number in histogram.items())
                <= length * q * divisors, "full reciprocal moment")
    for d, groups in packed.items():
        odd = sorted(n for _, members in groups for n in members)
        require(len(set(odd)) == len(odd), "disjoint primitive cycles")
        floors = []
        n = 0
        while len(floors) < len(odd):
            n += 1
            if gcd(n, 6*d) == 1:
                floors.append(n)
        total = sum(length for length, _ in groups)
        require(2**total * prod(floors) <= prod(3*n+d for n in floors),
                "packed clock")
    return dict(sorted(counts.items())) | {
        "maximum_word_length": last_length, "contracting_clock_pairs": len(clocks),
        "reduced_denominators_packed": len(packed)}


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
