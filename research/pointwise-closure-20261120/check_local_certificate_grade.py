#!/usr/bin/env python3
"""Exact, standard-library replay for LOCAL_CERTIFICATE_GRADE.md.

This is bounded implementation evidence, not a proof of universal convergence.
All first-hit loops have an explicit cap and fail rather than infer convergence.
"""

from __future__ import annotations

import copy
import hashlib
import json
import random
from collections import Counter
from fractions import Fraction


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    require(n > 0, "positive ordinary domain")
    return (3 * n + 1) // 2 if n & 1 else n // 2


def first_hit(n, cap=10000):
    word = []
    seen = set()
    while n != 1:
        require(len(word) < cap, "first-hit cap: unresolved")
        require(n not in seen, "nontrivial cycle: unresolved")
        seen.add(n)
        word.append(n & 1)
        n = step(n)
    return {"clock": len(word), "odds": sum(word),
            "kappa": len(word) - 2 * sum(word), "word": word}


def valuation(n, prime):
    count = 0
    while n % prime == 0:
        n //= prime
        count += 1
    return count


def slope_data(a):
    require(a > 0, "positive slope")
    u, v = valuation(a, 2), valuation(a, 3)
    return u, v, a // (2**u * 3**v)


def make_certificate(arms, t0):
    rows = []
    for a, b in arms:
        x = a * t0 + b
        hit = first_hit(x)
        u, v, residual = slope_data(a)
        rows.append((a, b, hit, u, v, residual))
    residuals = {row[5] for row in rows}
    grades = {row[2]["kappa"] - row[3] - 2 * row[4] for row in rows}
    if len(residuals) != 1 or len(grades) != 1:
        return None
    grade = next(iter(grades))
    h = max(0, max(row[2]["clock"] - row[3] for row in rows))
    h += (grade - h) % 2
    Q = (h - grade) // 2
    result = {"parameter": t0, "binary_depth": h,
              "common_residual": next(iter(residuals)),
              "common_exponent": Q, "arms": []}
    for a, b, hit, u, v, residual in rows:
        clock = h + u
        word = hit["word"] + [1, 0] * ((clock - hit["clock"]) // 2)
        result["arms"].append({"a": a, "b": b, "clock": clock,
                               "odd_count": sum(word), "word": word})
    return result


def verify_certificate(cert, lifts=(0, 1, 2, 5)):
    """Reconstruct coefficients and ordinary paths without first-hit metadata."""
    h = cert["binary_depth"]
    t0 = cert["parameter"]
    require(type(h) is int and h >= 0, "nonnegative integer binary depth")
    require(type(t0) is int, "integer parameter")
    q = cert["common_exponent"]
    require(type(q) is int and q >= 0, "nonnegative integer common exponent")
    residual = cert["common_residual"]
    require(type(residual) is int and residual > 0, "positive integer common residual")
    arms = cert["arms"]
    require(isinstance(arms, list) and len(arms) > 0, "nonempty arm list")
    expected_slope = residual * 3**q
    path_edges = 0
    for arm in arms:
        a, b, word = arm["a"], arm["b"], arm["word"]
        require(type(a) is int and a > 0, "positive integer slope")
        require(type(b) is int, "integer offset")
        require(type(arm["clock"]) is int and arm["clock"] >= 0,
                "nonnegative integer clock")
        require(type(arm["odd_count"]) is int and arm["odd_count"] >= 0,
                "nonnegative integer odd count")
        require(isinstance(word, list), "word list")
        require(len(word) == arm["clock"], "clock")
        require(all(type(bit) is int and bit in (0, 1) for bit in word), "binary word")
        require(sum(word) == arm["odd_count"], "odd count")
        coefficient, offset, denominator = 1, 0, 1
        for bit in word:
            if bit:
                coefficient *= 3
                offset = 3 * offset + denominator
            denominator *= 2
        endpoint_at_t0 = Fraction(coefficient * (a * t0 + b) + offset,
                                  denominator)
        lifted_slope = Fraction(coefficient * a * 2**h, denominator)
        require(endpoint_at_t0 == 1, "base endpoint")
        require(lifted_slope == expected_slope, "common lifted slope")
        require(a * 2**h % denominator == 0, "parity cylinder legality")
        for lift in lifts:
            t = t0 + 2**h * lift
            n = a * t + b
            require(n > 0, "positive lift")
            for bit in word:
                require(n % 2 == bit, "physical parity")
                n = step(n)
                path_edges += 1
            require(n == 1 + expected_slope * lift, "physical endpoint")
    return path_edges


def rejection_control(cert, mutate):
    bad = copy.deepcopy(cert)
    mutate(bad)
    try:
        verify_certificate(bad)
    except ValueError:
        return 1
    raise ValueError("corrupt certificate accepted")


def main():
    histogram = Counter()
    count = edges = 0
    for n in range(1, 4097):
        left, right = first_hit(n), first_hit(3 * n)
        delta = right["kappa"] - left["kappa"]
        histogram[delta] += 1
        cert = make_certificate([(1, 0), (3, 0)], n)
        require((cert is not None) == (delta == 2), "three-ray grade criterion")
        if cert is not None:
            edges += verify_certificate(cert)
            count += 1

    powers = []
    same_phase_obstructions = 0
    for r in range(65):
        n = 2**r
        left, right = first_hit(n), first_hit(3 * n)
        require(left["kappa"] == r and right["kappa"] == r + 1,
                "explicit power-of-two obstruction")
        require(make_certificate([(1, 0), (3, 0)], n) is None,
                "obstructed ordinary point")
        powers.append({"r": r, "first_clock": left["clock"],
                       "second_clock": right["clock"]})
        left, right = first_hit(5 * n), first_hit(15 * n)
        require(left["kappa"] == right["kappa"] == r + 2,
                "same-phase triple-ray obstruction")
        require(make_certificate([(1, 0), (3, 0)], 5 * n) is None,
                "same-phase obstructed ordinary point")
        same_phase_obstructions += 1

    generator = random.Random(20261120)
    general_count = general_rejections = 0
    for _ in range(512):
        residual = generator.choice([1, 5, 7])
        arms = [(residual * 2**generator.randrange(4) * 3**generator.randrange(3),
                 generator.randrange(-9, 10))
                for _ in range(generator.randrange(2, 5))]
        t0 = generator.randrange(10, 65)
        cert = make_certificate(arms, t0)
        if cert is None:
            general_rejections += 1
        else:
            edges += verify_certificate(cert)
            general_count += 1

    example = make_certificate([(1, 0), (2, 0), (3, 0)], 15)
    require(example is not None, "mixed-clock example")
    edges += verify_certificate(example)
    require(example["binary_depth"] == 12 and example["common_exponent"] == 5,
            "printed example")
    require([a["clock"] for a in example["arms"]] == [12, 13, 12],
            "mixed clocks")
    shifted = make_certificate([(1, 14), (3, 42)], 1)
    require(shifted is not None, "nonzero-offset example")
    edges += verify_certificate(shifted)

    # All base starts are 1 here, so grades alone agree, while residuals do not.
    require(make_certificate([(1, 0), (5, -4)], 1) is None,
            "incompatible slopes with equal adjusted defects")
    controls = 0
    controls += rejection_control(example, lambda c: c.update(binary_depth=11))
    controls += rejection_control(example, lambda c: c.update(common_exponent=6))
    controls += rejection_control(example, lambda c: c["arms"][0].update(odd_count=6))
    controls += rejection_control(example, lambda c: c["arms"][0]["word"].__setitem__(0, 0))
    controls += rejection_control(example, lambda c: c.update(arms=[]))

    def zero_slope_constant_arms(c):
        c["common_residual"] = 0
        c["arms"] = [{"a": 0, "b": 1, "clock": 0,
                      "odd_count": 0, "word": []}]

    controls += rejection_control(example, zero_slope_constant_arms)

    summary = {
        "status": "PASS",
        "scope": "bounded integer replay of a written local theorem; no universal convergence claim",
        "three_ray_parameters": 4096,
        "three_ray_local_certificates": count,
        "three_ray_convergent_parameters_outside_every_cylinder": 4096 - count,
        "three_ray_defect_difference_histogram": {str(k): v for k, v in sorted(histogram.items())},
        "explicit_power_of_two_parameters": len(powers),
        "explicit_same_phase_obstruction_parameters": same_phase_obstructions,
        "random_affine_lists": 512,
        "random_local_certificates": general_count,
        "random_rejected_local_memberships": general_rejections,
        "literal_lift_path_edges": edges,
        "corrupt_certificate_controls_rejected": controls,
        "mixed_clock_certificate": example,
        "shifted_certificate": shifted,
    }
    canonical = json.dumps(summary, sort_keys=True, separators=(",", ":")).encode()
    summary["payload_sha256_without_this_field"] = hashlib.sha256(canonical).hexdigest()
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
