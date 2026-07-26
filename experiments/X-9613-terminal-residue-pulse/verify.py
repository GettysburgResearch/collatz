#!/usr/bin/env python3
"""Independent exact checks for L-9610 and T-9609.

The program uses only standard-library exact integer arithmetic.  It checks the
terminal-mod-27 rule, the monotone height gate, all four exceptional alphabets,
and selected direct two-macro compositions.  The unbounded conclusions rest on
the claim proofs.
"""

from itertools import combinations
from math import comb


def centered_rows(a: int, b: int):
    length = a + b
    q = 8**a * 16**b
    p = 9**length
    d = q - p
    rows = []
    for b_positions in combinations(range(length), b):
        b_set = set(b_positions)
        constant = 0
        exponent = 0
        word = []
        for position in range(length):
            if position in b_set:
                word.append("B")
                constant = 9 * constant
                exponent += 4
            else:
                word.append("A")
                constant = 9 * constant + 3 * (1 << exponent)
                exponent += 3
        assert exponent == 3 * a + 4 * b
        rows.append(("".join(word), constant))
    assert len(rows) == comb(length, b)
    return q, p, d, rows


def emax_formula(a: int, b: int) -> int:
    return 3 * 16**b * (9**a - 8**a)


def target_pairs(q: int, p: int, d: int, emax: int):
    pairs = []
    rmax = emax // (3 * d)
    for r in range(1, rmax + 1):
        for k in range(3 * r):
            value = 3 * r * d + p * k
            if value <= emax:
                pairs.append((r, k, value))
    return pairs


def check_terminal_residue() -> None:
    # Exhaust every fixed-weight word in a broad small interface range.
    for a in range(1, 14):
        for b in range(1, 5):
            q, p, d, rows = centered_rows(a, b)
            n = 3 * a + 4 * b
            assert p % 27 == 0
            for word, value in rows:
                expected = 0 if word.endswith("B") else 3 * pow(2, n - 3, 27)
                assert value % 27 == expected % 27

            if d <= 0:
                continue
            emax = max(value for _, value in rows)
            for r, k, target in target_pairs(q, p, d, emax):
                # A target can meet the terminal alphabet residue only at the
                # claimed r-levels.
                residues = {value % 27 for _, value in rows}
                if target % 27 in residues:
                    assert r % 9 in (0, 8)

    # Synthetic algebra check of the two congruence branches.
    for n in range(7, 80):
        q27 = pow(2, n, 27)
        final_a = 3 * pow(2, n - 3, 27) % 27
        for r in range(1, 100):
            target = 3 * r * q27 % 27
            if target == 0:
                assert r % 9 == 0
            if target == final_a:
                assert r % 9 == 8


def check_uniform_gate() -> None:
    table = [
        (6, 2, 123_557_112),
        (7, 2, 508_034_232),
        (8, 3, 191_107_444_536),
        (9, 3, 1_101_491_710_200),
        (10, 3, 4_965_623_066_808),
        (11, 3, 5_108_189_001_336),
        (12, 4, 7_198_933_032_700_920),
        (13, 4, 24_258_000_647_973_816),
    ]
    for a, b, expected_margin in table:
        left = 9**a * (16**b + 8 * 9**b)
        right = 9 * 8**a * 16**b
        assert right - left == expected_margin > 0

        # The normalized denominator grows with b, so the ratio decreases.
        previous_num = emax_formula(a, b)
        previous_den = 8**a * 16**b - 9 ** (a + b)
        for later_b in range(b + 1, b + 8):
            num = emax_formula(a, later_b)
            den = 8**a * 16**later_b - 9 ** (a + later_b)
            assert den > 0
            assert num * previous_den < previous_num * den
            previous_num, previous_den = num, den

    # Exact supercritical/contracting boundary through a=13.
    expected_first_contracting = {
        6: 2,
        7: 2,
        8: 2,
        9: 2,
        10: 3,
        11: 3,
        12: 3,
        13: 3,
    }
    for a, first in expected_first_contracting.items():
        for b in range(1, first):
            assert 9 ** (a + b) > 8**a * 16**b
        assert 9 ** (a + first) < 8**a * 16**first


def check_mod7_phase(a: int, b: int, values) -> None:
    expected = 3 * pow(2, b, 7) * (pow(2, a, 7) - 1)
    assert {value % 7 for value in values} == {expected % 7}


def check_exception_8_2() -> None:
    a, b = 8, 2
    q, p, d, rows = centered_rows(a, b)
    values = [value for _, value in rows]
    emax = max(values)
    assert (q, p, d, emax) == (
        4_294_967_296,
        3_486_784_401,
        808_182_895,
        20_174_979_840,
    )
    assert emax < 27 * d
    assert emax < 24 * d + p
    pairs = [pair for pair in target_pairs(q, p, d, emax) if pair[0] % 9 in (0, 8)]
    assert pairs == [(8, 0, 24 * d)]
    check_mod7_phase(a, b, values)
    assert {value % 7 for value in values} == {1}
    assert (24 * d) % 7 == 6


def check_exception_9_2() -> None:
    a, b = 9, 2
    q, p, d, rows = centered_rows(a, b)
    values = [value for _, value in rows]
    emax = max(values)
    assert (q, p, d, emax) == (
        34_359_738_368,
        31_381_059_609,
        2_978_678_759,
        194_459_720_448,
    )
    assert emax < 66 * d
    pairs = [pair for pair in target_pairs(q, p, d, emax) if pair[0] % 9 in (0, 8)]
    by_r = {}
    for r, k, value in pairs:
        by_r.setdefault(r, []).append(k)
    assert {r: max(ks) for r, ks in by_r.items()} == {8: 3, 9: 3, 17: 1, 18: 1}

    check_mod7_phase(a, b, values)
    assert {value % 7 for value in values} == {0}
    pairs = [(r, k, value) for r, k, value in pairs if value % 7 == 0]
    assert {(r, k) for r, k, _ in pairs} == {(8, 0), (9, 0), (17, 0), (18, 0)}

    assert {value % 8 for value in values} == {0, 3}
    pairs = [(r, k, value) for r, k, value in pairs if value % 8 in {0, 3}]
    assert [(r, k) for r, k, _ in pairs] == [(8, 0)]

    assert {value % 16 for value in values} == {0, 3, 11}
    assert pairs[0][2] % 16 == 8


def check_exception_12_3() -> None:
    a, b = 12, 3
    q, p, d, rows = centered_rows(a, b)
    values = [value for _, value in rows]
    emax = max(values)
    assert (q, p, d, emax) == (
        281_474_976_710_656,
        205_891_132_094_649,
        75_583_844_616_007,
        2_626_069_214_146_560,
    )
    assert emax < 36 * d
    pairs = [pair for pair in target_pairs(q, p, d, emax) if pair[0] % 9 in (0, 8)]
    by_r = {}
    for r, k, value in pairs:
        by_r.setdefault(r, []).append(k)
    assert {r: max(ks) for r, ks in by_r.items()} == {8: 3, 9: 2}

    check_mod7_phase(a, b, values)
    assert {value % 7 for value in values} == {0}
    pairs = [(r, k, value) for r, k, value in pairs if value % 7 == 0]
    assert {(r, k) for r, k, _ in pairs} == {(8, 0), (9, 0)}

    assert {value % 8 for value in values} == {0, 3}
    pairs = [(r, k, value) for r, k, value in pairs if value % 8 in {0, 3}]
    assert [(r, k) for r, k, _ in pairs] == [(8, 0)]
    assert {value % 16 for value in values} == {0, 3, 11}
    assert pairs[0][2] % 16 == 8


def check_exception_13_3() -> None:
    a, b = 13, 3
    q, p, d, rows = centered_rows(a, b)
    values = [value for _, value in rows]
    emax = max(values)
    assert (q, p, d, emax) == (
        2_251_799_813_685_248,
        1_853_020_188_851_841,
        398_779_624_833_407,
        24_479_047_857_451_008,
    )
    assert emax < 63 * d
    pairs = [pair for pair in target_pairs(q, p, d, emax) if pair[0] % 9 in (0, 8)]
    by_r = {}
    for r, k, value in pairs:
        by_r.setdefault(r, []).append(k)
    assert {r: max(ks) for r, ks in by_r.items()} == {8: 8, 9: 7, 17: 2, 18: 1}

    check_mod7_phase(a, b, values)
    assert {value % 7 for value in values} == {3}
    pairs = [(r, k, value) for r, k, value in pairs if value % 7 == 3]
    assert {(r, k) for r, k, _ in pairs} == {(8, 3), (9, 1)}

    assert {value % 8 for value in values} == {0, 3}
    pairs8 = [(r, k, value) for r, k, value in pairs if value % 8 in {0, 3}]
    assert [(r, k) for r, k, _ in pairs8] == [(8, 3)]
    assert pairs8[0][2] % 128 == 107

    prefix_table = {}
    for word, value in rows:
        prefix_table.setdefault(word[:3], set()).add(value % 128)
    assert {prefix: residues for prefix, residues in prefix_table.items()} == {
        "AAA": {3},
        "AAB": {67},
        "ABA": {43},
        "ABB": {43},
        "BAA": {48},
        "BAB": {48},
        "BBA": {0},
        "BBB": {0},
    }
    assert 107 not in {value % 128 for value in values}


def check_selected_two_macro_compositions() -> None:
    # Corroborate composition orientation only; the theorem is not inferred
    # from these finite checks.
    for a, b in [(8, 2), (9, 2), (12, 3), (13, 3)]:
        q, p, d, rows = centered_rows(a, b)
        alphabet = [value for _, value in rows]
        denominator = q * q - p * p
        for left in alphabet:
            for right in alphabet:
                numerator = p * left + q * right
                assert numerator % denominator != 0


def main() -> None:
    check_terminal_residue()
    check_uniform_gate()
    check_exception_8_2()
    check_exception_9_2()
    check_exception_12_3()
    check_exception_13_3()
    check_selected_two_macro_compositions()
    print("all independent L-9610/T-9609 checks passed")


if __name__ == "__main__":
    main()
