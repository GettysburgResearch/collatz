"""Check the finite word, landing-test, octave and rounding identities."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from math import comb
import json


def require(condition, context):
    if not condition:
        raise ArithmeticError(context)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def odd_step(n):
    value = 3 * n + 1
    gap = (value & -value).bit_length() - 1
    return gap, value >> gap


def word_checks(k):
    total = 4 * k // 3
    modulus = 3**k
    residues = set()
    count = 0
    for internal in combinations(range(1, total), k - 1):
        ends = (0,) + internal + (total,)
        gaps = tuple(ends[i + 1] - ends[i] for i in range(k))
        partial = 0
        residue = 0
        for i, gap in enumerate(reversed(gaps)):
            partial += gap
            residue += 3**i * pow(2, -partial, modulus)
        residue %= modulus
        residues.add(residue)
        terminal = residue + modulus * (4 + int(residue % 2 == 0))
        seed = terminal
        for gap in reversed(gaps):
            seed, remainder = divmod((seed << gap) - 1, 3)
            require(remainder == 0 and seed % 2 and seed > 0, ("inverse", gaps))
        cursor = seed
        for expected in gaps:
            actual, cursor = odd_step(cursor)
            require(actual == expected, ("true gap", gaps, actual))
        require(cursor == terminal, ("terminal", k, gaps))
        count += 1
    require(count == comb(total - 1, k - 1), ("composition count", k))
    return {"grade": k, "total": total, "words_replayed": count,
            "different_residues": len(residues)}


def grid_checks(bits=14):
    frequencies = Counter()
    patterns = set()
    physical_marks = 0
    for seed in range(1, (1 << bits) + 1):
        n = seed
        native = []
        for _ in range(bits):
            native.append(n)
            n = step(n)
        pattern = sum((n % 2) << i for i, n in enumerate(native))
        require(pattern not in patterns, ("repeated parity pattern", seed))
        patterns.add(pattern)
        frequencies[pattern.bit_count()] += 1
        dates = [i for i, n in enumerate(native) if n % 2]
        for i in range(0, len(dates) - 3, 3):
            if dates[i + 3] - dates[i] != 4:
                continue
            value = native[dates[i]]
            for _ in range(3):
                _, value = odd_step(value)
            require(value == native[dates[i + 3]], ("natural endpoint", seed))
            physical_marks += 1
    require(frequencies == {k: comb(bits, k) for k in range(bits + 1)},
            "literal fair binomial")
    require(3**9 < 2**15, "strict later contraction coefficient")
    return {"parity_words": len(patterns), "native_bits": bits,
            "complete_three_gap_marks": physical_marks}


def gate_checks():
    gates = (3072, 1536, 768, 384, 192, 96, 48, 24)
    masks = [lambda n: n % 83 == 17, lambda n: n % 127 == 101,
             lambda n: n % 19 == 5, lambda n: n % 257 == 6]
    tested = marked = overshoots = even_observations = 0
    for seed in range(4097, 8192, 2):
        odd = [seed]
        while odd[-1] > gates[-1]:
            previous = odd[-1]
            gap, following = odd_step(previous)
            cursor = previous
            for elapsed in range(1, gap + 1):
                cursor = step(cursor)
                if cursor % 2 == 0:
                    require((cursor << elapsed) - 1 == 3 * previous,
                            ("actual even predecessor", seed, elapsed))
                    even_observations += 1
            odd.append(following)
        dates = [next(i for i, value in enumerate(odd) if value <= z) for z in gates]
        overshoots += sum(i == j for i, j in zip(dates, dates[1:]))
        for mask in masks:
            direct = any(mask(x) for x in odd[:dates[-1]])
            reconstructed = any(mask(x) for x in odd[:dates[0]])
            for pos, (left, right) in enumerate(zip(dates, dates[1:])):
                cursor = odd[left]
                via_landing = False
                while cursor > gates[pos + 1]:
                    via_landing |= mask(cursor)
                    _, cursor = odd_step(cursor)
                require(cursor == odd[right], ("first odd landing", seed, pos))
                require(via_landing == any(mask(x) for x in odd[left:right]),
                        ("piece test", seed, pos))
                reconstructed |= via_landing
            require(reconstructed == direct, ("all-gate identity", seed))
            tested += 1
            marked += int(direct)
    return {"odd_octave_sources": 2048, "piecewise_mask_identities": tested,
            "positive_full_tests": marked, "double_gate_overshoots": overshoots,
            "native_even_observations": even_observations}


def octave_depth(index, numerator, denominator):
    ell = index.bit_length() - 1
    rhs = 1 << (numerator * ell // denominator)
    left, right = ell**6, rhs
    power = 0
    while left * 27 <= right * 16:
        power += 1
        left *= 27
        right *= 16
    return 3 * max(1, power)


def depth_checks():
    tested = 0
    maximum = 0
    for a, b in ((1, 1), (2, 3), (1, 2), (1, 5)):
        for h in (32, 64, 127, 128, 255, 512, 1024):
            for j in ((1 << h) - 1, 1 << h, (1 << h) + 1):
                depth = octave_depth(j, a, b)
                for other in (j // 2 + 1, j - 1, j, j + 1, 2 * j - 1, 2 * j):
                    change = abs(octave_depth(other, a, b) - depth)
                    require(change <= 18, ("common depth", a, b, h))
                    tested += 1
                    maximum = max(maximum, change)
    return {"exact_octave_pairs": tested, "largest_depth_difference": maximum}


def main():
    rows = {"words": [word_checks(k) for k in (3, 6, 9, 12, 15)],
            "parity": grid_checks(), "gates": gate_checks(), "depth": depth_checks()}
    print(json.dumps({"summary_sha256": sha256(json.dumps(rows, sort_keys=True)
                                               .encode()).hexdigest(),
                      "checks": rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
