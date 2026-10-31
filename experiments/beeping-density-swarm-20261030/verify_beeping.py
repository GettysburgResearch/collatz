#!/usr/bin/env python3
"""Independent literal-table and arithmetic-energy checks for beeping17.

No upstream simulator is imported. Finite simulation does not certify Collatz
or replace the all-parameter invariant proof in the companion note.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import random

MACHINE = (
    "1RL0RB_1LC1RB_0LK0LD_1RE1LD_0RF0RB_0LG0LG_1LH1LG_0RA0RI_"
    "1RJ1RI_1RF1RF_0RA1LK_0LM0LM_0LN1LM_1RO1LN_0RA0RP_0RQ1RP_1RL1RQ"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def parse_machine():
    rows = MACHINE.split("_")
    require(len(rows) == 17, "state count")
    table = {}
    for state, row in enumerate(rows):
        require(len(row) == 6, "transition row length")
        for bit in (0, 1):
            write, direction, target = row[3 * bit:3 * bit + 3]
            require(write in "01" and direction in "LR" and target in "ABCDEFGHIJKLMNOPQ", "bad transition")
            table[(state, bit)] = (int(write), -1 if direction == "L" else 1, ord(target) - ord("A"))
    return table


TABLE = parse_machine()


def canonical(n, value, capacity):
    require(n >= 1 and 1 <= value <= capacity, "bad canonical parameters")
    ones = set(range(-n, -1)) | set(range(capacity))
    ones.remove(value - 1)
    return ones


def shortcut(value):
    return value // 2 if value % 2 == 0 else (3 * value + 1) // 2


def macro_spec(n, value, capacity):
    if value == 1:
        return n + 1, n + 1, max(capacity, n + 1), n, 2 * n * (n + 2)
    if value % 2 == 0:
        k = value // 2
        return n, k, capacity, 0, 2 * k * (k + 1)
    k = (value - 1) // 2
    out = 3 * k + 2
    return n, out, max(capacity, out), 0, 5 * k * k + 9 * k + 4


def literal_macro(ones, max_steps):
    """Return at the first A; reject a wrong head, timeout, or mutation."""
    head = state = 0
    beeps = []
    visited_min = visited_max = 0
    for step in range(1, max_steps + 1):
        visited_min = min(visited_min, head)
        visited_max = max(visited_max, head)
        bit = int(head in ones)
        write, move, target = TABLE[state, bit]
        if write:
            ones.add(head)
        else:
            ones.discard(head)
        if state == ord("O") - ord("A"):
            beeps.append(step)
        head += move
        state = target
        if state == 0:
            require(head == 0, "first A return at wrong head")
            return step, beeps, (visited_min, visited_max)
    raise RuntimeError("literal macro exceeded its claimed exact time")


def phi(value):
    return Fraction(2 * value * value, 3) + 2 * value


def odd_toll(value):
    require(value > 1 and value % 2, "odd toll domain")
    return Fraction((value + 1) * (25 * value + 23), 12)


def cost(value):
    require(value > 1, "arithmetic cost at terminal value")
    return Fraction(value * value, 2) + value if value % 2 == 0 else Fraction(5 * value * value + 8 * value + 3, 4)


def arithmetic_orbit(n, max_steps=1000000):
    values, seen = [], set()
    value = n
    for _ in range(max_steps):
        if value == 1:
            return values
        require(value not in seen, "a repeated nonterminal arithmetic value")
        seen.add(value)
        values.append(value)
        value = shortcut(value)
    raise RuntimeError("arithmetic orbit timeout")


def cumulative_cost_bound(height):
    """Exact sum of every possible macro cost for distinct 2<=v<=height."""
    m, r = height // 2, (height - 1) // 2
    sum_even = m * (m + 1) * (2 * m + 1) // 3 + m * (m + 1)
    sum_odd = Fraction(5 * r * (r + 1) * (2 * r + 1), 6) + Fraction(9 * r * (r + 1), 2) + 4 * r
    return sum_even + sum_odd


def check_polynomial_identities():
    # Construct polynomials independently from their defining expressions.
    # Increasing-degree Fraction coefficients, normalized to fixed degree 2.
    def add(a, b):
        return [x + y for x, y in zip(a, b)]
    def scale(c, a):
        return [c * x for x in a]
    def product(a, b):
        out = [Fraction(0)] * 3
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                if i + j < 3:
                    out[i + j] += x * y
                else:
                    require(x * y == 0, "unexpected degree above two")
        return out
    def phi_poly(v):
        return add(scale(Fraction(2, 3), product(v, v)), scale(2, v))
    zero, one = Fraction(0), Fraction(1)
    k = [zero, one, zero]
    two_k = scale(2, k)
    odd_v = add(two_k, [one, zero, zero])
    odd_out = add(scale(3, k), [2 * one, zero, zero])
    even_cost = [zero, 2 * one, 2 * one]
    even_phi_difference = add(phi_poly(two_k), scale(-1, phi_poly(k)))
    odd_cost = [4 * one, 9 * one, 5 * one]
    odd_phi_difference = add(phi_poly(odd_v), scale(-1, phi_poly(odd_out)))
    odd_toll_coefficients = scale(Fraction(1, 12), product(add(odd_v, [one, zero, zero]), add(scale(25, odd_v), [23 * one, zero, zero])))
    require(even_cost == even_phi_difference, "even coefficient identity")
    require(odd_cost == add(odd_phi_difference, odd_toll_coefficients), "odd coefficient identity")
    # Σ odd shuttle times + establishing FGH + expansion rounds.
    # Initial shuttle sum: Σ_{i=0}^{k-1}(4k-4i+1)=2k²+3k.
    # Expansion sum: Σ_{r=0}^{k-1}(9+6r)=3k²+6k.
    require([4, 9, 5] == [1 + 3, 3 + 6, 2 + 3], "odd macro sum")
    # Reset: (n+4) + (n-1)(2n+5) + 1 = 2n²+4n.
    require([0, 4, 2] == [4 - 5 + 1, 1 + 5 - 2, 2], "reset macro sum")
    return {"exact_rational_polynomial_identities": 5}


def finite_macro_checks():
    cases = set()
    for n in (1, 2, 3, 8, 25):
        for value in range(1, 65):
            for extra in (0, 1, 37):
                cases.add((n, value, value + extra))
    for n in (1, 2, 3, 10, 63, 128):
        for capacity in (1, 2, 10000):
            cases.add((n, 1, capacity))
    rng = random.Random(20261030)
    for _ in range(96):
        n, value = rng.randint(1, 64), rng.randint(2, 400)
        cases.add((n, value, value + rng.choice((0, 1, 10000))))
    transitions = resets = 0
    for n, value, capacity in sorted(cases):
        out_n, out_v, out_k, expected_beeps, expected_time = macro_spec(n, value, capacity)
        tape = canonical(n, value, capacity)
        elapsed, beeps, visited = literal_macro(tape, expected_time)
        require(tape == canonical(out_n, out_v, out_k), f"whole-tape mismatch at {(n, value, capacity)}")
        require(elapsed == expected_time, "exact macro time")
        require(len(beeps) == expected_beeps, "beep count")
        expected_interval = (-n - 1, n) if value == 1 else (-1, (value if value % 2 == 0 else shortcut(value)) - 1)
        require(visited == expected_interval, "visited interval")
        if value == 1:
            resets += 1
            require(beeps == [n + 5 + j * (2 * n + 5) for j in range(n)], "exact reset beep schedule")
        transitions += elapsed
    return {"cases": len(cases), "reset_cases": resets, "literal_transitions": transitions, "max_capacity": max(k for _, _, k in cases)}


def blank_trace(completed_inputs=26):
    tape, n, value, capacity = set(), 1, 1, 1
    absolute_time, macro_count, beep_count = 0, 0, 0
    completions = []
    first_beeps = []
    while n <= completed_inputs:
        old_n, old_value = n, value
        n, value, capacity, expected_beeps, expected_time = macro_spec(n, value, capacity)
        elapsed, beeps, _ = literal_macro(tape, expected_time)
        require(tape == canonical(n, value, capacity), "blank trace whole tape")
        require(elapsed == expected_time and len(beeps) == expected_beeps, "blank trace event mismatch")
        if beeps:
            first_beeps.append({"input": old_n, "time": absolute_time + beeps[0]})
        absolute_time += elapsed
        macro_count += 1
        beep_count += len(beeps)
        if old_value == 1:
            require(beep_count == old_n * (old_n + 1) // 2, "blank trace triangular beep number")
            completions.append({"input": old_n, "last_beep_time": absolute_time, "beeps": beep_count})
    return {"completed_inputs": completed_inputs, "literal_transitions": absolute_time, "macros": macro_count, "beeps": beep_count, "completions": completions, "first_beeps": first_beeps}


def orbit_energy_checks(limit=10000):
    largest_height = largest_cost = 0
    for n in range(1, limit + 1):
        values = arithmetic_orbit(n)
        total = sum((cost(v) for v in values), Fraction(0))
        energy = phi(n) - phi(1) + sum((odd_toll(v) for v in values if v % 2), Fraction(0))
        require(total == energy and total.denominator == 1, "orbit energy identity")
        height = max([1] + values)
        require(total <= cumulative_cost_bound(height), "height-to-time upper bound")
        if values:
            require(total >= Fraction(height * height, 2), "time-to-height lower bound")
        largest_height = max(largest_height, height)
        largest_cost = max(largest_cost, int(total))
    return {"starts": limit, "largest_height": largest_height, "largest_arithmetic_cost": largest_cost}


def run():
    symbolic = check_polynomial_identities()
    finite = finite_macro_checks()
    blank = blank_trace()
    energy = orbit_energy_checks()
    for event in blank["first_beeps"]:
        n = event["input"]
        previous_time = 0 if n == 1 else blank["completions"][n - 2]["last_beep_time"]
        arithmetic_time = int(sum((cost(v) for v in arithmetic_orbit(n)), Fraction(0)))
        require(event["time"] - previous_time == arithmetic_time + n + 5, "cross-burst gap formula")
    return {"status": "PASS", "scope": "bounded independent literal replay plus exact polynomial coefficient checks; not a Collatz proof or formal proof assistant certification", "literal_sha256_no_newline": hashlib.sha256(MACHINE.encode()).hexdigest(), "symbolic_identities": symbolic, "macro_checks": finite, "blank_trace": blank, "energy_checks": energy}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "blank_trace"}, indent=2))
    print(json.dumps({"blank_trace": {k: v for k, v in result["blank_trace"].items() if k not in ("completions", "first_beeps")}}, indent=2))
