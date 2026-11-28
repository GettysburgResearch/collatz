"""Independent finite reciprocal row, marked-column, and first-passage controls."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import json
from math import comb
from check_line_shadow_structure import require


def landed(n, m):
    h, d = n, m
    require(h > 0 and d > 0 and d % 3, "invalid ternary input")
    word = []
    while h:
        bit = d % 2
        word.append(bit)
        h -= bit
        d, remainder = divmod(d + bit * 3**h, 2)
        require(remainder == 0 and (h == 0 or d % 3), "inexact native prefix")
    require(word[-1] and d % 3 != 2, "forbidden first mark")
    return tuple(word), d


@lru_cache(None)
def upper_support(k):
    return Fraction(3, 2)**k - 1


@lru_cache(None)
def tail(k, x):
    """P(Y_k > x); positivity gives an exact finite cutoff in the infinite branch sum."""
    if k == 0:
        return Fraction(int(x < 0))
    if x >= upper_support(k):
        return Fraction(0)
    if x < Fraction(1, 2) or x == Fraction(1, 2) and k > 1:
        return Fraction(1)
    require(x > Fraction(1, 2), "unhandled lower support endpoint")
    threshold = (x - Fraction(1, 2)) * 2 / 3
    total = Fraction(0)
    e = 1
    while threshold < upper_support(k-1):
        total += tail(k-1, threshold) / 2**e
        e += 1
        threshold *= 2
    return total


def column_controls(counts):
    cumulative = Counter()
    for n in range(1, 11):
        q = 3**n
        column = Counter()
        for m in range(1, (q+1)//2):
            if m % 3:
                word, N = landed(n, m)
                column[N] += Fraction(1, 2**len(word))
                counts["half_window_physical_sources"] += 1
        cumulative.update(column)
        bound = max(2, int(upper_support(n+1)) + 1)
        for N in range(1, bound + 1):
            if N % 3 == 2:
                require(column[N] == 0 and cumulative[N] == 0, "forbidden residue has mass")
                counts["forbidden_column_cases"] += 1
                continue
            require(column[N] == tail(n+1,N)-tail(n,N), "one-grade exact crossing failed")
            require(cumulative[N] == tail(n+1,N), "finite telescoping failed")
            counts["exact_crossing_cases"] += 1
            counts["positive_crossings"] += column[N] > 0
    return {str(n): str(cumulative[n]) for n in (1,3,4,6,7)}


def row_controls(counts):
    snapshots = []
    for n, first, size in ((4, 1, 80), (5, 18, 131), (5, 2**50, 610),
                           (6, 1, 728), (7, 21, 1100), (9, 1, 19682)):
        q = 3**n
        words = Counter()
        physical_weight = Fraction()
        for m in range(first,first+size):
            if m % 3:
                word, mark = landed(n,m)
                words[word] += 1
                physical_weight += Fraction(1,2**len(word))
                counts["row_physical_sources"] += 1
        for word, count in words.items():
            t = len(word)
            scale = Fraction(2*size, 3*2**t)
            require(abs(count-scale) <= 2, "word occupancy error exceeds absolute boundary")
        for t in range(n, min(n+6,13)):
            for positions in combinations(range(t-1), n-1):
                odds = set(positions) | {t-1}
                word = tuple(int(j in odds) for j in range(t))
                ideal = Fraction(3**n,4**t)
                require(ideal == Fraction(3,4)**n * Fraction(1,4)**(t-n),
                        "tilted iid weight")
                require(abs(words[word] - Fraction(2*size,3*2**t)) <= 2,
                        "occupancy error on unrealized word")
                counts["all_short_word_controls"] += 1
        l = (n*7)//5
        tail_weight = sum((Fraction(c,2**len(w)) for w,c in words.items() if len(w)>l),
                          Fraction())
        bound = (Fraction(size,2**l) + 1) * sum(
            Fraction(comb(l,g),2**(l+n-g)) for g in range(n))
        require(tail_weight <= bound, "weighted long-word cylinder majorant")
        snapshots.append(dict(grade=n, width=size, raw_mass=str(physical_weight),
                              asymptotic_scale=str(Fraction(2*size,3*q))))
    return snapshots


def main():
    counts = Counter()
    columns = column_controls(counts)
    rows = row_controls(counts)
    require(counts["positive_crossings"] > 20 and counts["all_short_word_controls"] > 1000,
            "missing nontrivial controls")
    print(json.dumps(dict(scope="Finite exact arithmetic; no asymptotic fitting",
                          counts=dict(counts), cumulative_marks_through_grade_10=columns,
                          selected_rows=rows), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
