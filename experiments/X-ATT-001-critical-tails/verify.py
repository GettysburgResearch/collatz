#!/usr/bin/env python3
"""Independent finite replay of X-ATT-001. No generator/source-module imports.

The rank is evaluated by a provably terminating component scan; maximal modules
are traversed physically; raw pushforwards are aggregated endpoint-first.
This is implementation independence, not independent mathematical review.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path

BASE = '69b1ed57ce90fe8c9d6d7c80c69760a86eb0fd2a'
SCHEMA = 'X-ATT-001/v1'
SCOPE = 'finite arithmetic regressions and certified omitted-source mass; no all-time tightness or Collatz proof'
LIMIT = 4096
UNIT = 1 << 80
TIMES = (0, 1, 2, 4, 8, 16, 32, 64, 128)
CUTS = (1, 16, 256, 4096, 65536, 16777216)


def require(ok, why):
    if not ok:
        raise ValueError(why)


def seal(payload):
    return sha256(json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def encode(value):
    return [value.numerator, value.denominator]


def valuation(value, prime):
    require(value != 0, 'zero has no finite valuation')
    value = abs(value)
    power = 1
    exponent = 0
    while value % (power * prime) == 0:
        power *= prime
        exponent += 1
    return exponent


def T(value):
    return (value >> 1) if value % 2 == 0 else (3 * value + 1) // 2


@lru_cache(None)
def R(value):
    require(value >= 1, 'nonpositive rank argument')
    if value == 1:
        return 0
    best = value * value
    a, power3, power2 = 0, 1, 1
    while True:
        form = (power3 - 2 * power2) * value + power3 - power2
        # For a>=2 the forms are positive and strictly increasing. All later
        # components are >= their absolute form, hence cannot beat this best.
        if a >= 2 and form > best:
            return best
        require(form != 0, 'unexpected positive zero')
        trial = form * form // (3 ** valuation(form, 3))
        best = min(best, trial)
        a += 1
        power3 *= 3
        power2 *= 2


def mode(value):
    return valuation(value + 1, 2) if value & 1 else 0


@lru_cache(None)
def A(value):
    if value == 1:
        return (1, -1, 0, 0)
    a = mode(value)
    current, copies, clock = value, 0, 0
    while current != 1 and mode(current) == a:
        for _ in range(a):
            require(current % 2 == 1, 'odd portion is not physical')
            current = T(current)
            clock += 1
        require(current % 2 == 0, 'terminal zero is not physical')
        current = T(current)
        clock += 1
        copies += 1
    require(copies >= 1 and clock == copies * (a + 1), 'empty or malformed module')
    require((current + 5) ** 4 <= (value + 5) ** 9, 'height bound')
    return current, a, copies, clock


def in_G(value):
    return value != 1 and 4 * R(A(value)[0]) <= R(value)


@lru_cache(None)
def B(value):
    require(value >= 2 and not in_G(value), 'unsafe source required')
    current, _, _, time = A(value)
    entered_rank = R(current)
    safe_count = 0
    while current != 1 and in_G(current):
        previous = R(current)
        current, _, _, extra = A(current)
        time += extra
        safe_count += 1
        require(4 * R(current) <= previous, 'invalid safe edge')
    require(R(current) <= entered_rank, 'unsafe return endpoint exceeds entry rank')
    return current, safe_count, time


def enclose(floors, contributors):
    return [encode(Q(floors, UNIT)),
            encode(Q(floors + contributors, UNIT) + Q(43, LIMIT * LIMIT))]


def source_tails(weights):
    suffix = [0] * (LIMIT + 2)
    for n in range(LIMIT, 1, -1):
        suffix[n] = suffix[n + 1] + weights[n]
    rows = []
    for cutoff in (2, 8, 32, 128, 512, 1024):
        enclosure = enclose(suffix[cutoff + 1], LIMIT - cutoff)
        power = 1
        while power <= cutoff:
            power *= 3
        require(R(power) == power, 'power-of-three source rank')
        require(Q(*enclosure[1]) <= Q(43, cutoff * cutoff), 'ordinary upper bound')
        rows.append({'cut': cutoff, 'enclosure': enclosure, 'lower_source': power,
                     'lower_weight': encode(Q(1, power * power))})
    return rows


def height_census():
    transcript, modes = [], defaultdict(int)
    unsafe_count = longest_safe = longest_clock = 0
    for n in range(2, LIMIT + 1):
        rank = R(n)
        endpoint, a, copies, clock = A(n)
        require(n - 1 <= rank <= n * n, 'proper rank bound')
        modes[a] += 1
        if in_G(n):
            target = safe_count = duration = None
        else:
            unsafe_count += 1
            target, safe_count, duration = B(n)
            longest_safe = max(longest_safe, safe_count)
            longest_clock = max(longest_clock, duration)
        transcript.append([n, rank, endpoint, a, copies, clock, R(endpoint), target, safe_count, duration])
    return {'sources': LIMIT - 1, 'unsafe_sources': unsafe_count, 'active_modes': dict(modes),
            'maximum_safe_modules_in_return': longest_safe,
            'maximum_observed_shortcut_clock': longest_clock,
            'transcript_sha256': seal(transcript)}


def transported_tails(weights):
    # Keep the contributors at each endpoint. Summed fixed-point floors are
    # per original source, so merging does not change the rounding contract.
    live = {n: n for n in range(2, LIMIT + 1)}
    transcript, rows = [], []
    for time in range(TIMES[-1] + 1):
        if time in TIMES:
            endpoints = defaultdict(lambda: [0, 0])
            for source, endpoint in live.items():
                endpoints[endpoint][0] += weights[source]
                endpoints[endpoint][1] += 1
                transcript.append([source, time, endpoint, R(endpoint)])
            for cutoff in CUTS:
                selected = [data for endpoint, data in endpoints.items() if R(endpoint) > cutoff]
                floors = sum(data[0] for data in selected)
                count = sum(data[1] for data in selected)
                enclosure = enclose(floors, count)
                require(Q(*enclosure[1]) <= 77 * Q(9, 4) ** time / cutoff, 'raw transport bound')
                rows.append({'clock': time, 'rank_cut': cutoff, 'enumerated_sources': count,
                             'enclosure': enclosure})
        live = {source: T(endpoint) for source, endpoint in live.items() if T(endpoint) != 1}
    transcript.sort(key=lambda row: (row[0], row[1]))
    return {'rows': rows, 'transcript_sha256': seal(transcript)}


def unsafe_tails(weights):
    endpoints = defaultdict(lambda: [0, 0])
    transcript = []
    for source in range(2, LIMIT + 1):
        if in_G(source):
            continue
        target, count, duration = B(source)
        if target == 1:
            continue
        transcript.append([source, target, count, duration, R(target)])
        endpoints[target][0] += weights[source]
        endpoints[target][1] += 1
    rows = []
    for cutoff in CUTS:
        values = [data for target, data in endpoints.items() if R(target) > cutoff]
        floors = sum(data[0] for data in values)
        count = sum(data[1] for data in values)
        enclosure = enclose(floors, count)
        require(Q(*enclosure[1]) ** 9 * cutoff ** 4 <= 200 ** 9, 'fractional return bound')
        rows.append({'rank_cut': cutoff, 'enumerated_sources': count, 'enclosure': enclosure})
    return {'rows': rows, 'transcript_sha256': seal(transcript)}


def power_sources():
    rows = []
    for clock in (1, 2, 3, 4, 8, 12, 16):
        for extra in (0, 1, 3, 8):
            exponent = 2 * clock + 2 + extra
            source = 3 ** exponent
            value, bits = source, []
            for _ in range(clock):
                require(value > 1, 'premature killing')
                bits.append(value % 2)
                value = T(value)
            q = sum(bits)
            remainder = (2 ** clock) * value - (3 ** q) * source
            require(remainder > 0 and remainder % 2 == 1, 'odd affine remainder')
            require(R(source) == source and R(value) * 36 ** (clock + 1) >= source * source,
                    'fixed-clock rank lower bound')
            rows.append({'clock': clock, 'e': exponent, 'source': source, 'endpoint': value,
                         'word': ''.join(map(str, bits)), 'q': q, 'A': remainder,
                         'endpoint_h': valuation(2 * value + 1, 3), 'endpoint_rank': R(value)})
    return rows


def clock_family():
    rows = []
    for j in (2, 4, 6, 8):
        t = 1 << j
        M = 3 ** t
        n, a = 4 * M - 5, j + 4
        endpoint, active, copies, length = A(n)
        require((active, copies, length) == (a, 1, a + 1), 'maximal spike word')
        value = n
        for _ in range(a):
            require(value % 2 == 1, 'not all-odd prefix')
            value = T(value)
        u = value
        require(u == 2 * endpoint and u % 2 == 0, 'paired clocks')
        require(R(n) == 16 * M and 9 * R(endpoint) == (endpoint + 5) ** 2, 'spike ranks')
        require(valuation(endpoint, 2) == 1, 'exit parity')
        require(not in_G(n) and not in_G(endpoint) and B(n)[0] == endpoint, 'retained unsafe edge')
        next_rank = R(T(endpoint))
        require(next_rank == (endpoint // 2 - 1) ** 2 and next_rank > R(endpoint), 'unsafe successor rank')
        require(Q(R(endpoint), R(n) ** 2) > Q(9, 4) ** a / 1152, 'odd-clock lower ratio')
        require(R(u) == (u - 1) ** 2 and Q(R(u), R(n) ** 2) > Q(9, 4) ** a / 64,
                'even-clock lower ratio')
        rows.append({'j': j, 't': t, 'a': a, 'source': n, 'endpoint': endpoint,
                     'source_rank': R(n), 'endpoint_rank': R(endpoint), 'next_rank': next_rank,
                     'tail_cut': encode(Q(R(endpoint), 2)),
                     'weak_moment_lower': encode(Q(R(endpoint), 2 * R(n) ** 2)),
                     'even_clock': a, 'even_endpoint': u, 'even_rank': R(u),
                     'even_weak_moment_lower': encode(Q(R(u), 2 * R(n) ** 2))})
    return rows


def models():
    rows = []
    for cap in (2, 8, 32, 128):
        for time in (0, 1, cap, cap + 1):
            # Exact geometric complement of sources whose shifted endpoint is
            # at most cap. This is a different system, not Collatz dynamics.
            low = sum((Q(1, 2 ** source) for source in range(1, max(0, cap - time) + 1)), Q())
            rows.append([cap, time, encode(1 - low)])
    return {'shift_tail_rows': rows, 'shift_uniform_defect': [1, 1],
            'two_cycle_escape_defect': [0, 1], 'two_cycle_cesaro_mass': [1, 1],
            'model_scope': 'separate deterministic models; not Collatz counterexamples'}


def reconstruct():
    require(3 ** 17 < 2 ** 27 and 3 ** 2 > 2 ** 3, 'logarithm bracket')
    weights = {source: UNIT // R(source) ** 2 for source in range(2, LIMIT + 1)}
    result = {'schema': SCHEMA, 'scope': SCOPE, 'base': BASE,
              'source_cutoff': LIMIT, 'scale': UNIT,
              'ordinary_tail_constant': 43, 'raw_tail_constant': 77, 'unsafe_tail_constant': 200,
              'ordinary_tails': source_tails(weights), 'height_census': height_census(),
              'raw_tails': transported_tails(weights), 'unsafe_tails': unsafe_tails(weights),
              'fixed_clock_powers': power_sources(), 'clock_change_spikes': clock_family(),
              'limit_controls': models()}
    return json.loads(json.dumps(result))


def validate(report, expected):
    require(isinstance(report, dict) and set(report) == {'payload', 'sha256'}, 'report schema')
    require(report['sha256'] == seal(report['payload']), 'payload digest')
    require(report['payload'] == expected, 'semantic payload mismatch')


def self_test(expected):
    mutations = [
        lambda p: p.__setitem__('scope', 'Collatz proved'),
        lambda p: p.__setitem__('base', '0' * 40),
        lambda p: p.__setitem__('source_cutoff', LIMIT - 1),
        lambda p: p['raw_tails']['rows'].pop(),
        lambda p: p['height_census'].__setitem__('unsafe_sources', 0),
        lambda p: p['clock_change_spikes'][0].__setitem__('endpoint_rank', 1),
        lambda p: p.__setitem__('unsafe_tail_constant', 199),
        lambda p: p['limit_controls'].__setitem__('shift_uniform_defect', [0, 1]),
    ]
    for change in mutations:
        altered = deepcopy(expected)
        change(altered)
        require(altered != expected, 'no-op mutation')
        report = {'payload': altered, 'sha256': seal(altered)}
        try:
            validate(report, expected)
        except ValueError:
            continue
        raise ValueError('resealed corruption accepted')
    return len(mutations)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    expected = reconstruct()
    validate(json.loads(args.report.read_text(encoding='utf-8')), expected)
    if args.self_test:
        print(f'SELF-TEST PASS: {self_test(expected)} resealed corruptions rejected')
    if args.output:
        report = {'payload': expected, 'sha256': seal(expected)}
        args.output.write_text(json.dumps(report, sort_keys=True, separators=(',', ':')) + '\n', encoding='utf-8')
    print(seal(expected))
    print('VERIFIER PASS; finite interfaces, not an all-time or independent mathematical proof')


if __name__ == '__main__':
    main()
