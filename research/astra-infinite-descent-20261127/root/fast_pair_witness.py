#!/usr/bin/env python3
"""Construct and literally replay large synchronized first-hit pairs.

This is an independent, exact-integer implementation of the finite-gap rows,
two-gap router and inverse phase ladder in this packet. It is a certificate
generator, not a census or a proof that every integer reaches one. No floating
point approximation participates in construction or verification.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


@dataclass(frozen=True)
class Row:
    clock: int
    grade: int
    source_offset: int
    target_offset: int


def compose(first: Row, second: Row) -> Row:
    """Refine a dyadic cylinder so its endpoint fits the next cylinder."""
    modulus = 1 << second.clock
    t = ((second.source_offset - first.target_offset)
         * pow(3 ** first.grade, -1, modulus)) % modulus
    numerator = 3 ** first.grade * t + first.target_offset - second.source_offset
    require(numerator >= 0 and numerator % modulus == 0, "Bad cylinder join")
    v = numerator // modulus
    result = Row(first.clock + second.clock, first.grade + second.grade,
                 (1 << first.clock) * t + first.source_offset,
                 3 ** second.grade * v + second.target_offset)
    require(0 <= result.source_offset < 1 << result.clock, "Noncanonical source offset")
    require(0 <= result.target_offset < 3 ** result.grade, "Noncanonical target offset")
    return result


def merge_row(gap: int) -> Row:
    """Return n=2^h*t+i, T^h(n)=T^h(n+gap)=3^g*t+j."""
    require(gap >= 0, "Negative gap")
    if gap == 0:
        return Row(0, 0, 0, 0)
    if gap == 1:
        return Row(3, 1, 4, 2)
    if gap % 2 == 0:
        return compose(Row(1, 0, 0, 0), merge_row(gap // 2))
    q, residue = divmod(gap, 4)
    if residue == 1:
        return compose(Row(2, 1, 1, 1), merge_row(3 * q + 1))
    return compose(Row(2, 1, 2, 2), merge_row(3 * q + 2))


def phase_net(epsilon: Fraction) -> tuple[int, Fraction]:
    """Certify a finite multiplicative net of 2^m/3^d on [1,2)."""
    require(0 < epsilon < 1, "Net tolerance must lie in (0,1)")
    depth = 1
    while depth <= 16384:
        phases = []
        ternary = 1
        for _ in range(depth + 1):
            binary_exponent = (ternary - 1).bit_length()
            phases.append(Fraction(1 << binary_exponent, ternary))
            ternary *= 3
        phases.sort()
        gaps = [b / a for a, b in zip(phases, phases[1:])]
        gaps.append(2 * phases[0] / phases[-1])
        maximum = max(gaps)
        if maximum <= 1 + epsilon:
            return depth, maximum
        depth *= 2
    raise RuntimeError("Finite phase search exceeded the explicit resource bound")


def unit_predecessor(target: int, least_gap: int) -> tuple[int, int]:
    for gap in range(least_gap, least_gap + 6):
        numerator = (target << gap) - 1
        if numerator % 3 == 0 and (numerator // 3) % 3 != 0:
            source = numerator // 3
            require(source > 0 and source % 2 == 1, "Invalid ordinary odd predecessor")
            return source, gap
    raise RuntimeError("No unit-preserving valuation gap in a full six-step period")


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def binary_lift_above(source: int, lower: int) -> tuple[int, int]:
    exponent = max(0, lower.bit_length() - source.bit_length())
    if source << exponent < lower:
        exponent += 1
    return source << exponent, exponent


def route_pair(endpoint: int, gap: int, precision: int, residue: int,
               row: Row) -> tuple[int, int, int, int]:
    source_modulus = 3 ** precision
    parameter_class = ((residue - row.source_offset)
                       * pow(1 << row.clock, -1, source_modulus)) % source_modulus
    profile_class = row.target_offset + 3 ** row.grade * parameter_class
    router_precision = row.grade + precision
    period = 6 * 3 ** router_precision
    router_clock = period + 1
    modulus = 3 ** (router_precision + 2)
    address = (pow(2, router_clock, modulus) * endpoint - 3 - 9 * profile_class) % modulus
    power = 1
    for first_gap in range(1, period + 1):
        power = 2 * power % modulus
        if power == address:
            numerator = (endpoint << router_clock) - 3 - (1 << first_gap)
            require(numerator > 0 and numerator % 9 == 0, "Router identity failed")
            profile = numerator // 9
            t_numerator = profile - row.target_offset
            require(t_numerator >= 0 and t_numerator % (3 ** row.grade) == 0,
                    "Profile extraction failed")
            source = (t_numerator // (3 ** row.grade) << row.clock) + row.source_offset
            require(source % source_modulus == residue % source_modulus,
                    "Prescribed ternary class failed")
            return source, row.clock + router_clock, row.grade + 2, first_gap
    raise RuntimeError("Primitive-root address not found in its complete period")


def replay(source: int, target: int, clock: int) -> dict:
    require(source > 0 and target > 0, "Nonpositive trajectory")
    value = source
    grade = 0
    peak = source
    trajectory_digest = hashlib.sha256()
    for time in range(clock + 1):
        trajectory_digest.update(str(value).encode("ascii") + b"\n")
        if value == target:
            require(time == clock, "Target was reached before the claimed first-arrival time")
        if time == clock:
            break
        if value % 2:
            grade += 1
            value = (3 * value + 1) // 2
        else:
            value //= 2
        peak = max(peak, value)
    require(value == target, "Literal trajectory has the wrong final target")
    return {"first_hit_clock": clock, "odd_departures": grade,
            "peak": str(peak), "trajectory_sha256": trajectory_digest.hexdigest()}


def make_certificate(gap: int, precision: int, residue: int,
                     delta: Fraction, depth: int, maximum_gap: Fraction) -> dict:
    row = merge_row(gap)
    prefix_clock = row.clock + 6 * 3 ** (row.grade + precision) + 1
    prefix_grade = row.grade + 2
    # 85 first reaches 1 in eight shortcut steps; it cannot follow a previous 1.
    branch = 85
    branch_clock = 8
    first_inverse_gap = 20
    while Fraction(8, 5 * (1 << first_inverse_gap)) >= delta / 64:
        first_inverse_gap += 1
    height_exponent = prefix_clock + first_inverse_gap + 6 * depth + 40
    lower = branch << height_exponent
    upper = Fraction(1 + delta) * lower
    ideal_endpoint_lower = ceil_fraction(
        Fraction(3 ** prefix_grade * (lower + (1 << prefix_clock)), 1 << prefix_clock))
    ancestor, ladder_clock = branch, 0
    for ladder_grade in range(depth + 1):
        endpoint, lift_clock = binary_lift_above(ancestor, ideal_endpoint_lower)
        source, checked_clock, checked_grade, router_gap = route_pair(
            endpoint, gap, precision, residue, row)
        require((checked_clock, checked_grade) == (prefix_clock, prefix_grade),
                "Inconsistent fixed prefix")
        if lower <= source and source + gap < upper:
            total_clock = prefix_clock + lift_clock + ladder_clock + branch_clock
            total_grade = prefix_grade + ladder_grade + 1
            left = replay(source, 1, total_clock)
            right = replay(source + gap, 1, total_clock)
            require(left["odd_departures"] == total_grade == right["odd_departures"],
                    "The two arms have unequal grade")
            return {
                "gap": gap, "ternary_precision": precision,
                "source_residue": residue % (3 ** precision),
                "relative_width": str(delta), "target": 1,
                "interval_lower": str(lower), "interval_upper": str(upper),
                "source": str(source), "second_source": str(source + gap),
                "source_bits": source.bit_length(),
                "clock_minus_floor_log2_interval_lower": total_clock - (lower.bit_length() - 1),
                "prefix": {"merge_row": row.__dict__, "clock": prefix_clock,
                           "grade": prefix_grade, "first_router_gap": router_gap},
                "ladder": {"depth_bound": depth, "used_grade": ladder_grade,
                           "odd_clock": ladder_clock, "initial_even_clock": lift_clock,
                           "certified_phase_maximum_ratio": str(maximum_gap)},
                "left_replay": left, "right_replay": right,
            }
        if ladder_grade < depth:
            ancestor, new_gap = unit_predecessor(
                ancestor, first_inverse_gap if ladder_grade == 0 else 3)
            ladder_clock += new_gap
    raise RuntimeError("Certified ladder search unexpectedly missed the requested window")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    delta = Fraction(1, 10)
    depth, maximum = phase_net(delta / 16)
    fixtures = [(1, 0, 0), (3, 1, 2), (7, 1, 1), (13, 1, 0)]
    certificates = [make_certificate(d, s, c, delta, depth, maximum) for d, s, c in fixtures]
    result = {
        "schema": "collatz-infinite-descent-fast-pairs/v1",
        "scope": "Four constructed ordinary positive integer first-hit pairs; not a universal convergence test",
        "arithmetic": "exact integers and rational comparisons; no assert statements or floating point",
        "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "passed": True, "certificate_count": len(certificates),
        "certificates": certificates,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"passed": True, "phase_depth": depth,
                      "sources": [{k: c[k] for k in
                                   ("gap", "source_bits", "clock_minus_floor_log2_interval_lower")}
                                  for c in certificates]}, indent=2))


if __name__ == "__main__":
    main()
