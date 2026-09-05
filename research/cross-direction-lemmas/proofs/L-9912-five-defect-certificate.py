#!/usr/bin/env python3
"""Exact certificate for L-9912 (five centered defects).

The proof uses integer arithmetic only.  It rebuilds every finite candidate
from compositions of the total neutral length and retains an exact replay
path for any unexpected divisor hit.
"""

from __future__ import annotations

from itertools import product
from typing import Iterable, Iterator, Optional, Sequence, Tuple


Word = Tuple[int, ...]
Gaps = Tuple[int, int, int, int, int]


def centered_data(word: Sequence[int]) -> Tuple[int, int, int, int]:
    """Return (A,C,D,E) from the chronological valuation word."""

    if not word or any(a < 1 for a in word):
        raise ValueError("a valuation word must be nonempty and positive")
    k = len(word)
    prefix = 0
    c_value = 0
    for j, a_value in enumerate(word):
        c_value += 3 ** (k - 1 - j) * 2**prefix
        prefix += a_value
    d_value = 2**prefix - 3**k
    return prefix, c_value, d_value, c_value - d_value


def sparse_defect(word: Sequence[int]) -> int:
    """Independently evaluate the centered sparse sum."""

    k = len(word)
    prefix = 0
    result = 0
    for j, a_value in enumerate(word):
        result += 3 ** (k - 1 - j) * 2**prefix * (4 - 2**a_value)
        prefix += a_value
    return result


def compositions(total: int, parts: int) -> Iterator[Tuple[int, ...]]:
    """Generate all ordered weak compositions exactly once."""

    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def exceptional_patterns(high: Optional[int]) -> Iterable[Word]:
    if high is None:
        yield (1, 1, 1, 1, 1)
        return
    for position in range(5):
        yield tuple(high if j == position else 1 for j in range(5))


def build_full_word(exceptional: Sequence[int], gaps: Sequence[int]) -> Word:
    result = []
    for b_value, gap in zip(exceptional, gaps):
        result.append(b_value)
        result.extend([2] * gap)
    return tuple(result)


def build_core(exceptional: Sequence[int], gaps: Sequence[int]) -> Word:
    """Build the word after deleting the terminal largest neutral tail."""

    result = []
    for index, b_value in enumerate(exceptional):
        result.append(b_value)
        if index < 4:
            result.extend([2] * gaps[index])
    return tuple(result)


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 replay input must be positive")
    order = 0
    while value % 2 == 0:
        value //= 2
        order += 1
    return order


def audit_hit(word: Word) -> Tuple[int, int, int]:
    """Reconstruct an unexpected hit and return (n0, first_return, period)."""

    _, c_value, d_value, e_value = centered_data(word)
    assert d_value > 0 and e_value % d_value == 0
    n_start = 1 + e_value // d_value
    assert n_start > 0 and n_start % 2 == 1

    state = n_start
    first_return = 0
    for index, advertised in enumerate(word, start=1):
        numerator = 3 * state + 1
        actual = v2(numerator)
        assert actual == advertised
        state = numerator // 2**actual
        assert state > 0 and state % 2 == 1
        if state == n_start and first_return == 0:
            first_return = index

    assert state == n_start
    assert c_value % d_value == 0 and c_value // d_value == n_start
    assert first_return > 0
    return n_start, first_return, len(word)


def canonical_rows(high: Optional[int], total_neutral: int):
    """Enumerate all largest-gap rotations for one finite proof row."""

    b_total = 5 if high is None else high + 4
    expected_d = 2**b_total * 4**total_neutral - 243 * 3**total_neutral

    for raw_gaps in compositions(total_neutral, 5):
        gaps = tuple(raw_gaps)
        assert len(gaps) == 5
        if gaps[4] != max(gaps):
            continue
        for exceptional in exceptional_patterns(high):
            core = build_core(exceptional, gaps)
            full_word = build_full_word(exceptional, gaps)
            _, _, _, core_e = centered_data(core)
            _, _, full_d, full_e = centered_data(full_word)
            assert sparse_defect(core) == core_e
            assert sparse_defect(full_word) == full_e
            assert full_d == expected_d
            assert full_e == 3 ** gaps[4] * core_e
            yield exceptional, gaps, core_e, full_d, full_e, full_word


def row_statistics(high: Optional[int], total_neutral: int):
    candidates = list(canonical_rows(high, total_neutral))
    assert candidates
    d_value = candidates[0][3]
    assert all(row[3] == d_value for row in candidates)

    maximum_e = max(row[2] for row in candidates)
    height_rows = [row for row in candidates if row[2] >= 2 * d_value]
    # Search divisibility before applying the height sieve.  This makes every
    # formal hit explicit instead of silently discarding a negative or
    # subheight congruence.
    divisor_hits = [row for row in candidates if row[2] % d_value == 0]

    if height_rows:
        circular_remainders = []
        for row in height_rows:
            remainder = row[2] % d_value
            circular_remainders.append(min(remainder, d_value - remainder))
        least_circular = min(circular_remainders)
    else:
        least_circular = None

    audited_hits = []
    for row in divisor_hits:
        if row[2] <= 0:
            audited_hits.append(
                (row[0], row[1], None, None, len(row[5]), "negative/formal")
            )
        elif row[2] < 2 * d_value:
            audited_hits.append(
                (row[0], row[1], None, None, len(row[5]), "subheight/formal")
            )
        else:
            n_start, first_return, period = audit_hit(row[5])
            classification = "primitive" if first_return == period else "powered"
            if n_start == 1:
                classification = "trivial"
            audited_hits.append(
                (row[0], row[1], n_start, first_return, period, classification)
            )

    return (
        d_value,
        len(candidates),
        maximum_e,
        len(height_rows),
        least_circular,
        audited_hits,
    )


def rotations(word: Word) -> Tuple[Word, ...]:
    return tuple(word[index:] + word[:index] for index in range(len(word)))


def canonical_necklaces(high_count: int) -> Tuple[Word, ...]:
    seen = set()
    representatives = []
    for word in product((1, 3), repeat=5):
        if word.count(3) != high_count or word in seen:
            continue
        orbit = rotations(word)
        seen.update(orbit)
        representatives.append(min(orbit))
    return tuple(representatives)


def contraction_check() -> None:
    expected = {
        2: {
            (1, 1, 1, 3, 3): (269, -10),
            (1, 1, 3, 1, 3): (269, 62),
        },
        3: {
            (1, 1, 3, 3, 3): (1805, -1282),
            (1, 3, 1, 3, 3): (1805, -1174),
        },
        4: {(1, 3, 3, 3, 3): (7949, -6262)},
        5: {(3, 3, 3, 3, 3): (32525, -26020)},
    }

    for high_count in range(2, 6):
        assert 3**5 < 2 ** (5 + 2 * high_count)
        necklaces = canonical_necklaces(high_count)
        assert len(necklaces) == len(expected[high_count])
        for necklace in necklaces:
            selected = None
            for rotation in rotations(necklace):
                _, _, d_value, e_value = centered_data(rotation)
                if e_value < 2 * d_value:
                    selected = rotation
                    break
            assert selected is not None

        for representative, (expected_d, expected_e) in expected[high_count].items():
            _, _, d_value, e_value = centered_data(representative)
            assert (d_value, e_value) == (expected_d, expected_e)
            assert e_value < 2 * d_value

    # Boundary of the lone-high analytic family.
    _, _, d_five, e_five = centered_data((1, 1, 1, 1, 5))
    assert d_five == 269 and e_five == -58


def analytic_cutoff_check() -> None:
    def denominator(b_total: int, total_neutral: int) -> int:
        return 2**b_total * 4**total_neutral - 243 * 3**total_neutral

    # Exact positive-drift thresholds.
    assert denominator(5, 7) == -7153
    assert denominator(5, 8) == 502829
    assert denominator(7, 2) == -139
    assert denominator(7, 3) == 1631
    assert denominator(8, 0) == 13

    # First normalized comparisons; monotonicity handles every later R.
    comparisons = (
        (5, 9, 422, 2, 297230),
        (7, 6, 1040, 2, 428042),
        (8, 6, 2080, 2, 1210378),
    )
    for b_total, total_neutral, coefficient, min_tail, expected_margin in comparisons:
        d_value = denominator(b_total, total_neutral)
        upper = coefficient * 4 ** (total_neutral - min_tail)
        assert 2 * d_value - upper == expected_margin > 0


def finite_table_check() -> None:
    # (high letter or None, R): (D,N,max(Eu),height survivors,rho)
    expected = {
        (None, 8): (502829, 120, 751634, 0, None),
        (3, 3): (1631, 55, 11996, 26, 65),
        (3, 4): (13085, 95, 41108, 7, 148),
        (3, 5): (72023, 160, 131516, 0, None),
        (4, 0): (13, 5, 1108, 5, 2),
        (4, 1): (295, 5, 1108, 2, 72),
        (4, 2): (1909, 25, 5404, 3, 146),
        (4, 3): (9823, 55, 21076, 1, 1430),
        (4, 4): (45853, 95, 73468, 0, None),
        (4, 5): (203095, 160, 236788, 0, None),
    }

    print("finite exact table:")
    for key, expected_row in expected.items():
        actual = row_statistics(*key)
        actual_row = actual[:5]
        audited_hits = actual[5]
        assert actual_row == expected_row
        assert not audited_hits
        print(f"  type={key[0]!r}, R={key[1]}: {actual_row}")


def main() -> None:
    contraction_check()
    analytic_cutoff_check()
    finite_table_check()
    print("L-9912 five-defect certificate: PASS")
    print("exact positive divisor hits: 0")


if __name__ == "__main__":
    main()
