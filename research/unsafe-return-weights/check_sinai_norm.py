"""Exact finite-level replay of the quadratic Syracuse density identity."""

from fractions import Fraction


def advance_density(density):
    modulus = 3 * len(density)
    period = 2 * len(density)
    updated = [Fraction(0) for _ in range(modulus)]
    denominator = 2**period - 1
    for exponent in range(1, period + 1):
        inverse_power = pow(2, -exponent, modulus)
        weight = Fraction(3 * 2 ** (period - exponent), denominator)
        for source, value in enumerate(density):
            target = (3 * source + 1) * inverse_power % modulus
            updated[target] += weight * value
    return updated


def quadratic_increment(density):
    modulus = len(density)
    total = Fraction(0)
    shifted = list(range(modulus))
    for lag in range(1, modulus + 1):
        shifted = [(4 * residue + 1) % modulus for residue in shifted]
        correlation = sum(value * density[image] for value, image in zip(density, shifted)) / modulus
        total += Fraction(2 * 4 ** (modulus - lag), 4**modulus - 1) * correlation
    assert shifted == list(range(modulus))
    return total


def mean_square(density):
    return sum(value**2 for value in density) / len(density)


def main():
    density = [Fraction(1)]
    for level in range(1, 6):
        next_density = advance_density(density)
        growth = quadratic_increment(density)
        assert sum(next_density) == len(next_density)
        assert mean_square(next_density) - mean_square(density) == growth > 0
        for residue, value in enumerate(density):
            assert sum(next_density[residue::len(density)]) == 3 * value
        print(f"Depth {level}: verified {len(next_density)} residues with exact fractions")
        density = next_density


if __name__ == "__main__":
    main()
