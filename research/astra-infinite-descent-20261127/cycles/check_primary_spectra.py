"""Exact controls for primary spectra, native rectangles, and clock entropy."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import gcd, lcm, prod
import json
from check_spectral import (active_orders, cyclotomic, divisors, poly_remainder,
                            primary_factors, require)


def expected(g):
    factors = [q for _, q in primary_factors(g)]
    if g % 4 != 2:
        return {tuple(sorted([1] + factors))}
    odd = [q for q in factors if q != 2]
    return {tuple(sorted([1, 2] + [q * multiplier for q, multiplier in zip(odd, row)]))
            for row in product((1, 2), repeat=len(odd))}


def classify(rows, g, alphabet):
    ds = divisors(g)
    weights = []
    for order in ds[1:]:
        basis = [poly_remainder([0] * j + [1], cyclotomic(order)) for j in range(g)]
        radix = 2 + 2 * max(alphabet) * sum(max(map(abs, row), default=0) for row in basis)
        weights.append([sum(entry * radix ** k for k, entry in enumerate(row)) for row in basis])
    reached = {1}
    checked = 0
    for values in rows:
        checked += 1
        mask = 1
        for j, column in enumerate(weights, 1):
            if sum(x * y for x, y in zip(values, column)):
                mask |= 1 << j
        reached.add(mask)
    unions = {1}
    for mask in reached:
        unions.update({old | mask for old in unions})
    predicted = expected(g)
    threshold = 1 + sum(len(cyclotomic(q)) - 1 for _, q in primary_factors(g))
    observed = set()
    for mask in unions:
        orders = tuple(d for i, d in enumerate(ds) if mask & (1 << i))
        if lcm(*orders) != g:
            continue
        degree = sum(len(cyclotomic(d)) - 1 for d in orders)
        require(degree >= threshold, 'joint primary degree at arbitrary height')
        if degree == threshold:
            observed.add(orders)
    require(observed == predicted, 'all and only the equality order sets')
    return {'g': g, 'rows': checked, 'alphabet': list(alphabet), 'optimal_spectra': sorted(observed)}


def valuation(n, prime):
    require(n != 0, 'nonzero differences')
    n = abs(n)
    if prime == 2:
        return (n & -n).bit_length() - 1
    exponent = 0
    while n % prime == 0:
        exponent += 1
        n //= prime
    return exponent


def exact_native(g, twisted, wide):
    a, b = 31, 19
    # Offsets change only ranks whose immediately preceding baseline gap is two.
    dates = [i * a // b for i in range(b + 1)]
    if wide:
        for i in range(7, 13):
            dates[i] = dates[6] + i - 6
    slots = [i for i in range(1, b) if dates[i] - dates[i - 1] >= 2]
    factors = [q for _, q in primary_factors(g)]
    skip_parity = bool(twisted)
    primaries = [(prime, q) for prime, q in primary_factors(g) if not (q == 2 and skip_parity)]
    full_dates = []
    for j in range(g):
        cell = list(dates[:-1])
        for slot, (ell, q) in zip(slots, primaries, strict=False):
            v = int(j % q < q // ell)
            if q in twisted and j % 2:
                v = 1 - v
            cell[slot] -= v
        full_dates.extend(a * j + x for x in cell)
    full_dates.append(a * g)
    gaps = [y - x for x, y in zip(full_dates, full_dates[1:])]
    require(min(gaps) >= 1 and len(slots) >= len(primaries), 'positive true gap word')
    physical_date = 0
    carry = 0
    for v in gaps:
        carry = 3 * carry + (1 << physical_date)
        physical_date += v
    determinant = (1 << (g * a)) - 3 ** (g * b)
    common = gcd(carry, determinant)
    q = determinant // common
    x = carry // common
    exps = [i * a // b - full_dates[i] for i in range(b * g)]
    require(min(exps) == 0, 'canonical cut')
    width = max(exps)
    lowbits = [1 << (width - d) for d in exps]
    crows = [lowbits[r::b] for r in range(b)]
    orders = active_orders(crows, g)
    target_orders = {1, *factors} - set(twisted) | {2 * prime for prime in twisted}
    require(set(orders) == target_orders and lcm(*orders) == g, 'actual full twisted spectrum')
    labels = []
    for step, (e, c) in enumerate(zip(gaps, lowbits)):
        require(x > 0 and x % 2 == 1 and x % 3 and gcd(x, q) == 1, 'reduced positive odd state')
        y = c * x
        labels.append(y)
        require(y & -y == c, 'native lowbit')
        require((3 * x + q) % (1 << (e + 1)) == 1 << e, 'exact native exponent')
        x = (3 * x + q) >> e
    require(x == carry // common, 'exact closure')
    for i, y in enumerate(labels):
        beta = (i + 1) * a // b - i * a // b
        require((1 << beta) * labels[(i + 1) % len(labels)] == 3 * y + q * lowbits[i],
                'normalized native step including seam')
    levels = [0, 1] if twisted else [0]
    axes = [d for d in factors if not (twisted and d == 2)]
    conditional = 2 if twisted else 1
    triples_ok = all(len({v % 3 for v in row}) == len(set(row)) for row in crows)
    vtests = rects = entropy_checks = 0
    for parity in levels:
        labels_for = {tuple(j % axis for axis in axes): j
                      for j in range(g) if not twisted or j % 2 == parity}
        require(len(labels_for) == prod(axes), 'full CRT fibers')
        for r in range(b):
            zero = tuple(0 for _ in axes)
            origin = labels_for[zero]
            differences = []
            c_values = []
            for t, axis in enumerate(axes):
                vals = [labels[r + b * labels_for[tuple(z if n == t else 0 for n in range(len(axes)))]]
                        for z in range(axis)]
                diffs = [v - vals[0] for v in vals]
                cvals = [lowbits[r + b * labels_for[tuple(z if n == t else 0 for n in range(len(axes)))]]
                         for z in range(axis)]
                require(len(set(vals)) == axis and max(vals) - min(vals) <= 4*q*(1 << width)*(conditional*b*axis+1),
                        'uniform independent-coordinate difference bound')
                differences.append(diffs)
                c_values.append(cvals)
            for coordinate, j in labels_for.items():
                require(labels[r + b*j] == labels[r + b*origin] + sum(differences[t][v] for t, v in enumerate(coordinate)),
                        'actual additive label rectangle')
                require(lowbits[r + b*j] == lowbits[r + b*origin] +
                        sum(c_values[t][v] - c_values[t][0] for t, v in enumerate(coordinate)),
                        'actual additive lowbit rectangle')
                rects += 1
            owners = [t for t, axis in enumerate(axes) if len(set(c_values[t])) > 1]
            require(len(owners) <= 1, 'physical power-Sidon separation')
            for prime in ([2, 3] if triples_ok else [2]):
                previous = set()
                for diffs in differences:
                    bag = {valuation(u - v, prime) for u, v in combinations(diffs, 2)}
                    require(previous.isdisjoint(bag), 'disjoint native valuation sets')
                    vtests += len(bag) * len(previous)
                    previous |= bag
        # Direct finite word-distribution independence. It is enough to record at
        # each date which actual coordinate changes the lowbit on the given slice.
        for r in range(b):
            words = {}
            for coordinate, j in labels_for.items():
                words[coordinate] = tuple(lowbits[(r + n + b*j) % len(labels)] for n in range(11))
            partitions = []
            for t, axis in enumerate(axes):
                axis_words = {}
                for z in range(axis):
                    base = tuple(z if n == t else 0 for n in range(len(axes)))
                    axis_words[z] = words[base]
                partitions.append(axis_words)
            observed = Counter(words.values())
            projected = Counter(tuple(partitions[t][z] for t, z in enumerate(coord)) for coord in words)
            require(sorted(observed.values()) == sorted(projected.values()), 'word entropy equals projected sum')
            prod_counts = sorted(prod(vs) for vs in product(*(Counter(row.values()).values() for row in partitions)))
            require(prod_counts == sorted(observed.values()), 'exact product multiplicities')
            entropy_checks += 1
    return {'g': g, 'twisted': sorted(twisted), 'W': width, 'h': g*a, 'q_bits': q.bit_length(),
            'active_orders': orders, 'rectangle_labels': rects, 'valuation_comparisons': vtests,
            'ternary_unit_test': triples_ok, 'exact_entropy_checks': entropy_checks}


def schedules(width, lower, upper, length):
    # As alpha varies, the intercept ordering of floor(x+i*alpha) changes only
    # where (i-j)*alpha is integral. Verify the rational bracket misses every
    # such point, then evaluate all cyclic intercept cells at its midpoint.
    require((1 << lower.numerator) < 3 ** lower.denominator and
            (1 << upper.numerator) > 3 ** upper.denominator, 'exact log_2(3) bracket')
    require(all(n * lower // 1 == n * upper // 1 for n in range(1, length + 1)),
            'no arrangement event within rational slope bracket')
    alpha = (lower + upper) / 2
    cuts = sorted({(-i * alpha) % 1 for i in range(length)})
    highest = 0
    for intercept in cuts:
        counts = [1] * (width + 1)
        floor = intercept // 1
        for i in range(1, length):
            next_floor = (intercept + i * alpha) // 1
            increment = next_floor - floor
            # e>=1 gives d'<=d+beta-1; use unnormalized integer path counts.
            counts = [sum(counts[max(0, nxt - increment + 1):]) for nxt in range(width + 1)]
            floor = next_floor
        highest = max(highest, sum(counts))
    return highest


def main():
    # A ternary level alphabet exercises values beyond binary indicators.
    exhaustive = [classify(product((1, 2, 4), repeat=g), g, (1, 2, 4))
                  for g in (2, 3, 4, 5, 6, 7, 8, 9, 10, 12)]
    native = []
    for g in (6, 10, 12, 15, 18, 24, 30, 42, 45, 60):
        odd = [q for _, q in primary_factors(g) if q > 2]
        choices = [set(subset) for r in range(len(odd) + 1) for subset in combinations(odd, r)] if g % 4 == 2 else [set()]
        native.extend(exact_native(g, tws, wide) for tws in choices for wide in (False, True))
    # 1054/665 and 24727/15601 straddle the irrational slope.
    lower = Fraction(1054, 665)
    upper = Fraction(24727, 15601)
    length = 256
    maximum = schedules(3, lower, upper, length)
    require(maximum**5 < 3**(4*length), 'width-three word entropy below four fifths')
    print(json.dumps({'exhaustive_levels': exhaustive, 'native': native, 'width_three': {
        'length': length, 'lower': str(lower), 'upper': str(upper), 'max_words': maximum,
        'four_fifths_certificate': 'max_words**5 < 3**(4*length)'}}, indent=2))


if __name__ == '__main__':
    main()
