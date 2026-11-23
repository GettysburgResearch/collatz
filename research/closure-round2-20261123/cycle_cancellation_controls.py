#!/usr/bin/env python3
"""Exact positive/negative controls for the finite gcd transport law.

These are targeted finite controls, not a search or a proof of cycle absence.
The full-denominator controls use repetitions of the known 2 -> 1 -> 2 cycle.
The h=3 control uses an explicitly abstract modulus, not its cycle denominator.
All guards are explicit and remain active under python -O.
"""
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from math import gcd
from pathlib import Path
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def carry_positions(word):
    positions = [i for i, bit in enumerate(word) if bit == "1"]
    return sum(2**i * 3 ** (len(positions) - 1 - j)
               for j, i in enumerate(positions))


def carry_affine(word):
    value = 0
    for i, bit in enumerate(word):
        value = 3 * value + 2**i if bit == "1" else value
    return value


def make_control(prefix, h, suffix, modulus=None):
    source = prefix + "0" * h + "1" + suffix
    neighbor = prefix + "1" + "0" * h + suffix
    full_d = 2 ** len(source) - 3 ** source.count("1")
    return {
        "prefix": prefix, "h": h, "suffix": suffix,
        "source": source, "neighbor": neighbor,
        "D": full_d if modulus is None else modulus,
        "full_denominator": modulus is None,
        "C": carry_positions(source), "C_neighbor": carry_positions(neighbor),
    }


def verify(control):
    u, h, v = control["prefix"], control["h"], control["suffix"]
    require(isinstance(h, int) and h >= 1, "invalid shift length")
    require(set(u + v) <= {"0", "1"}, "invalid bits")
    source, neighbor = u + "0" * h + "1" + v, u + "1" + "0" * h + v
    require(control["source"] == source and control["neighbor"] == neighbor,
            "word mutation")
    d = control["D"]
    require(isinstance(d, int) and d > 0 and gcd(d, 6) == 1, "invalid unit modulus")
    c, c_next = carry_positions(source), carry_positions(neighbor)
    require(control["C"] == c and control["C_neighbor"] == c_next,
            "carry mutation")
    require(c == carry_affine(source) and c_next == carry_affine(neighbor),
            "independent carry disagreement")
    require(c % d == 0, "source is not a zero residue")
    factor = 2 ** len(u) * 3 ** v.count("1")
    require(c - c_next == factor * (2**h - 1), "whole-word difference failed")
    require(gcd(d, c_next) == gcd(d, 2**h - 1), "gcd transport failed")
    require(Fraction(c_next, d).denominator == d // gcd(d, 2**h - 1),
            "reduced denominator failed")
    if control["full_denominator"]:
        require(d == 2 ** len(source) - 3 ** source.count("1"),
                "incorrect full denominator")
        start = c // d
        require(start > 0, "ordinary cycle must be positive")
        state = start
        for bit in source:
            require(state % 2 == int(bit), "ordinary parity replay failed")
            state = (3 * state + 1) // 2 if bit == "1" else state // 2
        require(state == start, "ordinary cycle did not close")
    return {**control, "expected_gcd": gcd(d, 2**h - 1),
            "neighbor_reduced_denominator": Fraction(c_next, d).denominator}


def main():
    # Include D=1 explicitly: the adjacent neighbor then remains integral.
    controls = [make_control("", 1, ""),
                make_control("", 1, "01" * 5),
                make_control("0101", 1, "01" * 3),
                make_control("", 3, "01", modulus=7)]
    outcomes = [verify(control) for control in controls]
    rejected = []
    for field in ("C", "C_neighbor", "D"):
        changed = deepcopy(controls[1])
        changed[field] = 1 if field == "D" else changed[field] + 1
        try:
            verify(changed)
        except ValueError as error:
            rejected.append({"field": field, "reason": str(error)})
        else:
            raise ValueError("corrupted control was accepted: " + field)
    print(json.dumps({
        "scope": "finite transport controls; no unrestricted cycle exclusion",
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "controls": outcomes, "corruptions_rejected": rejected,
    }, indent=2))


if __name__ == "__main__":
    main()
