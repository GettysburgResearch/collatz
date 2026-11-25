"""Replay both original traces at their actual finite clocks using integers."""
from collections import Counter
import json


def check(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def trace(n, h):
    points, odd = [n], [0]
    for _ in range(h):
        odd.append(odd[-1] + points[-1] % 2)
        points.append(step(points[-1]))
    return points, odd


def first_hit(n):
    for h in range(4000):
        if n == 1:
            return h
        n = step(n)
    raise ValueError('finite control failed to hit within its recorded budget')


def ordinary_controls():
    totals = Counter()
    for z in range(1, 512, 2):
        for j in range(1, 4):
            upper = 3**j * z
            h = first_hit(upper)
            low, q = trace(z, h)
            high, p = trace(upper, h)
            for t in range(1, h + 1):
                debt = j + p[t] - q[t]
                if debt < 0:
                    break
                check(high[t] < 3**debt * low[t], 'pre-overshoot order')
            for d in range(5):
                m = max(2 * 3**d, j + p[h] + d)
                totals['scale_comparisons'] += 1
                if min(low) < m:
                    totals['drops'] += 1
                    continue
                check(j + p[h] + d < q[h], 'supplied odd work')
                t = next(i for i in range(h) if q[i] >= j + p[i])
                check(0 < t < h and q[t] == j + p[t] and high[t] < low[t], 'first balance')
                suffix, suffix_q = trace(high[t], h - t)
                check(suffix[-1] == 1 and suffix_q[-1] == p[h] - p[t] < p[h], 'saved actual suffix')
                totals['positive_carries'] += 1
    check(totals['positive_carries'] > 0, 'missing carry branch')
    return dict(totals)


def carry_controls():
    total = 0
    for c in range(1, 33):
        h = first_hit(c)
        _, odds_c = trace(c, h)
        for k in range(1, 4):
            for u in range(1, 32, 2):
                length = h + 2 * k
                endpoint = trace(c + 2**length * u, length)[0][-1]
                grade = odds_c[-1] + k - 1
                check(step(endpoint) == step(3**grade * u), 'adaptive positive carry meeting')
                total += 1
    return total


def canonical_control(h):
    z, rem = divmod(2**h - 271, 81)
    check(rem == 0 and z % 48 == 17, 'ordinary canonical source')
    low, q = trace(z, h)
    high, p = trace(3 * z, h)
    check(p[h] == 3 and high.index(1) == h, 'overall first hit and rank')
    check({i for i, x in enumerate(low) if x % 2 == 0} == {1, 3, 6, h}, 'isolated even inputs')
    check(all(x % 3 != 0 and x % 18 != 10 for x in low), 'any tripled successor excluded')
    check(min(low) * 2**40 > z, 'physical contraction absent')
    t = next(i for i in range(h + 1) if q[i] >= p[i] + 1)
    check(t == 5 and low[t] == high[t] + 1 and high[t] % 16 == 8, 'carry and runway')
    check(p[h] - p[t] == 1, 'one odd remains on the original upper suffix')
    return {'upper_first_hit': h, 'first_balance': t, 'upper_odd_inputs': p[-1],
            'saved_upper_odd_inputs': p[t], 'lower_odd_inputs_at_hit': q[-1],
            'criterion_checked_through_clock': h}


if __name__ == '__main__':
    records = [canonical_control(h) for h in (18, 180, 342, 504)]
    print(json.dumps({'ordinary': ordinary_controls(), 'canonical': records, 'adaptive_meetings': carry_controls()}, sort_keys=True, indent=2))
