#!/usr/bin/env python3
"""Exact local certificate for separation of two limiting protection laws."""
from fractions import Fraction
from functools import cache


def require(condition, message):
    if not condition:
        raise ValueError(message)


def mirror_first_hit(start, even_budget):
    seen = set()
    value = start
    odds = evens = 0
    while value != 1 and value not in seen and evens <= even_budget:
        seen.add(value)
        if value % 2:
            value = (3 * value - 1) // 2
            odds += 1
        else:
            value //= 2
            evens += 1
    return (odds, evens) if value == 1 and evens <= even_budget else None


@cache
def stopped_mass(grade, residue):
    """Sum of squared gains at the first grade-th odd inverse in this ball."""
    if grade == 0:
        return Fraction(1)
    period = 2 * 3 ** (grade - 1)
    modulus = 3 ** (grade - 1)
    total = Fraction(0)
    for even_count in range(period):
        numerator = 2 ** (even_count + 1) * residue - 1
        if numerator % 3 == 0:
            child = (numerator // 3) % modulus
            gain_squared = Fraction(9, 4 ** (even_count + 1))
            total += gain_squared * stopped_mass(grade - 1, child)
    return total / (1 - Fraction(1, 4 ** period))


def routed_gain(residue, word):
    target = residue
    for letter in word:
        if letter == 'E':
            target *= 2
        else:
            require(letter == 'O' and target % 3 == 2, 'illegal reverse odd')
            target = (2 * target - 1) // 3
    return Fraction(3 ** word.count('O'), 2 ** len(word))


def offset(word):
    grade = intercept = 0
    for clock, letter in enumerate(word):
        if letter == 'O':
            intercept = 3 * intercept + 2 ** clock
            grade += 1
    return intercept - 3 ** grade


def deficits(word):
    from itertools import product
    return {word.count('O') - candidate.count('O')
            for candidate in map(''.join, product('EO', repeat=len(word)))
            if offset(candidate) == offset(word)}


def main():
    fixed = 60
    require(deficits('E') == {0} and deficits('EO') == {0, 1}, 'offset fibres')
    gain = routed_gain(2 * (fixed + 1) - 1, 'EOOOO')
    require(gain == Fraction(81, 32) and gain > 2, 'productive unit scale')
    print('N = 60 mod 81; deficit-one target 2N+1; reverse EOOOO gain', gain)
    known = ((1,), (), (3,), (), (11,), (15,), (29, 43), (39, 59))
    finite_sum = Fraction(0)
    for ell, expected in enumerate(known):
        pool = []
        for origin in range(1, 2 ** ell + 1, 2):
            receipt = mirror_first_hit(origin, ell)
            if receipt is not None and receipt[1] == ell:
                pool.append(origin)
                require(receipt[0] <= 2 * ell, 'first-hit mirror energy')
        require(tuple(pool) == expected, 'mismatched mirror origin row')
        prices = [stopped_mass(4, (2 ** ell * (fixed + 1) - m) % 81) / 4 ** ell
                  for m in pool]
        finite_sum += sum(prices)
        print(f'ell {ell}: origins {pool}; conditional charge {float(sum(prices)):.12f}')
    supremum = Fraction(12, 5) ** 4
    require(max(stopped_mass(4, z) for z in range(81)) <= supremum, 'S4 supremum')
    tail = supremum / 256
    gap = (1 - finite_sum - tail) / 81
    require(gap > Fraction(1, 100), 'strict one-point separation')
    print('finite charge', finite_sum)
    print('tail charge', tail)
    print('gap lower bound', gap)
    print(f'decimal lower bound {float(gap):.12f}')
    print('exact margin over 1/100', gap - Fraction(1, 100))


if __name__ == '__main__':
    main()
