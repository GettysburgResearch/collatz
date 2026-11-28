"""Exact controls for actual block sums, their canonical width and signed height transfer."""
from collections import Counter
from fractions import Fraction
from itertools import accumulate, product
from math import gcd
import json

from check_rotation_occupation import lifted, primitive_necklace, require


def cycle(word, stats):
    p = len(word)
    A = sum(word)
    if A >= 2*p or (1 << A) <= 3**p:
        return
    q, states = lifted(word)
    stats["primitive_positive_rational_cycles"] += 1
    stats["cycles_with_proper_denominator_cancellation"] += 1 < q < (1 << A)-3**p
    stats["cycles_with_noncoprime_clocks"] += gcd(p, A) > 1
    prefixes = list(accumulate(word, initial=0))
    start = max(range(p), key=lambda i: p*prefixes[i]-i*A)
    word = word[start:] + word[:start]
    states = states[start:] + states[:start]
    sums = list(accumulate(word+word, initial=0))
    grades = [i*A//p-sums[i] for i in range(p)]
    require(min(grades) == 0, "canonical discrepancy root")
    W = max(grades)
    require(3*((1 << A)-3**p)*max(states) <= p*(1 << (A+W+1))*q,
            "true physical rational maximum from canonical discrepancy")
    lap = Fraction(1 << A, 3**p)
    for h in range(1, p):
        v = h*A//p + 1
        det = p*v-h*A
        L = [sums[i+h]-sums[i] for i in range(p)]
        n = sum(value != v for value in L)
        s = sum(word[i] != word[(i+h) % p] for i in range(p))
        require(sum(L) == h*A, "cyclic mean clock in a native window")
        require(all(L[(i+1) % p]-L[i] == word[(i+h) % p]-word[i] for i in range(p)),
                "true derivative through the period seam")
        require(all(s <= 2*sum(value != target for value in L) for target in set(L)|{v}),
                "arbitrary modal target controls the native shift mismatch")
        overlap = sum(L[i] != v and i*A % p < det for i in range(p))
        require(W <= n+det-1-overlap <= n+det-2,
                "attributed canonical-width theorem on the exact window")
        stats["upper_windows"] += 1
        stats["farey_parent_windows"] += det == 1
        stats["nontrivial_bounded_order_windows"] += p//gcd(h, p) in (2, 3)
        if len(set(L)) == 2:
            gap = max(L)-min(L)
            native_variation = sum(abs(word[(i+h) % p]-word[i]) for i in range(p))
            require(gap*s == native_variation <= 2*(A-p), "two count levels charge every jump")
            stats["two_value_windows"] += 1
            stats["two_value_windows_with_gap_above_one"] += gap > 1
        for i, cost in enumerate(L):
            j = (i+h) % p
            partial = Fraction((1 << cost)*states[j], 3**h*states[i])
            require(1 < partial < lap, "partial gain lies strictly inside full positive gain")
            centered = Fraction(1 << (p*cost), 1 << (h*A))
            ratio = Fraction(states[i], states[j])**p
            require(ratio/lap**p <= centered <= ratio*lap**p, "both signs of count error")
            if states[i]*2 <= states[j]:
                require(centered <= (lap/2)**p, "negative tail at a lower start")
                stats["factor_two_low_starts"] += 1
            if states[j]*2 <= states[i]:
                require(centered >= (2/lap)**p, "positive tail at a lower end")
                stats["factor_two_low_ends"] += 1
            stats["physical_windows_with_both_error_bounds"] += 1


def main():
    stats = Counter()
    for p in range(2, 10):
        alphabet = (1, 2, 3, 4) if p <= 6 else (1, 2, 3) if p <= 8 else (1, 2)
        for word in product(alphabet, repeat=p):
            if primitive_necklace(word):
                cycle(word, stats)
    for word in ((1,)*6 + (6, 1, 2, 2), (1, 2)*6 + (6,),
                 (1,)*7 + (7, 2, 2, 2), (1,)*9+(10,), (1, 1, 1, 1, 4, 4)):
        require(primitive_necklace(word), "structured primitive control")
        cycle(word, stats)
    require(len(stats) == 11 and all(stats.values()), "every named edge control occurred")
    return stats


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
