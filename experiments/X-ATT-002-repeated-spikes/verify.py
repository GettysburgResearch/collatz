#!/usr/bin/env python3
"""Separate exact replay: full component enumeration, literal paths, reverse graph labels.

No author generator, parent checker, or repository module is imported. Source
truncation is not time truncation. Every unknown residual is retained explicitly.
"""
from __future__ import annotations
import argparse
from collections import deque
from copy import deepcopy
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path

PARENT = '3c7fa4a0a2c5c48792c8efd5f5e90e94e44dab0f'
SCHEMA = 'X-ATT-002/repeated-spikes/v1'
SCOPE = ('complete finite rank balls and physical clearance forests; analytic omitted-input bound '
         'uniform over all subsequent returns; positive residual, not Collatz closure')
POWERS = (8, 12, 16, 20, 24, 28, 32)
CLEAR_POWERS = (24, 28, 32)
TIMES = (0, 1, 2, 4, 8, 16, 24, 32, 40, 48, 52, 64, 128, 1024)
SCALE = 1 << 128
PATH_CAP = 1024
GLOBAL_NODE_CAP = 2_000_000


def insist(test, label):
    if not test:
        raise RuntimeError(label)


def encoded(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'))


def sha(x):
    return sha256(encoded(x).encode('utf-8')).hexdigest()


def transcript(rows):
    checksum = sha256()
    for row in rows:
        checksum.update((encoded(row)+'\n').encode('utf-8'))
    return checksum.hexdigest()


def pair(x):
    q = Q(x)
    return [q.numerator, q.denominator]


def valuation(v, p):
    v = abs(v)
    insist(v != 0, 'zero valuation')
    count = 0
    while True:
        divided, rem = divmod(v, p)
        if rem:
            return count
        count += 1
        v = divided


def physical(n):
    insist(n >= 1, 'nonpositive shortcut input')
    if n % 2 == 0:
        return n//2
    return (3*n+1)//2


@lru_cache(None)
def R(n):
    """No four-entry theorem used by this implementation.

For a>=2, z_a increases strictly; component ranks are at least abs(z_a).
The first z_a exceeding a known candidate therefore certifies termination.
"""
    insist(n >= 1, 'rank domain')
    if n == 1:
        return 0
    best = n*n//(3**valuation(n, 3))
    a, power3, power2 = 1, 3, 2
    while True:
        v = power3*(n+1)-power2*(2*n+1)
        if a >= 2 and v > best:
            return best
        candidate = v*v//(3**valuation(v, 3)) if v else 0
        best = min(best, candidate)
        a += 1
        power3 *= 3
        power2 *= 2


def mode(n):
    return 0 if n % 2 == 0 else valuation(n+1, 2)


@lru_cache(None)
def A(n):
    """Consume literal copies while the physical active mode is unchanged."""
    insist(n > 1, 'absorbed module input')
    a, x, ticks, peak = mode(n), n, 0, n
    bound = 3*(n+5).bit_length()
    while True:
        for expected in [1]*a+[0]:
            insist(x > 1 and x % 2 == expected, 'illegal or post-absorption parity')
            x = physical(x)
            peak = max(peak, x)
            ticks += 1
            insist(ticks <= bound, 'literal module exceeds proved clock ceiling')
        if x == 1 or mode(x) != a:
            return x, ticks, peak


def G(n):
    if n == 1:
        return False
    return 4*R(A(n)[0]) <= R(n)


@lru_cache(None)
def B(n):
    insist(n > 1 and not G(n), 'wrong unsafe domain')
    x, duration, peak = A(n)
    count = 0
    start_rank = R(x)
    while x != 1 and G(x):
        before = R(x)
        x, steps, top = A(x)
        duration += steps
        peak = max(peak, top)
        count += 1
        insist(4*R(x) <= before, 'unsafe replacement of a safe edge')
        insist(count <= start_rank.bit_length()+1, 'safe chain did not terminate')
    return x, duration, count, peak


def complete_ball(Y):
    """Enumerate ALL component sublevels, not just the possible minimizers.

For a>=2, z_a(n)>=z_a(2); once z_a(2)>Y that whole component is absent.
For each 3-adic depth enumerate the exact linear congruence for the unit u.
"""
    result = set()
    a = 0
    while True:
        d, c = 3**a-2**(a+1), 3**a-2**a
        if a >= 2 and 2*d+c > Y:
            break
        p = 1
        while p <= Y:
            maximum = isqrt(Y//p)
            if a < 2:
                for u in range(1, maximum+1):
                    if u % 3:
                        n = (-p*u-c)//d
                        if n >= 2:
                            result.add(n)
            else:
                minimum = max(1, (2*d+c+p-1)//p)
                residue = 0 if d == 1 else (c*pow(p, -1, d)) % d
                start = minimum + (residue-minimum) % d
                for u in range(start, maximum+1, d):
                    if u % 3:
                        numerator = p*u-c
                        insist(numerator % d == 0, 'component congruence')
                        n = numerator//d
                        insist(n >= 2, 'component positivity')
                        result.add(n)
            p *= 3
        a += 1
    answer = sorted(result)
    insist(all(R(n) <= Y for n in answer), 'extra rank-ball source')
    return answer


def classify_reverse(edges):
    """Reverse propagation from exits and 1; leftover finite components are cyclic."""
    back = {n: [] for n in edges}
    answer, todo = {}, deque()
    for n, endpoint in edges.items():
        if endpoint == 1:
            answer[n] = 'killed', 1
            todo.append(n)
        elif endpoint not in edges:
            answer[n] = 'exit', 1
            todo.append(n)
        else:
            back[endpoint].append(n)
    while todo:
        x = todo.popleft()
        kind, distance = answer[x]
        for n in back[x]:
            insist(n not in answer, 'multiple classification of one source')
            answer[n] = kind, distance+1
            todo.append(n)
    for n in edges:
        if n not in answer:
            answer[n] = 'cycle', None
    return answer


def weight_bounds(sources):
    lower = Q(sum(SCALE//R(n)**2 for n in sources), SCALE)
    return lower, lower+Q(len(sources), SCALE)


def first_exit(power, ball):
    Y = 1 << power
    roots = [n for n in ball if not G(n)]
    edges = {n: B(n)[0] for n in roots}
    classes = classify_reverse(edges)
    exits = [n for n in roots if classes[n][0] == 'exit']
    cycles = [n for n in roots if classes[n][0] == 'cycle']
    killed = [n for n in roots if classes[n][0] == 'killed']
    low, high = weight_bounds(exits)
    _, cycle_high = weight_bounds(cycles)
    remainder = Q(12, Y*isqrt(Y))
    duration = max((classes[n][1] or 0 for n in roots), default=0)
    insist(duration <= len(roots), 'finite exit clock')
    return {
        'rank_cut': Y, 'ball_sources': len(ball), 'unsafe_sources': len(roots),
        'largest_source': max(ball), 'ball_sha256': transcript([n, R(n)] for n in ball),
        'killed_before_exit': len(killed), 'exit_sources': len(exits),
        'cycle_sources': len(cycles), 'maximum_finite_exit_or_kill_clock': duration,
        'first_exit_mass_interval': [pair(low), pair(high+remainder)],
        'all_future_survivor_upper_after_ball_size_returns': pair(high+cycle_high+remainder),
        'omitted_input_upper': pair(remainder), 'smallest_exiting_source': min(exits, default=None),
        'first_exit_transcript_sha256': transcript([n, R(n), edges[n], *classes[n]] for n in roots),
    }


def full_forest(roots):
    """Expand the reachable graph, then certify it by a reverse topological pass."""
    graph, todo, queued = {}, deque(roots), set(roots)
    while todo:
        n = todo.popleft()
        insist(n.bit_length() < 10000, 'unresolved arithmetic cap')
        edge = B(n)
        graph[n] = edge
        endpoint = edge[0]
        if endpoint != 1 and endpoint not in queued:
            insist(len(queued) < GLOBAL_NODE_CAP, 'unresolved global node cap')
            queued.add(endpoint)
            todo.append(endpoint)
    reverse = {1: []}
    for n, edge in graph.items():
        reverse.setdefault(edge[0], []).append(n)
    labels, ready = {1: (0, 0, 1)}, deque([1])
    while ready:
        endpoint = ready.popleft()
        J, clock, peak = labels[endpoint]
        for n in reverse.get(endpoint, []):
            insist(n not in labels, 'cycle in a supposedly clear forest')
            _, duration, g, local_top = graph[n]
            labels[n] = J+1, clock+duration, max(peak, local_top)
            ready.append(n)
    insist(len(labels) == len(graph)+1, 'unresolved component not connected to 1')
    insist(all(labels[n][0] <= PATH_CAP for n in roots), 'root exceeds clearance protocol cap')
    return graph, labels


def clearance(power, ball):
    Y = 1 << power
    roots = [n for n in ball if not G(n)]
    graph, labels = full_forest(roots)
    J = max(labels[n][0] for n in roots)
    clock = max(labels[n][1] for n in roots)
    peak = max(labels[n][2] for n in roots)
    remainder = Q(12, Y*isqrt(Y))
    mass_rows = []
    for j in TIMES:
        alive = [n for n in roots if labels[n][0] > j]
        lo, hi = weight_bounds(alive)
        mass_rows.append([j, len(alive), pair(lo), pair(hi+remainder)])
    insist(R(3) == 3 and not G(3), 'normalizing source 3')
    return {
        'rank_cut': Y, 'unsafe_roots': len(roots), 'forest_unsafe_nodes': len(graph),
        'forest_nodes_outside_rank_ball': sum(R(n) > Y for n in graph),
        'maximum_unsafe_returns': J, 'maximum_shortcut_hitting_time': clock,
        'maximum_physical_value': peak,
        'first_source_attaining_return_maximum': next(n for n in roots if labels[n][0] == J),
        'first_source_attaining_physical_peak': next(n for n in roots if labels[n][2] == peak),
        'all_future_survivor_upper': pair(remainder), 'normalized_survivor_upper': pair(9*remainder),
        'late_forest_occupation_upper': pair(J*remainder),
        'total_new_forest_entry_upper': pair(remainder),
        'all_time_ever_spike_rank_cut': peak*peak,
        'all_time_ever_spike_mass_upper': pair(remainder),
        'all_future_clause': 'EVERY j >= maximum_unsafe_returns; no cap on subsequent returns',
        'residual_clause': 'unknown input outside this rank ball is charged once, not discarded',
        'survivor_rows': mass_rows,
        'forest_sha256': transcript([n, R(n), *graph[n], *labels[n]] for n in sorted(graph)),
        'root_clock_sha256': transcript([n, *labels[n]] for n in roots),
    }


def controls():
    graph = {2: 3, 3: 2, 4: 5, 5: 8, 6: 1, 7: 6}
    result = classify_reverse(graph)
    insist(result[2][0] == result[3][0] == 'cycle', 'finite cycle lost')
    insist(result[4] == ('exit', 2) and result[7] == ('killed', 2), 'terminal paths')
    masses = [Q(1, 3), Q(1, 7), Q(1, 11)]
    once, visited = sum(masses), sum((20-i)*v for i, v in enumerate(masses))
    insist(visited > once, 'repeated visits must not equal once-only source mass')
    # Count the individual source histories rather than evolve the ensemble.
    edges = {2: 3, 3: 1, 4: 2, 5: 4, 6: 6}
    source_weights = {2: Q(5), 3: Q(7), 4: Q(1, 11), 5: Q(1, 13), 6: Q(1, 17)}
    late = Q(0); entry = Q(0)
    for root, weight in source_weights.items():
        x = root; entered = False
        for j in range(13):
            if x == 1:
                break
            if j >= 2 and x in {2, 3}:
                late += weight
            y = edges[x]
            if x not in {2, 3} and y in {2, 3}:
                insist(not entered, 'source entered a forward-closed forest twice')
                entered = True
                entry += weight
            x = y
    residual = Q(1, 11)+Q(1, 13)+Q(1, 17)
    insist(late == Q(35, 143) and entry == Q(24, 143), 'literal forest inflow/occupation')
    insist(late <= 2*residual, 'nilpotent occupation budget')
    return {'finite_classes': [[n, *result[n]] for n in sorted(result)],
            'transient_forest_late_occupation': pair(late),
            'transient_forest_total_inflow': pair(entry),
            'transient_forest_residual_input': pair(residual),
            'outside_cycle_persistent_mass': [1, 17],
            'once_only_mass': pair(once), 'twenty_clock_visit_sum': pair(visited),
            'scope': 'separate deterministic test graphs, not Collatz counterexamples'}


def egcd(a, b):
    x0, x1 = 1, 0
    while b:
        q, a, b = a//b, b, a % b
        x0, x1 = x1, x0-q*x1
    return a, x0


def binary_cylinder(bits):
    # Lift one parity bit at a time, keeping the exact current endpoint.
    root, x, q = 0, 0, 0
    for i, bit in enumerate(bits):
        if x % 2 != int(bit):
            root += 1 << i
            x += 3**q
        insist(x % 2 == int(bit), 'binary lift parity')
        if x % 2:
            x = (3*x+1)//2
            q += 1
        else:
            x //= 2
    return root


def shadows():
    rows = []
    for J in (1, 2, 4, 8, 16, 32, 52, 64, 128):
        K = (J+1)//2+1
        word = '111010'*(K+1)
        D = 1 << len(word)
        r = binary_cylinder(word)
        gcd, inverse = egcd(D, 243)
        insist(gcd == 1, 'CRT moduli not coprime')
        n = r+D*((10-r)*inverse % 243)
        insist(n >= 11 and n % 243 == 10, 'shadow ordinary CRT source')
        x, clock, trace = n, 0, []
        for _ in range(J):
            y, length, safe_count, peak = B(x)
            insist(safe_count == 0 and y != 1 and not G(y), 'unsafe shadow guard')
            trace.append([x, y, R(x), R(y), length])
            x, clock = y, clock+length
        rows.append({'returns': J, 'cycles_budget': K+1, 'source': n, 'endpoint': x,
                     'shortcut_clock': clock, 'input_mass': [1, 1], 'output_mass': [1, 1],
                     'transcript_sha256': transcript(trace)})
    return rows


def reconstruct():
    exits, cleared = [], []
    for p in POWERS:
        ball = complete_ball(1 << p)
        if p <= 12:
            insist(ball == [n for n in range(2, (1 << p)+2) if R(n) <= (1 << p)],
                    'complete low-rank ball versus ordinary exhaustive range')
        exits.append(first_exit(p, ball))
        if p in CLEAR_POWERS:
            cleared.append(clearance(p, ball))
    return {'schema': SCHEMA, 'scope': SCOPE, 'parent': PARENT, 'weight': '1_U/R_*^2',
            'safe_set': '4 R_*(A(n)) <= R_*(n); killed at 1',
            'rounding_denominator': SCALE, 'clearance_path_cap': PATH_CAP,
            'first_exit': exits, 'clearance': cleared, 'unsafe_shadows': shadows(),
            'controls': controls(), 'full_closure': False,
            'unproved': 'a cofinal sequence of successful finite clearance certificates'}


def validate(report, expected):
    insist(isinstance(report, dict) and set(report) == {'payload', 'sha256'}, 'report fields')
    insist(report['sha256'] == sha(report['payload']), 'digest does not match payload')
    insist(encoded(report) == encoded(expected), 'full independently reconstructed payload differs')


def self_test(expected):
    changed = []
    def alter(action):
        value = deepcopy(expected)
        action(value['payload'])
        value['sha256'] = sha(value['payload'])
        insist(encoded(value) != encoded(expected), 'no-op corruption')
        changed.append(value)
    alter(lambda p: p.__setitem__('full_closure', True))
    alter(lambda p: p.__setitem__('safe_set', 'R_*(A(n)) <= R_*(n)'))
    alter(lambda p: p['first_exit'].pop())
    alter(lambda p: p['clearance'][-1].__setitem__('unsafe_roots', 78827))
    alter(lambda p: p['clearance'][-1].__setitem__('maximum_unsafe_returns', 51))
    alter(lambda p: p['clearance'][-1].__setitem__('maximum_shortcut_hitting_time', 260))
    alter(lambda p: p['clearance'][-1].__setitem__('all_future_survivor_upper', [0, 1]))
    alter(lambda p: p['clearance'][-1].__setitem__('forest_nodes_outside_rank_ball', 0))
    alter(lambda p: p['unsafe_shadows'][-1].__setitem__('endpoint', 1))
    alter(lambda p: p['controls'].__setitem__('once_only_mass', p['controls']['twenty_clock_visit_sum']))
    alter(lambda p: p['clearance'][-1]['survivor_rows'].pop())
    alter(lambda p: p.__setitem__('unproved', 'nothing remains'))
    rejected = 0
    for value in changed:
        try:
            validate(value, expected)
        except RuntimeError:
            rejected += 1
        else:
            raise RuntimeError('resealed corrupted report accepted')
    insist(rejected == 12, 'tamper coverage')
    print('SELF-TEST PASS: 12 distinct resealed corruptions rejected')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    payload = reconstruct()
    expected = {'payload': payload, 'sha256': sha(payload)}
    validate(json.loads(args.report.read_text(encoding='utf-8')), expected)
    if args.self_test:
        self_test(expected)
    print(expected['sha256'])
    print('INDEPENDENT IMPLEMENTATION PASS; fixed finite certificate, all-future nonzero residual')


if __name__ == '__main__':
    main()
