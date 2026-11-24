"""Replay every smaller merger in the finite box stated in EVEN_INPUT_REFINEMENT.md."""

from collections import defaultdict
import json


SOURCE_LIMIT = 12_000
COMPETING_CLOCK_LIMIT = 40


def step(value):
    if value % 2:
        return (3 * value + 1) // 2
    return value // 2


def valuation(value, prime):
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def replay(start, clocks):
    value = start
    odd_inputs = 0
    for _ in range(clocks):
        odd_inputs += value % 2
        value = step(value)
    return value, odd_inputs


def run():
    earlier = defaultdict(list)
    eligible_sources = 0
    checked_mergers = 0
    for n in range(1, SOURCE_LIMIT + 1):
        e = valuation(n, 3)
        if e >= 1:
            eligible_sources += 1
            endpoint = n
            for b in range(valuation(n + 1, 2) + 1):
                for x, a, p in earlier.get(endpoint, ()):
                    if not 0 < x < n:
                        raise ValueError(f'Invalid smaller source {(n, x)}')
                    if replay(x, a) != (endpoint, p) or replay(n, b) != (endpoint, b):
                        raise ValueError(f'Physical replay failed for {(n, x, a, b)}')
                    if p <= b + e or a < p:
                        raise ValueError(f'Odd-input guard failed for {(n, x, a, b, p, e)}')
                    if 2 ** (a - p + e) <= 3 ** e:
                        raise ValueError(f'Even-input bound failed for {(n, x, a, b, p, e)}')
                    if 2 ** (a - b - 1) <= 3 ** e:
                        raise ValueError(f'Total-clock bound failed for {(n, x, a, b, p, e)}')
                    checked_mergers += 1
                endpoint = step(endpoint)

        # Inserting only after inspection makes the endpoint index contain all x < n.
        value, p = n, 0
        for a in range(COMPETING_CLOCK_LIMIT + 1):
            earlier[value].append((n, a, p))
            p += value % 2
            value = step(value)

    if eligible_sources != 4_000 or checked_mergers != 577:
        raise ValueError(f'Unexpected coverage totals {(eligible_sources, checked_mergers)}')
    return {
        'source_limit': SOURCE_LIMIT,
        'competing_clock_limit': COMPETING_CLOCK_LIMIT,
        'source_clock_range': '0 <= b <= v2(n + 1)',
        'eligible_sources_with_v3_positive': eligible_sources,
        'exact_smaller_mergers_replayed': checked_mergers,
        'odd_input_guard': 'p > b + e',
        'even_input_bound': '2 ** (a - p + e) > 3 ** e',
        'total_clock_bound': '2 ** (a - b - 1) > 3 ** e',
        'result': 'PASS',
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
