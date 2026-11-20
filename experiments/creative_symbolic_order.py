#!/usr/bin/env python3
"""Exact bounded checks for CSO-001--CSO-005; no Collatz resolution.

All verification gates remain active under optimized Python. The universal
order obstructions are written proofs, not conclusions of the finite menus.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import cache
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import random


RULES = (("ad", "d"), ("bd", "gd"), ("ae", "ea"), ("af", "eb"),
         ("ag", "fa"), ("be", "fb"), ("bf", "ga"), ("bg", "gb"),
         ("ce", "cb"), ("cf", "caa"), ("cg", "cab"))
ADMIN = RULES[2:]
LETTERS = "abefg"
AFFINE = {
    "a": (((1, 1), (1, 0)), (0, 0)),
    "b": (((1, 3), (3, 4)), (1, 1)),
    "c": (((1, 5), (0, 0)), (0, 0)),
    "d": (((1, 0), (1, 0)), (1, 1)),
    "e": (((7, 2), (2, 5)), (2, 1)),
    "f": (((2, 1), (1, 1)), (1, 0)),
    "g": (((2, 2), (2, 4)), (0, 2)),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def identity(dimension):
    return [[int(i == j) for j in range(dimension)] for i in range(dimension)]


def multiply(a, b):
    size = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(size))
             for j in range(size)] for i in range(size)]


def difference(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def augment(a, offset):
    return [list(row) + [offset[i]] for i, row in enumerate(a)] + [[0, 0, 1]]


MATRICES = {s: augment(*v) for s, v in AFFINE.items()}


def interpret_matrix(word):
    result = identity(3)
    for symbol in word:
        result = multiply(result, MATRICES[symbol])
    return result


@cache
def matrix_rank(word):
    x = y = 0
    for symbol in reversed(word):
        a, offset = AFFINE[symbol]
        x, y = a[0][0] * x + a[0][1] * y + offset[0], a[1][0] * x + a[1][1] * y + offset[1]
    return x


@cache
def inspect_word(word):
    require(word.startswith("c") and word.endswith("d") and
            all(s in LETTERS for s in word[1:-1]), "improper word")
    value = 1
    potential = 0
    for symbol in word[1:-1]:
        if symbol in "efg":
            potential += value.bit_length()
            value = 3 * value + "efg".index(symbol)
        else:
            value = 2 * value + int(symbol == "b")
    return value, potential


def canonical(n):
    return "c" + bin(n)[3:].translate(str.maketrans("01", "ab")) + "d"


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def odd_step(n):
    numerator = 3 * n + 1
    exponent = (numerator & -numerator).bit_length() - 1
    return numerator >> exponent, exponent


def administrative_envelope(n):
    result = 0
    while n >= 3:
        n //= 3
        result += n.bit_length()
    return result


def occurrences(word, rules=RULES):
    return [(i, left, right) for i in range(len(word) - 1)
            for left, right in rules if word.startswith(left, i)]


def apply(word, occurrence):
    i, left, right = occurrence
    return word[:i] + right + word[i + len(left):]


def word_corpus(maximum):
    for length in range(maximum + 1):
        for interior in product(LETTERS, repeat=length):
            yield "c" + "".join(interior) + "d"


def check_rule_certificates():
    deltas = {}
    for left, right in RULES:
        lhs, rhs = interpret_matrix(left), interpret_matrix(right)
        delta = difference(lhs, rhs)
        deltas[f"{left}->{right}"] = delta
        if left != "af":
            require(all(v >= 0 for row in delta for v in row), "negative weak rule coefficient")
            require(delta[0][-1] >= 1, "missing strict first-coordinate constant")
        else:
            require(any(v < 0 for row in delta for v in row), "exceptional rule incorrectly removed")
            require(all(rhs[i][j] <= 26 * lhs[i][j] for i in range(3) for j in range(3)),
                    "factor-26 majorant failed")
            require(any(rhs[i][j] > 25 * lhs[i][j] for i in range(3) for j in range(3)),
                    "factor-25 coefficient control unexpectedly passed")
    require(all(m[0][0] >= 1 for m in MATRICES.values()), "context monotonicity interface")
    return {"all_rule_difference_matrices": deltas, "strict_rules": 10,
            "exceptional_rule": "af->eb", "proved_multiplicative_majorant": 26,
            "factor_25_coefficientwise_control_rejected": True}


def check_complete_words():
    words = edges = 0
    counts = Counter()
    for word in word_corpus(5):
        value, h = inspect_word(word)
        bits = value.bit_length()
        require(h <= administrative_envelope(value) <= bits * (bits - 1) // 2,
                "administrative envelope failed")
        require(matrix_rank(word) <= 6 * 11 ** (bits - 1), "mixed source rank bound")
        for item in occurrences(word):
            _, left, _ = item
            new_word = apply(word, item)
            new_value, new_h = inspect_word(new_word)
            cost = 0
            if left in ("ad", "bd"):
                require(value > 1 and new_value == shortcut(value), "dynamic ordinary value mismatch")
                cost = 1 if left == "ad" else bits
            else:
                require(new_value == value, "administrative ordinary value mismatch")
            require(1 == h - new_h + cost, "exact one-step work balance failed")
            before, after = matrix_rank(word), matrix_rank(new_word)
            require(after <= 26 * before if left == "af" else after < before,
                    "contextual matrix rank change failed")
            counts[left] += 1
            edges += 1
        words += 1
    normalizations = normal_steps = 0
    for initial in word_corpus(3):
        value, h = inspect_word(initial)
        for mode in range(3):
            word = initial
            steps = 0
            while True:
                options = occurrences(word, ADMIN)
                if not options:
                    break
                index = 0 if mode == 0 else (-1 if mode == 1 else steps % len(options))
                word = apply(word, options[index])
                steps += 1
                require(steps <= h, "administrative schedule exceeded exact clock")
            require(word == canonical(value) and steps == h, "normal form or exact clock mismatch")
            normalizations += 1
            normal_steps += steps
    for exponent in range(129):
        value, h = inspect_word("c" + "e" * exponent + "d")
        require(value == 3 ** exponent and h == administrative_envelope(value), "power-of-three sharpness failed")
    return {"proper_words_in_complete_corpus": words, "maximum_interior_length": 5,
            "all_applicable_rule_occurrences": edges, "occurrences_by_left_side": dict(sorted(counts.items())),
            "complete_administrative_schedules": normalizations,
            "administrative_rewrite_steps": normal_steps,
            "sharp_power_of_three_envelopes": 129}


@cache
def certified_ordinary_cost(n):
    cost = steps = 0
    while n != 1:
        cost += 1 if n % 2 == 0 else n.bit_length()
        n = shortcut(n)
        steps += 1
        require(steps < 100000, "bounded ordinary-cost replay exhausted")
    return cost


def check_controllers():
    values = list(range(1, 49)) + [97, 127, 129, 171, 255, 257, 5461]
    sources = [canonical(n) for n in values] + list(word_corpus(2))
    outcomes = Counter()
    total_steps = maximum_steps = used_carries = dynamic_steps = 0
    for initial in sources:
        original_value, original_h = inspect_word(initial)
        if initial == canonical(original_value):
            require(matrix_rank(initial) <= 6 * 8 ** (original_value.bit_length() - 1) <= 6 * original_value ** 3,
                    "canonical cubic rank bound")
        for allowance in (0, 1, 4):
            for mode in range(3):
                word, remaining, steps, ordinary_cost = initial, allowance, 0, 0
                initial_rank = 26 ** allowance * matrix_rank(initial) + allowance
                while True:
                    options = [o for o in occurrences(word) if o[1] != "af" or remaining > 0]
                    if not options:
                        break
                    index = 0 if mode == 0 else (-1 if mode == 1 else steps % len(options))
                    chosen = options[index]
                    old_value, _ = inspect_word(word)
                    before = 26 ** remaining * matrix_rank(word) + remaining
                    word = apply(word, chosen)
                    if chosen[1] == "af":
                        remaining -= 1
                        used_carries += 1
                    if chosen[1] in ("ad", "bd"):
                        ordinary_cost += 1 if chosen[1] == "ad" else old_value.bit_length()
                        dynamic_steps += 1
                    after = 26 ** remaining * matrix_rank(word) + remaining
                    require(after < before, "nonlinear controller rank did not decrease")
                    steps += 1
                    require(steps < 50000 and steps <= initial_rank, "bounded controller replay exhausted")
                    require(steps == original_h - inspect_word(word)[1] + ordinary_cost,
                            "full-prefix exact work balance")
                if word == "cd":
                    require(steps == original_h + certified_ordinary_cost(original_value),
                            "complete schedule length depends on scheduling")
                    outcomes["reached_one"] += 1
                else:
                    require(remaining == 0 and any(o[1] == "af" for o in occurrences(word)),
                            "incorrect unresolved outcome")
                    outcomes["unresolved_carry_budget"] += 1
                total_steps += steps
                maximum_steps = max(maximum_steps, steps)
    require(outcomes["unresolved_carry_budget"] > 0, "missing real failed-guard control")
    return {"source_words": len(sources), "allowances": [0, 1, 4], "scheduling_modes": 3,
            "controller_runs": sum(outcomes.values()), "outcomes": dict(sorted(outcomes.items())),
            "literal_rewrite_steps": total_steps, "dynamic_steps": dynamic_steps,
            "exceptional_carry_steps": used_carries, "maximum_single_run_rewrites": maximum_steps}


def check_collapse_algebra():
    degree_survivors = []
    for a, b, e, f, g in product(range(1, 9), repeat=5):
        if g >= f and e >= f and a * f >= e * b and b * f >= g * a and f >= a * a and b >= g:
            degree_survivors.append([a, b, e, f, g])
    require(degree_survivors == [[1, 1, 1, 1, 1]], "degree/slopes bounded negative control")
    offset_survivors = []
    for a, b, e, f, g in product(range(7), repeat=5):
        if g >= a + b and b >= g and g >= f and e >= f and a + f >= e + b:
            offset_survivors.append([a, b, e, f, g])
    require(offset_survivors == [[0, 0, 0, 0, 0]], "offset bounded negative control")
    # Exact nonnegative zero-sum identities for the written leading-term proof.
    degree_log_rows = [(0, 0, 0, -1, 1), (0, 0, 1, -1, 0),
                       (1, -1, -1, 1, 0), (-1, 1, 0, 1, -1)]
    require(all(sum(row[j] for row in degree_log_rows) == 0 for j in range(5)),
            "degree log cancellation certificate")
    beta_negative = (0, -1, 0)
    beta_minus_alpha = (-1, 1, 0)
    alpha_plus_beta = (1, 1, 0)
    require(tuple(2 * beta_negative[i] + beta_minus_alpha[i] + alpha_plus_beta[i]
                  for i in range(3)) == (0, 0, 0), "polynomial energy zero-sum certificate")
    generator = random.Random(20261120)
    band_checks = 0
    for dimension in range(2, 10):
        for distance in range(1, dimension):
            for _ in range(5):
                interiors = []
                for _symbol in range(5):
                    mat = identity(dimension)
                    for i in range(dimension):
                        for j in range(i + distance, dimension):
                            mat[i][j] = generator.randrange(4)
                    interiors.append(mat)
                a, b, e, f, g = interiors
                c = [[generator.randrange(1, 4) if i == j else
                      (generator.randrange(4) if i < j else 0)
                      for j in range(dimension)] for i in range(dimension)]
                d = [[generator.randrange(1, 4) if i == j else
                      (generator.randrange(4) if i < j else 0)
                      for j in range(dimension)] for i in range(dimension)]
                ab = multiply(a, b)
                left_boundary = multiply(c, difference(g, ab))
                right_boundary = multiply(difference(b, g), d)
                for i in range(dimension - distance):
                    j = i + distance
                    require(ab[i][j] == a[i][j] + b[i][j], "first-band additivity")
                    require(left_boundary[i][j] == c[i][i] * (g[i][j] - a[i][j] - b[i][j]),
                            "left-boundary first-band cancellation")
                    require(right_boundary[i][j] == (b[i][j] - g[i][j]) * d[j][j],
                            "right-boundary first-band cancellation")
                    band_checks += 1
    # Constant boundaries can hide a locally strict comparison in context.
    degenerate = {"a": (1, 1), "b": (1, 1), "e": (1, 0), "f": (1, 0),
                  "g": (1, 0), "c": (0, 0), "d": (0, 0)}
    def affine_word(word):
        slope, offset = 1, 0
        for symbol in reversed(word):
            a, b = degenerate[symbol]
            slope, offset = a * slope, a * offset + b
        return slope, offset
    for left, right in RULES:
        a, b = affine_word(left)
        c, d = affine_word(right)
        require(a >= c and b >= d, "constant-boundary scope control")
    require(affine_word("ad")[1] > affine_word("d")[1] and affine_word("cad") == affine_word("cd"),
            "constant left context should erase strictness")
    return {"bounded_degree_and_slope_assignments": 8 ** 5, "degree_survivors": degree_survivors,
            "bounded_offset_assignments": 7 ** 5, "offset_survivors": offset_survivors,
            "exact_zero_sum_identities": 2, "first_superdiagonal_identity_checks": band_checks,
            "matrix_dimensions": [2, 9], "constant_boundary_strictness_erasure_checked": True,
            "scope": "finite checks exercise identities; unbounded exclusions are the written proofs"}


def run_lengths(n):
    result = []
    for digit in bin(n)[2:]:
        if result and result[-1][0] == digit:
            result[-1][1] += 1
        else:
            result.append([digit, 1])
    return result


def energy(n, digit, degree):
    return sum(length ** degree for bit, length in run_lengths(n) if bit == digit)


def check_carry_families():
    odd_parameters = list(range(3, 130, 2)) + [257, 1025]
    even_parameters = list(range(4, 130, 2)) + [256, 1024]
    power_checks = 0
    for m in odd_parameters:
        k = (m - 1) // 2
        n = ((1 << (m + 2)) - 5) // 3
        target = (1 << m) - 1
        require(odd_step(n) == (target, 2), "one-run collapse ordinary edge")
        require(bin(n)[2:] == "10" * (k - 1) + "1001", "one-run collapse source pattern")
        require(n.bit_length() == m + 1 and target.bit_length() == m, "one-run bitlengths")
        require(energy(n, "1", 2) + energy(n, "0", 2) == m + 3, "one-run square energy")
        for degree in range(2, 9):
            require(energy(n, "1", degree) == k + 1, "source one-run moments")
            require(energy(n, "0", degree) == k - 1 + 2 ** degree, "source zero-run moments")
            require(energy(target, "1", degree) == m ** degree, "target one-run moments")
            power_checks += 1
    for m in even_parameters:
        k = m // 2
        n = ((1 << (m + 1)) + 1) // 3
        target = (1 << m) + 1
        require(odd_step(n) == (target, 1), "zero-run collapse ordinary edge")
        require(bin(n)[2:] == "10" * (k - 1) + "11", "zero-run collapse source pattern")
        require(n.bit_length() == m and target.bit_length() == m + 1, "zero-run bitlengths")
        require(energy(n, "1", 2) + energy(n, "0", 2) == m + 2, "zero-run square energy")
        for degree in range(2, 9):
            require(energy(n, "1", degree) == k - 1 + 2 ** degree, "source one-run moments")
            require(energy(n, "0", degree) == k - 1, "source zero-run moments")
            require(energy(target, "0", degree) == (m - 1) ** degree, "target zero-run moments")
            power_checks += 1
    for m in range(3, 130):
        n, target = (1 << m) - 1, 3 * (1 << (m - 1)) - 1
        require(odd_step(n) == (target, 1), "Mersenne ordinary edge")
        for degree in range(2, 9):
            require(energy(target, "1", degree) == (m - 1) ** degree + 1, "Mersenne energy change")
            require(energy(target, "0", degree) == 1, "Mersenne zero run")
            power_checks += 1
    return {"one_run_collapse_edges": len(odd_parameters), "zero_run_collapse_edges": len(even_parameters),
            "Mersenne_edges": 127, "run_moment_degrees": [2, 8], "moment_identity_checks": power_checks,
            "largest_parameter_m": 1025}


def build_report():
    return {"schema": "creative-symbolic-order-v1", "status": "PASS",
            "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            "claims": ["CSO-001", "CSO-002", "CSO-003", "CSO-004", "CSO-005"],
            "scope": "exact symbolic local certificates and bounded replay; no total Collatz order",
            "rule_certificates": check_rule_certificates(),
            "word_checks": check_complete_words(), "controllers": check_controllers(),
            "order_class_checks": check_collapse_algebra(), "carry_families": check_carry_families(),
            "limitations": ["A finite carry allowance may return UNRESOLVED.",
                            "No source-dependent sufficient allowance or total ordinary cost function is proved.",
                            "Finite degree and matrix menus are not the basis of the unbounded impossibility claims.",
                            "The two-dimensional ten-rule interpretation is attributed to AYH Example 4.3."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--output", type=Path)
    modes.add_argument("--compare", type=Path)
    args = parser.parse_args()
    if args.output and args.output.exists():
        parser.error("output already exists")
    report = build_report()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.compare:
        require(args.compare.read_text(encoding="utf-8") == rendered, "frozen report differs")
        print("PASS: exact report regeneration")
    elif args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8", newline="\n") as target:
            target.write(rendered)
        print(f"PASS: wrote {args.output}")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
