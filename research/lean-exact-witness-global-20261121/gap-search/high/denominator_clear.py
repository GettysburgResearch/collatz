#!/usr/bin/env python3
"""Construct and exactly replay the uniform ternary denominator-clearing rule.

The all-index existence, clock bounds, and full-witness rewrite are proved in
Collatz/MergerDenominatorClear.lean. This independent integer implementation
checks one requested template and its entire ordinary affine progression.
It does not run a convergence oracle on the terminal additive offset.
"""

import argparse
import json
from pathlib import Path

from unbounded_pump import coefficients, highest_drop, prefix, require


def clear_template(k):
    require(isinstance(k, int) and k >= 1, 'denominator power must be positive')
    if k == 1:
        return [1], 0
    numerator = -1
    denominator = 3 ** k
    word = []
    for _ in range(k):
        # After cancellation of one ternary factor, each step has a positive
        # even numerator. No rational floating point arithmetic is used.
        denominator //= 3
        numerator += denominator
        require(numerator > 0 and numerator % 2 == 0, 'invalid clearing step')
        gap = (numerator & -numerator).bit_length() - 1
        numerator >>= gap
        word.append(gap)
    require(denominator == 1, 'uncleared denominator')
    return word, numerator


def make_rule(k, first_gap=None):
    word, offset = clear_template(k)
    length, clock, correction = coefficients(word)
    require(length == k, 'wrong odd-step count')
    require(correction == 1 + 2 ** clock * offset, 'clearing identity')
    require(max(word) <= 2 * k - 1 and clock <= k * (2 * k - 1),
            'quadratic clock or gap bound failed')
    require(2 ** k * (offset + 1) < 3 ** k, 'terminal height bound failed')
    a = clock if first_gap is None else first_gap
    require(isinstance(a, int) and a >= clock, 'first source gap must fit template')
    modulus = 2 ** (a + 1)
    first = (2 ** a - 1) * pow(3 ** k, -1, modulus) % modulus
    target = (modulus, first)
    source = tuple(3 ** (k - 1) * v for v in target)
    odd_tail = prefix(source, [a])
    require(odd_tail[0] % 2 == 0 and odd_tail[1] % 2 == 1, 'inexact source gap')
    even_run = a - clock
    child = tuple(2 ** even_run * v for v in odd_tail)
    wanted = (child[0], child[1] + offset)
    require(prefix(target, word) == wanted, 'ordinary target splice mismatch')
    child_grades = [] if even_run == 0 else [2 * even_run + 1]
    pivot = highest_drop(child_grades, [2 * a])
    require(pivot == 2 * a, 'incorrect full-source rank decrease')
    return dict(status='EXACT ADDITIVE HANDOFF; ADDITIVE COVERAGE OPEN',
                denominator_power=k, reverse_factor=3 ** (k - 1),
                target_prefix=word, target_clock=clock, additive_offset=offset,
                source_first_gap=a, remaining_even_run=even_run,
                parent_known_source=list(source), parent_wanted_target=list(target),
                child_known_source=list(child), child_wanted_target=list(wanted),
                inherited_odd_tail_source=list(odd_tail),
                affine_convention='[slope, intercept], parameter any nonnegative integer',
                graded_multiset_pivot=pivot, inherits_entire_source_tail=True,
                terminal_convergence_not_assumed=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--power', type=int, default=3)
    parser.add_argument('--first-gap', type=int)
    parser.add_argument('--receipt')
    args = parser.parse_args()
    output = json.dumps(make_rule(args.power, args.first_gap), indent=2, sort_keys=True) + '\n'
    if args.receipt:
        Path(args.receipt).write_text(output, encoding='utf-8')
    print(output, end='')


if __name__ == '__main__':
    main()
