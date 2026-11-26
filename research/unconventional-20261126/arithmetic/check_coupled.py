"""Exact paired-cycle identities, full physical words and small least-basin certificates."""
import json
from fractions import Fraction
from itertools import combinations
from math import comb, gcd


BLOCKS = {'A': ('10', '01'), 'B': ('010', '100'), 'C': ('110100000001', '000001110100')}


def require(value, message):
    if not value:
        raise ArithmeticError(message)


def carry(word):
    c = 0
    for j, e in enumerate(map(int, word)):
        c = (3 * c if e else c) + (e << j)
    return c


def shortcut(num, d):
    return (3 * num + d) // 2 if num % 2 else num // 2


def oddmap(num, d):
    val = 3 * num + d
    return val // (val & -val)


def cycle_states(value, word):
    d = value.denominator
    u = value.numerator
    odd = set()
    states = set()
    for e in map(int, word):
        require(u % 2 == e and u > 0 and u not in states, 'wrong physical cyclic word')
        states.add(u)
        if e:
            odd.add(u)
        u = shortcut(u, d)
    require(u == value.numerator, 'period did not close')
    return states, odd


def paired(pattern):
    w, v = [''.join(BLOCKS[c][side] for c in pattern + 'C') for side in range(2)]
    p = w.count('1')
    D = (1 << len(w)) - 3 ** p
    require(len(v) == len(w) and v.count('1') == p and D > 0, 'clock mismatch')
    X, Y = Fraction(carry(w), D), Fraction(carry(v), D)
    require(carry(v) == 3 * carry(w) - D and Y == 3 * X - 1, 'affine pairing')
    qa = (2 * X - 1) / 3
    qb = (64 * qa - 1) / 9
    d = qa.denominator
    require(d == X.denominator == Y.denominator == qb.denominator and gcd(d, 6) == 1, 'denominators')
    aa, a = cycle_states(X, w)
    bb, b = cycle_states(Y, v)
    require(not (aa & bb), 'full cycles intersect')
    ua, ub = qa.numerator, qb.numerator
    require(min(a) == ua and min(b) == ub, 'marked odd minima')
    require(shortcut(3 * ua, d) == Y.numerator and oddmap(3 * ub, d) == ua, 'reciprocal tripling')
    return d, ua, ub, a, b


def small_fate(pattern):
    d, ua, ub, a, b = paired(pattern)
    q = min(ua, ub)
    bad = b if q == ua else a
    memo = dict.fromkeys(bad, True)
    hits = []
    starts = edges = excluded = 0
    for source in range(1, 3 * q + 1, 2):
        if source > q and source % 3:
            continue
        starts += 1
        if gcd(source, d) > 1:
            excluded += 1
            continue
        u = source
        path = set()
        while u not in memo and u not in path:
            require(len(path) < 100000, 'unresolved fate')
            path.add(u)
            u = oddmap(u, d)
        # Repetition in the current path, without hitting a previously marked
        # vertex, gives a new deterministic cycle disjoint from the target.
        result = memo.get(u, False)
        memo.update(dict.fromkeys(path, result))
        edges += len(path)
        if result:
            hits.append(source)
    require(hits == [3 * q], 'smaller hit in designated positive basin')
    return {'pattern': pattern + 'C', 'reduced_denominator': d, 'q_numerator': q,
            'tripled_numerator': 3 * q, 'cycle_minimum_numerators': [ua, ub],
            'tested_odd_starts': starts, 'gcd_excluded': excluded, 'new_odd_edges': edges}


def shuffles(a, b):
    for indices in combinations(range(a + b), a):
        positions = set(indices)
        yield ''.join('A' if i in positions else 'B' for i in range(a + b))


def paired_examples():
    total = 0
    for a, b in ((1, 1), (2, 3), (4, 4), (5, 5)):
        input_minima, output_minima = set(), set()
        for s in shuffles(a, b):
            d, x, y, _, _ = paired(s)
            input_minima.add((x, d))
            output_minima.add((y, d))
            total += 1
        require(len(input_minima) == comb(a + b, a) == len(output_minima), 'duplicate cycle')
        require(not (input_minima & output_minima), 'cycle families overlap')
    return total


if __name__ == '__main__':
    small = [small_fate(p) for p in ('AB', 'AAB', 'ABB', 'AABB')]
    denominators = [5, 47, 13, 1909, 1631, 84997] + [c['reduced_denominator'] for c in small]
    count = 0
    for first, second in combinations(denominators, 2):
        require(gcd(first, second) == 1, 'common local obstruction')
        count += 1
    print(json.dumps({'shuffled_pair_checks': paired_examples(), 'all_depth_models': small,
                      'all_denominators': denominators, 'pairwise_coprimality_checks': count}, indent=2))
