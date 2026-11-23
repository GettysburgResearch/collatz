#!/usr/bin/env python3
"""Replay an exact local-carry dual identity; no optimizer is required.

This checks a finite certificate ruling out one explicitly defined universal
Lyapunov-certificate class. It does not exclude integer Collatz cycles.
"""

from collections import Counter
from copy import deepcopy
from fractions import Fraction
import hashlib
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def state(value):
    require(isinstance(value, list) and len(value) == 3, "state shape")
    require(all(type(v) is int for v in value), "state integer type")
    w, c, h = value
    require(w in (0, 1), "state word bit")
    require(c in ((-1, 0) if w == 0 else (-1, 0, 1, 2)), "carry alphabet")
    require(0 <= h <= 5, "state category")
    require(h == 5 or h % 2 == c % 2, "state parity")
    return tuple(value)


def add_term(expression, kind, pair, coefficient):
    key = (kind, tuple(pair))
    expression[key] += coefficient
    if expression[key] == 0:
        del expression[key]


def add_delta(expression, first, second, coefficient):
    starts = ((0, 0, 5), (1, 1, 5))
    zeros = ((0, 0, 0), (1, 0, 0))
    add_term(expression, "V", (starts[first], starts[second]), coefficient)
    add_term(expression, "V", (zeros[first], zeros[second]), -coefficient)


def check_certificate(payload):
    require(payload.get("schema") == "collatz-positive-carry-pair-dual-v1", "schema")
    require(payload.get("category_cutoff") == 5, "category cutoff")
    require(payload.get("target") == {"delta_11": 2, "delta_01": 3, "delta_10": 3}, "target")
    transitions = payload.get("transitions")
    require(isinstance(transitions, list) and len(transitions) == 34, "transition count")
    total = Counter()
    weight_sum = 0
    for entry in transitions:
        weight = entry["weight"]
        require(type(weight) is int and weight > 0, "positive integer weight")
        ins = tuple(state(s) for s in entry["input"])
        outs = tuple(state(s) for s in entry["output"])
        require(len(ins) == 3 and len(outs) == 2, "local window shape")
        ns = entry["integer_witness"]
        require(len(ns) == 4 and all(type(n) is int and n >= 0 for n in ns), "nonnegative integer witness")
        for i, (w, c, h) in enumerate(ins):
            require(h == min(ns[i], 5), "input quotient category")
            require(c % 2 == ns[i] % 2, "input quotient parity")
            require(2 * ns[i + 1] - 3**w * ns[i] == c, "exact horizontal carry equation")
        for i in range(2):
            w, c, _ = ins[i]
            numerator = c + 3**w * (c % 2) - 2 * (ins[i + 1][1] % 2)
            require(numerator % 2 == 0, "integral vertical carry")
            expected = (w, numerator // 2, min(ns[i] // 2, 5))
            require(outs[i] == expected, "exact vertical output")
            require(2 * (ns[i + 1] // 2) - 3**w * (ns[i] // 2) == outs[i][1], "halved horizontal equation")
        # R = V(s0,s1) - V(t0,t1) + F(s1,s2) - F(s0,s1).
        add_term(total, "V", ins[:2], weight)
        add_term(total, "V", outs, -weight)
        add_term(total, "F", ins[1:], weight)
        add_term(total, "F", ins[:2], -weight)
        weight_sum += weight
    target = Counter()
    add_delta(target, 1, 1, 2)
    add_delta(target, 0, 1, 3)
    add_delta(target, 1, 0, 3)
    require(total == target, "exact coefficient identity")
    require(weight_sum == 40, "weight sum")
    return {"local_transitions": len(transitions), "weight_sum": weight_sum,
            "coefficient_identity": "2 delta_11 + 3 delta_01 + 3 delta_10", "flux_cancels": True}


def carry(word):
    p = word.count("1")
    positions = [i for i, bit in enumerate(word) if bit == "1"]
    return sum(2**position * 3**(p - 1 - j) for j, position in enumerate(positions))


def check_family(k):
    require(type(k) is int and k >= 1, "family parameter")
    word = "11101010" + "11011010" * (k - 1)
    denominator = 256**k - 243**k
    require(denominator % 13 == 0, "full denominator divisibility")
    numerator = 319 * (denominator // 13) - 36 * 243**(k - 1)
    require(carry(word) == numerator, "full ordered numerator")
    expected_gcd = 13 if k % 13 == 7 else 1
    require(gcd(denominator, numerator) == expected_gcd, "full numerical gcd")
    require(word.count("1") == 5 * k and len(word) == 8 * k, "word clocks")
    pairs = Counter(word[i] + word[(i + 1) % len(word)] for i in range(len(word)))
    require(pairs == {"11": 2 * k, "10": 3 * k, "01": 3 * k}, "cyclic pair counts")
    triples = [(word + word[:2])[i:i + 3] for i in range(len(word))]
    require(triples.count("111") == 1, "unique marker proving primitivity")
    x = Fraction(numerator, denominator)
    origin = x
    minimum = x
    for bit in word:
        require(x.denominator % 2 == 1, "odd reduced denominator")
        require(x.numerator % 2 == int(bit), "actual rational parity")
        minimum = min(minimum, x)
        x = (3 * x + 1) / 2 if bit == "1" else x / 2
    require(x == origin, "actual rational closure")
    require(minimum >= Fraction(283, 13), "whole-cycle lower bound")
    return {"k": k, "length": 8 * k, "weight": 5 * k,
            "full_denominator_bits": denominator.bit_length(),
            "full_gcd": expected_gcd, "minimum": str(minimum)}


def main():
    certificate_path = HERE / "positive_carry_dual.json"
    raw = certificate_path.read_bytes()
    payload = json.loads(raw)
    result = check_certificate(payload)
    mutation_rejections = []
    for name in ("weight", "witness", "output"):
        bad = deepcopy(payload)
        if name == "weight":
            bad["transitions"][0]["weight"] += 1
        elif name == "witness":
            bad["transitions"][0]["integer_witness"][0] += 2
        else:
            bad["transitions"][0]["output"][0][2] = 1
        try:
            check_certificate(bad)
        except ValueError:
            mutation_rejections.append(name)
        else:
            raise ValueError("corrupted certificate accepted: " + name)
    result.update({"certificate_sha256": hashlib.sha256(raw).hexdigest(),
                   "mutation_rejections": mutation_rejections,
                   "family_controls": [check_family(k) for k in (1, 2, 7, 13, 20)],
                   "scope": "exact local-potential obstruction; no cycle-exclusion theorem"})
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
