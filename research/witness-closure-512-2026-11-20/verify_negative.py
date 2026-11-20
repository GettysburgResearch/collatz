#!/usr/bin/env python3
"""Exact replay for W512-070--072; no claim of full-problem coverage."""

from fractions import Fraction
import json


SOURCE_PREFIX = (2, 2, 2, 1, 2, 4)
OLD_SOURCE = SOURCE_PREFIX + (5,)
NEW_SOURCE = (2, 2, 2, 1, 1, 2, 2, 1, 2, 4, 5, 1)
OLD_TARGET = (2, 2, 3, 1, 3, 2)
NEW_TARGET = (2, 2, 4, 2, 1, 1, 2, 1, 2, 1, 2)
RULES = (
    {
        "claim": "W512-070",
        "denominator": 243, "residue": 49,
        "multiplier": 128, "offset": -69,
        "M_step": 497664, "M_base": 292863,
        "child_step": 262144, "child_base": 154265,
        "source_word": NEW_SOURCE[:-1], "target_word": NEW_TARGET,
        "length_change": 5, "exponent_change": 7,
        "source_endpoint": (5668704, 3335893),
        "child_endpoint": (354294, 208493),
        "target_endpoint": (2834352, 1667947),
    },
    {
        "claim": "W512-072",
        "denominator": 729, "residue": 675,
        "multiplier": 512, "offset": -271,
        "M_step": 1492992, "M_base": 774143,
        "child_step": 1048576, "child_base": 543705,
        "source_word": (2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 4, 5),
        "target_word": (2, 2, 4, 2) + (1, 2) * 4,
        "length_change": 6, "exponent_change": 9,
        "source_endpoint": (17006112, 8817973),
        "child_endpoint": (1062882, 551123),
        "target_endpoint": (8503056, 4408987),
    },
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def v2(n):
    require(type(n) is int and n != 0, "v2 requires a nonzero integer")
    return (n & -n).bit_length() - 1


def validate_witness(start, word):
    require(type(start) is int and start > 0 and start % 2 == 1,
            "witness start must be a positive odd integer")
    n, total, constant = start, 0, 0
    for exponent in word:
        require(type(exponent) is int and exponent > 0,
                "witness exponents must be positive integers")
        numerator = 3 * n + 1
        require(v2(numerator) == exponent, "witness exponent is not exact")
        n = numerator >> exponent
        constant = 3 * constant + (1 << total)
        total += exponent
    require(n == 1, "witness does not end at 1")
    require(3 ** len(word) * start + constant == 1 << total,
            "witness fails the defining identity")
    return len(word), total


def fixture_witness(start, step_limit=20000):
    """Generate only the explicitly bounded replay fixtures."""
    word, n = [], start
    while n != 1:
        require(len(word) < step_limit, "fixture exceeded its explicit limit")
        numerator = 3 * n + 1
        exponent = v2(numerator)
        word.append(exponent)
        n = numerator >> exponent
    validate_witness(start, tuple(word))
    return tuple(word)


def matching_rule(m):
    if type(m) is not int or m <= 0 or m % 2048 != 2047:
        return None
    for rule in RULES:
        if (m + 1) % rule["denominator"] == rule["residue"]:
            return rule
    return None


def child_parameter(m):
    rule = matching_rule(m)
    if rule is None:
        return None
    numerator = rule["multiplier"] * m + rule["offset"]
    require(numerator % rule["denominator"] == 0,
            "child parameter is not integral")
    child = numerator // rule["denominator"]
    require(0 < child < m and child % 2 == 1, "child parameter is invalid")
    return child


def source_to_child(m, word):
    child = child_parameter(m)
    if child is None:
        return {"status": "UNRESOLVED"}
    rule = matching_rule(m)
    old_length, old_total = validate_witness(128 * m + 1, word)
    require(len(word) > len(SOURCE_PREFIX), "source stops before the tail")
    require(tuple(word[:len(SOURCE_PREFIX)]) == SOURCE_PREFIX,
            "source does not have the certified prefix")
    tail = tuple(word[len(SOURCE_PREFIX):])
    require(tail[0] >= 5, "source tail cannot be unjumped twice")
    unjumped = (tail[0] - 4,) + tail[1:]
    result = rule["source_word"] + unjumped
    new_length, new_total = validate_witness(128 * child + 1, result)
    require((new_length, new_total)
            == (old_length + rule["length_change"],
                old_total + rule["exponent_change"]),
            "source reconstruction bookkeeping failed")
    return {"status": "REDUCED", "child": child, "word": result}


def target_from_child(m, word):
    child = child_parameter(m)
    if child is None:
        return {"status": "UNRESOLVED"}
    rule = matching_rule(m)
    old_length, old_total = validate_witness(64 * child + 1, word)
    require(len(word) > len(rule["target_word"]),
            "child target stops before the common endpoint tail")
    require(tuple(word[:len(rule["target_word"])]) == rule["target_word"],
            "child target does not have the certified prefix")
    result = OLD_TARGET + tuple(word[len(rule["target_word"]):])
    new_length, new_total = validate_witness(64 * m + 1, result)
    require((new_length, new_total)
            == (old_length - rule["length_change"],
                old_total - rule["exponent_change"]),
            "target reconstruction bookkeeping failed")
    return {"status": "RECONSTRUCTED", "word": result}


def symbolic_prefix(coefficient, constant, word):
    """Certify the odd reference plus even perturbation at every prefix."""
    coefficient, constant = Fraction(coefficient), Fraction(constant)
    states = [(coefficient, constant)]
    for exponent in word:
        coefficient *= Fraction(3, 1 << exponent)
        constant = (3 * constant + 1) / (1 << exponent)
        require(coefficient.denominator % 2 == 1
                and coefficient.numerator % 2 == 0,
                "perturbation is not 2-adically even")
        require(constant.denominator % 2 == 1
                and constant.numerator % 2 == 1,
                "reference endpoint is not 2-adically odd")
        states.append((coefficient, constant))
    return states


def replay():
    for rule in RULES:
        source = symbolic_prefix(128 * rule["M_step"],
                                 128 * rule["M_base"] + 1, SOURCE_PREFIX)
        child_source = symbolic_prefix(128 * rule["child_step"],
                                       128 * rule["child_base"] + 1,
                                       rule["source_word"])
        target = symbolic_prefix(64 * rule["M_step"],
                                 64 * rule["M_base"] + 1, OLD_TARGET)
        child_target = symbolic_prefix(64 * rule["child_step"],
                                       64 * rule["child_base"] + 1,
                                       rule["target_word"])
        require(source[-1] == rule["source_endpoint"]
                and child_source[-1] == rule["child_endpoint"],
                "primary source endpoint differs from its certificate")
        require(source[-1] == (16 * child_source[-1][0],
                               16 * child_source[-1][1] + 5),
                "primary source J-squared relation failed")
        require(target[-1] == child_target[-1] == rule["target_endpoint"],
                "primary target merger failed")
        for states in (source, child_source, target, child_target):
            for coefficient, constant in states:
                require(coefficient.denominator == constant.denominator == 1
                        and coefficient > 0 and constant > 0,
                        "primary positive affine prefix is invalid")

    positive_source_old = symbolic_prefix(128 * 995328, 128 * 790527 + 1,
                                          OLD_SOURCE)
    positive_source_new = symbolic_prefix(128 * 524288, 128 * 416409 + 1,
                                          NEW_SOURCE)
    positive_target_old = symbolic_prefix(64 * 995328, 64 * 790527 + 1,
                                          OLD_TARGET)
    positive_target_new = symbolic_prefix(64 * 524288, 64 * 416409 + 1,
                                          NEW_TARGET)
    require(positive_source_old[-1] == positive_source_new[-1]
            == (Fraction(1062882), Fraction(844181)),
            "positive source affine identity failed")
    require(positive_target_old[-1] == positive_target_new[-1]
            == (Fraction(5668704), Fraction(4502299)),
            "positive target affine identity failed")
    for states in (positive_source_old, positive_source_new,
                   positive_target_old, positive_target_new):
        for coefficient, constant in states:
            require(coefficient.denominator == constant.denominator == 1
                    and coefficient > 0 and constant > 0,
                    "positive affine certificate has an invalid prefix")

    source_old = symbolic_prefix(1 << 19, -127, OLD_SOURCE)
    source_new = symbolic_prefix(Fraction(1 << 26, 243),
                                Fraction(-24973, 243), NEW_SOURCE)
    target_old = symbolic_prefix(1 << 18, -63, OLD_TARGET)
    target_new = symbolic_prefix(Fraction(1 << 25, 243),
                                Fraction(-12365, 243), NEW_TARGET)
    require(source_old[-1] == source_new[-1] == (Fraction(4374), Fraction(-1)),
            "source affine identity failed")
    require(target_old[-1] == target_new[-1] == (Fraction(23328), Fraction(-5)),
            "target affine identity failed")

    fixtures = []
    for rule in RULES:
        for offset in (0, 1, 2, 3, 7, 11):
            m = rule["M_step"] * offset + rule["M_base"]
            child = child_parameter(m)
            require(child == rule["child_step"] * offset + rule["child_base"],
                    "fixture child does not match its positive cylinder")
            source = fixture_witness(128 * m + 1)
            reduced = source_to_child(m, source)
            require(reduced["status"] == "REDUCED", "source fixture unresolved")
            target = fixture_witness(64 * child + 1)
            rebuilt = target_from_child(m, target)
            require(rebuilt["status"] == "RECONSTRUCTED",
                    "target fixture unresolved")
            fixtures.append({"rule": rule["claim"], "j": offset,
                             "M": m, "child_M": child})

    require(source_to_child(4095, ()) == {"status": "UNRESOLVED"},
            "unsupported source was treated as proved")
    require(target_from_child(4095, ()) == {"status": "UNRESOLVED"},
            "unsupported target was treated as proved")
    rejected = 0
    for start, word in ((129, (1,)), (65, ()), (1, (0,)), (1, (True,))):
        try:
            validate_witness(start, word)
        except ValueError:
            rejected += 1
        else:
            raise ValueError("malformed witness was accepted")

    return {
        "status": "PASS",
        "claim_ids": ["W512-070", "W512-071", "W512-072"],
        "primary_source_J2_certificates": len(RULES),
        "primary_target_mergers": len(RULES),
        "fixed_specialization_affine_pairs": 2,
        "rational_reference_endpoint_pairs": 2,
        "complete_prefix_parity_certificates": 16,
        "source_reconstruction_fixtures": len(fixtures),
        "target_reconstruction_fixtures": len(fixtures),
        "fixtures": fixtures,
        "malformed_witnesses_rejected": rejected,
        "unsupported_case": "UNRESOLVED",
        "full_claim": "UNRESOLVED",
        "coverage": "Two stated congruence families; no global cover.",
    }


if __name__ == "__main__":
    print(json.dumps(replay(), sort_keys=True))
