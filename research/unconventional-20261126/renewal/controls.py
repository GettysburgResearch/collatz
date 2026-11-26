"""Exact integer controls for renewal counting, endpoint restrictions and height caps."""

from fractions import Fraction
from functools import cache
from itertools import product
from math import comb
import json


def floor_alpha(length):
    return (3**length).bit_length() - 1


def ladder_counts(limit):
    """First-crossing dynamic program, with each unrestricted gap summed by prefix."""
    clock_limit = floor_alpha(limit)
    previous = [0] * (clock_limit + 1)
    previous[0] = 1
    counts = [0]
    for length in range(1, limit + 1):
        next_row = [0] * (clock_limit + 1)
        crossing = 0
        running = 0
        for clock in range(1, clock_limit + 1):
            running += previous[clock - 1]
            if clock <= floor_alpha(length):
                crossing += running
            else:
                next_row[clock] = running
        counts.append(crossing)
        previous = next_row
    return counts


def pressure_checks(limit):
    counts = ladder_counts(limit)
    unrestricted = [0] + [comb(floor_alpha(m), m) for m in range(1, limit + 1)]
    for m in range(1, limit + 1):
        rhs = unrestricted[m] - sum(counts[k] * unrestricted[m - k] for k in range(1, m))
        assert m * counts[m] == rhs
        assert bool(counts[m]) == (m == 1 or floor_alpha(m) - floor_alpha(m - 1) == 2)
        if m >= 2 and counts[m]:
            assert counts[m] * (m - 1) >= comb(floor_alpha(m) - 2, m - 2)
    return {"verified_lengths": limit, "feasible_lengths": sum(bool(x) for x in counts),
            "length_127_count": str(counts[127]), "length_129_count": str(counts[129])}


def prefix_counts(n, lo_num, lo_den, hi_num, hi_den):
    """Count all prefix lengths in [lo_num/lo_den, hi_num/hi_den]."""
    output = [1]
    row = {0: 1}
    powers3 = [3**p for p in range(n + 1)]
    for length in range(1, n + 1):
        next_row = {}
        for p in range(min(row), max(row) + 2):
            within = ((1 << length) * lo_num <= powers3[p] * lo_den
                      and powers3[p] * hi_den <= (1 << length) * hi_num)
            if within:
                count = row.get(p, 0) + row.get(p - 1, 0)
                if count:
                    next_row[p] = count
        if not next_row:
            return output + [0] * (n + 1 - len(output))
        row = next_row
        output.append(sum(row.values()))
    return output


def range_count(n, numerator, denominator):
    forward = prefix_counts(n, 1, 1, numerator, denominator)
    backward = prefix_counts(n, denominator, numerator, 1, 1)
    return sum(backward[t] * forward[n - t] for t in range(n + 1))


@cache
def unrestricted_cap(height):
    """The exact finite recursion (H5)."""
    if height < 16:
        return height
    t = height.bit_length() - 1
    k = 0
    while 9 * 3 ** (k + 1) <= 1 << t:
        k += 1
    smaller = ((3**k * height * 2**k + 3**k * 2**t) // 2**(t + k)) - 1
    assert 0 <= smaller < height
    tail = sum(comb(t, p) for p in range(k + 1, t + 1))
    multiplicity = (height + (1 << t) - 1) >> t
    return min(height, t + multiplicity * tail + unrestricted_cap(smaller))


def height_checks():
    brute = 0
    for length in range(1, 13):
        words = list(product((0, 1), repeat=length))
        for numerator, denominator in ((2, 1), (5, 2), (4, 1)):
            exact = 0
            for bits in words:
                multiplier = Fraction(1)
                smallest = largest = multiplier
                for bit in bits:
                    multiplier *= Fraction(3 if bit else 1, 2)
                    smallest = min(smallest, multiplier)
                    largest = max(largest, multiplier)
                exact += largest * denominator <= smallest * numerator
            assert range_count(length, numerator, denominator) == exact
            brute += len(words)
    caps = []
    for n, shift in ((64, 7), (128, 8), (256, 10), (512, 13)):
        x = 1 << n
        y = x >> shift
        high = range_count(n, 3 * x, 3 * y - n)
        band_cap = n + (n + 1) * unrestricted_cap(y - 1) + high
        caps.append({"log2_height": n, "log2_height_to_floor_ratio": shift,
                     "range_words": str(high), "unrestricted_cap": str(unrestricted_cap(x)),
                     "bounded_path_cap": str(min(unrestricted_cap(x), band_cap))})
    return {"exhaustive_word_band_tests": brute, "caps": caps}


def valuation(value, prime):
    assert value
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def affine(word):
    clock = 0
    carry = 0
    for gap in word:
        carry = 3 * carry + (1 << clock)
        clock += gap
    return clock, carry


def finite_lift(word):
    clock, carry = affine(word)
    modulus = 1 << (clock + 1)
    source = ((1 << clock) - carry) * pow(3**len(word), -1, modulus) % modulus
    assert source > 0 and source % 2 == 1
    return source


def bridge_checks():
    rational2 = (Fraction(-1), Fraction(1), Fraction(5, 3), Fraction(-2, 7))
    rational3 = (Fraction(-1), Fraction(2, 5), Fraction(-3, 8))
    tests = 0
    bridges = 0
    spacing_tests = 0
    for length in range(1, 13):
        total = floor_alpha(length)
        for bits in product((1, 2), repeat=length):
            if sum(bits) != total:
                continue
            clock, carry = affine(bits)
            if any((1 << sum(bits[:i])) <= 3**i for i in range(1, length)):
                continue
            if 1 << clock >= 3**length:
                continue
            bridges += 1
            q = finite_lift(bits)
            end = q
            for gap in bits:
                assert valuation(3 * end + 1, 2) == gap
                end = (3 * end + 1) >> gap
            assert 2**length * carry <= 9**length
            for u in rational2:
                for v in rational3:
                    a, d = u.as_integer_ratio()
                    b, e = v.as_integer_ratio()
                    diff2 = d*q-a
                    diff3 = e*end-b
                    t2 = min(valuation(diff2, 2), clock) if diff2 else clock
                    t3 = min(valuation(diff3, 3), length) if diff3 else length
                    bridge = (3**length*a*e + d*e*carry - 2**clock*b*d)
                    assert bridge % (2**t2 * 3**t3) == 0
                    if length > 3 * (max(v, 0) - u):
                        assert bridge != 0
                    tests += 1
            fixed = Fraction(-carry, 3**length - 2**clock)
            for v in rational3:
                distance = min((valuation(q*v.denominator - v.numerator, 3)
                                if q*v.denominator != v.numerator else length + 1),
                               (valuation(end*v.denominator - v.numerator, 3)
                                if end*v.denominator != v.numerator else length + 1))
                diff = fixed.numerator*v.denominator-v.numerator*fixed.denominator
                assert diff % 3**distance == 0
                spacing_tests += 1
    return {"first_ladders_over_1_2": bridges, "joint_bridge_checks": tests,
            "periodic_return_residue_checks": spacing_tests}


def symbolic_checks():
    blocks = []
    for index in range(1, 33):
        length = index
        while True:
            clock = floor_alpha(length)
            # 3/8 < log2(3**length)-clock < 1/2, tested without real logs.
            if (1 << (8 * clock + 3)) < 3**(8 * length) and 3**(2*length) < 1 << (2*clock+1):
                break
            length += 1
        twos = clock - length
        ones = length - twos
        word = [2] * twos + [1] * ones
        assert twos > 0 and ones > 0
        assert all(2**sum(word[:i]) > 3**i for i in range(1, length))
        assert 2**clock < 3**length
        blocks.append(word)
    whole = [gap for word in blocks for gap in word]
    source = finite_lift(whole)
    x = source
    for word in blocks:
        twos = word.count(2)
        ones = word.count(1)
        assert (x - 1) % (4**twos) == 0
        for expected in word:
            assert valuation(3*x+1, 2) == expected
            x = (3*x+1) >> expected
        assert (x + 1) % (3**ones) == 0
    return {"blocks": len(blocks), "odd_gaps": len(whole), "native_clock": sum(whole),
            "positive_finite_source_bits": source.bit_length(), "terminal_bits": x.bit_length()}


if __name__ == "__main__":
    result = {"pressure": pressure_checks(256), "height": height_checks(),
              "bridges": bridge_checks(), "symbolic_prefix": symbolic_checks()}
    print(json.dumps(result, indent=2, sort_keys=True))
