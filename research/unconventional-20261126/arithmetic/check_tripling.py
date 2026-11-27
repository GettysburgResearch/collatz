"""Exact finite controls for the joint-clock theorem, using integer arithmetic."""
import json
from bisect import bisect_right
from collections import Counter
from math import gcd


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def trajectory(num, den, depth):
    dates = [0]
    states = [num]
    carries = [1]
    for _ in range(depth):
        value = 3 * states[-1] + den
        power = value & -value
        dates.append(dates[-1] + (power.bit_length() - 1))
        states.append(value // power)
        carries.append(3 * carries[-1] + (1 << dates[-1]))
    return dates, states, carries


def finite_joint(num, den, depth):
    s, x, f = trajectory(num, den, depth)
    t, y, g = trajectory(3 * num, den, depth)
    stop = min(s[-1], t[-1])
    dates = sorted(({z for z in s if z <= stop} | {z for z in t if z <= stop}))
    counts = Counter()
    for cut, following in zip(dates, dates[1:]):
        i, j = bisect_right(s, cut) - 1, bisect_right(t, cut) - 1
        h = max(i + 1, j + 2)
        cross = 3 ** (h - i - 1) * f[i] - 3 ** (h - j - 2) * g[j]
        require(f[i] % 3 and g[j] % 3, 'unsimplified ternary denominator')
        require(cross % (1 << following) == 0, 'dyadic cut failed')
        require(abs(cross) * 2 < (1 << cut) * 3 ** h, 'real cut failed')
        if cross == 0:
            require(i == j + 1 and s[i + 1] == t[j + 1] and x[i + 1] == y[j + 1],
                    'false synchronized merger')
            counts['zero'] += 1
        else:
            require(1 << (following - cut) < 3 ** h, 'local clock bound')
            counts['nonzero'] += 1
    if not counts['zero']:
        require(1 << stop < 3 ** ((2 * depth - 1) * (depth + 1)), 'global clock bound')
    return counts


def cycle(num, den, cap=20000):
    seen = {}
    while num not in seen:
        require(len(seen) < cap, 'cycle safety cap')
        seen[num] = len(seen)
        value = 3 * num + den
        num = value // (value & -value)
    return seen, {n for n in seen if seen[n] >= seen[num]}


def fixed_examples():
    pairs = [(17, 5), (83, 47), (217, 13), (4033, 1909), (10211, 1631), (414961, 84997)]
    results = []
    for num, den in pairs:
        left, first = cycle(num, den)
        right, second = cycle(3 * num, den)
        require(not (first & second) and not (left.keys() & right.keys()), 'orbits intersect')
        depth = max(len(left), len(right))
        require(den < 3 ** ((2 * depth - 1) * (depth + 1)), 'denominator condition')
        counts = finite_joint(num, den, depth)
        require(counts['zero'] == 0, 'full cycle certificate inconsistent')
        results.append({'numerator': num, 'denominator': den, 'odd_cardinalities': [len(left), len(right)],
                        'joint_cuts': counts['nonzero']})
    return results


def delayed_mergers():
    # The common singular center is -19/27. Clearing its denominator gives
    # positive ordinary x and an exact delayed merger at an arbitrary date N.
    dates = [8, 17, 83, 257, 1024, 4096]
    for n in dates:
        c = 19 * pow(2 ** n, -1, 27) % 27
        c += 27 * (1 - c % 2)
        src, remainder = divmod((1 << n) * c - 19, 27)
        require(not remainder and src % 2 == 1 and src > 0, 'delayed source')
        s, x, _ = trajectory(src, 1, 3)
        t, y, _ = trajectory(3 * src, 1, 2)
        require(s == [0, 1, 2, n] and t == [0, 4, n] and x[-1] == y[-1] == c,
                'delayed physical merger missing')
        require(finite_joint(src, 1, 3)['zero'] >= 1, 'missed singular cancellation')
    return dates


def symbolic_tree(k, budget=200000):
    # At time t, the two shortcut states are affine functions of the remaining
    # dyadic source bits z. The entries are their coefficients and constants.
    # A whole cylinder of synchronized identical states can be removed exactly.
    # Terminal cylinders may contain extra mergers, so the returned maximum
    # is a finite upper bound for disjoint paths, without a sharpness claim.
    # Starting odd source 1+2z has time-one values 2+3z and 5+9z.
    work = [(1, 1, 1, 2, 5)]
    visits = terminals = pruned = longest = 0
    while work:
        t, a, b, x, y = work.pop()
        px, py = 3 ** a, 3 ** (b + 1)
        visits += 1
        require(visits <= budget, 'symbolic tree safety cap')
        if px == py and x == y:
            pruned += 1
            continue
        for bit in (0, 1):
            ux, uy = x + px * bit, y + py * bit
            ex, ey = ux % 2, uy % 2
            if (a >= k and ex) or (b >= k and ey):
                require((1 << t) < 3 ** ((2 * k - 1) * (k + 1)), 'symbolic bound')
                longest = max(longest, t)
                terminals += 1
            else:
                xx = ((3 if ex else 1) * ux + ex) // 2
                yy = ((3 if ey else 1) * uy + ey) // 2
                work.append((t + 1, a + ex, b + ey, xx, yy))
    return {'K': k, 'nodes': visits, 'terminal_cylinders': terminals,
            'pruned_synchronized_cylinders': pruned, 'maximum_nonpruned_clock': longest}


if __name__ == '__main__':
    tally = Counter()
    sampled = 0
    for den in (1, 3, 5, 7, 11, 13, 17):
        for num in range(1, 256, 2):
            if gcd(num, den) == 1:
                tally.update(finite_joint(num, den, 20))
                sampled += 1
    print(json.dumps({'sample_size': sampled, 'sampled_cut_types': tally,
                      'known_disjoint_pairs': fixed_examples(), 'delayed_merger_dates': delayed_mergers(),
                      'symbolic_certificates': [symbolic_tree(k) for k in range(1, 9)]}, indent=2))
