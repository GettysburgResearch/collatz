"""Exact finite physical word/mark tables and absolute-date coincidence ledger."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def integral_landing(m, h):
    clock = 0
    while h:
        if m % 2:
            m = (m + 3 ** (h - 1)) // 2
            h -= 1
        else:
            m //= 2
        clock += 1
    return clock, m


def ordinary_entry(n):
    t = 0
    while n not in (1, 2):
        require(t < 2000, "finite control ordinary entry deadline")
        n = step(n)
        t += 1
    return t, n - 1


def direct_state(m, h, clock):
    # Canonical reduced numerator and ternary exponent agree exactly iff values agree.
    for _ in range(clock):
        if h == 0:
            m = step(m)
        elif m % 2:
            m = (m + 3 ** (h - 1)) // 2
            h -= 1
        else:
            m //= 2
    return m, h


def word_mark_counts(n, lo, hi, bound):
    counts = Counter()
    for clock in range(n, bound + 1):
        for earlier in combinations(range(clock - 1), n - 1):
            odds = (*earlier, clock - 1)
            carry = sum((1 << t) * 3 ** (n - j - 1) for j, t in enumerate(odds))
            den = 1 << clock
            # Endpoint mark interval is F_w((lo,hi)); inverse numerator is 2^t N - C.
            left, right = 3 ** n * lo + carry, 3 ** n * hi + carry
            first = int(left // den) + 1
            last = -((-right) // den) - 1
            for mark in range(first, last + 1):
                if mark % 3 == 2:
                    continue
                source = den * mark - carry
                require(source % 3 and 3 ** n * lo < source < 3 ** n * hi, "word inverse")
                counts[clock, mark] += 1
    return counts


def main():
    rows = []
    total_sources = total_cells = absolute_checks = pair_checks = 0
    for n in range(1, 9):
        for lo, hi in ((Fraction(0), Fraction(1, 2)), (Fraction(1, 2), Fraction(3, 2)),
                       (Fraction(3), Fraction(5))):
            actual = []
            for m in range(int(3 ** n * lo) + 1, -((-3 ** n * hi) // 1)):
                if m % 3:
                    t, mark = integral_landing(m, n)
                    require(mark % 3 != 2, "ineligible mark")
                    actual.append((m, t, mark))
            finite = Counter((t, mark) for _, t, mark in actual if t <= 15)
            require(finite == word_mark_counts(n, lo, hi, 15), "complete finite word/mark slice")
            total_cells += len(finite)
            total_sources += len(actual)
            max_t = max((t for _, t, _ in actual), default=0)
            for H in (n + 2, 2 * n + 3, 4 * n + 11):
                observed, on, off, entry_dates = Counter(), Counter(), Counter(), {}
                weights = []
                for m, t, mark in actual:
                    # Common dyadic denominator for all unnormalized reciprocal weights.
                    weight = 1 << (max_t - t)
                    val, h = direct_state(m, n, H)
                    observed[val, h] += weight
                    enter, final = ordinary_entry(mark)
                    absolute_phase = (final - enter - t) % 2
                    if t + enter <= H:
                        require((val, h) == (1 + (absolute_phase + H) % 2, 0),
                                "wrong absolute cycle phase")
                        on[absolute_phase] += weight
                    else:
                        require(h != 0 or val > 2, "premature cycle entry")
                        key = val, h
                        require(entry_dates.setdefault(key, t + enter) == t + enter,
                                "coincidence with different later absolute entry dates")
                        off[key] += weight
                    weights.append(((val, h), weight))
                actual_second = sum(z * z for z in observed.values())
                require(actual_second == sum(z * z for z in on.values())
                        + sum(z * z for z in off.values()), "on/off decomposition")
                if len(weights) <= 22:
                    direct = sum(w * v for q, w in weights for r, v in weights if q == r)
                    require(direct == actual_second, "brute weighted ordered pair")
                    pair_checks += len(weights) ** 2
                absolute_checks += len(actual)
            rows.append([n, str(lo), str(hi), len(actual), len(finite), max_t])
    print(json.dumps({"scanned_reduced_sources": total_sources, "exact_clock_mark_cells": total_cells,
                      "absolute_date_state_checks": absolute_checks, "direct_pair_checks": pair_checks,
                      "rows_grade_interval_count_cells_maxclock": rows}, indent=2))


if __name__ == "__main__":
    main()
