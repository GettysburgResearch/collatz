"""Exact checks of near-octave rank masks and odd-clock packing."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd
from random import Random
import json


def check(condition, label):
    if not condition:
        raise ArithmeticError(label)


def carry(gaps):
    value = date = 0
    for gap in gaps:
        value = 3 * value + (1 << date)
        date += gap
    return value


def orbit(gaps, determinant):
    numerator = carry(gaps)
    values = []
    for gap in gaps:
        check(numerator % 2 == 1, 'native odd source')
        values.append(numerator)
        incoming = 3 * numerator + determinant
        check(incoming % (1 << (gap + 1)) == (1 << gap), 'exact odd valuation')
        numerator = incoming >> gap
    check(numerator == values[0], 'cycle closure')
    return values


def offsets(gaps):
    p, h = len(gaps), sum(gaps)
    date = 0
    values = []
    for i, gap in enumerate(gaps):
        quotient, rank = divmod(i * h, p)
        values.append((rank, quotient - date))
        date += gap
    return values


def mask(gaps, determinant):
    p, h = len(gaps), sum(gaps)
    coefficients = Counter({0: 1})
    positive = negative = 0
    for rank, delta in offsets(gaps):
        check(delta in (-1, 0, 1), 'signed-unit offset')
        if delta == 0:
            continue
        if delta == 1:
            exponent, weight = rank, -1
            positive += 1
        else:
            exponent, weight = rank - p, 1
            negative += 1
        coefficients[exponent] += weight
        coefficients[exponent + 1] -= weight
    support = [k for k, v in coefficients.items() if v]
    check(sum(coefficients.values()) == 1 and all(abs(v) <= 1 for v in coefficients.values()),
          'unit coefficients with H(1)=1')
    v = pow(h, -1, p)
    u = (1 - v * h) // p
    z = pow(2, u, determinant) * pow(3, v, determinant) % determinant
    x = pow(z, -1, determinant)
    check(pow(z, p, determinant) == 2 % determinant and
          pow(z, h, determinant) == 3 % determinant, 'Bezout generator')
    residue = sum(coefficients[k] * pow(x, k, determinant) for k in support) % determinant
    c = carry(gaps)
    check(residue == (2 * (1 - x) * c * pow(3, 1 - p, determinant)) % determinant,
          'literal full-modulus identity')
    check(gcd(residue, determinant) == gcd(c, determinant), 'complete numeric canceled factor')
    return positive, negative, max(support) - min(support), gcd(c, determinant) > 1


def check_packing(gaps, values, determinant, stats):
    p, h = len(gaps), sum(gaps)
    off = offsets(gaps)
    errors = sum(delta != 0 for _, delta in off)
    mechanical = [(i + 1) * h // p - i * h // p for i in range(p)]
    edits = sum(a != b for a, b in zip(gaps, mechanical))
    check(edits <= 2 * errors, 'physical Hamming error')
    t = (p - 2) // (1 + edits)
    if t <= 0:
        return
    def factors(word):
        extended = word + word
        return [tuple(extended[i:i + t]) for i in range(p)]
    clean = factors(mechanical)
    observed = factors(gaps)
    check(len(set(clean)) <= t + 1, 'mechanical factor count')
    check(len(set(observed)) <= t + 1 + edits * t < p, 'physical factor collision')
    starts = {}
    for second, word in enumerate(observed):
        if word in starts:
            first = starts[word]
            break
        starts[word] = second
    else:
        raise ArithmeticError('missing physical collision')
    common = gcd(values[0], determinant)
    difference = abs(values[first] - values[second]) // common
    check(difference > 0 and difference % (1 << (1 + sum(word))) == 0,
          'nonzero separation including terminal odd bit')
    check(1 << t < max(values) // common, 'clear-denominator height packing')
    stats['positive_packing_windows'] += 1
    stats['maximum_packing_window'] = max(stats['maximum_packing_window'], t)


def physical(gaps, stats):
    p, h = len(gaps), sum(gaps)
    if p < 2:
        return
    determinant = (1 << h) - 3 ** p
    if determinant <= 1:
        return
    values = orbit(gaps, determinant)
    if len(set(values)) < p:
        return
    scale = Fraction(1 << h, 3 ** p)
    low_width = scale * max(1, Fraction(max(values), 2 * min(values)))
    if low_width ** 4 >= 2:
        return
    start = values.index(min(values))
    gaps = gaps[start:] + gaps[:start]
    values = values[start:] + values[:start]
    check(carry(gaps) == values[0], 'minimum rooting')
    g = gcd(p, h)
    phase_limits = {}
    for rank, delta in offsets(gaps):
        check(delta in (-1, 0, 1), 'physical cut clipping')
        if delta and delta not in phase_limits:
            phase_limits[delta] = (low_width if delta == 1 else scale) ** p
        if delta == 1:
            check((g > 1 or rank > 0) and 2 ** rank <= phase_limits[delta], 'low clipping')
        elif delta == -1:
            check(2 ** (p - rank) <= phase_limits[delta], 'high clipping')
    stats['primitive_near_octave_words'] += 1
    stats['noncoprime_primitive_words'] += g > 1
    check_packing(gaps, values, determinant, stats)
    if g == 1:
        pos, neg, degree, canceled = mask(gaps, determinant)
        stats['minimum_rooted_coprime_words'] += 1
        stats['minimum_rooted_positive_mask'] += pos > 0
        stats['minimum_rooted_negative_mask'] += neg > 0
        stats['minimum_rooted_nontrivial_cancellations'] += canceled
        stats['maximum_minimum_rooted_mask_degree'] = max(
            stats['maximum_minimum_rooted_mask_degree'], degree)


def main():
    rng = Random(43716)
    stats = Counter()
    for h in range(3, 16):
        for p in range(2, h):
            if (1 << h) <= 3 ** p:
                continue
            for cuts in combinations(range(1, h), p - 1):
                dates = (0,) + cuts + (h,)
                physical([b - a for a, b in zip(dates, dates[1:])], stats)
    candidates = [p for p in range(18, 131) if gcd(p, (3 ** p).bit_length()) == 1
                  and Fraction(1 << (3 ** p).bit_length(), 3 ** p) ** 12 < 3]
    for _ in range(260):
        p = rng.choice(candidates)
        h = (3 ** p).bit_length()
        width = min(7, max(1, p // 16))
        low = {t for t in range(1, width + 1) if rng.randrange(2)}
        high = {p - t for t in range(1, width + 1) if rng.randrange(3) == 0}
        dates = [i * h // p - (i * h % p in low) + (i * h % p in high)
                 for i in range(p)] + [h]
        gaps = [b - a for a, b in zip(dates, dates[1:])]
        if min(gaps) < 1:
            continue
        # These separately counted roots need not be the physical minimum.
        pos, neg, _, _ = mask(gaps, (1 << h) - 3 ** p)
        stats['arbitrary_rooted_both_signs'] += bool(pos and neg)
        physical(gaps, stats)
    for p, h in ((12, 19), (41, 65), (53, 84), (306, 485)):
        if (1 << h) <= 3 ** p:
            continue
        for g in (2, 3, 5):
            if Fraction(1 << h, 3 ** p) ** (8 * g) >= 2:
                continue
            for _ in range(5):
                # Different visits to the same reduced rank have distinct offsets.
                dates = [i * h // p - int(i > 0 and i * h % p in (0, 1, 2)
                                          and rng.randrange(3) == 0)
                         for i in range(p * g)] + [h * g]
                gaps = [b - a for a, b in zip(dates, dates[1:])]
                if min(gaps) >= 1:
                    physical(gaps, stats)
    check(stats['arbitrary_rooted_both_signs'] > 0, 'wrapped Laurent control')
    check(stats['noncoprime_primitive_words'] > 0, 'unequal masks at repeated ranks')
    print(json.dumps(dict(sorted(stats.items())), indent=2))


if __name__ == '__main__':
    main()
