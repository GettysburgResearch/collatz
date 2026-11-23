#!/usr/bin/env python3
"""Generate and exactly replay one arbitrary member of the high-gap pump.

The integer coefficients describe every nonnegative parameter in the returned
progression. The unbounded theorem is in Collatz/HighGapPump.lean; a run of
this program checks the requested indices, not a complete global dispatcher.
Only the Python standard library is used. No convergence oracle is used.
"""

import argparse
from collections import Counter
import json
from pathlib import Path


SOURCE_BASE = [1, 1, 3, 2, 3, 1, 3, 3]
TARGET_BASE = [3, 1, 1, 1, 1, 2, 2, 1, 1, 1, 3]
PARENT_TARGET = [1, 1, 2, 1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def coefficients(word):
    length = total = correction = 0
    for gap in word:
        require(isinstance(gap, int) and gap > 0, 'nonpositive gap')
        correction = 3 * correction + 2 ** total
        total += gap
        length += 1
    return length, total, correction


def prefix(start, word):
    """Replay an affine family at all nonnegative parameters simultaneously."""
    slope, intercept = start
    for gap in word:
        require(slope > 0 and intercept > 0, 'nonpositive affine state')
        require(slope % 2 == 0 and intercept % 2 == 1, 'non-odd pre-step state')
        divisor = 2 ** gap
        require((3 * slope) % divisor == 0, 'nonintegral affine slope')
        require((3 * intercept + 1) % divisor == 0, 'nonintegral affine intercept')
        slope, intercept = 3 * slope // divisor, (3 * intercept + 1) // divisor
    require(slope > 0 and intercept > 0, 'nonpositive endpoint')
    return slope, intercept


def highest_drop(new, old):
    left, right = Counter(new), Counter(old)
    changed = [a for a in left.keys() | right.keys() if left[a] != right[a]]
    require(changed, 'identical exponent multisets')
    pivot = max(changed)
    require(left[pivot] < right[pivot], 'multiset does not decrease')
    return pivot


def make_rule(j, a):
    require(isinstance(j, int) and j >= 0, 'pump index must be nonnegative')
    require(isinstance(a, int) and a >= 5, 'parent first gap must be at least five')
    power3, power4 = 3 ** j, 4 ** j
    modulus3 = 3 ** (j + 7)
    numerator = 4096 * power4
    offset = 81 * power3 - 554 * power4
    residue3 = -offset * pow(numerator, -1, modulus3) % modulus3

    # Specify the exact first source gap a, rather than just its lower bound.
    modulus2 = 2 ** (a + 1)
    residue2 = (2 ** a - 1) * pow(81, -1, modulus2) % modulus2
    first = residue2 + modulus2 * ((residue3 - residue2)
                                  * pow(modulus2, -1, modulus3) % modulus3)
    parent = (modulus2 * modulus3, first)
    require(first > 0 and first % 32 == 15, 'incorrect parent entrance')
    require((numerator * first + offset) % modulus3 == 0, 'incorrect child guard')
    child = (numerator * modulus2, (numerator * first + offset) // modulus3)
    require(child[0] > parent[0] and child[1] > parent[1], 'expected source expansion')

    unadjusted = [2] * j + SOURCE_BASE
    source_word = unadjusted[:-1] + [a - 2]
    target_word = (TARGET_BASE if j == 0 else
                   [1] + [2] * (j - 1) + [4] + TARGET_BASE[1:])
    r, b, c = coefficients(unadjusted)
    vr, vb, vc = coefficients(target_word)
    require((r, b) == (j + 8, 2 * j + 17), 'source word size identity')
    require(c + 3 ** (j + 8) == 48970 * power4, 'source correction identity')
    require((vr, vb) == (j + 11, 2 * j + 17), 'target word size identity')
    require(vc + 3 ** (j + 10) == 702874 * power4, 'target correction identity')

    parent_source = tuple(27 * v for v in parent)
    child_source = tuple(27 * v for v in child)
    source_end = prefix(parent_source, [a])
    require(source_end == prefix(child_source, source_word), 'source splice mismatch')
    require(source_end[0] % 2 == 0 and source_end[1] % 2 == 1, 'inexact final source gap')
    parent_target = tuple(9 * v for v in parent)
    child_target = tuple(9 * v for v in child)
    target_end = prefix(parent_target, PARENT_TARGET)
    require(target_end == prefix(child_target, target_word), 'target splice mismatch')
    pivot = highest_drop(source_word, [a])
    require(pivot == a and max(source_word) < a, 'wrong multiset pivot')
    require(sum(source_word) - a == 2 * j + 12, 'incorrect source clock increment')

    # Exact valuation selector: each eligible ordinary m determines its own j.
    linear = 4096 * first - 554
    valuation = 0
    while linear % 3 == 0:
        valuation += 1
        linear //= 3
    require(valuation == j + 4, 'incorrect unbounded valuation selector')
    require((power4 * linear + 1) % 27 == 0, 'incorrect normalized unit guard')

    return dict(status='EXACT GUARDED FAMILY; GLOBAL COVERAGE OPEN', pump_index=j,
                parent_first_gap=a, parent_m=list(parent), child_p=list(child),
                affine_convention='[slope, intercept], parameter any nonnegative integer',
                ternary_residue=residue3, ternary_modulus=modulus3,
                source_prefix=source_word, parent_target_prefix=PARENT_TARGET,
                child_target_prefix=target_word, common_source_endpoint=list(source_end),
                common_target_endpoint=list(target_end), multiset_pivot=pivot,
                inserted_length=len(source_word), source_clock_increase=2 * j + 12,
                inherits_entire_source_tail=True, child_source_strictly_larger=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pump', type=int, default=0)
    parser.add_argument('--first-gap', type=int, default=5)
    parser.add_argument('--receipt')
    args = parser.parse_args()
    result = make_rule(args.pump, args.first_gap)
    output = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.receipt:
        Path(args.receipt).write_text(output, encoding='utf-8')
    print(output, end='')


if __name__ == '__main__':
    main()
