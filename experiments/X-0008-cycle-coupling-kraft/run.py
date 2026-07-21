#!/usr/bin/env python3
from fractions import Fraction
from math import log


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def P(v: int) -> int:
    return v // 2 if v % 2 == 0 else (3 * v - 1) // 2


def C(v: int) -> int:
    return 3 * v // 2 if v % 2 == 0 else (v + 1) // 2


def coupled_step(q: int, v: int) -> tuple[int, int]:
    p = q & 1
    r = v & 1
    e = p ^ r
    q1 = (3**e * q + p) // 2
    v1 = (3**e * v + (2 * p - 1) * r) // 2
    assert T(q - v) == q1 - v1
    return q1, v1


def odd_count_on_P(v: int, steps: int) -> int:
    a = 0
    for _ in range(steps):
        a += v & 1
        v = P(v)
    return a


def accelerated(q: int, v: int) -> tuple[int, int, int]:
    assert q > 0
    k = 0
    m = q
    while m % 2 == 0:
        m //= 2
        k += 1
    w = v
    a = 0
    for _ in range(k):
        a += w & 1
        w = P(w)
    g = a + (1 if w % 2 == 0 else 0)
    q1 = (3**g * m + 1) // 2
    v1 = C(w)
    qq, vv = q, v
    for _ in range(k + 1):
        qq, vv = coupled_step(qq, vv)
    assert (qq, vv) == (q1, v1)
    return q1, v1, k


V11 = [136, 68, 34, 17, 25, 37, 55, 82, 41, 61, 91]
V3 = [5, 7, 10]
TARGETS = set(V11 + V3 + [1])


def basin_data(w: int) -> tuple[int, int, int, list[int]]:
    z = C(w)
    x = z
    r = 0
    b = 0
    path = []
    while x not in TARGETS:
        path.append(x)
        b += x & 1
        x = P(x)
        r += 1
    return r, b, x, path


def verify_cycle_tower() -> list[tuple]:
    v0 = 136
    cycle_len = 11
    cycle_odds = 7
    rows = []
    w = v0
    A = 0
    for k0 in range(cycle_len):
        r, b, target, _ = basin_data(w)
        delta = 1 if w % 2 == 0 else 0
        g0 = A + delta
        base_length = k0 + r + 1
        base_odds = g0 + b
        modulus = 1 << (r + 1)
        m0 = (-pow(3, -g0, modulus)) % modulus
        assert m0 & 1

        for t in range(4):
            k = k0 + t * cycle_len
            g = g0 + t * cycle_odds
            mod = 1 << (r + 1)
            mt = (-pow(3, -g, mod)) % mod
            q = (1 << k) * mt
            q1 = 3**b * (3**g * mt + 1) // (1 << (r + 1))
            steps = base_length + t * cycle_len
            odds = base_odds + t * cycle_odds
            n = q - v0
            x = n
            got_odds = 0
            for _ in range(steps):
                got_odds += x & 1
                x = T(x)
            assert x == q1 - target
            assert got_odds == odds
            N = 3**odds
            M = 1 << steps
            digit = N * q - M * q1
            assert digit == -(1 << k) * 3**b

        rows.append((k0, w, r, b, target, base_length, base_odds, m0))
        A += w & 1
        w = P(w)

    assert w == v0 and A == cycle_odds
    return rows


def kraft_data(code: list[tuple[int, ...]]) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    kraft = sum(Fraction(1, 2 ** len(w)) for w in code)
    tilted = sum(Fraction(3 ** sum(w), 4 ** len(w)) for w in code)
    expected_length = sum(Fraction(len(w), 2 ** len(w)) for w in code)
    expected_odds = sum(Fraction(sum(w), 2 ** len(w)) for w in code)
    expected_multiplier = sum(
        Fraction(1, 2 ** len(w)) * Fraction(3 ** sum(w), 2 ** len(w))
        for w in code
    )
    for w in code:
        fair = Fraction(1, 2 ** len(w))
        biased = Fraction(3 ** sum(w), 4 ** len(w))
        multiplier = Fraction(3 ** sum(w), 2 ** len(w))
        assert biased / fair == multiplier
    assert kraft == 1
    assert tilted == 1
    assert expected_multiplier == 1
    assert expected_odds * 2 == expected_length
    mean_log = float(expected_odds) * log(3) - float(expected_length) * log(2)
    exact_formula = 0.5 * log(3 / 4) * float(expected_length)
    assert abs(mean_log - exact_formula) < 1e-15
    assert mean_log < 0
    return kraft, tilted, expected_length, expected_odds


def verify_kraft() -> tuple[Fraction, Fraction, Fraction, Fraction]:
    codes = [
        [(0,), (1,)],
        [(0,), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 0), (1, 1)],
        [(0,), (1, 0), (1, 1, 0), (1, 1, 1)],
    ]
    for code in codes:
        kraft_data(code)
    return kraft_data(codes[-1])


def main() -> None:
    for v in range(1, 301):
        for q in range(1, 1001):
            q1, v1 = coupled_step(q, v)
            assert q1 - v1 == T(q - v)
            if q > v:
                assert q1 > v1

    for v in V11 + V3 + [1]:
        for q in range(1, 5000):
            q1, v1, k = accelerated(q, v)
            assert k >= 0 and q1 > 0 and v1 > 0
    print('verified synchronous coupling and valuation acceleration')

    rows = verify_cycle_tower()
    print('negative-11-cycle complement basin table:')
    for row in rows:
        print(
            'k=%d phase=%d r=%d b=%d target=%d L0=%d a0=%d m0=%d'
            % row
        )

    # Exact grouped base families from phase 136.
    first = [row for row in rows if row[0] <= 6]
    second = [row for row in rows if row[0] >= 7]
    assert {(r[4], r[5], r[6]) for r in first} == {(7, 9, 3)}
    assert {(r[4], r[5], r[6]) for r in second} == {(34, 13, 7)}
    residues_9 = [((1 << r[0]) * r[7]) % 512 for r in first]
    residues_13 = [((1 << r[0]) * r[7]) % 8192 for r in second]
    assert residues_9 == [341, 170, 340, 504, 336, 224, 320]
    assert residues_13 == [640, 3840, 2560, 7168]
    print('phase-136 base transfers:', residues_9, residues_13)

    lam = Fraction(2187, 2048)
    t1 = 0
    x = Fraction(27, 512)
    while x <= 1:
        x *= lam
        t1 += 1
    t2 = 0
    y = Fraction(2187, 8192)
    while y <= 1:
        y *= lam
        t2 += 1
    assert (t1, t2) == (45, 21)
    print('first supercritical padding levels:', t1, t2)

    kraft, tilted, elen, eodd = verify_kraft()
    print(
        'verified Collatz-Kraft identities:',
        f'kraft={kraft}',
        f'tilted={tilted}',
        f'E[L]={elen}',
        f'E[a]={eodd}',
    )
    print('all cycle-coupling and Kraft checks passed')


if __name__ == '__main__':
    main()
