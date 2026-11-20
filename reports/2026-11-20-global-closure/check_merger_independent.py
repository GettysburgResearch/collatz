#!/usr/bin/env python3
"""Independent rational-polynomial audit of the directed five certificate.

This implementation does not import the producer. Coverage uses pairwise
CRT incompatibility plus exact rational density, not a residue bitmap.
The division-by-five implication is an ASSUMPTION, not a Collatz edge.
"""

from fractions import Fraction as Q
from hashlib import sha256
from math import gcd
from pathlib import Path
import argparse
import copy
import json

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "reports/2026-11-20-global-closure/merger-certificate.json"
EXPECTED = "751523dd92445610a26302947a2f689aecc56a27eaf6fa1f9954eb2e59f5c7c1"


def check(ok, why):
    if not ok:
        raise ValueError(why)


def integral(poly):
    return all(v.denominator == 1 for v in poly)


def value(poly, t):
    return poly[0] * t + poly[1]


def guard(poly, t0, odd=False):
    check(integral(poly), "not an integer polynomial")
    a, b = map(int, poly)
    check(a > 0 and value(poly, t0) > 0, "positivity fails")
    check(a % 3 == 0 and b % 3 != 0, "ternary-unit guard fails")
    if odd:
        check(a % 2 == 0 and b % 2 == 1, "odd-source guard fails")


def ratio(poly, start, t0):
    return max(poly[0] / start[0], value(poly, t0) / value(start, t0))


def audit(packet):
    check(packet["schema"] == "collatz-directed-five-unit-descent-v1", "schema")
    cells = packet["cells"]
    words = {w["id"]: w["steps"] for w in packet["word_table"]}
    check(len(words) == len(packet["word_table"]), "repeated word identifier")
    density = sum((Q(1, c["modulus"]) for c in cells), Q(0))
    check(density == Q(4, 15), "missing residue density")
    comparisons = 0
    for j, c in enumerate(cells):
        M, r = c["modulus"], c["residue"]
        check(type(M) is int and type(r) is int, "cell not integral")
        check(M > 0 and M % 30 == 0 and 0 < r < M and gcd(r, 30) == 1,
              "cell not contained in the required units")
        for d in cells[:j]:
            check((r - d["residue"]) % gcd(M, d["modulus"]) != 0,
                  "CRT overlap")
            comparisons += 1

    primitive_count = five_count = 0
    max_ratio = Q(0)
    max_intermediate = Q(0)
    max_five_argument = Q(0)
    max_five_cell = None
    per_cell = []
    for c in cells:
        M, r, t0 = c["modulus"], c["residue"], c["min_parameter"]
        check(t0 == int((M, r) == (1440, 1)), "unexpected finite exception")
        start = (Q(M), Q(r))
        p = start
        guard(p, t0, odd=True)
        uses = 0
        for op, divisions in words[c["word"]]:
            if op == "B":
                guard(p, t0, odd=True)
                p = (3 * p[0], 3 * p[1] + 1)
            else:
                check(op.startswith("I") and op[1:].isdigit(), "unknown primitive")
                g = int(op[1:])
                check(g >= 1, "nonpositive inverse exponent")
                p = (Q(2**g, 3) * p[0], Q(2**g, 3) * p[1] - Q(1, 3))
                guard(p, t0, odd=True)
            primitive_count += 1
            guard(p, t0)
            max_intermediate = max(max_intermediate, ratio(p, start, t0))
            for digit in divisions:
                check(digit in ("2", "5"), "unlicensed division")
                p = (p[0] / int(digit), p[1] / int(digit))
                guard(p, t0)
                primitive_count += 1
                if digit == "5":
                    uses += 1
                    five_count += 1
                    current = ratio(p, start, t0)
                    if current > max_five_argument:
                        max_five_argument = current
                        max_five_cell = [M, r, c["word"]]
                max_intermediate = max(max_intermediate, ratio(p, start, t0))
        check(uses <= 1, "more than one conditional use")
        check(p == tuple(map(Q, c["endpoint"])), "endpoint mismatch")
        current = ratio(p, start, t0)
        check(current <= Q(19, 20), "uniform contraction fails")
        max_ratio = max(max_ratio, current)
        per_cell.append([M, r, int(p[0]), int(p[1]), uses])

    return {
        "cells": len(cells),
        "pairwise_crt_checks": comparisons,
        "exact_cover_density": str(density),
        "rational_primitive_checks": primitive_count,
        "conditional_five_uses": five_count,
        "maximum_endpoint_ratio": str(max_ratio),
        "maximum_intermediate_ratio": str(max_intermediate),
        "maximum_five_argument_ratio": str(max_five_argument),
        "maximum_five_argument_cell": max_five_cell,
        "cell_transcript_sha256": sha256(json.dumps(per_cell, separators=(",", ":")).encode()).hexdigest(),
        "scope": "Complete symbolic conditional descent, not a proof of the physical five-closure premise.",
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--compare", type=Path)
    args = ap.parse_args()
    check(not (args.output and args.compare), "choose one output mode")
    raw = PACKET.read_bytes()
    check(sha256(raw).hexdigest() == EXPECTED, "frozen certificate changed")
    packet = json.loads(raw)
    result = audit(packet)
    controls = []
    missing = copy.deepcopy(packet)
    missing["cells"].pop()
    overlap = copy.deepcopy(packet)
    overlap["cells"][-1] = overlap["cells"][-2]
    endpoint = copy.deepcopy(packet)
    endpoint["cells"][0]["endpoint"][1] += 1
    illegal = copy.deepcopy(packet)
    illegal["word_table"][0]["steps"][0][1] += "3"
    for label, altered in [("missing cell", missing), ("overlapping cells", overlap),
                           ("wrong endpoint", endpoint), ("unlicensed division", illegal)]:
        try:
            audit(altered)
        except ValueError:
            controls.append(label)
        else:
            raise ValueError("accepted corruption: " + label)
    report = {
        "schema": "independent-directed-five-audit-v1",
        "status": "PASS",
        "certificate_sha256": EXPECTED,
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "results": result,
        "corruptions_rejected": controls,
    }
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        with args.output.open("x", encoding="utf-8") as f:
            f.write(text)
    elif args.compare:
        check(json.loads(args.compare.read_text()) == report, "replay differs")
        print("PASS exact independent audit comparison")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
