#!/usr/bin/env python3
"""Exact finite controls for ordinary first-passage cells and landing templates.

This checks finite affine identities and source sets. It does not establish
the renewal input, total-variation limit, entropy asymptotic, or any orbit fate.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def affine(word):
    numerator, total = 0, 0
    for exponent in word:
        numerator = 3 * numerator + 2 ** total
        total += exponent
    return 3 ** len(word), numerator, 2 ** total


def passage(source, floor):
    state, word, departed = source, [], []
    while state > floor and len(word) < 128:
        departed.append(state)
        shifted = 3 * state + 1
        exponent = (shifted & -shifted).bit_length() - 1
        word.append(exponent)
        state = shifted >> exponent
    require(state <= floor, "bounded sample exceeded its explicit passage cap")
    return state, tuple(word), departed


def first_passage_predicate(floor, source_low, target, word):
    multiplier, offset, denominator = affine(word)
    dividend = denominator * target - offset
    if dividend % multiplier:
        return None
    source = dividend // multiplier
    if source % 2 != 1 or not source_low <= source < 2 * source_low:
        return None
    for index in range(len(word)):
        mul, off, den = affine(word[index:])
        if den * target <= floor * mul + off:
            return None
    return source


def main():
    sources = cells = template_tests = suffix_tests = covariance_tests = 0
    synthetic = {()}
    for length in range(1, 4):
        synthetic.update(product(range(1, 5), repeat=length))
    for floor in (17, 32, 65, 129):
        for ratio in (1, 2, 5, 11):
            low = floor * ratio
            observed = defaultdict(set)
            grouped = defaultdict(list)
            for source in range(low + (low % 2 == 0), 2 * low, 2):
                target, word, departed = passage(source, floor)
                grade, clock = len(word), sum(word)
                mul, off, den = affine(word)
                require(den * target == mul * source + off, "forward affine identity")
                require(all(x > floor for x in departed), "first-passage floor")
                require(3 * floor * den * target <=
                        3 * floor * mul * source + grade * den * target,
                        "native first-passage source strip")
                for index, state in enumerate(departed):
                    sm, so, sd = affine(word[index:])
                    require(sd * target == sm * state + so, "suffix affine identity")
                    require(sd * target > floor * sm + so, "strict suffix cutoff")
                    suffix_tests += 1
                observed[word].add((source, target))
                grouped[(target, grade, clock)].append(source)
                sources += 1
            for (target, grade, clock), values in grouped.items():
                require(3 * floor * 3 ** grade * (max(values) - min(values)) <=
                        grade * 2 ** clock * target, "same-clock source-cell width")
                cells += 1
            for word in set(observed) | synthetic:
                predicted = set()
                for target in range(1, floor + 1, 2):
                    source = first_passage_predicate(floor, low, target, word)
                    if source is not None:
                        predicted.add((source, target))
                    template_tests += 1
                require(predicted == observed.get(word, set()),
                        "word, progression and suffix inequalities disagree with actual sources")

    # A target-first first-gap shift simultaneously halves every real multiplier
    # and the ternary intercept; its geometric probability is also halved.
    for length in range(1, 6):
        for word in product(range(1, 5), repeat=length):
            moved = (word[0] + 1,) + word[1:]
            def record_data(gaps):
                total = 0
                intercept = Fraction(0)
                multipliers = []
                for index, gap in enumerate(gaps):
                    total += gap
                    intercept += Fraction(3 ** index, 2 ** total)
                    multipliers.append(Fraction(3 ** (index + 1), 2 ** total))
                return intercept, max(multipliers), Fraction(1, 2 ** total)
            z, maximum, weight = record_data(word)
            z2, maximum2, weight2 = record_data(moved)
            require(2 * z2 == z and 2 * maximum2 == maximum and 2 * weight2 == weight,
                    "joint finite dyadic covariance")
            covariance_tests += 1
    print(json.dumps({
        "status": "pass", "source_octaves": 16, "actual_sources": sources,
        "same_clock_cells": cells, "exact_suffix_tests": suffix_tests,
        "word_endpoint_tests": template_tests,
        "joint_dyadic_covariance_tests": covariance_tests,
        "scope": "finite ordinary first-passage cells and exact template interfaces only"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
