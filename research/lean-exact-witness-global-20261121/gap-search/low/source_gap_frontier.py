#!/usr/bin/env python3
"""Exact one-query affine dispatcher using accelerated-exponent multisets.

The shared ordinary frontier can have an arbitrary final two-adic valuation.
That valuation is added to the final gap on both nonempty source prefixes.
It is checked symbolically by a finite exhaustive breakpoint argument.
"""
import argparse
from collections import Counter, deque
import json
from math import gcd
from pathlib import Path


def forward(node):
    a, b = node
    if a % 2:
        raise ValueError('odd-slope frontier has no uniform next step')
    return ('E', (a // 2, b // 2)) if b % 2 == 0 else ('O', (3 * a // 2, (3 * b + 1) // 2))


def frontier(node):
    path = []
    while node[0] % 2 == 0:
        move, node = forward(node)
        path.append([move, list(node)])
    return node, path


def invert_path(start, path):
    nodes = [start] + [tuple(step[1]) for step in path]
    inverse = {'O': 'I', 'E': 'D'}
    return [[inverse[path[i][0]], list(nodes[i])] for i in range(len(path) - 1, -1, -1)]


def oddpart_residues(a, b, modulus):
    if min(a, b) <= 0 or modulus % 2:
        raise ValueError('invalid positive affine query domain')
    while a % 2 == b % 2 == 0:
        a //= 2
        b //= 2
    if a % 2 == 0:
        divisor = gcd(a, modulus)
        return [r for r in range(1, modulus, 2) if (r - b) % divisor == 0]
    odd_modulus = modulus
    while odd_modulus % 2 == 0:
        odd_modulus //= 2
    divisor = gcd(a, odd_modulus)
    orbit = set()
    residue = b % divisor
    while residue not in orbit:
        orbit.add(residue)
        residue = residue * pow(2, -1, divisor) % divisor if divisor > 1 else 0
    return [r for r in range(1, modulus, 2) if r % divisor in orbit]


def queries_and_verify(row):
    modulus, residue, kind = row['M'], row['r'], row['p']
    if kind not in ('F3', 'R3') or modulus % 2 or not 0 < residue < modulus or residue % 2 != 1:
        raise ValueError('invalid root')
    starts = [(modulus, residue), (3 * modulus, 3 * residue)]
    if kind == 'R3':
        starts.reverse()
    queries = []
    endpoints = []
    for side, name in enumerate(('left', 'right')):
        node = starts[side]
        for move, output in row[name]:
            a, b = node
            if move == 'D':
                expected = (2 * a, 2 * b)
            elif move == 'E':
                if a % 2 or b % 2:
                    raise ValueError('invalid even edge')
                expected = (a // 2, b // 2)
            elif move == 'O':
                if a % 2 or b % 2 != 1:
                    raise ValueError('invalid odd edge')
                expected = (3 * a // 2, (3 * b + 1) // 2)
            elif move == 'I':
                if a % 3 or (2 * b - 1) % 3:
                    raise ValueError('invalid inverse odd edge')
                expected = (2 * a // 3, (2 * b - 1) // 3)
            elif move in ('M3', 'V3'):
                if move == 'M3':
                    expected = (3 * a, 3 * b)
                    query_base = node
                else:
                    if a % 3 or b % 3:
                        raise ValueError('invalid division query')
                    expected = (a // 3, b // 3)
                    query_base = expected
                child_kind = 'F3' if (move == 'M3') == (side == 0) else 'R3'
                queries.append({'kind': child_kind, 'form': list(query_base),
                                'residues': oddpart_residues(*query_base, modulus)})
            else:
                raise ValueError('unknown move')
            if tuple(output) != expected or min(expected) <= 0:
                raise ValueError('affine edge mismatch')
            node = expected
        endpoints.append(node)
    if endpoints[0] != endpoints[1] or endpoints[0] != tuple(row['endpoint']):
        raise ValueError('path endpoints disagree')
    return queries


def gaps(path):
    result = []
    for move, node in path:
        if move == 'O':
            result.append(1)
        elif move == 'E' and result:
            result[-1] += 1
        else:
            raise ValueError('not an odd-start forward ordinary path')
    return tuple(result)


def smaller_multiset(old, new):
    difference = Counter(old)
    difference.subtract(new)
    differing = [a for a, count in difference.items() if count]
    return bool(differing) and difference[max(differing)] > 0


def gap_guard(old, new):
    if not old:
        return False
    if not new:
        return True
    # Above this cutoff both variable final gaps exceed all fixed gaps.
    # Their order and every remaining fixed count then stay unchanged.
    cutoff = max(old + new) + 1
    if old[-1] < new[-1]:
        return False
    return all(smaller_multiset(old[:-1] + (old[-1] + delta,),
                                new[:-1] + (new[-1] + delta,))
               for delta in range(cutoff + 1))


def predecessors(root, source_gaps):
    """Enumerate every potentially decreasing inverse accelerated word.

    Each inverse odd step consumes one factor3 from the affine slope.  Every
    inserted gap is <=max(source_gaps), by the necessary delta=0 comparison.
    A failed partial multiset comparison cannot improve by prepending letters.
    """
    todo = deque([(root, (), [])])
    while todo:
        node, word, path = todo.popleft()
        yield node, word, path
        a, b = node
        if a % 3:
            continue
        for exponent in range(1, max(source_gaps) + 1):
            numerator = (1 << exponent) * b - 1
            if numerator % 3:
                continue
            child = ((1 << exponent) * a // 3, numerator // 3)
            word2 = (exponent,) + word
            if min(child) <= 0 or not gap_guard(source_gaps, word2):
                continue
            prefix = []
            state = child
            for index in range(exponent):
                move, state = forward(state)
                if move != ('O' if index == 0 else 'E'):
                    raise ValueError('inverse accelerated word is not exact')
                prefix.append([move, list(state)])
            if state != node:
                raise ValueError('inverse accelerated endpoint')
            todo.append((child, word2, prefix + path))


def search(kind, modulus, residue, deep_children=False):
    starts = ((modulus, residue), (3 * modulus, 3 * residue))
    if kind == 'R3':
        starts = starts[::-1]
    source_frontier, source_path = frontier(starts[0])
    target_frontier, target_path = frontier(starts[1])
    source_gaps = gaps(source_path)
    rows = []
    nodes = 0
    if source_frontier == target_frontier:
        rows.append({'p': kind, 'M': modulus, 'r': residue,
                     'left': source_path, 'right': target_path,
                     'endpoint': list(source_frontier), 'ordinary_merger': True,
                     'dependencies': []})
    for source, word, forward_path in predecessors(source_frontier, source_gaps):
        nodes += 1
        for child_kind in ('F3', 'R3'):
            if child_kind == 'F3':
                if deep_children:
                    continue
                desired = (3 * source[0], 3 * source[1])
                move = 'M3'
                query = source
            else:
                if source[0] % 3 or source[1] % 3:
                    continue
                desired = (source[0] // 3, source[1] // 3)
                move = 'V3'
                query = desired
                if deep_children and (query[0] % 9 or query[1] % 9):
                    continue
            desired_frontier, desired_path = frontier(desired)
            if desired_frontier != target_frontier:
                continue
            row = {'p': kind, 'M': modulus, 'r': residue,
                   'left': source_path + invert_path(source, forward_path) + [[move, list(desired)]],
                   'right': target_path + invert_path(desired, desired_path),
                   'endpoint': list(desired),
                   'source_gap_prefix': list(source_gaps), 'child_gap_prefix': list(word),
                   'shared_final_valuation': True,
                   'query_kind': child_kind, 'query_base': list(query),
                   'finite_entrance_parameters': [0]}
            queries = queries_and_verify(row)
            if len(queries) != 1 or queries[0]['kind'] != child_kind:
                raise ValueError('query replay')
            row['dependencies'] = [[child_kind, r] for r in queries[0]['residues']]
            rows.append(row)
    return rows, {'kind': kind, 'r': residue, 'source_gap_prefix': list(source_gaps),
                  'inverse_nodes': nodes}


def closure(rows, modulus):
    choices = {}
    for row in rows:
        choices.setdefault((row['p'], row['r']), []).append(row)
    active = set(choices)
    rounds = []
    while True:
        dead = {state for state in active
                if not any(all(tuple(dep) in active for dep in row['dependencies'])
                           for row in choices[state])}
        if not dead:
            break
        active -= dead
        rounds.append(len(dead))
    required = {('R3', r) for r in range(9, modulus, 18)}
    return {'closed_states': len(active), 'required_present': len(active & required),
            'required_total': len(required), 'removal_rounds': rounds,
            'active_states': [list(state) for state in sorted(active)],
            'missing_required': [list(state) for state in sorted(required - active)]}


def verify_rows(rows):
    """Replay paths and independently check an all-delta integer energy formula."""
    base = max(2, 1 + max((len(row.get('child_gap_prefix', ())) for row in rows), default=0))
    mergers = replacements = 0
    for row in rows:
        queries = queries_and_verify(row)
        if row.get('ordinary_merger'):
            if queries or row['dependencies']:
                raise ValueError('queried unconditional merger')
            mergers += 1
            continue
        if len(queries) != 1:
            raise ValueError('replacement requires exactly one query')
        query = queries[0]
        if query['kind'] != row['query_kind'] or query['form'] != row['query_base']:
            raise ValueError('incorrect query metadata')
        expected_dependencies = [[query['kind'], r] for r in query['residues']]
        if row['dependencies'] != expected_dependencies:
            raise ValueError('incorrect exact query domains')
        factor = 3 if row['p'] == 'R3' else 1
        parent = (factor * row['M'], factor * row['r'])
        child_factor = 3 if query['kind'] == 'R3' else 1
        child = tuple(child_factor * x for x in query['form'])
        parent_endpoint, parent_path = frontier(parent)
        child_endpoint, child_path = frontier(child)
        old, new = gaps(parent_path), gaps(child_path)
        if parent_endpoint != child_endpoint:
            raise ValueError('source prefixes do not join')
        if list(old) != row['source_gap_prefix'] or list(new) != row['child_gap_prefix']:
            raise ValueError('incorrect source-word prefix')
        if not old:
            raise ValueError('empty removed source prefix')
        coefficient = base ** old[-1] - (base ** new[-1] if new else 0)
        constant = sum(base ** a for a in old[:-1]) - sum(base ** b for b in new[:-1])
        # Difference is coefficient*base**delta + constant for every delta>=0.
        if coefficient < 0 or coefficient + constant <= 0:
            raise ValueError('energy does not decrease for every shared final valuation')
        replacements += 1
    return {'all_affine_edges_replayed': len(rows), 'ordinary_mergers': mergers,
            'universal_gap_energy_polynomials_checked': replacements,
            'uniform_gap_energy_base': base,
            'rank_formula': 'sum(base**gap); delta is the shared final two-adic valuation'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--M', type=int, default=288)
    parser.add_argument('--out', required=True)
    parser.add_argument('--deep-only', action='store_true')
    parser.add_argument('--deep-children', action='store_true')
    args = parser.parse_args()
    if args.M <= 0 or args.M % 18:
        raise ValueError('modulus must be divisible by18')
    roots = ([('R3', r) for r in range(9, args.M, 18)] if args.deep_only
             else [(kind, r) for r in range(1, args.M, 2) for kind in ('F3', 'R3')])
    rows = []
    statistics = []
    for kind, residue in roots:
        found, stats = search(kind, args.M, residue, args.deep_children)
        rows.extend(found)
        statistics.append(stats)
    states = {(row['p'], row['r']) for row in rows}
    required = {('R3', r) for r in range(9, args.M, 18)}
    result = {'status': 'EXACT GAP-MULTISET CANDIDATES; complete dispatcher not asserted',
              'M': args.M, 'rows': rows, 'statistics': statistics,
              'summary': {'rows': len(rows), 'states_with_rule': len(states),
                          'required_with_rule': len(states & required),
                          'inverse_nodes': sum(x['inverse_nodes'] for x in statistics),
                          'max_inserted_gaps': max((len(row.get('child_gap_prefix', ())) for row in rows), default=0)},
              'closure': closure(rows, args.M), 'verification': verify_rows(rows)}
    Path(args.out).write_text(json.dumps(result, separators=(',', ':')) + '\n')
    print(json.dumps({key: (value if key != 'closure' else {k: v for k, v in value.items() if k not in ('active_states', 'missing_required')})
                      for key, value in result.items() if key not in ('rows', 'statistics')}, indent=2))


if __name__ == '__main__':
    main()
