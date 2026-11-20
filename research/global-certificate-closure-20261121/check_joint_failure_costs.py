#!/usr/bin/env python3
"""Exact all-lift checks and a directed five-oracle proof compiler.

This verifies a conditional theorem. It does not assume or prove physical
five closure. A compiled query must be discharged by an actual ordinary
certificate for its target before it can be used to continue the proof.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "directed_five_certificate.json"
EXPECTED_SHA256 = "751523dd92445610a26302947a2f689aecc56a27eaf6fa1f9954eb2e59f5c7c1"
FIVE_COST = Fraction(3669265, 2239)
REVERSE_COST = Fraction(2025217, 23)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def oddpart(n):
    need(n > 0, "odd part needs a positive input")
    while n % 2 == 0:
        n //= 2
    return n


def shortcut(n):
    need(n > 0, "ordinary shortcut needs a positive input")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def ratio_max(a, b, m, r, u0):
    """Supremum of (a*u+b)/(m*u+r), u>=u0, by affine monotonicity."""
    need(m > 0 and m * u0 + r > 0, "nonpositive source domain")
    return max(Fraction(a, m), Fraction(a * u0 + b, m * u0 + r))


def affine_unit(a, b, u0):
    need(a > 0 and a * u0 + b > 0, "nonpositive affine family")
    need(a % 3 == 0 and b % 3 != 0, "not uniformly a ternary unit")


def check_certificate(data):
    words = {word["id"]: word["steps"] for word in data["word_table"]}
    need(len(words) == len(data["word_table"]), "duplicate word identifier")
    cells = data["cells"]
    common = lcm(*(cell["modulus"] for cell in cells))
    coverage = bytearray(common)
    queries = []
    max_endpoint = Fraction(0)
    for cell in cells:
        m, r, u0 = cell["modulus"], cell["residue"], cell["min_parameter"]
        need(m > 0 and 0 < r < m and gcd(r, 30) == 1, "bad initial cell")
        need(u0 == (1 if r == 1 else 0), "unexpected base exclusion")
        need(m % 30 == 0 and common % m == 0, "bad covering modulus")
        for residue in range(r, common, m):
            need(coverage[residue] == 0, "overlapping cells")
            coverage[residue] = 1
        a, b = m, r
        query_count = 0
        affine_unit(a, b, u0)
        for position, (operation, divisions) in enumerate(words[cell["word"]]):
            if operation == "B":
                need(a % 2 == 0 and b % 2 == 1, "B input not uniformly odd")
                a, b = 3 * a, 3 * b + 1
            else:
                need(operation.startswith("I"), "unknown operation")
                exponent = int(operation[1:])
                need(exponent >= 1, "nonpositive inverse exponent")
                power = 1 << exponent
                need((power * a) % 3 == 0 and (power * b - 1) % 3 == 0,
                     "nonintegral inverse family")
                a, b = power * a // 3, (power * b - 1) // 3
                need(a % 2 == 0 and b % 2 == 1, "inverse output not odd")
            affine_unit(a, b, u0)
            for digit in divisions:
                divisor = int(digit)
                need(divisor in (2, 5), "unsupported divisor")
                need(a % divisor == 0 and b % divisor == 0, "nonintegral division")
                a, b = a // divisor, b // divisor
                affine_unit(a, b, u0)
                if divisor == 5:
                    query_count += 1
                    upper = ratio_max(a, b, m, r, u0)
                    queries.append({
                        "ratio": upper,
                        "word": cell["word"],
                        "cell": [m, r, u0],
                        "position": position,
                        "antecedent": [a, b],
                    })
        need(query_count <= 1, "word has more than one five query")
        need([a, b] == cell["endpoint"], "false endpoint")
        need(19 * m - 20 * a >= 0, "endpoint slope exceeds 19/20")
        need((19 * m - 20 * a) * u0 + 19 * r - 20 * b >= 0,
             "endpoint exceeds 19/20 on domain")
        need(m - a >= 0 and (m - a) * u0 + r - b > 0,
             "no strict integer decrease")
        max_endpoint = max(max_endpoint, ratio_max(a, b, m, r, u0))
    need(all(bool(coverage[r]) == (gcd(r, 30) == 1) for r in range(common)),
         "incomplete cover")
    need(len(queries) == 219, "wrong number of five queries")
    maximizer = max(queries, key=lambda query: query["ratio"])
    need(maximizer["ratio"] == FIVE_COST, "wrong five-query maximum")
    need(maximizer["cell"] == [8640, 2239, 0], "wrong maximizing cell")
    need(maximizer["antecedent"] == [14155776, 3669265], "wrong maximizing query")
    need(max_endpoint == Fraction(13403, 14119), "wrong endpoint maximum")
    return words, {
        "cells": len(cells),
        "words": len(words),
        "common_modulus": common,
        "covered_residues": sum(coverage),
        "five_queries": len(queries),
        "sharp_five_query_ratio": str(FIVE_COST),
        "sharp_endpoint_ratio": str(max_endpoint),
        "maximizer": {key: str(value) if isinstance(value, Fraction) else value
                      for key, value in maximizer.items()},
    }


def numeric_word(n, steps):
    """Path from n to its smaller endpoint, in implication-reverse order."""
    path = []
    x = n
    for operation, divisions in steps:
        old = x
        if operation == "B":
            need(x % 2 == 1, "numeric B domain")
            x = 3 * x + 1
            need(shortcut(old) == shortcut(x), "B ordinary connection")
        else:
            exponent = int(operation[1:])
            numerator = (1 << exponent) * x - 1
            need(numerator % 3 == 0, "numeric inverse integrality")
            x = numerator // 3
            need(x > 0 and x % 2 == 1 and x % 3 != 0, "numeric inverse domain")
            value = x
            for _ in range(exponent):
                value = shortcut(value)
            need(value == old, "inverse ordinary clock")
        path.append([operation, old, x])
        for digit in divisions:
            divisor = int(digit)
            need(x % divisor == 0, "numeric exact division")
            old, x = x, x // divisor
            path.append([f"/{divisor}", old, x])
    return x, path


def compile_unit(n, data, words):
    """Produce an executable conditional proof program for any ternary unit.

    Every query is accompanied by an ordinary path from the previous
    recursively certified endpoint to its antecedent. This routine outputs
    the actual integer proof skeleton, not an ordinary convergence claim.
    """
    need(n > 0 and n % 3 != 0, "compiler domain is positive ternary units")
    original = n
    levels = []
    while n != 1:
        if n % 2 == 0:
            q, path, cell_name = n // 2, [["/2", n, n // 2]], "even"
        elif n % 5 == 0:
            q, path, cell_name = n // 5, [["/5", n, n // 5]], "five"
        else:
            matches = [cell for cell in data["cells"]
                       if n % cell["modulus"] == cell["residue"]
                       and (n - cell["residue"]) // cell["modulus"] >= cell["min_parameter"]]
            need(len(matches) == 1, "source not uniquely covered")
            cell = matches[0]
            u = (n - cell["residue"]) // cell["modulus"]
            q, path = numeric_word(n, words[cell["word"]])
            need(q == cell["endpoint"][0] * u + cell["endpoint"][1], "numeric endpoint")
            cell_name = cell["word"]
        need(q > 0 and q % 3 != 0 and 20 * q <= 19 * n, "compiler descent")
        queries = []
        for index, (operation, before, after) in enumerate(path):
            if operation == "/5":
                antecedent = oddpart(after)
                need(antecedent % 3 != 0 and before == 5 * after, "bad five arrow")
                need(antecedent <= FIVE_COST * n, "query over local budget")
                queries.append({
                    "antecedent": antecedent,
                    "target": 5 * antecedent,
                    "unstripped_antecedent": after,
                    "ordinary_suffix": path[index + 1:],
                })
        need(len(queries) <= 1, "more than one conditional query in a level")
        levels.append({"source": n, "endpoint": q, "rule": cell_name,
                       "reverse_implication_path": path, "five_queries": queries})
        n = q
    # Execute from 1 outwards. The ordinary suffix of each query is reversed
    # only after all deeper levels have supplied a genuine endpoint certificate.
    ordered_levels = list(reversed(levels))
    ordered_queries = [query for level in ordered_levels for query in level["five_queries"]]
    need(all(query["antecedent"] <= FIVE_COST * original for query in ordered_queries),
         "query over global budget")
    return {"source": original, "base": 1, "execution_levels": ordered_levels,
            "queries": ordered_queries,
            "requires": "an actual ordinary target certificate for every five query"}


def bounded_certificate(n, limit=100000):
    result = [n]
    for _ in range(limit):
        if result[-1] == 1:
            return result
        result.append(shortcut(result[-1]))
    raise RuntimeError("bounded replay unresolved; not a nonconvergence claim")


def check_ordinary_certificate(values, expected_start):
    need(isinstance(values, (list, tuple)) and values
         and values[0] == expected_start and values[-1] == 1,
         "bad supplied ordinary certificate endpoints")
    need(all(a > 0 and shortcut(a) == b for a, b in zip(values, values[1:])),
         "nonordinary supplied certificate")


def transfer_backwards(path, endpoint_certificate, five_oracle):
    proof = endpoint_certificate[:]
    for operation, before, after in reversed(path):
        check_ordinary_certificate(proof, after)
        if operation == "/2":
            proof = [before] + proof
        elif operation == "B":
            need(len(proof) >= 2 and proof[1] == before * 3 // 2 + 1, "bad B merge")
            proof = [before] + proof[1:]
        elif operation.startswith("I"):
            count = int(operation[1:])
            extended = proof[:]
            while len(extended) <= count:
                extended.append(shortcut(extended[-1]))
            need(extended[count] == before, "bad inverse splice")
            proof = extended[count:]
            if proof[-1] != 1:
                # A certificate may have been padded past its first 1.
                proof.append(1)
        elif operation == "/5":
            r = oddpart(after)
            offset = 0
            while proof[offset] != r:
                offset += 1
            antecedent_certificate = proof[offset:]
            check_ordinary_certificate(antecedent_certificate, r)
            target_certificate = five_oracle(r, antecedent_certificate)
            check_ordinary_certificate(target_certificate, 5 * r)
            prefix = [before]
            while prefix[-1] != 5 * r:
                need(prefix[-1] % 2 == 0, "bad even five normalization")
                prefix.append(prefix[-1] // 2)
            proof = prefix[:-1] + target_certificate
        else:
            raise ValueError("unknown proof operation")
        check_ordinary_certificate(proof, before)
    return proof


def execute(program, five_oracle):
    proof = [1]
    for level in program["execution_levels"]:
        check_ordinary_certificate(proof, level["endpoint"])
        proof = transfer_backwards(level["reverse_implication_path"], proof, five_oracle)
        check_ordinary_certificate(proof, level["source"])
    check_ordinary_certificate(proof, program["source"])
    return proof


def rejection_controls(data, words):
    controls = []
    def rejects(name, action):
        try:
            action()
        except (ValueError, KeyError):
            controls.append(name)
        else:
            raise ValueError(f"negative control accepted: {name}")
    missing = copy.deepcopy(data)
    missing["cells"].pop()
    rejects("missing infinite residue cell", lambda: check_certificate(missing))
    broken_inverse = copy.deepcopy(data)
    for word in broken_inverse["word_table"]:
        for pair in word["steps"]:
            if pair[0].startswith("I"):
                pair[0] = "I0"
                break
        else:
            continue
        break
    rejects("nonpositive inverse exponent", lambda: check_certificate(broken_inverse))
    rejects("ternary nonunit compiler source", lambda: compile_unit(3, data, words))
    program = compile_unit(5, data, words)
    rejects("membership boolean in place of ordinary certificate",
            lambda: execute(program, lambda r, antecedent: True))
    rejects("reversed physical-five direction",
            lambda: execute(program, lambda r, antecedent: antecedent))
    rejects("false ordinary target edge",
            lambda: execute(program, lambda r, antecedent: [5 * r, 1]))
    return controls


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--program", type=int, help="write a conditional program for this unit")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    raw = CERTIFICATE.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256, "frozen source hash changed")
    data = json.loads(raw)
    words, report = check_certificate(data)
    samples = [1, 2, 5, 7, 23, 95, 239, 2239, 5119, 7999, 14119, 299239, 1000001]
    cases = []
    def oracle(r, antecedent_certificate):
        check_ordinary_certificate(antecedent_certificate, r)
        return bounded_certificate(5 * r)
    for n in samples:
        program = compile_unit(n, data, words)
        proof = execute(program, oracle)
        cases.append({"source": n, "levels": len(program["execution_levels"]),
                      "queries": len(program["queries"]),
                      "max_query": max([0] + [q["antecedent"] for q in program["queries"]]),
                      "ordinary_replay_steps": len(proof) - 1})
    report["bounded_execution_replays"] = cases
    report["rejected_controls"] = rejection_controls(data, words)
    report["reverse_cost_from_PR163"] = str(REVERSE_COST)
    report["generic_five_to_reverse_budget"] = str(5 * REVERSE_COST)
    report["hard_rank_five_two_way_budget_product"] = str(5 * REVERSE_COST / 4)
    report["global_theorem_proved"] = False
    report["status"] = "exact conditional all-source compiler; physical five queries remain open"
    # The universal part is the coefficient/coverage proof above, not these replays.
    if args.program is not None:
        report["conditional_program"] = compile_unit(args.program, data, words)
    rendered = json.dumps(report, indent=2) + "\n"
    if args.output:
        need(not args.output.exists(), "refusing to overwrite an evidence file")
        args.output.write_text(rendered)
    print(rendered)


if __name__ == "__main__":
    main()
