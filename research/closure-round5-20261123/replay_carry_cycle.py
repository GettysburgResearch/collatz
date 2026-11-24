#!/usr/bin/env python3
"""Exact finite controls for complete carries and rational circuit words.

These checks are finite arithmetic evidence, not proofs of an asymptotic
entropy statement, the all-threshold obstruction, or the Collatz conjecture.
Only standard-library integer, Fraction, and full-gcd arithmetic is used.
The large fixtures are checked through closed forms and divisibility; their
long state lists and rotated carries are deliberately not enumerated.

Import run_checks() for deterministic JSON-serializable results, or execute
this file to print the same results. Explicit require calls remain active
under python -O.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd
import json


class VerificationError(RuntimeError):
    """A finite arithmetic control failed."""


def require(condition, message):
    if not condition:
        raise VerificationError(message)


def compositions(total, length):
    """Enumerate all ordered positive compositions in lexicographic order."""
    if length == 1:
        yield (total,)
        return
    for first in range(1, total - length + 2):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def full_shortcut_carry(word):
    """Forward affine recurrence: 2^k x_k = 3^p x_0 + C."""
    carry = 0
    ones = 0
    for clock, bit in enumerate(word):
        require(bit in (0, 1), "shortcut word contains a nonbinary value")
        if bit == 1:
            carry = 3 * carry + (1 << clock)
            ones += 1
    return carry, ones


def inverse_gap_carry(gaps):
    """The full sum C_m = sum_i 3^(i-1) 2^(A_m-A_i)."""
    total = sum(gaps)
    prefix = 0
    carry = 0
    for index, gap in enumerate(gaps):
        prefix += gap
        carry += (3 ** index) * (1 << (total - prefix))
    return carry


def forward_word_from_backward_gaps(gaps):
    word = []
    for gap in reversed(gaps):
        word.append(1)
        word.extend([0] * (gap - 1))
    return tuple(word)


def check_gap_carries():
    max_length = 5
    max_total = 16
    full_keys = {}
    quotient_keys = {}
    by_length = Counter()
    fixed_total_fibres = defaultdict(list)
    residue_fibres = defaultdict(list)
    without_total = {}
    without_quotient = {}
    omitted_total_witness = None
    omitted_quotient_witness = None
    words = 0

    for length in range(1, max_length + 1):
        modulus = 3 ** length
        for total in range(length, max_total + 1):
            for gaps in compositions(total, length):
                label = f"gap word {gaps}"
                require(sum(gaps) == total, f"{label}: wrong total")
                require(len(gaps) == length, f"{label}: wrong length")
                require(min(gaps) > 0, f"{label}: nonpositive gap")

                carry = inverse_gap_carry(gaps)
                forward_word = forward_word_from_backward_gaps(gaps)
                forward_carry, odd_count = full_shortcut_carry(forward_word)
                require(len(forward_word) == total, f"{label}: wrong binary clock")
                require(odd_count == length, f"{label}: wrong odd clock")
                require(carry == forward_carry, f"{label}: full carry formulas differ")

                residue = (carry * pow(1 << total, -1, modulus)) % modulus
                prefix = 0
                direct_residue = 0
                for index, gap in enumerate(gaps):
                    prefix += gap
                    direct_residue += (3 ** index) * pow(1 << prefix, -1, modulus)
                require(residue == direct_residue % modulus,
                        f"{label}: ternary residue formulas differ")
                quotient, remainder = divmod(carry, modulus)
                require(remainder == (residue * pow(2, total, modulus)) % modulus,
                        f"{label}: residue does not recover the carry remainder")

                full_key = (length, total, carry)
                quotient_key = (length, total, residue, quotient)
                require(full_key not in full_keys,
                        f"{label}: fixed-clock full-carry injection failed")
                require(quotient_key not in quotient_keys,
                        f"{label}: residue/total/full-quotient injection failed")
                full_keys[full_key] = gaps
                quotient_keys[quotient_key] = gaps
                fixed_total_fibres[(length, total, residue)].append(quotient)
                residue_fibres[(length, residue)].append((total, quotient))

                # These witnesses explain why neither retained coordinate can
                # simply be dropped from the tested injection.
                no_total_key = (length, residue, quotient)
                previous = without_total.get(no_total_key)
                if previous is not None and omitted_total_witness is None:
                    omitted_total_witness = {
                        "length": length,
                        "residue": residue,
                        "carry_quotient": quotient,
                        "first_gaps": list(previous),
                        "second_gaps": list(gaps),
                    }
                without_total.setdefault(no_total_key, gaps)

                no_quotient_key = (length, total, residue)
                previous = without_quotient.get(no_quotient_key)
                if previous is not None and omitted_quotient_witness is None:
                    omitted_quotient_witness = {
                        "length": length,
                        "total": total,
                        "residue": residue,
                        "first_gaps": list(previous),
                        "second_gaps": list(gaps),
                    }
                without_quotient.setdefault(no_quotient_key, gaps)
                words += 1
                by_length[length] += 1

    bounded_fibre_checks = 0
    for key, quotients in sorted(fixed_total_fibres.items()):
        require(len(set(quotients)) == len(quotients),
                f"fixed-total fibre {key}: duplicate full quotient")
        for count, quotient in enumerate(sorted(quotients), start=1):
            require(count <= quotient + 1,
                    f"fixed-total fibre {key}: quotient-cutoff count failed")
            bounded_fibre_checks += 1
    for key, pairs in sorted(residue_fibres.items()):
        total_choices = len({total for total, _ in pairs})
        max_quotient = max(quotient for _, quotient in pairs)
        require(len(pairs) <= total_choices * (max_quotient + 1),
                f"residue fibre {key}: total/quotient rectangle bound failed")
        bounded_fibre_checks += 1

    require(words == 6884, "positive composition enumeration count changed")
    require(len(full_keys) == words, "full-carry key count differs")
    require(len(quotient_keys) == words, "residue/total/quotient key count differs")
    require(omitted_total_witness is not None, "missing omitted-total control")
    require(omitted_quotient_witness is not None, "missing omitted-quotient control")
    return {
        "max_gap_word_length": max_length,
        "max_total_clock": max_total,
        "positive_compositions": words,
        "words_by_length": {str(k): by_length[k] for k in sorted(by_length)},
        "complete_carry_formula_comparisons": words,
        "residue_formula_comparisons": words,
        "fixed_length_total_carry_distinct_keys": len(full_keys),
        "residue_total_full_quotient_distinct_keys": len(quotient_keys),
        "fixed_total_residue_fibres": len(fixed_total_fibres),
        "residue_fibres": len(residue_fibres),
        "bounded_fibre_checks": bounded_fibre_checks,
        "largest_fixed_total_residue_fibre": max(map(len, fixed_total_fibres.values())),
        "omitted_total_witness": omitted_total_witness,
        "omitted_quotient_witness": omitted_quotient_witness,
    }


def least_positive_ordinary_residue(p, h, carry):
    modulus = 1 << (p + h)
    residue = (-carry * pow(3 ** p, -1, modulus)) % modulus
    return residue if residue > 0 else modulus


def check_bounded_cycles():
    cases = 0
    edges = 0
    rotated_carries = 0
    prefix_coefficients = 0
    ordinary_descents = 0
    ordinary_edges = 0
    nontrivial_gcd_cases = 0
    greatest_gcd = 1

    for p in range(2, 25):
        three_power = 3 ** p
        for h in range(1, 25):
            total = p + h
            denominator = (1 << total) - three_power
            carry = three_power - (1 << p)
            if denominator <= 0 or carry <= denominator:
                continue
            label = f"circuit p={p}, h={h}"
            root = Fraction(carry, denominator)
            word = (1,) * p + (0,) * h
            literal_carry, odd_count = full_shortcut_carry(word)
            require(literal_carry == carry and odd_count == p,
                    f"{label}: complete carry formula failed")
            require(denominator % 2 == 1, f"{label}: even denominator")

            full_gcd = gcd(denominator, carry)
            require(full_gcd == gcd(denominator, (1 << h) - 1),
                    f"{label}: full numerical gcd identity failed")
            require(root.denominator == denominator // full_gcd,
                    f"{label}: reduced denominator differs")
            require(root.denominator * (1 << h) > denominator,
                    f"{label}: full-denominator lower bound failed")
            nontrivial_gcd_cases += int(full_gcd > 1)
            greatest_gcd = max(greatest_gcd, full_gcd)

            states = []
            state = root
            for index, bit in enumerate(word):
                require(state.denominator % 2 == 1,
                        f"{label}, edge {index}: denominator is not odd")
                require(state.numerator % 2 == bit,
                        f"{label}, edge {index}: rational parity is illegal")
                if index <= p:
                    closed_numerator = ((3 ** index) * (1 << (p - index))
                                        * ((1 << h) - 1) - denominator)
                    closed_state = Fraction(closed_numerator, denominator)
                else:
                    closed_state = Fraction((1 << (total - index)) * carry, denominator)
                require(state == closed_state,
                        f"{label}, edge {index}: literal and closed states differ")
                states.append(state)
                state = (3 * state + 1) / 2 if bit else state / 2
                edges += 1
            require(state == root, f"{label}: cycle does not close")
            require(len(set(states)) == total, f"{label}: repeated proper state")
            require(min(states) == root and states.count(root) == 1,
                    f"{label}: root is not the unique minimum")
            for period in range(1, total):
                if total % period == 0:
                    require(word != word[:period] * (total // period),
                            f"{label}: word has a proper period")

            proper_carry_gaps = []
            for index in range(total):
                rotated = word[index:] + word[:index]
                rotation_carry, rotation_odds = full_shortcut_carry(rotated)
                require(rotation_odds == p, f"{label}: rotation changed odd clock")
                require(Fraction(rotation_carry, denominator) == states[index],
                        f"{label}, rotation {index}: complete carry misses state")
                require(gcd(denominator, rotation_carry) == full_gcd,
                        f"{label}, rotation {index}: full gcd changed")
                if index:
                    require(rotation_carry > carry,
                            f"{label}: nonpositive proper carry gap")
                    proper_carry_gaps.append(rotation_carry - carry)
                rotated_carries += 1
            minimum_gap_numerator = (1 << (p - 1)) * ((1 << h) - 1)
            require(2 * minimum_gap_numerator == carry + denominator,
                    f"{label}: least-gap closed identity failed")
            require(min(proper_carry_gaps) == minimum_gap_numerator,
                    f"{label}: least complete-carry gap differs")
            require(min(state - root for state in states[1:]) == (root + 1) / 2,
                    f"{label}: least rational state gap differs")

            ones = 0
            for length, bit in enumerate(word, start=1):
                ones += bit
                if length < total:
                    require(3 ** ones > (1 << length),
                            f"{label}: proper prefix coefficient is not above one")
                    prefix_coefficients += 1
            require(three_power < (1 << total),
                    f"{label}: full coefficient is not below one")

            if denominator > (1 << h) - 1:
                source = least_positive_ordinary_residue(p, h, carry)
                require(0 < source <= (1 << total),
                        f"{label}: source is not the least positive residue")
                require(source % (1 << p) == (1 << p) - 1,
                        f"{label}: odd-run source grid failed")
                require(source > root, f"{label}: ordinary source not above fixed point")
                endpoint = source
                for index, bit in enumerate(word):
                    require(endpoint > 0 and endpoint % 2 == bit,
                            f"{label}, ordinary edge {index}: illegal branch")
                    endpoint = (3 * endpoint + 1) // 2 if bit else endpoint // 2
                    ordinary_edges += 1
                require((1 << total) * endpoint == three_power * source + carry,
                        f"{label}: complete ordinary affine identity failed")
                require(endpoint < source, f"{label}: ordinary residue did not descend")
                ordinary_descents += 1
            cases += 1

    require(cases == 22, "bounded rational circuit count changed")
    require(edges == 482, "bounded rational edge count changed")
    require(rotated_carries == 482, "bounded rotated-carry count changed")
    return {
        "p_range_inclusive": [2, 24],
        "h_range_inclusive": [1, 24],
        "filter": "D > 0 and C/D > 1",
        "legal_primitive_rational_cycles": cases,
        "literal_rational_edges": edges,
        "complete_rotated_carries": rotated_carries,
        "proper_prefix_coefficients": prefix_coefficients,
        "nontrivial_full_gcd_cases": nontrivial_gcd_cases,
        "greatest_full_gcd": greatest_gcd,
        "least_positive_ordinary_residue_descents": ordinary_descents,
        "literal_ordinary_edges": ordinary_edges,
    }


def check_large_closed_forms():
    fixtures = (
        (10, 100, 41, 65, 59),
        (100, 10 ** 6, 306, 485, 476),
        (1000, 10 ** 9, 14271, 22619, 22606),
        (10000, 10 ** 12, 47468, 75235, 75219),
    )
    results = []
    for floor, denominator_floor, p, total, expected_bits in fixtures:
        label = f"large fixture B={floor}, Q={denominator_floor}, p={p}, A={total}"
        h = total - p
        require(p >= 2 and h >= 1, f"{label}: invalid circuit clocks")
        two_p = 1 << p
        two_h = 1 << h
        two_total = 1 << total
        three_power = 3 ** p
        denominator = two_total - three_power
        carry = three_power - two_p
        require(denominator > 0 and carry > 0, f"{label}: nonpositive fixed point")
        require(carry + denominator == two_p * (two_h - 1),
                f"{label}: complete closed-form identity failed")

        # epsilon=1/(16B), with no floating logarithms or approximations.
        require(16 * floor * denominator > three_power,
                f"{label}: R does not exceed 1+epsilon")
        require(8 * floor * denominator < three_power,
                f"{label}: R is not below 1+2epsilon")
        require(2 * two_p < three_power,
                f"{label}: (2/3)^p is not below one half")
        require(two_p > denominator_floor * (16 * floor + 2),
                f"{label}: chosen p misses the denominator threshold")
        require(carry > 4 * floor * denominator, f"{label}: minimum floor failed")
        minimum_gap_numerator = (1 << (p - 1)) * (two_h - 1)
        require(2 * minimum_gap_numerator == carry + denominator,
                f"{label}: least-gap identity failed")
        require(minimum_gap_numerator > 2 * floor * denominator,
                f"{label}: least-gap threshold failed")

        full_gcd = gcd(denominator, carry)
        require(full_gcd == gcd(denominator, two_h - 1),
                f"{label}: full numerical gcd identity failed")
        reduced_denominator = denominator // full_gcd
        require(full_gcd == 1, f"{label}: recorded fixture gcd changed")
        require(reduced_denominator > denominator_floor,
                f"{label}: full reduced denominator is too small")
        require(reduced_denominator.bit_length() == expected_bits,
                f"{label}: recorded reduced denominator bit length changed")
        require(reduced_denominator * two_h > denominator,
                f"{label}: full-denominator lower bound failed")
        require(denominator > two_h - 1,
                f"{label}: ordinary-source strict descent condition failed")
        require(two_total // 2 < three_power < two_total,
                f"{label}: final coefficient crossing failed")

        # An exact complete residue, checked by whole-run divisibility rather
        # than by constructing tens of thousands of huge intermediate states.
        source = least_positive_ordinary_residue(p, h, carry)
        require(0 < source < two_total, f"{label}: noncanonical ordinary residue")
        require((source + 1) % two_p == 0,
                f"{label}: ordinary odd-run divisibility failed")
        odd_run_parameter = (source + 1) // two_p
        require(odd_run_parameter >= 1, f"{label}: nonpositive odd-run parameter")
        odd_run_top = three_power * odd_run_parameter - 1
        require(odd_run_top % two_h == 0,
                f"{label}: ordinary even-run divisibility failed")
        endpoint = odd_run_top // two_h
        require(two_total * endpoint == three_power * source + carry,
                f"{label}: complete ordinary affine identity failed")
        require(source * denominator > carry,
                f"{label}: ordinary source not above rational fixed point")
        require(0 < endpoint < source, f"{label}: ordinary closed-form descent failed")

        if p == 41:
            require(denominator == 420491770248316829,
                    "first fixture: recorded denominator changed")
            require(carry == 36472994178147530851,
                    "first fixture: recorded complete carry changed")
            require(minimum_gap_numerator == 18446742974197923840,
                    "first fixture: recorded gap numerator changed")
        results.append({
            "B": floor,
            "Q": denominator_floor,
            "p": p,
            "A": total,
            "full_gcd": full_gcd,
            "fully_reduced_denominator_bits": reduced_denominator.bit_length(),
            "minimum_state_floor": carry // denominator,
            "minimum_gap_floor": minimum_gap_numerator // denominator,
            "ordinary_source_bits": source.bit_length(),
            "ordinary_endpoint_bits": endpoint.bit_length(),
            "ordinary_residue_closed_form_descent": True,
        })
    return {
        "method": "exact closed forms, complete numerical gcd, and whole-run divisibility",
        "long_state_trajectories_enumerated": False,
        "long_rotated_carry_lists_enumerated": False,
        "fixtures": results,
    }


def run_checks():
    """Return all deterministic finite control results; raise on failure."""
    return {
        "status": "pass",
        "scope": "finite exact arithmetic controls; no asymptotic or Collatz proof",
        "gap_carries": check_gap_carries(),
        "bounded_cycles": check_bounded_cycles(),
        "large_closed_form_cycles": check_large_closed_forms(),
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
