#!/usr/bin/env python3
"""Independent bounded reconstruction of C5-001--005; no author import."""

from pathlib import Path
from hashlib import sha256
import argparse
import json


ROOT = Path(__file__).resolve().parents[2]
PINS = {
    "research/creative-closure-20261120/five_closure.md":
        "cde080ac777ab6673029fe8ed769f13f84500c23a59d5111075fb6e44e1261d6",
    "experiments/creative_five_closure.py":
        "c72e23840297d8eac4c988c02a08d7e83129dfc53de00fa8025363ed2141b05c",
    "reports/2026-11-20-creative-closure/five-report.json":
        "0b3cfa27a941fa43f1c9daacb484b5923dcc4537886a53c7fada19e530f32c31",
}


def require(value, label):
    if not value:
        raise RuntimeError(label)


def step(value):
    require(value >= 1, "positive ordinary input")
    return value // 2 if value % 2 == 0 else (3 * value + 1) // 2


def walk(value, length):
    odds = 0
    early_one = False
    for _ in range(length):
        early_one |= value == 1
        odds += value % 2
        value = step(value)
    return value, odds, early_one


def hit(value, bound):
    odds = 0
    for clock in range(bound + 1):
        if value == 1:
            return clock, odds
        odds += value % 2
        value = step(value)
    raise RuntimeError("literal first-hit bound failed")


def valuation(value, prime):
    require(value != 0, "nonzero valuation")
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def run():
    for name, digest in PINS.items():
        require(sha256((ROOT / name).read_bytes()).hexdigest() == digest,
                "frozen source hash changed: " + name)

    paired = 0
    # Start from the ordinary source cylinder, not the author's target loop.
    for u in range(1024):
        x = 64 * u + 49
        z = 9 * u + 7
        q = z
        extra = 0
        while q % 2 == 0:
            q //= 2
            extra += 1
        length = 6 + extra
        require(q % 3 != 0 and 7 * q <= x, "paired reduced unit and height")
        require(walk(x, length) == (q, 2, False), "lower source-cylinder path")
        require(walk(5 * x, length) == (5 * q, 2, False), "upper source-cylinder path")
        paired += 1

    unit_targets = 0
    selected_lengths = set()
    for q in range(1, 512, 2):
        if q % 3 == 0:
            continue
        choices = []
        for length in range(6, 18):
            numerator = (2 ** length) * q - 7
            if numerator % 9 == 0 and (numerator // 9) % 3:
                choices.append((length, numerator // 9))
        require(choices, "bounded unit lift exists")
        length, x = min(choices)
        require(x > q and x % 2 and x % 3, "selected unit predecessor")
        require(walk(x, length) == (q, 2, False), "selected lower path")
        require(walk(5 * x, length) == (5 * q, 2, False), "selected upper path")
        selected_lengths.add(length)
        unit_targets += 1

    rank_two = 0
    for r in (1, 2, 7, 13, 26, 41, 80):
        x = (2 ** (6 * r + 4) - 7) // 9
        require(hit(x, 6 * r + 4) == (6 * r + 4, 2), "rank-two first hit")
        require(hit(5 * x, 6 * r + 8) == (6 * r + 8, 3), "rank-three five first hit")
        rank_two += 1

    branch_checks = 0
    for h in range(1, 1001):
        n = 10 * h - 1
        if h % 3 == 0:
            predecessor = (2 * n - 1) // 3
            require(predecessor == 10 * (2 * h // 3) - 1, "inverse-one integer form")
            require(walk(predecessor, 1) == (n, 1, False), "inverse-one path")
        elif h % 3 == 1:
            predecessor = (16 * n + 3) // 3
            require(predecessor == 10 * ((16 * h - 1) // 3) - 1, "detour integer form")
            require(walk(predecessor, 5) == (step(n), 2, False), "detour path")
        else:
            q = (8 * h - 1) // 3
            require(q % 2 and walk(5 * q, 2) == (n, 1, False), "exit path")
            require(bool(q % 3) == (h % 9 in (2, 5)), "exit unit domain")
        branch_checks += 1

    recharge_checks = 0
    for v in range(513):
        h = 81 * v + 13
        middle = (16 * h - 1) // 3
        end = 2 * middle // 3
        require(middle % 3 == 0 and end > h, "complete recharge branches")
        require([valuation(h, 3), valuation(13 * h - 1, 3)] == [0, 1],
                "initial two debts")
        require([valuation(end, 3), valuation(13 * end - 1, 3)] == [0, 1],
                "renewed two debts")
        require(walk(10 * end - 1, 6) == (step(10 * h - 1), 3, False),
                "complete recharge physical meeting")
        recharge_checks += 1

    known_renewals = []
    for r in (0, 3, 7):
        exponent = 5 + 243 * r
        source = (58 * 16 ** exponent - 1) // 3
        require((source + 1) % 15 == 0, "known source carry integral")
        h = (source + 1) // 15
        end = (32 * h - 2) // 9
        require(h % 81 == 13, "known source recharge class")
        require(hit(source, 4 * exponent + 14) == (4 * exponent + 14, 6),
                "known source exact first hit")
        require(hit(10 * h - 1, 4 * exponent + 15) == (4 * exponent + 15, 7),
                "known initial carry first hit")
        require(hit(10 * end - 1, 4 * exponent + 20) == (4 * exponent + 20, 9),
                "known renewed carry first hit")
        known_renewals.append({"r": r, "exponent": exponent, "source_bits": source.bit_length()})

    lifts = []
    modular_states = 0
    for k in range(1, 8):
        modulus = 3 ** (k + 4)
        order = 3 ** (k + 3)
        residue = pow(7, (1 - k) % 3, 9)
        target = ((19 + 5 * 3 ** (k + 2) * residue) * pow(754, -1, modulus)) % modulus
        # Exhaust the finite multiplicative orbit, rather than digit lifting.
        current = 1
        matches = []
        seen = set()
        for exponent in range(order):
            require(current not in seen, "order prematurely repeats")
            seen.add(current)
            if current == target:
                matches.append(exponent)
            current = 16 * current % modulus
        require(current == 1 and len(matches) == 1, "full finite subgroup and unique lift")
        exponent = matches[0]
        require(exponent % 3 == 2, "lifted exponent domain")
        modular_states += order
        row = {"k": k, "exponent": exponent, "group_order": order,
               "literal_complete_first_hits": k <= 5}
        if k <= 5:
            source = (58 * 16 ** exponent - 1) // 3
            require((source + 1) % 15 == 0, "long-run source carry integral")
            h = (source + 1) // 15
            require(valuation(13 * h - 1, 3) == k, "long-run exact debt")
            initial = h
            for _ in range(k):
                require(h % 3 == 1, "successive legal detours")
                h = (16 * h - 1) // 3
            require(h % 9 == 2, "terminal unit branch")
            q = (8 * h - 1) // 3
            require(q % 2 and q % 3 == 2, "output ordinary unit")
            require(walk(5 * q, 4 * k + 3) == (source, k + 2, False),
                    "concatenated physical ancestor path")
            require(hit(source, 4 * exponent + 14) == (4 * exponent + 14, 6),
                    "long-run known source first hit")
            require(hit(5 * q, 4 * exponent + 4 * k + 17)
                    == (4 * exponent + 4 * k + 17, k + 8),
                    "long-run known five-output first hit")
            require(q * 195 * 3 ** k >= source * 28 * 16 ** k,
                    "exact output-height ratio bound")
            require(h >= initial, "increasing detour block")
            row["source_bits"] = source.bit_length()
            row["output_bits"] = q.bit_length()
        lifts.append(row)

    require(walk(17, 5)[0] == 5 and walk(85, 5)[0] != 25,
            "clock-five transfer remains rejected")
    require((8 * 8 - 1) // 3 == 21, "nonunit exit retained")
    return {
        "status": "PASS",
        "scope": "Independent bounded reconstruction; no global closure or quotient convergence claim.",
        "source_sha256": PINS,
        "review_checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_cylinder_blocks": paired,
        "searched_unit_targets": unit_targets,
        "selected_unit_clock_range": [min(selected_lengths), max(selected_lengths)],
        "rank_two_family_parameters_checked": rank_two,
        "carry_branch_instances": branch_checks,
        "complete_recharge_classes_checked": recharge_checks,
        "known_convergent_renewals": known_renewals,
        "exhaustive_modular_states": modular_states,
        "finite_exponent_lifts": lifts,
        "negative_controls": ["clock-five transfer", "nonunit exit"],
        "author_imports": False,
        "quotient_convergence_tested": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--compare", type=Path)
    args = parser.parse_args()
    report = run()
    if args.compare:
        require(json.loads(args.compare.read_text(encoding="utf-8")) == report,
                "independent frozen report mismatch")
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "modular_states": report["exhaustive_modular_states"],
                      "paired_blocks": report["source_cylinder_blocks"]}, sort_keys=True))


if __name__ == "__main__":
    main()
