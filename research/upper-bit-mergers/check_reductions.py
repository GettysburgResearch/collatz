"""Exact finite replays for the prefix quotient and the ordered inverse words."""

from collections import Counter
from itertools import product

from check import step, walk


def check_prefixes(max_depth):
    representatives = {(0, 1): 0}
    tested = 0
    for h in range(max_depth + 1):
        exact = {}
        for r in range(2**h):
            y, odd = walk(1 + 3 * r, h)
            key = (odd, y)
            small = exact.setdefault(key, r)
            if 3 * (r - small) > 2 ** (h - odd):
                raise AssertionError(("distance", h, r, small))
            for tail in (0, 1, 7):
                n = 1 + 3 * (r + 2**h * tail)
                partner = 1 + 3 * (small + 2**h * tail)
                expected = (y + 3 ** (odd + 1) * tail, odd)
                if walk(n, h) != expected or walk(partner, h) != expected:
                    raise AssertionError(("lifted pair", h, r, small, tail))
            tested += 1
        if exact != representatives:
            raise AssertionError(("least representatives", h))
        if h == max_depth:
            break
        children = {}
        for (odd, y), r in representatives.items():
            for bit in (0, 1):
                z = y + 3 ** (odd + 1) * bit
                key = (odd + z % 2, step(z))
                child = r + 2**h * bit
                if key not in children or child < children[key]:
                    children[key] = child
        representatives = children
    print(f"{tested} prefixes, {len(representatives)} representatives at depth {max_depth}")


def box_residues(coefficients, intervals, modulus):
    """Count linear combinations by convolution, using only modular powers."""
    counts = {0: 1}
    for coefficient, interval in zip(coefficients, intervals, strict=True):
        terms = Counter(coefficient * pow(2, v, modulus) % modulus for v in interval)
        next_counts = Counter()
        for residue, count in counts.items():
            for term, ways in terms.items():
                next_counts[(residue + term) % modulus] += count * ways
        counts = next_counts
    return counts


def inverse_source(t, exponents):
    """Replay individual odd inverses, returning None at the first illegal one."""
    x = t
    for i in range(len(exponents) - 2, -1, -1):
        numerator = 2 ** (exponents[i + 1] - exponents[i]) * x - 1
        x, remainder = divmod(numerator, 3)
        if remainder:
            return None
        if x < 1 or x % 2 != 1:
            raise AssertionError(("invalid inverse state", t, exponents, x))
    return x * 2 ** exponents[0]


def check_box(s, length, t, width, start, delay):
    divisor = 3**length
    modulus = divisor * 3**s
    first_allowed_clock = start + length * width
    clock = first_allowed_clock + delay
    intervals = [
        range(start + i * width, start + (i + 1) * width)
        for i in range(length)
    ] + [range(clock, clock + 1)]
    coefficients = [-3 ** (length - 1 - i) for i in range(length)] + [t]
    modular = box_residues(coefficients, intervals, modulus)
    physical = Counter()
    seen = set()
    for exponents in product(*intervals):
        source = inverse_source(t, exponents)
        if source is None:
            continue
        if source in seen or walk(source, clock) != (t, length):
            raise AssertionError(("repeated source or wrong ordinary path", t, exponents))
        if not 0 < 2**clock * t - divisor * source < 2**first_allowed_clock:
            raise AssertionError(("physical interval", t, exponents))
        seen.add(source)
        physical[source % (3**s)] += 1
    for y in range(3**s):
        if physical[y] != modular.get(divisor * y, 0):
            raise AssertionError(("target residue count", s, length, t, width, y))
    return len(seen), len(physical)


def check_ancestors():
    ordinary = all_classes = 0
    cases = [
        (1, 1, 1, 6, 0, 0),
        (2, 1, 5, 18, 2, 11),
        (3, 2, 5, 24, 1, 0),
        (4, 2, 1, 54, 0, 17),
        (3, 3, 7, 24, 3, 41),
        (5, 2, 7, 54, 0, 115),
    ]
    for s, length, t, width, start, delay in cases:
        count, represented = check_box(s, length, t, width, start, delay)
        ordinary += count
        all_classes += represented == 3**s
    print(f"{ordinary} paths across {len(cases)} fixed clocks, {all_classes} cover every class")


def check_tails():
    checked = 0
    for w in range(32):
        x = 1 + 3 * w
        d = a = 0
        y = x
        while y != 1 and d < 300:
            a += y % 2
            y = step(y)
            d += 1
        if y != 1:
            raise AssertionError(("lower endpoint unavailable", x))
        for q in range(5):
            for e in (0, 1):
                j = d + 2 * q + e
                n = x + 3 * 2**j
                endpoint, _ = walk(n, d + 2 * q)
                if endpoint != 1 + 2**e * 3 ** (a + q + 1):
                    raise AssertionError(("shifted-power endpoint", n, q, e))
                if e == 1 and step(endpoint) != 2 + 3 ** (a + q + 2):
                    raise AssertionError(("odd residual step", n, q))
                checked += 1
    print(f"{checked} exact shifted-power tail identities")


if __name__ == "__main__":
    check_prefixes(14)
    check_ancestors()
    check_tails()
