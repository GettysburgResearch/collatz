"""Rebuild an ordinary binary cylinder and replay all 1,024 first arrivals."""

import json
from pathlib import Path


def check(condition, description):
    if not condition:
        raise ValueError(description)


def step(value):
    return value // 2 if value % 2 == 0 else (3 * value + 1) // 2


def trace(value, clock):
    grade = 0
    for _ in range(clock):
        grade += value % 2
        value = step(value)
    return value, grade


def advance(profile, clock, parameter):
    grade, base = profile
    endpoint, extra = trace(3**grade * parameter + base, clock)
    return grade + extra, endpoint


def refinement(left, right):
    """Select a dyadic prefix shrinking a fixed gap or the initial grade gap."""
    left_grade, left_base = left
    right_grade, right_base = right
    if left_grade == right_grade:
        if left_base > right_base:
            return refinement(right, left)
        gap = right_base - left_base
        check(gap > 0, "merging a pair already equal")
        if gap == 1:
            clock, residue = 3, 4
        elif gap % 2 == 0:
            clock, residue = 1, 0
        elif gap % 4 == 1:
            clock, residue = 2, 1
        else:
            clock, residue = 2, 2
        modulus = 2**clock
        parameter = (residue - left_base) * pow(3**left_grade, -1, modulus) % modulus
        return clock, parameter
    if left_grade > right_grade:
        return refinement(right, left)

    parameter = int(left_base == right_base)
    left_value = 3**left_grade * parameter + left_base
    right_value = 3**right_grade * parameter + right_base
    difference = abs(left_value - right_value)
    check(difference > 0, "distinct-slope sample collision")
    matched = (difference & -difference).bit_length() - 1
    first, first_grade = trace(left_value, matched)
    second, second_grade = trace(right_value, matched)
    check(first_grade == second_grade and first % 2 != second % 2, "first parity disagreement")
    if first % 2 == 0:
        parameter += 2**matched
    clock = matched + 1
    return clock, parameter % 2**clock


def synchronize(offsets, binary_depth=0, binary_residue=0):
    """Return (clock, grade, lower residue, endpoint) for the entire cylinder."""
    clock = binary_depth
    residue = binary_residue % 2**clock
    profiles = [advance((0, offset), clock, residue) for offset in offsets]
    for index in range(1, len(profiles)):
        while profiles[index] != profiles[0]:
            extra, parameter = refinement(profiles[0], profiles[index])
            residue += 2**clock * parameter
            clock += extra
            profiles = [advance(profile, extra, parameter) for profile in profiles]
    grade, endpoint = profiles[0]
    return clock, grade, residue, endpoint


def first_one(value, budget):
    grade = 0
    for clock in range(budget + 1):
        if value == 1:
            return clock, grade
        if clock < budget:
            grade += value % 2
            value = step(value)
    raise ValueError(f"first arrival exceeds the supplied {budget}-clock budget")


def main():
    fixture = json.loads(Path(__file__).with_name("FINITE_BLOCK_1024.json").read_text())
    offsets = range(fixture["members"])
    prefix = fixture["prefix"]
    clock, grade, residue, endpoint = synchronize(offsets)
    check(
        (clock, grade, residue, endpoint)
        == (prefix["clock"], prefix["grade"], int(prefix["source"]), int(prefix["endpoint"])),
        "regenerated full binary cylinder",
    )
    for parameter in fixture["free_parameter_controls"]:
        expected = endpoint + 3**grade * parameter
        for offset in offsets:
            start = residue + 2**clock * parameter + offset
            check(trace(start, clock) == (expected, grade), "ordinary affine cylinder replay")

    lifts = fixture["power_of_two_lifts"]
    exponent = int(lifts["exponent_residue"])
    period = int(lifts["exponent_period"])
    check(lifts["ternary_precision"] == grade and period == 2 * 3 ** (grade - 1), "exponent period")
    check(exponent > endpoint.bit_length(), "positive power-of-two lift")
    check(pow(2, exponent, 3**grade) == endpoint % 3**grade, "exact dyadic address")
    check(pow(2, period, 3**grade) == 1, "persistent dyadic address")
    tail = fixture["common_tail"]
    check(first_one(endpoint, tail["budget"]) == (tail["clock"], tail["grade"]), "bounded common tail")
    total = (clock + tail["clock"], grade + tail["grade"])
    check(total == (fixture["first_clock"], fixture["first_grade"]), "composed first arrival")
    for offset in offsets:
        actual = first_one(residue + offset, total[0])
        check(actual == total, f"literal first arrival for member {offset}")
    check(len(offsets) * total[0] == fixture["full_trace_steps"], "full replay count")
    print(f"PASS {len(offsets)} consecutive first arrivals to 1, clock {total[0]}, grade {total[1]}")
    print(f"PASS {fixture['full_trace_steps']} ordinary steps in separate first-hit traces")


if __name__ == "__main__":
    main()
