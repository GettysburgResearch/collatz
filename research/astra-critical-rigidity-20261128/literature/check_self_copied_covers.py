"""Exact checks for reference anchors induced by copies in one actual parity word."""

from collections import Counter
from fractions import Fraction
from itertools import groupby
from math import gcd


def require(condition, description):
    if not condition:
        raise ArithmeticError(description)


def affine(word):
    grade = carry = 0
    for j, bit in enumerate(word):
        if bit:
            carry = 3 * carry + (1 << j)
            grade += 1
    return grade, carry


def center(word):
    g, c = affine(word)
    return Fraction(c, (1 << len(word)) - 3**g)


def path(source):
    states, word, seen = [], [], set()
    x = source
    while len(states) < 520 and x not in seen:
        seen.add(x)
        states.append(x)
        bit = x.numerator % 2
        word.append(bit)
        x = (3 * x + 1) / 2 if bit else x / 2
    states.append(x)
    return states, word


def check_window(states, word, earlier, size, counts):
    form = word[earlier:earlier + size]
    require(len(form) == size, "complete physical offset window")
    g, c = affine(form)
    det = (1 << size) - 3**g
    z = center(form)
    x, y = states[earlier], states[earlier + size]
    require(z == x + (1 << size) * (y - x) / det, "two physical endpoints")
    require(z.denominator <= 3**size and abs(z.numerator) <= 3**size, "center height")
    if x.denominator == y.denominator == 1:
        require(z.denominator == abs(det) // gcd(abs(det), (y - x).numerator),
                "complete reduced determinant")
        counts["integer_gcd_windows"] += 1
        counts["proper_cancellations"] += 1 < z.denominator < abs(det)
    return z


def replay(states, word, lag, policy, counts):
    limit = min(95, len(word) - lag)
    i = j = 0
    columns = []
    while i < limit and j < limit:
        direction = (i + 5 * j + policy) % 29
        if policy and direction in (2, 3):
            columns.append((i, j, "left"))
            i += 1
        elif policy and direction == 11:
            columns.append((i, j, "right"))
            j += 1
        else:
            kind = "match" if word[i] == word[lag + j] else "sub"
            columns.append((i, j, kind))
            i += 1
            j += 1
    for idx in range(i, limit):
        columns.append((idx, j, "left"))
    for idx in range(j, limit):
        columns.append((limit, idx, "right"))
    require(sum(kind != "right" for _, _, kind in columns) == limit, "first-track partition")
    require(sum(kind != "left" for _, _, kind in columns) == limit, "second-track partition")
    edits = sum(kind != "match" for _, _, kind in columns)
    pieces = 0
    length = 0
    for matching, segment in groupby(columns, key=lambda z: z[2] == "match"):
        segment = list(segment)
        if not matching:
            n = sum(kind != "right" for _, _, kind in segment)
            pieces += n
            length += n
            continue
        i, j, _ = segment[0]
        h = lag + j - i
        d = len(segment)
        if h == 0:
            counts["discarded_zero_displacement"] += 1
            return
        u = abs(h)
        left = min(i, lag + j)
        require(all(h == lag + b - a for a, b, _ in segment), "unchanging displacement")
        enclosing = word[left:left + u + d]
        require(len(enclosing) == u + d and enclosing[:d] == enclosing[u:],
                "actual periodic enclosure")
        start = check_window(states, word, left, u, counts)
        end = check_window(states, word, left + d, u, counts)
        require(center(enclosing[d:d + u]) == end, "terminal rotated phase")
        require(word[i:i + d] == enclosing[:d], "correct first-track phase")
        value = start
        for bit in word[i:i + d]:
            require(value.numerator % 2 == bit, "native signed reference parity")
            value = (3 * value + 1) / 2 if bit else value / 2
        require(value == end, "exact reference transport")
        counts["separated_runs"] += start != states[i]
        counts["periodic_hits"] += start == states[i]
        counts["overlapping_copies"] += d > u
        counts["disjoint_copies"] += d <= u
        counts["matched_bits"] += d
        pieces += 1
        length += d
    require(length == limit and pieces <= 2 * edits + 1, "cover length and edit budget")
    counts["complete_alignments"] += 1


def main():
    counts = Counter()
    for den in (1, 5, 7):
        for num in (27, 73, 97, 327, 703, 871, 6171, 77031, 837799, 274133):
            for sign in (1, -1):
                states, word = path(Fraction(sign * num, den))
                for lag in (2, 3, 5, 8, 13):
                    if len(word) < lag + 6:
                        continue
                    for policy in (0, 1, 2):
                        replay(states, word, lag, policy, counts)
    require(min(counts[key] for key in ("complete_alignments", "overlapping_copies",
                                        "disjoint_copies", "proper_cancellations")) > 100,
            "coverage")
    for key, count in sorted(counts.items()):
        print(key, count)


if __name__ == "__main__":
    main()
