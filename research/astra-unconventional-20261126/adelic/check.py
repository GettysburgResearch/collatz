#!/usr/bin/env python3
"""Exact local replay for the squareclass packet; no floating point or convergence oracle."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import json
from math import isqrt, prod


def require(condition: bool, label: str) -> None:
    if not condition:
        raise ValueError(label)


def odd_step(n: int) -> tuple[int, int]:
    y = 3 * n + 1
    a = (y & -y).bit_length() - 1
    return a, y >> a


def square(n: int) -> bool:
    return isqrt(n) ** 2 == n


def dependent(xs: tuple[int, ...]) -> bool:
    return any(square(prod(rows)) for k in range(1, len(xs) + 1) for rows in combinations(xs, k))


def shortcut(n: int) -> int:
    return (3 * n + 1) // 2 if n % 2 else n // 2


def elementary(w: tuple[int, ...]) -> list[int]:
    e = [1]
    for value in w:
        e.append(0)
        for j in range(len(e) - 1, 0, -1):
            e[j] += value * e[j - 1]
    return e


def grid_numerator(k: int, w: tuple[int, ...]) -> tuple[int, int]:
    e = elementary(w)
    if k == 1:
        return e[1], 2
    if k == 2:
        return 4 * e[2] - e[1] ** 2, 8
    return 8 * e[3] - 4 * e[1] * e[2] + e[1] ** 3, 16


def sqrt_approx(offsets: tuple[Fraction, ...], n: int) -> Fraction:
    k = len(offsets) // 2
    e = elementary(offsets)
    c = [Fraction(1)]
    for j in range(1, k + 1):
        c.append((e[j] - sum(c[l] * c[j - l] for l in range(1, j))) / 2)
    return sum(y * n ** (k - j) for j, y in enumerate(c))


def check_growth() -> dict[str, int]:
    total = growth = compensated = 0
    for x in range(1, 100_002, 2):
        a, y = odd_step(x)
        b, z = odd_step(y)
        c, w = odd_step(z)
        total += 1
        if a != 1:
            require(x == 1 or y < x, 'ordinary decrease')
            continue
        growth += 1
        require(2 ** (b + 1) * z == 9 * x + 5, 'two-step carry')
        require(dependent((x, y, z)) == square(z), 'rank-three local equivalence')
        if square(z):
            compensated += 1
            require(b >= 2 and c == 2 and (x < 5 or w < x), 'three-step compensation')
    u = v = 1
    for _ in range(70):
        require(u % 2 == v % 2 == 1 and 4 * v * v == 3 * u * u + 1, 'Pell invariant')
        require(odd_step(u * u) == (2, v * v), 'Pell ordinary edge')
        u, v = 7 * u + 8 * v, 6 * u + 7 * v
    return dict(odd_sources=total, growth_triples=growth, dependent_growth_triples=compensated,
                pell_pairs=70)


def check_convergent_words() -> dict[str, int]:
    words = steps = 0
    for length in range(9):
        for word in product(range(2), repeat=length):
            carry = s = 0
            for i, bit in enumerate(word):
                if bit:
                    carry = 3 * carry + 2 ** i
                    s += 1
            mod = 3 ** s
            period = 2 * 3 ** (s - 1) if s else 1
            e0 = next(e for e in range(period) if (2 ** (length + e) - carry) % mod == 0)
            for e in (e0 + period, e0 + 2 * period):
                x = (2 ** (length + e) - carry) // mod
                require(x > 0, 'ordinary source positivity')
                for bit in word:
                    require(x % 2 == bit, 'exact requested parity')
                    x = shortcut(x)
                    steps += 1
                require(x == 2 ** e, 'literal endpoint hitting one')
            words += 1
    return dict(parity_words=words, terminal_power_paths=2 * words, shortcut_steps=steps)


def check_mixed_grid() -> dict[str, int]:
    checked = 0
    # The first thirteen states of both these high ordinary examples are >= their source.
    for n in (2 ** 73 - 1, 2 ** 94 - 1):
        x = n
        clock = 0
        rows = []
        for i in range(13):
            require(x >= n, 'no-descent fixture')
            z = Fraction(2 ** clock * x, 3 ** i)
            rows.append(z)
            require(0 <= z - n <= Fraction(i, 3), 'archimedean offsets')
            a, x = odd_step(x)
            clock += a
        for k in (1, 2, 3):
            for ix in combinations(range(13), 2 * k):
                h = max(ix)
                zsub = tuple(rows[i] for i in ix)
                ws = tuple(z * 3 ** h for z in zsub)
                require(all(x.denominator == 1 for x in ws), 'common ternary denominator')
                w = tuple(x.numerator for x in ws)
                require(sum(x % 3 != 0 for x in w) == 1, 'precisely one ternary unit')
                p, denominator = grid_numerator(k, w)
                require(p % 3 != 0 and prod(w) % 3 == 0, 'ternary separation')
                Q = sqrt_approx(tuple(z - n for z in zsub), n)
                require(Fraction(p, denominator * 3 ** (h * k)) == Q, 'translation of truncation')
                # Equivalence to |sqrt(P)-Q| < 80/n without numerical square-root evaluation.
                P = prod(zsub)
                err = Fraction(80, n)
                require(Q > err and (Q - err) ** 2 < P < (Q + err) ** 2, 'archimedean grid bound')
                require(not square(P.numerator) or not square(P.denominator), 'no normalized square')
                checked += 1
    require(80 * 16 * 3 ** 36 < 2 ** 71, 'external base numerical interface')
    absolute = []
    for k in (1, 2, 3):
        c = [Fraction(1)]
        for j in range(1, k + 2):
            c.append(abs(c[-1] * (Fraction(1, 2) - j + 1) / j))
        coeff = [Fraction(1)] + [Fraction(0)] * (k + 1)
        for _ in range(2 * k):
            coeff = [sum(coeff[t] * c[j - t] for t in range(j + 1)) for j in range(k + 2)]
        absolute.append(coeff[-1])
    require(absolute == [Fraction(1, 2), Fraction(3, 2), Fraction(135, 32)], 'Taylor constants')
    return dict(checked_even_subsets=checked, exact_absolute_taylor_coefficients=len(absolute),
                cutoff_product=80 * 16 * 3 ** 36, published_base=2 ** 71)


def check_dyadic() -> dict[str, int]:
    for x in range(1, 20_000, 2):
        a, _ = odd_step(x)
        minus_one = 1 if x % 4 == 1 else -1
        two = 1 if x % 8 in (1, 7) else -1
        require(4 * a >= 7 + 3 * minus_one - two - minus_one * two, 'dyadic bias inequality')
    return {'odd_sources': 10_000}


if __name__ == '__main__':
    print(json.dumps({'growth': check_growth(), 'convergent_controls': check_convergent_words(),
                      'mixed_grid': check_mixed_grid(), 'dyadic': check_dyadic()},
                     indent=2, sort_keys=True))
