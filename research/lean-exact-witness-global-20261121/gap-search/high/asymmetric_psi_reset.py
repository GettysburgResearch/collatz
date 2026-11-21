#!/usr/bin/env python3
"""Exact whole-affine replay of the unbounded asymmetric psi reset.

The Lean theorem quantifies over every index and supplied source tail.
This generator exposes one complete arithmetic progression at a requested
index. No search or convergence oracle is involved.
"""

import argparse
import json
from pathlib import Path

from unbounded_pump import coefficients, highest_drop, prefix, require


SOURCE_FRONT = [1, 2, 2, 3, 1, 3, 2, 1, 2, 3, 2, 3]
TARGET_BASE = [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3]


def make_rule(j, e):
    require(isinstance(j, int) and j >= 0, 'pump index must be nonnegative')
    require(isinstance(e, int) and e >= 3, 'initial even run must be at least three')
    ternary = 3 ** (j + 13)
    binary = 2 ** (e + 1)
    residue3 = 75116642 * pow(2 ** 24, -1, ternary) % ternary
    residue2 = 2 ** e
    first = residue2 + binary * ((residue3 - residue2)
                                 * pow(binary, -1, ternary) % ternary)
    parent = (binary * ternary, first)
    require(first >= 8 and first % 3 == 2, 'incorrect positive parent residue')
    require(first % binary == residue2, 'incorrect exact initial even run')
    numerator = 2 ** 24 * first - 75116642
    require(numerator > 0 and numerator % ternary == 0, 'incorrect ternary guard')
    child = (4 ** j * 2 ** 24 * binary, 1 + 4 ** j * (numerator // ternary))
    require(child[0] > parent[0] and child[1] > parent[1], 'source expansion failed')

    source_word = [2] * j + SOURCE_FRONT + [e - 1]
    target_word = [2] * j + TARGET_BASE
    r, total, correction = coefficients(source_word)
    vr, vt, vc = coefficients(target_word)
    require((r, total) == (j + 13, 2 * j + e + 24), 'source word sizes')
    require(correction + 3 ** (j + 13) == 75116642 * 4 ** j,
            'source correction identity')
    require((vr, vt) == (j + 14, 2 * j + 25), 'target word sizes')
    require(vc + 2 ** vt == 6 * correction + 3 ** (j + 14),
            'asymmetric target identity')
    require(max(source_word) <= e and min(source_word) > 0, 'illegal source gap')

    parent_odd = tuple(v // (2 ** e) for v in parent)
    require(parent_odd[0] % 2 == 0 and parent_odd[1] % 2 == 1,
            'parent odd endpoint is inexact')
    require(prefix(child, source_word) == parent_odd, 'source splice mismatch')
    child_target = (2 * child[0], 2 * child[1] - 1)
    parent_target = (2 * parent[0], 2 * parent[1] - 1)
    common_target = (3 * parent[0], 3 * parent[1] - 1)
    require(prefix(child_target, target_word) == common_target, 'child target mismatch')
    require(prefix(parent_target, [1]) == common_target, 'parent target mismatch')
    grade_pivot = highest_drop([2 * a for a in source_word], [2 * e + 1])
    require(grade_pivot == 2 * e + 1, 'incorrect graded multiset decrease')
    return dict(status='EXACT GUARDED PSI FAMILY; GLOBAL COVERAGE OPEN',
                pump_index=j, initial_even_run=e, parent_source=list(parent),
                child_source=list(child), source_prefix=source_word,
                child_target_prefix=target_word, parent_target_prefix=[1],
                common_source_endpoint=list(parent_odd),
                common_target_endpoint=list(common_target),
                affine_convention='[slope, intercept], parameter any nonnegative integer',
                ternary_residue=residue3, ternary_modulus=ternary,
                guard_cells_nested_in_pump_depth=True,
                inserted_length=len(source_word), source_clock_increase=2 * j + 24,
                graded_multiset_pivot=grade_pivot, inherits_entire_source_tail=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pump', type=int, default=0)
    parser.add_argument('--even-run', type=int, default=3)
    parser.add_argument('--receipt')
    args = parser.parse_args()
    output = json.dumps(make_rule(args.pump, args.even_run), indent=2, sort_keys=True) + '\n'
    if args.receipt:
        Path(args.receipt).write_text(output, encoding='utf-8')
    print(output, end='')


if __name__ == '__main__':
    main()
