#!/usr/bin/env python3
"""Total cofinal source rewrites from a supplied complete Collatz certificate.

The all-bound existence and strict multiset decrease are proved in
Collatz/BoundedGapCofinal.lean. This implementation follows that construction
using exact integers. It never evaluates a wanted target's Collatz orbit.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def certificate(source, word):
    """Validate every supplied gap and the complete endpoint, including loops."""
    require(isinstance(source, int) and source > 0 and source % 2 == 1,
            'a certificate source must be positive and odd')
    value = source
    states = [value]
    for gap in word:
        require(isinstance(gap, int) and gap > 0, 'all gaps must be positive')
        value, remainder = divmod(3 * value + 1, 2 ** gap)
        require(remainder == 0 and value > 0 and value % 2 == 1,
                'the supplied gap does not have a positive odd endpoint')
        states.append(value)
    require(value == 1, 'the complete supplied certificate must end at one')
    return states


def predecessor(unit):
    """The six exact branches of the kernel-checked unit_predecessor."""
    require(unit > 0 and unit % 2 == 1 and unit % 3 != 0,
            'predecessor endpoint must be a positive odd ternary unit')
    gap = {1: 4, 5: 3, 7: 4, 11: 3, 13: 2, 17: 1}[unit % 18]
    parent, remainder = divmod(2 ** gap * unit - 1, 3)
    require(remainder == 0 and parent > 1 and parent % 2 == 1 and parent % 3,
            'unit predecessor invariant failed')
    return parent, gap


def cofinal(source, tail, bound):
    """Produce a certified unit above any bound; there is no search cutoff.

    Every selected parent is nonterminal and has the supplied certified tail.
    BoundedGapCofinal.cofinal_predecessors proves termination: an arbitrarily
    long such chain cannot stay inside a fixed finite interval. The explicit
    table here is the same one used in that proof.
    """
    certificate(source, tail)
    require(source % 3 != 0, 'cofinal endpoint must be a ternary unit')
    require(isinstance(bound, int) and bound >= 0, 'bound must be nonnegative')
    value = source
    inverse_gaps = []
    while value <= bound:
        value, gap = predecessor(value)
        inverse_gaps.append(gap)
    prefix = list(reversed(inverse_gaps))
    certificate(value, prefix + tail)
    return value, prefix


def grades(even_run, gaps):
    return ([2 * even_run + 1] if even_run else []) + [2 * gap for gap in gaps]


def strict_drop(child, parent):
    child_counts, parent_counts = Counter(child), Counter(parent)
    changed = [grade for grade in child_counts.keys() | parent_counts.keys()
               if child_counts[grade] != parent_counts[grade]]
    require(bool(changed), 'rank did not change')
    pivot = max(changed)
    require(child_counts[pivot] < parent_counts[pivot],
            'the highest changed grade did not decrease')
    return pivot


def rewrite(source, even_run, gaps, bound, high_gap_index=None):
    require(isinstance(even_run, int) and even_run >= 0,
            'initial even run must be nonnegative')
    odd, remainder = divmod(source, 2 ** even_run)
    require(remainder == 0, 'initial even run does not divide the source')
    states = certificate(odd, gaps)
    if high_gap_index is None:
        high_gap_index = next((i for i, gap in enumerate(gaps) if gap >= 5), None)
    if high_gap_index is not None:
        require(0 <= high_gap_index < len(gaps) and gaps[high_gap_index] >= 5,
                'selected odd gap must be at least five')
        tail = gaps[high_gap_index + 1:]
        endpoint = states[high_gap_index + 1]
        reason = 'odd gap at least five'
    else:
        require(even_run >= 4, 'rewrite needs a high odd gap or even run at least four')
        # This matches large_even_replacement, including ternary nonunits.
        tail = gaps[1:] if gaps else []
        endpoint = states[1] if gaps else odd
        reason = 'initial even run at least four'
    child, prefix = cofinal(endpoint, tail, bound)
    child_word = prefix + tail
    pivot = strict_drop(grades(0, child_word), grades(even_run, gaps))
    return dict(status='COMPLETE SOURCE REWRITE; LOW INTERVAL COVERAGE OPEN',
                parent_source=source, parent_even_run=even_run, parent_word=gaps,
                requested_bound=bound, consumed_high_gap_index=high_gap_index,
                rewrite_reason=reason, retained_endpoint=endpoint, retained_tail=tail,
                child_source=child, child_even_run=0, inserted_prefix=prefix,
                child_word=child_word, inserted_alphabet_bound=4,
                child_strictly_above_bound=child > bound,
                highest_changed_grade=pivot, target_orbit_evaluated=False)


def replay():
    fixtures = [
        (21, 0, [6]),
        (35, 0, [1, 5, 4]),
        (909, 0, [3, 10]),
        (16, 4, []),
        (112, 4, [1, 1, 2, 3, 4]),
        (96, 5, [1, 4]),
    ]
    bounds = [0, 1, 1000, 10 ** 100, 2 ** 1024]
    cases = [rewrite(source, run, word, bound)
             for source, run, word in fixtures for bound in bounds]
    compact = []
    for case in cases:
        word = case.pop('child_word')
        prefix = case.pop('inserted_prefix')
        case['inserted_length'] = len(prefix)
        case['inserted_gap_counts'] = dict(sorted(Counter(prefix).items()))
        case['child_odd_length'] = len(word)
        case['child_shortcut_clock'] = sum(word)
        case['child_word_sha256'] = hashlib.sha256(
            json.dumps(word, separators=(',', ':')).encode('ascii')).hexdigest()
        compact.append(case)
    return dict(status='PASS', cases=len(cases),
                scope='Exact complete certificates and rank drops at selected inputs; '
                      'all-bound theorem is in Lean; no target convergence test.',
                results=compact)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=int, default=35)
    parser.add_argument('--even-run', type=int, default=0)
    parser.add_argument('--gaps', default='1,5,4')
    parser.add_argument('--bound', type=int, default=1000)
    parser.add_argument('--high-gap-index', type=int)
    parser.add_argument('--replay', action='store_true')
    parser.add_argument('--receipt')
    args = parser.parse_args()
    gaps = [int(value) for value in args.gaps.split(',') if value.strip()]
    result = replay() if args.replay else rewrite(
        args.source, args.even_run, gaps, args.bound, args.high_gap_index)
    output = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.receipt:
        Path(args.receipt).write_text(output, encoding='utf-8')
    print(output, end='')


if __name__ == '__main__':
    main()
