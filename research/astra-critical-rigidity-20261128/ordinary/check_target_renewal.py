"""Exact stopped word inverses, blocked crossing laws and prefix transport."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from check_line_shadow_structure import require
from check_reciprocal_landing import landed, tail, upper_support


def interior(n, lo, hi):
    den = 3**n
    low, high = lo * den, hi * den
    return (m for m in range(low.numerator//low.denominator + 1,
                             (high.numerator+high.denominator-1)//high.denominator)
            if m % 3)


def mapped(word, lo, hi):
    for odd in word:
        lo = ((3 if odd else 1) * lo + odd) / 2
        hi = ((3 if odd else 1) * hi + odd) / 2
    return lo, hi


def blocked(counts):
    for k in (2, 3, 4):
        for n in range(1, 7):
            left = Counter()
            for m in interior(n, Fraction(), upper_support(k)):
                w, mark = landed(n, m)
                left[mark] += tail(k, Fraction(m, 3**n)) / 2**len(w)
                counts["weighted_blocked_sources"] += 1
            cap = int(upper_support(n+k)) + 1
            for mark in range(1, cap+1):
                expected = tail(n+k, mark) - tail(n, mark) if mark % 3 != 2 else 0
                require(left[mark] == expected, "grade-blocked column identity")
                counts["exact_blocked_columns"] += 1
                counts["nonzero_blocked_columns"] += expected > 0


def profile(counts):
    for lo, hi in ((Fraction(0), Fraction(7, 8)),
                   (Fraction(7, 3), Fraction(29, 9)),
                   (Fraction(11, 4), Fraction(19, 4))):
        for n in range(1, 6):
            prefix = Counter()
            for m in interior(n, lo, hi):
                w, mark = landed(n, m)
                L, Y = Fraction(1), Fraction()
                for bit in w:
                    L *= Fraction(3 if bit else 1, 2)
                    Y = ((3 if bit else 1) * Y + bit) / 2
                require(L == Fraction(3**n, 2**len(w)) and
                        (mark-Y)/L == Fraction(m, 3**n), "native marked inverse")
                require(Fraction(1, 2**len(w))*L == Fraction(3**n, 4**len(w)),
                        "exact tilted likelihood ratio")
                counts["joint_native_marks"] += 1
                for length in range(1, min(len(w)-1,4)+1):
                    if sum(w[:length]) < n:
                        prefix[w[:length], mark] += Fraction(1, 2**len(w))
            for length in range(1, 5):
                for w in product((0,1), repeat=length):
                    g = sum(w)
                    if g >= n:
                        continue
                    lower, upper = mapped(w, lo, hi)
                    suffix = Counter()
                    for m in interior(n-g,lower,upper):
                        rem, mark = landed(n-g,m)
                        suffix[mark] += Fraction(1,2**(length+len(rem)))
                    physical = {mark: mass for (w0,mark),mass in prefix.items() if w0 == w}
                    require(physical == suffix, "whole physical prefix transport")
                    counts["all_prefix_transport_cases"] += 1
                    counts["positive_prefix_transport_cases"] += bool(suffix)


def main():
    counts = Counter()
    blocked(counts)
    profile(counts)
    require(counts["nonzero_blocked_columns"] > 70 and
            counts["positive_prefix_transport_cases"] > 200, "thin finite coverage")
    print(json.dumps(dict(scope="Exact finite blocked identities and physical prefix transport",
                          counts=dict(counts)), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
