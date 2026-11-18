"""Check the native, minimal-period and bilateral identities over finite supports."""

from itertools import combinations


def reflected_orbits(modulus):
    return sorted({tuple(sorted({j, (-1 - j) % modulus})) for j in range(modulus)})


def check_modulus(modulus):
    orbits = reflected_orbits(modulus)
    masks = [frozenset(j for orbit in subset for j in orbit)
             for length in range(len(orbits) + 1)
             for subset in combinations(orbits, length)]
    period = 9 * modulus
    true_period = 0

    for mask in masks:
        def bit(j):
            return int(j % 9 == 3 and ((j - 3) // 9) % modulus in mask)

        def exponent(j):
            return 36 * j * (j + 3) + j % 9 + 9 * bit(j)

        def height(j):
            return 8 * (j + 1) - int(j % 9 == 0) + bit(j) - bit(j - 1)

        assert height(0) == 7 and exponent(0) == 0
        increments = [height(j) - height(j - 1) for j in range(period)]
        assert min(increments) >= 5
        for j in range(-period, period + 1):
            assert exponent(j) - exponent(j - 1) == 9 * height(j) + 1
            assert bit(-3 - j) == bit(j)
            if bit(j):
                assert exponent(j) - 9 == 9 * (2 * j + 3) ** 2 - 78

        minimal = next(t for t in range(1, period + 1)
                       if period % t == 0 and increments[t:] + increments[:t] == increments)
        true_period += minimal == period
        # Reflection maps the positive support to the whole negative support.
        positive = {2*j + 3 for j in range(period) if bit(j)}
        both = {2*j + 3 for j in range(-period - 2, period) if bit(j)}
        assert both == positive | {-n for n in positive}

    assert true_period == 2 ** ((modulus + 1) // 2) - 2
    return len(masks), true_period


if __name__ == "__main__":
    for prime in (3, 5, 7, 11, 13, 17):
        total, primitive = check_modulus(prime)
        print(f"period {9 * prime}: {total} masks, {primitive} of exact period")
