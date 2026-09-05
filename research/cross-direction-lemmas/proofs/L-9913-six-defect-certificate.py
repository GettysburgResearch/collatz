#!/usr/bin/env python3
"""Exact certificate for L-9913 (six centered defects)."""

from __future__ import annotations

from itertools import combinations, permutations, product
from typing import Iterator, Optional, Sequence, Tuple


Word = Tuple[int, ...]


def centered_data(word: Sequence[int]) -> Tuple[int, int, int, int]:
    k_value = len(word)
    prefix = 0
    c_value = 0
    for j, a_value in enumerate(word):
        c_value += 3 ** (k_value - 1 - j) * 2**prefix
        prefix += a_value
    d_value = 2**prefix - 3**k_value
    return prefix, c_value, d_value, c_value - d_value


def sparse_defect(word: Sequence[int]) -> int:
    k_value = len(word)
    prefix = 0
    result = 0
    for j, a_value in enumerate(word):
        result += 3 ** (k_value - 1 - j) * 2**prefix * (4 - 2**a_value)
        prefix += a_value
    return result


def rotations(word: Word) -> Tuple[Word, ...]:
    return tuple(word[j:] + word[:j] for j in range(len(word)))


def compositions(total: int, parts: int) -> Iterator[Tuple[int, ...]]:
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def patterns(kind: str) -> Tuple[Word, ...]:
    if kind == "all1":
        return ((1, 1, 1, 1, 1, 1),)
    if kind in ("one3", "one4"):
        high = 3 if kind == "one3" else 4
        return tuple(
            tuple(high if j == position else 1 for j in range(6))
            for position in range(6)
        )
    if kind == "two3":
        return tuple(
            tuple(3 if j in positions else 1 for j in range(6))
            for positions in combinations(range(6), 2)
        )
    raise ValueError(kind)


def build_words(exceptional: Word, gaps: Tuple[int, ...]) -> Tuple[Word, Word]:
    core = []
    full = []
    for index, (b_value, gap) in enumerate(zip(exceptional, gaps)):
        core.append(b_value)
        full.append(b_value)
        full.extend([2] * gap)
        if index < 5:
            core.extend([2] * gap)
    return tuple(core), tuple(full)


def v2(value: int) -> int:
    order = 0
    while value % 2 == 0:
        value //= 2
        order += 1
    return order


def audit_hit(word: Word) -> Tuple[int, int, int]:
    _, c_value, d_value, e_value = centered_data(word)
    assert d_value > 0 and e_value % d_value == 0
    start = 1 + e_value // d_value
    assert start > 0 and start % 2 == 1
    state = start
    first_return = 0
    for index, advertised in enumerate(word, start=1):
        numerator = 3 * state + 1
        actual = v2(numerator)
        assert actual == advertised
        state = numerator // 2**actual
        assert state > 0 and state % 2 == 1
        if state == start and first_return == 0:
            first_return = index
    assert state == start and first_return > 0
    assert c_value // d_value == start and c_value % d_value == 0
    return start, first_return, len(word)


B_TOTAL = {"all1": 6, "one3": 8, "one4": 9, "two3": 10}


def canonical_rows(kind: str, total_neutral: int):
    expected_d = (
        2 ** B_TOTAL[kind] * 4**total_neutral - 729 * 3**total_neutral
    )
    for gaps in compositions(total_neutral, 6):
        if gaps[5] != max(gaps):
            continue
        for exceptional in patterns(kind):
            core, full = build_words(exceptional, gaps)
            _, _, _, core_e = centered_data(core)
            _, _, full_d, full_e = centered_data(full)
            assert sparse_defect(core) == core_e
            assert sparse_defect(full) == full_e
            assert full_d == expected_d
            assert full_e == 3 ** gaps[5] * core_e
            yield exceptional, gaps, core_e, full_d, full_e, full


def row_statistics(kind: str, total_neutral: int):
    rows = list(canonical_rows(kind, total_neutral))
    d_value = rows[0][3]
    assert all(row[3] == d_value for row in rows)
    maximum_e = max(row[2] for row in rows)
    height_rows = [row for row in rows if row[2] >= 2 * d_value]
    divisor_hits = [row for row in rows if row[2] % d_value == 0]
    if height_rows:
        rho = min(
            min(row[2] % d_value, d_value - row[2] % d_value)
            for row in height_rows
        )
    else:
        rho = None

    audited = []
    for row in divisor_hits:
        if row[2] <= 0:
            audited.append((row[0], row[1], "negative/formal"))
        elif row[2] < 2 * d_value:
            audited.append((row[0], row[1], "subheight/formal"))
        else:
            start, first_return, period = audit_hit(row[5])
            label = "primitive" if first_return == period else "powered"
            if start == 1:
                label = "trivial"
            audited.append((row[0], row[1], start, first_return, period, label))

    return d_value, len(rows), maximum_e, len(height_rows), rho, audited


def necklaces(high_count: int) -> Tuple[Word, ...]:
    seen = set()
    result = []
    for word in product((1, 3), repeat=6):
        if word.count(3) != high_count or word in seen:
            continue
        orbit = rotations(word)
        seen.update(orbit)
        result.append(min(orbit))
    return tuple(result)


def contraction_check() -> None:
    high_expected = {
        3: {
            (1, 1, 1, 3, 3, 3): (3367, -2078),
            (1, 1, 3, 1, 3, 3): (3367, -1862),
            (1, 1, 3, 3, 1, 3): (3367, -1286),
            (1, 3, 1, 3, 1, 3): (3367, -962),
        },
        4: {
            (1, 1, 3, 3, 3, 3): (15655, -12038),
            (1, 3, 1, 3, 3, 3): (15655, -11714),
            (1, 3, 3, 1, 3, 3): (15655, -10850),
        },
        5: {(1, 3, 3, 3, 3, 3): (64807, -51554)},
        6: {(3, 3, 3, 3, 3, 3): (261415, -209132)},
    }
    for high_count, expected in high_expected.items():
        assert set(necklaces(high_count)) == set(expected)
        assert 3**6 < 2 ** (6 + 2 * high_count)
        for word, target in expected.items():
            _, _, d_value, e_value = centered_data(word)
            assert (d_value, e_value) == target
            assert e_value < 2 * d_value

    pair_expected = {
        (3, 4): {
            (1, 1, 1, 1, 3, 4): (1319, -558),
            (1, 1, 1, 1, 4, 3): (1319, -430),
            (1, 1, 1, 3, 1, 4): (1319, -414),
            (1, 1, 1, 4, 1, 3): (1319, -94),
            (1, 1, 3, 1, 1, 4): (1319, -198),
        },
        (4, 4): {
            (1, 1, 1, 1, 4, 4): (3367, -2478),
            (1, 1, 1, 4, 1, 4): (3367, -2142),
            (1, 1, 4, 1, 1, 4): (3367, -1638),
        },
    }
    for high_pair, expected in pair_expected.items():
        found = set()
        for positions in combinations(range(6), 2):
            for ordered in set(permutations(high_pair)):
                word_list = [1] * 6
                word_list[positions[0]] = ordered[0]
                word_list[positions[1]] = ordered[1]
                found.add(min(rotations(tuple(word_list))))
        assert found == set(expected)
        for word, target in expected.items():
            _, _, d_value, e_value = centered_data(word)
            assert (d_value, e_value) == target
            assert e_value < 2 * d_value

    _, _, adjacent_d, adjacent_e = centered_data((1, 1, 1, 1, 3, 3))
    assert (adjacent_d, adjacent_e) == (295, 466)
    assert adjacent_e < 2 * adjacent_d

    _, _, lone_d, lone_e = centered_data((1, 1, 1, 1, 1, 5))
    assert (lone_d, lone_e) == (295, 370)
    assert lone_e < 2 * lone_d


def cutoff_check() -> None:
    def denominator(b_total: int, total_neutral: int) -> int:
        return 2**b_total * 4**total_neutral - 729 * 3**total_neutral

    thresholds = (
        (6, 8, -588665, 9, 2428309),
        (8, 3, -3299, 4, 6487),
        (9, 1, -139, 2, 1631),
    )
    for b_total, before_r, before_d, first_r, first_d in thresholds:
        assert denominator(b_total, before_r) == before_d
        assert denominator(b_total, first_r) == first_d
    assert denominator(10, 0) == 295

    comparisons = (
        (6, 13, 1330, 3, 4870805578),
        (8, 7, 3376, 2, 1742938),
        (9, 7, 6752, 2, 6674522),
        (10, 7, 8320, 2, 21846106),
    )
    for b_total, total_neutral, coefficient, tail, margin in comparisons:
        d_value = denominator(b_total, total_neutral)
        upper = coefficient * 4 ** (total_neutral - tail)
        assert 2 * d_value - upper == margin > 0


def finite_table_check() -> None:
    expected = {
        ("all1", 9): (2428309, 412, 8206498, 30, 85987),
        ("all1", 10): (24062143, 607, 27240934, 0, None),
        ("all1", 11): (139295293, 872, 85917106, 0, None),
        ("all1", 12): (686321335, 1223, 274528534, 0, None),
        ("one3", 4): (6487, 186, 139708, 130, 2),
        ("one3", 5): (84997, 336, 460084, 20, 1776),
        ("one3", 6): (517135, 612, 1445788, 2, 105617),
        ("one4", 2): (1631, 36, 18260, 25, 55),
        ("one4", 3): (13085, 96, 71420, 26, 216),
        ("one4", 4): (72023, 186, 253172, 15, 2065),
        ("one4", 5): (347141, 336, 841436, 3, 42706),
        ("one4", 6): (1565711, 612, 2655380, 0, None),
        ("two3", 0): (295, 15, 4756, 14, 16),
        ("two3", 1): (1909, 15, 4756, 1, 938),
        ("two3", 2): (9823, 90, 22588, 2, 350),
        ("two3", 3): (45853, 240, 93268, 1, 1562),
        ("two3", 4): (203095, 465, 357628, 0, None),
        ("two3", 5): (871429, 840, 1236724, 0, None),
        ("two3", 6): (3662863, 1530, 3972316, 0, None),
    }
    print("finite exact table:")
    for key, target in expected.items():
        actual = row_statistics(*key)
        assert actual[:5] == target
        assert not actual[5]
        print(f"  type={key[0]}, R={key[1]}: {actual[:5]}")


def main() -> None:
    contraction_check()
    cutoff_check()
    finite_table_check()
    print("L-9913 six-defect certificate: PASS")
    print("exact divisor hits: 0")


if __name__ == "__main__":
    main()
