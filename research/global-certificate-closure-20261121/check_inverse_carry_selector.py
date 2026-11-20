#!/usr/bin/env python3
"""Exact controls for the all-H inverse-carry selector obstruction.

The universal proof is INVERSE_CARRY_SELECTOR.md. This standalone checker
certifies its integer constants, exact source witnesses, valuations, finite
endpoint decisions, and positive ordinary-return controls. It does not
simulate the fivefold targets of the obstruction family.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
E = (2, 1, 1, 1, 2, 1, 7)
F = (3, 6, 1, 2, 1, 1, 1)


class CheckFailure(RuntimeError):
    pass


def require(ok, message):
    if not ok:
        raise CheckFailure(message)


def valuation(n, prime):
    require(n != 0, "valuation at zero")
    n = abs(n)
    if prime == 2:
        return (n & -n).bit_length() - 1
    value = 0
    while n % prime == 0:
        n //= prime
        value += 1
    return value


def U(n):
    require(n > 0 and n % 2 == 1, "nonpositive or even odd input")
    numerator = 3 * n + 1
    exponent = valuation(numerator, 2)
    return numerator >> exponent, exponent


def replay(n, word, first_hit=False):
    value = n
    require(value > 0 and value % 2, "invalid certificate start")
    for exponent in word:
        require(isinstance(exponent, int) and exponent > 0, "invalid exponent")
        if first_hit:
            require(value != 1, "early first hit")
        value, actual = U(value)
        require(exponent == actual, "false division exponent")
    if first_hit:
        require(value == 1, "certificate does not end at one")
    return value


def words(r, b):
    require(r >= 0 and b >= 2, "invalid carry parameters")
    return E + (1,) * r + (3, b), F + (1,) * r + (4, b - 1)


def correction(word):
    result = 0
    clock = 0
    for j, exponent in enumerate(word):
        result += 3 ** (len(word) - 1 - j) * 2 ** clock
        clock += exponent
    return result, clock


def carry_numerator(q, r, b):
    return (q << (r + b + 18)) - 1351 * 3 ** (r + 5) - (1 << (r + 16))


def finite_inverse_selector(q, require_unit=True):
    """Complete finite decision justified by IC2, not a guessed search cap."""
    require(q >= 5 and q % 2 and q % 3, "selector endpoint guard")
    maximum_r = (81 * q + 1350).bit_length() - 17
    choices = []
    inspected = 0
    for b in range(2, max(2, maximum_r)):
        inspected += 1
        numerator = (q << (b + 2)) - 1
        ternary_order = valuation(numerator, 3)
        r = ternary_order - 5
        if r < 0 or r > maximum_r or b >= r:
            continue
        D = numerator // (3 ** ternary_order)
        source_numerator = (D << (r + 16)) - 1351
        if source_numerator % 81:
            continue
        x = source_numerator // 81
        if not (0 < x < q) or (require_unit and x % 3 == 0):
            continue
        require(x % 2, "integral inverse unexpectedly even")
        source, target = words(r, b)
        require(replay(x, source) == q, "source ordinary endpoint")
        require(replay(5 * x, target) == 5 * q, "target ordinary endpoint")
        require(carry_numerator(q, r, b) == 3 ** (r + 9) * x,
                "full inverse numerator")
        choices.append({"r": r, "b": b, "x": x})
    return {"maximum_r": maximum_r, "b_values_inspected": inspected,
            "eligible_returns": choices}


def source_at_height(H):
    exponent = 3 ** H + 1
    numerator = (1 << exponent) - 1
    require(numerator % 3 == 0, "rank-one source integrality")
    q = numerator // 3
    require(q > 1 and q % 2 and q % 3, "rank-one source unit guard")
    require(replay(q, (exponent,), first_hit=True) == 1,
            "rank-one supplied certificate")
    return q, exponent


def obstruction_controls():
    rows = []
    complete_decisions = []
    for H in range(4, 10):
        q, exponent = source_at_height(H)
        M = 3 ** (H - 1)
        t = 1 << M
        z = t + 1
        bracket = -9 + 12 * z - 8 * z * z + 2 * z ** 3
        require(valuation(q + 1, 3) == H, "endpoint minus-one precision")
        require(valuation(z, 3) == H, "cubing valuation")
        require(valuation(bracket, 3) == 2, "bracket exact valuation")
        require(3 * (t * q - 1) == z * bracket, "factorization identity")
        require(valuation(t * q - 1, 3) == H + 1, "forced carry valuation")
        require(81 * q + 1351 == 54 * (1 << (3 ** H)) + 1324,
                "exact binary height comparison")
        require(81 * q + 1351 < (1 << (3 ** H + 6)), "binary height cutoff")
        maximum_r = (81 * q + 1350).bit_length() - 17
        require(maximum_r <= 3 ** H - 11, "integer run cutoff")
        require(M - 2 > H - 4, "forced b exceeds forced r")
        rows.append({"H": H, "q_bits": q.bit_length(),
                     "supplied_first_hit_exponent": exponent,
                     "v3_q_plus_one": H, "v3_t_plus_one": H,
                     "v3_bracket": 2, "v3_tq_minus_one": H + 1,
                     "forced_r": H - 4, "forced_b": M - 2,
                     "maximum_r_from_strict_height": maximum_r})
        if H <= 8:
            # The stronger theorem excludes integral inverse sources even
            # without the ternary-unit restriction, so omit that restriction.
            decision = finite_inverse_selector(q, require_unit=False)
            require(not decision["eligible_returns"], "obstructed endpoint returned a source")
            complete_decisions.append({"H": H, **decision})
    return rows, complete_decisions


def endpoint_for_parameters(r, b, require_source_unit=True):
    B = 1351 * 3 ** (r + 5) + 2 ** (r + 16)
    clock = r + b + 18
    modulus = 3 ** (r + 9)
    q = (B * pow(pow(2, clock, modulus), -1, modulus)) % modulus
    if q % 2 == 0:
        q += modulus
    for _ in range(3):
        numerator = carry_numerator(q, r, b)
        require(numerator % modulus == 0, "constructed endpoint integrality")
        x = numerator // modulus
        if x > 0 and (not require_source_unit or x % 3):
            return q, x
        q += 2 * modulus
    raise CheckFailure("positive unit control not obtained")


def positive_controls():
    rows = []
    for r, b in ((10, 2), (12, 3), (14, 4)):
        q, x = endpoint_for_parameters(r, b)
        require(0 < x < q and x % 2 and x % 3, "positive descent control")
        source, target = words(r, b)
        require(replay(x, source) == q and replay(5 * x, target) == 5 * q,
                "positive-control ordinary pair")
        result = finite_inverse_selector(q)
        require(any(c == {"r": r, "b": b, "x": x} for c in result["eligible_returns"]),
                "finite selector missed a legal positive return")
        rows.append({"r": r, "b": b, "q": q, "x": x,
                     "ratio_x_over_q": str(Fraction(x, q)),
                     "source_word": list(source), "target_word": list(target),
                     "selector_return_count": len(result["eligible_returns"])})
    return rows


def congruence_without_height_control():
    """A solved inverse congruence at an obstructed q does not pay height."""
    H, r = 4, 0
    q, exponent = source_at_height(H)
    modulus = 3 ** (r + 9)
    B = 1351 * 3 ** (r + 5) + 2 ** (r + 16)
    period = 2 * 3 ** (r + 8)
    power = pow(2, r + 2 + 18, modulus) * (q % modulus) % modulus
    selected = None
    for b in range(2, 2 + period):
        if power == B % modulus:
            selected = b
            break
        power = 2 * power % modulus
    require(selected is not None, "inverse congruence control missing")
    x = carry_numerator(q, r, selected) // modulus
    source, target = words(r, selected)
    require(replay(x, source) == q and replay(5 * x, target) == 5 * q,
            "large ordinary inverse control")
    # Preserve q's supplied witness in the actual source certificate.
    require(replay(x, source + (exponent,), first_hit=True) == 1,
            "antecedent certificate was not preserved")
    require(x > q, "large congruence incorrectly counted as descent")
    return {"H": H, "r": r, "b": selected,
            "q_bits": q.bit_length(), "x_bits": x.bit_length(),
            "ordinary_inverse_integral": True, "strict_height_guard_satisfied": False,
            "supplied_q_certificate_preserved": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "inverse_carry_selector_expected.json")
    args = parser.parse_args()
    coefficient = 5 * 2 ** 18 - 5 * 3 ** 9 - 1351 * 3 ** 5 - 2 ** 16
    require(coefficient == 818476 and coefficient > 0, "height-lemma coefficient")
    require(2 ** 18 > 3 ** 9, "positive coefficient before substituting q>=5")
    for j in range(10):
        require(valuation((1 << (3 ** j)) + 1, 3) == j + 1,
                "exact cubing control")
    for r in range(25):
        for b in (2, 3, 7):
            source, target = words(r, b)
            B, L = correction(source)
            Bt, Lt = correction(target)
            require(B == 1351 * 3 ** (r + 5) + 2 ** (r + 16), "carry correction")
            require(Bt == 5 * B and Lt == L == r + b + 18, "paired carry correction")
    obstruction, decisions = obstruction_controls()
    rejected = []
    q, exponent = source_at_height(4)
    try:
        replay(q, (exponent - 1,), first_hit=True)
    except CheckFailure:
        rejected.append("false supplied rank-one exponent")
    else:
        raise CheckFailure("false supplied certificate accepted")
    try:
        finite_inverse_selector(3)
    except CheckFailure:
        rejected.append("ternary nonunit endpoint")
    else:
        raise CheckFailure("ternary nonunit endpoint accepted")
    report = {
        "status": "PASS: scoped inverse-selector obstruction; no target nonconvergence claim",
        "source_pin_PR170": "656063d5efa0f5708356ab2563a4348d39bae013",
        "proof_sha256": hashlib.sha256((HERE / "INVERSE_CARRY_SELECTOR.md").read_bytes()).hexdigest(),
        "height_lemma_positive_coefficient": coefficient,
        "symbolic_correction_controls": 75,
        "obstruction_family_controls": obstruction,
        "complete_finite_selector_decisions": decisions,
        "positive_eligible_return_controls": positive_controls(),
        "congruence_without_height_control": congruence_without_height_control(),
        "rejected_controls": rejected,
        "all_q_successful_selector_proved": False,
        "fivefold_targets_asserted_nonconvergent": False,
        "full_collatz_proved": False,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    args.output.write_text(rendered)
    print(json.dumps({"status": report["status"],
                      "obstruction_H_controls": [row["H"] for row in obstruction],
                      "complete_endpoint_decisions": [row["H"] for row in decisions],
                      "positive_return_controls": len(report["positive_eligible_return_controls"]),
                      "proof_sha256": report["proof_sha256"],
                      "report_sha256": hashlib.sha256(rendered.encode()).hexdigest()},
                     sort_keys=True))


if __name__ == "__main__":
    main()
