#!/usr/bin/env python3
"""Exact source-tagged first-exit and clearance certificates; no cofinal claim."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
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


def need(test, message):
    if not test:
        raise ValueError(message)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))


def digest(obj):
    return sha256(canonical(obj).encode()).hexdigest()


def rows_digest(rows):
    h = sha256()
    for row in rows:
        h.update((canonical(row) + '\n').encode())
    return h.hexdigest()


def rat(x):
    x = Fraction(x)
    return [x.numerator, x.denominator]


def vp(n, p):
    n = abs(n)
    need(n > 0, 'undefined valuation at zero')
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def step(n):
    return (3*n+1)//2 if n & 1 else n//2


def z(n, a):
    return 3**a*(n+1) - 2**a*(2*n+1)


def component(n, a):
    v = z(n, a)
    return v*v//3**vp(v, 3) if v else 0


@lru_cache(None)
def rank(n):
    need(n >= 1, 'rank requires a positive ordinary integer')
    h = vp(2*n+1, 3)
    return min(component(n, a) for a in ({0, 1, 2, h} if h >= 3 else {0, 1, 2}))


@lru_cache(None)
def module(n):
    need(n > 1, 'absorbed state cannot start a module')
    a = vp(n+1, 2) if n & 1 else 0
    v = z(n, a)
    k = vp(v, 2)//(a+1)
    need(k >= 1, 'empty module')
    d, c = 3**a-2**(a+1), 3**a-2**a
    numerator = 3**(a*k)*(v//2**((a+1)*k)) - c
    need(numerator % d == 0, 'nonintegral module endpoint')
    y = numerator//d
    need(y >= 1, 'nonpositive module endpoint')
    peak = 2*y if a >= 2 else ((3*n+1)//2 if a == 1 else n)
    need((y+5)**4 <= (n+5)**9, 'parent height bound')
    return y, (a+1)*k, peak


def safe(n):
    return n > 1 and 4*rank(module(n)[0]) <= rank(n)


@lru_cache(None)
def b_edge(n):
    need(n > 1 and not safe(n), 'source outside quarter-unsafe set')
    x, clock, peak = module(n)
    safe_steps = 0
    r0 = rank(x)
    while safe(x):
        old = rank(x)
        x, length, local_peak = module(x)
        clock += length
        peak = max(peak, local_peak)
        safe_steps += 1
        need(4*rank(x) <= old, 'lost safe rank guard')
        need(safe_steps <= r0.bit_length()+1, 'safe-return bound exceeded')
    return x, clock, safe_steps, peak


def rank_ball(Y):
    """Generate candidates by complete fibers of the minimum rank."""
    answer = set()
    p, e = 1, 0
    while p <= Y:
        for u in range(1, isqrt(Y//p)+1):
            if u % 3 == 0:
                continue
            Z, value = p*u, p*u*u
            candidates = [Z, Z+1, Z-5]
            for a in range(3, e+1):
                d, c = 3**a-2**(a+1), 3**a-2**a
                if (Z-c) % d == 0:
                    candidates.append((Z-c)//d)
            for n in candidates:
                if n >= 2 and rank(n) == value:
                    answer.add(n)
        p *= 3
        e += 1
    return sorted(answer)


def terminal_classes(edges):
    """Source -> (first terminal type, steps); cycles get no fictitious exit time."""
    result = {}
    for root in sorted(edges):
        if root in result:
            continue
        trail, position, x = [], {}, root
        while x in edges and x not in result and x not in position:
            position[x] = len(trail)
            trail.append(x)
            x = edges[x]
        if x == 1:
            kind, distance = 'killed', 0
        elif x not in edges:
            kind, distance = 'exit', 0
        elif x in result:
            kind, distance = result[x]
        else:
            kind, distance = 'cycle', None
        for v in reversed(trail):
            if distance is not None:
                distance += 1
            result[v] = kind, distance
    return result


def interval_sources(sources):
    lo = sum(SCALE//rank(n)**2 for n in sources)
    return Fraction(lo, SCALE), Fraction(lo+len(sources), SCALE)


def exit_report(power, ball):
    Y = 1 << power
    roots = [n for n in ball if not safe(n)]
    edges = {n: b_edge(n)[0] for n in roots}
    result = terminal_classes(edges)
    counts = Counter(v[0] for v in result.values())
    exiting = [n for n in roots if result[n][0] == 'exit']
    cycles = [n for n in roots if result[n][0] == 'cycle']
    lo, hi = interval_sources(exiting)
    _, chi = interval_sources(cycles)
    tail = Fraction(12, Y*isqrt(Y))
    terminal_clock = max((v[1] or 0 for v in result.values()), default=0)
    need(terminal_clock <= len(roots), 'finite-graph first exit exceeded dimension')
    transcript = ([n, rank(n), edges[n], *result[n]] for n in roots)
    return {
        'rank_cut': Y, 'ball_sources': len(ball), 'unsafe_sources': len(roots),
        'largest_source': max(ball), 'ball_sha256': rows_digest([n, rank(n)] for n in ball),
        'killed_before_exit': counts['killed'], 'exit_sources': counts['exit'],
        'cycle_sources': counts['cycle'], 'maximum_finite_exit_or_kill_clock': terminal_clock,
        'first_exit_mass_interval': [rat(lo), rat(hi+tail)],
        'all_future_survivor_upper_after_ball_size_returns': rat(hi+chi+tail),
        'omitted_input_upper': rat(tail),
        'smallest_exiting_source': min(exiting, default=None),
        'first_exit_transcript_sha256': rows_digest(transcript),
    }


def clear_forest(roots):
    """A bounded attempt. Any unclosed path is an error, never an accepted proof."""
    labels = {1: (0, 0, 1)}
    graph = {}
    for root in roots:
        x, trail, seen = root, [], set()
        while x not in labels:
            need(x not in seen, 'unresolved cycle in clearance forest')
            need(len(trail) < PATH_CAP, 'UNRESOLVED at declared path cap')
            need(x.bit_length() < 10000, 'UNRESOLVED at arithmetic resource cap')
            seen.add(x)
            edge = b_edge(x)
            graph[x] = edge
            trail.append(x)
            x = edge[0]
        J, clock, peak = labels[x]
        for v in reversed(trail):
            endpoint, length, g, local_peak = graph[v]
            J, clock, peak = J+1, clock+length, max(peak, local_peak)
            labels[v] = J, clock, peak
    return graph, labels


def clearance_report(power, ball):
    Y = 1 << power
    roots = [n for n in ball if not safe(n)]
    graph, labels = clear_forest(roots)
    J = max(labels[n][0] for n in roots)
    clock = max(labels[n][1] for n in roots)
    peak = max(labels[n][2] for n in roots)
    tail = Fraction(12, Y*isqrt(Y))
    weights = {n: SCALE//rank(n)**2 for n in roots}
    mass_rows = []
    for j in TIMES:
        alive = [n for n in roots if labels[n][0] > j]
        lo = Fraction(sum(weights[n] for n in alive), SCALE)
        hi = lo + Fraction(len(alive), SCALE) + tail
        mass_rows.append([j, len(alive), rat(lo), rat(hi)])
    records = ([n, rank(n), *graph[n], *labels[n]] for n in sorted(graph))
    need(rank(3) == 3 and not safe(3), 'normalizing atom 3')
    return {
        'rank_cut': Y, 'unsafe_roots': len(roots), 'forest_unsafe_nodes': len(graph),
        'forest_nodes_outside_rank_ball': sum(rank(n) > Y for n in graph),
        'maximum_unsafe_returns': J, 'maximum_shortcut_hitting_time': clock,
        'maximum_physical_value': peak,
        'first_source_attaining_return_maximum': next(n for n in roots if labels[n][0] == J),
        'first_source_attaining_physical_peak': next(n for n in roots if labels[n][2] == peak),
        'all_future_survivor_upper': rat(tail), 'normalized_survivor_upper': rat(9*tail),
        'late_forest_occupation_upper': rat(J*tail),
        'total_new_forest_entry_upper': rat(tail),
        'all_time_ever_spike_rank_cut': peak*peak,
        'all_time_ever_spike_mass_upper': rat(tail),
        'all_future_clause': 'EVERY j >= maximum_unsafe_returns; no cap on subsequent returns',
        'residual_clause': 'unknown input outside this rank ball is charged once, not discarded',
        'survivor_rows': mass_rows,
        'forest_sha256': rows_digest(records),
        'root_clock_sha256': rows_digest([n, *labels[n]] for n in roots),
    }


def finite_controls():
    # A finite core with a cycle: (I-K)^-1 is unavailable, but first exits remain exact.
    edges = {2: 3, 3: 2, 4: 5, 5: 8, 6: 1, 7: 6}
    classes = terminal_classes(edges)
    need(classes[2][0] == 'cycle' and classes[4] == ('exit', 2), 'cycle/exit control')
    need(classes[7] == ('killed', 2), 'absorption control')
    # Distinct sources merge; source mass, not endpoint count, must be preserved.
    masses = {2: Fraction(1, 3), 3: Fraction(1, 7), 4: Fraction(1, 11)}
    first_hits = {2: 1, 3: 2, 4: 3}
    ever = sum(masses.values())
    repeated_visits = sum((20-first_hits[n]+1)*mass for n, mass in masses.items())
    need(repeated_visits > ever, 'visit multiplicity control')
    # A forward-closed transient forest, with both delayed inflow and an outside cycle.
    Fset = {2, 3}
    graph = {2: 3, 3: 1, 4: 2, 5: 4, 6: 6}
    initial = {2: Fraction(5), 3: Fraction(7), 4: Fraction(1, 11),
               5: Fraction(1, 13), 6: Fraction(1, 17)}
    mass = initial.copy(); late = Fraction(0); inflow = Fraction(0)
    for j in range(13):
        if j >= 2:
            late += sum(v for x, v in mass.items() if x in Fset)
        following = {}
        for x, v in mass.items():
            y = graph[x]
            if x not in Fset and y in Fset:
                inflow += v
            if y != 1:
                following[y] = following.get(y, Fraction(0))+v
        mass = following
    residual = sum(initial[x] for x in (4, 5, 6))
    need(late == Fraction(1, 11)+Fraction(2, 13) and late <= 2*residual, 'late occupation')
    need(inflow == Fraction(1, 11)+Fraction(1, 13), 'single source entry')
    return {'finite_classes': [[n, *classes[n]] for n in sorted(classes)],
            'transient_forest_late_occupation': rat(late),
            'transient_forest_total_inflow': rat(inflow),
            'transient_forest_residual_input': rat(residual),
            'outside_cycle_persistent_mass': [1, 17],
            'once_only_mass': rat(ever), 'twenty_clock_visit_sum': rat(repeated_visits),
            'scope': 'separate deterministic test graphs, not Collatz counterexamples'}


def unsafe_shadows():
    rows = []
    for J in (1, 2, 4, 8, 16, 32, 52, 64, 128):
        K = (J+1)//2 + 1
        D = 1 << (6*(K+1))
        residue = (-73*pow(17, -1, D)) % D
        n = residue + D*((10-residue)*pow(D, -1, 243) % 243)
        need(n >= 11 and n % 243 == 10, 'unsafe-shadow CRT')
        x, clock = n, 0
        trace = []
        for j in range(J):
            need(not safe(x), 'shadow has a safe source')
            y, length, g, peak = b_edge(x)
            need(y != 1 and g == 0, 'shadow entered safe region or core')
            trace.append([x, y, rank(x), rank(y), length])
            clock += length
            x = y
        rows.append({'returns': J, 'cycles_budget': K+1, 'source': n, 'endpoint': x,
                     'shortcut_clock': clock, 'input_mass': [1, 1], 'output_mass': [1, 1],
                     'transcript_sha256': rows_digest(trace)})
    return rows


def build():
    first, cleared = [], []
    for power in POWERS:
        ball = rank_ball(1 << power)
        # Independent low-radius source exhaustion within this generator is only a regression.
        if power <= 12:
            need(ball == [n for n in range(2, (1 << power)+2) if rank(n) <= 1 << power],
                 'small rank-ball exhaustive comparison')
        first.append(exit_report(power, ball))
        if power in CLEAR_POWERS:
            cleared.append(clearance_report(power, ball))
    return {'schema': SCHEMA, 'scope': SCOPE, 'parent': PARENT, 'weight': '1_U/R_*^2',
            'safe_set': '4 R_*(A(n)) <= R_*(n); killed at 1',
            'rounding_denominator': SCALE, 'clearance_path_cap': PATH_CAP,
            'first_exit': first, 'clearance': cleared, 'unsafe_shadows': unsafe_shadows(),
            'controls': finite_controls(), 'full_closure': False,
            'unproved': 'a cofinal sequence of successful finite clearance certificates'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--check', type=Path)
    args = parser.parse_args()
    payload = build()
    report = {'payload': payload, 'sha256': digest(payload)}
    if args.check:
        need(json.loads(args.check.read_text(encoding='utf-8')) == report, 'canonical mismatch')
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(canonical(report)+'\n', encoding='utf-8')
    print(report['sha256'])
    print('GENERATOR PASS: finite physical forests + all-future positive residual; no full closure')


if __name__ == '__main__':
    main()
