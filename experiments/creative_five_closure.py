#!/usr/bin/env python3
"""Exact finite replay of physical five blocks and a failed carry rank.

No all-source termination or forward-five basin closure is asserted.
The proof of each unbounded family is in five_closure.md; this checker
reconstructs the stated bounded instances using literal ordinary steps.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(n):
    require(n > 0, "ordinary positive domain")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def advance(n, clock):
    odd = 0
    for _ in range(clock):
        odd += n % 2
        n = shortcut(n)
    return n, odd


def valuation(n, prime):
    require(n != 0, "valuation at zero")
    n, result = abs(n), 0
    while n % prime == 0:
        n //= prime
        result += 1
    return result


def first_hit(n, cap):
    clock = odd = 0
    while n != 1 and clock < cap:
        odd += n % 2
        clock += 1
        n = shortcut(n)
    require(n == 1, "known source did not hit within its stated exact clock")
    return clock, odd


def supplied_odd_word(n, word):
    """Replay each exact valuation; reject early first hits and extra factors."""
    require(n > 1 and n % 2 == 1, "nontrivial odd supplied source")
    for index, exponent in enumerate(word):
        value = 3 * n + 1
        require(valuation(value, 2) == exponent, "supplied odd valuation mismatch")
        n = value // (2 ** exponent)
        require(n != 1 or index == len(word) - 1, "supplied word continued after first hit")
    require(n == 1, "supplied odd word does not end at one")


def paired_predecessor(q, clock):
    require(q > 0 and q % 2 == 1 and q % 3 != 0, "paired target must be an odd ternary unit")
    require(clock >= 6, "paired block needs its sixth shortcut output")
    numerator = 2 ** clock * q - 7
    require(numerator % 9 == 0, "paired predecessor is not integral")
    x = numerator // 9
    require(x > 0 and x % 2 == 1, "paired predecessor ordinary domain")
    return x


def unit_paired_predecessor(q):
    base_clocks = {1: 10, 2: 9, 4: 8, 5: 11, 7: 6, 8: 7}
    clock = base_clocks[q % 9]
    x = paired_predecessor(q, clock)
    if x % 3 == 0:
        clock += 6
        x = paired_predecessor(q, clock)
    require(6 <= clock <= 17 and x % 3 != 0 and x > q, "unit paired lift guard")
    return x, clock


def carry_step(h):
    require(h > 0, "positive carry parameter")
    if h % 3 == 0:
        return "inverse_one", 2 * h // 3
    if h % 3 == 1:
        return "physical_detour", (16 * h - 1) // 3
    q = (8 * h - 1) // 3
    return ("unit_exit" if q % 3 else "nonunit_exit"), q


def lift_exponent(k):
    """Finite base-three digit lifting, not an unbounded discrete-log search."""
    require(k >= 1, "positive expansion length")
    c = pow(7, (1 - k) % 3, 9)
    final_modulus = 3 ** (k + 4)
    target = ((19 + 5 * 3 ** (k + 2) * c) * pow(754, -1, final_modulus)) % final_modulus
    a = 0
    for exponent in range(2, k + 5):
        modulus = 3 ** exponent
        stride = 3 ** (exponent - 2)
        candidates = [a + digit * stride for digit in range(3)
                      if pow(16, a + digit * stride, modulus) == target % modulus]
        require(len(candidates) == 1, "nonunique finite ternary lift")
        a = candidates[0]
    require(0 <= a < 3 ** (k + 3) and a % 3 == 2, "lifted exponent domain")
    require(pow(16, a, final_modulus) == target, "final exponent congruence")
    return a, c


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--compare", type=Path)
    args = parser.parse_args()

    pair_count = unit_choices = 0
    for q in range(1, 3002, 2):
        if q % 3 == 0:
            continue
        for clock in range(6, 26):
            if (2 ** clock * q - 7) % 9:
                continue
            x = paired_predecessor(q, clock)
            require(advance(x, clock) == (q, 2), "lower paired ordinary word")
            require(advance(5 * x, clock) == (5 * q, 2), "upper paired ordinary word")
            require(x % 64 == 49, "paired source class")
            pair_count += 1
        x, clock = unit_paired_predecessor(q)
        require(advance(x, clock) == (q, 2) and advance(5 * x, clock) == (5 * q, 2),
                "selected unit paired predecessor")
        unit_choices += 1

    second_odd_positions = []
    for i in range(1, 41):
        for j in range(1, 41):
            if 3 + 2 ** j == 5 * (3 + 2 ** i):
                second_odd_positions.append([i, j])
    require(second_odd_positions == [[2, 5]], "two-odd block classification")

    rank_two_family = []
    for r in range(1, 26):
        x = (2 ** (6 * r + 4) - 7) // 9
        lower_word = [2, 6 * r + 2]
        upper_word = [5, 6 * r - 1, 4]
        supplied_odd_word(x, lower_word)
        supplied_odd_word(5 * x, upper_word)
        require(first_hit(x, 6 * r + 4) == (6 * r + 4, 2), "rank-two source clock")
        require(first_hit(5 * x, 6 * r + 8) == (6 * r + 8, 3), "rank-three five clock")
        rank_two_family.append({"r": r, "source_bits": x.bit_length(),
                                "source_word": lower_word, "five_word": upper_word,
                                "source_is_ternary_unit": x % 3 != 0})

    carry_counts = {"inverse_one": 0, "physical_detour": 0, "unit_exit": 0, "nonunit_exit": 0}
    for h in range(1, 1501):
        n = 10 * h - 1
        kind, value = carry_step(h)
        carry_counts[kind] += 1
        if kind == "inverse_one":
            m = 10 * value - 1
            require(advance(m, 1) == (n, 1), "physical inverse-one realization")
        elif kind == "physical_detour":
            m = 10 * value - 1
            require(advance(m, 5) == (shortcut(n), 2), "physical detour realization")
        else:
            require(advance(5 * value, 2) == (n, 1), "physical five-multiple exit")
            require((value % 3 != 0) == (h % 9 in (2, 5)), "exit unit guard")

    require(first_hit(19, 14) == (14, 6), "known seed 19")
    renewal_cases = []
    for r in range(5):
        a = 5 + 243 * r
        source = (58 * 16 ** a - 1) // 3
        require((source + 1) % 15 == 0, "renewal carry parameter is integral")
        h = (source + 1) // 15
        require(h % 81 == 13 and h % 2 == 0, "convergent recharge congruence")
        n = 10 * h - 1
        kind, middle = carry_step(h)
        require(kind == "physical_detour", "renewal first branch")
        kind, end = carry_step(middle)
        require(kind == "inverse_one", "renewal second branch")
        m = 10 * end - 1
        require(end == (32 * h - 2) // 9 and m > n, "renewal height increase")
        debts = [valuation(h, 3), valuation(13 * h - 1, 3)]
        end_debts = [valuation(end, 3), valuation(13 * end - 1, 3)]
        require(debts == end_debts == [0, 1], "renewal debt recharge")
        source_clock = first_hit(source, 4 * a + 14)
        start_clock = first_hit(n, 4 * a + 15)
        end_clock = first_hit(m, 4 * a + 20)
        require(source_clock == (4 * a + 14, 6), "J-lift source clocks")
        require(start_clock == (4 * a + 15, 7) and end_clock == (4 * a + 20, 9),
                "renewal supplied first-hit clock increases")
        require(advance(m, 6) == (shortcut(n), 3), "complete renewal ordinary meeting")
        renewal_cases.append({"r": r, "a": a, "source_bits": source.bit_length(),
                              "start_clock": list(start_clock), "end_clock": list(end_clock),
                              "debts": debts, "end_debts": end_debts})

    long_runs = []
    for k in range(1, 7):
        a, c = lift_exponent(k)
        source = (58 * 16 ** a - 1) // 3
        require((source + 1) % 15 == 0, "long-run carry parameter is integral")
        h = (source + 1) // 15
        require((13 * h - 1) % (3 ** k) == 0, "long-run divisibility")
        t = (13 * h - 1) // (3 ** k)
        require(t % 9 == c and t % 2 == 1 and valuation(13 * h - 1, 3) == k,
                "long-run exact ternary debt")
        current = h
        for j in range(k):
            require(current == (16 ** j * 3 ** (k - j) * t + 1) // 13,
                    "long-run intermediate formula")
            kind, current = carry_step(current)
            require(kind == "physical_detour", "long-run expansion branch")
        require(current == (16 ** k * t + 1) // 13 and current % 9 == 2,
                "long-run terminal unit exit")
        kind, q = carry_step(current)
        require(kind == "unit_exit" and q % 2 == 1 and q % 3 == 2, "valid output unit")
        require(advance(5 * q, 4 * k + 3) == (source, k + 2), "long-run physical ancestor identity")
        require(first_hit(source, 4 * a + 14) == (4 * a + 14, 6), "long-run supplied convergence")
        require(first_hit(5 * q, 4 * a + 4 * k + 17) == (4 * a + 4 * k + 17, k + 8),
                "long-run five-multiple convergence")
        require(Fraction(q, source) >= Fraction(28, 195) * Fraction(16, 3) ** k,
                "unbounded output ratio lower bound")
        long_runs.append({"k": k, "a": a, "t_mod9": t % 9,
                          "source_bits": source.bit_length(), "output_bits": q.bit_length(),
                          "source_odd_clock": 6, "five_output_odd_clock": k + 8,
                          "quotient_convergence_tested": False})

    negatives = []
    try:
        paired_predecessor(5, 5)
    except ValueError:
        negatives.append("clock-five off-by-one rejected")
    else:
        raise ValueError("clock-five negative control accepted")
    require(advance(17, 5)[0] == 5 and advance(85, 5)[0] == 8 != 25,
            "literal failed clock-five transfer")
    require(paired_predecessor(113, 11) % 3 == 0 and unit_paired_predecessor(113)[1] == 17,
            "paired predecessor unit repair")
    negatives.append("nonunit first paired predecessor repaired by six extra halvings")
    require(carry_step(8) == ("nonunit_exit", 21), "nonunit carry exit is not a successful unit guard")
    negatives.append("nonunit quotient exit remains explicitly nonunit")
    require(carry_step(13) == ("physical_detour", 69) and carry_step(69) == ("inverse_one", 46),
            "expanding complete renewal retained")
    negatives.append("expanding full renewal is retained rather than silently declared descending")

    report = {
        "schema": "collatz-creative-five-closure-v1",
        "status": "PASS: physical local identities and explicit failed ranks; forward-five closure remains OPEN",
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "paired_block_instances": pair_count,
        "selected_unit_paired_predecessors": unit_choices,
        "two_odd_position_solutions_through_40": second_odd_positions,
        "rank_two_sources_with_exact_rank_three_five_word": rank_two_family,
        "carry_steps_by_kind": carry_counts,
        "known_convergent_complete_renewals": renewal_cases,
        "known_convergent_long_expansion_runs": long_runs,
        "negative_controls": negatives,
        "arbitrary_carry_termination_claimed": False,
        "quotient_basin_membership_inferred_from_five_multiple": False,
        "complete_physical_five_closure_claimed": False,
    }
    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(serialized)
        print(f"PASS: wrote new report {args.output}")
    elif args.compare:
        require(json.loads(args.compare.read_text(encoding="utf-8")) == report, "frozen report differs")
        print(f"PASS: exact comparison {args.compare}")
    else:
        print(serialized, end="")


if __name__ == "__main__":
    main()
