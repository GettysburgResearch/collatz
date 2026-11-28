"""Exact rational controls of CRT normalization and the nearest-point reduction."""
from fractions import Fraction as Q
from math import gcd
import json


def require(ok, detail):
    if not ok:
        raise RuntimeError(detail)


def native_gap(x):
    y = 3 * x + 1
    return (y & -y).bit_length() - 1


def ternary_profile(k):
    # An outer geometric gap has periodic affine residues, exactly summed.
    law = {0: Q(1)}
    for j in range(1, k + 1):
        modulus = 3 ** j
        order = 2 * 3 ** (j - 1)
        updated = {}
        for gap in range(1, order + 1):
            weight = Q(1, 2 ** gap) / (1 - Q(1, 2 ** order))
            inv = pow(2, -gap, modulus)
            for previous, prob in law.items():
                target = ((3 * previous + 1) * inv) % modulus
                updated[target] = updated.get(target, Q(0)) + prob * weight
        law = updated
        require(sum(law.values()) == 1, "geometric tail aggregation")
    return {a: p * 3 ** k for a, p in law.items()}


def crt_controls():
    checks = 0
    for k in range(1, 4):
        modulus = 3 ** k
        profile = ternary_profile(k)
        for gap in range(1, 7):
            width = modulus * 2 ** (gap + 1)
            total = sum(profile.get(x % modulus, Q(0))
                        for x in range(1, width, 2) if native_gap(x) == gap)
            require(total / width == Q(1, 2 ** (gap + 1)), "harmonic flux CRT mean")
            checks += 1
    return checks


def nearest_controls():
    controls = 0
    for k in range(1, 5):
        q = 3 ** k
        for z in range(q):
            if gcd(z, 3) != 1:
                continue
            for r in (Q(1, 8), Q(z), Q(2*q-1, 3), Q(31*q+z, 2)):
                first = next(a for a in range(int(r) + 1, int(r) + 2*q + 1)
                             if a % 2 and a % q == z)
                require(r < first <= r + 2*q, "strict nearest representative")
                for j in range(1, 8):
                    a = first + 2*q*j
                    # Square all three terms for u=1/2.
                    middle = Q(q*q, a) / (a-r)
                    require(Q(q*q, a*a) <= middle <= Q(1, 4*j*j), "tail sandwich")
                    controls += 1
    return controls


if __name__ == "__main__":
    print(json.dumps({"native_crt_means": crt_controls(),
                      "nearest_representative_tail_sandwiches": nearest_controls()},
                     sort_keys=True))
