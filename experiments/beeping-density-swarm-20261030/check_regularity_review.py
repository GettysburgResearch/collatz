#!/usr/bin/env python3
"""Independent finite checks for the majority-parity and softened-clock review."""
from fractions import Fraction
from math import comb
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def step(n):
    return n // 2 if not n % 2 else (3 * n + 1) // 2


def majority(n, k):
    count = 0
    for _ in range(k):
        count += n % 2
        n = step(n)
    return int(2 * count > k)


def check_majority():
    rows = []
    anchors = {1: Fraction(1), 2: Fraction(2, 3), 3: Fraction(2, 7), 27: Fraction(1, 4)}
    for k in (1, 3, 5, 7, 9, 11, 13):
        m, period = (k - 1) // 2, 2 ** k
        table = [majority(n, k) for n in range(period)]
        mean = Fraction(sum(table), period)
        defect = Fraction(sum(abs(table[n % period] - table[step(n) % period]) for n in range(2 * period)), 2 * period)
        require(mean == Fraction(1, 2), "majority mean")
        expected = Fraction(comb(2 * m, m), 2 ** (2 * m + 1))
        require(defect == expected, "majority exact defect")
        row = {"K": k, "mean": str(mean), "defect": str(defect), "exact_formula": str(expected)}
        if period > max(anchors):
            patched = [Fraction(x) for x in table]
            for n, value in anchors.items():
                patched[n] = value
            patch_distance = sum(abs(a - b) for a, b in zip(table, patched)) / period
            patch_defect = sum(abs(patched[n % period] - patched[step(n) % period]) for n in range(2 * period)) / (2 * period)
            patch_mean = sum(patched) / period
            require(patch_distance <= Fraction(len(anchors), period), "anchor distance bound")
            require(abs(patch_mean - mean) <= patch_distance, "anchor mean bound")
            require(abs(patch_defect - defect) <= 2 * patch_distance, "anchor defect bound")
            row.update({"patched_mean": str(patch_mean), "patched_defect": str(patch_defect), "patch_L1": str(patch_distance)})
        rows.append(row)
    return rows


def tau(n):
    t = 0
    while n != 1:
        n = step(n)
        t += 1
        require(t <= 1000000, "bounded convergence test timed out")
    return t


def check_soft_clock():
    worst = Fraction(0)
    for n in range(2, 5001):
        t, b = tau(n), n.bit_length()
        successor = step(n)
        bp = successor.bit_length()
        require(tau(successor) == t - 1, "hitting time recurrence")
        r = Fraction(b, b + t)
        rp = Fraction(bp, bp + t - 1)
        defect = abs(rp - r)
        require(defect <= Fraction(1, b - 1), "rational-clock defect bound")
        for m in (1, 2, 4, 8):
            approximation = r if t <= m * b else Fraction(0)
            require(abs(r - approximation) <= Fraction(1, m + 1), "uniform cutoff error")
        worst = max(worst, defect)
    return {"starts": 4999, "worst_observed_absolute_defect": str(worst), "cutoff_multipliers": [1, 2, 4, 8]}


if __name__ == "__main__":
    print(json.dumps({"status": "PASS", "scope": "finite independent replay only; see handwritten review for all-input proofs", "majority": check_majority(), "soft_clock": check_soft_clock()}, indent=2))
