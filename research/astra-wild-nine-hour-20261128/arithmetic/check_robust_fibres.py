"""Finite exact controls for conditional ternary fibres and the physical floor."""

import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

from check_branch_spectrum import canonical, iterate, require, word_row


def geometric_laws(parameter, depth):
    laws = [{0: Fraction(1)}]
    for n in range(1, depth + 1):
        modulus = 3**n
        period = 2 * 3 ** (n - 1)
        residue = Counter()
        mass = parameter / (1 - (1 - parameter) ** period)
        for e in range(1, period + 1):
            inverse = pow(2**e, -1, modulus)
            for suffix, probability in laws[-1].items():
                residue[((1 + 3 * suffix) * inverse) % modulus] += mass * probability
            mass *= 1 - parameter
        require(sum(residue.values()) == 1, (n, parameter, "infinite-gap normalization"))
        laws.append(residue)
    return laws


def moment_checks():
    count, conditional = 0, 0
    for parameter in (Fraction(1, 2), Fraction(3, 5), Fraction(2, 3)):
        laws = geometric_laws(parameter, 5)
        for n in range(1, 5):
            for m in range(1, 6 - n):
                width = 3**n
                for q in (2, 3):
                    leaf_bound = sum(weight**q for weight in laws[m].values())
                    joint = sum(weight**q for weight in laws[n + m].values())
                    low = sum(weight**q for weight in laws[n].values())
                    require(joint <= low * leaf_bound, (n, m, q, parameter))
                    count += 1
                    for z, marginal in laws[n].items():
                        leaf = [laws[n + m].get(z + width * u, Fraction(0))
                                for u in range(3**m)]
                        require(sum(leaf) == marginal, (z, n, parameter, "marginal"))
                        require(sum(weight**q for weight in leaf) <= marginal**q * leaf_bound,
                                (z, n, m, q, parameter, "conditional moment"))
                        conditional += 1
    return {"global": count, "positive_low_cells": conditional}


def finite_composition_rows():
    count = 0
    for k in range(1, 15):
        row = [Counter() for _ in range(k + 1)]
        direct = [Counter() for _ in range(k + 1)]
        for r in range(2**k):
            p, endpoint = iterate(r, k)
            direct[p][endpoint] += 1
        for p in range(k + 1):
            for positions in combinations(range(k), p):
                distances = [k - i for i in reversed(positions)]
                bounds = [0] + distances + [k + 1]
                gaps = [y - x for x, y in zip(bounds, bounds[1:])]
                require(len(gaps) == p + 1 and min(gaps) > 0 and sum(gaps) == k + 1,
                        (k, positions, gaps))
                modulus = 3**p
                offset = sum(3**j * pow(2**distance, -1, modulus)
                             for j, distance in enumerate(distances)) % modulus
                row[p][offset] += 1
                count += 1
            require(row[p] == direct[p] and sum(row[p].values()) == comb(k, p),
                    (k, p, "whole composition row including multiplicities"))
    return count


def bars(k, p, mask):
    seen = 0
    values = [0]
    for i in range(k):
        seen += (mask >> i) & 1
        values.append(k * seen - (i + 1) * p)
    return values


def rotate_at_minimum(k, mask, values):
    cut = values.index(min(values))
    return (mask >> cut) | ((mask % (1 << cut)) << (k - cut))


def translated_intervals():
    count = 0
    survivors = 0
    for k in range(1, 12):
        size = 2**k
        for start in (1, size // 2 + 1, size + size // 3 + 1, 6 * size + 1):
            splits = {}
            parity_words = set()
            for source in range(start, start + size):
                state, grade, mask = source, 0, 0
                least, greatest = source, source
                maximum_multiplier = Fraction(1)
                coefficient_positive = True
                for j in range(k):
                    odd = state % 2
                    mask |= odd << j
                    grade += odd
                    state = (3 * state + 1) // 2 if odd else state // 2
                    least = min(least, state)
                    greatest = max(greatest, state)
                    multiplier = Fraction(3**grade, 2 ** (j + 1))
                    maximum_multiplier = max(maximum_multiplier, multiplier)
                    coefficient_positive &= multiplier >= 1
                parity_words.add(mask)
                p, offset = canonical(k, mask)
                require(p == grade and state == 3**p * (source // size) + offset,
                        (k, start, source, "integer split"))
                splits.setdefault((p, offset), set()).add(state)
                if least >= source and source >= k:
                    require(2 * 3**grade >= size, (k, source, "physical grade lower bound"))
                    survivors += 1
                if coefficient_positive and source >= k:
                    require(least >= source and greatest < 2 * maximum_multiplier * source,
                            (k, source, "whole excursion band"))
                count += 1
            require(len(parity_words) == size, (k, start, "complete translate"))
            require(max(map(len, splits.values())) <= 2, (k, start, "split count"))
    return {"starts": count, "floor_survivors_at_or_above_clock": survivors}


def corridor_checks():
    quota_words = 0
    physical_words = 0
    data = []
    for k in range(2, 17):
        p = next(p for p in range(k + 1) if 3**p >= 2**k)
        block = max(1, k // 4)
        hits = Counter()
        endpoints = Counter()
        for positions in combinations(range(k), p):
            mask = sum(1 << i for i in positions)
            values = bars(k, p, mask)
            if all((values[t] + t * p) // k == (t * p) // k
                   for t in range(block, k, block)):
                rotated = rotate_at_minimum(k, mask, values)
                after = bars(k, p, rotated)
                require(min(after) == 0 and max(after) <= (2 * block + 2) * k,
                        (k, mask, "rotated corridor"))
                hits[rotated] += 1
                quota_words += 1
            if min(values) >= 0:
                grade, numerator = word_row(k, mask)
                residue = (-numerator * pow(3**p, -1, 2**k)) % 2**k
                _, endpoint = canonical(k, mask)
                endpoints[endpoint] += 1
                require(grade == p and numerator * 3 <= k * 3**p,
                        (k, mask, "real correction"))
                for high in (1, 4):
                    start = 2**k * high + residue
                    value = start
                    for i in range(k):
                        require(value % 2 == (mask >> i) & 1, (k, mask, "source"))
                        value = (3 * value + 1) // 2 if value % 2 else value // 2
                        require(value >= start, (k, mask, "source-relative floor"))
                    require(value == 3**p * high + endpoint, (k, mask, "endpoint"))
                physical_words += 1
        require(max(hits.values()) <= k, (k, "rotation multiplicity"))
        require(max(endpoints.values()) <= 1 + k // 3, (k, "physical fibre cap"))
        data.append({"k": k, "p": p, "chord_words": sum(endpoints.values()),
                     "chord_endpoints": len(endpoints),
                     "maximum_chord_multiplicity": max(endpoints.values())})
    return {"quota_words": quota_words, "physical_chord_words": physical_words,
            "rows": data}


if __name__ == "__main__":
    print(json.dumps({"exact_power_sums": moment_checks(),
                      "composition_words": finite_composition_rows(),
                      "corridor": corridor_checks(),
                      "translated_intervals": translated_intervals()}, indent=2))
