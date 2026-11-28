"""Finite controls for the actual inverse suffix and arithmetic reference laws."""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import gcd
from pathlib import Path
import json


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def physical_path(n):
    seen = set()
    path = []
    while n not in seen:
        require(len(path) < 1000, "finite control budget exceeded")
        seen.add(n)
        path.append(n)
        n = step(n)
    require(n in (1, 2), "unplanned repeat")
    return path


def source_controls():
    paths = [physical_path(n) for n in range(1, 769)]
    counts = Counter()
    for target in (5, 7, 10, 13, 16, 20, 23, 26):
        require(target not in (1, 2) and target in paths[target - 1], "invalid root")
        successes = [(p, p.index(target)) for p in paths if target in p]
        for k in range(7):
            cylinder_counts = Counter(p[t-k] for p, t in successes if t >= k)
            for v, count in cylinder_counts.items():
                require(count == sum(v in p for p in paths), "depth fibre is not its counted basin")
                p = paths[v-1] if v <= len(paths) else physical_path(v)
                require(p[k] == target, "wrong terminal point")
                odd_inputs = [x for x in p[:k] if x % 2]
                correction = Fraction(1)
                for x in odd_inputs:
                    correction *= Fraction(3 * x + 1, 3 * x)
                require(Fraction(2 ** k * target, 3 ** len(odd_inputs) * v) == correction,
                        "native correction identity")
                counts["depth_fibres"] += 1
            for z in (target, 2*target, 5*target, 200):
                for path, t in successes:
                    d = next(i for i, v in enumerate(path) if v % 2 and v <= z)
                    if t < d:
                        require(path[d] * 2 ** (d-t) == target, "post-target halving identity")
                        counts["even_target_before_odd_entrance"] += 1
                    if t < d + k:
                        require(path[d] <= 2 ** k * target, "missed suffix above small-landing bound")
                        counts["small_missed_suffixes"] += 1
                    if path[d] > 2 ** k * target:
                        require(d + k <= t, "large-landing native suffix is truncated")
                        direct = tuple(path[t-i] for i in range(k+1))
                        landed = path[d:]
                        adjusted = tuple(landed[t-d-i] for i in range(k+1))
                        require(direct == adjusted, "ordered integer suffix changed")
                        counts["high_readable_suffixes"] += 1
                    counts["source_target_depth_threshold_checks"] += 1
    for group in ("even_target_before_odd_entrance", "small_missed_suffixes", "high_readable_suffixes"):
        require(counts[group] > 0, "missing finite branch")
    return dict(sorted(counts.items()))


def geometric_mod_three(d):
    previous = [Fraction(1)]
    modulus = 1
    for _ in range(d):
        modulus *= 3
        order = 2 * (modulus // 3)
        require(pow(2, order, modulus) == 1, "invalid ternary period")
        distribution = [Fraction(0) for _ in range(modulus)]
        for r, mass in enumerate(previous):
            for gap in range(1, order+1):
                out = ((3*r+1) * pow(2, -gap, modulus)) % modulus
                distribution[out] += mass * Fraction(2 ** (order-gap), 2 ** order-1)
        require(sum(distribution) == 1, "lost geometric gap mass")
        previous = distribution
    return previous


def stationary_controls():
    checks = 0
    for depth in range(4):
        ternary = geometric_mod_three(depth)
        for unit in (1, 5, 7, 11, 35):
            require(gcd(unit, 6) == 1, "invalid finite cofactor")
            modulus = (3 ** depth) * unit
            expected = [ternary[r % (3**depth)] / unit for r in range(modulus)]
            forward = [Fraction(0) for _ in range(modulus)]
            for r, mass in enumerate(expected):
                if modulus == 1:
                    forward[0] += mass
                    continue
                for branch in (r, 3*r+1):
                    forward[(branch * pow(2, -1, modulus)) % modulus] += mass / 2
            require(forward == expected, "complete odd-modulus product stationarity")
            checks += modulus
    return checks


def parity_crt_checks():
    count = 0
    for modulus in (1, 5, 9, 15, 27):
        for length in range(1, 8):
            pairs = set()
            for y in range(1, modulus * 2**length + 1):
                x = y
                word = []
                for _ in range(length):
                    word.append(x % 2)
                    x = step(x)
                key = (y % modulus, tuple(word))
                require(key not in pairs, "nonunique parity CRT cylinder")
                pairs.add(key)
            require(len(pairs) == modulus * 2**length, "incomplete CRT grid")
            count += len(pairs)
    return count


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    names = ("NATURAL_INVERSE_RAY_EQUIDISTRIBUTION.md", "INVERSE_RAY_BROWNIAN_MOTION.md",
             "INVERSE_RAY_CYLINDER_INFORMATION.md")
    print(json.dumps({"scope": "exact finite arithmetic and genuine suffix tests only",
                      "physical": source_controls(), "stationary_residues": stationary_controls(),
                      "native_crt_cells": parity_crt_checks(),
                      "manuscript_hashes": {n: sha256((root/n).read_bytes()).hexdigest() for n in names}},
                     indent=2, sort_keys=True))
