"""Stationary quotient masses of the tilted law and its two ordinary traces."""

from fractions import Fraction
from itertools import product


def require(truth):
    if not truth:
        raise ValueError("tilted integer trace check failed")


def odd_part(n):
    exponent = 0
    while n % 2 == 0:
        n //= 2
        exponent += 1
    return n, exponent


def least_odd(residue, modulus, sign):
    if sign == -1:
        return -least_odd(-residue, modulus, 1)
    n = residue % modulus
    return n if n % 2 else n + modulus


def quotient_next(previous):
    modulus = 3 * len(previous)
    period = 2 * len(previous)
    denominator = 4**period - 1
    coefficients = [Fraction(3 * 4 ** (period - e), denominator) for e in range(1, period + 1)]
    output = []
    for y in range(modulus):
        value = Fraction(0)
        source = y
        for weight in coefficients:
            source = (2 * source) % modulus
            if source % 3 == 1:
                value += weight * previous[(source - 1) // 3]
        output.append(value)
    require(sum(output) == 1)
    return output


def finite_paths(depth, max_gap, law):
    modulus = 3**depth
    recovered = {sign: set() for sign in (-1, 1)}
    selected_probability = [Fraction(0)] * modulus
    comparisons = 0
    for word in product(range(1, max_gap + 1), repeat=depth):
        # The input order here is physical forward time.
        numerator = 0
        denominator = 1
        for e in word:
            numerator = 3 * numerator + denominator
            denominator *= 2**e
        r = (numerator * pow(denominator, -1, modulus)) % modulus if modulus > 1 else 0
        probability = Fraction(3**depth, denominator**2)
        selected_probability[r] += probability
        for sign in (-1, 1):
            y = least_odd(r, modulus, sign)
            source = (denominator * y - numerator) // modulus
            require(source * sign > 0 and source % 2 and source not in recovered[sign])
            recovered[sign].add(source)
            value = source
            correction = Fraction(1)
            for e in word:
                correction *= Fraction(3 * value, 3 * value + 1)
                value, actual = odd_part(3 * value + 1)
                require(actual == e)
            require(value == y)
            likelihood = Fraction(3**depth, y * y)
            if sign == -1:
                likelihood *= Fraction(4, 9) ** depth
                correction *= Fraction(2, 3) ** depth
            require(probability * likelihood == correction**2 / source**2)
            require(correction <= 1)
            comparisons += 1
    require(all(p <= q for p, q in zip(selected_probability, law)))
    return comparisons


def posterior_checks(previous, following):
    # Group the period of all alternate gaps 1+2h at a digit-one output.
    modulus = len(previous)
    tested = 0
    for y, mass in enumerate(previous):
        if not mass:
            continue
        offset = (3 * y + 1) * pow(2, -1, 3 * modulus) % (3 * modulus)
        position = y
        alternative = Fraction(0)
        for h in range(1, modulus + 1):
            position = (4 * position + 1) % modulus
            alternative += Fraction(16 ** (modulus - h), 16**modulus - 1) * previous[position]
        require(position == y)
        require(following[offset] == Fraction(3, 4) * (mass + alternative))
        tested += 1
    return tested


def main():
    law = [Fraction(1)]
    comparisons = 0
    coordinates = 0
    posterior = 0
    for depth in range(6):
        modulus = len(law)
        coordinates += modulus
        require(max(law) <= Fraction(4, 5) ** depth)
        fixed_mass = law[(-1) % modulus]
        require(fixed_mass >= Fraction(3, 4) ** depth)
        for sign in (-1, 1):
            mean = sum(
                probability * Fraction(3**depth, least_odd(r, modulus, sign) ** 2)
                for r, probability in enumerate(law)
            )
            if sign == -1:
                mean *= Fraction(4, 9) ** depth
                require(mean >= 1)
            # Elementary rational upper bound on the odd reciprocal-square sum.
            require(mean < Fraction(5, 4))
        comparisons += finite_paths(depth, 5, law)
        if depth < 5:
            following = quotient_next(law)
            posterior += posterior_checks(law, following)
            law = following
    print("exact stationary quotient coordinates", coordinates)
    print("complete first-digit posterior sums over higher exponents", posterior)
    print("signed literal words, true exponent and weighted trace identities", comparisons)


if __name__ == "__main__":
    main()
