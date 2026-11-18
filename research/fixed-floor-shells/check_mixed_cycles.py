"""Exact finite dictionaries for the three mixed-completion certificates."""

from fractions import Fraction

CYCLES = ((1,), (5, 7), (17, 25, 37, 55, 41, 61, 91))
DEPTH_CUTOFF = 10000
MASS_CUTOFF = 50000


def strip_twos(n):
    exponent = (n & -n).bit_length() - 1
    return exponent, n >> exponent


def classify_mirror(limit):
    # A record gives the first hitting clock on the listed cycles, the
    # valuation total, and the entrance vertex. None means a disjoint cycle.
    records = {v: (0, 0, v) for cycle in CYCLES for v in cycle}
    for start in range(1, limit + 1, 2):
        vertex = start
        path = []
        seen = set()
        while vertex not in records and vertex not in seen:
            seen.add(vertex)
            exponent, nxt = strip_twos(3 * vertex - 1)
            path.append((vertex, exponent))
            vertex = nxt
        result = records.get(vertex)
        for vertex, exponent in reversed(path):
            if result is not None:
                depth, total, target = result
                result = (depth + 1, total + exponent, target)
            records[vertex] = result
    return records


def period_data(cycle):
    prefix = [0]
    for i, vertex in enumerate(cycle):
        exponent, nxt = strip_twos(3 * vertex - 1)
        assert nxt == cycle[(i + 1) % len(cycle)]
        prefix.append(prefix[-1] + exponent)
        assert 3 ** (i + 1) > 2 ** prefix[-1]
    return prefix


def reference_total(depth, prefix):
    periods, index = divmod(depth, len(prefix) - 1)
    return periods * prefix[-1] + prefix[index]


def certify_distortion(cycle, prefix, records):
    # min_at[target][i] is the least y<=DEPTH_CUTOFF with this first entry.
    min_at = {vertex: {} for vertex in cycle}
    for y in range(1, DEPTH_CUTOFF + 1, 2):
        result = records[y]
        if result is None:
            continue
        depth, _, target = result
        if not depth or target not in min_at:
            continue
        assert y > cycle[0]
        min_at[target].setdefault(depth, y)

    last_small = max(max(table) for table in min_at.values())
    period = len(cycle)
    fallback = DEPTH_CUTOFF + 1
    next_factor = Fraction(3 * fallback, 3 * fallback - 1)
    period_gain = Fraction(3**period, 2**prefix[-1])
    assert next_factor**period < period_gain
    bound_max = Fraction()
    for depth in range(1, last_small + period + 1):
        target = cycle[depth % period]
        bound = Fraction(target * 2**reference_total(depth, prefix), 3**depth)
        for i in range(1, depth + 1):
            low = min_at[target].get(i, fallback)
            bound *= Fraction(3 * low, 3 * low - 1)
        assert bound < cycle[0]
        bound_max = max(bound_max, bound)
    return last_small, bound_max


def certify_integer_completions(cycle, prefix, records):
    # At z=0,1 any reducing continuation gives x<z+d. Follow every such
    # positive odd x to 1. Further laps at 1 only increase the multiplier.
    biggest_candidate = 0
    for z in (0, 1):
        for x in range(1, z + cycle[0], 2):
            state = x
            multiplier = Fraction(1)
            while state != 1:
                exponent, state = strip_twos(3 * state + 1)
                multiplier *= Fraction(2**exponent, 3)
                b = 1
                while 2**b * multiplier <= 1:
                    y = 2**b * (z + cycle[0]) - state
                    biggest_candidate = max(biggest_candidate, y)
                    if y > 0:
                        assert y <= MASS_CUTOFF and y % 2 == 1
                        record = records[y]
                        if record is not None:
                            q, total, target = record
                            forbidden = (
                                q > 0
                                and cycle[q % len(cycle)] == target
                                and total - reference_total(q, prefix) == b
                            )
                            assert not forbidden
                    b += 1
    return biggest_candidate


def main():
    records = classify_mirror(MASS_CUTOFF)
    affine_events = set()
    for cycle in CYCLES:
        prefix = period_data(cycle)
        last, bound = certify_distortion(cycle, prefix, records)
        candidate = certify_integer_completions(cycle, prefix, records)
        for y in range(1, MASS_CUTOFF + 1, 2):
            record = records[y]
            if record is None:
                continue
            q, total, target = record
            if not q or target != cycle[q % len(cycle)]:
                continue
            b = total - reference_total(q, prefix)
            assert b >= 1
            intercept = 2**b * cycle[0] - y
            assert intercept > 0
            # Any unit passing the initial screen is 1 mod 3.
            if (pow(2, b, 3) + intercept) % 3:
                affine_events.add((b, intercept))
        print('cycle', cycle[0], 'last small depth', last, 'max bound', bound,
              'largest integer-completion candidate', candidate)

    mass = sum((Fraction(1, 4**b) for b, _ in affine_events), Fraction())
    assert mass < Fraction(1, 10)
    tail = Fraction(sum(cycle[0] ** 2 for cycle in CYCLES), MASS_CUTOFF)
    good = Fraction(2, 3) - Fraction(517167, 10**6) - Fraction(1, 10) - tail
    assert good > Fraction(43, 1000)
    print('combined finite events', len(affine_events),
          'mass below 1/10; tail at most', tail,
          'common good additive Haar mass above 43/1000')


if __name__ == '__main__':
    main()
