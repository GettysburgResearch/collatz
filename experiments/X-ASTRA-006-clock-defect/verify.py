#!/usr/bin/env python3
"""Separate physical replay and exact-affine verification; does not import run.py."""
from __future__ import annotations
import argparse
import copy
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

DEPTH = 18
SCOPE = "finite corpus; unbounded ordinary heights, fixed h=2; full closure OPEN"


def check(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def val(a: int, p: int = 3) -> int:
    check(a != 0, "zero valuation")
    a = abs(a)
    b = 1
    while a % (b*p) == 0:
        b *= p
    e = 0
    while b > 1:
        b //= p
        e += 1
    return e


def height(n: int) -> int:
    check(n >= 1, "nonpositive integer")
    z = 2*n+1
    return z*z // 3**val(z)


def walk(n: int, count: int) -> tuple[int, str]:
    word = []
    for _ in range(count):
        if n % 2:
            word.append("1")
            n = (3*n+1)//2
        else:
            word.append("0")
            n //= 2
    return n, "".join(word)


def bezout(a: int, b: int) -> tuple[int, int, int]:
    if not b:
        return a, 1, 0
    g, x, y = bezout(b, a % b)
    return g, y, x-(a//b)*y


def combine(a: int, m: int, b: int, modulus: int) -> int:
    g, inverse, _ = bezout(m, modulus)
    check(g == 1, "noncoprime CRT")
    return a + m*((b-a)*inverse % modulus)


def depth_two_bases(res: int, j: int) -> list[int]:
    ans = [res + t*2**j for t in range(27) if val(2*(res+t*2**j)+1) == 2]
    check(len(ans) == 2, "exact depth-two base coverage")
    return ans


def physical_data(res: int, j: int) -> tuple[str, int, int, int]:
    y, word = walk(res, j)
    q = word.count("1")
    y2, word2 = walk(res+2**j, j)
    check(word == word2 and y2-y == 3**q, "affine cylinder slope")
    A = 2**j*y-3**q*res
    return word, q, A, 2*A+2**j-3**q


def test_rule(res: int, j: int, kind: str) -> dict | None:
    word, q, A, B = physical_data(res, j)
    D = B if kind == "forward" else B-2**(j-1)
    if kind != "forward":
        trailing = len(word)-len(word.rstrip("0"))
        if trailing < 2 or trailing % 2 or D == 0 or D % 3:
            return None
    delta = val(D)
    if delta >= q+2:
        return None
    n = depth_two_bases(res, j)[0]
    y, _ = walk(n, j)
    y2, _ = walk(n+27*2**j, j)
    if kind == "forward":
        x, x2 = y, y2
        hx = delta
    else:
        if y % 3 != 2 or y2 % 3 != 2:
            return None
        x, x2 = (2*y-1)//3, (2*y2-1)//3
        hx = delta-1
    if x < 1 or val(2*x+1) != hx or height(x) >= height(n):
        return None
    slope = Fraction(x2-x, 27*2**j)
    limiting = Fraction(9, 3**hx)*slope*slope
    if limiting >= 1:
        return None
    return dict(word=word, residue=res, j=j, q=q, A=A, B=B, kind=kind,
                D=D, delta=delta, hx=hx, minimum_n=n, witness=x,
                limit_num=limiting.numerator, limit_den=limiting.denominator)


def reconstruct_rules() -> list[dict]:
    rules = []
    for j in range(4, DEPTH+1):
        for res in range(11, 2**j, 16):
            if any(res % 2**r["j"] == r["residue"] for r in rules):
                continue
            row = test_rule(res, j, "forward") or test_rule(res, j, "odd_predecessor")
            if row:
                rules.append(row)
    return rules


def samples(rules: list[dict]) -> list[list[int]]:
    rows = []
    for i, r in enumerate(rules):
        for base in depth_two_bases(r["residue"], r["j"]):
            for t in (0, 1, 7, 10**6):
                n = base+27*2**r["j"]*t
                y, w = walk(n, r["j"])
                check(w == r["word"] and val(2*n+1) == 2, "source guards")
                if r["kind"] == "forward":
                    x = y
                else:
                    check(y % 3 == 2, "odd inverse integrality")
                    x = (2*y-1)//3
                    check(walk(x, 1) == (y, "1"), "actual odd inverse")
                check(height(x) < height(n) and val(2*x+1) == r["hx"], "rank guard")
                rows.append([i, n, x, y])
    return rows


def inverse_words(k: int) -> list[tuple]:
    ans = []
    for bits in itertools.product("01", repeat=k):
        w = "".join(bits)
        a, b = Fraction(1), Fraction(0)
        for bit in reversed(w):
            if bit == "0":
                a, b = 2*a, 2*b
            else:
                a, b = 2*a/3, (2*b-1)/3
        q = w.count("1")
        A = -b*3**q
        check(A.denominator == 1, "inverse affine constant")
        ans.append((w, a, b, q, 2*int(A)+2**k-3**q))
    return ans


def rigidity_tests() -> tuple[list, int, int]:
    templates = [inverse_words(k) for k in range(9)]
    rows, pairs, lower = [], 0, 0
    for M in range(1, 9):
        H = next(h for h in range(3*M+1) if 3**h >= 12**M)
        for label, res in (("odd_run", 2**M-1), ("mixed", 21 % 2**M)):
            for unit in (1, 2):
                modulus = 3**(H+1)
                b = ((unit*3**H-1)*bezout(2, modulus)[1]) % modulus
                n = combine(res, 2**M, b, modulus)+2**M*modulus
                local_pairs = local_lower = 0
                for j in range(M+1):
                    y, v = walk(n, j)
                    qv = v.count("1")
                    Bv = 2*(2**j*y-3**qv*n)+2**j-3**qv
                    for k in range(M+1):
                        found = set()
                        for w, a, b, qw, Bw in templates[k]:
                            x = a*y+b
                            if x.denominator != 1 or x <= 0:
                                continue
                            x = int(x)
                            check(walk(x, k) == (y, w), "backward word guard")
                            check(x not in found, "duplicate fixed-time inverse")
                            found.add(x)
                            d = min(j, k)
                            D = 2**(k-d)*Bv-2**(j-d)*Bw
                            check(abs(D) < 3**M, "defect bound")
                            if D:
                                check(3*height(x) > 4*height(n), "defect rank barrier")
                            if height(x) < height(n):
                                check(j == k and Bv == Bw and qw > qv, "short-clock classification")
                                check(2*n+1 == 3**(qw-qv)*(2*x+1), "exact strip")
                                check(label != "odd_run", "all-odd exclusion")
                                local_lower += 1
                            local_pairs += 1
                rows.append([M, H, label, unit, n, local_pairs, local_lower])
                pairs += local_pairs
                lower += local_lower
    return rows, pairs, lower


def cost_tests() -> tuple[list, int]:
    rows, steps = [], 0
    for H in (3, 6, 12, 24, 48, 96):
        a = 4*H
        M = max(m for m in range(H+1) if 12**m <= 3**H)
        for unit in (1, 2):
            mod = 3**(H+1)
            b = (unit*3**H-1)*bezout(2, mod)[1] % mod
            base = combine(2**a-1, 2**(a+1), b, mod)
            for t in (1, 2):
                n = base+t*2**(a+1)*mod
                check(val(2*n+1) == H and val(n+1, 2) == a, "cost source")
                y, odds = n, 0
                while y % 2:
                    y = (3*y+1)//2
                    odds += 1
                y //= 2
                check(odds == a and val(2*y+1) == a, "whole odd-run endpoint")
                ratio = Fraction(height(y), height(n))
                check(ratio == Fraction(243, 256)**H*Fraction(n+1, 2*n+1)**2, "exact adaptive ratio")
                check(ratio < 1, "adaptive reduction")
                rows.append([H, a, M+1, unit, t, n, y])
                steps += a+1
    return rows, steps


def named_tests() -> list:
    rows = []
    for t in (0, 1, 7, 1000, 10**30):
        n, x = 859+1769472*t, 517+1062882*t
        y, v = walk(n, 16)
        check(v == "1101110101011100" and walk(x, 1) == (y, "1"), "named diagram")
        check(y == 776+1594323*t and 8*height(x) < 3*height(n), "named rank bound")
        rows.append([2, t, n, x])
    for H in (3, 4, 10, 30):
        for unit in (1, 2):
            mod = 3**(H+1)
            b = (unit*3**H-1)*bezout(2, mod)[1] % mod
            n = combine(859, 2**16, b, mod)+2**16*mod
            y, v = walk(n, 16)
            x = (2*y-1)//3
            check(v == "1101110101011100" and walk(x, 1) == (y, "1"), "high-depth physical guard")
            check(height(x) > height(n), "all-height extension must fail")
            rows.append([H, unit, n, x])
    return rows


def sha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def reconstruct() -> tuple[dict, dict]:
    rules = reconstruct_rules()
    covered = set()
    for r in rules:
        covered.update(range(r["residue"], 2**DEPTH, 2**r["j"]))
    residual = sorted(set(range(11, 2**DEPTH, 16))-covered)
    ordinary = sorted(combine(r, 2**DEPTH, b, 81) for r in residual for b in (4, 22, 31, 49, 58))
    rr = samples(rules)
    rg, pairs, lower = rigidity_tests()
    costs, steps = cost_tests()
    full = dict(rules=rules, residual_dyadic=residual, residual_ordinary=ordinary, rule_replays=rr,
                rigidity=rg, cost_family=costs, named_cases=named_tests())
    report = dict(schema=1, scope=SCOPE, depth=DEPTH, rules=len(rules),
                  forward_rules=sum(r["kind"] == "forward" for r in rules),
                  asymmetric_rules=sum(r["kind"] == "odd_predecessor" for r in rules),
                  covered_dyadic=len(covered), residual_dyadic=len(residual),
                  old_residual_modulus=81*2**DEPTH, old_residual_classes=5*len(residual), first_old_residual=ordinary[0],
                  rule_replays=len(rr), rigidity_cases=len(rg), rigidity_pairs=pairs,
                  homogeneous_lower_pairs=lower, cost_cases=len(costs), cost_forward_steps=steps,
                  named_cases=len(full["named_cases"]),
                  parts={k:sha(v) for k,v in full.items()}, full_sha256=sha(full))
    report["semantic_sha256"] = sha(report)
    return report, full


def validate(actual: dict, expected: dict) -> None:
    bare = {k:v for k,v in actual.items() if k != "semantic_sha256"}
    check(sha(bare) == actual.get("semantic_sha256"), "invalid report seal")
    check(actual == expected, "independent mathematical/coverage reconstruction mismatch")


def self_test(expected: dict) -> None:
    changes = [("scope", "Collatz proved"), ("depth", 17), ("rules", 262),
               ("covered_dyadic", 15981), ("residual_dyadic", 0),
               ("rigidity_pairs", expected["rigidity_pairs"]-1),
               ("cost_forward_steps", expected["cost_forward_steps"]-1),
               ("parts", {**expected["parts"], "rules": "0"*64})]
    for key, value in changes:
        bad = copy.deepcopy(expected)
        bad[key] = value
        bad["semantic_sha256"] = sha({k:v for k,v in bad.items() if k != "semantic_sha256"})
        try:
            validate(bad, expected)
        except ValueError as error:
            check("reconstruction" in str(error), "tamper rejected only by hash")
        else:
            raise ValueError("resealed tamper accepted")
    print("RESEALED TAMPER TESTS PASS", len(changes))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--full-output", type=Path)
    args = parser.parse_args()
    expected, full = reconstruct()
    validate(json.loads(args.report.read_text()), expected)
    if args.full_output:
        args.full_output.write_text(json.dumps(full, sort_keys=True, separators=(",", ":"))+"\n")
    if args.self_test:
        self_test(expected)
    print("SEPARATE REPLAY PASS", expected["semantic_sha256"])


if __name__ == "__main__":
    main()
