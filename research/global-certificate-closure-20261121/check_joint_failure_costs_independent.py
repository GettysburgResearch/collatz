#!/usr/bin/env python3
"""Independent critical checks of the sibling directed-five cost theorem.

Does not import the reviewed checker, its ratio helper, its compiler, or
its certificate splicer. Uses the frozen source JSON as the certificate.
"""
import argparse
from fractions import Fraction as F
from functools import reduce
from math import gcd
from pathlib import Path
import hashlib
import json


HERE = Path(__file__).resolve().parent
BASE = HERE if (HERE / "directed_five_certificate.json").exists() else HERE.parent / "agent_global_reverse_20261121"
BUDGET = F(3669265, 2239)
REVERSE = F(2025217, 23)
PINNED_SHA256 = "751523dd92445610a26302947a2f689aecc56a27eaf6fa1f9954eb2e59f5c7c1"


def require(ok, reason):
    if not ok:
        raise RuntimeError(reason)


def T(x):
    require(isinstance(x, int) and x > 0, "ordinary input")
    return (3 * x + 1) // 2 if x % 2 else x // 2


def certify(x):
    path = [x]
    for _ in range(100000):
        if path[-1] == 1:
            return path
        path.append(T(path[-1]))
    raise RuntimeError("finite ordinary replay unresolved")


def verify(path, start):
    require(isinstance(path, list) and path and path[0] == start and path[-1] == 1,
            "ordinary certificate endpoints")
    for x, y in zip(path, path[1:]):
        require(T(x) == y, "ordinary certificate edge")


def normalize(pair):
    require(all(v.denominator == 1 for v in pair), "nonintegral affine family")
    return tuple(v.numerator for v in pair)


def positive_unit(pair):
    slope, value_at_zero = pair
    require(slope > 0 and value_at_zero > 0, "nonpositive all-lift family")
    require(slope % 3 == 0 and value_at_zero % 3, "ternary-unit guard")


def analyze_cover(data):
    words = {w["id"]: w["steps"] for w in data["word_table"]}
    require(len(words) == len(data["word_table"]) == 55, "word table count")
    require(all(sum(step[1].count("5") for step in word) <= 1
                for word in words.values()), "multiple five queries in a word")
    cells = data["cells"]
    require(len(cells) == 464, "cell count")
    common = reduce(lambda x, y: x // gcd(x, y) * y,
                    (cell["modulus"] for cell in cells), 1)
    covered = bytearray(common)
    query_count = 0
    witness = None
    endpoint_max = F(0)
    for cell in cells:
        modulus, residue, lower = cell["modulus"], cell["residue"], cell["min_parameter"]
        require(modulus % 30 == 0 and 0 < residue < modulus and gcd(residue, 30) == 1,
                "cell source guard")
        require(lower == int(residue == 1), "base exclusion")
        for r in range(residue, common, modulus):
            require(covered[r] == 0, "overlapping residue cells")
            covered[r] = 1
        # Write u=lower+t, t>=0. Coefficient and intercept inequalities now
        # directly prove the all-lift bounds without a ratio maximizer helper.
        initial = (modulus, residue + modulus * lower)
        pair = initial
        local_queries = 0
        positive_unit(pair)
        for operation, divisions in words[cell["word"]]:
            a, b = pair
            if operation == "B":
                require(a % 2 == 0 and b % 2 == 1, "odd B input")
                pair = (3 * a, 3 * b + 1)
            else:
                require(operation.startswith("I"), "operation syntax")
                exponent = int(operation[1:])
                require(exponent >= 1, "inverse exponent")
                pair = normalize((F((1 << exponent) * a, 3),
                                  F((1 << exponent) * b - 1, 3)))
                require(pair[0] % 2 == 0 and pair[1] % 2 == 1, "odd inverse output")
            positive_unit(pair)
            for digit in divisions:
                divisor = int(digit)
                require(divisor in (2, 5), "division syntax")
                pair = normalize(tuple(F(v, divisor) for v in pair))
                positive_unit(pair)
                if divisor == 5:
                    local_queries += 1
                    query_count += 1
                    slack = tuple(BUDGET * start - query for start, query in zip(initial, pair))
                    require(all(v >= 0 for v in slack), "all-lift query-budget inequality")
                    if slack[1] == 0:
                        require(pair[0] % 2 == 0 and pair[1] % 2 == 1,
                                "sharp query loses odd normalization")
                        witness = {"source": initial[1], "query": pair[1],
                                   "cell": [modulus, residue, lower], "word": cell["word"]}
        require(local_queries <= 1, "more than one query per cell")
        endpoint = (cell["endpoint"][0], cell["endpoint"][1] + lower * cell["endpoint"][0])
        require(pair == endpoint, "endpoint identity")
        contraction = tuple(19 * start - 20 * end for start, end in zip(initial, pair))
        require(all(v >= 0 for v in contraction), "all-lift 19/20 contraction")
        endpoint_max = max(endpoint_max, F(pair[0], initial[0]), F(pair[1], initial[1]))
    require(common == 1866240, "cover modulus")
    require(sum(covered) == 497664, "covered unit residues")
    require(all(bool(covered[r]) == (gcd(r, 30) == 1) for r in range(common)),
            "incomplete residue partition")
    require(query_count == 219, "query appearance count")
    require(witness == {"source": 2239, "query": 3669265,
                        "cell": [8640, 2239, 0], "word": "W17"}, "sharp witness")
    require(endpoint_max == F(13403, 14119), "endpoint maximum")
    return words, {"cells": len(cells), "words": len(words), "common_modulus": common,
                   "covered_residues": sum(covered), "query_appearances": query_count,
                   "all_lift_query_budget": str(BUDGET), "sharp_witness": witness,
                   "endpoint_maximum": str(endpoint_max)}


def descend(n, data, words):
    require(n > 0 and n % 3, "descent unit domain")
    if n % 2 == 0:
        return n // 2, [("2", n, n // 2)]
    if n % 5 == 0:
        return n // 5, [("5", n, n // 5)]
    matches = [c for c in data["cells"] if n % c["modulus"] == c["residue"]
               and (n - c["residue"]) // c["modulus"] >= c["min_parameter"]]
    require(len(matches) == 1, "unique numeric cell")
    cell = matches[0]
    value, edges = n, []
    for op, digits in words[cell["word"]]:
        previous = value
        if op == "B":
            require(value % 2, "numeric B input")
            value = 3 * value + 1
            require(T(previous) == T(value), "B common successor")
        else:
            exponent = int(op[1:])
            numerator = (value << exponent) - 1
            require(numerator % 3 == 0, "numeric inverse guard")
            value = numerator // 3
            clock_value = value
            for _ in range(exponent):
                clock_value = T(clock_value)
            require(clock_value == previous, "ordinary inverse clock")
        edges.append((op, previous, value))
        for d in digits:
            previous = value
            require(value % int(d) == 0, "numeric division guard")
            value //= int(d)
            edges.append((d, previous, value))
    require(20 * value <= 19 * n and 0 < value < n and value % 3,
            "numeric strict descent")
    return value, edges


def splice(edges, proof, calls):
    for kind, source, endpoint in reversed(edges):
        verify(proof, endpoint)
        if kind == "2":
            require(T(source) == endpoint, "halving direction")
            proof = [source] + proof
        elif kind == "B":
            require(len(proof) > 1 and T(source) == proof[1], "B splice")
            proof = [source] + proof[1:]
        elif kind.startswith("I"):
            clock = int(kind[1:])
            while len(proof) <= clock:
                proof = proof + [T(proof[-1])]
            require(proof[clock] == source, "inverse splice clock")
            proof = proof[clock:]
            if proof[-1] == 2:
                proof += [1]
        elif kind == "5":
            value, halvings = endpoint, 0
            while value % 2 == 0:
                value //= 2
                halvings += 1
            antecedent_proof = proof[halvings:]
            verify(antecedent_proof, value)
            target_proof = certify(5 * value)
            verify(target_proof, 5 * value)
            prefix = [source]
            for _ in range(halvings):
                prefix.append(T(prefix[-1]))
            require(prefix[-1] == 5 * value, "five normalization direction")
            calls.append({"antecedent": value, "antecedent_certificate_length": len(antecedent_proof)})
            proof = prefix[:-1] + target_proof
        else:
            raise RuntimeError("unknown splice operation")
        verify(proof, source)
    return proof


def execute_control(n, data, words):
    value, levels = n, []
    while value > 1:
        endpoint, edges = descend(value, data, words)
        require(20 * endpoint <= 19 * value, "level contraction")
        levels.append((value, endpoint, edges))
        value = endpoint
    require(n * 19 ** len(levels) >= 20 ** len(levels),
            "exact integer equivalent of level logarithmic bound")
    proof, calls = [1], []
    for source, endpoint, edges in reversed(levels):
        verify(proof, endpoint)
        prior = len(calls)
        proof = splice(edges, proof, calls)
        verify(proof, source)
        require(len(calls) - prior <= 1, "multiple level calls")
    require(all(call["antecedent"] <= BUDGET * n for call in calls), "global query bound")
    verify(proof, n)
    return {"source": n, "levels": len(levels), "queries": len(calls),
            "ordinary_clocks": len(proof) - 1,
            "largest_query": max([0] + [call["antecedent"] for call in calls])}


def main():
    global BASE
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=BASE)
    parser.add_argument("--output", type=Path,
                        default=HERE / "joint-failure-independent-review-report.json")
    args = parser.parse_args()
    BASE = args.source_dir
    raw = (BASE / "directed_five_certificate.json").read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PINNED_SHA256, "frozen certificate hash")
    data = json.loads(raw)
    words, cover = analyze_cover(data)
    # Critical splice clocks beyond the supplied first arrival at one.
    require(splice([("I2", 1, 1)], [1], []) == [1], "padding to one")
    require(splice([("I1", 2, 1)], [1], []) == [2, 1], "padding to two")
    cases = [execute_control(n, data, words) for n in
             (1, 2, 5, 7, 23, 95, 239, 2239, 5119, 7999, 14119, 299239, 1000001)]
    require(5 * REVERSE / 4 > 1 and 5 * REVERSE / 13 > 1, "joint budget product")
    # Literal six-clock identity on eligible sample indices is an additional
    # implementation control; the affine identity is proved in the review.
    for k in (1, 2, 3, 5, 11, 12345):
        value = 64 * k + 1
        for _ in range(6):
            value = T(value)
        require(value == 27 * k + 1, "reverse lower unit endpoint")
    report = {
        "status": "PASS; scoped independent review, no global closure",
        "reviewed_files": {
            name: hashlib.sha256((BASE / name).read_bytes()).hexdigest()
            for name in ("JOINT_FAILURE_CERTIFICATE_COSTS.md", "check_joint_failure_costs.py")
        },
        "frozen_certificate_sha256": PINNED_SHA256,
        "all_lift_cover": cover,
        "independent_conditional_program_replays": cases,
        "inverse_cycle_padding_controls": ["I2(1)=1", "I1(2)=1"],
        "generic_return_cost": str(5 * REVERSE),
        "old_forward_interface_budget_product": str(5 * REVERSE / 4),
        "new_thirteen_interface_budget_product": str(5 * REVERSE / 13),
        "conditional_queries_proved_universally": False,
    }
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(json.dumps({"status": report["status"], "cells": cover["cells"],
                      "query_appearances": cover["query_appearances"],
                      "sharp_witness": cover["sharp_witness"],
                      "execution_controls": len(cases),
                      "report_sha256": hashlib.sha256(encoded.encode()).hexdigest()},
                     sort_keys=True))


if __name__ == "__main__":
    main()
