"""Exact bounds and positive-trajectory checks for NATIVE_LOWER_TYPE.md."""
from fractions import Fraction as F
from itertools import product
import json


def require(condition, description):
    if not condition:
        raise ValueError(description)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    products = [x * y for x in a for y in b]
    return min(products), max(products)


def div(a, b):
    require(b[0] > 0, "positive interval denominator required")
    return mul(a, (1 / b[1], 1 / b[0]))


def point(x):
    return F(x), F(x)


def log_small(x):
    require(1 <= x <= 2, "outside logarithm reduction interval")
    u = (x - 1) / (x + 1)
    terms = 25
    total = 2 * sum(u ** (2 * k + 1) / (2 * k + 1) for k in range(terms))
    tail = 2 * u ** (2 * terms + 1) / ((2 * terms + 1) * (1 - u * u))
    return total, total + tail


LN2 = log_small(F(2))


def log2(x):
    x = F(x)
    require(x > 0, "logarithm argument")
    scale = 0
    while x < 1:
        x *= 2
        scale -= 1
    while x > 2:
        x /= 2
        scale += 1
    return add(div(log_small(x), LN2), point(scale))


def entropy(p):
    return neg(add(mul(point(p), log2(p)), mul(point(1 - p), log2(1 - p))))


TABLE = [
    ("1.01", ".0062", ".994", ".0008"),
    ("1.10", ".056", ".952", ".0070"),
    ("1.25", ".121", ".907", ".0060"),
    ("1.50", ".195", ".870", ".0081"),
    ("2", ".280", ".839", ".0135"),
    ("3", ".359", ".815", ".0080"),
    ("4.82", ".414", ".804", ".0225"),
    ("6", ".432", ".797", ".0035"),
    ("10", ".459", ".799", ".0480"),
]


def table_checks():
    theta = log2(3)
    drift = sub(point(1), mul(point(F(1, 2)), theta))
    for row in TABLE:
        kappa, p1, z, margin = map(F, row)
        p0 = (kappa - 1) / (2 * kappa)
        require(p0 < p1 < F(1, 2), "nonempty lower sector")
        require(kappa * p1 * theta[1] < kappa - 1, "finite target criterion")
        log_b = add(mul(sub(point(1), theta), log2(z)), log2((1 + z*z) / (1 - z**6)))
        for p in (p0, p1):
            r = div(point(kappa * p - (kappa - 1) / 2), drift)
            trial = add(neg(log2(z)), mul(r, log_b))
            fair = sub(mul(point(kappa), entropy(p)), point(kappa - 1))
            require(sub(fair, trial)[0] > margin, "claimed strict fair margin")
    return len(TABLE) * 2


def children(v, first):
    return [e for e in range(first, first + 6) if (pow(2, e, 9) * v) % 9 in (4, 7)]


def shortcut(x):
    return (3*x+1)//2 if x % 2 else x//2


def replay(n, t):
    q = 0
    for _ in range(t):
        q += n % 2
        n = shortcut(n)
    return n, q


def branch_checks():
    hits = 0
    paths = 0
    for residue in (1, 2, 4, 5, 7, 8):
        for first in (1, 3):
            d = children(residue, first)
            require(len(d) == 2 and d[0] % 2 == d[1] % 2, "two unit branch classes")
            hits += 1
    for depth in range(1, 6):
        seen = set()
        for letters in product(range(4), repeat=depth):
            u = 1
            h = 0
            for letter in letters:
                e = 6*(letter//2) + children(u, 3)[letter % 2]
                parent = u
                u = ((1 << e)*u-1)//3
                require(u > parent and u % 2 == 1 and u % 3, "strict ordinary unit child")
                require(replay(u, e) == (parent, 1), "exact native inverse")
                h += e
            require(u not in seen, "distinct first-hit ancestors")
            seen.add(u)
            n = u << (100 - u.bit_length())
            h += 100 - u.bit_length()
            require((1 << 99) <= n < (1 << 100), "octave lift")
            require(replay(n, h) == (1, depth), "ordinary first arrival")
            require(replay(n, h-1)[0] == 2, "last ordinary even state")
            for extra in range(8):
                require(replay(n, h + extra)[1] == depth + (extra+1)//2, "actual alternating suffix")
            paths += 1
    return hits, paths


if __name__ == "__main__":
    rows = table_checks()
    residues, paths = branch_checks()
    print(json.dumps({"analytic_table_endpoints": rows, "unit_residue_periods": residues,
                      "ordinary_inverse_paths": paths, "full_suffix_replays": 8*paths}, indent=2))
