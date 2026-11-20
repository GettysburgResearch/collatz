#!/usr/bin/env python3
"""Root reconstruction of the five cover. No author/search imports.

Work in the original n coordinate with rational affine forms, then prove
each guard on the full progression. All acceptance checks survive -OO.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import lcm
import copy
import hashlib
import json


def need(condition, message):
    if not condition:
        raise ArithmeticError(message)


def integral_progression(form, modulus, residue):
    slope, offset = form
    step = slope * modulus
    first = slope * residue + offset
    need(step.denominator == first.denominator == 1, "integral progression")
    need(step > 0 and first > 0, "positive complete progression")
    return int(step), int(first)


def advance(form, symbol, modulus, residue):
    step, first = integral_progression(form, modulus, residue)
    slope, offset = form
    query = None
    if symbol == "D":
        result = (2 * slope, 2 * offset)
    elif symbol == "E":
        need(step % 2 == 0 and first % 2 == 0, "even input")
        result = (slope / 2, offset / 2)
    elif symbol == "O":
        need(step % 2 == 0 and first % 2 == 1, "odd input")
        result = (3 * slope / 2, (3 * offset + 1) / 2)
    elif symbol == "I":
        result = (2 * slope / 3, (2 * offset - 1) / 3)
        out_step, out_first = integral_progression(result, modulus, residue)
        need(out_step % 2 == 0 and out_first % 2 == 1, "odd inverse source")
        need((3 * result[0] / 2, (3 * result[1] + 1) / 2) == form,
             "inverse is literal ordinary edge")
    elif symbol == "M":
        need(step % 3 == 0 and first % 3 != 0, "five query unit")
        query = form
        result = (5 * slope, 5 * offset)
    elif symbol == "V":
        result = (slope / 5, offset / 5)
        out_step, out_first = integral_progression(result, modulus, residue)
        need(out_step % 3 == 0 and out_first % 3 != 0, "inverse five query unit")
        query = result
    else:
        raise ArithmeticError("unknown symbol")
    integral_progression(result, modulus, residue)
    return result, query


def prove(data):
    rows = data["rows"]
    need(isinstance(rows, list) and len(rows) > 0, "nonempty cover")
    period = lcm(*(row["modulus"] for row in rows))
    need(period == data["period"] and period > 0 and period % 2 == 0,
         "advertised even period")
    owner = [-1] * (period // 2)
    cap_sum = Q(0)
    max_cap = Q(0)
    cell_count = move_count = query_count = 0
    transcript = []
    for row_index, row in enumerate(rows):
        modulus, residues, words = row["modulus"], row["residues"], row["words"]
        need(modulus > 0 and modulus % 2 == 0 and period % modulus == 0,
             "cell modulus")
        need(len(words) == 2 and len(residues) > 0, "two paths and nonempty cells")
        need(len(set(residues)) == len(residues), "unique representatives")
        reference_queries = None
        caps = None
        for residue in residues:
            need(isinstance(residue, int) and 0 < residue < modulus
                 and residue % 2 == 1, "positive odd cell")
            endpoints, queries = [], []
            for start, word in zip((1, 3), words):
                form = Q(start), Q(0)
                for symbol in word:
                    form, query = advance(form, symbol, modulus, residue)
                    if query is not None:
                        queries.append(query)
                endpoints.append(form)
            need(endpoints[0] == endpoints[1], "same global affine endpoint")
            if reference_queries is None:
                reference_queries = queries
                caps = [Q(0)] * len(queries)
            need(queries == reference_queries, "same injective queries on row union")
            for index, (slope, offset) in enumerate(queries):
                need(slope > 0, "injective query")
                caps[index] = max(caps[index], slope, slope + offset / residue)
            for value in range(residue, period, modulus):
                if owner[value // 2] == -1:
                    owner[value // 2] = row_index
            cell_count += 1
            transcript.append([row_index, modulus, residue,
                               [str(x) for x in endpoints[0]],
                               [[str(a), str(b)] for a, b in queries]])
        move_count += sum(len(word) for word in words)
        query_count += len(caps)
        cap_sum += sum(caps, Q(0))
        max_cap = max([max_cap] + caps)
    need(-1 not in owner, "all odd sources covered")
    need(cap_sum < 2500 and max_cap <= Q(7153, 21), "energy constants")
    need(query_count <= 248, "query count in stated inequality")
    encoded = json.dumps(transcript, separators=(",", ":"), sort_keys=True).encode()
    return {
        "status": "PASS",
        "scope": "Independent exact affine guard, cover, injectivity and weight reconstruction; no finite-energy upper bound or Collatz proof",
        "rows": len(rows), "cells": cell_count, "period": period,
        "odd_sources_in_period": len(owner),
        "row_moves": move_count, "row_queries": query_count,
        "maximum_query_ratio": str(max_cap), "sum_query_ratios": str(cap_sum),
        "harmonic_all_source_constant": str(4 * cap_sum),
        "global_coordinate_transcript_sha256": hashlib.sha256(encoded).hexdigest(),
    }


def negative_controls(data):
    bad = []
    x = copy.deepcopy(data); x["rows"] = x["rows"][:1]; bad.append(x)
    x = copy.deepcopy(data); x["rows"][0]["words"][0] += "D"; bad.append(x)
    x = copy.deepcopy(data); x["rows"][0]["words"][0] = "E" + x["rows"][0]["words"][0]; bad.append(x)
    x = copy.deepcopy(data); x["rows"][0]["words"][1] = "M" + x["rows"][0]["words"][1]; bad.append(x)
    x = copy.deepcopy(data); x["rows"][0]["residues"][0] = 0; bad.append(x)
    x = copy.deepcopy(data); x["rows"][0]["words"][0] = "V" + x["rows"][0]["words"][0]; bad.append(x)
    x = copy.deepcopy(data); x["period"] *= 2; bad.append(x)
    for candidate in bad:
        try:
            prove(candidate)
        except (ArithmeticError, ValueError, KeyError, TypeError):
            pass
        else:
            raise ArithmeticError("invalid fixture passed")
    return len(bad)


if __name__ == "__main__":
    path = Path(__file__).with_name("five_cover_candidates.json")
    payload = json.loads(path.read_text(encoding="utf8"))
    result = prove(payload)
    result["negative_controls_rejected"] = negative_controls(payload)
    result["certificate_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))
