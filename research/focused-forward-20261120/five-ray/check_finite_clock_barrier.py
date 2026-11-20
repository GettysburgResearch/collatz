#!/usr/bin/env python3
"""Exact bounded replays and arithmetic for FINITE_CLOCK_BARRIER.md.

This does not enumerate the enormous effective shell threshold, prove the
external logarithmic-form theorem, or decide any permanent failure set.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product

if not __debug__:
    raise SystemExit("Refusing optimized execution: exact checks require assertions")


def step(n):
    assert n > 0
    return (3 * n + 1) // 2 if n & 1 else n // 2


def path(n, clock):
    values, odd_counts, word = [n], [0], []
    for _ in range(clock):
        bit = n & 1
        word.append(bit)
        n = step(n)
        values.append(n)
        odd_counts.append(odd_counts[-1] + bit)
    return values, odd_counts, tuple(word)


def word_affine(word):
    odd_count, offset = 0, 0
    for j, bit in enumerate(word):
        if bit:
            odd_count += 1
            offset = 3 * offset + 2**j
    return len(word), odd_count, offset


def check_rational_margins():
    assert 2**19 < 3**12 < 2**24
    state_floor = F(49, 100) * F(19, 12) - F(3, 4)
    assert state_floor == F(31, 1200)
    assert state_floor - F(1, 40) == F(1, 1200)
    baker_bound = 18 * 24 * 81 * 32**5 * 8
    assert baker_bound == 9393093476352 < 10**13
    # Base cases; doubling 2**r dominates the linear factor r+2 thereafter.
    assert 40 * (10**13 + 1) * 62 < 2**60
    assert 10000 * 62 < 2**60
    # Every needed exponential/logarithmic comparison is in the written proof.
    exp2_partial = sum(F(2**j, fact(j)) for j in range(5))
    assert exp2_partial == 7 > 6
    assert F(2, 100**2) == F(1, 5000)
    assert F(1, 5000) - F(1, 10000) == F(1, 10000)
    return {
        "state_floor_lower": str(state_floor),
        "state_floor_margin": str(state_floor - F(1, 40)),
        "baker_constant_upper": baker_bound,
        "effective_log_size_threshold": 2**60,
    }


def fact(n):
    value = 1
    for k in range(2, n + 1):
        value *= k
    return value


def check_words():
    words = []
    all_words = 0
    for length in range(13):
        for word in product((0, 1), repeat=length):
            i, p, a = word_affine(word)
            assert 0 <= a <= 3**i - 2**i < 3**i
            all_words += 1
            if length <= 6:
                words.append((word, i, p, a))
    candidates = legal = 0
    for word1, i, p, a in words:
        for word2, j, q, b in words:
            coefficient = 2**j * 3**p - 5 * 2**i * 3**q
            rhs = 2**i * (3**q + b) - 2**j * a
            assert coefficient != 0
            assert abs(rhs) < 3 * 6**max(i, j)
            t = F(rhs, coefficient)
            if t.denominator == 1 and t > 0:
                candidates += 1
                t = int(t)
                assert t < 3 * 6**max(i, j)
                p1 = path(t, i)
                p2 = path(5 * t + 1, j)
                if p1[2] == word1 and p2[2] == word2:
                    assert p1[0][-1] == p2[0][-1]
                    legal += 1
    return {
        "affine_words": all_words,
        "word_pairs": len(words) ** 2,
        "positive_integral_equation_candidates": candidates,
        "legally_realized_meeting_word_pairs": legal,
    }


def check_intervals():
    records = []
    total_far = total_shell = 0
    for h in range(1, 13):
        size = 2**h
        lower = 4 * 6**h
        labels = Counter()
        unresolved = 0
        for t in range(lower, lower + size):
            a, aq, _ = path(t, h)
            b, bq, _ = path(5 * t + 1, h)
            assert set(a).isdisjoint(b)
            unresolved += 1
            labels[(a[-1], aq[-1], b[-1], bq[-1])] += 1
        assert unresolved == size
        total_far += size
        # Marginal uniformity of the two h-bit words: no arm independence is
        # assumed. Also record actual finite-clock outcomes in a natural shell.
        lower_words, upper_words = set(), set()
        shell_unresolved = 0
        horizon = 7 * h // 4
        for t in range(size, 2 * size):
            a, _, aw = path(t, horizon)
            b, _, bw = path(5 * t + 1, horizon)
            lower_words.add(aw[:h])
            upper_words.add(bw[:h])
            shell_unresolved += set(a).isdisjoint(b)
        assert len(lower_words) == len(upper_words) == size
        total_shell += size
        records.append((h, size, len(labels), max(labels.values()),
                        unresolved, horizon, shell_unresolved))
    return records, total_far, total_shell


def check_returns():
    count = 0
    for u in range(128):
        for source, target in ((64 * u + 11, 27 * u + 5),
                               (64 * u + 35, 9 * u + 5)):
            a, aq, _ = path(source, 6)
            b, bq, _ = path(5 * source + 1, 6)
            assert a[-1] == target
            assert b[-1] == 5 * target + 1
            assert aq[-1] == bq[-1]
            count += 1
    return count


def negative_controls():
    # A missing prime-5 incompatibility condition invalidates FR-001.
    t = 25
    assert t > 3 * 6
    assert step(t) == step(3 * t + 1)
    # Finite-clock failure is not a permanent failure. This is in I_2.
    t = 24
    a = path(t, 1)[0]
    b = path(5 * t + 1, 1)[0]
    assert set(a).isdisjoint(b)
    a_long = path(t, 400)[0]
    b_long = path(5 * t + 1, 400)[0]
    assert 1 in a_long and 1 in b_long
    return {
        "compatible_slope_meeting": (t + 1, 3 * (t + 1) + 1, 1, 1),
        "short_unresolved_but_later_convergent":
            (t, 5 * t + 1, a_long.index(1), b_long.index(1)),
    }


def main():
    print("RATIONAL MARGINS", check_rational_margins())
    print("WORD REPLAY", check_words())
    records, far, shell = check_intervals()
    print("h N joint_labels max_fiber far_unresolved shell_clock shell_unresolved")
    for record in records:
        print(*record)
    print("EXPLICIT FAR PARAMETERS", far)
    print("NATURAL SHELL PARAMETERS", shell)
    print("PAIRED RETURN REPLAYS", check_returns())
    print("NEGATIVE CONTROLS", negative_controls())
    print("PASS: bounded exact checks only; no permanent five-ray claim")


if __name__ == "__main__":
    main()
