"""Check the stopped positive grid kernel using literal rational arithmetic."""

from collections import Counter
from fractions import Fraction


def require(condition):
    if not condition:
        raise RuntimeError("entrance kernel identity failed")


def consume(numerator, degree, marks):
    elapsed = 0
    for j in range(degree, degree - marks, -1):
        while numerator % 2 == 0:
            numerator //= 2
            elapsed += 1
        numerator = (numerator + 3 ** (j - 1)) // 2
        elapsed += 1
    return numerator, elapsed


def backward_count(numerator, depth, outer_degree, cutoff):
    if depth == 0:
        return int(numerator <= cutoff)
    child = 2 * numerator - 3**outer_degree
    total = 0
    # Any ancestor along a positive branch is at most max(cutoff, 3^original_degree).
    bound = max(cutoff, 3 ** (depth + outer_degree))
    if child > 0:
        while child <= bound:
            total += backward_count(child, depth - 1, outer_degree + 1, cutoff)
            child *= 2
    return total


def main():
    rows = atoms = 0
    for height in (1, 2, 5, 13):
        for degree in range(1, 7):
            cutoff = height * 3**degree
            for steps in range(1, degree + 1):
                counts = Counter(consume(u, degree, steps)[0] for u in range(1, cutoff + 1))
                remaining = degree - steps
                mass = Fraction()
                # The max stays below the original numerator bound at every step.
                for v in range(1, cutoff + 1):
                    actual = backward_count(v, steps, remaining, cutoff)
                    require(actual == counts[v])
                    mass += Fraction(actual, cutoff)
                    atoms += 1
                require(mass == 1)
                rows += 1
    print(f"Verified {rows} positive grids, {atoms} individual atoms and every normalization.")


if __name__ == "__main__":
    main()
