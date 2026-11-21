#!/usr/bin/env python3
"""Exact affine replay of the arbitrary-length (1,b) source pump.

Shared arithmetic helpers are imported from unbounded_pump, never from Lean
or a claimed universal dispatcher. The arbitrary-index proof is separate.
"""

import argparse
import json
from pathlib import Path

from unbounded_pump import coefficients, highest_drop, prefix, require


SOURCE_BASE = [1, 1, 3, 2, 3, 1, 2, 2, 2]
TARGET_BASE = [3, 1, 1, 1, 1, 2, 2, 1, 4, 1]
PARENT_TARGET = [2, 2, 1]


def make_rule(j, b):
    require(isinstance(j, int) and j >= 0, 'pump index must be nonnegative')
    require(isinstance(b, int) and b >= 4, 'second parent gap must be at least four')
    power3, power4 = 3 ** j, 4 ** j
    modulus3 = 3 ** (j + 7)
    numerator = 4096 * power4
    offset = 81 * power3 - 554 * power4
    residue3 = -offset * pow(numerator, -1, modulus3) % modulus3
    modulus2 = 2 ** (b + 2)
    residue2 = (2 ** (b + 1) - 5) * pow(243, -1, modulus2) % modulus2
    first = residue2 + modulus2 * ((residue3 - residue2)
                                  * pow(modulus2, -1, modulus3) % modulus3)
    require(first > 0 and first % 32 == 25, 'incorrect binary parent cell')
    parent = (modulus2 * modulus3, first)
    require((numerator * first + offset) % modulus3 == 0, 'incorrect child guard')
    child = (numerator * modulus2, (numerator * first + offset) // modulus3)
    require(child[0] > parent[0] and child[1] > parent[1], 'expected source expansion')

    unadjusted = [2] * j + SOURCE_BASE
    source_word = unadjusted[:-1] + [b - 2]
    target_word = (TARGET_BASE if j == 0 else
                   [1] + [2] * (j - 1) + [4] + TARGET_BASE[1:])
    r, clock, correction = coefficients(unadjusted)
    vr, vb, vc = coefficients(target_word)
    require((r, clock) == (j + 9, 2 * j + 17), 'source sizes')
    require(correction + 3 ** (j + 9) == 155102 * power4, 'source correction')
    require((vr, vb) == (j + 10, clock), 'target sizes')
    require(vc == correction + 2 ** clock, 'target correction')

    source_end = prefix(tuple(27 * v for v in parent), [1, b])
    require(source_end == prefix(tuple(27 * v for v in child), source_word),
            'source splice mismatch')
    require(source_end[0] % 2 == 0 and source_end[1] % 2 == 1, 'inexact source gaps')
    target_end = prefix(tuple(9 * v for v in parent), PARENT_TARGET)
    require(target_end == prefix(tuple(9 * v for v in child), target_word),
            'target splice mismatch')
    pivot = highest_drop(source_word, [1, b])
    require(pivot == b and max(source_word) < b, 'incorrect multiset decrease')
    require(sum(source_word) - (1 + b) == 2 * j + 12, 'source clock increment')
    return dict(status='EXACT GUARDED LOW-GAP FAMILY; GLOBAL COVERAGE OPEN',
                pump_index=j, parent_gaps=[1, b], parent_m=list(parent),
                child_p=list(child), source_prefix=source_word,
                parent_target_prefix=PARENT_TARGET, child_target_prefix=target_word,
                affine_convention='[slope, intercept], parameter any nonnegative integer',
                common_source_endpoint=list(source_end), common_target_endpoint=list(target_end),
                inserted_length=len(source_word), source_clock_increase=2 * j + 12,
                multiset_pivot=pivot, inherits_entire_source_tail=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pump', type=int, default=0)
    parser.add_argument('--second-gap', type=int, default=4)
    parser.add_argument('--receipt')
    args = parser.parse_args()
    output = json.dumps(make_rule(args.pump, args.second_gap), indent=2, sort_keys=True) + '\n'
    if args.receipt:
        Path(args.receipt).write_text(output, encoding='utf-8')
    print(output, end='')


if __name__ == '__main__':
    main()
