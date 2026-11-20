#!/usr/bin/env python3
"""Independent, bounded exact replay of the certificate-transfer intake.

No supplied script is imported, and no assertion is used as an acceptance
check. UNRESOLVED means that a specified finite search did not emit a
certificate; it is never interpreted as nonconvergence or nonmerger.
This program does not prove a universal transfer rule or Collatz.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def standard(n: int) -> int:
    require(type(n) is int and n > 0, "positive ordinary state required")
    return 3 * n + 1 if n & 1 else n // 2


def shortcut(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def odd_step(n: int) -> tuple[int, int]:
    require(type(n) is int and n > 0 and n & 1, "positive odd state required")
    value = 3 * n + 1
    exponent = (value & -value).bit_length() - 1
    return value >> exponent, exponent


def advance(n: int, steps: int) -> int:
    for _ in range(steps):
        n = standard(n)
    return n


def make_certificate(n: int, budget: int = 2000) -> list[int] | None:
    require(n > 0 and n & 1, "positive odd certificate source required")
    cumulative = [0]
    for _ in range(budget):
        if n == 1:
            return cumulative
        n, exponent = odd_step(n)
        cumulative.append(cumulative[-1] + exponent)
    return cumulative if n == 1 else None


def replay_certificate(n: int, cumulative: list[int]) -> list[int]:
    require(type(n) is int and n > 0 and n & 1, "positive odd source required")
    require(bool(cumulative) and cumulative[0] == 0, "certificate must start at zero")
    require(all(type(a) is int and a >= 0 for a in cumulative), "nonnegative integer exponents required")
    states = [n]
    for before, after in zip(cumulative, cumulative[1:]):
        require(after > before, "strictly increasing cumulative exponents required")
        numerator = 3 * states[-1] + 1
        denominator = 1 << (after - before)
        require(numerator % denominator == 0, "nonintegral certificate edge")
        target = numerator // denominator
        require(target > 0 and target & 1, "division exponent is not the exact odd-step valuation")
        states.append(target)
    require(states[-1] == 1, "certificate does not end at one")
    r = len(cumulative) - 1
    correction = sum(3 ** (r - 1 - j) * (1 << cumulative[j]) for j in range(r))
    require(3**r * n + correction == 1 << cumulative[-1], "global certificate identity failed")
    return states


def bounded_transfer(x: int, source: list[int], budget: int) -> dict:
    require(x > 1 and x % 128 == 1 and ((x - 1) // 128) % 4 != 0, "outside reverse-transfer domain")
    require(type(budget) is int and budget >= 0, "nonnegative finite budget required")
    a = list(source)
    x_states = replay_certificate(x, a)
    w = (x + 1) // 2
    current = w
    b = [0]
    for s in range(1, budget + 1):
        current, exponent = odd_step(current)
        b.append(b[-1] + exponent)
        while len(a) <= s:
            a.append(a[-1] + 2)
            x_states.append(1)
        if current == x_states[s] and b[s] == a[s] - 1:
            result = b[:s] + [entry - 1 for entry in a[s:]]
            replay_certificate(w, result)
            return {"status": "CERTIFIED", "merge_odd_clock": s, "certificate": result}
    return {"status": "UNRESOLVED", "odd_clock_budget": budget}


def affine_standard(coefficient: int, constant: int, steps: int) -> tuple[int, int]:
    for _ in range(steps):
        require(coefficient % 2 == 0, "affine parity is not forced for all integer lifts")
        if constant & 1:
            coefficient, constant = 3 * coefficient, 3 * constant + 1
        else:
            coefficient, constant = coefficient // 2, constant // 2
    return coefficient, constant


def type_from_forms(px: int, bx: int, py: int, by: int) -> tuple[int, int]:
    level = py - px
    offset = by - 3**level * bx if level >= 0 else bx - 3**(-level) * by
    return level, offset


def type_step(level: int, offset: int, bit: int) -> tuple[int, int]:
    """Signed transition table, checked below against literal affine paths."""
    require(bit in (0, 1), "driver parity must be a bit")
    if level == 0:
        if offset % 2 == 0:
            return 0, offset // 2 if bit == 0 else 3 * offset // 2
        return (1, (3 * offset + 1) // 2) if bit == 0 else (-1, (1 - 3 * offset) // 2)
    height = abs(level)
    if offset % 2 == 0:
        new_height = height
        new_offset = offset // 2 if bit == 0 else (3 * offset + 1 - 3**height) // 2
    elif bit == 0:
        new_height, new_offset = height + 1, (3 * offset + 1) // 2
    else:
        new_height, new_offset = height - 1, (offset - 3**(height - 1)) // 2
    if level > 0:
        return new_height, new_offset
    return (-new_height, new_offset) if new_height else (0, -new_offset)


def affine_digit(exponent: int, constant: int, digit: int) -> tuple[int, int]:
    value = constant + digit * 3**exponent
    return (exponent + 1, (3 * value + 1) // 2) if value & 1 else (exponent, value // 2)


def run_checks() -> dict:
    report: dict = {"schema": "collatz-certificate-intake-check/v1", "status": "PASS"}
    certificate_count = 0
    for n in range(1, 4000, 2):
        a = make_certificate(n)
        require(a is not None, "bounded certificate construction exhausted on the declared sample")
        replay_certificate(n, a)
        padded = list(a)
        for _ in range(3):
            padded.append(padded[-1] + 2)
        replay_certificate(n, padded)
        certificate_count += 2
    report["source_certificates"] = {"odd_sources_below": 4000, "validated_including_padding": certificate_count}

    good = make_certificate(257)
    require(good is not None, "source 257 certificate missing")
    bad_inputs = [(257, [1] + good[1:]), (257, good[:-1] + [good[-1] + 1]), (257, [0, 0] + good[1:]), (258, good)]
    rejected = 0
    for n, a in bad_inputs:
        try:
            replay_certificate(n, a)
        except ValueError:
            rejected += 1
    require(rejected == len(bad_inputs), "a deliberately invalid certificate was accepted")
    report["invalid_certificates_rejected"] = rejected

    certified = unresolved = 0
    for m in range(1, 2001):
        if m % 4 == 0:
            continue
        x = 128 * m + 1
        a = make_certificate(x)
        require(a is not None, "source construction exhausted on the transfer sample")
        result = bounded_transfer(x, a, len(a) + 60)
        if result["status"] == "CERTIFIED":
            certified += 1
        else:
            unresolved += 1
    require(bounded_transfer(257, good, 0)["status"] == "UNRESOLVED", "zero budget must not claim success")
    example = bounded_transfer(257, good, 100)
    require(example["status"] == "CERTIFIED" and example["merge_odd_clock"] == 6, "257 to 129 witness changed")
    a385 = make_certificate(385)
    require(a385 is not None and bounded_transfer(385, a385, 100)["status"] == "UNRESOLVED", "bounded obstruction example changed")
    report["bounded_reverse_transfer"] = {"m_at_most": 2000, "eligible_sources": certified + unresolved, "certified": certified, "unresolved": unresolved, "budget": "len(source_certificate)+60 odd steps", "unresolved_meaning": "no certificate emitted within this budget only", "example_257_to_129_merge_odd_clock": 6}

    families = [(2,4,11,12,162,22), (6,5,13,14,486,94), (24,6,14,15,486,184), (30,6,15,16,1458,688), (8,7,16,17,1458,94), (105,7,15,16,486,400), (110,7,17,18,4374,3766)]
    for residue, exponent, lower_clock, upper_clock, coefficient, constant in families:
        modulus = 1 << exponent
        lower = affine_standard(16 * modulus, 16 * residue + 1, lower_clock)
        upper = affine_standard(32 * modulus, 32 * residue + 1, upper_clock)
        require(lower == upper == (coefficient, constant), "all-lift affine merger failed")
    report["affine_families"] = {"all_lift_certificates": len(families), "parameter_domain": "k=residue+2^exponent*t, every integer t>=0", "clock": "standard 3n+1/halving steps", "rows": families}

    # Numerical equality on the root cycle does not imply equal affine coefficients.
    x, y, p, q = 10, 29, 2, 3
    for _ in range(13):
        p += x & 1
        q += y & 1
        x, y = shortcut(x), shortcut(y)
    require((x, y, p, q) == (1, 1, 7, 8), "k=1 phase/count witness changed")
    require((3**(q-p) * x - 2) == y, "nonabsorbed relation witness failed")
    report["k1_numerical_meeting_without_structural_absorption"] = {"shortcut_clock_from_10_29": 13, "states": [x, y], "total_odd_counts_including_initial_prefixes": [p, q], "relation": [1, -2], "D": 2}

    fixed_clock_count = 0
    for odd_a in range(3, 4001, 2):
        value = odd_a + 1
        b = (value & -value).bit_length() - 1
        u = value >> b
        if u % 4 != (1 if b % 2 == 0 else 3):
            continue
        target = (3**b * u - 1) // 2
        require(advance(odd_a, 2*b+1) == advance(odd_a-1, 2*b+1) == target, "fixed-clock consecutive identity failed")
        fixed_clock_count += 1
    require(advance(3, 5) == advance(2, 5) == 4, "A=3 first-passage correction failed")
    require(advance(5, 3) == advance(4, 3) == 4, "A=5 first-passage correction failed")
    report["corrected_consecutive_fixed_clocks"] = {"odd_A_at_most": 3999, "eligible_checked": fixed_clock_count, "special_cases": [[3, 2, 5, 4], [5, 4, 3, 4]], "continues_after_one": True}

    rank_four_rows = []
    for s in range(1, 9):
        power = 1 << (54*s)
        require((power - 1) % 81 == 0, "rank-four integrality failed")
        core = (power - 1) // 81
        x = 256*core + 1
        a = [0, 2, 4, 6, 8+54*s]
        states = replay_certificate(x, a)
        require(states == [x, 192*core+1, 144*core+1, 108*core+1, 1], "rank-four literal path failed")
        require(81*x + 175 == 256*power, "rank-four scalar certificate failed")
        first, second = (x+1)//2, ((x+1)//2+1)//2
        require(x % 512 == 257 and first % 512 in (129, 385) and second == 64*core+1, "double-transfer domain failed")
        first_value, first_odd_count = first, 0
        first_hit_before_cut = False
        for _ in range(54*s+7):
            first_hit_before_cut = first_hit_before_cut or first_value == 1
            first_odd_count += first_value & 1
            first_value = shortcut(first_value)
        require(not first_hit_before_cut and first_value == 3**(27*s)+1 and first_odd_count == 27*s+4, "first-companion clock or odd count failed")
        require(shortcut(first_value) == shortcut(3**(27*s-1)), "first-companion pure-power meeting failed")
        target = 3**(27*s-1) + 1
        require(advance(9*core, 81*s+1) == target, "fixed clock from nine times core failed")
        require(advance(second, 81*s+9) == target, "double-transfer target path failed")
        require(standard(3**(27*s-2)) == target, "pure-power target failed")
        rank_four_rows.append({"s": s, "cumulative_certificate": a, "first_companion_shortcut_clock": 54*s+7, "first_companion_odd_count": first_odd_count, "first_companion_pure_power_exponent": 27*s-1, "two_transfer_pure_power_exponent": 27*s-2, "second_companion_standard_clock": 81*s+9})
    report["rank_four_and_double_transfer"] = {"s_values": list(range(1,9)), "rows": rank_four_rows, "scope": "source certificates and fixed common-endpoint identities; no unproved transfer is executed or assumed"}

    forward_rows = []
    for d in range(1, 9):
        e = 6*d + 1
        numerator = (1 << (e-1)) - 1
        require(numerator % 9 == 0, "forward family integrality failed")
        k = numerator // 9
        lower, upper = 16*k+1, 32*k+1
        a = make_certificate(lower)
        require(a is not None and len(a)-1 == 2 and a[-1] == e+3, "two-odd source certificate failed")
        value = upper
        odd_count = 0
        reached_one_before_cut = False
        for _ in range(e+4):
            reached_one_before_cut = reached_one_before_cut or value == 1
            odd_count += value & 1
            value = shortcut(value)
        require(not reached_one_before_cut and value == 3**e - 1 and odd_count-2 == e, "forward landing obstruction failed")
        forward_rows.append({"d": d, "e": e, "source_odd_count": 2, "source_halvings": e+3, "upper_halving_clock": e+4, "upper_lead": e, "upper_endpoint": str(value)})
    report["forward_landing_obstruction"] = {"rows": forward_rows, "scope": "eight exact fixed-clock instances; no later upper convergence assumed"}

    # Fully enumerate a small binary residue partition independently of the C DFS.
    depth = 12
    modulus = 1 << depth
    coverage = []
    for residue in (4, 8, 12):
        matches = 0
        for k in range(residue, modulus, 16):
            x, y, px, py = 9*k+1, 27*k+2, 2, 3
            for _ in range(depth):
                px += x & 1
                py += y & 1
                x, y = shortcut(x), shortcut(y)
            # Verify the coefficient on a second physical lift, rather than
            # treating equality for one ordinary representative as a cylinder.
            lx, ly = 9*(k+modulus)+1, 27*(k+modulus)+2
            for _ in range(depth):
                lx, ly = shortcut(lx), shortcut(ly)
            require(lx-x == 3**px and ly-y == 3**py, "literal high-bit coefficient check failed")
            matches += int(x == y and px == py)
        coverage.append({"k_mod_16": residue, "matched_cells": matches, "total_cells": modulus//16})
    report["small_complete_residue_partition"] = {"k_bit_depth": depth, "reverse_m_bit_depth": depth-2, "parameter_conversion": "k=4m; conv_dfs depth counts bits of k, two more than bits of m", "classes": coverage, "exact_arithmetic": True, "scope": "finite prefix coverage only"}

    # All three reverse types, with the manuscript's m-bit clock, rather than
    # silently identifying it with the C program's k-bit clock.
    m_depth = 10
    expected_types = {1: (-3, -1), 2: (1, 2), 3: (-1, -2)}
    transition_count = literal_checks = 0
    for residue, initial_type in expected_types.items():
        for tail in range(1 << (m_depth-2)):
            m = residue + 4*tail
            px, bx, py, by = 4, 2, 3, 1
            for digit_index in range(m_depth):
                level, offset = type_from_forms(px, bx, py, by)
                digit = (m >> digit_index) & 1
                driver = bx + digit*3**px if level >= 0 else by + digit*3**py
                predicted = type_step(level, offset, driver & 1)
                px, bx = affine_digit(px, bx, digit)
                py, by = affine_digit(py, by, digit)
                require(type_from_forms(px, bx, py, by) == predicted, "signed transition disagrees with affine branches")
                if digit_index == 1:
                    require(predicted == initial_type, "one of the three reverse initial types failed")
                transition_count += 1
            for lift in (0, 1):
                parameter = m + (1 << m_depth)*lift
                lx, ly = 128*parameter+1, 64*parameter+1
                for _ in range(m_depth+7):
                    lx = shortcut(lx)
                for _ in range(m_depth+6):
                    ly = shortcut(ly)
                require(lx == bx+3**px*lift and ly == by+3**py*lift, "reverse affine path disagrees with physical lift")
                literal_checks += 2
    report["reverse_type_transition_checks"] = {"m_bit_depth": m_depth, "initial_types_by_m_mod_4": {str(r): list(t) for r,t in expected_types.items()}, "transition_checks": transition_count, "physical_arm_lift_checks": literal_checks}

    # Exact scalar enclosure from DENSITY_ONE.md (16). This is not a
    # computational proof of its probabilistic stopping argument.
    r = Fraction(897, 1000)
    sqrt3_lower = Fraction(433, 250)
    inverse_sqrt2_upper = Fraction(708, 1000)
    require(sqrt3_lower > 0 and sqrt3_lower**2 < 3, "sqrt(3) lower enclosure failed")
    require(inverse_sqrt2_upper > 0 and inverse_sqrt2_upper**2 > Fraction(1,2), "inverse sqrt(2) upper enclosure failed")
    kappa_squared_upper = 6-3*sqrt3_lower
    require(0 < kappa_squared_upper < r*r < 1, "kappa upper enclosure failed")
    finite_sum = 3*r/(1-r) + r*r/(1-r*r)
    finite_sum += sum((r**(2**j)/(1-r**(2**j)) for j in range(1,6)), Fraction(0))
    tail_upper = r**64/(1-r**64)**2
    c_upper = inverse_sqrt2_upper*(1+2*(finite_sum+tail_upper))
    require(c_upper < Fraction(10667,200) < 54, "exact additive constant upper bound failed")
    report["density_one_scalar_constant"] = {"r": str(r), "sqrt3_lower": str(sqrt3_lower), "inverse_sqrt2_upper": str(inverse_sqrt2_upper), "kappa_squared_upper": str(kappa_squared_upper), "C_upper_numerator": str(c_upper.numerator), "C_upper_denominator": str(c_upper.denominator), "strict_rational_display_upper": "10667/200 = 53.335 < 54", "scope": "exact finite rational expression and root enclosures only; stochastic inference uses the written proof"}
    report["scope"] = "Exact bounded replay, explicit all-lift affine certificates, and negative controls; not universal convergence, a complete merger cover, or formal proof-assistant verification."
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write the same deterministic JSON receipt to this new path")
    args = parser.parse_args()
    report = run_checks()
    report["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
