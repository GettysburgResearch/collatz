#!/usr/bin/env python3
"""Self-contained exact replay of the frozen 71-row directed certificate.

The replay proves its affine legality/coverage and a conditional-antecedent
height bound. It does not prove any open reverse-basin implication.
"""
import copy
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path
import hashlib
import json


def need(ok, message):
    if not ok:
        raise ValueError(message)


def run_certificate(data):
    rows = data["certificates"]
    bound = data["integer_unit_height_bound"]
    need(len(rows) == 71, "incomplete source list")
    period = lcm(*(row[0] for row in rows))
    need(period == 62208, "unexpected cover period")
    cover = set()
    maximum = Fraction(0)
    argmax = None
    total_moves = total_extra = longest = 0
    for modulus, residue, word in rows:
        need(modulus % 6 == 0 and gcd(residue, 6) == 1
             and 0 < residue < modulus, "invalid source progression")
        cover.update(range(residue, period, modulus))
        a, b = modulus, residue
        t0 = int(residue == 1)
        moves = extras = 0
        for position, token in enumerate(word.split()):
            need(a > 0 and b > 0, "nonpositive affine state")
            if token == "M":
                need(a % 18 == 0 and b % 18 == 9, "ineligible tripling source")
                upper_a, upper_b = 256*a//9, 256*b//9+1
                ratio = max(Fraction(upper_a, modulus),
                            Fraction(upper_a*t0+upper_b, modulus*t0+residue))
                need(ratio < bound, "conditional antecedent exceeds height bound")
                if ratio > maximum:
                    maximum = ratio
                    argmax = {"modulus": modulus, "residue": residue,
                              "word_position_zero_based": position,
                              "tripling_slope": a, "tripling_intercept": b,
                              "upper_slope": upper_a, "upper_intercept": upper_b}
                a *= 3
                b *= 3
                moves += 1
                extras += 1
            else:
                need(token[0] in "SI" and token[1:].isdigit(), "invalid move")
                h = int(token[1:])
                need(h >= 1, "invalid ordinary clock")
                if token[0] == "S":
                    need(a % 2 == 0 and b % 2 == 1, "forward source is not uniformly odd")
                    need(3*a % 2**h == 0 and (3*b+1) % 2**h == 0,
                         "nonintegral forward division")
                    a, b = 3*a//2**h, (3*b+1)//2**h
                else:
                    need(2**h*a % 3 == 0 and (2**h*b-1) % 3 == 0,
                         "nonintegral odd predecessor")
                    a, b = 2**h*a//3, (2**h*b-1)//3
                    need(a % 2 == 0 and b % 2 == 1, "inverse output is not uniformly odd")
                moves += h
        need(a > 0 and b > 0 and a % 3 == 0 and b % 3 != 0, "target is not a positive ternary unit")
        need(25*a <= 24*modulus, "contraction slope failed")
        need(25*(a*t0+b) <= 24*(modulus*t0+residue), "contraction endpoint failed")
        total_moves += moves
        total_extra += extras
        longest = max(longest, moves)
    need(cover == {r for r in range(period) if gcd(r, 6) == 1}, "incomplete ternary-unit cover")
    need((total_moves, total_extra, longest) == (3974, 284, 198), "source certificate totals changed")
    need(maximum == Fraction(2025217, 23), "exact peak changed")
    need(data["integer_all_source_height_bound"] == 2*bound == 176106, "wrong all-source bound")
    return {"source_classes": len(rows), "unit_residues": len(cover),
            "expanded_moves": total_moves, "eligible_triplings": total_extra,
            "maximum_expanded_moves": longest,
            "exact_peak": str(maximum), "peak_location": argmax,
            "unit_height_bound": bound, "all_source_height_bound": 2*bound}


def binary_replacement():
    def step(a, b):
        need(a % 2 == 0, "replacement parity varies")
        return (a//2, b//2) if b % 2 == 0 else (3*a//2, (3*b+1)//2)
    def run(a, b, clocks):
        for _ in range(clocks):
            a, b = step(a, b)
        return a, b
    # h=2t+1 checks both infinite families, with actual ordinary steps.
    need(run(128, 65, 6) == (54, 28), "left replacement connection")
    need(run(512, 257, 8) == (162, 82), "right replacement connection")
    need(run(18, 9, 1) == run(54, 28, 1), "left common endpoint")
    need(run(54, 27, 1) == run(162, 82, 1), "right common endpoint")


def cutoff():
    C = 176106
    need(4**42 > C*3**42, "coarse fourth-valuation cutoff")
    even_delta = 2**78-81*C*3**34-175
    odd_delta = 2**85-162*C*3**38-81*C-175
    need(even_delta > 0 and odd_delta > 0, "parity-specific cutoff")
    return {"coarse_maximum_fourth_valuation": 86,
            "even_first_excluded_r": 34, "even_first_excluded_c": 72,
            "even_cutoff_delta": even_delta,
            "odd_first_excluded_r": 38, "odd_first_excluded_c": 79,
            "odd_cutoff_delta": odd_delta}


def rank_four_control():
    n = 3**26
    states = [n]
    for _ in range(10000):
        if n == 1:
            break
        n = n//2 if n % 2 == 0 else (3*n+1)//2
        states.append(n)
    need(n == 1, "finite rank-four certificate did not reach 1")
    need((len(states)-1, sum(n % 2 for n in states[:-1]), max(states))
         == (219, 112, 16286310253592), "rank-four trajectory changed")
    return {"source": states[0], "shortcut_clocks": len(states)-1,
            "odd_inputs": sum(n % 2 for n in states[:-1]), "peak": max(states),
            "trajectory_sha256": hashlib.sha256(json.dumps(states, separators=(",", ":")).encode()).hexdigest()}


def rank_five_controls():
    H = 176106
    c1_delta = 2**77-653-243*H*3**32
    c3_delta = 2**193-1037-243*H*3**91
    need(c1_delta == 71818029920988665229141 and c1_delta > 0,
         "rank-five c=1 source-height cutoff")
    need(c3_delta == 12554202350266279230985313864847138776593601623775633598729
         and c3_delta > 0, "rank-five c=3 source-height cutoff")
    need(4**81 > 3**81, "rank-five progression induction")
    n = 3**10
    states = [n]
    for _ in range(10000):
        if n == 1:
            break
        n = n//2 if n % 2 == 0 else (3*n+1)//2
        states.append(n)
    need(n == 1, "finite rank-five residual did not reach 1")
    need((len(states)-1, sum(n % 2 for n in states[:-1]), max(states))
         == (89, 46, 1135052), "rank-five residual trajectory changed")
    return {"c1_first_gap": 70, "c1_cutoff_delta": c1_delta,
            "c3_first_uniform_gap": 184, "c3_cutoff_delta": c3_delta,
            "remaining_c3_source": states[0], "remaining_c3_clocks": 89,
            "remaining_c3_odd_inputs": 46, "remaining_c3_peak": 1135052}


def negative_controls(data):
    corruptions = []
    bad = copy.deepcopy(data)
    bad["certificates"] = []
    corruptions.append(bad)
    bad = copy.deepcopy(data)
    bad["certificates"][0][2] = "S3"
    corruptions.append(bad)
    bad = copy.deepcopy(data)
    bad["integer_unit_height_bound"] = 88052
    corruptions.append(bad)
    rejected = 0
    for bad in corruptions:
        try:
            run_certificate(bad)
        except ValueError:
            rejected += 1
    need(rejected == len(corruptions), "corrupt certificate accepted")
    return rejected


def main():
    data = json.loads(Path(__file__).with_name("deep_reverse_certificate.json").read_text())
    result = run_certificate(data)
    binary_replacement()
    result.update({"scope": "conditional least-failure height and rank exclusions; Collatz and the remaining guarded cover are unproved",
                   "cutoff": cutoff(), "rank_four_control": rank_four_control(),
                   "rank_five_controls": rank_five_controls(),
                   "invalid_fixtures_rejected": negative_controls(data),
                   "source_author_implementation_imported": False})
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
