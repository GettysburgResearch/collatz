#!/usr/bin/env python3
"""Exact finite evidence for analytic_flow.md; not a proof of Collatz.

All complex arithmetic is over Q(i). Every residual includes all image
coordinates, and every retained macro edge is replayed in shortcut time.
The infinite eigenvectors are justified by the manuscript's geometric tail.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import random


ZERO = (F(0), F(0))
ONE = (F(1), F(0))
COUNTS = defaultdict(int)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def scale(a, q):
    return a[0] * q, a[1] * q


def power(a, n):
    out = ONE
    for _ in range(n):
        out = mul(out, a)
    return out


def abs2(a):
    return a[0] ** 2 + a[1] ** 2


def clean(vector):
    return {n: a for n, a in vector.items() if a != ZERO}


def accumulate(vector, n, value):
    vector[n] = add(vector.get(n, ZERO), value)


def norm2(vector):
    return sum((abs2(a) for a in vector.values()), F(0))


def shortcut(n):
    require(n > 0, "positive source required")
    return (3 * n + 1) // 2 if n & 1 else n // 2


def children(p):
    require(p > 1 and p & 1 and p % 3, "odd unit parent above one required")
    exponents = (2, 4, 6) if p % 3 == 1 else (3, 5, 7)
    out = []
    for j in exponents:
        numerator = (p << j) - 1
        require(numerator % 3 == 0, "nonintegral child")
        n = numerator // 3
        if n % 3:
            require(n > p and n & 1, "child must be larger and odd")
            out.append((j, n))
    require(len(out) == 2, "exactly two retained unit children required")
    return out


def replay(child, parent, j):
    current = child
    for step in range(j):
        require((current & 1) == (step == 0), "physical parity mismatch")
        current = shortcut(current)
        COUNTS["physical_shortcut_edges"] += 1
    require(current == parent, "physical endpoint mismatch")


def q_apply(vector):
    result = {}
    for n, a in vector.items():
        accumulate(result, shortcut(n), a)
    return clean(result)


def p_apply(vector):
    result = {}
    for n, a in vector.items():
        accumulate(result, 2 * n, a)
        if n % 3 == 2:
            accumulate(result, (2 * n - 1) // 3, a)
    return clean(result)


def difference(left, right):
    result = dict(left)
    for n, a in right.items():
        accumulate(result, n, scale(a, -1))
    return clean(result)


def verify_residual(vector, leaves, eigenvalue):
    actual = difference(q_apply(vector), {n: mul(eigenvalue, a) for n, a in vector.items()})
    expected = clean({n: scale(mul(eigenvalue, a), -1) for n, a in leaves.items()})
    require(actual == expected, "unaccounted interior or exterior residual coordinate")
    return actual


def build(root, depth, eigenvalue):
    require(depth >= 1 and eigenvalue != ZERO, "nonzero eigenvalue and positive depth required")
    vector = {}
    frontier = [(root, ZERO)]
    seen = {root}
    generation_squares = []
    edge_count = 0
    for generation in range(1, depth + 1):
        next_frontier = []
        for parent, weight in frontier:
            for branch, (j, child) in enumerate(children(parent)):
                require(child not in seen, "selected inverse tree collided")
                seen.add(child)
                replay(child, parent, j)
                edge_count += 1
                base = scale(ONE, 1 if branch == 0 else -1) if generation == 1 else scale(weight, F(1, 2))
                child_weight = mul(power(eigenvalue, j), base)
                accumulate(vector, child, child_weight)
                for k in range(1, j):
                    accumulate(vector, parent << k, mul(power(eigenvalue, k), base))
                next_frontier.append((child, child_weight))
        frontier = next_frontier
        generation_squares.append(sum((abs2(a) for _, a in frontier), F(0)))
    vector = clean(vector)
    leaves = dict(frontier)
    residual = verify_residual(vector, leaves, eigenvalue)
    COUNTS["macro_edges"] += edge_count
    COUNTS["residual_coordinates_examined"] += len(set(vector) | set(q_apply(vector)))
    r2 = abs2(eigenvalue)
    ratio = max(r2 ** 2, r2 ** 7) / 2
    require(ratio < 1, "outside proved geometric disk")
    require(generation_squares[0] <= 4 * ratio, "first generation energy bound")
    for previous, following in zip(generation_squares, generation_squares[1:]):
        require(following <= ratio * previous, "geometric generation bound")
    even_constant = sum((r2 ** k for k in range(1, 7)), F(0))
    tail_bound = generation_squares[-1] * (even_constant + ratio) / (1 - ratio)
    if eigenvalue == ONE:
        require(norm2(vector) <= 32, "stationary full energy envelope")
        require(norm2(residual) == F(4, 2 ** depth), "exact stationary residual energy")
        require(sum(abs(a[0]) for a in residual.values()) == 2, "stationary residual absolute mass")
        require(sum(abs(a[0]) for _, a in frontier) == 2, "stationary leaf absolute mass")
        require(generation_squares == [F(4, 2 ** d) for d in range(1, depth + 1)], "stationary generation formula")
    return vector, leaves, {
        "root": root,
        "depth": depth,
        "eigenvalue": [str(x) for x in eigenvalue],
        "odd_nodes": len(seen) - 1,
        "nonzero_physical_coordinates": len(vector),
        "macro_edges": edge_count,
        "maximum_integer_bits": max(vector).bit_length(),
        "norm_squared": str(norm2(vector)),
        "residual_norm_squared": str(norm2(residual)),
        "generation_square_bound_ratio": str(ratio),
        "certified_omitted_square_tail_upper": str(tail_bound),
        "leaf_count": len(leaves),
    }


def digest_vector(vector):
    payload = [[n, str(a[0]), str(a[1])] for n, a in sorted(vector.items())]
    return sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()


def run():
    COUNTS.clear()
    records = []
    for depth in range(1, 13):
        vector, leaves, row = build(5, depth, ONE)
        row["vector_sha256"] = digest_vector(vector)
        records.append(row)
    for eigenvalue, depth in (((F(1, 2), F(0)), 7), ((F(-1), F(0)), 7),
                             ((F(0), F(1)), 7), ((F(3, 5), F(4, 5)), 6),
                             ((F(21, 20), F(0)), 8)):
        vector, leaves, row = build(5, depth, eigenvalue)
        row["vector_sha256"] = digest_vector(vector)
        records.append(row)

    antichain = []
    stem = 5
    occupied = set()
    antichain_records = []
    for _ in range(8):
        choices = children(stem)
        root = choices[1][1]
        antichain.append(root)
        vector, _, row = build(root, 5, ONE)
        require(not occupied.intersection(vector), "antichain supports overlap")
        occupied.update(vector)
        row["vector_sha256"] = digest_vector(vector)
        antichain_records.append(row)
        stem = choices[0][1]
    COUNTS["antichain_disjoint_pairs"] = len(antichain) * (len(antichain) - 1) // 2

    kernel_sources = set()
    for k in range(1, 65):
        target = 1 << (2 * k + 1)
        vector = {2 * target: ONE, (2 * target - 1) // 3: scale(ONE, -1)}
        require(not kernel_sources.intersection(vector), "zero-eigenvalue pair collision")
        kernel_sources.update(vector)
        require(not q_apply(vector), "collision vector is not in kernel")
        COUNTS["zero_eigenvalue_pairs"] += 1

    triangular = []
    for h in range(1, 41):
        coefficients = list(range(1, h + 1)) + list(range(h - 1, 0, -1))
        vector = {3 << j: scale(ONE, c) for j, c in enumerate(coefficients)}
        residual = difference(vector, p_apply(vector))
        require(norm2(vector) == F(2 * h ** 3 + h, 3), "triangular energy")
        require(norm2(residual) == 2 * h, "triangular residual")
        require(norm2(residual) / norm2(vector) == F(6, 2 * h * h + 1), "triangular ratio")
        triangular.append({"h": h, "degree_bits": max(vector).bit_length(),
                           "norm_squared": str(norm2(vector)), "residual_squared": str(norm2(residual))})

    rng = random.Random(20261120)
    for degree in list(range(1, 130)) + [255, 256, 257, 511, 1024]:
        for _ in range(4):
            vector = clean({n: (F(rng.randint(-3, 3)), F(rng.randint(-3, 3))) for n in range(1, degree + 1)})
            residual = difference(vector, p_apply(vector))
            length = degree.bit_length()
            require(2 * norm2(vector) <= length * (length + 1) * norm2(residual), "finite coercivity")
            COUNTS["finite_coercivity_cases"] += 1

    rejected = []
    vector, leaves, _ = build(5, 5, ONE)
    for name, changed in (
        ("interior_weight", dict(vector)),
        ("missing_leaf", dict(vector)),
        ("outside_support", dict(vector)),
        ("root_leakage", dict(vector)),
    ):
        if name == "interior_weight":
            n = next(n for n in changed if n % 2 == 0)
            changed[n] = add(changed[n], (F(1, 7), F(0)))
        elif name == "missing_leaf":
            changed.pop(next(iter(leaves)))
        elif name == "outside_support":
            changed[3] = ONE
        else:
            changed[5] = ONE
        try:
            verify_residual(clean(changed), leaves, ONE)
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError("damaged flow accepted: " + name)
    positive_edge_count = COUNTS["physical_shortcut_edges"]
    try:
        replay(13, 5, 4)
    except ValueError:
        rejected.append("wrong_physical_clock")
    else:
        raise ValueError("wrong physical clock accepted")
    COUNTS["negative_control_physical_prefix_edges"] = COUNTS["physical_shortcut_edges"] - positive_edge_count
    COUNTS["physical_shortcut_edges"] = positive_edge_count
    return {
        "schema": "collatz-creative-analytic-flow/v1",
        "status": "PASS",
        "scope": "exact finite rational-complex flow, physical clock and complete residual checks; infinite claims use written geometric-tail proofs",
        "operator": "unweighted Hardy Q e_n=e_T(n), P=Q* on positive integer coefficients",
        "flow_cases": records,
        "antichain_roots": antichain,
        "antichain_cases": antichain_records,
        "triangular_cases": triangular,
        "counts": dict(sorted(COUNTS.items())),
        "negative_controls_rejected": rejected,
        "limitations": [
            "No Collatz proof, no new positive cycle, and no divergent ordinary source.",
            "All eigenvector supports are constructively in the known basin of one.",
            "Finite evidence does not by itself certify the infinite eigenspace or geometric tail.",
            "The stated spectral disk is a sufficient inclusion, not a sharp spectral radius."
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--compare", type=Path)
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        require(not args.output.exists(), "refusing to overwrite report")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    elif args.compare:
        require(json.loads(args.compare.read_text(encoding="utf-8")) == result, "frozen report mismatch")
    print(json.dumps({"status": "PASS", "flow_cases": len(result["flow_cases"]),
                      "antichain_cases": len(result["antichain_cases"]),
                      "counts": result["counts"], "negative_controls": len(result["negative_controls_rejected"]),
                      "report_sha256": sha256(rendered.encode()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
