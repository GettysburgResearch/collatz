"""Exact integer checks for the two source-shell and harmonic phase observables."""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
import json


def require(test, explanation):
    if not test:
        raise AssertionError(explanation)


@lru_cache(maxsize=None)
def trajectory(n, length):
    states = [n]
    grades = [0]
    prefix_min = [n]
    for _ in range(length):
        y = states[-1]
        odd = y % 2
        y = (3 * y + 1) // 2 if odd else y // 2
        states.append(y)
        grades.append(grades[-1] + odd)
        prefix_min.append(min(prefix_min[-1], y))
    return states, grades, prefix_min


def phase_event(source, state, clock):
    numerator = (1 << clock) * state
    base = source
    while 3 * base <= numerator:
        base *= 3
    require(base <= numerator < 3 * base, 'failed phase bracket')
    return numerator**4 <= 3 * base**4


def two_date_counts(starts, t, max_clock):
    counts = Counter()
    for n in starts:
        states, _, _ = trajectory(n, max_clock)
        counts[states[t]] += 1
        counts[states[t + 3]] += 1
    return counts


def shell_control():
    total_pairs = total_meetings = forced_small = monotone_checks = 0
    zero_dates = []
    nonzero_unsmoothed_at_zero = 0
    for scale in (20, 31, 64, 100, 159, 255):
        first = range(scale, 21 * scale // 20 + 1)
        second = range(5 * scale, 21 * scale // 4 + 1)
        require(first and second, 'empty test interval')
        max_clock = 225
        previous = Fraction(1)
        first_zero = None
        for t in range(max_clock - 2):
            left = two_date_counts(first, t, max_clock)
            right = two_date_counts(second, t, max_clock)
            common = left.keys() & right.keys()
            overlap = sum(min(left[y] * len(second), right[y] * len(first)) for y in common)
            tv = 1 - Fraction(overlap, 2 * len(first) * len(second))
            require(0 <= tv <= previous, 'the deterministic pushforward increased TV')
            previous = tv
            monotone_checks += 1
            if tv == 0 and first_zero is None:
                first_zero = t
                single_left = Counter(trajectory(n, max_clock)[0][t] for n in first)
                single_right = Counter(trajectory(n, max_clock)[0][t] for n in second)
                if any(single_left[y] * len(second) != single_right[y] * len(first)
                       for y in single_left.keys() | single_right.keys()):
                    nonzero_unsmoothed_at_zero += 1
            for n in first:
                states_x, odds_x, minima_x = trajectory(n, max_clock)
                for m in second:
                    states_y, odds_y, minima_y = trajectory(m, max_clock)
                    require(100 * n <= 21 * m and 4 * m <= 21 * n, 'incorrect cone')
                    for a, b in ((t, t), (t, t + 3), (t + 3, t), (t + 3, t + 3)):
                        total_pairs += 1
                        if states_x[a] != states_y[b]:
                            continue
                        total_meetings += 1
                        big_x = 3 * (1 << a) * states_x[a] >= 4 * 3**odds_x[a] * n
                        big_y = 3 * (1 << b) * states_y[b] >= 4 * 3**odds_y[b] * m
                        require(big_x or big_y, 'meeting without the exact 4/3 correction')
                        # A finite elementary floor independent of any large published certificate.
                        require((big_x and minima_x[a] <= 2 * a) or
                                (big_y and minima_y[b] <= 2 * b), 'missing clock-dependent floor')
                        forced_small += 1
        require(first_zero is not None, 'two-date measure failed to agree on the finite sample')
        zero_dates.append([scale, first_zero])
    return {'candidate_pairs': total_pairs, 'actual_meetings': total_meetings,
            'finite_floor_witnesses': forced_small, 'tv_monotonicity_checks': monotone_checks,
            'first_zero_at': zero_dates, 'nonzero_single_date_at_first_zero': nonzero_unsmoothed_at_zero}


def harmonic_control():
    phase_tests = protected_high = 0
    snapshots = []
    for scale in (16, 64, 256, 1024):
        sources = range(scale + 1, 3 * scale + 1)
        max_clock = 150
        harmonic_total = sum((Fraction(1, n) for n in sources), Fraction())
        for t in (0, 1, 11, 25, 50, 75, 100, 150):
            mass = Fraction()
            for n in sources:
                states, grades, minima = trajectory(n, max_clock)
                event = phase_event(n, states[t], t)
                # Independent phase extraction after stripping the full odd grade first.
                correction = Fraction((1 << t) * states[t], 3**grades[t] * n)
                while correction >= 3:
                    correction /= 3
                require(1 <= correction < 3 and event == (correction**4 <= 3),
                        'raw endpoint and counted reconstruction disagree')
                if minima[t] > 2 * t:
                    require(event, 'small correction left the quarter arc')
                    protected_high += 1
                if event:
                    mass += Fraction(1, n)
                phase_tests += 1
            # Return six decimal truncations using only exact integer operations.
            snapshots.append([scale, t, (10**6 * mass // harmonic_total)])
    return {'integer_phase_tests': phase_tests, 'protected_high_prefixes': protected_high,
            'harmonic_probabilities_floor_ppm': snapshots}


if __name__ == '__main__':
    print(json.dumps({'shell': shell_control(), 'harmonic': harmonic_control()}, sort_keys=True))
