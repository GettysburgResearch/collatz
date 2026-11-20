"""Propose, then exactly certify, a small positive cap-six inverse policy.

NumPy solves the finite policy-iteration equations only to propose labels
and a rational bias.  The exported certificate is checked with integers.
It certifies stationary mean cost for the locally Haar finite matrix;
it is not a pointwise robust inverse-credit certificate.
"""

import argparse
from fractions import Fraction
import json
from pathlib import Path

import numpy as np


def propose(digits=5, limit=100):
    modulus = 3**digits
    states = [r for r in range(1, modulus) if r % 3]
    index = {r: i for i, r in enumerate(states)}
    observed = [r for r in range(1, 3 * modulus) if r % 3]
    rows = {}
    for residue in observed:
        edges = []
        for exponent in range(1, 7):
            numerator = (1 << exponent) * residue - 1
            if numerator % 3 == 0 and (numerator // 3) % 3:
                edges.append((exponent, index[(numerator // 3) % modulus]))
        assert len(edges) == 2
        rows[residue] = edges
    selected = {residue: 0 for residue in observed}
    size = len(states)
    for iteration in range(1, limit + 1):
        matrix = np.zeros((size, size), dtype=float)
        costs = np.zeros(size, dtype=float)
        for i, residue in enumerate(states):
            for digit in range(3):
                source = residue + digit * modulus
                chosen = selected[source]
                for j, (exponent, child) in enumerate(rows[source]):
                    weight = (99 if j == chosen else 1) / 300
                    matrix[i, child] += weight
                    costs[i] += weight * exponent
        linear = np.zeros((size + 1, size + 1))
        linear[:size, :size] = np.eye(size) - matrix
        linear[:size, size] = 1
        linear[size, 0] = 1
        rhs = np.append(costs, 0)
        solution = np.linalg.solve(linear, rhs)
        bias, mean = solution[:size], solution[size]
        changes = 0
        for residue in observed:
            scores = [exponent + bias[child] for exponent, child in rows[residue]]
            best = int(scores[1] < scores[0] - 1e-10)
            if best != selected[residue]:
                selected[residue] = best
                changes += 1
        if changes == 0:
            break
    else:
        raise RuntimeError("Policy iteration did not stabilize")
    denominator = 10**9
    return {
        "format": 1,
        "cap": 6,
        "cell_digits": digits,
        "observed_digits": digits + 1,
        "preferred_probability_numerator": 99,
        "probability_denominator": 100,
        "bias_denominator": denominator,
        "labels": [rows[r][selected[r]][0] for r in observed],
        "bias_numerators": [int(round(value * denominator)) for value in bias],
        "proposal_iterations": iteration,
        "proposal_floating_mean": float(mean),
    }


def verify(certificate):
    assert certificate["cap"] == 6
    digits = certificate["cell_digits"]
    modulus = 3**digits
    states = [r for r in range(1, modulus) if r % 3]
    observed = [r for r in range(1, 3 * modulus) if r % 3]
    labels = certificate["labels"]
    bias = certificate["bias_numerators"]
    denominator = certificate["bias_denominator"]
    assert len(labels) == len(observed) and len(bias) == len(states)
    assert all(type(x) is int for x in labels + bias)
    assert denominator > 0
    lookup = dict(zip(observed, labels))
    bias_lookup = dict(zip(states, bias))
    numerators = []
    for residue in states:
        numerator = -300 * bias_lookup[residue]
        for digit in range(3):
            source = residue + digit * modulus
            legal = []
            for exponent in range(1, 7):
                top = (1 << exponent) * source - 1
                if top % 3 == 0 and (top // 3) % 3:
                    legal.append((exponent, (top // 3) % modulus))
            assert len(legal) == 2
            assert lookup[source] in [edge[0] for edge in legal]
            for exponent, child in legal:
                weight = 99 if lookup[source] == exponent else 1
                numerator += weight * (exponent * denominator + bias_lookup[child])
        assert 1000 * numerator > 1937 * 300 * denominator
        assert 500 * numerator < 969 * 300 * denominator
        numerators.append(numerator)
    return {
        "status": "PASS",
        "policy_rows": len(observed),
        "stationary_cells": len(states),
        "minimum_bias_expression": str(Fraction(min(numerators), 300 * denominator)),
        "maximum_bias_expression": str(Fraction(max(numerators), 300 * denominator)),
        "certified_stationary_mean_lower": "1937/1000",
        "certified_stationary_mean_upper": "969/500",
        "minimum_integer_upper_margin": 39 * 300 * denominator - 20 * max(numerators),
    }


def main():
    if not __debug__:
        raise RuntimeError("This optional producer requires assertions; omit -O.")
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--digits", type=int, default=5)
    args = parser.parse_args()
    certificate = propose(args.digits)
    report = verify(certificate)
    iterations = certificate.pop("proposal_iterations")
    floating_mean = certificate.pop("proposal_floating_mean")
    args.out.write_text(json.dumps(certificate, separators=(",", ":")) + "\n")
    print(json.dumps(dict(report, proposal_iterations=iterations,
                          proposal_floating_mean=floating_mean), indent=2))


if __name__ == "__main__":
    main()
