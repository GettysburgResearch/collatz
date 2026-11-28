"""Exact finite controls for SPARSE_EDIT_INVERSE_REUNION.md."""

from collections import defaultdict
from dataclasses import dataclass
from functools import cache
from itertools import combinations
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


@dataclass(frozen=True)
class Word:
    gaps: tuple
    clock: int
    depth: int
    numerator: int


def words_up_to(max_clock):
    result = [Word((), 0, 0, 0)]
    for clock in range(1, max_clock + 1):
        for depth in range(1, clock + 1):
            for cuts in combinations(range(1, clock), depth - 1):
                ends = cuts + (clock,)
                gaps = tuple(b - a for a, b in zip((0,) + cuts, ends))
                numerator = sum(3**i * 2**(clock - end) for i, end in enumerate(ends))
                result.append(Word(gaps, clock, depth, numerator))
    return result


def legal_inverse(root, word):
    if root % 3 == 0:
        return None
    for exponent in word.gaps:
        numerator = (root << exponent) - 1
        if numerator % 3:
            return None
        root = numerator // 3
        if root % 3 == 0:
            return None
    return root


def valuation_3(number):
    require(number != 0, "valuation of zero")
    power = 0
    while number % 3 == 0:
        number //= 3
        power += 1
    return power


@cache
def min_signed_weight(residue, digits):
    if digits == 0:
        return 0
    modulus = 3**(digits - 1)
    choices = (trit for trit in range(-2, 3) if (residue - trit) % 3 == 0)
    return min(int(trit != 0) + min_signed_weight(((residue - trit) // 3) % modulus,
                                                  digits - 1) for trit in choices)


def check_decoding(words):
    grade_buckets = defaultdict(dict)
    for word in words:
        residue = word.numerator % 2**word.clock
        bucket = grade_buckets[word.depth, word.clock]
        require(residue not in bucket, "binary numerator collision")
        bucket[residue] = word
        if word.depth:
            require(0 < word.numerator < 3**word.depth * 2**(word.clock - word.depth),
                    "wrong numerator growth")
        start = -word.numerator * pow(3, -word.depth, 2**word.clock) % 2**word.clock
        for gap in reversed(word.gaps):
            require(start % 2 == 1, "missing odd start")
            start = (3 * start + 1) // 2
            for _ in range(gap - 1):
                require(start % 2 == 0, "missing even suffix")
                start //= 2
    return grade_buckets


def check_unequal_clocks(words):
    count = 0
    roots_tested = 0
    legal_reunions = 0
    for u in words:
        for v in words:
            if u.clock + v.clock > 5 or (u.depth, u.clock) == (v.depth, v.clock):
                continue
            n, m = u.depth, v.depth
            a = 3**m * 2**u.clock - 3**n * 2**v.clock
            val = valuation_3(a)
            difference = abs(u.clock - v.clock)
            expected = min(n, m) if n != m else n + (0 if difference % 2 else
                                                        1 + valuation_3(difference // 2))
            require(val == expected, "slope valuation")
            for digits in (1, 2, 3):
                period = 3**(digits + max(n, m))
                modulus = 3**(digits + n + m)
                for displacement in (-9, -2, 1, 3):
                    b = (3**m * u.numerator + 3**n *
                         (2**v.clock * displacement - v.numerator))
                    hits = 0
                    for x in range(period):
                        left = legal_inverse(x, u)
                        right = legal_inverse(x + displacement, v)
                        congruent = (a*x - b) % modulus == 0
                        if congruent:
                            hits += 1
                        if left is not None and right is not None:
                            same = (left - right) % 3**digits == 0
                            require(same == congruent, "legal reunion and congruence disagree")
                            legal_reunions += int(same)
                    roots_tested += period
                    common = 3**min(val, digits + n + m)
                    predicted = 0 if b % common else period * common // modulus
                    require(hits == predicted, "number of root cells")
                    count += 1
    return {"unequal_clock_congruences": count, "root_representatives_tested": roots_tested,
            "legal_reunions_detected": legal_reunions}


def check_equal_clocks(grade_buckets):
    count = 0
    forward_witnesses = 0
    for (n, clock), residue_map in grade_buckets.items():
        for u, v in combinations(residue_map.values(), 2):
            for digits in range(1, 12):
                precision = digits + n
                modulus = 3**precision
                required = ((v.numerator - u.numerator) * pow(2, -clock, modulus)) % modulus
                if required == 0:
                    continue
                edits = min_signed_weight(required, precision)
                exponent = (edits + 1) * clock - n
                require(3**max(0, digits - 2*edits) <= 2**exponent, "edit-cost bound")
                count += 1
                # Start both paths at forward-coded antecedents of terminal unit 1.
                x = (3**n + u.numerator) * pow(2, -clock, modulus) % modulus
                y = (3**n + v.numerator) * pow(2, -clock, modulus) % modulus
                require((y - x) % modulus == required, "forward displacement")
                left = legal_inverse(x, u)
                right = legal_inverse(y, v)
                require(left is not None and right is not None and
                        left % 3**digits == right % 3**digits == 1, "missing legal witness")
                physical_edits = sum((x // 3**j) % 3 != (y // 3**j) % 3
                                     for j in range(precision))
                require(physical_edits >= edits, "signed Hamming minimum")
                forward_witnesses += 1
    return {"equal_clock_sparse_bounds": count, "legal_same_endpoint_pairs": forward_witnesses}


def main():
    words = words_up_to(8)
    buckets = check_decoding(words)
    counts = {"inverse_words": len(words), "distinct_clock_depth_pairs": len(buckets)}
    counts.update(check_unequal_clocks(words))
    counts.update(check_equal_clocks(buckets))
    print(json.dumps(counts, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
