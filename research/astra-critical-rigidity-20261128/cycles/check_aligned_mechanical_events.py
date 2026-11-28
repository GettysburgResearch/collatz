"""Exact aligned heights and native near-period transfer on physical rational cycles."""
from collections import Counter
from itertools import accumulate, product
from math import gcd
import json

from check_rotation_occupation import lifted, primitive_necklace, require


def verify(word, q, states, counts):
    period = len(word)
    clock = sum(word)
    divisor = gcd(clock, period)
    lag = period // divisor if divisor > 1 else pow(clock, -1, period)
    det = 2**clock - 3**period
    physical_distance = sum(a != word[(i+lag) % period] for i, a in enumerate(word))
    counts["cycles_with_reduced_clock" if divisor == 1 else "cycles_with_imprimitive_clock"] += 1
    for phase in range(period // divisor):
        offset = phase * divisor
        reference = [((i+1)*clock + offset) // period - (i*clock + offset) // period
                     for i in range(period)]
        discrepancies = [b-a for b, a in zip(reference, word)]
        partial = [0, *accumulate(discrepancies)]
        width = max(partial) - min(partial)
        changes = sum(d != 0 for d in discrepancies)
        ref_distance = sum(b != reference[(i+lag) % period]
                           for i, b in enumerate(reference))
        require(0 < lag < period and ref_distance <= 2, "proper mechanical shift")
        require(physical_distance <= 2*changes + ref_distance, "actual Hamming transfer")
        require(partial[-1] == 0 and width <= changes, "complete aligned prefix range")
        require(3*det*max(states) <= q * 2**(width+1) * period * 2**clock,
                "complete rational physical height bound")
        counts["distinct_aligned_references"] += 1
        counts["comparisons_with_one_dyadic_drop_of_two_or_more"] += min(discrepancies) <= -2
        counts["exactly_matching_references"] += changes == 0
        counts["zero_distance_mechanical_shifts"] += ref_distance == 0
        counts["two_distance_mechanical_shifts"] += ref_distance == 2


def main():
    counts = Counter()
    for period in range(2, 8):
        for word in product(range(1, 5), repeat=period):
            if sum(word) > 2*period or not primitive_necklace(word):
                continue
            actual = lifted(word)
            if actual is None:
                continue
            q, states = actual
            verify(word, q, states, counts)
    require(all(counts.values()) and len(counts) == 7, "all exact control cases occur")
    return counts


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
