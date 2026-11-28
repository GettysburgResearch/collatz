"""Exact finite shape, dual, and source-grid controls for localized real intervals."""
from collections import Counter
from itertools import product
from math import gcd
import json

from check_line_shadow_structure import require


def convergents(p, q):
    old_p, last_p = 0, 1
    old_q, last_q = 1, 0
    while q:
        digit, remainder = divmod(p, q)
        p, q = q, remainder
        old_p, last_p = last_p, old_p + digit * last_p
        old_q, last_q = last_q, old_q + digit * last_q
        yield last_p, last_q


def short_dual(h, t, length, width):
    q = 3**h
    scale = pow(2, t + length, q)
    a_max = 2**(length - 1)
    b_max = q // (2 * width)
    require(a_max < q and b_max < q and 2 * a_max * b_max < q,
            "continued fractions require the Legendre range")
    for p, b in convergents(scale, q):
        if b > b_max:
            break
        a = q * p - scale * b
        if abs(a) <= a_max:
            require(a and b and (a + 2**(t + length) * b) % q == 0, "false dual witness")
            return a, b
    return None


def direct_dual(h, t, length, width):
    q = 3**h
    scale = pow(2, t + length, q)
    for b in range(1, 1 + q // (2 * width)):
        a = -(scale * b) % q
        if min(a, q - a) <= 2**(length - 1):
            return True
    return False


def exact_distribution(h, t, length, width, first, floor, counts):
    q = 3**h
    mod = 2**length
    direct = Counter()
    inv = pow(2, -t, q)
    for m in range(first, first + width):
        d = floor * q + m * inv % q
        direct[d % mod] += 1
    by_lattice = Counter()
    for d in range(floor * q, (floor + 1) * q):
        first_m = first + ((pow(2, t, q) * d - first) % q)
        if first_m < first + width:
            by_lattice[d % mod] += 1 + (first + width - 1 - first_m) // q
    require(direct == by_lattice and sum(direct.values()) == width,
            "affine translated lattice disagrees with direct fixed-floor count")
    if q <= width:
        require(max(direct.values()) * mod <= 4 * width, "small modulus estimate")
        counts["small_modulus_boxes"] += 1
    elif not short_dual(h, t, length, width):
        require(max(direct.values()) * mod <= 8 * width, "dual-free box majorant")
        counts["dual_free_boxes"] += 1
        counts["nontrivial_bounds"] += mod > 8
    else:
        counts["finite_obstructed_boxes"] += 1
    counts["source_positions"] += width
    counts["all_residues_in_boxes"] += mod


def outside(x, primes):
    x = abs(x)
    require(x > 0, "zero cofactor")
    for p in primes:
        while x % p == 0:
            x //= p
    return x


def endpoint_ledger(n, m, q, counts):
    primes = (2, 3, 5, 7)
    d, h = m, n
    trace = []
    while h:
        odd = d % 2
        trace.append((h, d, odd))
        h -= odd
        d = (d + odd * q * 3**h) // 2
    for i, (start_h, u, _) in enumerate(trace):
        for j in range(i + 1, min(i + 15, len(trace))):
            h, v, _ = trace[j]
            if h == start_h:
                continue
            Q = q * 3**h
            x = 2**(j - i) * v
            diff = x - u
            require(diff > 0 and diff % Q == 0, "nonpositive carry or incorrect denominator")
            k = diff // Q
            g = gcd(x, u)
            require(k % g == 0, "primitive gcd does not divide the word carry")
            w = outside(x // g, primes) * outside(u // g, primes) * outside(diff // g, primes)
            require(w * g <= k * outside(u, primes) * outside(v, primes),
                    "outside-prime product failed to cancel")
            counts["coprime_endpoint_pairs"] += 1
            counts["nonprimitive_endpoint_pairs"] += g > 1
            counts["negative_endpoint_inputs"] += u < 0


def main():
    counts = Counter()
    for h in range(2, 11):
        for length in range(1, min(5, h) + 1):
            for width in (2**(2 * length), 2**(2 * length) + 5):
                for t in range(0, 3 * h + 3):
                    result = short_dual(h, t, length, width)
                    require(bool(result) == direct_dual(h, t, length, width),
                            "continued fraction search missed a primitive small dual")
                    counts["dual_exhaustive_comparisons"] += 1
                    counts["genuine_nonzero_quotient_obstructions"] += bool(result)
    for h, length, width in ((4, 1, 4), (4, 3, 140), (6, 4, 729), (7, 4, 257),
                             (8, 5, 1025), (9, 5, 1024)):
        for t, floor in product((0, 1, 3, h - 1, 2 * h, 3 * h), (0, 7)):
            for first in (1, 41, 3**h - min(3**h, width) + 1):
                exact_distribution(h, t, length, width, first, floor, counts)
    for n in (40, 80, 160, 320, 640):
        width = 3**(n // 4) + 1
        for h, t, length in product((n // 3, n // 2, n), (0, n // 2, n, 3 * n), (2, n // 12)):
            result = short_dual(h, t, length, width)
            counts["large_modulus_cf_tests"] += 1
            counts["large_modulus_short_duals"] += bool(result)
    for n, m, q in product(range(2, 9), (1, 5, 16, 25, 49, -1, -7, -32), (1, 5, 7, 35)):
        if gcd(m, 3 * q) == 1:
            endpoint_ledger(n, m, q, counts)
    for key in ("genuine_nonzero_quotient_obstructions", "finite_obstructed_boxes",
                "dual_free_boxes", "nontrivial_bounds", "small_modulus_boxes",
                "nonprimitive_endpoint_pairs", "negative_endpoint_inputs"):
        require(counts[key] > 0, f"missing {key} control")
    print(json.dumps(dict(counts), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
