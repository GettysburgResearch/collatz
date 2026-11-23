#!/usr/bin/env python3
"""Bounded exact controls for CRITICAL_CARRY_TRANSFER.md; not a global proof."""

from collections import Counter
from fractions import Fraction
from math import comb
import json


def positive_words(total, length):
    if length == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - length + 2):
        for tail in positive_words(total - first, length - 1):
            yield (first,) + tail


def carry(word):
    value = 0
    clock = 0
    for gap in word:
        value = 3 * value + (1 << clock)
        clock += gap
    return value


def balanced(word):
    m, total = len(word), sum(word)
    prefix = 0
    for i, gap in enumerate(word, 1):
        prefix += gap
        if m * prefix > total * i:
            return False
    return True


def strip(word, slack):
    m = len(word)
    total = sum(word)
    critical = (3**m).bit_length() - 1
    if abs(total - critical) > slack:
        return False
    prefix = 0
    for i, gap in enumerate(word, 1):
        prefix += gap
        if (1 << prefix) > (1 << slack) * 3**i:
            return False
    return True


def ordinary_witness(word):
    total, m = sum(word), len(word)
    modulus = 1 << (total + 1)
    start = (((1 << total) - carry(word)) * pow(3**m, -1, modulus)) % modulus
    if start == 0:
        start += modulus
    while start % 3 == 0:
        start += modulus
    x = start
    for gap in word:
        z = 3 * x + 1
        actual = (z & -z).bit_length() - 1
        if actual != gap:
            raise AssertionError((word, start, gap, actual))
        x = z >> gap
        if not (x > 0 and x % 2 == 1 and x % 3 != 0):
            raise AssertionError((word, start, x))
        if balanced(word) and x < start:
            raise AssertionError((word, start, x, "lost prefix floor"))
    if (1 << total) * x != 3**m * start + carry(word):
        raise AssertionError((word, start, x, "affine identity"))


def actual_prefix(start):
    states, gaps, seen = [], [], set()
    x = start
    while x not in seen:
        seen.add(x)
        states.append(x)
        z = 3 * x + 1
        gap = (z & -z).bit_length() - 1
        y = z >> gap
        if y in seen:
            break
        gaps.append(gap)
        x = y
    return states, gaps


def check():
    exact_rows = []
    total_replays = 0
    for m in range(1, 13):
        critical = (3**m).bit_length() - 1
        words = list(positive_words(critical, m))
        if len(words) != comb(critical - 1, m - 1):
            raise AssertionError((m, "composition count"))
        good = [w for w in words if balanced(w)]
        if m * len(good) < len(words):
            raise AssertionError((m, "rotation count"))
        for w in words:
            if not any(balanced(w[i:] + w[:i]) for i in range(m)):
                raise AssertionError((m, w, "missing balanced rotation"))
        carries = [carry(w) for w in words]
        if len(set(carries)) != len(words):
            raise AssertionError((m, "complete carry decoder"))
        modulus = 3**m
        inverse = pow(2, -critical, modulus)
        counts = Counter((carry(w) * inverse) % modulus for w in good)
        bound = 1 + m // 3
        if max(counts.values()) > bound:
            raise AssertionError((m, "reference fiber"))
        if any(3 * carry(w) > m * modulus for w in good):
            raise AssertionError((m, "complete carry size"))
        collision = Fraction(sum(v * v for v in counts.values()), len(good) ** 2)
        if collision > Fraction(bound, len(good)):
            raise AssertionError((m, "reference collision"))
        for w in good:
            ordinary_witness(w)
            total_replays += 1
        exact_rows.append({
            "m": m,
            "A": critical,
            "all_words": len(words),
            "balanced_words": len(good),
            "max_endpoint_multiplicity": max(counts.values()),
            "proved_fiber_bound": bound,
            "collision": str(collision),
        })

    strip_checks = 0
    for m in range(1, 9):
        critical = (3**m).bit_length() - 1
        for slack in range(3):
            words = [
                w
                for total in range(max(m, critical - slack), critical + slack + 1)
                for w in positive_words(total, m)
                if strip(w, slack)
            ]
            modulus = 3**m
            counts = Counter(
                (carry(w) * pow(2, -sum(w), modulus)) % modulus for w in words
            )
            bound = (2 * slack + 1) * (1 + (m * (1 << slack)) // 3)
            if max(counts.values()) > bound:
                raise AssertionError((m, slack, "strip fiber"))
            strip_checks += 1

    states, gaps = actual_prefix(41)
    occurrence_checks = 0
    for end in range(2, len(states)):
        for m in range(1, min(end, 8) + 1):
            for slack in range(3):
                modulus = 3**m
                full = Counter(x % modulus for x in states[:end + 1])
                word_counts = Counter()
                selected_endpoints = Counter()
                for j in range(m, end + 1):
                    w = tuple(gaps[j - m:j])
                    if strip(w, slack):
                        word_counts[w] += 1
                        selected_endpoints[states[j] % modulus] += 1
                retained = sum(word_counts.values())
                omitted = end + 1 - retained
                bound = (2 * slack + 1) * (1 + (m * (1 << slack)) // 3)
                word_energy = sum(c * c for c in word_counts.values())
                retained_energy = sum(c * c for c in selected_endpoints.values())
                full_energy = sum(c * c for c in full.values())
                if retained_energy > bound * word_energy:
                    raise AssertionError((end, m, slack, "weighted fiber consumer"))
                # Rational consequence of the exact square-root bound (16).
                if full_energy > 2 * bound * word_energy + 2 * omitted * omitted:
                    raise AssertionError((end, m, slack, "omitted mass consumer"))
                occurrence_checks += 1

    return {
        "status": "passed",
        "scope": "bounded exact arithmetic only; no escaping orbit is sampled",
        "exact_total_rows": exact_rows,
        "ordinary_positive_unit_replays": total_replays,
        "strip_cases": strip_checks,
        "actual_source": 41,
        "actual_injective_prefix_states": len(states),
        "actual_weighted_occurrence_cases": occurrence_checks,
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
