#!/usr/bin/env python3
"""Exact, bounded controls for the literature-directed fourth checkpoint.

These are ordinary finite trajectories and exact rational/integer calculations.
They do not construct an escaping orbit, sample a hypothetical canonical flow,
or verify the universal Collatz conjecture. Guards survive python -O.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import comb
from pathlib import Path

from verify_triadic import verify_triadic


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest_integer(n):
    return sha256(n.to_bytes(max(1, (n.bit_length() + 7) // 8), "big")).hexdigest()


def shortcut(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def odd_step(n):
    value = 3 * n + 1
    gap = (value & -value).bit_length() - 1
    return value >> gap, gap


def carry(word):
    c = 0
    for i, bit in enumerate(word):
        c = 3 * c + (1 << i) if bit else c
    return c


def gap_carry(gaps):
    c, a = 0, 0
    for gap in gaps:
        c = 3 * c + (1 << a)
        a += gap
    return c, a


def rotate(word, i):
    return word[i:] + word[:i]


def de_bruijn(alphabet_size, order):
    a = [0] * (alphabet_size * order + 1)
    answer = []

    def visit(t, p):
        if t > order:
            if order % p == 0:
                answer.extend(a[1:p + 1])
            return
        a[t] = a[t - p]
        visit(t + 1, p)
        for letter in range(a[t - p] + 1, alphabet_size):
            a[t] = letter
            visit(t + 1, t)

    visit(1, 1)
    require(len(answer) == alphabet_size ** order, "de Bruijn length")
    return answer


def normalize_period(gaps):
    ratios = [Fraction(1)]
    for gap in gaps:
        ratios.append(ratios[-1] * Fraction(1 << gap, 3))
    require(ratios[-1] < 1, "period must have expanding forward coefficient")
    cut = max(range(len(gaps)), key=lambda i: ratios[i])
    result = rotate(gaps, cut)
    ratio = Fraction(1)
    for gap in result:
        ratio *= Fraction(1 << gap, 3)
        require(ratio <= 1, "normalized prefix coefficient")
    return result


def finite_periodic_control(labels, order, precision, sample_size, floor):
    require(order >= 1 and precision >= 1 and sample_size >= 1 and floor >= 1, "positive input parameters")
    script = normalize_period([labels[a] for a in de_bruijn(len(labels), order)])
    period = len(script)
    ratios = [Fraction(1)]
    for gap in script:
        ratios.append(ratios[-1] * Fraction(1 << gap, 3))
    carry_constant = 1 / min(ratios[:-1])
    require(sample_size % period == 0, "whole periods required")
    warmup = max(precision, order)
    total = warmup + sample_size + order - 1
    gaps = [script[i % period] for i in range(total)]
    full_carry, clock = gap_carry(gaps)
    binary_modulus = 1 << (clock + 1)
    # The final odd bit is retained, not just the preceding shortcut word.
    residue = (((1 << clock) - full_carry)
               * pow(pow(3, total, binary_modulus), -1, binary_modulus)) % binary_modulus
    source = residue + binary_modulus * ((1 - residue) * pow(binary_modulus, -1, 3) % 3)
    lattice = 3 * binary_modulus
    if source < floor:
        source += ((floor - source - 1) // lattice + 1) * lattice
    first_source = source
    lifts = 0
    while True:
        values = [source]
        for index, gap in enumerate(gaps):
            value, actual_gap = odd_step(values[-1])
            require(actual_gap == gap, ("actual prescribed gap", index))
            values.append(value)
        if len(set(values)) == len(values):
            break
        source += lattice
        lifts += 1
        require(lifts <= comb(total + 1, 2), "affine coincidence avoidance budget")
    require(source % 3 == 1 and source % 2 == 1, "original ordinary unit")
    require(floor <= source < floor + (comb(total + 1, 2) + 1) * lattice,
            "ordinary source upper bound with coincidence allowance")
    require(all(n >= source for n in values), "fixed original floor retained")
    require(all(n % 2 and n % 3 for n in values), "actual odd unit states")

    period_carries = [gap_carry(rotate(script, i))[0] for i in range(period)]
    denominator = 3 ** period - (1 << sum(script))
    require(denominator > 0 and denominator % 6 in (1, 5), "full rational-cycle denominator")
    for i in range(period):
        require(3 * period_carries[i] == denominator + (1 << script[i])
                * period_carries[(i + 1) % period], "rotated exact carry")

    invariant = denominator * source + period_carries[0]
    require(invariant > 0 and invariant % (1 << clock) == 0, "source divisibility")
    require((1 << clock) <= invariant, "source-height lower bound")
    available_twos = (invariant & -invariant).bit_length() - 1
    extra_clock = clock
    extra_state = values[-1]
    extra_index = total
    while True:
        next_state, actual_gap = odd_step(extra_state)
        requested_gap = script[extra_index % period]
        if actual_gap != requested_gap:
            first_mismatch = extra_index
            break
        extra_clock += requested_gap
        require(extra_clock <= available_twos, "fixed source cannot exceed its exact binary budget")
        extra_state = next_state
        extra_index += 1
        require(extra_index <= available_twos + 1, "finite mismatch budget")
    chosen_clocks = set(range(min(total + 1, 2 * period + 1)))
    chosen_clocks.update([precision, total, sample_size, total // 2])
    binary_clock, ternary_power = 0, 1
    telescope_checks = 0
    for i in range(total + 1):
        if i in chosen_clocks:
            require((1 << binary_clock) * (denominator * values[i] + period_carries[i % period])
                    == ternary_power * invariant, ("exact phase telescope", i))
            telescope_checks += 1
        if i < total:
            binary_clock += gaps[i]
            ternary_power *= 3

    modulus = 3 ** precision
    inv_denominator = pow(denominator, -1, modulus)
    phase_residues = [(-c * inv_denominator) % modulus for c in period_carries]
    residues = Counter()
    for j in range(warmup, warmup + sample_size):
        value = values[j] % modulus
        require(value == phase_residues[j % period], "actual ternary phase locking")
        residues[value] += 1
    collision = Fraction(sum(count * count for count in residues.values()), sample_size ** 2)
    require(len(residues) <= period and collision >= Fraction(1, period), "phase collision lower")
    if len(set(phase_residues)) == period:
        require(collision == Fraction(1, period), "separated phases exact collision")

    label_counts = Counter(labels)
    block_checks = 0
    for length in range(1, order + 1):
        actual = Counter(tuple(gaps[j:j + length])
                         for j in range(warmup, warmup + sample_size))
        backward = Counter(tuple(gaps[j - length:j])
                           for j in range(warmup, warmup + sample_size))
        for block in product(sorted(label_counts), repeat=length):
            expected = Fraction(sample_size)
            for gap in block:
                expected *= Fraction(label_counts[gap], len(labels))
            require(actual[block] == expected, ("exact local product law", block))
            require(backward[block] == expected, ("exact backward local product law", block))
            block_checks += 2
    longer = order + 1
    # Test a depth with more positive-probability words than script phases.
    # An incidental extra product marginal at order+1 is permitted.
    while len(label_counts) ** longer <= period:
        longer += 1
    longer_actual = Counter(tuple(script[(j + k) % period] for k in range(longer))
                           for j in range(period))
    longer_defect = False
    for block in product(sorted(label_counts), repeat=longer):
        expected = Fraction(period)
        for gap in block:
            expected *= Fraction(label_counts[gap], len(labels))
        longer_defect |= longer_actual[block] != expected
    require(longer_defect, "finite product tests do not establish all product marginals")

    # These are the literal source boxes of round three, with uniform
    # actual empirical weights; no harmonic/canonical weight is asserted.
    profiles = [gap_carry([script[(i + h) % period] for h in range(precision)])
                for i in range(period)]
    for window_carry, _ in profiles:
        require(Fraction(window_carry, modulus) <= precision * carry_constant / 3,
                "period-dependent linear complete-carry cap")
    boxes = defaultdict(set)
    phase_boxes = [set() for _ in range(period)]
    for j in range(warmup, warmup + sample_size):
        begin = j - precision
        window_carry, window_clock = profiles[begin % period]
        for offset in range(precision + 1):
            require(carry_constant.denominator * values[begin]
                    <= carry_constant.numerator * values[begin + offset],
                    "actual downward-ratio bound")
        require((1 << window_clock) * values[j] == modulus * values[begin] + window_carry,
                "literal full window")
        box = (window_clock, window_carry // modulus, values[begin] // (1 << window_clock))
        residue_j = values[j] % modulus
        require(residue_j not in boxes[box], "within-box endpoint injection")
        boxes[box].add(residue_j)
        phase_boxes[j % period].add(box)
    require(all(len(group) == sample_size // period for group in phase_boxes),
            "each fixed phase uses distinct original source boxes")
    if sample_size > period:
        require(collision > Fraction(1, sample_size), "cross-box terms cannot be dropped")
    # In each phase the box triangle inequality is saturated exactly:
    # N/d singleton boxes each carry weight 1/N, giving (1/d)^2.
    phase_energy = Fraction(1, period ** 2)
    require(phase_energy == Fraction(sample_size // period, sample_size) ** 2,
            "exact phase aggregation")

    return {
        "labels": labels, "local_order": order, "period": period,
        "gap_period": script, "precision": precision,
        "warmup": warmup, "carry_constant": str(carry_constant),
        "sample_size": sample_size, "total_odd_steps": total,
        "total_binary_clock": clock, "source_bits": source.bit_length(),
        "source_sha256": digest_integer(source), "avoided_lifts": lifts,
        "fixed_source_first_gap_mismatch": first_mismatch,
        "v2_source_invariant": available_twos,
        "first_lift_bits": first_source.bit_length(), "full_denominator": denominator,
        "distinct_states": len(values), "residue_classes": len(residues),
        "collision": str(collision), "ordinary_diagonal": str(Fraction(1, sample_size)),
        "source_boxes": len(boxes), "local_product_equalities": block_checks,
        "nonproduct_control_depth": longer,
        "telescope_checks": telescope_checks, "phase_residues": phase_residues,
        "canonical_harmonic_weights": False,
    }


def dual_from_finite_convergence(n):
    states = [n]
    while states[-1] != 1:
        require(len(states) < 10000, "bounded convergence fixture limit")
        states.append(shortcut(states[-1]))
    dual = Fraction(2)
    for value in reversed(states[:-1]):
        dual = 2 * dual if value % 2 else (2 * dual - 1) / 3
    return states, dual


def triadic_controls():
    count = 0
    verifier_checks = 0
    maxima = {"shortcut_steps": 0, "denominator_exponent": 0}
    for n in list(range(1, 1025)) + [6171, 77031, 837799]:
        states, dual = dual_from_finite_convergence(n)
        denominator, exponent = dual.denominator, 0
        while denominator % 3 == 0:
            denominator //= 3
            exponent += 1
        require(denominator == 1, "convergent source gives triadic dual")
        if n > 1:
            hit_two = states.index(2)
            even_before_two = sum(value % 2 == 0 for value in states[:hit_two])
            require(exponent == even_before_two, "exact denominator stopping statistic")
        require(len(states) - 1 < 3 * (exponent + 1), "strict stopping clock bound")
        value = dual
        current_exponent = exponent
        for original in states[:-1]:
            require((original + value.numerator) % 2 == 1, "opposite rational parity")
            next_value = value / 2 if original % 2 else (3 * value + 1) / 2
            d, e = next_value.denominator, 0
            while d % 3 == 0:
                d //= 3
                e += 1
            require(d == 1, "localization preserved")
            if current_exponent > 0:
                require(e == current_exponent - (original % 2 == 0), "reduced denominator update")
            value, current_exponent = next_value, e
        require(value == 2, "exact terminal dual")
        accepted = verify_triadic(n, dual.numerator, exponent)
        require(accepted["accepted"] and accepted["ordinary_stopping_time"] == len(states) - 1,
                "linear-clock verifier accepts the exact dual")
        require(verify_triadic(n, 9 * dual.numerator, exponent + 2)["accepted"],
                "linear-clock verifier accepts unreduced denominator data")
        require(not verify_triadic(n, dual.numerator + dual.denominator, exponent)["accepted"],
                "exact backward equality rejects a perturbed candidate")
        verifier_checks += 3
        if exponent > 0:
            require(not verify_triadic(n, dual.numerator, exponent - 1)["accepted"],
                    "insufficient denominator budget rejected")
            verifier_checks += 1
        maxima["shortcut_steps"] = max(maxima["shortcut_steps"], len(states) - 1)
        maxima["denominator_exponent"] = max(maxima["denominator_exponent"], exponent)
        count += 1

    power_cases = []
    for k in range(1, 129):
        n = 1 << k
        states, dual = dual_from_finite_convergence(n)
        expected = Fraction(1 << k, 3 ** (k - 1)) - 1
        require(dual == expected and dual.denominator == 3 ** (k - 1), "power-of-two exact dual")
        bits = max(1, abs(dual.numerator), dual.denominator).bit_length()
        old_horizon = 8 * n.bit_length() + (9 * (k - 1) + 8) * bits + 2
        require(old_horizon == 8 * k + 10 + (9 * k - 1) * (3 ** (k - 1)).bit_length(),
                "old certificate exact horizon")
        if k in [1, 2, 8, 32, 128]:
            power_cases.append({"k": k, "ordinary_steps_to_one": k,
                                "reduced_denominator_exponent": k - 1,
                                "old_own_height_horizon": old_horizon})
    short_prefix_controls = 0
    for r in range(9):
        bound = 3 * (r + 1)
        a = 3 ** r * (2 + (1 << bound))
        x, y = 1, Fraction(a, 3 ** r)
        for _ in range(bound):
            require((x + y.numerator) % 2 == 1, "short parity agreement countercontrol")
            y = y / 2 if x % 2 else (3 * y + 1) / 2
            x = shortcut(x)
        require(not verify_triadic(1, a, r)["accepted"],
                "short parity agreement must not replace exact pullback equality")
        short_prefix_controls += 1
    return {"convergent_sources": count, "power_of_two_cases": 128,
            "linear_verifier_checks": verifier_checks,
            "short_parity_prefix_false_candidates": short_prefix_controls,
            "maxima": maxima, "power_examples": power_cases,
            "scope": "known finite trajectories; all-time classification is a written theorem, not inferred from this census"}


def cycle_controls():
    determinant_checks = 0
    rational_roots = 0
    integral_roots = 0
    necklace_classes = 0
    for length in range(1, 13):
        by_weight = defaultdict(list)
        for word in product([0, 1], repeat=length):
            word = list(word)
            count = sum(word)
            denominator = (1 << length) - 3 ** count
            c = carry(word)
            for cut in range(1, length):
                left, right = word[:cut], word[cut:]
                d_left = (1 << len(left)) - 3 ** sum(left)
                d_right = (1 << len(right)) - 3 ** sum(right)
                difference = carry(right + left) - c
                require(difference == d_right * carry(left) - d_left * carry(right),
                        "complete cut determinant")
                determinant_checks += 1
            if count == 0 or denominator <= 0:
                continue
            rotations = [rotate(word, i) for i in range(length)]
            if len({tuple(v) for v in rotations}) != length:
                continue
            cs = [carry(v) for v in rotations]
            require(len(set(cs)) == length, "primitive carries distinct")
            is_root = c == min(cs)
            integral = c % denominator == 0
            require(all((other % denominator == 0) == integral for other in cs),
                    "full-denominator integrality rotation invariance")
            by_weight[count].append((is_root, integral))
            if is_root:
                rational_roots += 1
                for cut in range(1, length):
                    right = word[cut:]
                    require((1 << len(right)) > 3 ** sum(right), "all suffixes contract at least root")
                    difference = cs[cut] - c
                    require(difference > 0, "strict least-carry cut")
                    if integral:
                        require(difference % denominator == 0 and difference >= denominator,
                                "full-D quantized cut gap")
                        if word[cut] == 1:
                            require(difference >= 2 * denominator and (difference // denominator) % 2 == 0,
                                    "odd-to-odd full-D gap")
                integral_roots += integral
        for weight, entries in by_weight.items():
            roots = sum(root for root, _ in entries)
            zeros = sum(zero for _, zero in entries)
            root_zeros = sum(root and zero for root, zero in entries)
            require(length * roots == len(entries), "one least root per primitive necklace")
            require(root_zeros * len(entries) == zeros * roots, "root conditioning does not improve zero proportion")
            necklace_classes += 1

    control = [1, 1, 1, 0, 0, 1, 0]
    c, denominator = carry(control), (1 << len(control)) - 3 ** sum(control)
    suffix_rotations = [i for i in range(len(control))
                        if all((1 << len(rotate(control, i)[j:])) > 3 ** sum(rotate(control, i)[j:])
                               for j in range(1, len(control)))]
    require((c, denominator, carry(rotate(control, 5)) - c) == (89, 47, 14), "rational full-D control")
    require(0 in suffix_rotations and 5 in suffix_rotations, "suffix barrier does not choose minimum")
    require(c % denominator != 0 and 14 < denominator, "full denominator rejects false cycle")
    weight_four = [list(w) for w in product([0, 1], repeat=7) if sum(w) == 4]
    least_roots = [w for w in weight_four if carry(w) == min(carry(rotate(w, i)) for i in range(7))]
    barrier_words = [w for w in weight_four
                     if all((1 << len(w[j:])) > 3 ** sum(w[j:]) for j in range(1, 7))]
    require((len(weight_four), len(least_roots), len(barrier_words)) == (35, 5, 7),
            "least-root and ballot event dependence")
    coarse = [1, 1, 0, 1, 1, 0, 1, 0]
    coarse_cs = [carry(rotate(coarse, i)) for i in range(8)]
    require(coarse_cs == [319, 485, 734, 367, 557, 842, 421, 638], "large-gap rational control")
    require(min(c - coarse_cs[0] for c in coarse_cs[1:]) == 48 and 319 % 13 != 0,
            "large carry gaps do not establish full divisibility")
    return {"word_lengths_through": 12, "cut_determinants": determinant_checks,
            "primitive_positive_rational_roots": rational_roots,
            "primitive_positive_integral_roots": integral_roots,
            "necklace_weight_classes": necklace_classes,
            "rational_control": {"word": "1110010", "carry": c, "denominator": denominator,
                                 "cut_5_gap": 14, "suffix_barrier_rotations": suffix_rotations},
            "root_ballot_counts": [35, 5, 7],
            "large_gap_control": {"word": "11011010", "full_denominator": 13,
                                  "minimum_root_gap": 48, "integral": False}}


def main():
    # A one-gap control: omitting the final odd bit permits source 1 for
    # requested gap 1, although its actual valuation is 2.
    wrong_source = (-pow(3, -1, 2)) % 2
    require(wrong_source == 1 and odd_step(wrong_source)[1] != 1,
            "missing final-odd-bit control")
    cases = [
        ([1, 2], 3, 1, 8, 1),
        ([1, 2], 1, 5, 128, 1),
        ([1, 2], 2, 8, 4096, 1 << 80),
        ([1, 2], 3, 7, 1024, 1 << 40),
        ([1, 1, 2], 2, 6, 729, 1000),
    ]
    controls = [finite_periodic_control(*case) for case in cases]
    result = {
        "schema": "collatz-literature-round4-exact/v1",
        "scope": "bounded exact controls, not a universal proof or a canonical-law sample",
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "verifier_sha256": sha256(Path(__file__).with_name("verify_triadic.py").read_bytes()).hexdigest(),
        "ordinary_periodic_shadow_controls": controls,
        "triadic_controls": triadic_controls(),
        "cycle_controls": cycle_controls(),
        "invalid_inferences_rejected": [
            "omit the final odd bit in ordinary gap realization",
            "delete cross-source-box collision pairs",
            "infer whole-window independence from finitely many exact product marginals",
            "retain one positive source while extending its periodic template indefinitely",
            "replace full numerical cycle divisibility by the suffix coefficient barrier",
            "multiply the zero-residue probability by a second necklace-root factor",
        ],
        "success": True,
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
