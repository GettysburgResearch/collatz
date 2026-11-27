"""Exact tests for pair orientations, frequency escape, burst recovery and gcd sieving."""

from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import combinations, product
from math import comb, gcd, prod


def check(truth, message):
    if not truth:
        raise AssertionError(message)


def affine(word):
    c = 0
    for i, bit in enumerate(word):
        if bit:
            c = 3 * c + 2 ** i
    return c


def factors(t):
    f = {}
    p = 2
    while p * p <= t:
        while t % p == 0:
            f[p] = f.get(p, 0) + 1
            t //= p
        p += 1 if p == 2 else 2
    if t > 1:
        f[t] = 1
    return f


def divisors(f):
    yield from (prod(p ** e for (p, _), e in zip(f.items(), exponents))
                for exponents in product(*(range(a + 1) for a in f.values())))


def phi(t):
    return prod(p ** (a - 1) * (p - 1) for p, a in factors(t).items())


def phase_escape():
    groups = small_transitions = 0
    for mod in range(5, 400):
        if gcd(mod, 6) != 1:
            continue
        ell = 0
        while 4 ** ell < mod:
            ell += 1
        inv3 = pow(3, -1, mod)

        @cache
        def test(k, remaining):
            nonlocal small_transitions
            centered = k if 2 * k <= mod else k - mod
            if 20 * abs(centered) >= mod:
                return
            check(remaining > 0, "large frequency missing")
            for r in (0, 1, 2):
                nxt = 4 * k * inv3 ** r % mod
                z = nxt if 2 * nxt <= mod else nxt - mod
                if 20 * abs(z) < mod:
                    check(3 ** r * z == 4 * centered, "small carry")
                    small_transitions += 1
                test(nxt, remaining - 1)

        for k in range(1, mod):
            test(k, ell)
            groups += 1
    print("frequency roots", groups, "small integer transitions", small_transitions)


def oriented_laws():
    pattern_count = 0
    for n in range(2, 11):
        for weights in product((0, 1, 2), repeat=n // 2):
            for single in range(2 if n % 2 else 1):
                u = sum(weights) + single
                if u == 0:
                    continue
                options = [[(0, 0)] if r == 0 else [(1, 1)] if r == 2
                           else [(1, 0), (0, 1)] for r in weights]
                tails = (single,) if n % 2 else ()
                words = [tuple(bit for pair in pairs for bit in pair) + tails
                         for pairs in product(*options)]
                base = affine(words[0])
                for mod in (5, 25, 35):
                    offsets = Counter({base % mod: 1})
                    previous = 0
                    for j, r in enumerate(weights):
                        if r == 1:
                            gap = pow(2, 2 * j, mod) * pow(3, u - 1 - previous, mod) % mod
                            offsets += Counter({(k + gap) % mod: v for k, v in offsets.items()})
                        previous += r
                    check(offsets == Counter(affine(w) % mod for w in words),
                          "mixed orientation convolution")
                pattern_count += 1
    print("exact paired occupancy laws", pattern_count)


def burst_laws():
    checked = 0
    for n in range(2, 10):
        for g in (5, 7, 11, 25, 35, 101, 1009):
            m = 0
            while m < n and 3 ** (m + 1) <= g:
                m += 1
            for start in range(n - m + 1):
                seen = set()
                for w in product((0, 1), repeat=n):
                    key = (sum(w), w[:start] + w[start + m:], affine(w) % g)
                    check(key not in seen, "burst collision")
                    seen.add(key)
                    checked += 1
    print("exact burst recoveries", checked)


def gcd_law(n, u, sieve_order):
    D = abs(2 ** n - 3 ** u)
    fs = factors(D)
    ds = tuple(divisors(fs))
    N = comb(n, u)
    histogram = Counter()
    for odd in combinations(range(n), u):
        c = sum(2 ** i * 3 ** (u - 1 - j) for j, i in enumerate(odd))
        histogram[gcd(c, D)] += 1
    check(sum(histogram.values()) == N, "slice size")
    model = {d: Fraction(phi(D // d), D) for d in ds}
    check(sum(model.values()) == 1, "totient histogram")
    div_actual = {d: sum(v for b, v in histogram.items() if b % d == 0) for d in ds}
    marginal = max(abs(Fraction(div_actual[d], N) - Fraction(1, d)) for d in ds)
    tv = sum(abs(Fraction(histogram[d], N) - model[d]) for d in ds) / 2
    for d in ds:
        ps = tuple(p for p in fs if (D // d) % p == 0)
        partial = Fraction(0)
        partial0 = Fraction(0)
        for j in range(sieve_order):
            for subset in combinations(ps, j):
                v = d * prod(subset)
                partial += (-1) ** j * Fraction(div_actual[v], N)
                partial0 += (-1) ** j * Fraction(1, v)
        err = sum(Fraction(div_actual[d * prod(ii)], N) for ii in combinations(ps, sieve_order))
        err0 = sum(Fraction(1, d * prod(ii)) for ii in combinations(ps, sieve_order))
        check(abs(Fraction(histogram[d], N) - partial) <= err, "observed Bonferroni bound")
        check(abs(model[d] - partial0) <= err0, "uniform Bonferroni bound")
    for p, e in fs.items():
        mu = sum(Fraction(div_actual[p ** j], N) for j in range(1, e + 1))
        exact = sum(Fraction(num * factors(d).get(p, 0), N) for d, num in histogram.items())
        check(mu == exact, "prime-power logarithmic coefficient")
    print("full histogram", (n, u), "D", D, "TV", str(tv), "max divisor mass error", str(marginal))
    return histogram, D


def residue_counts(n, target, mod):
    """Independent recurrence keeping the integer numerator and the odd count."""
    rows = [[0] * mod for _ in range(target + 1)]
    rows[0][0] = 1
    for i in range(n):
        it = pow(2, i, mod)
        for r in range(min(target, i + 1), 0, -1):
            diagonal = rows[r - 1]
            current = rows[r]
            for x, mass in enumerate(diagonal):
                current[(3 * x + it) % mod] += mass
    return rows[target]


if __name__ == "__main__":
    phase_escape()
    oriented_laws()
    burst_laws()
    for n, u in ((8, 4), (10, 5), (14, 8), (16, 10), (18, 11), (20, 12), (12, 9)):
        gcd_law(n, u, 2)
    for n, u, g in ((40, 25, 25), (80, 50, 35), (160, 100, 35), (200, 126, 77)):
        counts = residue_counts(n, u, g)
        N = comb(n, u)
        check(sum(counts) == N, "dynamic exact slice")
        num = max(abs(g * mass - N) for mass in counts)
        print("exact slice", (n, u, g), "max point error", str(Fraction(num, g * N)))
    # A finite nonuniform example protects the absolute-error interpretation.
    c = residue_counts(8, 4, 175)
    check(sum(m > 0 for m in c) < 175 and len(set(c)) > 1, "finite sparse support")
