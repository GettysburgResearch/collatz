#!/usr/bin/env python3
"""Finite controls for the modular carry classification. No external dependencies."""

from math import gcd, lcm


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


def dates_from_gaps(gaps):
    dates = [0]
    for gap in gaps:
        dates.append(dates[-1] + gap)
    return dates


def gaps_from_dates(dates):
    return tuple(b - a for a, b in zip(dates, dates[1:]))


def mechanical(a, p):
    return [(i * a + p - 1) // p for i in range(p + 1)]


def direct_carry(dates):
    total = 0
    for exponent in dates[:-1]:
        total = 3 * total + (1 << exponent)
    return total


def physical_replay(dates):
    p, a = len(dates) - 1, dates[-1]
    divisor = (1 << a) - 3**p
    check(divisor > 0, 'nonpositive cycle divisor')
    carry = direct_carry(dates)
    g = gcd(carry, divisor)
    d = divisor // g
    initial = carry // g
    state = initial
    visited = set()
    for exponent in gaps_from_dates(dates):
        check(state > 0 and state % 2 and gcd(state, d) == 1, 'bad odd phase')
        check(state not in visited, 'imprimitive cycle')
        visited.add(state)
        numerator = 3 * state + d
        check((numerator & -numerator).bit_length() - 1 == exponent, 'incorrect valuation')
        state = numerator >> exponent
    check(state == initial, 'word did not close physically')
    return g, d


def generated_subgroup(modulus, generators=(2, 3)):
    elements, frontier = {1}, [1]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            neighbor = current * generator % modulus
            if neighbor not in elements:
                elements.add(neighbor)
                frontier.append(neighbor)
    return elements


def order(x, modulus):
    y = x % modulus
    n = 1
    while y != 1:
        y = y * x % modulus
        n += 1
    return n


def invariants(modulus):
    group = generated_subgroup(modulus)
    v = lcm(order(2, modulus), order(3, modulus))
    return len(group) // v, v


def direct_clock_test(modulus, g):
    two, three = pow(2, g, modulus), pow(3, g, modulus)
    period = lcm(order(two, modulus), order(three, modulus))
    p2 = [pow(two, k, modulus) for k in range(period)]
    p3 = [pow(three, k, modulus) for k in range(period)]
    return any(gcd(gcd(a, s), period) == 1 and p2[a] == p3[s]
               for a in range(period) for s in range(period))


def marker_data(a, p):
    gaps = gaps_from_dates(mechanical(a, p))
    j = next(i for i in range(p) if gaps[i - 1] == gaps[i] == 2)
    start = (j - 1) % p
    gaps = gaps[start:] + gaps[:start]
    slots = [i for i in range(1, p) if (gaps[i - 1], gaps[i]) == (1, 2)]
    check(len(slots) >= 2*p - a - 1 and 2 not in slots, 'marker slot count')
    base = dates_from_gaps(gaps)
    base[1] += 1
    return base, slots


def choices(base, slots, modulus):
    p = len(base) - 1
    choices = {direct_carry(base) % modulus: ()}
    for i in slots:
        jump = pow(3, p - 1 - i, modulus) * pow(2, base[i], modulus) % modulus
        check(gcd(jump, modulus) == 1, 'not a unit increment')
        previous = len(choices)
        candidates = [((r + jump) % modulus, (*selected, i))
                      for r, selected in choices.items()]
        for r, selected in candidates:
            choices.setdefault(r, selected)
        check(len(choices) >= min(modulus, previous + 1), 'subset growth failed')
        if len(choices) == modulus:
            break
    return choices


def shifted(dates, slots):
    result = dates.copy()
    for i in slots:
        result[i] += 1
    return result


def test_marker():
    residue_witnesses = 0
    for p in range(9, 34):
        for a in range(3*p//2 + 1, 2*p):
            base, slots = marker_data(a, p)
            for m in range(2, 2*p - a + 1):
                if gcd(m, 6) > 1:
                    continue
                mode = choices(base, slots[:m-1], m)
                check(len(mode) == m, 'missing carry residue')
                for r, selection in mode.items():
                    dates = shifted(base, selection)
                    gaps = gaps_from_dates(dates)
                    check(min(gaps) == 1 and gaps.count(3) == 1, 'marker uniqueness failed')
                    check(direct_carry(dates) % m == r, 'incorrect residue')
                    if (1 << a) > 3**p:
                        physical_replay(dates)
                    residue_witnesses += 1
    return residue_witnesses


def tangible_witness(m, g, h):
    # Choose exact contracting clocks by comparing integer powers.
    for s in range(4, 1200):
        p = g * s
        for a in range((3*s)//2 + 1, (5*s)//3 + 1):
            A = g * a
            if (gcd(a, s) != 1 or 2*p-A < m or (1 << a) <= 3**s
                    or pow(2, A, m) != pow(3, p, m)):
                continue
            dates, slots = marker_data(A, p)
            base_carry = direct_carry(dates)
            found = choices(dates, slots[:m-1], m)[h]
            output = shifted(dates, found)
            actual = direct_carry(output)
            check(actual - base_carry == sum(3**(p-i-1) * 2**dates[i] for i in found),
                  'integer switch difference')
            G, d = physical_replay(output)
            check(actual % m == h and gcd(m, G) == gcd(m, h), 'full gcd restriction')
            return (p, A, G, d.bit_length(), found)
    raise ArithmeticError('expected example not found')


def vp(n, prime):
    k = 0
    while n % prime == 0:
        n //= prime
        k += 1
    return k


def cubic_examples():
    results = {}
    for p in range(4, 1600):
        for a in range(3*p//2 + 1, (5*p)//3 + 1):
            if gcd(a, p) != 1 or (1 << a) <= 3**p:
                continue
            D = (1 << a) - 3**p
            if D % 25:
                continue
            root_rank = (-2 * pow(a, -1, p)) % p
            E = mechanical(a, p)
            if E[root_rank + 1] - E[root_rank] != 2 or root_rank == 0:
                continue
            E[root_rank] += 1
            C = direct_carry(E)
            e = vp(gcd(C, D), 5)
            remainder = vp(D, 5) - e
            if (e not in (1, 2, 3) or remainder < 1 or e in results):
                continue
            G, d = physical_replay(E)
            check(vp(d, 5) == remainder and vp(G, 5) == e, 'incorrect partial valuation')
            results[e] = p, a, root_rank, e, remainder, G
            if len(results) == 3:
                return results
    raise ArithmeticError(f'cubic examples missing {results}')


def main():
    tested = 0
    for m in range(5, 180):
        if gcd(m, 6) != 1:
            continue
        u, _ = invariants(m)
        for g in range(1, 10):
            check(direct_clock_test(m, g) == (g % u == 0), 'group converse failed')
            tested += 1
    check(invariants(35) == (2, 12), '35 invariant factors')
    print('primitive modular-clock comparisons:', tested)
    print('direct switched carry witnesses:', test_marker())
    for m, g, h in ((5, 1, 0), (7, 1, 0), (35, 2, 0), (35, 2, 11), (25, 1, 0)):
        print('marker', (m, g, h), '-> (p,A,G,denominator bits,switches)', tangible_witness(m,g,h))
    print('single cubic (p,A,switched date,cancelled 5-valuation,retained 5-valuation,G):')
    print(cubic_examples())


if __name__ == '__main__':
    main()
