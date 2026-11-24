"""Exact scaled-word and full-period controls for the geometric gap law."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import json


def check(ok):
    if not ok:
        raise ValueError('exact dyadic scale control failed')


@lru_cache(maxsize=None)
def words(length, total):
    rows = []
    for cuts in combinations(range(1, total), length-1):
        stops = (0,) + cuts + (total,)
        gaps = tuple(b-a for a, b in zip(stops, stops[1:]))
        numerator = sum(3**i * 2**(total-stops[i+1]) for i in range(length))
        rows.append((gaps, Fraction(numerator, 2**total)))
    return rows


def residue(x, modulus):
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def main():
    stats = Counter()
    intervals = [(Fraction(0), Fraction(1)), (Fraction(1, 2), Fraction(1)),
                 (Fraction(1, 7), Fraction(2, 7))]
    for b in range(2, 6):
        for s in range(b, 2*b+3):
            for m in range(6):
                for lo, hi in intervals:
                    short = [(w, x) for w, x in words(b, s) if lo < x <= hi]
                    long = [(w, x) for w, x in words(b, s+m) if lo < 2**m*x <= hi]
                    expected = {((w[0]+m,) + w[1:], x / 2**m) for w, x in short}
                    check(set(long) == expected)
                    stats['complete_word_bijections'] += 1
                    stats['scaled_word_matches'] += len(long)
                    for j in range(1, 5):
                        mod = 3**j
                        counts = Counter(residue(x, mod) for _, x in short)
                        scaled = Counter(2**m * residue(x, mod) % mod for _, x in long)
                        check(counts == scaled)
                        stats['full_residue_histograms'] += 1
    # Use the numerator labels as exact real observations. This compares the
    # joint histogram with product counts, rather than just its two marginals.
    base = [(x, x) for _, x in words(4, 9) if 0 < x <= 1]
    check(len(base) > 1)
    real_counts = Counter(x for x, _ in base)
    for j in range(1, 7):
        mod = 3**j
        period = 2*3**(j-1)
        units = [z for z in range(mod) if z % 3]
        target = Counter({(x, z): count for x, count in real_counts.items() for z in units})
        for start in (0, 1, 13):
            actual = Counter((x, residue(z, mod)*pow(2, -m, mod) % mod)
                             for x, z in base for m in range(start, start+period))
            check(actual == target)
            stats['labelled_joint_product_histograms'] += 1
    for m in range(1, 8):
        check(words(1, m) == [((m,), Fraction(1, 2**m))])
        stats['empty_tail_boundary_controls'] += 1
    print(json.dumps(stats, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
