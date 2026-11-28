"""Exact finite collision and literal common-prefix checks for the fair gap law."""

from fractions import Fraction


def check(condition):
    if not condition:
        raise ValueError("finite collision genealogy identity failed")


def gap_classes(depth):
    """Each class has its fair mass and the sum of squared literal masses."""
    modulus = 3**depth
    period = 2 * (modulus // 3)
    return [
        (
            pow(2, e, modulus),
            Fraction(2 ** (period - e), 2**period - 1),
            Fraction(4 ** (period - e), 4**period - 1),
        )
        for e in range(1, period + 1)
    ]


def lift(suffix, classes, law):
    """Transfer a joint or one-word probability through one outer branch."""
    modulus = 3 * len(suffix)
    lifted = []
    for root in range(modulus):
        value = Fraction()
        for power, fair_mass, literal_pair_mass in classes:
            numerator = (power * root - 1) % modulus
            if numerator % 3:
                continue
            if law == "fair":
                coefficient = fair_mass
            elif law == "same":
                coefficient = literal_pair_mass
            elif law == "tilted":
                coefficient = 3 * literal_pair_mass
            else:
                raise ValueError("unrecognized outer letter law")
            value += coefficient * suffix[numerator // 3]
        lifted.append(value)
    return lifted


def split_mass(root, suffix, classes):
    """Two independent distinct first gaps; equal period classes may split."""
    modulus = 3 * len(suffix)
    parts = []
    for power, fair_mass, literal_pair_mass in classes:
        numerator = (power * root - 1) % modulus
        if numerator % 3 == 0:
            parts.append((suffix[numerator // 3], fair_mass, literal_pair_mass))

    mass = Fraction()
    for i, (left, fair, literal_pair) in enumerate(parts):
        mass += (fair * fair - literal_pair) * left * left
        for right, other_fair, _ in parts[i + 1 :]:
            mass += 2 * fair * other_fair * left * right
    return mass


def main():
    fair = [Fraction(1)]
    tilted = [[Fraction(1)]]
    common = [[Fraction(1)]]
    energies = [Fraction(1)]
    defects = 0
    cells = 0
    prefix_cells = 0
    for depth in range(1, 5):
        modulus = 3**depth
        classes = gap_classes(depth)
        check(sum(w for _, w, _ in classes) == 1)
        check(sum(v for _, _, v in classes) == Fraction(1, 3))
        grouped = sum(w * w for _, w, _ in classes)
        check(grouped > Fraction(1, 3))
        if depth == 1:
            check(grouped == Fraction(5, 9))
        defects += 1

        next_fair = lift(fair, classes, "fair")
        tilted.append(lift(tilted[-1], classes, "tilted"))
        next_common = [[p * p for p in next_fair]] + [
            lift(suffix, classes, "same") for suffix in common
        ]
        energies.append(modulus * sum(next_common[0]))
        direct_split = [split_mass(y, fair, classes) for y in range(modulus)]
        for y, mass in enumerate(direct_split):
            check(mass == next_common[0][y] - next_common[1][y])
            cells += 1
        check(modulus * sum(direct_split) == energies[-1] - energies[-2])

        for length, row in enumerate(next_common):
            partition = 3**length
            check(modulus * sum(row) == energies[depth - length])
            for residue in range(partition):
                check(
                    modulus * sum(row[residue::partition])
                    == energies[depth - length] * tilted[length][residue]
                )
                prefix_cells += 1
            if length < depth:
                check(
                    modulus * (sum(row) - sum(next_common[length + 1]))
                    == energies[depth - length] - energies[depth - length - 1]
                )
        fair, common = next_fair, next_common
    print("distinct-letter root cell identities", cells)
    print("literal common-prefix angular projections", prefix_cells)
    print("grouped-action equality errors rejected", defects)


if __name__ == "__main__":
    main()
