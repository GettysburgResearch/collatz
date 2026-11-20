#!/usr/bin/env python3
"""Exact checks for UNBOUNDED_FIRST_ONE_TRANSPORT.md; no external imports.

The mathematical proof handles the infinite families. This program replays
ordinary paths and certifies every row of the finite rational coefficient
bound. It deliberately imports no earlier project checker.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from pathlib import Path


class CheckFailure(RuntimeError):
    pass


def need(condition, message):
    if not condition:
        raise CheckFailure(message)


def valuation(n, prime):
    need(n != 0, "valuation of zero")
    n = abs(n)
    if prime == 2:
        return (n & -n).bit_length() - 1
    exponent = 0
    while n % prime == 0:
        exponent += 1
        n //= prime
    return exponent


def odd_step(n):
    need(isinstance(n, int) and n > 0 and n % 2 == 1, "invalid odd input")
    value = 3 * n + 1
    exponent = valuation(value, 2)
    return value >> exponent, exponent


def correction(word):
    need(len(word) > 0 and all(isinstance(a, int) and a > 0 for a in word),
         "invalid exponent word")
    p = len(word)
    clock = 0
    value = 0
    for i, exponent in enumerate(word):
        value += 3 ** (p - 1 - i) * 2 ** clock
        clock += exponent
    return value, clock, p


def inverse(word, endpoint):
    value = endpoint
    for exponent in reversed(word):
        need(exponent >= 1, "nonpositive inverse exponent")
        numerator = (value << exponent) - 1
        need(numerator % 3 == 0, "nonintegral inverse")
        value = numerator // 3
        need(value > 0 and value % 2, "nonpositive or even inverse")
    return value


def replay(start, word, first_hit=False):
    need(start > 0 and start % 2, "invalid replay start")
    value = start
    if first_hit and start == 1:
        need(not word, "nonempty first-hit word at one")
    for index, exponent in enumerate(word):
        need(isinstance(exponent, int) and exponent >= 1, "malformed exponent")
        if first_hit:
            need(value != 1, "early first hit")
        value, actual = odd_step(value)
        need(actual == exponent, "incorrect actual division exponent")
    if first_hit:
        need(value == 1, "incomplete first-hit certificate")
    return value


def new_block(r, a, b):
    need(r >= 3 and a in (2, 4) and b >= 4, "invalid new-block parameters")
    source = (1,) + (2,) * r + (1, a, b)
    middle = (3, 3, 1) if a == 2 else (3, 1, 5)
    target = (1, 1, 4) + (2,) * (r - 3) + middle + (b - 3,)
    return source, target


def old_ladder(r, b):
    need(r >= 1 and b >= 4, "invalid ladder parameters")
    source = (2,) * r + (b,)
    target = (5, b - 3) if r == 1 else (4,) + (2,) * (r - 2) + (3, b - 3)
    return source, target


def old_short(a, b):
    need(a in (1, 2, 4) and b >= (6 if a == 1 else 4), "invalid short block")
    prefix, delta = {1: ((1, 2, 5), 5), 2: ((1, 5, 1), 3),
                     4: ((1, 3, 5), 3)}[a]
    return (1, 1, a, b), prefix + (b - delta,)


def consume(word, offset):
    """Explicit dictionary parser; a strict subclass of PR167 HT2."""
    rest = word[offset:]
    if not rest:
        return None
    if rest[0] == 2:
        r = 0
        while r < len(rest) and rest[r] == 2:
            r += 1
        if r < len(rest) and rest[r] >= 4:
            return old_ladder(r, rest[r])
        return None
    if len(rest) >= 4 and rest[:2] == (1, 1):
        a, b = rest[2:4]
        if a in (1, 2, 4) and b >= (6 if a == 1 else 4):
            return old_short(a, b)
        return None
    if rest[0] == 1:
        r = 0
        while r + 1 < len(rest) and rest[r + 1] == 2:
            r += 1
        if r >= 3 and len(rest) >= r + 4:
            tail = rest[r + 1:r + 4]
            if tail[0] == 1 and tail[1] in (2, 4) and tail[2] >= 4:
                return new_block(r, tail[1], tail[2])
    return None


def compile_word(start, word):
    word = tuple(word)
    replay(start, word, first_hit=True)
    offset = 0
    target = ()
    while offset < len(word):
        block = consume(word, offset)
        if block is None:
            return None
        source_piece, target_piece = block
        need(word[offset:offset + len(source_piece)] == source_piece,
             "parser source mismatch")
        target += target_piece
        offset += len(source_piece)
    target += (4,)
    replay(5 * start, target, first_hit=True)
    need(len(target) == len(word) + 1, "compiler rank mismatch")
    need(sum(target) == sum(word) + 4, "compiler clock mismatch")
    return target


def odd_minimum(c, modulus):
    value = c
    while value < 5 or value % 2 == 0:
        value += modulus
    return value


@lru_cache(maxsize=None)
def least_power(c, rhs, modulus, offset, minimum, period):
    current = pow(2, minimum + offset, modulus) * c % modulus
    found = []
    for b in range(minimum, minimum + period):
        if current == rhs % modulus:
            found.append(b)
        current = 2 * current % modulus
    need(len(found) == 1, "power class not unique")
    return found[0]


def gamma_inputs(c):
    """Reconstruct PR167 ER2, retaining its coarse endpoint q mod81."""
    q = odd_minimum(c, 81)
    direct = []
    for r in (1, 2):
        period = 2 * 3 ** r
        b = least_power(c, 4, 3 ** (r + 1), 0, 4, period)
        B = 4 ** (r + 1) - 3 ** (r + 1)
        A = F(3 ** (r + 1), 1) / (2 ** (2 * r + b) - F(B, q))
        direct.append((A, period))
    b3 = least_power(c, 4, 81, 0, 4, 54)
    tail = F(3, 1) / (2 ** b3 - F(4, q))
    for a, B, minimum in ((1, 65, 6), (2, 73, 4), (4, 121, 4)):
        b = least_power(c, B, 81, a + 2, minimum, 54)
        G = F(81, 1) / (2 ** (a + 2 + b) - F(B, q))
        direct.append((G, 54))
    return direct, tail


GRID = 10 ** 9


@lru_cache(maxsize=None)
def upper_power_21_25(value):
    """Least k/GRID above value^(21/25), by integer inequalities only."""
    need(value >= 0, "negative rational power")
    if value == 0:
        return F(0)
    numerator = value.numerator ** 21 * GRID ** 25
    denominator = value.denominator ** 21
    lo, hi = 0, GRID
    while hi ** 25 * denominator < numerator:
        hi *= 2
    while lo < hi:
        middle = (lo + hi) // 2
        if middle ** 25 * denominator >= numerator:
            hi = middle
        else:
            lo = middle + 1
    need(lo ** 25 * denominator >= numerator, "power enclosure too low")
    need(lo == 0 or (lo - 1) ** 25 * denominator < numerator,
         "power enclosure not least grid point")
    return F(lo, GRID)


@lru_cache(maxsize=None)
def gamma(c, exponent):
    direct, tail = gamma_inputs(c)
    power = (lambda v: v) if exponent == 1 else upper_power_21_25
    result = F(0)
    for A, period in direct:
        denominator = 1 - power(F(1, 2 ** period))
        need(denominator > 0, "nonpositive geometric denominator")
        result += power(A) / denominator
    z = power(F(3, 4))
    result += power(tail) * z ** 3 / ((1 - z) * (1 - power(F(1, 2 ** 54))))
    return result


def new_fiber_inputs(c):
    q = odd_minimum(c, 729)
    out = []
    for a, C in ((2, 100), (4, 148)):
        b = least_power(c, C, 729, a + 2, 4, 486)
        H = 81 * F(3, 4) ** 3 / (2 ** (b + a + 2) - F(C, q))
        need(H > 0, "nonpositive new fiber coefficient")
        out.append((a, b, H))
    return q, out


def ceiling_grid(value):
    return (value.numerator * GRID + value.denominator - 1) // value.denominator


def coefficient_certificate():
    rows = []
    maximum = {1: (F(-1), None), F(21, 25): (F(-1), None)}
    for c in range(1, 729):
        if c % 3 == 0:
            continue
        q, inputs = new_fiber_inputs(c)
        bounds = {}
        for exponent, threshold in ((1, F(5, 8)), (F(21, 25), F(91, 100))):
            power = (lambda v: v) if exponent == 1 else upper_power_21_25
            denominator = 1 - power(F(1, 2 ** 486))
            value = gamma(c % 81, exponent) + sum(power(H) for _, _, H in inputs) / denominator
            need(value < threshold, "coefficient bound fails")
            if value > maximum[exponent][0]:
                maximum[exponent] = value, c
            bounds[str(exponent)] = ceiling_grid(value)
        rows.append({"c": c, "least_odd_q": q,
                     "least_b_a2": inputs[0][1], "least_b_a4": inputs[1][1],
                     "harmonic_upper_grid": bounds["1"],
                     "power_21_25_upper_grid": bounds["21/25"]})
    need(len(rows) == 486, "incomplete unit residue certificate")
    return {
        "grid_denominator": GRID,
        "residue_modulus": 729,
        "rows": rows,
        "maxima": {
            str(exponent): {"c": c, "upper_grid": ceiling_grid(value),
                            "upper_fraction": str(value)}
            for exponent, (value, c) in maximum.items()
        },
    }


def legal_endpoint_for_word(word, multiple=0):
    B, clock, p = correction(word)
    modulus = 3 ** p
    q = B * pow(2 ** clock, -1, modulus) % modulus
    if q == 0:
        q += modulus
    if q % 2 == 0:
        q += modulus
    q += 2 * multiple * modulus
    x = inverse(word, q)
    return x, q


def prepend_block(endpoint, kind, parameter, r=0):
    """Construct integral first-hit controls; never treats this search as proof."""
    if kind == "new":
        maker = lambda b: new_block(r, parameter, b)
        minimum = 4
    elif kind == "ladder":
        maker = lambda b: old_ladder(r, b)
        minimum = 4
    else:
        maker = lambda b: old_short(parameter, b)
        minimum = 6 if parameter == 1 else 4
    probe, _ = maker(minimum)
    B, clock, p = correction(probe)
    offset = clock - minimum
    period = 2 * 3 ** (p - 1)
    b = least_power(endpoint % (3 ** p), B, 3 ** p, offset, minimum, period)
    for adjustment in range(3):
        source, target = maker(b + adjustment * period)
        value = inverse(source, endpoint)
        if value % 3 != 0:
            return value, source, target
    raise CheckFailure("unit source not found in three lifts")


def check_paths_and_algebra():
    algebra_rows = 0
    block_replays = 0
    cylinder_replays = 0
    for r in range(3, 65):
        for a in (2, 4):
            for b in (4, 5, 8, 17):
                source, target = new_block(r, a, b)
                B, L, p = correction(source)
                Bt, Lt, pt = correction(target)
                C = 84 + 2 ** (a + 2)
                need(B == C * 4 ** r - 27 * 3 ** r, "source correction formula")
                need(Bt == 5 * B and Lt == L and pt == p, "paired correction mismatch")
                need(p == r + 4 and L == 2 * r + b + a + 2, "resource formula")
                algebra_rows += 1
                if r <= 14:
                    for multiple in (0, 1, 7):
                        x, q = legal_endpoint_for_word(source, multiple)
                        need(replay(x, source) == q, "source replay endpoint")
                        need(replay(5 * x, target) == 5 * q, "target replay endpoint")
                        need(7 * q <= x, "strict endpoint contraction")
                        need(valuation(2 ** (b + a + 2) * q - C, 3) == r + 3,
                             "unique ternary run valuation")
                        block_replays += 1
            if r <= 8:
                B = (84 + 2 ** (a + 2)) * 4 ** r - 27 * 3 ** r
                modulus = 2 ** (2 * r + a + 6)
                rho = (-B * pow(3 ** (r + 4), -1, modulus)) % modulus
                for lift in range(16):
                    x = rho + lift * modulus
                    value = x
                    word = []
                    for _ in range(r + 4):
                        value, exponent = odd_step(value)
                        word.append(exponent)
                    need(tuple(word[:-1]) == (1,) + (2,) * r + (1, a), "cylinder fixed prefix")
                    need(word[-1] >= 4, "cylinder final valuation")
                    need(valuation(3 * x - 1, 2) == 2 * r + 2, "binary run separator")
                    need(7 * value <= x, "cylinder endpoint contraction")
                    need(replay(5 * x, new_block(r, a, word[-1])[1]) == 5 * value,
                         "cylinder target replay")
                    cylinder_replays += 1
    need(F(1, 12288) + F(1, 49152) == F(5, 49152), "new cylinder density")
    need(F(85, 1536) + F(5, 24576) == F(455, 8192), "combined relative density")

    # The new seed equations are checked as exact rational affine functions.
    seed_rows = []
    for a in (2, 4):
        for b in (4, 7, 15):
            source = (1, a, b)
            target = ((3, 3, 1) if a == 2 else (3, 1, 5)) + (b - 3,)
            Bs, Ls, ps = correction(source)
            Bt, Lt, pt = correction(target)
            need(F(5 * 2 ** Lt, 3 ** pt) == F(10, 3) * F(2 ** Ls, 3 ** ps),
                 "seed linear coefficient")
            need(F(-Bt, 3 ** pt) - 1 == F(10, 3) * (F(-Bs, 3 ** ps) - 1),
                 "seed constant coefficient")
            seed_rows.append({"a": a, "b": b, "source_correction": Bs,
                              "target_correction": Bt})

    return {"parametric_correction_controls": algebra_rows,
            "literal_paired_block_replays": block_replays,
            "literal_cylinder_replays": cylinder_replays,
            "seed_controls": seed_rows}


def check_compiler_and_controls():
    specifications = [
        [("new", 2, 3)],
        [("new", 4, 4)],
        [("new", 2, 3), ("short", 1, 0), ("ladder", 0, 2)],
        [("short", 2, 0), ("new", 4, 3), ("short", 4, 0), ("ladder", 0, 1)],
    ]
    mixed = []
    for spec in specifications:
        value = 1
        source = ()
        for kind, parameter, r in reversed(spec):
            value, prefix, _ = prepend_block(value, kind, parameter, r)
            source = prefix + source
        target = compile_word(value, source)
        need(target is not None, "mixed compiler unresolved")
        mixed.append({"source_bits": value.bit_length(), "source_word": list(source),
                      "target_word": list(target), "source_rank": len(source),
                      "source_clock": sum(source), "target_rank": len(target),
                      "target_clock": sum(target)})
    need(compile_word(1, ()) == (4,), "empty compiler base")
    need(compile_word(7, (1, 1, 2, 3, 4)) is None, "valid unresolved seven")
    need(compile_word(17, (2, 3, 4)) is None, "valid unresolved seventeen")
    rejected = []
    for name, start, word in [
            ("zero_exponent", 1, (0,)),
            ("wrong_source_gap", 7, (1, 2, 2, 3, 4)),
            ("premature_one", 5, (4, 2)),
            ("incomplete_witness", 7, (1, 1))]:
        try:
            compile_word(start, word)
        except CheckFailure:
            rejected.append(name)
        else:
            raise CheckFailure("malformed witness accepted")
    corrupted_targets = 0
    for r, a, b in ((3, 2, 4), (7, 4, 9), (15, 2, 6)):
        source, target = new_block(r, a, b)
        x, _ = legal_endpoint_for_word(source)
        bad = list(target)
        bad[1] += 1
        try:
            replay(5 * x, bad)
        except CheckFailure:
            corrupted_targets += 1
        else:
            raise CheckFailure("corrupted target accepted")
    return {"mixed_first_hit_certificates": mixed,
            "valid_unresolved_controls": [7, 17],
            "malformed_controls_rejected": rejected,
            "corrupted_target_controls_rejected": corrupted_targets}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="unbounded-first-one-report.json")
    args = parser.parse_args()
    report = {
        "status": "PASS; scoped identities and renewal only; Collatz remains open",
        "proof_file": "UNBOUNDED_FIRST_ONE_TRANSPORT.md",
        "source_pins": {
            "PR166": "5996b9f525ca50978bc34f423192c36a87765bf3",
            "PR167": "e83cc8b35ad614c616df7c00318cc9645a174c34",
            "PR146": "fd991063721e9c157d318e40bb20131762f7d750",
        },
        "paths_and_algebra": check_paths_and_algebra(),
        "compiler": check_compiler_and_controls(),
        "coefficient_certificate": coefficient_certificate(),
    }
    proof = Path(__file__).with_name("UNBOUNDED_FIRST_ONE_TRANSPORT.md")
    report["proof_sha256"] = hashlib.sha256(proof.read_bytes()).hexdigest()
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    Path(args.output).write_text(encoded)
    summary = {
        "status": report["status"],
        "parametric_correction_controls": report["paths_and_algebra"]["parametric_correction_controls"],
        "literal_block_replays": report["paths_and_algebra"]["literal_paired_block_replays"],
        "literal_cylinder_replays": report["paths_and_algebra"]["literal_cylinder_replays"],
        "mixed_first_hit_certificates": len(report["compiler"]["mixed_first_hit_certificates"]),
        "coefficient_rows": len(report["coefficient_certificate"]["rows"]),
        "coefficient_maxima": report["coefficient_certificate"]["maxima"],
        "report_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
