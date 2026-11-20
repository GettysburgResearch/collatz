#!/usr/bin/env python3
"""Exact finite checks for AR1/AR2 and the fixed-source closing calculations.

No floating point is used. Finding finitely many witnesses does not establish
density. Formal tails in the product check are not asserted to be actual orbits.
All checks remain active under python -OO.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
from math import gcd
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def valuation(n: int, p: int) -> int:
    require(n != 0, "valuation of zero is outside this check")
    n = abs(n)
    exponent = 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent


def t_step(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def prefix(n: int, length: int) -> tuple[list[int], int, int, int]:
    word: list[int] = []
    c = q = 0
    current = n
    for k in range(length):
        bit = current & 1
        word.append(bit)
        if bit:
            c = 3 * c + (1 << k)
            q += 1
        current = t_step(current)
    require((1 << length) * current == 3**q * n + c, "affine prefix")
    return word, q, c, current


def integer_digest(n: int) -> str:
    require(n >= 0, "digest domain")
    return sha256(n.to_bytes(max(1, (n.bit_length() + 7) // 8), "big")).hexdigest()


def fraction_record(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def floor_log2_ratio(numerator: int, denominator: int) -> int:
    require(numerator > 0 and denominator > 0, "positive ratio required")
    k = numerator.bit_length() - denominator.bit_length()

    def at_least_power(exponent: int) -> bool:
        if exponent >= 0:
            return numerator >= (denominator << exponent)
        return (numerator << (-exponent)) >= denominator

    while not at_least_power(k):
        k -= 1
    while at_least_power(k + 1):
        k += 1
    return k


def ternary_exponent(target: int, precision: int) -> tuple[int, int]:
    if precision == 0:
        return 0, 1
    modulus = 3**precision
    require(target % 3 != 0, "ternary target must be a unit")
    period = 2 * 3 ** (precision - 1)
    inverse_two = pow(2, -1, modulus)
    value = 1
    for a0 in range(period):
        if (-value - target) % modulus == 0:
            return a0, period
        value = value * inverse_two % modulus
    raise RuntimeError("two did not generate the ternary unit group")


def find_cycle(case: dict, max_b: int) -> dict:
    target = Fraction(*case["real_target"])
    error = Fraction(*case["real_error"])
    k = case["binary_precision"]
    z = case["binary_residue"] % (1 << k)
    m = case["ternary_precision"]
    ternary_target = case["ternary_residue"]
    require(target > 0 and error > 0 and k >= 0 and m >= 0, "case domain")
    word, q, c, _ = prefix(z, k)
    a0, period = ternary_exponent(ternary_target, m)
    two_k = 1 << k
    three_q = 3**q
    upper = target + error
    after_w_upper_plus_one = (three_q * upper + c) / two_k + 1
    three_b = 1

    for b in range(1, max_b + 1):
        three_b *= 3
        if b < m:
            continue
        if (1 << b) <= after_w_upper_plus_one:
            continue
        numerator = three_b * (c + two_k) - (two_k << b)
        return_slope_numerator = three_q * three_b
        # Root equals target when 2^(K+b+a) equals this positive ratio.
        threshold_num = (
            return_slope_numerator * target.numerator
            + numerator * target.denominator
        )
        ideal_a = floor_log2_ratio(threshold_num, target.numerator) - k - b
        residue_lower = a0 + ((ideal_a - a0) // period) * period
        for a in (residue_lower, residue_lower + period):
            if a < 1:
                continue
            denominator = (1 << (k + a + b)) - return_slope_numerator
            if denominator <= 0:
                continue
            score = 8 * (q + b) - 5 * (k + a + b)
            if score <= 0:
                continue
            error_numerator = abs(
                numerator * target.denominator - target.numerator * denominator
            )
            if (
                error_numerator * error.denominator
                >= denominator * target.denominator * error.numerator
            ):
                continue
            root = Fraction(numerator, denominator)
            require(root.denominator > 1, "nonintegrality criterion")
            witness = {
                "target": target,
                "error": error,
                "k": k,
                "z": z,
                "m": m,
                "t": ternary_target,
                "word": word,
                "q": q,
                "c": c,
                "a": a,
                "b": b,
                "root": root,
                "score": score,
                "period": period,
                "a0": a0,
            }
            return witness
    raise RuntimeError(f"bounded witness search exhausted: {case!r}")


def check_cycle(witness: dict) -> dict:
    k, z, m, target3 = (witness[key] for key in ("k", "z", "m", "t"))
    a, b = witness["a"], witness["b"]
    root = witness["root"]
    target, error = witness["target"], witness["error"]
    numerator, denominator = root.numerator, root.denominator
    require(gcd(denominator, 6) == 1 and denominator > 1, "denominator domain")
    require((numerator - z * denominator) % (1 << k) == 0, "binary agreement")
    if m:
        require((numerator - target3 * denominator) % (3**m) == 0, "ternary agreement")
        require((a - witness["a0"]) % witness["period"] == 0, "exponent progression")
    require(abs(root - target) < error, "real neighborhood")

    full_word = witness["word"] + [1] * b + [0] * a
    current = numerator
    phase_numerators: list[int] = []
    odd_positions: list[int] = []
    after_w_numerator = numerator if k == 0 else None
    for index, bit in enumerate(full_word):
        require(current > 0 and current % 3 != 0, "positive ternary-unit phase")
        require(current & 1 == bit, "actual parity agrees with prescribed word")
        phase_numerators.append(current)
        if bit:
            odd_positions.append(index)
            require((3 * current + denominator) % 2 == 0, "odd-branch integrality")
            current = (3 * current + denominator) // 2
        else:
            require(current % 2 == 0, "even-branch integrality")
            current //= 2
        if index + 1 == k:
            after_w_numerator = current
    require(current == numerator, "exact cyclic return")
    require(after_w_numerator is not None, "after-w phase captured")
    require((after_w_numerator + denominator) % (1 << b) == 0, "long-run divisibility")
    upper = target + error
    a_slope = Fraction(3 ** witness["q"], 1 << k)
    b_offset = Fraction(witness["c"], 1 << k)
    require(
        denominator * (a_slope * upper + b_offset + 1) > (1 << b),
        "quantitative run denominator bound",
    )

    total_gap = 0
    length = len(full_word)
    for index, position in enumerate(odd_positions):
        next_position = odd_positions[(index + 1) % len(odd_positions)]
        gap = (next_position - position) % length or length
        odd_num = phase_numerators[position]
        exact_gap = valuation(3 * odd_num + denominator, 2)
        require(exact_gap == gap, "exact accelerated valuation")
        require(
            (3 * odd_num + denominator) // (1 << gap)
            == phase_numerators[next_position],
            "accelerated edge",
        )
        total_gap += gap
    require(total_gap == length, "lap gap sum")
    score = 8 * len(odd_positions) - 5 * total_gap
    require(score == witness["score"] and score > 0, "positive critical lap score")

    diagonal_checked = False
    if target.denominator == 1:
        n = target.numerator
        local_modulus = (1 << k) * 3**m
        difference_numerator = numerator - n * denominator
        if difference_numerator % local_modulus == 0:
            require(difference_numerator != 0, "noninteger root differs from integer")
            require(abs(difference_numerator) >= local_modulus, "AR2 integer threshold")
            require(denominator * error > local_modulus, "AR2 strict denominator growth")
            diagonal_checked = True

    return {
        "real_target": fraction_record(target),
        "real_error": fraction_record(error),
        "binary_precision": k,
        "binary_residue": z,
        "ternary_precision": m,
        "ternary_residue": target3,
        "a": a,
        "b": b,
        "prefix": "".join(map(str, witness["word"])),
        "shortcut_lap_length": length,
        "odd_lap_count": len(odd_positions),
        "critical_lap_score": score,
        "numerator_bits": numerator.bit_length(),
        "denominator_bits": denominator.bit_length(),
        "numerator_sha256_big_endian": integer_digest(numerator),
        "denominator_sha256_big_endian": integer_digest(denominator),
        "AR2_diagonal_bound_checked": diagonal_checked,
    }


def check_binary_and_ternary_interfaces() -> dict:
    binary_cases = 0
    for k in range(11):
        words = set()
        for residue in range(1 << k):
            word, _, _, _ = prefix(residue, k)
            words.add(tuple(word))
            binary_cases += 1
        require(len(words) == (1 << k), "parity-prefix bijection")
    ternary_units = 0
    for m in range(1, 8):
        modulus = 3**m
        period = 2 * 3 ** (m - 1)
        values = {pow(2, exponent, modulus) for exponent in range(period)}
        require(len(values) == period, "primitive root order")
        require(values == {x for x in range(modulus) if x % 3}, "full ternary unit group")
        ternary_units += len(values)
    return {"binary_residue_cases": binary_cases, "ternary_unit_cases": ternary_units}


def check_fixed_source_pins(limit: int, horizon: int) -> dict:
    checked = returns = completions = 0
    for source in range(1, limit + 1):
        current, q, c = source, 0, 0
        for k in range(1, horizon + 1):
            if current & 1:
                c = 3 * c + (1 << (k - 1))
                q += 1
            current = t_step(current)
            require((1 << k) * current == 3**q * source + c, "ordinary affine identity")
            if not q:
                continue
            d_raw = (1 << k) - 3**q
            pin = Fraction(c, d_raw)
            h = current - source
            common = gcd(c, abs(d_raw))
            require(common == gcd(h, abs(d_raw)), "FS1 gcd identity")
            require(pin.denominator == abs(d_raw) // common, "FS1 full reduced denominator")
            require(pin - source == Fraction((1 << k) * h, d_raw), "FS1 pin difference")
            if h:
                u, v = valuation(h, 2), valuation(h, 3)
                residue_integer = Fraction(
                    pin.denominator * abs(pin - source), (1 << (k + u)) * 3**v
                )
                require(residue_integer.denominator == 1 and residue_integer >= 1, "FS1 exact integer obstruction")
                require(
                    residue_integer == abs(h) // ((1 << u) * 3**v * common),
                    "FS1 residual factor",
                )
                require(valuation((pin - source).numerator, 2) == k + u, "FS1 exact binary precision")
                require(valuation((pin - source).numerator, 3) == v, "FS1 exact ternary precision")
                checked += 1
            else:
                require(pin == source and pin.denominator == 1, "actual return pin")
                returns += 1

            if source <= 32 and k <= 16:
                for a in range(1, 5):
                    for b in range(1, 5):
                        big_c = 3**b * (c + (1 << k)) - (1 << (k + b))
                        big_d = (1 << (k + a + b)) - 3 ** (q + b)
                        root = Fraction(big_c, big_d)
                        exact_equation = 3**b * (current + 1) == (1 << b) * (source * (1 << a) + 1)
                        require((root == source) == exact_equation, "completion equation iff")
                        if exact_equation:
                            require(b == valuation(current + 1, 2), "available odd-run constraint")
                        completions += 1
    return {
        "sources": limit,
        "shortcut_horizon": horizon,
        "nonreturn_prefix_checks": checked,
        "actual_return_controls": returns,
        "completion_equation_checks": completions,
    }


def check_critical_products(limit: int, horizon: int) -> dict:
    sources = products = 0
    for source in range(1, limit + 1, 2):
        if source % 3 == 0:
            continue
        values = [source]
        accumulated = [0]
        seen = {source}
        for _ in range(horizon):
            n = values[-1]
            a = valuation(3 * n + 1, 2)
            nxt = (3 * n + 1) // (1 << a)
            if nxt in seen:
                break
            values.append(nxt)
            accumulated.append(accumulated[-1] + a)
            seen.add(nxt)
        lambdas = [Fraction(1 << exponent, 3**j) for j, exponent in enumerate(accumulated)]
        scaled = [lam * n for lam, n in zip(lambdas, values)]
        for j in range(len(values) - 1):
            require(scaled[j + 1] - scaled[j] == lambdas[j] / 3, "scaled-height increment")
        # Algebraic control only: all future exponents are formally set to 1.
        # This is not claimed to extend the actual parity orbit.
        formal_limit = scaled[-1] + lambdas[-1]
        for j, (n, exponent, lam, scaled_height) in enumerate(zip(values, accumulated, lambdas, scaled)):
            p, q = (1 << exponent) * n, 3**j
            require(gcd(p, q) == 1 and valuation(p, 2) == exponent, "primitive pair")
            product = abs(formal_limit * q - p) * q * Fraction(1, (1 << exponent) * 3**j)
            require(product == (formal_limit - scaled_height) / lam, "critical product identity")
            require(product >= 1, "critical positive-tail floor")
            height = max(p, q)
            require(product / height**2 >= Fraction(1, height**2), "normalized critical scale")
            available_run = valuation(n + 1, 2)
            if j + available_run < len(values):
                require(
                    product >= 1 + Fraction(2, 3) ** available_run,
                    "strict floor from the first actual gap greater than one",
                )
            products += 1
        sources += 1
    return {
        "ordinary_unit_sources": sources,
        "maximum_odd_prefix_length": horizon,
        "exact_product_checks": products,
        "future_control": "formal valuation-one continuation; not asserted to be an actual orbit",
    }


CASES = [
    {"real_target": (1, 1), "real_error": (1, 4), "binary_precision": 0, "binary_residue": 0, "ternary_precision": 0, "ternary_residue": 1},
    {"real_target": (1, 1), "real_error": (1, 8), "binary_precision": 4, "binary_residue": 1, "ternary_precision": 1, "ternary_residue": 1},
    {"real_target": (5, 1), "real_error": (1, 4), "binary_precision": 6, "binary_residue": 5, "ternary_precision": 2, "ternary_residue": 5},
    {"real_target": (7, 1), "real_error": (1, 4), "binary_precision": 8, "binary_residue": 7, "ternary_precision": 3, "ternary_residue": 7},
    {"real_target": (25, 1), "real_error": (1, 2), "binary_precision": 9, "binary_residue": 25, "ternary_precision": 3, "ternary_residue": 25},
    {"real_target": (13, 7), "real_error": (1, 40), "binary_precision": 6, "binary_residue": 5, "ternary_precision": 3, "ternary_residue": 2},
    {"real_target": (11, 3), "real_error": (1, 20), "binary_precision": 7, "binary_residue": 0, "ternary_precision": 2, "ternary_residue": 8},
    {"real_target": (2, 5), "real_error": (1, 40), "binary_precision": 5, "binary_residue": 18, "ternary_precision": 3, "ternary_residue": 11},
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-b", type=int, default=40000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    require(args.max_b >= 1, "positive max-b required")
    cycles = [check_cycle(find_cycle(case, args.max_b)) for case in CASES]
    report = {
        "status": "PASS",
        "arithmetic": "integers and fractions only; checks active under -OO",
        "scope": "finite interfaces and witnesses; no claim of integer nonconvergence or global closure",
        "cycle_cases": cycles,
        "cycle_case_count": len(cycles),
        "total_shortcut_edges": sum(case["shortcut_lap_length"] for case in cycles),
        "total_accelerated_edges": sum(case["odd_lap_count"] for case in cycles),
        "interfaces": check_binary_and_ternary_interfaces(),
        "fixed_source_pins": check_fixed_source_pins(400, 80),
        "critical_products": check_critical_products(1000, 80),
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
