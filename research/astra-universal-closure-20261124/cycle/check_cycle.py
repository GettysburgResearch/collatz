"""Replay two rational controls and check the finite input to the all-clock argument."""

from fractions import Fraction
from math import gcd


def require(condition, message):
    if not condition:
        raise ValueError(message)


def odd_cycle(word):
    exponents = [int(digit) for digit in word]
    numerator = 0
    h = 0
    for exponent in exponents:
        numerator = 3 * numerator + 2**h
        h += exponent
    denominator = 2**h - 3**len(exponents)
    root = Fraction(numerator, denominator)
    value = root
    cycle = []
    for exponent in exponents:
        require(value.numerator % 2 == 1, "expected an odd site")
        cycle.append(value)
        value = (3 * value + 1) / 2**exponent
        require(value.denominator == root.denominator, "incorrect odd valuation")
    require(value == root and len(set(cycle)) == len(cycle), "cycle failed to close primitively")
    return numerator, denominator, cycle


def rank_rotation(cycle, base, shift):
    minimum = min(cycle)
    normalized = []
    for value in cycle:
        while value >= base * minimum:
            value /= base
        normalized.append(value)
    ordered = sorted(normalized)
    require(len(set(ordered)) == len(ordered), "normalized collision")
    ranks = [ordered.index(value) for value in normalized]
    for current, successor in zip(ranks, ranks[1:] + ranks[:1]):
        require((current + shift) % len(cycle) == successor, "incorrect cyclic rank shift")
    return ranks


def shortcut(n):
    return (3 * n + 13) // 2 if n % 2 else n // 2


def iterate(n, clocks):
    for _ in range(clocks):
        n = shortcut(n)
    return n


def check_basin():
    other = set()
    for root in (1, 13, 131, 211, 227, 251, 259, 287):
        cycle = []
        value = root
        while value not in cycle:
            require(len(cycle) < 70, "alternative cycle did not close")
            cycle.append(value)
            value = shortcut(value)
        require(value == root and other.isdisjoint(cycle), "alternative cycles overlap")
        other.update(cycle)
    require(len(other) == 70 and all(shortcut(n) in other for n in other), "closure failed")
    require(iterate(283, 70) not in other, "distinguished cycle entered the other set")
    required = [n for n in range(1, 579) if n < 283 or n % 3 == 0]
    require(all(iterate(n, 70) in other for n in required), "lower basin cutoff failed")
    require(iterate(579, 9) == 283 and 3 * 193 == 579, "tripling disagreement failed")
    return len(required)


def main():
    numerator, denominator, large = odd_cycle("12112212212212121212212121221221212121222")
    require((numerator, denominator) == (326313631156465704911, 420491770248316829),
            "41-step affine equation changed")
    require(gcd(numerator, denominator) == 19 and numerator % denominator != 0,
            "incorrect common divisor")
    minimum = min(large)
    require(minimum == Fraction(17174401639813984469, 22131145802542991),
            "incorrect 41-step minimum")
    require(max(large) < 8 * minimum / 3 and (minimum.numerator - minimum.denominator) % 18 == 0,
            "height or congruence failed")
    rank_rotation(large, 2, 65)

    _, _, small = odd_cycle("11222")
    require(min(small) == Fraction(283, 13), "incorrect five-odd-step minimum")
    rank_rotation(small, 2, 8)
    physical = [283, 431, 653, 986, 493, 746, 373, 566]
    require(all(shortcut(n) == target for n, target in zip(physical, physical[1:] + physical[:1])),
            "eight-clock orbit mismatch")
    rationals = [Fraction(n, 13) for n in physical]
    require([x for x in rationals if x.numerator % 2] == small, "odd clock mismatch")
    ranks = rank_rotation(rationals, 3, -5)
    require(ranks == [0, 3, 6, 1, 4, 7, 2, 5], "ternary order mismatch")
    count = check_basin()
    print(f"41-step gcd 19; eight-clock ternary ranks {ranks}; {count} lower sources certified.")


if __name__ == "__main__":
    main()
