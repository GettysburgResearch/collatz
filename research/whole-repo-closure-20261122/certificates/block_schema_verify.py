#!/usr/bin/env python3
"""Independent checker for complete fixed-block cycle classification certificates.

No generator import, no floating-point comparisons, and no assertion guards.
Every unbounded conclusion is checked through exact rational inequalities.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def need(ok, message):
    if not ok:
        raise ValueError(message)


def integer(value, label):
    need(type(value) is int and value >= 0, label)
    return value


def q(value):
    need(isinstance(value, str), "rational strings required")
    return Fraction(value)


def show(value):
    return f"{value.numerator}/{value.denominator}"


def integer_affine(word):
    coefficient, carry, denominator = 1, 0, 1
    for bit in word:
        if bit == "1":
            coefficient *= 3
            carry = 3*carry+denominator
        denominator *= 2
    return coefficient, carry, denominator


def physical(word, start):
    value = start
    for bit in word:
        need(value > 0 and value % 2 == int(bit), "physical parity/positivity")
        value = (3*value+1)//2 if bit == "1" else value//2
    return value


def finite_expected(blocks, k):
    word = "".join(b["word"]*(b["a"]*k+b["b"]) for b in blocks)
    if not word:
        return {"k": k, "status": "empty_word"}
    coefficient, carry, denominator = integer_affine(word)
    need(denominator != coefficient, "nonempty slope equality")
    point = Fraction(carry, denominator-coefficient)
    out = {"k": k, "fixed_point": show(point)}
    if point <= 0:
        out["status"] = "nonpositive"
    elif point.denominator != 1:
        out["status"] = "nonintegral"
    else:
        start = int(point)
        need(physical(word, start) == start, "full cycle replay")
        orbit, x = [], start
        for _ in range(len(word)):
            orbit.append(x)
            x = (3*x+1)//2 if x % 2 else x//2
            if x == start:
                break
        need(x == start, "first return missing")
        out.update(status="positive_cycle", primitive_cycle=orbit)
    return out


def add(poly, root, coefficient):
    poly[root] = poly.get(root, Fraction(0))+coefficient
    if poly[root] == 0:
        del poly[root]


def read_terms(rows):
    need(isinstance(rows, list), "term list")
    result = {}
    for row in rows:
        root, coefficient = q(row["root"]), q(row["coefficient"])
        need(root > 0 and coefficient != 0 and root not in result, "coalesced positive roots")
        result[root] = coefficient
    return result


def verify_identity(identity, blocks, value, rotation):
    need(identity["value"] == value, "identity value")
    x = value
    expected = []
    for block in blocks:
        coefficient, carry, denominator = integer_affine(block["word"])
        entry = x
        if block["a"]:
            need(coefficient*x+carry == denominator*x, "varying block must fix entry")
            x = physical(block["word"], x)
        else:
            x = physical(block["word"]*block["b"], x)
        expected.append({"entry": entry, "exit": x, "varying": bool(block["a"])})
    need(x == value and identity["blocks"] == expected, "identity cycle stitching")
    original = value if rotation == 0 else expected[len(blocks)-rotation-1]["exit"]
    need(identity["original_value"] == original, "identity original boundary")
    sample = finite_expected(blocks, 1)
    need(sample["status"] == "positive_cycle", "identity sample positivity")
    need(identity["primitive_cycle"] == sample["primitive_cycle"], "identity primitive cycle")


def verify(cert):
    need(cert["schema"] == "collatz-fixed-block-cycle-certificate/v1", "schema")
    blocks = cert["blocks"]
    need(isinstance(blocks, list) and blocks, "block list")
    growth, prefactor = Fraction(1), Fraction(1)
    for b in blocks:
        need(set(b) == {"word", "a", "b"}, "block keys")
        need(isinstance(b["word"], str) and b["word"] and set(b["word"]) <= {"0", "1"}, "binary word")
        a, offset = integer(b["a"], "a"), integer(b["b"], "b")
        coefficient, carry, denominator = integer_affine(b["word"])
        slope = Fraction(coefficient, denominator)
        growth *= slope**a
        prefactor *= slope**offset
    need(q(cert["growth"]) == growth and q(cert["prefactor"]) == prefactor, "total slope data")
    regime = cert["regime"]
    if growth == 1:
        need(regime == "constant" and all(b["a"] == 0 for b in blocks), "constant regime")
        need(cert["constant_case"] == finite_expected(blocks, 0), "constant complete word")
        return {"regime": regime, "finite_cases": 1, "candidates": 0}
    cutoff = integer(cert["cutoff"], "cutoff")
    finite = cert["finite_cases"]
    need(isinstance(finite, list) and len(finite) == cutoff, "complete finite parameter range")
    for k in range(cutoff):
        need(finite[k] == finite_expected(blocks, k), f"complete quotient/replay at k={k}")
    if growth > 1:
        need(regime == "expanding", "expanding regime")
        need(prefactor*growth**cutoff >= 1, "expanding tail slope")
        return {"regime": regime, "finite_cases": cutoff, "candidates": 0}
    need(regime == "contracting" and cutoff >= 1, "contracting regime")
    rotation = integer(cert["rotation"], "rotation")
    need(rotation < len(blocks), "rotation range")
    rotated = blocks[rotation:]+blocks[:rotation]
    centers, hs, ls = [], [], []
    for b in rotated:
        coefficient, carry, denominator = integer_affine(b["word"])
        slope = Fraction(coefficient, denominator)
        centers.append(Fraction(carry, denominator-coefficient))
        hs.append(slope**b["b"])
        ls.append(slope**b["a"])
    r = len(blocks)
    sh, sl = [Fraction(1)]*(r+1), [Fraction(1)]*(r+1)
    for i in range(r-1, -1, -1):
        sh[i], sl[i] = hs[i]*sh[i+1], ls[i]*sl[i+1]
    need([q(x) for x in cert["suffix_prefactors"]] == sh, "suffix prefactors")
    need([q(x) for x in cert["suffix_growth"]] == sl and all(x <= 1 for x in sl), "all suffix growth bounded")
    numerator = {}
    bound = Fraction(0)
    for i, center in enumerate(centers):
        add(numerator, sl[i+1], center*sh[i+1])
        add(numerator, sl[i], -center*sh[i])
        bound += abs(center)*(sh[i]+sh[i+1])
    need(read_terms(cert["numerator"]) == numerator, "complete numerator power sum")
    need(q(cert["numerator_bound"]) == bound, "uniform rotated numerator bound")
    k0 = integer(cert["half_slope_cutoff"], "half slope cutoff")
    need(prefactor*growth**k0 <= Fraction(1, 2) and cutoff >= k0, "denominator lower bound")
    candidate_bound = (2*bound).numerator//(2*bound).denominator
    need(cert["candidate_bound"] == candidate_bound, "complete integer candidate bound")
    candidates = cert["candidates"]
    need(len(candidates) == candidate_bound, "candidate coverage")
    identities = []
    for m, row in enumerate(candidates, start=1):
        need(row["value"] == m, "candidate order/coverage")
        terms = dict(numerator)
        add(terms, Fraction(1), Fraction(-m))
        add(terms, growth, m*prefactor)
        need(read_terms(row["power_sum"]) == terms, "candidate full denominator equation")
        if not terms:
            need("dominance" not in row, "identity/dominance separation")
            verify_identity(row["identity"], rotated, m, rotation)
            identities.append(m)
            continue
        need("identity" not in row, "false identity")
        d = row["dominance"]
        largest = max(terms)
        lead = terms[largest]
        other = {base: coefficient for base, coefficient in terms.items() if base != largest}
        total = sum((abs(x) for x in other.values()), Fraction(0))
        ratio = max(other, default=Fraction(0))/largest
        need(q(d["largest_root"]) == largest and q(d["leading_coefficient"]) == lead, "leading term")
        need(q(d["other_absolute_sum"]) == total and q(d["root_ratio"]) == ratio, "tail majorant")
        dk = integer(d["cutoff"], "dominance cutoff")
        need(0 <= ratio < 1 and 2*total*ratio**dk <= abs(lead), "strict eventual nonvanishing")
        need(cutoff >= dk, "global cutoff dominates each root equation")
    need(len(identities) <= 1 and cert["tail_identities"] == identities, "all infinite identity families")
    return {"regime": regime, "finite_cases": cutoff, "candidates": candidate_bound,
            "tail_identities": identities}


def suite_verify(artifact):
    if artifact["schema"] == "collatz-fixed-block-cycle-suite/v1":
        return {name: verify(cert) for name, cert in artifact["certificates"].items()}
    return {"input": verify(artifact)}


def controls(artifact):
    need("certificates" in artifact, "controls require suite")
    attack = artifact["certificates"]["alphabet_four_signed_cycle"]
    changes = []
    c = copy.deepcopy(attack); c["growth"] = "1/2"; changes.append(("wrong total slope", c))
    c = copy.deepcopy(attack); c["candidate_bound"] -= 1; changes.append(("wrong candidate bound", c))
    c = copy.deepcopy(attack); c["candidates"].pop(); changes.append(("omitted integer candidate", c))
    c = copy.deepcopy(attack); c["finite_cases"].pop(); changes.append(("missing finite parameter", c))
    c = copy.deepcopy(attack); c["finite_cases"][1]["fixed_point"] = "1/1"; changes.append(("false cycle quotient", c))
    c = copy.deepcopy(attack); c["candidates"][0]["dominance"]["leading_coefficient"] = "0/1"; changes.append(("altered leading coefficient", c))
    c = copy.deepcopy(attack); c["suffix_growth"][0] = "2/1"; changes.append(("uncontrolled rotated suffix", c))
    c = copy.deepcopy(artifact["certificates"]["trivial_cycle_identity"])
    c["candidates"][0]["identity"]["blocks"][0]["entry"] = 7
    changes.append(("false identity physical boundary", c))
    rejected = []
    for name, malformed in changes:
        try:
            verify(malformed)
        except (ValueError, KeyError, TypeError, ZeroDivisionError):
            rejected.append(name)
        else:
            raise ValueError(f"invalid certificate was accepted: {name}")
    return rejected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    artifact = json.loads(raw)
    report = {"success": True, "certificate_sha256": hashlib.sha256(raw).hexdigest(),
              "results": suite_verify(artifact),
              "scope": "complete parameter classification for the supplied fixed block schemas; no universal Collatz conclusion"}
    if args.self_test:
        report["invalid_certificates_rejected"] = controls(artifact)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
