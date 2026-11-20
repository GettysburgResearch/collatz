#!/usr/bin/env python3
"""Exact finite replay of V1--V5; universal statements are proved in the note."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def need(ok: bool, why: str) -> None:
    if not ok:
        raise ValueError(why)


def positive_odd(n: int) -> None:
    need(type(n) is int and n > 0 and n % 2 == 1, "positive ordinary odd input")


def shortcut(n: int) -> int:
    need(type(n) is int and n > 0, "positive ordinary integer input")
    return (3*n+1)//2 if n % 2 else n//2


def odd_step(n: int) -> tuple[int, int]:
    positive_odd(n)
    y, a = 3*n+1, 0
    while y % 2 == 0:
        y //= 2
        a += 1
    return y, a


def inverse_word(q: int, word: list[int]) -> int:
    positive_odd(q)
    for a in reversed(word):
        need(type(a) is int and a >= 1, "positive exact integer exponent")
        raw = (q << a)-1
        need(raw % 3 == 0, "legal ordinary inverse division")
        q = raw//3
        positive_odd(q)
    return q


def run_word(x: int, word: list[int], first_hit: bool = False) -> int:
    positive_odd(x)
    for a in word:
        need(type(a) is int and a >= 1, "positive exact integer exponent")
        if first_hit:
            need(x != 1, "premature first hit")
        x, actual = odd_step(x)
        need(a == actual, "literal exponent mismatch")
    return x


def a_target(r: int, b: int) -> list[int]:
    need(type(r) is int and r >= 1 and type(b) is int and b >= 4,
         "A-block domain")
    return [5,b-3] if r == 1 else [4]+[2]*(r-2)+[3,b-3]


def b_target(b: int) -> list[int]:
    need(type(b) is int and b >= 6, "B-block domain")
    return [1,2,5,b-5]


def compile_five(x: int, source: list[int]) -> dict:
    need(run_word(x,source,True) == 1, "supplied complete first-hit certificate")
    i, out, kinds = 0, [], []
    while i < len(source):
        start = i
        if source[i] == 2:
            while i < len(source) and source[i] == 2:
                i += 1
            r = i-start
            if i == len(source) or source[i] < 4:
                return {"status":"UNRESOLVED","consumed_letters":start}
            out += a_target(r,source[i])
            i += 1
            kinds.append("A")
        elif source[i:i+3] == [1,1,1] and i+3 < len(source) and source[i+3] >= 6:
            out += b_target(source[i+3])
            i += 4
            kinds.append("B")
        else:
            return {"status":"UNRESOLVED","consumed_letters":start}
    out.append(4)
    need(run_word(5*x,out,True) == 1, "produced first-hit certificate")
    need(len(out) == len(source)+1 and sum(out) == sum(source)+4,
         "exact output odd count and shortcut clock")
    return {"status":"CERTIFIED","word":out,"block_kinds":kinds}


def discrete_log_table(modulus: int, period: int) -> dict[int,int]:
    result, v = {}, 1
    for e in range(period):
        need(v not in result, "exact multiplicative order")
        result[v] = e
        v = 2*v % modulus
    need(v == 1, "exact multiplicative period")
    return result


def first_legal_b(q: int, kind: str, r: int = 0) -> tuple[int,int]:
    positive_odd(q)
    need(q % 3 != 0, "ternary-unit endpoint")
    if kind == "A":
        need(type(r) is int and r >= 1, "positive A run")
        modulus, period, lower = 3**(r+1), 2*3**r, 4
        table = discrete_log_table(modulus,period)
        residue = (2-table[q % modulus]) % period
    else:
        need(kind == "B", "recognized block kind")
        modulus, period, lower = 81, 54, 6
        table = discrete_log_table(modulus,period)
        residue = (table[(65*pow(q,-1,81)) % 81]-3) % 54
    b = lower+(residue-lower) % period
    return b,period


def pick_lift(q: int, kind: str, r: int = 0) -> tuple[int,list[int]]:
    b,period = first_legal_b(q,kind,r)
    for _ in range(3):
        word = [2]*r+[b] if kind == "A" else [1,1,1,b]
        x = inverse_word(q,word)
        if x % 3:
            return x,word
        b += period
    raise ValueError("unit lift missing in three periods")


def first_hit(n: int) -> tuple[int,int]:
    clock, odds = 0,0
    while n != 1 and clock < 10000:
        odds += n % 2
        n = shortcut(n)
        clock += 1
    need(n == 1, "explicit finite convergence control")
    return clock,odds


def run() -> dict:
    counts = {"paired_B_blocks":0,"literal_shortcut_edges":0,
              "cylinder_inputs_tested":0,"cylinder_members":0,
              "closed_first_hit_families":0,"compiled_certificates":0,
              "endpoint_partition_cases":0,"residual_family_cases":0,
              "one_then_threes_boundaries":0,"two_antecedent_identities":0,
              "exact_power_inequalities":0,"rejected_controls":0,
              "unresolved_controls":0}
    fixtures = []

    # Exercise every unit endpoint <= 999 and three distinct legal lifts.
    for q in range(1,1000,2):
        if q % 3 == 0:
            continue
        b0,period = first_legal_b(q,"B")
        for lift in (0,1,3):
            b = b0+period*lift
            source, target = [1,1,1,b],b_target(b)
            x = inverse_word(q,source)
            need(inverse_word(5*q,target) == 5*x, "B inverse identity")
            need(run_word(x,source,True) == q, "B source legality")
            need(run_word(5*x,target,True) == 5*q, "B target legality")
            need(x % 512 == 271 and 6*q <= x, "B cylinder and height")
            need(len(source) == len(target) and sum(source) == sum(target),
                 "B equal odd counts and clocks")
            a,c = x,5*x
            for _ in range(sum(source)):
                need(a > 1 and c > 1, "no premature shortcut hit")
                a,c = shortcut(a),shortcut(c)
                counts["literal_shortcut_edges"] += 2
            need((a,c) == (q,5*q), "literal B shortcut endpoints")
            counts["paired_B_blocks"] += 1
            fixtures.append((q,b,x))

    # Two-way finite cylinder census, including inputs divisible by three.
    for x in range(1,131072,2):
        q, word = x,[]
        for _ in range(4):
            q,a = odd_step(q)
            word.append(a)
        matches = word[:3] == [1,1,1] and word[3] >= 6
        need(matches == (x % 512 == 271), "two-way B cylinder census")
        if matches:
            need(q % 3 != 0 and 6*q <= x, "census smaller unit endpoint")
            counts["cylinder_members"] += 1
        counts["cylinder_inputs_tested"] += 1

    for k in range(13):
        raw = (1 << (54*k+31))-65
        need(raw % 81 == 0, "closed-family integrality")
        x = raw//81
        source = [1,1,1,54*k+28]
        need(x % 3 == 2*k % 3, "closed-family unit guard")
        result = compile_five(x,source)
        need(result["status"] == "CERTIFIED" and
             result["word"] == [1,2,5,54*k+23,4], "closed-family target")
        counts["closed_first_hit_families"] += 1
        counts["compiled_certificates"] += 1

    patterns = [[("B",0)],[("A",1),("B",0)],[("B",0),("A",2)],
                [("B",0),("A",4),("B",0),("A",3),("B",0)],
                [("B",0)]*12,[("A",1),("B",0)]*8]
    for pattern in patterns:
        q,word = 1,[]
        for kind,r in reversed(pattern):
            q,prefix = pick_lift(q,kind,r)
            word = prefix+word
        result = compile_five(q,word)
        need(result["status"] == "CERTIFIED" and
             result["block_kinds"] == [kind for kind,_ in pattern],
             "arbitrary mixed block composition")
        counts["compiled_certificates"] += 1
    need(compile_five(1,[])["word"] == [4], "empty source certificate")
    counts["compiled_certificates"] += 1

    # Check the endpoint class split and actual inverse progression growth.
    for q in range(1,1000,2):
        if q % 3 == 0:
            continue
        for r in range(2,7):
            b,period = first_legal_b(q,"A",r)
            x = inverse_word(q,[2]*r+[b])
            x_next = inverse_word(q,[2]*r+[b+period])
            need(x_next >= (x << period), "A progression growth")
            if q % 27 != 7:
                need(b >= 5, "A endpoint class exclusion")
                if q >= 5:
                    need(5*3**r*x >= 52*4**r*q,
                         "A q-not-seven class lower bound")
            elif q != 7:
                need(q >= 61 and 61*3**r*x >= 324*4**r*q,
                     "A q-seven class lower bound")
            counts["endpoint_partition_cases"] += 1
        b,period = first_legal_b(q,"B")
        x = inverse_word(q,[1,1,1,b])
        x_next = inverse_word(q,[1,1,1,b+period])
        need(x_next >= (x << period), "B progression growth")
        if q >= 5:
            need(81*x >= 499*q, "B global height coefficient")
        if q % 27 == 7:
            need(b % 18 == 12 and b >= 12, "B endpoint class exclusion")
            need(81*x >= 32755*q, "B restricted height coefficient")
        counts["endpoint_partition_cases"] += 1

    inequalities = [
        (3**21*500**25,4**21*393**25,"t<393/500"),
        (393*5,4*500,"393/500<4/5"),
        (32**25,64**21,"64^-s<1/32"),
        (5**25,7**21,"7^-s<1/5"),
        (5**21*7**25,52**21,"(5/52)^s<1/7"),
        (81**21*4**25,499**21,"(81/499)^s<1/4"),
        (61**21*4**25,324**21,"(61/324)^s<1/4"),
        (81**21*129**25,32755**21,"(81/32755)^s<1/129"),
        (129**25,2**(54*21),"2^(-54s)<1/129")]
    for lhs,rhs,name in inequalities:
        need(lhs < rhs,name)
        counts["exact_power_inequalities"] += 1
    case_a = Fraction(32,155)+Fraction(512,1085)+Fraction(8,31)
    case_b = Fraction(3144,3317)+Fraction(1,128)
    kappa = Fraction(405749,424576)
    need(case_a == Fraction(1016,1085) and case_a < kappa == case_b < 1,
         "complete exact rational renewal coefficient")
    need(1/(1-kappa) == Fraction(424576,18827), "finite energy factor")
    need(Fraction(16,21)+Fraction(2**54,6*(2**54-1)) < Fraction(14,15),
         "harmonic contraction")
    need(Fraction(1,24)+Fraction(1,256) == Fraction(35,768), "domain density")

    residuals = []
    for k in range(33):
        raw = (1 << (6*k+5))-5
        need(raw % 9 == 0, "residual-source integrality")
        z = raw//9
        need(z % 3 == 2*k % 3, "residual-source unit guard")
        need(run_word(z,[1,6*k+4],True) == 1, "residual first-hit source")
        n,odds = 5*z,0
        for _ in range(6*k+8):
            need(n > 1, "residual target has no premature hit")
            odds += n % 2
            n = shortcut(n)
            counts["literal_shortcut_edges"] += 1
        w_raw = 5*(3**(4*k+2)-1)
        need(w_raw % 8 == 0 and w_raw % 16 == 8, "residual exact final valuation")
        need(n == w_raw//8 and n >= 5 and n % 2 == 1, "exact residual endpoint")
        need(odds == 4*k+4, "exact pre-endpoint odd count")
        need(compile_five(z,[1,6*k+4])["status"] == "UNRESOLVED",
             "residual family outside compiler grammar")
        counts["residual_family_cases"] += 1
        counts["unresolved_controls"] += 1
        residuals.append((k,z,n,odds))

    for r in range(129):
        p = r+2
        positions = [0]+[1+3*j for j in range(r+1)]
        correction = sum(3**(p-1-j)*2**positions[j] for j in range(p))
        need(5*correction == 3**p+2**(3*r+4),
             "one-then-threes correction formula")
        value = 5*correction
        for j in range(p-1):
            need(value == 3**(p-j)+2**(3*r+4-j), "decoder induction formula")
            remainder = value-3**(p-1-j)
            need(remainder > 0 and remainder % 4 == 2,
                 "forced decoder exponent one")
            value = remainder//2
        need(value == 3+2**(2*r+3) and value != 1,
             "one-then-threes decoder rejection")
        counts["one_then_threes_boundaries"] += 1
    for q in range(3,10000,4):
        if q % 3 == 0:
            continue
        u,a = odd_step(q)
        need(a == 1 and u % 3 == 2 and u % 9 != 5,
             "two-antecedent domain")
        need(q == (2*u-1)//3 and shortcut(5*q) == 5*u-2,
             "two-antecedent ordinary reduction")
        counts["two_antecedent_identities"] += 1

    for x,word in [(5,[4]),(13,[3,4]),(3,[1,4])]:
        need(compile_five(x,word)["status"] == "UNRESOLVED",
             "valid unsupported word not certified")
        counts["unresolved_controls"] += 1
    controls = [lambda: b_target(5),lambda: b_target(6.0),
                lambda: odd_step(True),lambda: odd_step(-1),
                lambda: compile_five(271,[1,1,1,5]),
                lambda: compile_five(3,[True,4]),
                lambda: compile_five(3,[1.0,4]),
                lambda: compile_five(1,[2]),
                lambda: inverse_word(3,[1]),lambda: a_target(0,4)]
    for control in controls:
        try:
            control()
        except ValueError:
            counts["rejected_controls"] += 1
        else:
            raise ValueError("negative control accepted")

    zero_defect_controls = {str(q):first_hit(q) for q in (1,5,7,35)}
    return {"status":"PASS","counts":counts,
            "coefficient":{"case_q_not_7_mod_27":str(case_a),
                           "case_q_7_mod_27":str(case_b),
                           "kappa":str(kappa),
                           "energy_factor":str(1/(1-kappa))},
            "zero_defect_controls_clock_oddcount":zero_defect_controls,
            "residual_k1":{"source":227,"target_start":1135,
                           "endpoint":455,"clock":14,"odd_inputs":8},
            "fixture_sha256":hashlib.sha256(repr((fixtures,residuals)).encode()).hexdigest(),
            "grh_used":False,
            "scope":"Exact finite ordinary replay and exact rational comparisons for V1--V5. V1--V3 rederive or cross-check refreshed PR167--169 results; V4--V5 are scoped residual/boundary extensions. Universal claims rest on the written proof. No full five closure, residual-energy finiteness, or Collatz proof."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    raw = json.dumps(run(),indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(raw,encoding="utf-8")
    print(raw,end="")
