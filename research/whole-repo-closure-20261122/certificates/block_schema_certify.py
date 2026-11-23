#!/usr/bin/env python3
"""Exact finite classification certificates for one-parameter Collatz cycle words.

Input: [{"word": "110", "a": 1, "b": 0}, ...]. Words are chronological
shortcut-map parity words. A block occurs a*k+b times, for integer k>=0.
This implements the theorem in FIXED_BLOCK_CYCLE_CLASSIFICATION.md; it does
not enumerate, or claim to cover, arbitrary Collatz cycle words.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rat(value):
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def block_affine(word):
    slope, offset = F(1), F(0)
    for bit in word:
        if bit == "1":
            slope, offset = 3*slope/2, (3*offset+1)/2
        else:
            slope, offset = slope/2, offset/2
    return slope, offset


def validate_spec(spec):
    require(isinstance(spec, list) and spec, "nonempty block list required")
    for row in spec:
        require(set(row) == {"word", "a", "b"}, "exact word/a/b keys required")
        require(isinstance(row["word"], str) and row["word"] and
                set(row["word"]) <= {"0", "1"}, "nonempty binary block required")
        require(type(row["a"]) is int and type(row["b"]) is int and
                row["a"] >= 0 and row["b"] >= 0, "nonnegative integer exponents required")


def word_at(spec, k):
    return "".join(row["word"]*(row["a"]*k+row["b"]) for row in spec)


def finite_case(spec, k):
    word = word_at(spec, k)
    if not word:
        return {"k": k, "status": "empty_word"}
    slope, offset = block_affine(word)
    require(slope != 1, "nonempty shortcut word cannot have unit slope")
    value = offset/(1-slope)
    out = {"k": k, "fixed_point": rat(value)}
    if value <= 0:
        out["status"] = "nonpositive"
    elif value.denominator != 1:
        out["status"] = "nonintegral"
    else:
        start = int(value)
        x = start
        primitive = []
        for bit in word:
            require(x % 2 == int(bit), "integer fixed point failed physical parity")
            primitive.append(x)
            x = (3*x+1)//2 if x % 2 else x//2
            if x == start:
                break
        require(x == start, "primitive cycle did not close")
        x = start
        for bit in word:
            require(x % 2 == int(bit), "full word failed physical parity")
            x = (3*x+1)//2 if x % 2 else x//2
        require(x == start, "full word did not close")
        out.update(status="positive_cycle", primitive_cycle=primitive)
    return out


def add_term(terms, root, coefficient):
    terms[root] = terms.get(root, F(0)) + coefficient
    if terms[root] == 0:
        del terms[root]


def terms_json(terms):
    return [{"root": rat(root), "coefficient": rat(coefficient)}
            for root, coefficient in sorted(terms.items())]


def dominance(terms):
    require(bool(terms), "zero power sum needs identity certificate")
    root = max(terms)
    leading = terms[root]
    others = {r: c for r, c in terms.items() if r != root}
    total = sum((abs(c) for c in others.values()), F(0))
    ratio = max(others, default=F(0))/root
    k = 0
    tail = 2*total
    while tail > abs(leading):
        tail *= ratio
        k += 1
    return {"largest_root": rat(root), "leading_coefficient": rat(leading),
            "other_absolute_sum": rat(total), "root_ratio": rat(ratio),
            "cutoff": k}


def identity_structure(rotated, value):
    """Certify that every varying block fixes its ordinary entry state."""
    x = int(value)
    rows = []
    for row in rotated:
        slope, offset = block_affine(row["word"])
        entry = x
        if row["a"]:
            require(slope*x+offset == x,
                    "all-k integer identity must fix every varying block")
            repetitions = 1  # one complete cycle proves every repetition
        else:
            repetitions = row["b"]
        word = row["word"]*repetitions
        for bit in word:
            require(x > 0 and x % 2 == int(bit), "identity physical parity")
            x = (3*x+1)//2 if x % 2 else x//2
        rows.append({"entry": entry, "exit": x, "varying": bool(row["a"])})
    require(x == value, "identity stitching did not close")
    case = finite_case(rotated, 1)
    require(case["status"] == "positive_cycle", "nonempty identity sample")
    return {"value": value, "blocks": rows, "primitive_cycle": case["primitive_cycle"]}


def certify(spec):
    validate_spec(spec)
    affines = [block_affine(row["word"]) for row in spec]
    lambdas = [mu**row["a"] for row, (mu, _) in zip(spec, affines)]
    constants = [mu**row["b"] for row, (mu, _) in zip(spec, affines)]
    growth = F(1)
    prefactor = F(1)
    for value in lambdas:
        growth *= value
    for value in constants:
        prefactor *= value
    out = {"schema": "collatz-fixed-block-cycle-certificate/v1", "blocks": spec,
           "parameter_domain": "integers k >= 0; empty words excluded",
           "growth": rat(growth), "prefactor": rat(prefactor)}
    if growth == 1:
        require(all(row["a"] == 0 for row in spec), "unit growth cannot vary")
        out.update(regime="constant", constant_case=finite_case(spec, 0))
        return out
    if growth > 1:
        k, slope = 0, prefactor
        while slope < 1:
            slope *= growth
            k += 1
        out.update(regime="expanding", cutoff=k,
                   finite_cases=[finite_case(spec, j) for j in range(k)],
                   tail="no positive cycles: complete slope >= 1")
        return out

    # Rotating after the least product makes every suffix growth <= 1.
    products, prefix = [], F(1)
    for value in lambdas:
        products.append(prefix)
        prefix *= value
    rotation = min(range(len(spec)), key=lambda i: products[i])
    rotated = spec[rotation:]+spec[:rotation]
    data = []
    for row in rotated:
        mu, nu = block_affine(row["word"])
        data.append((nu/(1-mu), mu**row["b"], mu**row["a"]))
    r = len(spec)
    suffix_h, suffix_l = [F(1)]*(r+1), [F(1)]*(r+1)
    for i in reversed(range(r)):
        suffix_h[i] = data[i][1]*suffix_h[i+1]
        suffix_l[i] = data[i][2]*suffix_l[i+1]
    require(all(x <= 1 for x in suffix_l), "suffix rotation invariant")
    numerator = {}
    bound = F(0)
    for i, (center, _, _) in enumerate(data):
        add_term(numerator, suffix_l[i+1], center*suffix_h[i+1])
        add_term(numerator, suffix_l[i], -center*suffix_h[i])
        bound += abs(center)*(suffix_h[i]+suffix_h[i+1])
    k0, slope = 0, prefactor
    while slope > F(1, 2):
        slope *= growth
        k0 += 1
    cutoff = max(1, k0)
    candidates, identities = [], []
    for m in range(1, (2*bound).numerator//(2*bound).denominator+1):
        terms = dict(numerator)
        add_term(terms, F(1), F(-m))
        add_term(terms, growth, m*prefactor)
        row = {"value": m, "power_sum": terms_json(terms)}
        if terms:
            row["dominance"] = dominance(terms)
            cutoff = max(cutoff, row["dominance"]["cutoff"])
        else:
            row["identity"] = identity_structure(rotated, m)
            row["identity"]["original_value"] = (
                m if rotation == 0 else row["identity"]["blocks"][r-rotation-1]["exit"])
            identities.append(m)
        candidates.append(row)
    require(len(identities) <= 1, "at most one constant fixed point identity")
    out.update(regime="contracting", rotation=rotation,
               suffix_prefactors=[rat(x) for x in suffix_h],
               suffix_growth=[rat(x) for x in suffix_l],
               numerator=terms_json(numerator), numerator_bound=rat(bound),
               half_slope_cutoff=k0, candidate_bound=(2*bound).numerator//(2*bound).denominator,
               candidates=candidates, cutoff=cutoff,
               finite_cases=[finite_case(spec, j) for j in range(cutoff)],
               tail_identities=identities,
               tail="only the displayed fixed-cycle identities; no other positive cycles")
    return out


def gap_word(gaps):
    return "".join("1"+"0"*(g-1) for g in gaps)


def examples():
    return {
        "alphabet_four_signed_cycle": [
            {"word": gap_word([1, 1, 4, 1, 1, 1, 2]), "a": 1, "b": 0},
            {"word": gap_word([2]), "a": 1, "b": 0}],
        "trivial_cycle_identity": [{"word": "10", "a": 1, "b": 1}],
        "nontrivial_rotation_identity": [
            {"word": "1", "a": 0, "b": 1},
            {"word": "01", "a": 1, "b": 0},
            {"word": "0", "a": 0, "b": 1}],
        "expanding_finite_cycle": [
            {"word": "1", "a": 1, "b": 1},
            {"word": "0", "a": 0, "b": 1}],
        "constant_trivial_cycle": [{"word": "10", "a": 0, "b": 3}],
        "contracting_no_odd_steps": [{"word": "0", "a": 1, "b": 0}],
        "all_empty_constant": [{"word": "10", "a": 0, "b": 0}],
        "unequal_growth_with_offsets": [
            {"word": "110", "a": 1, "b": 1},
            {"word": "1000", "a": 2, "b": 0}],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.input:
        artifact = certify(json.loads(args.input.read_text()))
    else:
        artifact = {"schema": "collatz-fixed-block-cycle-suite/v1",
                    "certificates": {name: certify(spec) for name, spec in examples().items()}}
    args.output.write_text(json.dumps(artifact, indent=2)+"\n")
    if "certificates" in artifact:
        print(json.dumps({name: {"regime": cert["regime"], "cutoff": cert.get("cutoff"),
                                  "identities": cert.get("tail_identities", [])}
                          for name, cert in artifact["certificates"].items()}, indent=2))
    else:
        print("Certificate generated:", artifact["regime"], "cutoff", artifact.get("cutoff"))


if __name__ == "__main__":
    main()
