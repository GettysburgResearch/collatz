"""Exact finite controls for the multi-arm path and growing-family fibre theorems."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def odd(x):
    return x.numerator % 2


def step(x):
    return (3 * x + 1) // 2 if isinstance(x, int) and odd(x) else (
        x // 2 if isinstance(x, int) else (3 * x + 1) / 2 if odd(x) else x / 2)


def trace(x, length):
    values = [x]
    grades = [0]
    carries = [0]
    for k in range(length):
        bit = odd(values[-1])
        grades.append(grades[-1] + bit)
        carries.append((1 + 2 * bit) * carries[-1] + (1 << k) * bit)
        values.append(step(values[-1]))
        require((1 << (k + 1)) * values[-1] == 3 ** grades[-1] * x + carries[-1],
                "true affine source identity")
    return values, grades, carries


def filtration_controls():
    configs = [((0, 1, 3, 6), (7, 0, -13, 25)), ((0, 2, 4), (0, 0, 0)),
               ((3, 5, 7), (0, -17, 51))]
    cells = pairs = unequal = 0
    for exponents, offsets in configs:
        for depth in range(10):
            for z in range(1 << depth):
                outputs = []
                for x in (z, z + (1 << depth)):
                    arms = [trace(3 ** s * x + offset, depth + 1)
                            for s, offset in zip(exponents, offsets)]
                    outputs.append(arms)
                cells += 1
                for i, j in combinations(range(len(exponents)), 2):
                    sign_sums = [0, 0]
                    signs = []
                    for arms in outputs:
                        a, b = arms[i], arms[j]
                        a_bits = [odd(y) for y in a[0][:-1]]
                        b_bits = [odd(y) for y in b[0][:-1]]
                        sign_sums[0] += 2 * a_bits[-1] - 1
                        sign_sums[1] += 2 * b_bits[-1] - 1
                        products = [(2 * a0 - 1) * (2 * b0 - 1) for a0, b0 in zip(a_bits, b_bits)]
                        mismatch = sum(a0 != b0 for a0, b0 in zip(a_bits, b_bits))
                        require(sum(products) == depth + 1 - 2 * mismatch, "pair bracket")
                        signs.append(products[-1])
                        unequal += int(a[0][-1] == b[0][-1] and
                                       exponents[i] + a[1][-1] != exponents[j] + b[1][-1])
                    require(sign_sums == [0, 0] and signs[0] == signs[1],
                            "joint fair labels and predictable pair sign")
                    pairs += 1
    require(unequal > 0, "control must include accidental numerical hits")
    return {"joint_cells": cells, "pair_child_checks": pairs, "unequal_slope_leaf_hits": unequal}


def fibre_controls():
    intervals = [(3, 1), (8, 17), (9, 8071), (9, 10 ** 18 + 137)]
    checks = moments = hole_triples = fragmented = edges = 0
    for depth, origin in intervals:
        sizes = [0, 1, 2, 4, 5, 7, 8]
        for x in range(origin, origin + (1 << depth)):
            endpoints = [trace(3 ** s * x, depth)[0][-1] for s in sizes]
            counts = Counter(endpoints)
            length = len(sizes)
            for power in (2, 3):
                expected = sum(n ** power for n in counts.values())
                actual = sum(len({endpoints[k] for k in choice}) == 1
                             for choice in product(range(length), repeat=power))
                require(actual == expected, "conditional sampling power sum")
                moments += 1
            for i, j, k in combinations(range(length), 3):
                p, q, r = (endpoints[h] for h in (i, j, k))
                hole = p == r and p != q
                require(len({p, q, r}) == 3 or p == q or q == r or hole,
                        "three-label partition")
                require((len({p, q, r}) == 3) ==
                        ((p != q) + (q != r) - (p != r) - 2 * hole),
                        "finite correction to three-path formula")
                hole_triples += hole
            fine = sum(a != b for a, b in zip(endpoints, endpoints[1:]))
            coarse = sum(a != b for a, b in zip(endpoints[::2], endpoints[2::2]))
            require(coarse <= fine, "coarse boundaries bounded by fine")
            fragmented += fine > coarse
            edges += fine - coarse
            checks += 1
    require(hole_triples and fragmented, "both microscopic countercontrols")
    return {"integer_families": checks, "independent_label_moments": moments,
            "outer_equal_interior_unequal_triples": hole_triples,
            "families_with_coarse_boundary_loss": fragmented, "coarse_boundary_loss_sum": edges}


def signed_pair(x, y, k, length):
    v1, g1, _ = trace(x, length)
    v2, g2, _ = trace(y, length)
    levels = [k + b - a for a, b in zip(g1, g2)]
    for h in range(length):
        if levels[h] == 0 and v1[h] == v2[h]:
            require(levels[h + 1] == 0 and v1[h + 1] == v2[h + 1], "counted persistence")
    return levels


def tower_controls():
    samples = 0
    lower_certificates = []
    for d in range(3, 14):
        previous = None
        for stage in (d, d + 1):
            branches = [x for x in range(1 << stage) if x % 8 in (1, 3)]
            final = [signed_pair(x, 3 * x, 1, stage) for x in branches]
            mean = Fraction(sum(z[-1] for z in final), len(final))
            absolute = Fraction(sum(abs(z[-1]) for z in final), len(final))
            reverse = Fraction(sum(max(-z[-1], 0) for z in final), len(final))
            require(mean == 1 and absolute == 1 + 2 * reverse, "stationary signed rank")
            if previous is not None:
                departures = Fraction(sum(z[-2] == 0 and z[-1] != 0 for z in final), len(final))
                require(absolute == previous + departures, "absolute-rank drift")
                lower_certificates.append([stage, str(absolute)])
            previous = absolute
            samples += len(branches)
    require(max(Fraction(row[1]) for row in lower_certificates) >= Fraction(11, 8),
            "strict boundary surplus coefficient")
    rational_pairs = 0
    for shift in (0, 2):
        for n in (0, 5, 14, 40):
            m = 6
            family = [shift + Fraction(1, 3 ** (n + m - 1 - k)) for k in range(m)]
            for i, j in combinations(range(m), 2):
                require(family[j] == 3 ** (j-i) * family[i] + (1 - 3 ** (j-i)) * shift,
                        "reversed descending affine pair")
                signed_pair(family[i], family[j], j-i, 12)
                rational_pairs += 1
    return {"adjacent_tower_lifts": samples, "exact_mean_absolute_ranks": lower_certificates,
            "signed_rational_pair_controls": rational_pairs}


if __name__ == "__main__":
    result = {"finite_scope": "exact source, martingale-step and fibre identities; asymptotic laws are proved in the manuscripts",
              "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "filtration": filtration_controls(), "fibres": fibre_controls(), "towers": tower_controls()}
    print(json.dumps(result, indent=2, sort_keys=True))
