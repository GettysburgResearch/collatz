#!/usr/bin/env python3
"""Exact finite tests of the ordinary record map and ternary edge-flow balance."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def inverse(y, e):
    numerator = (y << e) - 1
    if numerator % 3:
        return None
    x = numerator // 3
    return x if x % 3 else None


def forward(x):
    v = 3 * x + 1
    e = (v & -v).bit_length() - 1
    return v >> e, e


def real_word(root, word):
    path = [root]
    for e in word:
        x = inverse(path[-1], e)
        if x is None:
            return None
        path.append(x)
    return path


def first_record_test():
    positive, with_loss, strict_max_ties = 0, 0, 0
    for root in (1, 5, 7, 11, 13, 17, 19, 23, 25, 31, 2 * 3**7 - 1):
        for word in product(range(1, 7), repeat=5):
            path = real_word(root, word)
            if path is None:
                continue
            values = [0]
            for e in word:
                values.append(values[-1] + 7 - 4 * e)
            record = max(range(len(values)), key=lambda j: (values[j], j))
            x, total = path[record], 0
            for j, e in enumerate(reversed(word[:record]), 1):
                x, observed = forward(x)
                check(e == observed, "wrong physical edge")
                total += observed
                check(4 * total <= 7 * j, "running maximum did not certify a prefix")
            check(x == root, "changed terminal root")
            for i in range(len(values)):
                passed = all(values[i] >= v for v in values[:i])
                total = 0
                actual = True
                for j, e in enumerate(reversed(word[:i]), 1):
                    total += e
                    actual = actual and 4 * total <= 7 * j
                check(passed == actual, "forward/reverse gate equivalence")
            positive += record > 0
            with_loss += 0 < record < len(word)
            strict_max_ties += values.count(max(values)) > 1
    check(positive > with_loss > 0 and strict_max_ties > 0, "missing records or ties")
    return positive, with_loss, strict_max_ties


def small_flow_test():
    # Exact two-gap policy with differently sized sets of available words.
    b, cap, lifts = 2, 6, 9
    mod = 3 ** (b + 1)
    units = [x for x in range(mod) if x % 3]
    policies = {}
    for residue in units:
        words = [w for w in product(range(1, cap + 1), repeat=b)
                 if real_word(residue, w) is not None]
        limit = min(sum(w) for w in words) + 2
        policies[residue] = [w for w in words if sum(w) <= limit]

    classes = (1, 2)
    transition = {i: Counter() for i in classes}
    for i in classes:
        xs = [x for x in units if x % 3 == i]
        for x in xs:
            for w in policies[x]:
                end = real_word(x, w)[-1] % 3
                transition[i][end] += Fraction(1, len(xs) * len(policies[x]))
    a, d = transition[1][2], transition[2][1]
    check(a and d, "fixture is not irreducible")
    pi = {1: d / (a + d), 2: a / (a + d)}

    # Work at a deeper output precision than the policy reads. To compare a
    # whole telescoping block there, add b further free ternary input digits.
    out_mod = lifts * mod
    in_mod = out_mod * 3 ** b
    per_class = in_mod // 3
    edges = defaultdict(Fraction)
    before, after = Counter(), Counter()
    for source in range(in_mod):
        if source % 3 == 0:
            continue
        ws = policies[source % mod]
        weight = pi[source % 3] / (per_class * len(ws))
        for w in ws:
            path = real_word(source, w)
            before[path[0] % out_mod] += weight
            after[path[-1] % out_mod] += weight
            for j, e in enumerate(w):
                edges[path[j] % out_mod, e] += weight / b
    check(before == after, "block lost unread-tail balance")
    row = Counter()
    for (x, e), mass in edges.items():
        row[x] += mass
        check(inverse(x, e) is not None, "flow charges an illegal edge")
    for x in range(out_mod):
        if x % 3 == 0:
            continue
        for e in range(1, cap + 1):
            check(edges[x, e] == edges[x % mod, e], "edge condition depends on hidden digits")
        check(row[x] == row[x % (mod // 3)], "stationary density has excess precision")

    # Incorrectly mixing two unrelated source and action marginals would charge
    # illegal edges; independently resampling a root residue would lose (3).
    forbidden = sum(1 for x in units for e in range(1, cap + 1) if inverse(x, e) is None)
    check(forbidden > 0 and sum(row.values()) == 1, "negative-control fixture")
    return sum(map(len, policies.values())), len(row), forbidden


def haar_count_test():
    checked_words = 0
    for b in range(1, 5):
        mod = 3 ** (b + 1)
        units = [x for x in range(1, mod) if x % 3]
        for word in product(range(1, 5), repeat=b):
            valid = sum(real_word(x, word) is not None for x in units)
            check(valid == 2, "wrong Haar average at a fixed word")
            checked_words += 1
    return checked_words


if __name__ == "__main__":
    positive, discarded, ties = first_record_test()
    choices, rows, forbidden = small_flow_test()
    print(f"{positive} nonzero records, {discarded} proper cuts, {ties} tied maxima")
    print(f"{choices} selected two-gap choices, {rows} balanced lifted rows, {forbidden} illegal pairs")
    print(f"{haar_count_test()} single-word ternary Haar counts")
