"""Replay one literal positive rational orbit used for the finite local tests."""

from fractions import Fraction
from math import gcd

WORD = (
    "1011100110010111101101000010011000001111101100111111101011001001"
    "0111111101110110111110110011100101011001010111001110111011101000"
    "11011011001000110110111011011011101111111001111111101110"
)


def require(test, message):
    if not test:
        raise ValueError(message)


def main():
    length = len(WORD)
    weight = WORD.count("1")
    require((length, weight) == (184, 116), "wrong clock")
    carry = 0
    for i, bit in enumerate(WORD):
        if bit == "1":
            carry = 3 * carry + 2**i
    defect = 2**length - 3**weight
    start = Fraction(carry, defect)
    denominator = start.denominator
    require(gcd(carry, defect) == 5, "inspected factor does not cancel")
    require(denominator % 7 == 0, "missing forced denominator factor")
    require(gcd(denominator, 180) == 1, "source has a local pole")
    require((start.numerator - 157 * denominator) % 180 == 0, "wrong source residue")

    phases = set()
    current = start
    for bit in WORD:
        require(current not in phases, "period is imprimitive")
        phases.add(current)
        require(current.denominator == denominator, "denominator changed")
        require(current.numerator % 2 == int(bit), "parity mismatch")
        if bit == "1":
            current = (3 * current + 1) / 2
        else:
            current /= 2
    require(current == start, "did not return")
    smallest = min(phases)
    require(48 < smallest < 49, "wrong minimum")
    print(f"primitive period {length}, odd steps {weight}, residue 157 modulo 180")
    print(f"cancelled gcd 5, reduced denominator {denominator}")
    print(f"cycle minimum {smallest}")


if __name__ == "__main__":
    main()
