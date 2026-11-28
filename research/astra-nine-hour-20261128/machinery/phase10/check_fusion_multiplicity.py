"""Verify finite fusion on actual positive paths and the pressure triple action."""
from collections import defaultdict
from itertools import combinations


def check(condition, message):
    if not condition:
        raise ValueError(message)


def numerator(gaps):
    total = 0
    result = 0
    for gap in gaps:
        result = 3 * result + (1 << total)
        total += gap
    return result


def odd_path(x, count):
    gaps = []
    for _ in range(count):
        y = 3 * x + 1
        gap = (y & -y).bit_length() - 1
        x = y >> gap
        gaps.append(gap)
    return x, tuple(gaps)


def check_fusions():
    tested_words = tested_matches = tested_lifts = 0
    for total in range(1, 15):
        for count in range(1, total + 1):
            groups = defaultdict(list)
            for cuts in combinations(range(1, total), count - 1):
                limits = (0,) + cuts + (total,)
                word = tuple(b - a for a, b in zip(limits, limits[1:]))
                d = numerator(word)
                groups[d % 3**count].append((word, d))
            for group in groups.values():
                base_word, base_d = group[0]
                modulus = 1 << (total + 1)
                x = modulus + (((1 << total) - base_d)
                               * pow(3**count, -1, modulus)) % modulus
                y, actual = odd_path(x, count)
                check(actual == base_word, "dyadic period decoding")
                companions = set()
                for word, d in group:
                    h = (base_d - d) // 3**count
                    check(h % 2 == 0 and x + h > 0, "positive even offset")
                    check(odd_path(x + h, count) == (y, word), "counted fusion")
                    companions.add(h)
                    tested_words += 1
                check(len(companions) == len(group), "fixed-total freeness")
                tested_matches += len(group)**2
                if len(group) > 1:
                    mark_set = {h % 3 for h in companions}
                    inv = pow(1 << total, -1, 3**(count + 1))
                    ternary = {(d * inv % 3**(count + 1)) // 3**count
                               for _, d in group}
                    check(len(ternary) == len(mark_set), "extra trit cardinality")
                    tested_lifts += 1
    return tested_words, tested_matches, tested_lifts


def check_pressure():
    cells = 0
    for width in range(2, 7):
        mod = 3**width
        period = 2 * 3**(width - 1)
        for s in range(1, mod):
            if s % 3 == 0:
                continue
            targets = set()
            for e in range(1, period + 1):
                a = (pow(2, e, 3 * mod) * s - 1) % (3 * mod)
                if a % 3 or (a // 3) % 3 == 0:
                    continue
                low = (a // 3) % (mod // 3)
                if low in targets:
                    continue
                targets.add(low)
                table = [[((pow(2, e + k * period, 3 * mod) *
                            (s + j * mod) - 1) % (3 * mod)) // 3
                          for k in range(3)] for j in range(3)]
                triple = {low + k * (mod // 3) for k in range(3)}
                check(all(set(row) == triple for row in table), "action group lift")
                check(all(set(col) == triple for col in zip(*table)), "source trit lift")
                cells += 1
            check(len(targets) == 2 * 3**(width - 2), "all unit targets")
    return cells


if __name__ == "__main__":
    print("words, ordered matches, nontrivial cells:", *check_fusions())
    print("pressure Latin triples:", check_pressure())
