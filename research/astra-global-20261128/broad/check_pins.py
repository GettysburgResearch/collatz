"""Independent finite audits for the rational pin and greedy clock identities."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import comb
import json


def require(condition: bool, message: object) -> None:
    if not condition:
        raise ValueError(message)


def step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def twos(n: int) -> int:
    require(n > 0, ("positive valuation argument", n))
    return (n & -n).bit_length() - 1


def actual_events(n: int, e: int) -> tuple[list[int], int]:
    """Read the first e zero positions and the time of the next zero directly."""
    ones = time = 0
    before_zero = []
    while True:
        if n % 2:
            ones += 1
        elif len(before_zero) == e:
            return before_zero, time
        else:
            before_zero.append(ones)
        n = step(n)
        time += 1


def rational_pin(word: tuple[int, ...]) -> Fraction:
    z = Fraction(-1)
    for bit in reversed(word):
        z = (2 * z - 1) / 3 if bit else 2 * z
    return z


def expanded_pin(odds: list[int]) -> Fraction:
    return -1 - sum((2**j * Fraction(2, 3) ** u for j, u in enumerate(odds)), Fraction())


def check_all_words() -> dict[str, int]:
    words = tests = 0
    for length in range(10):
        for word in product((0, 1), repeat=length):
            odds = [sum(word[:j]) for j, bit in enumerate(word) if bit == 0]
            pin = rational_pin(word)
            require(pin == expanded_pin(odds), ("pin expansion", word))
            require(1 <= -pin <= 2 ** len(odds), ("archimedean pin interval", word))
            words += 1
            for source in range(1, 65):
                diff = source - pin
                depth = twos(diff.numerator)
                n = source
                for j in range(depth + 1):
                    bit = word[j] if j < length else 1
                    require((n % 2 == bit) == (j < depth), ("shared parity depth", source, word, j, depth))
                    n = step(n)
                tests += 1
    return {"parity_words": words, "source_word_pairs": tests}


def check_all_tuples() -> dict[str, int]:
    cases = tuples = max_depth = 0
    for source in range(1, 65):
        for e in range(5):
            actual, target = actual_events(source, e)
            modulus = 2 ** (target + 1)
            sentinel = target + 1
            ratio = 2 * pow(3, -1, modulus) % modulus
            powers = [pow(ratio, u, modulus) for u in range(sentinel + 1)]
            winners = []
            for us in combinations_with_replacement(range(sentinel + 1), e):
                residue = (source + 1 + sum(powers[u] << j for j, u in enumerate(us))) % modulus
                require(residue != 0, (source, e, us, "unexpected deeper competitor"))
                if residue == 2**target:
                    winners.append(us)
            require(winners == [tuple(actual)], (source, e, winners, actual))
            # All larger exponents contribute zero modulo this modulus.
            require(sentinel not in actual, ("sentinel in winning tuple", source, e, actual))
            tuples += comb(sentinel + e, e)
            cases += 1
            max_depth = max(max_depth, target)
    return {"source_arity_pairs": cases, "finite_tuple_classes": tuples, "max_depth": max_depth}


def check_periods() -> dict[str, int]:
    events = 0
    for h in range(2, 14):
        d = 3**h - 2 ** (h + 1)
        phases = [-1 - Fraction(2 ** (h - i) * 3**i, d) for i in range(h + 1)]
        require(all(z.denominator == d for z in phases), ("period denominator", h))
        for i, z in enumerate(phases):
            target = (3 * z + 1) / 2 if i < h else z / 2
            require(target == phases[(i + 1) % (h + 1)], ("period branch", h, i))
        for count in (1, 3, 7):
            length = count * (h + 1)
            modulus = 2 ** (length + 5)
            z = phases[0]
            source = modulus + z.numerator * pow(z.denominator, -1, modulus) % modulus
            x = source
            for i in range(length):
                require(x % 2 == (i % (h + 1) < h), ("ordinary shadow parity", h, count, i))
                x = step(x)
            require(x - z == Fraction(3**h, 2 ** (h + 1)) ** count * (source - z), ("shadow endpoint", h, count))
            events += length
    return {"periods": 12, "ordinary_shadow_steps": events}


def check_post_burst() -> dict[str, int]:
    # H_m is the unique solution class to 3^H = -7 mod 2^m.
    exponent = 2
    congruences = direct = affine = 0
    for m in range(4, 97):
        modulus = 1 << m
        if pow(3, exponent, modulus) != modulus - 7:
            exponent += 1 << (m - 3)
        require(0 < exponent < 1 << (m - 2), ("minimal exponent representative", m))
        require(exponent % 4 == 2 and pow(3, exponent, modulus) == modulus - 7, ("lift congruence", m))
        if exponent <= 10000:
            k = exponent - 1
            _, clock = actual_events((1 << k) - 1, 2)
            require(clock == k + twos(3 ** exponent + 7) and clock >= k + m, ("Mersenne clock", m, k))
            direct += 1
        congruences += 1
    for q in (1, 3, 5, 7, 9, 11, 101):
        for k in (1, 2, 7, 50, 113):
            y = q * 3**k - 1
            n = y
            evens_offset = odds = 0
            for t in range(51):
                z = n + 1
                numerator = q * 3**(k + odds) + evens_offset
                require(numerator == (1 << t) * z, ("post-burst affine identity", q, k, t))
                require(0 <= evens_offset <= 6**t, ("post-burst offset bound", q, k, t))
                require(twos(numerator) == t + twos(z), ("post-burst valuation", q, k, t))
                if n % 2:
                    odds += 1
                    evens_offset *= 3
                else:
                    evens_offset += 1 << t
                n = step(n)
                affine += 1
    return {"lift_moduli": congruences, "direct_mersenne_clocks": direct, "affine_steps": affine}


def main() -> None:
    result = {"all_words": check_all_words(), "all_tuples": check_all_tuples(), "periods": check_periods(), "post_burst": check_post_burst()}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
