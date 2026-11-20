"""Independent bounded reconstruction of the local affine-grade theorem."""

from collections import defaultdict
from fractions import Fraction
import json


def demand(value, message):
    if not value:
        raise RuntimeError(message)


def T(x):
    demand(x >= 1, "ordinary positive source")
    return (3 * x + 1) // 2 if x % 2 else x // 2


def hit(x):
    d = p = 0
    bits = []
    while x != 1:
        demand(d < 10000, "unresolved first hit")
        bits.append(x % 2)
        p += x % 2
        x = T(x)
        d += 1
    return d, p, bits


def val(x, prime):
    v = 0
    while x % prime == 0:
        x //= prime
        v += 1
    return v


cocycles = 0
for n in range(1, 257):
    d, p, _ = hit(n)
    base = d - 2 * p
    x = n
    q = 0
    for j in range(d + 11):
        dz, pz, _ = hit(x)
        demand(base == j - 2 * q + dz - 2 * pz, "cocycle, including beyond first hit")
        cocycles += 1
        q += x % 2
        x = T(x)

groups = defaultdict(list)
t0 = 10
for a in (1, 2, 3, 4, 6, 8, 9, 12, 5, 10, 15, 20):
    u, v = val(a, 2), val(a, 3)
    residual = a // (2**u * 3**v)
    for x in range(1, 33):
        d, p, bits = hit(x)
        C = d - 2 * p - u - 2 * v
        groups[(residual, C)].append((a, x - a * t0, x, d, p, bits, u, v))

certificates = arms_checked = edges = 0
for (residual, C), arms in groups.items():
    h = max(0, *(d - u for a, b, x, d, p, bits, u, v in arms))
    while (h - C) % 2:
        h += 1
    Q = (h - C) // 2
    demand(Q >= 0, "nonnegative common exponent")
    for a, b, x, d, p, bits, u, v in arms:
        l = h + u
        demand(l >= d and (l - d) % 2 == 0, "padding clock")
        word = bits + [1, 0] * ((l - d) // 2)
        demand(sum(word) + v == Q, "common ternary exponent")
        # Formal affine reconstruction works on rational inputs as algebra,
        # independently of the ordinary path calculations below.
        slope, offset = Fraction(a), Fraction(b)
        for bit in word:
            slope = slope * (3 if bit else 1) / 2
            offset = (3 * offset + 1) / 2 if bit else offset / 2
        demand(slope * t0 + offset == 1, "base endpoint")
        demand(slope * 2**h == residual * 3**Q, "cylinder endpoint slope")
        for k in (-2, -1, 0, 1, 3):
            n = a * (t0 + 2**h * k) + b
            if n <= 0:
                continue
            demand(k >= 0, "unexpected positive negative lift")
            for bit in word:
                demand(n % 2 == bit, "parity legality")
                n = T(n)
                edges += 1
            demand(n == 1 + residual * 3**Q * k, "ordinary lift endpoint")
        arms_checked += 1
    certificates += 1

# The h=0, unequal padded-length corner: a=4 and a=3, both starts 1.
for t in range(1, 65):
    demand(T(T(4 * t - 3)) == 3 * t - 2, "h=0 certificate with an empty arm")

# A genuine cylinder meeting at the nonterminal value 5 when t=1.
nonterminal = 0
for t in range(1, 65):
    x, y, z = 2 * t + 1, 6 * t + 4, 3 * t + 2
    demand(T(x) == z == T(y), "nonterminal cylinder meeting")
    dx, px, _ = hit(x)
    dy, py, _ = hit(y)
    demand(dx - 2 * px - 1 == dy - 2 * py - 3, "nonterminal adjusted grades")
    nonterminal += 1

print(json.dumps({
    "status": "PASS", "cocycle_prefixes_including_post_hit": cocycles,
    "general_grade_groups": certificates, "general_affine_arms": arms_checked,
    "literal_lift_edges": edges, "zero_depth_mixed_clock_lifts": 64,
    "nonterminal_endpoint_cylinder_parameters": nonterminal,
    "scope": "Independent bounded arithmetic; universal local equivalence reconstructed separately."
}, indent=2, sort_keys=True))
