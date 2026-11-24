"""Independent finite controls for translated carry-row counts and native-clock cuts."""

import json
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import ceil, comb, gcd, prod


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def shortcut(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def odd_segment(x, s):
    states, gaps = [x], []
    for _ in range(s):
        a = 3 * states[-1] + 1
        gap = (a & -a).bit_length() - 1
        states.append(a >> gap)
        gaps.append(gap)
    return states, tuple(gaps)


@lru_cache(None)
def factors(n):
    remaining, result, p = n, {}, 2
    while p * p <= remaining:
        while remaining % p == 0:
            result[p] = result.get(p, 0) + 1
            remaining //= p
        p = 3 if p == 2 else p + 2
    if remaining > 1:
        result[remaining] = 1
    return result


def divisors(powers):
    values = [1]
    for p, n in powers.items():
        values = [v * p**e for v in values for e in range(n + 1)]
    return sorted(values)


def factor_cut(n, y, available):
    current = 1
    for p, e in sorted(available.items()):
        for _ in range(e):
            if n % (current * p):
                break
            if current * p > y:
                return current, p
            current *= p
    raise ArithmeticError('large divisor lacked a first crossing')


def shifted_check():
    intervals = crossings = 0
    products = [1, 2**12 * 3**6 * 5**4, 2 * 3 * 5 * 7 * 11 * 13 * 17,
                991 * 997, 239 * 241 * 243, 2**8 * 7**3 * 83**2]
    for n in products:
        fac = factors(n)
        ds = divisors(fac)
        for y in (1, 3, 25, 128, 2000):
            small = sum(d <= y for d in ds)
            for start in sorted({0, *ds, *(max(0, d - y // 2) for d in ds)}):
                ds_here = [d for d in ds if start <= d <= start + y]
                labels = [factor_cut(d, y, fac) for d in ds_here if d > y]
                require(len(labels) == len(set(labels)), 'duplicate translated divisor code')
                for d, (g, p) in zip((d for d in ds_here if d > y), labels):
                    require(g <= y < g * p and d % (g * p) == 0, 'invalid crossing factor')
                require(len(ds_here) <= (1 + len(fac)) * small, 'translated divisor bound')
                intervals += 1
                crossings += len(labels)
    return {'intervals': intervals, 'large_divisors_encoded': crossings}


@lru_cache(None)
def rows(word):
    s = len(word)
    carries = [[] for _ in range(s + 1)]
    for i in range(s):
        clock, carry = 0, 0
        for j in range(i + 1, s + 1):
            carry = 3 * carry + (1 << clock)
            clock += word[j - 1]
            carries[i].append(carry)
            carries[j].append(carry)
    return tuple(tuple(row) for row in carries)


def cut_control(start, length, s, k, level):
    def physical_slope(word, j):
        return Fraction(3**j, 1 << sum(word[:j]))

    occupancy = Counter()
    selected = Counter()
    covered, overrun, high = 0, 0, 0
    y = ceil(level * length)
    for x in range(start + 1 + (start % 2), start + length + 1, 2):
        states, word = odd_segment(x, s)
        cv = [all(sum(factors(b).get(p, 0) for h, b in enumerate(states) if h != j) >= e
                  for p, e in factors(a).items()) for j, a in enumerate(states)] if start < 10000 else None
        actual = [prod(gcd(a, b) for h, b in enumerate(states) if h != j) % a == 0
                  for j, a in enumerate(states)]
        if cv is not None:
            require(actual == cv, 'valuation/gcd disagreement')
        covered += any(actual)
        if sum(word) > k:
            overrun += 1
            z, odds = x, 0
            for _ in range(k):
                odds += z % 2
                z = shortcut(z)
            require(odds <= s, 'overrun had too many native odd inputs')
            continue
        if max(physical_slope(word, j) for j in range(s + 1)) > level:
            high += 1
            continue
        products = rows(word)
        for j, flag in enumerate(actual):
            if flag:
                require(prod(products[j]) % states[j] == 0, 'missing physical divisor')
                occupancy[word, j] += 1
                selected[x] += 1
    per_period = ceil(Fraction(length, 1 << k))
    require(overrun <= per_period * sum(comb(k, h) for h in range(s + 1)), 'long-clock bound')
    require(high * level <= per_period * (1 << k), 'physical maximal bound')
    if level >= Fraction(3, 2)**s:
        require(high == 0, 'unnecessary maximal term')
    sum_bounds = 0
    word_count = 0
    for positions in combinations(range(1, k + 1), s):
        word = tuple(b - a for a, b in zip((0, *positions), positions))
        word_count += 1
        if max(physical_slope(word, j) for j in range(s + 1)) > level:
            continue
        for j, row in enumerate(rows(word)):
            fac = Counter()
            for c in row:
                fac.update(factors(c))
            require(prod(p**e for p, e in fac.items()) == prod(row), 'row factorization')
            cap = sum(d <= y for d in divisors(fac))
            bd = cap * (1 + len(fac))
            require(occupancy[word, j] <= bd, 'shifted physical row omitted a source')
            sum_bounds += bd
    require(word_count == comb(k, s), 'native budget word enumeration')
    require(covered <= len(selected) + high + overrun, 'finite cover of all original sources')
    require(len(selected) <= sum_bounds, 'finite row union')
    return [length // 2, covered, overrun, high, len(selected)]


def max_control():
    checked = 0
    for k in (3, 6, 9, 12):
        count = 1 << k
        for start in (0, 231, 3**55 + 71):
            parity_codes = set()
            maxima = []
            for n in range(start + 1, start + count + 1):
                z, odd, mask, peak = n, 0, 0, Fraction(1)
                for h in range(k):
                    bit = z % 2
                    odd += bit
                    mask |= bit << h
                    peak = max(peak, Fraction(3**odd, 1 << (h + 1)))
                    z = shortcut(z)
                parity_codes.add(mask)
                maxima.append(peak)
            require(len(parity_codes) == count, 'translated period lost a code')
            for level in (Fraction(1), Fraction(3, 2), Fraction(7, 3), Fraction(5), Fraction(11)):
                fair_hits = sum(p >= level for p in maxima)
                weighted = Fraction(0)
                frontier = [(0, 0)]
                expected_hits = 0
                while frontier:
                    depth, weight = frontier.pop()
                    if Fraction(3**weight, 1 << depth) >= level:
                        expected_hits += 1 << (k - depth)
                        weighted += Fraction(3**weight, 4**depth)
                    elif depth < k:
                        frontier.extend(((depth + 1, weight), (depth + 1, weight + 1)))
                require(expected_hits == fair_hits, 'physical first-passage period differs')
                require(level * fair_hits <= count * weighted <= count, 'first-passage mass')
                checked += 1
    return checked


def main():
    require(3**5 < 2**8 and 8**40 < 2**22 * 7**35, 'entropy certificate')
    summary = [0] * 5
    windows = 0
    for start in (0, 121, 100003, 3**80 + 17):
        for s, k in ((2, 5), (3, 7), (4, 9)):
            for level in (Fraction(5, 4), Fraction(3, 2)**s):
                for i, value in enumerate(cut_control(start, 1024, s, k, level)):
                    summary[i] += value
                windows += 1
    print(json.dumps({'shifted_divisors': shifted_check(), 'physical_maximal_inequalities': max_control(),
                      'physical_window_configurations': windows, 'odd_start_window_probes': summary[0],
                      'covered_start_probes': summary[1], 'long_clock_probes': summary[2],
                      'large_slope_probes': summary[3], 'covered_good_word_probes': summary[4],
                      'entropy_comparisons': 2}, indent=2))


if __name__ == '__main__':
    main()
