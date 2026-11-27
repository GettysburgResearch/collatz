"""Exact positive periodic points, directed carry comparisons and scalar thresholds."""
from fractions import Fraction
from hashlib import sha256
from math import gcd, lcm
import json


def require(test, message):
    if not test:
        raise ValueError(message)


def rotate(word, start):
    return word[start:] + word[:start]


def cycle(word):
    length = len(word)
    raw = 2 ** length - 3 ** sum(word)
    require(raw > 0, "positive raw determinant required")
    carry = 0
    for index, digit in enumerate(word):
        carry = 3 ** digit * carry + digit * 2 ** index
    factor = gcd(raw, carry)
    denominator = raw // factor
    initial = carry // factor
    state = initial
    states = []
    for digit in word:
        require(state % 2 == digit and gcd(state, denominator) == 1,
                "parity or reduced denominator changed")
        states.append(state)
        state = (3 ** digit * state + digit * denominator) // 2
    require(initial == state, "physical lap failed")
    return states, denominator


def geometry(count):
    return sum(Fraction(46, 29) ** power for power in range(count + 1))


def compare(first, second, a, qa, b, qb):
    require(len(first) == len(second) and first != second, "distinct aligned scripts required")
    if sum(first) < sum(second):
        return compare(second, first, b, qb, a, qa)
    length = len(first)
    denom = lcm(qa, qb)
    a = [x * (denom // qa) for x in a]
    b = [x * (denom // qb) for x in b]
    raises = sum(s < t for s, t in zip(first, second))
    mismatches = sum(s != t for s, t in zip(first, second))
    require(2 * raises <= mismatches, "incorrect directed mismatch count")
    scale = 3 ** raises
    anchor = min(range(length), key=a.__getitem__)
    for i in range(length):
        require(2 * b[i] + denom <= scale * (2 * a[i] + denom), "center comparison failed")
        require(a[i] != b[i], "two distinct scripts shared an aligned physical state")
    offset = 0
    while offset < length:
        k = offset
        while k < length and first[(anchor + k) % length] == second[(anchor + k) % length]:
            k += 1
        run = k - offset
        i = (anchor + offset) % length
        require((a[i] - b[i]) % (2 ** run) == 0, "common-run divisibility failed")
        require(2 ** (run + offset) <= 3 ** offset * scale * (a[anchor] + denom),
                "physical two-arm growth bound failed")
        offset = k + 1
    initial_bits = (scale * (a[anchor] + denom) - 1).bit_length()
    require(length + 1 <= (initial_bits + 1) * geometry(mismatches), "geometric budget failed")
    return mismatches


def primitive(word):
    return all(rotate(word, k) != word for k in range(1, len(word)))


def certify_thresholds():
    require(3 ** 29 < 2 ** 46 and 2 ** 3 < 3 ** 2, "rational logarithm brackets")
    require(137_500_000_000 > 2 ** 37, "published odd-period floor")
    checks = []
    for shift_cap, exponent, period_floor in [(40, 37, 3 * 2 ** 36),
                                             (40, 38, 2 ** 38),
                                             (132, 100, 2 ** 100)]:
        cost = 10 + 15 * (exponent + 1) + Fraction(4 * shift_cap, 5)
        upper = cost * geometry(shift_cap)
        require(upper < period_floor, "dyadic shell base case failed")
        require(cost + 15 < 2 * cost, "dyadic shell induction failed")
        checks.append(dict(mismatch_cap=shift_cap, shell=exponent, period_floor=period_floor,
                           upper_ceiling=-(-upper.numerator // upper.denominator)))
    return checks


def main():
    counts = {"primitive_necklaces": 0, "rotations": 0, "distinct_script_pairs": 0}
    for length in range(2, 14):
        words = []
        for mask in range(1, 2 ** length):
            word = tuple((mask >> k) & 1 for k in range(length))
            if 3 ** sum(word) >= 2 ** length:
                continue
            if any(rotate(word, k) <= word for k in range(1, length)):
                continue
            nums, q = cycle(word)
            counts["primitive_necklaces"] += 1
            for k in range(1, length):
                compare(word, rotate(word, k), nums, q, rotate(nums, k), q)
                counts["rotations"] += 1
            words.append((word, nums, q))
        for first_row, second_row in zip(words, words[1:]):
            w, a, qa = first_row
            v, b, qb = second_row
            compare(w, v, a, qa, b, qb)
            counts["distinct_script_pairs"] += 1
    trivial = (1, 0)
    require(cycle(trivial) == ([1, 2], 1), "trivial positive cycle")
    require(cycle((1, 1, 1, 0, 0)) == ([19, 31, 49, 76, 38], 5), "denominator-five control")
    sparse_controls = []
    for size in (41, 83, 167):
        ranks = sorted(range(size), key=lambda i: sha256(f'half-{i}'.encode()).digest())
        base = set(ranks[:size // 2])
        left = tuple(int(i in base) for i in range(size))
        right = tuple(1 - b if i == ranks[size // 2] else b for i, b in enumerate(left))
        word = left + right
        require(primitive(word), "small-order control not primitive")
        nums, q = cycle(word)
        h = compare(word, rotate(word, size), nums, q, rotate(nums, size), q)
        require(h == 2 and q > 1, "order-two control lost its sparse shift")
        sparse_controls.append(dict(length=2 * size, shift_order=2, mismatches=h,
                                    denominator_bits=q.bit_length()))
    length, grade = 485, 306
    ranked = sorted(range(length), key=lambda i: sha256(f'dense-{i}'.encode()).digest())
    ones = set(ranked[:grade])
    word = tuple(int(i in ones) for i in range(length))
    nums, q = cycle(word)
    distances = [sum(a != b for a, b in zip(word, rotate(word, k))) for k in range(1, length)]
    require(min(distances) >= 134 and min(nums) > q and q > 1, "high-distance control")
    dense = dict(length=length, grade=grade, all_shift_minimum=min(distances),
                 physical_minimum=str(Fraction(min(nums), q)), denominator=q)
    print(json.dumps(dict(counts=counts, thresholds=certify_thresholds(),
                          order_two=sparse_controls, high_distance=dense), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
