#!/usr/bin/env python3
"""Exact bounded checks for PERSISTENT_DEFECT_CLASSES.md.

No search result is extrapolated to an infinite family. An unresolved ordinary
path raises an error. Only Python's standard library is used.
"""

from fractions import Fraction
import json


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


META = {1: (0, 0)}


def first_hit(n, cap=10000):
    path = []
    seen = set()
    x = n
    while x not in META:
        if len(path) >= cap or x in seen:
            raise AssertionError(("unresolved ordinary path", n, len(path), x))
        seen.add(x)
        path.append(x)
        x = step(x)
    d, a = META[x]
    for x in reversed(path):
        d += 1
        a += x % 2
        META[x] = (d, a)
    return META[n]


def defect(n):
    d, a = first_hit(n)
    return d - 2 * a


def augmented(n, h):
    x, a = n, 0
    for _ in range(h):
        a += x % 2
        x = step(x)
    return a, x


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def check_defect_identity():
    checked = 0
    for n in range(1, 2049):
        k = defect(n)
        x, a = n, 0
        for h in range(33):
            assert k == h - 2 * a + defect(x), (n, h)
            checked += 1
            a += x % 2
            x = step(x)
    return checked


def check_product_and_positive_minima():
    products = 0
    for n in range(1, 2049):
        x, product = n, Fraction(1)
        while x != 1:
            if x % 2:
                product *= Fraction(4 * x, 3 * x + 1)
            x = step(x)
        k = defect(n)
        power = Fraction(2**k) if k >= 0 else Fraction(1, 2 ** (-k))
        assert Fraction(n) / power == product
        if n & (n - 1):
            assert product >= Fraction(5, 4)
        products += 1

    candidates = {}
    for k in range(17):
        if k % 2 == 0:
            candidates[k] = 2**k
        elif k == 1:
            candidates[k] = 7
        else:
            candidates[k] = 5 * 2 ** (k - 2)
    bound = max(candidates.values())
    minima = {}
    for n in range(1, bound + 1, 3):
        minima.setdefault(defect(n), n)
    for k, n in candidates.items():
        assert n % 3 == 1 and defect(n) == k
        assert minima[k] == n, (k, minima[k], n)
    return {"products": products, "nonnegative_classes": len(candidates),
            "minimum_census_bound": bound}


NEGATIVE = {
    -1: (334, 45, 23), -2: (223, 46, 24), -3: (466, 55, 29),
    -4: (175, 52, 28), -5: (274, 59, 32), -6: (103, 56, 31),
    -7: (91, 59, 33), -8: (142, 66, 37), -9: (94, 67, 38),
    -10: (82, 70, 40), -11: (31, 67, 39), -12: (487, 90, 51),
}


def check_negative_minima():
    minima = {}
    for n in range(1, 488, 3):
        minima.setdefault(defect(n), n)
    for k, (n, d, a) in NEGATIVE.items():
        assert minima[k] == n, (k, minima[k], n)
        assert first_hit(n) == (d, a)
        assert d - 2 * a == k
    return {"classes": len(NEGATIVE), "census_H_sources": 163,
            "largest_source": 487}


def check_eventual_classes_and_prefix_filter():
    groups = {}
    comparisons = 0
    for n in range(1, 1501, 3):
        k = defect(n)
        if k in groups:
            m = groups[k]
            h = max(first_hit(n)[0], first_hit(m)[0])
            assert augmented(n, h) == augmented(m, h)
            assert augmented(n, h + 1) == augmented(m, h + 1)
            comparisons += 2
        else:
            groups[k] = n

    persistent = {1, 4, 7, 10, 16, 40, 64, 160, 256, 640, 1024}
    persistent.update(n for n, _, _ in NEGATIVE.values())
    prefix_states = 0
    for h in range(13):
        least = {}
        for r in range(2**h):
            n = 1 + 3 * r
            pair = augmented(n, h)
            least.setdefault(pair, n)
            if n in persistent:
                assert least[pair] == n, (n, h, least[pair])
            prefix_states += 1
    # Explicit control: a larger member of the same defect class is discarded.
    assert defect(13) == defect(10) == 3
    assert augmented(13, 7) == augmented(10, 7)
    # A tempting unrestricted-positive minimum would be wrong for k=1.
    assert defect(3) == defect(7) == 1 and 3 % 3 != 1
    return {"eventual_pair_checks": comparisons,
            "prefix_source_depth_pairs": prefix_states,
            "prefix_depth_max": 12, "negative_controls": 2}


def check_fibonacci_bound():
    checks = 0
    for target in range(1, 101):
        preimages = {target}
        for h in range(13):
            bound = (1 if target % 3 == 0 else
                     fibonacci(h + 1) if target % 3 == 1 else
                     fibonacci(h + 2))
            assert len(preimages) <= bound, (target, h, len(preimages), bound)
            assert all(augmented(n, h)[1] == target for n in preimages)
            checks += 1
            new = set()
            for n in preimages:
                new.add(2 * n)
                if n % 3 == 2:
                    m = (2 * n - 1) // 3
                    assert m > 0 and m % 2 == 1
                    new.add(m)
            preimages = new
    return {"target_depth_checks": checks, "targets": 100, "depth_max": 12}


def check_class_constructions():
    checks = 0
    for t in range(1, 1000, 2):
        if t % 3 == 0:
            continue
        candidates = [e for e in range(1, 7) if (2**e * t - 4) % 9 == 0]
        assert len(candidates) == 1
        e = candidates[0]
        child = (2**e * t - 1) // 3
        assert child > 0 and child % 2 == 1 and child % 3 == 1
        assert defect(child) == defect(t) + e - 2
        if t % 3 == 1:
            assert defect(4 * t) == defect(t) + 2
            assert (8 * t + 2) % 3 == 1
            assert defect(8 * t + 2) == defect(t) + 3
        checks += 1
    return {"odd_unit_sources": checks}


def check_forward_closing_fixture():
    rows = []
    for t in range(1, 33, 2):
        if t % 3 == 0:
            continue
        d, a = first_hit(t)
        q = 5 * d - 8 * a
        assert q <= 1 or 2 ** (q - 1) <= t**5, (t, d, a, q)
        rows.append([t, d, a, q])
    assert len(rows) == 11
    return {"ordinary_units": 11, "exact_log_free_inequalities": 11,
            "rows": rows}


if __name__ == "__main__":
    result = {
        "status": "PASS",
        "defect_identity_checks": check_defect_identity(),
        "product_and_nonnegative": check_product_and_positive_minima(),
        "negative_minima": check_negative_minima(),
        "persistent_filter": check_eventual_classes_and_prefix_filter(),
        "preimage_bound": check_fibonacci_bound(),
        "class_constructions": check_class_constructions(),
        "forward_closing_fixture": check_forward_closing_fixture(),
        "scope": "Exact bounded arithmetic; infinite claims require written proofs; "
                 "negative-class existence for all integers uses the stated external input.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
