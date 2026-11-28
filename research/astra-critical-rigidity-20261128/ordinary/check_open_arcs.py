"""Replay exact open-path carries, boundary products and the two terminal normalizations."""

from collections import Counter
from fractions import Fraction
from math import prod
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x, q):
    numerator = 3 * x + q
    exponent = (numerator & -numerator).bit_length() - 1
    require(x > 0 and x % 2 and exponent >= 1, "expected a positive odd state")
    return numerator >> exponent, exponent


def check_path(first, second, q, length, stats):
    rows = [[first], [second]]
    words = [[], []]
    for _ in range(length):
        if rows[0][-1] == rows[1][-1]:
            break
        for row, word in zip(rows, words):
            following, exponent = step(row[-1], q)
            row.append(following)
            word.append(exponent)
    if rows[0][-1] == rows[1][-1]:
        stats["truncated_meeting_controls"] += 1
        if not words[0]:
            return
        for row, word in zip(rows, words):
            row.pop()
            word.pop()
    p = len(words[0])
    if p < 2:
        return
    require(all(a != b for a, b in zip(*rows)), "an interior synchronized meeting was missed")
    upper = [max(a, b) + q for a, b in zip(*rows)]
    lower = [min(a, b) + q for a, b in zip(*rows)]
    drops = [max(Fraction(1), Fraction(a, b)) for a, b in zip(upper, upper[1:])]
    rises = [max(Fraction(1), Fraction(b, a)) for a, b in zip(upper, upper[1:])]
    require(prod(drops) * upper[-1] == prod(rises) * upper[0], "open variation endpoint identity")
    require(prod(rises) <= Fraction(3, 2)**p, "open growth ceiling")
    stats["open_paths"] += 1
    stats["different_total_divisions"] += sum(words[0]) != sum(words[1])
    stats["first_or_last_scale_decreased"] += upper[-1] < upper[0]
    marks = {i + 1 for i, (a, b) in enumerate(zip(*words)) if a != b}
    for additional in (set(), {p // 2}, set(range(2, p, 3))):
        cuts = sorted({0, p} | marks | additional)
        term_sum = [Fraction(rows[0][0]), Fraction(rows[1][0])]
        cumulative = [0, 0]
        carry_product = 1
        factors = 1
        for left, right in zip(cuts, cuts[1:]):
            block_length = right - left
            high = int(rows[1][left] > rows[0][left])
            B = sum(words[0][left:right-1]) + min(words[0][right-1], words[1][right-1])
            require((rows[high][left] - rows[1-high][left]) % 2**B == 0, "mixed final divisor")
            carry = prefix = 0
            for h in range(block_length):
                t = left + h
                require(rows[high][t] + q == upper[t], "higher track changed on a common interior")
                require(Fraction(2**prefix * upper[t], 3**h) <= rows[high][left] * (1 + q),
                        "shifted high-track bound")
                carry = 3 * carry + 2**prefix
                prefix += words[high][t]
                stats["true_high_prefixes"] += 1
            require(carry <= block_length * 3**block_length * (1 + q) * prod(drops[left:right]),
                    "one-envelope carry charge")
            carry_product *= q * carry
            factors *= q * (1 + q) * block_length
            for j in range(2):
                term_sum[j] += Fraction(q * carry * 2**cumulative[j], 3**right)
                cumulative[j] += sum(words[j][left:right])
                require(term_sum[j] == Fraction(2**cumulative[j] * rows[j][right], 3**right),
                        "initial and terminal prefix sums disagree")
            stats["different_high_tracks_at_exit"] += (rows[0][left] > rows[1][left]) != (
                rows[0][right] > rows[1][right])
        require(carry_product * upper[-1] <= upper[0] * Fraction(9, 2)**p * factors,
                "open aggregate carries with both boundary factors")
        joint = Fraction(rows[0][-1] * rows[1][-1] * carry_product, 3**(2*p))
        require(joint <= Fraction(upper[0] * lower[-1] * factors, 2**p),
                "terminal maximum cancellation in the two-place bound")
        stats["open_mesh_partitions"] += 1


def main():
    out = Counter()
    for q in (1, 5, 7, 13, 29, 61, 1021):
        for a in range(1, 96, 2):
            for b in (a + 2, 3*a, 5*a + 2):
                check_path(a, b, q, 19, out)
    for seed in (27, 31, 97, 703, 871, 6171):
        shifted = seed
        for _ in range(9):
            shifted = step(shifted, 1)[0]
            check_path(seed, shifted, 1, 27, out)
            out["same_ordinary_orbit_comparisons"] += 1
    require(all(out.values()) and len(out) == 8, "a required physical regime was missed")
    return dict(sorted(out.items()))


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
