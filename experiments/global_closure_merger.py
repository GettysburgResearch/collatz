#!/usr/bin/env python3
"""Check all-lift directed descent from ordinary edges and forward five.

This proves a conditional rigidity certificate. It does not prove that the
ordinary basin of 1 is closed under multiplication by five. No orbit census
or finite search is used to certify an unbounded residue cell.
"""

from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction
import hashlib
import json
from math import gcd, lcm
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = ROOT / "reports/2026-11-20-global-closure/merger-certificate.json"
CERTIFICATE_SHA256 = "751523dd92445610a26302947a2f689aecc56a27eaf6fa1f9954eb2e59f5c7c1"
SCHEMA = "collatz-directed-five-unit-descent-v1"


class CertificateError(ValueError):
    """An exact guard, identity, coverage condition, or decrease failed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CertificateError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unit(a: int, b: int, minimum: int) -> None:
    require(a > 0 and a * minimum + b > 0, "nonpositive affine value")
    require(a % 3 == 0 and b % 3 != 0, "not a ternary unit on the entire cell")


def step(a: int, b: int, operation: str, divisions: str, minimum: int):
    """Return exact new coefficients and a count of augmented graph edges.

    The semantic direction is always S(new) => S(old). B and Ij are ordinary
    component equivalences; /2 is an ordinary equivalence; /5 is the reverse
    use of the ASSUMED implication S(x) => S(5*x).
    """
    unit(a, b, minimum)
    if operation == "B":
        require(a % 2 == 0 and b % 2 == 1, "B input is not always odd")
        a, b = 3 * a, 3 * b + 1
        cost = 2
    else:
        require(re.fullmatch(r"I[1-9][0-9]*", operation) is not None,
                "unknown or incorrectly directed primitive")
        exponent = int(operation[1:])
        require(exponent <= 64, "unreasonably large certificate exponent")
        numerator_a, numerator_b = (1 << exponent) * a, (1 << exponent) * b - 1
        require(numerator_a % 3 == 0 and numerator_b % 3 == 0,
                "inverse odd step is not integral")
        a, b = numerator_a // 3, numerator_b // 3
        require(a % 2 == 0 and b % 2 == 1, "inverse odd source is not always odd")
        # In particular, this forbids silently treating division by three as
        # ordinary component invariance.
        unit(a, b, minimum)
        cost = exponent
    unit(a, b, minimum)
    for digit in divisions:
        require(digit in "25", "division by an unlicensed factor")
        divisor = int(digit)
        require(a % divisor == 0 and b % divisor == 0,
                "division is not exact on the entire cell")
        a, b = a // divisor, b // divisor
        unit(a, b, minimum)
        cost += 1
    return a, b, cost


def validate(packet: dict) -> dict:
    require(packet["schema"] == SCHEMA, "unrecognized certificate schema")
    words = {entry["id"]: entry["steps"] for entry in packet["word_table"]}
    require(len(words) == len(packet["word_table"]), "duplicate word identifier")
    cells = packet["cells"]
    require(bool(cells), "empty certificate")
    common_modulus = lcm(*(cell["modulus"] for cell in cells))
    require(common_modulus <= 10_000_000, "unexpected certificate cover size")
    covered = bytearray(common_modulus)
    modulus_counts: Counter[int] = Counter()
    operation_counts: Counter[str] = Counter()
    division_counts: Counter[str] = Counter()
    maximum_cost = maximum_word_length = maximum_fives = 0
    maximum_ratio = Fraction(0)
    minimum_gap = None
    total_steps = cells_with_five = 0
    bounded_replays = 0
    used_words = set()

    for cell in cells:
        modulus, residue, minimum = (cell[k] for k in ("modulus", "residue", "min_parameter"))
        require(all(type(x) is int for x in (modulus, residue, minimum)), "noninteger cell")
        require(modulus > 0 and modulus % 30 == 0, "cell modulus must be positive and divisible by 30")
        require(0 < residue < modulus and gcd(residue, 30) == 1, "cell is not a reduced residue")
        require(minimum == (1 if (modulus, residue) == (1440, 1) else 0),
                "unexplained finite exceptions to a cell")
        require(cell["word"] in words, "unknown word identifier")
        used_words.add(cell["word"])
        path = words[cell["word"]]
        a, b, cost, fives = modulus, residue, 0, 0
        for operation, divisions in path:
            a, b, added_cost = step(a, b, operation, divisions, minimum)
            cost += added_cost
            operation_counts[operation] += 1
            division_counts.update(divisions)
            fives += divisions.count("5")
        require([a, b] == cell["endpoint"], "advertised endpoint is wrong")
        gap_slope, gap_at_minimum = modulus - a, (modulus - a) * minimum + residue - b
        require(gap_slope >= 0 and gap_at_minimum > 0, "terminal value does not strictly decrease")
        # This is an exact coefficientwise check of q <= 19*n/20, for every
        # unrestricted integer parameter u >= minimum, not sample evidence.
        require(19 * modulus - 20 * a >= 0 and
                (19 * modulus - 20 * a) * minimum + 19 * residue - 20 * b >= 0,
                "uniform 19/20 decrease failed")
        ratio = max(Fraction(a, modulus),
                    Fraction(a * minimum + b, modulus * minimum + residue))
        maximum_ratio = max(maximum_ratio, ratio)
        minimum_gap = gap_at_minimum if minimum_gap is None else min(minimum_gap, gap_at_minimum)
        maximum_cost = max(maximum_cost, cost)
        maximum_word_length = max(maximum_word_length, len(path))
        maximum_fives = max(maximum_fives, fives)
        cells_with_five += bool(fives)
        total_steps += len(path)
        modulus_counts[modulus] += 1
        for r in range(residue, common_modulus, modulus):
            require(covered[r] == 0, "overlapping residue cells")
            covered[r] = 1

        # Separate, explicitly bounded, ordinary-clock sanity checks. The
        # preceding symbolic checks carry the all-lift proof.
        for u in (minimum, minimum + 1, minimum + 2, minimum + 17):
            value = modulus * u + residue
            for operation, divisions in path:
                old = value
                if operation == "B":
                    require(old % 2 == 1, "concrete B parity failure")
                    value = 3 * old + 1
                    require(shortcut(old) == shortcut(value), "concrete B ordinary meeting failed")
                else:
                    exponent = int(operation[1:])
                    value = ((1 << exponent) * old - 1) // 3
                    orbit_value = value
                    for _ in range(exponent):
                        orbit_value = shortcut(orbit_value)
                    require(orbit_value == old, "concrete inverse ordinary clock failed")
                for digit in divisions:
                    require(value % int(digit) == 0, "concrete division failed")
                    value //= int(digit)
                require(value > 0 and value % 3 != 0, "concrete ternary-unit domain failed")
            require(value == a * u + b < modulus * u + residue, "concrete endpoint or decrease failed")
            bounded_replays += 1

    require(used_words == set(words), "unused or missing word table entry")
    expected_count = 0
    for residue, is_covered in enumerate(covered):
        expected = gcd(residue, 30) == 1
        require(bool(is_covered) == expected, "incomplete or overextended residue cover")
        expected_count += expected
    return {
        "cells": len(cells),
        "distinct_words": len(words),
        "modulus_cell_counts": {str(k): v for k, v in sorted(modulus_counts.items())},
        "common_cover_modulus": common_modulus,
        "covered_reduced_residues": expected_count,
        "ordinary_base_exception": 1,
        "conditional_division_factors": [5],
        "division_by_three_used": False,
        "operation_counts": dict(sorted(operation_counts.items())),
        "division_counts": dict(sorted(division_counts.items())),
        "affine_steps": total_steps,
        "maximum_word_length": maximum_word_length,
        "maximum_augmented_edge_cost": maximum_cost,
        "maximum_five_uses_per_cell": maximum_fives,
        "cells_using_five": cells_with_five,
        "maximum_endpoint_source_ratio": [maximum_ratio.numerator, maximum_ratio.denominator],
        "uniform_decrease_bound": [19, 20],
        "minimum_integer_decrease": minimum_gap,
        "bounded_concrete_replays": bounded_replays,
        "all_lift_scope": "Exact affine guards, identities, positivity, ternary-unit preservation, strict descent, and complete residue cover.",
        "excluded_claim": "No physical forward-five closure or ordinary stopping-time bound was proved.",
    }


def shortcut(value: int) -> int:
    return value // 2 if value % 2 == 0 else (3 * value + 1) // 2


def negative_controls(packet: dict) -> list[str]:
    passed = []

    def rejected(name, action):
        try:
            action()
        except CertificateError:
            passed.append(name)
        else:
            raise CertificateError(f"negative control was accepted: {name}")

    rejected("B must have odd inputs on the whole cell", lambda: step(30, 2, "B", "", 0))
    rejected("inverse odd source must be integral", lambda: step(30, 1, "I1", "", 0))
    rejected("inverse source may not become divisible by three", lambda: step(90, 14, "I1", "", 0))
    rejected("multiplication by five is not a reverse proof primitive", lambda: step(30, 1, "M5", "", 0))
    rejected("division by three is unlicensed", lambda: step(30, 1, "B", "3", 0))
    rejected("division must hold for every lift", lambda: step(30, 1, "B", "5", 0))

    missing = deepcopy(packet)
    missing["cells"].pop()
    rejected("a missing infinite residue cell is rejected", lambda: validate(missing))
    wrong_endpoint = deepcopy(packet)
    wrong_endpoint["cells"][1]["endpoint"][1] += 1
    rejected("a false terminal affine identity is rejected", lambda: validate(wrong_endpoint))
    no_descent = deepcopy(packet)
    c = no_descent["cells"][1]
    no_descent["word_table"].append({"id": "NONDECREASING", "steps": []})
    c["word"] = "NONDECREASING"
    c["endpoint"] = [c["modulus"], c["residue"]]
    rejected("a legal but nondecreasing path is rejected", lambda: validate(no_descent))
    return passed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, default=CERTIFICATE)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path, help="create a new evidence file; never overwrite")
    group.add_argument("--compare", type=Path, help="compare exact regenerated evidence with a frozen report")
    args = parser.parse_args()
    require(sha256(args.certificate) == CERTIFICATE_SHA256, "certificate differs from the frozen source")
    packet = json.loads(args.certificate.read_text(encoding="utf-8"))
    report = {
        "schema": "collatz-global-closure-merger-report-v1",
        "status": "PASS: exact conditional unit descent; physical basin closure remains OPEN",
        "certificate_sha256": sha256(args.certificate),
        "checker_sha256": sha256(Path(__file__)),
        "results": validate(packet),
        "negative_controls_rejected": negative_controls(packet),
    }
    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(serialized)
        print(f"PASS: wrote new report {args.output}")
    elif args.compare:
        require(json.loads(args.compare.read_text(encoding="utf-8")) == report,
                "regenerated report differs from frozen evidence")
        print(f"PASS: exact report comparison {args.compare}")
    else:
        print(serialized, end="")


if __name__ == "__main__":
    main()
