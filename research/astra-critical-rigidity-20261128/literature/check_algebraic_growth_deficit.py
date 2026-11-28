"""Exact finite identities for odd-orbit partial sums and their dyadic precision."""
from collections import Counter
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def orbit(starter, length):
    states = [starter]
    extras = [0]
    partials = [Fraction(starter + 1)]
    for date in range(1, length + 1):
        raw = 3 * states[-1] + 1
        exponent = (raw & -raw).bit_length() - 1
        states.append(raw >> exponent)
        extras.append(extras[-1] + exponent - 1)
        partials.append(Fraction((states[-1] + 1) << (date + extras[-1]), 3 ** date))
        addend = Fraction(2, 3) ** date * ((1 << extras[-1]) - (1 << extras[-2]))
        require(partials[-1] - partials[-2] == addend, 'incorrect odd increment')
    return states, extras, partials


def check_source(starter, length, stats):
    states, extras, partials = orbit(starter, length)
    stats['sources'] += 1
    stats['physical_steps'] += length
    for horizon in (1, length // 3, length // 2, length - 1, length):
        for stop in sorted({1, max(1, horizon // 2), horizon}):
            dates = [0]
            dates.extend(j for j in range(1, stop) if extras[j] > extras[j - 1])
            dates.append(stop)
            require(len(set(partials[u] for u in dates[:-1])) == len(dates) - 1,
                    'left endpoints repeated a real slope')
            for u, v in zip(dates, dates[1:]):
                x = (states[u] + 1) << (u + extras[u])
                y = 3 ** u
                require(Fraction(x, y) == partials[u], 'incorrect integer coordinates')
                require(x % (1 << v) == 0, 'dyadic precision failed')
                require(partials[v - 1] == partials[u], 'missed an active date')
                require(0 <= partials[horizon] - partials[u]
                        <= (1 << extras[horizon]) * Fraction(2, 3) ** v,
                        'single-horizon real tail estimate failed')
                stats['neighbor_pairs'] += 1
                if extras[v] == extras[v - 1]:
                    stats['artificial_quiet_ends'] += 1
                if extras[v] > extras[v - 1] + 1:
                    stats['multi_slip_ends'] += 1
                stats['widest_common_run'] = max(stats['widest_common_run'], v - u)


def main():
    stats = Counter()
    for starter in list(range(1, 256, 2)) + [(1 << k) - 1 for k in (17, 31, 67, 101)]:
        check_source(starter, 108, stats)
    print(json.dumps(stats, sort_keys=True))


if __name__ == '__main__':
    main()
