#!/usr/bin/env python3
"""Check an exact positive inverse-policy stationary-cost certificate.

Only Python's standard library is used.  This certifies the finite matrix
and its rational drift inequality, not uniqueness among all 3-adic laws,
uniform convergence, or a pointwise robust inverse-credit inequality.
"""

from collections import Counter
from fractions import Fraction
import argparse
import hashlib
import json
from pathlib import Path


def require(condition, explanation):
    if not condition:
        raise ValueError(explanation)


def check(certificate):
    expected = {
        "format": 1,
        "cap": 6,
        "cell_digits": 5,
        "observed_digits": 6,
        "preferred_probability_numerator": 99,
        "probability_denominator": 100,
        "bias_denominator": 10**9,
    }
    for key, value in expected.items():
        require(type(certificate.get(key)) is int and certificate[key] == value,
                f"Invalid certificate field {key}")
    labels = certificate.get("labels")
    biases = certificate.get("bias_numerators")
    require(isinstance(labels, list) and len(labels) == 486, "Wrong label count")
    require(isinstance(biases, list) and len(biases) == 162, "Wrong bias count")
    require(all(type(x) is int for x in labels + biases), "Noninteger certificate entry")

    cells = [n for n in range(1, 243) if n % 3]
    phases = [n for n in range(1, 729) if n % 3]
    cell_index = {n: i for i, n in enumerate(cells)}
    preferred = dict(zip(phases, labels))
    denominator = expected["bias_denominator"]
    drift_numerators = []
    transitions = []
    for i, cell in enumerate(cells):
        row = Counter()
        cost_numerator = 0
        for digit in (0, 1, 2):
            phase = cell + 243 * digit
            legal = []
            for exponent in range(1, 7):
                numerator = (2**exponent) * phase - 1
                if numerator % 3 == 0:
                    child = numerator // 3
                    if child % 3:
                        require(child > 0, "Nonpositive ordinary representative")
                        legal.append((exponent, child % 243))
            require(len(legal) == 2, "Unexpected cap-six legal degree")
            require(preferred[phase] in [e for e, _ in legal],
                    f"Illegal designated exponent at phase {phase}")
            for exponent, child in legal:
                weight = 99 if exponent == preferred[phase] else 1
                row[cell_index[child]] += weight
                cost_numerator += weight * exponent
        require(sum(row.values()) == 300, "Nonstochastic finite matrix row")
        numerator = denominator * cost_numerator - 300 * biases[i]
        numerator += sum(weight * biases[j] for j, weight in row.items())
        require(1000 * numerator > 1937 * 300 * denominator,
                f"Lower drift bound failed at cell {cell}")
        require(500 * numerator < 969 * 300 * denominator,
                f"Upper drift bound failed at cell {cell}")
        drift_numerators.append(numerator)
        transitions.append(row)

    # Exact support computation for K^5, without floating matrix powers.
    complete = set(range(162))
    for initial in range(162):
        reached = {initial}
        for _ in range(5):
            reached = {child for source in reached for child in transitions[source]}
        require(reached == complete, f"Fifth matrix power has a zero in row {initial}")

    total_denominator = 300 * denominator
    return {
        "status": "PASS",
        "policy_rows": 486,
        "stationary_cells": 162,
        "matrix_denominator": 300,
        "positive_fifth_matrix_power": True,
        "minimum_bias_expression": str(Fraction(min(drift_numerators), total_denominator)),
        "maximum_bias_expression": str(Fraction(max(drift_numerators), total_denominator)),
        "strict_stationary_mean_lower": "1937/1000",
        "strict_stationary_mean_upper": "969/500",
        "minimum_integer_lower_margin": min(1000 * n - 1937 * total_denominator
                                            for n in drift_numerators),
        "minimum_integer_upper_margin": min(969 * total_denominator - 500 * n
                                            for n in drift_numerators),
        "scope": "Finite locally Haar stationary-cost certificate only",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", type=Path,
                        default=Path(__file__).with_name("small_positive_policy.json"))
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    certificate = json.loads(raw)
    result = check(certificate)
    result["certificate_sha256"] = hashlib.sha256(raw).hexdigest()

    for name, changed in (
        ("zero_bias", dict(certificate, bias_numerators=[0] * 162)),
        ("zero_labels", dict(certificate, labels=[0] * 486)),
    ):
        try:
            check(changed)
        except ValueError as error:
            result[name + "_mutation_rejected"] = str(error)
        else:
            raise ValueError(f"Mutation unexpectedly accepted: {name}")

    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(output, end="")
    if args.report:
        args.report.write_text(output)


if __name__ == "__main__":
    main()
