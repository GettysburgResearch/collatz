#!/usr/bin/env python3
"""Exact, finite high-gap source-zero search; universal closure is unresolved.

Only Python's standard library is used. The full catalogue is regenerated in
memory and checked universally by rational affine identities. By default only
a compact deterministic receipt is emitted; --catalog optionally saves it.
"""

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def correction(word):
    clock = value = 0
    for exponent in word:
        value = 3 * value + (1 << clock)
        clock += exponent
    return clock, value


def integral_suffixes():
    result = []
    for word in product(range(1, 5), repeat=4):
        clock, value = correction(word)
        if ((1 << clock) - 32 * value) % 81 == 0:
            result.append((word, clock, value))
    require(len(result) == 6, 'incorrect length-four integrality census')
    return result


def source_words(length, suffixes):
    if length < 4:
        for word in product(range(1, 5), repeat=length):
            clock, value = correction(word)
            if ((1 << clock) - 32 * value) % 81 == 0:
                yield word, clock, value
        return
    for prefix in product(range(1, 5), repeat=length - 4):
        prefix_clock, prefix_value = correction(prefix)
        for suffix, suffix_clock, suffix_value in suffixes:
            yield (prefix + suffix, prefix_clock + suffix_clock,
                   81 * prefix_value + (1 << prefix_clock) * suffix_value)


def target_word(length, clock, value):
    """Exact signed-reference test, terminated by its nonnegative clock grade.

    The denominator starts at 3^(length+2). At each odd step its ternary
    exponent drops until integral. A target reaching -1 gives k additional
    parent exponent-one steps. Only k=0 or1 is later retained.
    """
    goal = clock - length - 3
    if goal < 0:
        return None
    numerator = -((1 << clock) + 3 * value)
    denominator = 3 ** (length + 2)
    grade = 0
    word = []
    while True:
        if numerator == -denominator:
            if grade != goal:
                return None
            padding = len(word) - length - 2
            require(padding >= 0, 'unexpected early denominator clearing')
            return padding, tuple(word)
        if numerator >= 0:
            return None
        if denominator > 1:
            denominator //= 3
            numerator += denominator
        else:
            numerator = 3 * numerator + 1
        if numerator == 0:
            return None
        absolute = abs(numerator)
        exponent = (absolute & -absolute).bit_length() - 1
        require(exponent >= 1, 'signed reference ceased to be odd')
        grade += exponent - 1
        if grade > goal:
            return None
        numerator //= 1 << exponent
        word.append(exponent)


def partial_prefix(start, word):
    """Every pre-step state is positive odd; the final state may be even."""
    slope, intercept = start
    for exponent in word:
        require(slope.denominator == intercept.denominator == 1,
                'nonintegral pre-step affine state')
        require(slope > 0 and slope % 2 == 0 and intercept > 0 and intercept % 2 == 1,
                'invalid positive odd affine state')
        slope = 3 * slope / (1 << exponent)
        intercept = (3 * intercept + 1) / (1 << exponent)
    require(slope.denominator == intercept.denominator == 1 and min(slope, intercept) > 0,
            'invalid partial affine endpoint')
    return slope, intercept


def verify_rule(word, clock, value, padding, target):
    length = len(word)
    require(padding in (0, 1), 'target template is not uniform for all high gaps')
    target_clock, target_value = correction(target)
    require(len(target) == length + 2 + padding and target_clock == clock + padding - 1,
            'target grade mismatch')
    require(target_value == 3 ** padding * ((1 << clock) + 3 * value)
            - (1 << (clock + padding - 1)), 'target correction mismatch')
    require(all(1 <= exponent <= 4 for exponent in word), 'source alphabet mismatch')

    numerator = 1 << clock
    offset = (numerator - 32 * value) // 81
    require(numerator - 32 * value == 81 * offset, 'integral ternary guard failed')
    ternary_modulus = 3 ** (length - 1)
    residue = (-offset * pow(numerator, -1, ternary_modulus)) % ternary_modulus
    modulus = 32 * ternary_modulus
    first = 15 + 32 * ((residue - 15) * pow(32, -1, ternary_modulus) % ternary_modulus)
    threshold = max(1, (-offset) // numerator + 1)
    first += max(0, (threshold - first + modulus - 1) // modulus) * modulus
    parent = Fraction(modulus), Fraction(first)
    child = (numerator * parent[0] / (32 * ternary_modulus),
             (numerator * parent[1] + offset) / (32 * ternary_modulus))
    source = partial_prefix((27 * parent[0], 27 * parent[1]), (5,))
    child_source = partial_prefix((27 * child[0], 27 * child[1]), word)
    desired = partial_prefix((9 * parent[0], 9 * parent[1]), (1, 1, 2) + (1,) * padding)
    child_desired = partial_prefix((9 * child[0], 9 * child[1]), target)
    require(source == child_source and desired == child_desired, 'affine endpoints fail to meet')

    # For the fixed receipt length<=14. If the parent first gap is a=5+h,
    # inserted gaps are word[:-1] followed by word[-1]+h, all <=a-1.
    # Thus sum(15^inserted) <=14*15^(a-1)<15^a, for every h>=0.
    if length <= 14:
        require(length < 15 and word[-1] <= 4, 'C15 energy guard failed')
    return dict(r=length, B=clock, C=value, k=padding, W=list(word), V=list(target),
                ternary_precision=length - 1, ternary_modulus=ternary_modulus,
                ternary_residue=residue, parent_modulus=modulus, first_parent=first,
                slope=str(Fraction(numerator, 32 * ternary_modulus)),
                offset=str(Fraction(offset, 32 * ternary_modulus)))


def prefix_union(rules):
    """Exact union of finite ternary cylinders, with all sibling merges."""
    cells = set()
    for precision, residue in sorted((rule['ternary_precision'], rule['ternary_residue'])
                                     for rule in rules):
        if any((depth, residue % (3 ** depth)) in cells for depth in range(precision + 1)):
            continue
        cells.add((precision, residue))
        while precision:
            parent = residue % (3 ** (precision - 1))
            siblings = {(precision, parent + digit * 3 ** (precision - 1)) for digit in range(3)}
            if not siblings <= cells:
                break
            cells -= siblings
            precision -= 1
            residue = parent
            cells.add((precision, residue))
    measure = sum((Fraction(1, 3 ** precision) for precision, _ in cells), Fraction())
    return sorted(cells), measure


def digest(data):
    canonical = json.dumps(data, sort_keys=True, separators=(',', ':')).encode()
    return sha256(canonical).hexdigest()


def run(maximum_length):
    suffixes = integral_suffixes()
    rules = []
    census = []
    for length in range(1, maximum_length + 1):
        tested = nonuniform = new_rules = 0
        for word, clock, value in source_words(length, suffixes):
            tested += 1
            result = target_word(length, clock, value)
            if result is None:
                continue
            padding, target = result
            if padding not in (0, 1):
                nonuniform += 1
                continue
            rules.append(verify_rule(word, clock, value, padding, target))
            new_rules += 1
        census.append(dict(r=length, integral_source_words=tested, new_rules=new_rules,
                           excluded_nonuniform_target_templates=nonuniform))
    cells, measure = prefix_union(rules)
    mathematical_records = dict(rules=rules, prefix_cells=cells)
    receipt = dict(status='EXACT FINITE SEARCH; UNIVERSAL CLOSURE REMAINS OPEN',
        grammar=dict(parent_state='Basin(27m) -> Basin(9m)', parent_first_gap='a>=5',
                     parent_binary_guard='m=15 mod32', child_source_alphabet=[1, 2, 3, 4],
                     target_padding=[0, 1], maximum_child_length=maximum_length,
                     child_size_contraction_required=False),
        integral_suffixes=[list(word) for word, _, _ in suffixes], census=census,
        rules=len(rules), minimal_ternary_prefix_cells=len(cells),
        ternary_cylinder_measure=str(measure), full_high_gap_ternary_cover=(cells == [(0, 0)]),
        child_slope_counts=dict(Counter('expanding' if Fraction(rule['slope']) > 1 else 'contracting'
                                       for rule in rules)),
        exponent_energy_base=15 if maximum_length <= 14 else None,
        energy_scope='For each retained rule and every a>=5; inherited tail is unchanged',
        remaining_obligations=['uncovered high-gap ternary cells',
                               'source first gaps 1 through3',
                               'any auxiliary comparison states required by a global dispatcher'],
        separate_gap_four='Handled by the ordinary merger in the direct-R normal forms',
        mathematical_records_sha256=digest(mathematical_records))
    return receipt, mathematical_records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-r', type=int, default=14)
    parser.add_argument('--receipt')
    parser.add_argument('--catalog')
    args = parser.parse_args()
    require(1 <= args.max_r <= 14, 'this checkpoint supports finite lengths1 through14')
    receipt, records = run(args.max_r)
    text = json.dumps(receipt, sort_keys=True, indent=2) + '\n'
    if args.receipt:
        Path(args.receipt).write_text(text)
    if args.catalog:
        Path(args.catalog).write_text(json.dumps(records, sort_keys=True, separators=(',', ':')) + '\n')
    print(text, end='')


if __name__ == '__main__':
    main()
