#!/usr/bin/env python3
"""Exact local replays for adaptive one-demand tripling reductions.

This does not prove that the guarded reductions cover every integer.
All arithmetic is integer or Fraction arithmetic. No third-party dependency.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


ROWS = (
    (17, 48, "IMOEOE", "OOEEI", (32, 11), (54, 19), 0),
    (25, 64, "OEOOEEIM", "OOEOEEI", (18, 7), (54, 21), 0),
    (51, 64, "OOEEIMOE", "OEOOEEI", (24, 19), (54, 43), 0),
    (1, 64, "OEMOOEE", "OOEEEO", (48, 1), (81, 2), 1),
    (29, 96, "IMOEOOE", "OOOEEI", (64, 19), (162, 49), 0),
    (67, 128, "OOEEIMOOE", "OEOOOEEI", (48, 25), (162, 85), 0),
    (5, 192, "IMOEOOOE", "OOOOEEI", (128, 3), (486, 13), 0),
    (81, 128, "OEMOOOEE", "OOEEOEO", (96, 61), (243, 155), 0),
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise ValueError(message)


def step(n: int) -> int:
    require(n > 0, ("nonpositive ordinary value", n))
    return (3 * n + 1) // 2 if n & 1 else n // 2


def v2(n: int) -> int:
    require(n > 0, ("v2 domain", n))
    return (n & -n).bit_length() - 1


def good(z: int) -> bool:
    if z <= 0 or z & 1:
        return False
    k = v2(z)
    return (z >> k) % 4 == pow(3, k, 4)


def walk(n: int, clock: int) -> tuple[int, int]:
    odds = 0
    for _ in range(clock):
        odds += n & 1
        n = step(n)
    return n, odds


def ordinary_word(n: int, clock: int) -> str:
    letters = []
    for _ in range(clock):
        letters.append("O" if n & 1 else "E")
        n = step(n)
    return "".join(letters)


def affine_replay(r: int, modulus: int, factor: int, word: str):
    """Prove legality for every u>=0, keeping the induction source r+m*u."""
    a, b = factor * modulus, factor * r
    demands = []
    for letter in word:
        if letter == "D":
            a, b = 2 * a, 2 * b
        elif letter == "I":
            require(a % 3 == 0 and b % 3 == 2, ("nonintegral odd preimage", a, b))
            a, b = 2 * a // 3, (2 * b - 1) // 3
            require(a % 2 == 0 and b % 2 == 1, ("wrong preimage parity", a, b))
        elif letter == "E":
            require(a % 2 == 0 and b % 2 == 0, ("even branch guard", a, b))
            a, b = a // 2, b // 2
        elif letter == "O":
            require(a % 2 == 0 and b % 2 == 1, ("odd branch guard", a, b))
            a, b = 3 * a // 2, (3 * b + 1) // 2
        elif letter == "M":
            require(0 < a <= modulus and 0 < b < r, ("not uniformly smaller", a, b, modulus, r))
            demands.append((a, b))
            a, b = 3 * a, 3 * b
        else:
            raise ValueError(("unknown certificate letter", letter))
        require(min(a, b) > 0, ("nonpositive affine state", a, b))
    return (a, b), demands


def check_affine_row(row):
    r, m, left, right, demand, endpoint, minimum_u = row
    # Shift the sole base exception n=1 to n=65 before checking u>=0.
    shifted_r = r + m * minimum_u
    left_endpoint, left_demands = affine_replay(shifted_r, m, 1, left)
    right_endpoint, right_demands = affine_replay(shifted_r, m, 3, right)
    expected_endpoint = (endpoint[0], endpoint[1] + endpoint[0] * minimum_u)
    expected_demand = (demand[0], demand[1] + demand[0] * minimum_u)
    require(left_endpoint == right_endpoint == expected_endpoint, ("wrong affine endpoint", row))
    require(left_demands + right_demands == [expected_demand], ("wrong induction demand", row))


def literal_replay(n: int, factor: int, word: str):
    x = factor * n
    demands = []
    for letter in word:
        if letter == "D":
            x *= 2
        elif letter == "I":
            require(x % 3 == 2, ("nonintegral literal preimage", x))
            x = (2 * x - 1) // 3
            require(x > 0 and x & 1, ("invalid literal preimage", x))
        elif letter == "E":
            require(x % 2 == 0, ("literal even branch", x))
            x //= 2
        elif letter == "O":
            require(x % 2 == 1, ("literal odd branch", x))
            x = (3 * x + 1) // 2
        elif letter == "M":
            require(0 < x < n, ("literal demand is not smaller", x, n))
            demands.append(x)
            x *= 3
        else:
            raise ValueError(("unknown literal letter", letter))
        require(x > 0, ("nonpositive literal state", x))
    return x, demands


def adaptive_certificate(n: int, rule: str):
    if rule == "G":
        require(n & 1 and n % 3 == 2 and good(3 * n + 1), ("G guard", n))
        a, x = (2 * n - 1) // 3, 3 * n
        left_head, right_head = "IMO", ""
        left_is_upper = False
    elif rule == "F":
        require(n > 1 and n % 16 == 1 and good(9 * n + 7), ("F guard", n))
        a, x = (3 * n + 1) // 4, (27 * n + 13) // 8
        left_head, right_head = "OEMO", "OOE"
        left_is_upper = True
    elif rule == "H":
        require(n % 16 == 3 and good(9 * n + 5), ("H guard", n))
        a, x = (3 * n - 1) // 8, (27 * n + 7) // 8
        left_head, right_head = "OOEEIMOD", "OEO"
        left_is_upper = False
    elif rule == "J":
        require(n % 64 == 25, ("J guard", n))
        return "OEOOEEIM", "OOEOEEI", (9 * n - 1) // 32, None
    else:
        raise ValueError(("unknown rule", rule))
    require(x > 1 and x & 1 and good(x + 1), ("adjacent guard transfer", rule, n, x))
    horizon = v2(x + 1) + 2
    low = ordinary_word(x - 1, horizon)
    high = ordinary_word(x, horizon)
    return (left_head + (high if left_is_upper else low),
            right_head + (low if left_is_upper else high), a, horizon)


def check_adaptive(n: int, rule: str):
    left, right, a, horizon = adaptive_certificate(n, rule)
    endpoint, d1 = literal_replay(n, 1, left)
    endpoint2, d2 = literal_replay(n, 3, right)
    require(endpoint == endpoint2, ("literal endpoints differ", rule, n, endpoint, endpoint2))
    require(d1 + d2 == [a], ("wrong literal demand", rule, n, d1, d2, a))
    return len(left) + len(right), horizon


def first_hit(n: int, cap: int = 10000):
    clock = 0
    odds = 0
    while n != 1:
        require(clock < cap, ("hitting-time replay exhausted", n, cap))
        odds += n & 1
        n = step(n)
        clock += 1
    return clock, odds


def neighborhood(r: int):
    hits = [first_hit(a * r) for a in (1, 3)]
    depth = max(9, r.bit_length(), *(tau + 22 for tau, _ in hits))
    modulus = 2**depth
    arms = []
    for a, (tau, odds) in zip((1, 3), hits, strict=True):
        clock = tau + 22
        total_odds = odds + 11
        coefficient = a * 3**total_odds * 2**(depth - clock)
        require(Fraction(coefficient, modulus) <= Fraction(3, 4)**11 / r,
                ("seed slope bound", r, a))
        require(4 * modulus > 81 * coefficient, ("no eventual demand gap", r, a))
        require(81 * (coefficient + 2) < 4 * (r + modulus), ("first positive lift gap", r, a))
        arms.append((a, clock, total_odds, coefficient))
    return depth, arms


def expect_rejection(operation):
    try:
        operation()
    except (ValueError, ZeroDivisionError):
        return
    raise ValueError("negative control was accepted")


def run():
    for row in ROWS:
        check_affine_row(row)
    require(walk(3, 5)[0] == 1, "P(1) base replay")
    period = 384
    old = set(range(7, period, 8))
    new = set().union(*(set(range(r, period, m)) for r, m, *_ in ROWS))
    require((len(old), len(old | new), len(new - old)) == (48, 83, 35), "residue union count")

    adjacent_count = 0
    for x in range(3, 100001, 2):
        if good(x + 1):
            k = v2(x + 1)
            t = (x + 1) >> k
            expected = ((3**k * t - 1) // 4, k)
            require(walk(x, k + 2) == walk(x - 1, k + 2) == expected,
                    ("adjacent identity", x))
            adjacent_count += 1

    counts = dict.fromkeys(("G", "F", "H", "J"), 0)
    path_edges = 0
    largest_adjacent_clock = 0
    for n in range(2, 100001):
        applicable = []
        if n & 1 and n % 3 == 2 and good(3 * n + 1):
            applicable.append("G")
        if n % 16 == 1 and good(9 * n + 7):
            applicable.append("F")
        if n % 16 == 3 and good(9 * n + 5):
            applicable.append("H")
        if n % 64 == 25:
            applicable.append("J")
        for rule in applicable:
            edges, clock = check_adaptive(n, rule)
            path_edges += edges
            counts[rule] += 1
            largest_adjacent_clock = max(largest_adjacent_clock, clock or 0)

    stress_count = 0
    largest_stress_bits = 0
    for rule, start_k, target, offset, divisor in (
        ("G", 1, 7, 1, 3), ("F", 4, 7, 7, 9), ("H", 4, 5, 5, 9)
    ):
        for k in range(start_k, 81):
            residues = [t for t in range(1, 37, 2)
                        if t % 4 == pow(3, k, 4) and (2**k * t) % 9 == target]
            require(len(residues) == 1, ("stress CRT construction", rule, k, residues))
            for lift in (1, 17, 2**128 + 3):
                t = residues[0] + 36 * lift
                n = (2**k * t - offset) // divisor
                edges, clock = check_adaptive(n, rule)
                path_edges += edges
                largest_adjacent_clock = max(largest_adjacent_clock, clock or 0)
                largest_stress_bits = max(largest_stress_bits, n.bit_length())
                stress_count += 1
    for lift in (1, 17, 2**256 + 3):
        edges, _ = check_adaptive(25 + 64 * lift, "J")
        path_edges += edges
        stress_count += 1

    exact_coefficient = Fraction(81, 4) * (Fraction(3, 4)**11 + Fraction(2, 512))
    require(exact_coefficient == Fraction(15676011, 16777216) < 1, "neighborhood coefficient")
    neighborhood_replays = 0
    largest_depth = 0
    for r in range(1, 513):
        depth, arms = neighborhood(r)
        largest_depth = max(largest_depth, depth)
        modulus = 2**depth
        for a, clock, odds, coefficient in arms:
            for lift in (0, 1, 2, 17, 2**128 + 3):
                n = r + modulus * lift
                require(walk(a * n, clock) == (1 + coefficient * lift, odds),
                        ("ordinary neighborhood replay", r, a, lift))
                if lift:
                    y = 1 + coefficient * lift
                    require(81 * ((y + 1) // 4) < n, ("ordinary demand bound", r, a, lift))
                neighborhood_replays += 1

    corrupt = list(ROWS[0])
    corrupt[2] = corrupt[2][:-1] + "O"
    expect_rejection(lambda: check_affine_row(tuple(corrupt)))
    corrupt_endpoint = list(ROWS[1])
    corrupt_endpoint[5] = (54, 22)
    expect_rejection(lambda: check_affine_row(tuple(corrupt_endpoint)))
    expect_rejection(lambda: affine_replay(5, 192, 1, "M"))
    expect_rejection(lambda: literal_replay(5, 1, "M"))
    expect_rejection(lambda: affine_replay(1, 64, 1, "I"))
    expect_rejection(lambda: adaptive_certificate(9, "G"))
    expect_rejection(lambda: adaptive_certificate(1, "F"))
    expect_rejection(lambda: adaptive_certificate(3, "H"))
    require(not good(8) and walk(6, 5) != walk(7, 5), "false unguarded adjacent control")

    return {
        "status": "bounded exact replays passed; universal coverage remains open",
        "source_pr": 146,
        "source_head": "7d04c4dd756cfe495eb3eee78eba35a99085cd2a",
        "affine_rows": len(ROWS),
        "residue_period": period,
        "odd_residues": period // 2,
        "inherited_excluded_odd_residues": len(old),
        "combined_excluded_odd_residues": len(old | new),
        "new_excluded_odd_residues": len(new - old),
        "adjacent_cases_through_100000": adjacent_count,
        "adaptive_cases_through_100000": counts,
        "deep_valuation_stress_cases": stress_count,
        "largest_stress_input_bits": max(largest_stress_bits, (25 + 64 * (2**256 + 3)).bit_length()),
        "largest_adjacent_clock": largest_adjacent_clock,
        "total_replayed_adaptive_graph_edges": path_edges,
        "neighborhood_seed_pairs": 512,
        "neighborhood_ordinary_replays": neighborhood_replays,
        "largest_neighborhood_binary_depth": largest_depth,
        "neighborhood_exact_coefficient": str(exact_coefficient),
        "negative_controls": 9,
        "limits": [
            "The infinite adaptive families are established by the written argument, not the bounded census.",
            "The neighborhood result inherits the source-qualified finite 81h convergence implication.",
            "No proof that the guards cover every ordinary integer is supplied.",
            "No proof-assistant verification is claimed."
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    dest = parser.add_mutually_exclusive_group()
    dest.add_argument("--output", type=Path, help="Write a new exact bounded replay report; refuse existing paths")
    dest.add_argument("--compare", type=Path, help="Regenerate and compare with an existing exact replay report")
    args = parser.parse_args()
    if args.output and args.output.exists():
        parser.error("--output refuses to overwrite existing evidence; choose a new path or use --compare")
    report = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output:
        with args.output.open("x", encoding="utf-8") as output:
            output.write(report)
    if args.compare:
        require(args.compare.read_text(encoding="utf-8") == report, "existing report differs from exact regeneration")
    print(report, end="")


if __name__ == "__main__":
    main()
