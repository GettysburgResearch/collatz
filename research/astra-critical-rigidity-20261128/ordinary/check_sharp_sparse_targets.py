"""Exact finite cylinder probabilities and marked true odd returns."""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json


def require(value, reason):
    if not value:
        raise ValueError(reason)


def stationary_rows(depth):
    row = {0: Fraction(1)}
    rows = [row]
    for d in range(1, depth + 1):
        modulus = 3**d
        period = 2 * 3**(d - 1)
        require(pow(2, period, modulus) == 1, "geometric denominator period")
        next_row = Counter()
        for a in range(1, period + 1):
            prob = Fraction(2**(period - a), 2**period - 1)
            for x, mass in row.items():
                y = (3 * x + 1) * pow(2, -a, modulus) % modulus
                next_row[y] += prob * mass
        require(sum(next_row.values()) == 1, "normalized scalar law")
        projected = Counter()
        for y, mass in next_row.items():
            projected[y % (modulus // 3)] += mass
        require(projected == row, "exact conditional marginals")
        row = next_row
        rows.append(row)
    return rows


def residue(gaps):
    mod = 3 ** len(gaps)
    x = 0
    for a in gaps:
        x = (3 * x + 1) * pow(2, -a, mod) % mod
    return x


def in_interval(J, k, s):
    # 2^(J-1/2) <= 2^s/3^k <= 2^(J-1/4), using integers.
    left = 3 ** (4 * k)
    power = 2 ** (4 * s)
    return (left << (4 * J - 2)) <= power <= (left << (4 * J - 1))


def composition_count(total, parts):
    if not parts:
        return int(total == 0)
    return comb(total - 1, parts - 1) if total >= parts else 0


def negative_binomial_checks():
    tested = 0
    selected = 0
    for k in range(1, 7):
        for d in range(1, min(k, 3) + 1):
            for total in range(k, 15):
                suffix = Counter()
                whole = Counter()
                direct = [((), total)]
                while direct:
                    w, remaining = direct.pop()
                    if len(w) == k:
                        if remaining == 0:
                            whole[residue(w) % 3**d] += 1
                        continue
                    for a in range(1, remaining - (k - len(w) - 1) + 1):
                        direct.append((w + (a,), remaining - a))
                for gaps in product(range(1, total + 1), repeat=d):
                    b = sum(gaps)
                    if b <= total:
                        suffix[residue(gaps)] += composition_count(total - b, k - d)
                require(whole == +suffix, "reversed d-gap statistic with free NB front")
                require(sum(whole.values()) == composition_count(total, k), "all words on this slice")
                selected += sum(whole.values())
                tested += 1
    return tested, selected


def actual_checks(rows):
    records = []
    for J in [3, 5, 7]:
        Y = 1536
        lo = (2**J) * Y
        # Use [1,1+1/8] inside [1,2^(1/4)].
        hi = lo + lo // 8
        for d in (1, 2, 3):
            A = {max(rows[d], key=rows[d].get)}
            hits = 0
            marks = 0
            for n in range(lo + 1, hi + 1, 2):
                x = n
                s = 0
                gaps = []
                marked = False
                for k in range(1, 4 * J + 5):
                    raw = 3 * x + 1
                    a = (raw & -raw).bit_length() - 1
                    x = raw >> a
                    s += a
                    gaps.append(a)
                    if k >= d and in_interval(J, k, s):
                        require(x % 3**d == residue(gaps[-d:]), "last genuine odd gaps")
                        if x % 3**d in A:
                            require(Y <= x <= 2 * Y, "finite homogeneous-scale margin")
                            marked = True
                            marks += 1
                hits += marked
            records.append([J, d, next(iter(A)), hi // 2 - lo // 2, hits, marks])
    return records


if __name__ == "__main__":
    rows = stationary_rows(4)
    tested, words = negative_binomial_checks()
    base = Path(__file__).resolve().parent
    names = [Path(__file__).name, "SHARP_SPARSE_TARGET_EXPONENT.md"]
    print(json.dumps({"scope": "Finite exact identities and physical probes; no asymptotic inference",
                      "sha256": {n: sha256((base / n).read_bytes()).hexdigest() for n in names},
                      "stationary_quadratic_energies": [str(3**k * sum(p*p for p in r.values()))
                                                         for k, r in enumerate(rows)],
                      "NB_slices": tested, "NB_words": words, "odd_marks": actual_checks(rows)},
                     sort_keys=True, indent=2))
