"""Verify descent with directed tripling restricted to odd multiples of nine."""

from math import gcd, lcm

from check_reverse_basin import replay


# Each row covers one integral progression. Rows may overlap.
# S_h advances h native steps; I_h traverses such a path backwards.
# M is the exceptional arrow, from an odd multiple of nine to its triple.
CERTIFICATES = (
    (12, 1, "S2"),
    (12, 5, "S2"),
    (18, 11, "I1"),
    (18, 17, "I1"),
    (48, 19, "S1 S3"),
    (48, 35, "S1 S3"),
    (54, 13, "I2 I1"),
    (54, 49, "I2 I1"),
    (96, 11, "S1 S2 S2"),
    (96, 43, "S1 S2 S2"),
    (96, 55, "S1 S1 S3"),
    (108, 95, "I1 M S3"),
    (144, 127, "S1 S1 I3 M S1 S1 S3 I1 I2 I1 I2 I3 M M S9 I1 I1"),
    (192, 79, "S1 S1 S1 S3 I1"),
    (216, 167, "S1 I7 I3 M M S5 S1 S1 S1 S1 S2 S1 I3 I1 I1 I1 I1 I1 I5 I1 I2 M S1 S2 S3 S1 S3 I1 I2 I3 I1 M S2 S1 S7 S3 I1 I2 I1 I1 I1 I2 I2 M S1 S5 S1 S3 I1 I2 I1 I2 I1 M S2 S5 I1"),
    (324, 31, "I2 I1 M S2 S3"),
    (324, 127, "I2 I2 M S1 S5"),
    (384, 7, "S1 S1 S2 S3"),
    (384, 187, "S1 S2 S1 S3"),
    (384, 283, "S1 S2 S1 S1 I3 M S1 S1 S3 I1 I2 I1 I2 I5 I2 M S1 S3 S1 S1 S4 I2 I2 I1 I1 M S9 I1 I1"),
    (384, 295, "S1 S1 I3 M M S8"),
    (432, 23, "S1 I5 I4 M M M M S12 I2 I2 I3 I3 M M S5 S4 I2 I4 I2 I5 M M S3 S1 S10 I2 I2 I2 I3 I2 M S1 S3 S4 I2 I2 M S1 S4 I2 I2 I2 I5 I2 I1 M S2 S2 S1 S1 S1 S5 S4 I2 I2 I2 I2 I2 I1 I2 I2 M S1 S14"),
    (432, 79, "S1 S1 I3 M S1 S1 S3 I1 I2 I3 I1 I3 M M M M S3 I1 I1 I2 I1 I1 I3 M S1 S1 S3 S1 S1 S9 I1 I4 I1 I1 I2 I1 I2 M S1 S2 S2 S1 S4 I2 I2 M S1 S4 I2 I2 I2 I1 I1 M S9 I1 I1"),
    (432, 239, "S1 I5 I4 M M M M S11 I1 I2 I3 I3 M M S5 S5 I3 I4 I2 I5 M M S3 S1 S9 I1 I2 I2 I3 I2 M S1 S3 S4 I2 I2 M S1 S4 I2 I2 I2 I5 I2 I1 M S2 S2 S1 S1 S1 S5 S3 I1 I2 I2 I2 I2 I1 I2 I2 M S1 S13 I1"),
    (576, 319, "S1 S1 S1 S1 I7 I3 I1 I2 M M S2 S2 S1 S1 S3 I1 I2 I1 M S2 S5 I1 I1 I1 I2 I2 I1 M S2 S2 S3 S1 S3 I1 I2 I1 I2 I3 I3 M M S5 S7 I1 I1 I1 I1"),
    (768, 199, "S1 S1 S2 S2 S2"),
    (768, 379, "S1 S2 S1 S2 S2"),
    (768, 475, "S1 S2 S1 S1 S3"),
    (768, 487, "S1 S1 I3 M M S7 S2"),
    (768, 583, "S1 S1 I3 M M S6 S3"),
    (864, 59, "S1 S2 I8 I3 I3 M M S5 S3 S1 S1 S1 S1 S1 S3 I1 I2 I1 I1 I1 I1 I3 I2 I3 I2 M S1 S3 S4 I2 I2 M S1 S7 S1 S1 S3 I1 I2 I1 I1 I1 M S3 S3 I1 I2 I3 I4 I2 I1 M M S1 S5 S3 S4 I2 I2 M S1 S3 I1 I2 I2 I1 I1 M S7"),
    (864, 91, "S1 I3 I1 M S2 S1 S5"),
    (864, 223, "I2 M M S2 S5"),
    (864, 295, "S1 I5 M M M S1 S1 S4 S3 I1 M M S1 I3 I2 I2 I2 I2 I1 I1 M S12 I2 I4 M M S3 I1 I3 I1 I3 M S1 S1 S10 I2 I2 I4 I2 I1 M M S1 S5 S4 I2 I2 I2 I1 M M S1 S4 I2 I2 I2 I1 I1 I1 M S3 S9"),
    (864, 347, "S1 I5 I4 M M M M S10 I2 I1 I1 M S7"),
    (864, 571, "S1 I3 I3 M M S5 S5"),
    (864, 583, "S1 I3 I5 M M M S1 S1 S10 I2 I4 I1 I4 I2 I1 M S2 S2 S1 S1 S5 S3 I1 I2 I2 I2 I1 M M S1 S4 I2 I4 I1 I1 I3 M S1 S1 S3 S1 S2 S3 S3 I1 I2 I2 I2 I2 I2 I1 I2 I1 M S2 S13"),
    (864, 799, "S1 I5 M M S3 I1 I3 I1 I3 M S1 S1 S7 S3 I1 I2 I1 I6 I3 M M S5 S1 S1 S1 S7 I1 I1 M M S1 I5 I3 I2 I1 I1 I1 I2 I2 M S1 S5 S1 S4 I2 I2 I1 I2 I1 M S2 S11 I1"),
    (1728, 367, "S1 I5 M M S3 S1 I5 I2 M S1 S3 S1 S1 S4 I2 I2 I1 I1 M S9 I1 I1 I5 I1 I4 I2 I1 M S2 S2 S1 S1 S5 S1 S3 I1 I2 I1 I2 I2 I1 M M S1 S4 I2 I4 I1 I1 I3 M S1 S1 S3 S1 S2 S3 S1 S3 I1 I2 I1 I2 I2 I2 I2 I1 I2 I1 M S2 S11 S3"),
    (1728, 1627, "S1 S2 S1 I3 I1 I3 I2 M S1 S3 S2 S5 I1"),
    (2592, 475, "I4 I4 M M S3 S2 S1 S3 S1 S3 I1 I2 I3 I2 I1 I2 M S1 S2 S2 S4 I2 M S1 S3 I1 I2 I2 I1 I1 I2 I3 I2 I1 M S2 S2 S1 S5 S5 I3 I2 I2 M S1 S4 I2 I2 I2 I1 I1 I1 M S3 S7"),
    (2592, 1051, "S1 I3 I1 I4 M M S3 S6 S3"),
    (2592, 1339, "S1 I3 I1 I2 M S1 S2 S4 S3"),
    (3456, 763, "I2 M M S2 S2 S3 I1 M S3 I1 I1"),
    (3456, 1531, "I6 M M S3 S1 S1 S7 I1 I1 M S3 I1 I1"),
    (3456, 1639, "I6 M M M S1 S1 S3 S1 S4 S3 I1 M S1 I3 I2 I2 I2 I1 I1 M S10 I2 I1 I3 I2 M S1 S3 I1 I2 I2 I3 M M S6 S7"),
    (3456, 2395, "S1 S2 I4 M M S3 S3 S1 S1 I5 I4 I2 I2 I1 I1 I1 I1 M S3 S1 S6 S2 I4 I1 I2 M S1 S2 S3 S2 S1 S2 S1 I3 I1 I3 I2 I2 I1 I2 I2 I1 I1 M S7 S3 S2 S6"),
    (5184, 1519, "S1 S1 I3 M S1 S1 S4 I2 I2 I3 I1 I1 I1 I2 M S1 S2 S1 S9"),
    (5184, 1759, "I2 I7 M M S3 S1 S1 S1 S7 I1 I1 M S3 I1 I1 I2 I1 I4 I1 I3 M S1 S1 S5 S2 S2 I4 I1 I3 I1 I4 M S1 S1 S1 S2 S2 S2 S3 S4 I2 I2 I2 I1 I1 I2 I1 M S2 S3 S6 I4 I2 I2 M S1 S4 I2 I2 I2 I1 I1 I4 M M S3 S3 S1 S1 S1 S1 S1 S1 S3 I1 I2 I1 I1 I1 I1 I1 I3 I2 M M S2 S1 S7 I1 I1 I1 I3 I2 I1 I1 M S6 S5"),
    (5184, 1915, "I4 I2 M S1 S3 S1 S4 S1 S1 I5 I2 I2 I1 I1 I1 M S3 S6 S4"),
    (5184, 2407, "S1 I3 I3 M S1 S1 S2 S1 I3 I1 I3 M S1 S1 S11 I1 M S1 I3 I2 I2 I2 M S1 S4 I2 I2 I2 I1 I1 I1 I4 M M S3 S3 S3 I1 I4 I2 M S1 S3 S1 S3 I1 I2 I1 M S2 S5 I1 I3 M S1 S1 S3 I1 I2 I1 I2 I1 I1 I2 I1 I1 M S5 S2 S7"),
    (5184, 2779, "S1 S2 S1 I3 I1 I5 I1 I2 M S1 S2 S3 S1 S7 I1"),
    (5184, 3055, "I2 I7 M M S3 S1 S1 S1 S8 I2 I1 M S2 S2 I4 I1 I2 I2 I2 I1 I2 I2 M S1 S11"),
    (5184, 3247, "I2 M M M S1 S3 S1 S3 I1 I2 I1 M M S1 S3 I1 I2 I2 I1 I5 I2 I2 M S1 S4 I2 I2 I2 I1 I1 M S9 S5"),
    (5184, 3487, "S1 S1 I3 M S1 S1 S3 I1 I2 I1 I2 I1 I5 I4 M M S3 S2 S1 S2 S2 S3 I1 M S6 I2 I4 I2 M S1 S3 I1 I2 I2 I1 I1 I2 I1 I1 I1 M S3 S3 S2 S2 S1 S1 S1 I5 I2 M S1 S3 I1 I2 I2 I1 I1 I1 M S3 I1 I1 I2 I1 I1 M S5 S2 S1 S7 I1 I1"),
    (5184, 4507, "I4 I2 M S1 S3 S1 S4 S1 S2 I6 I2 I2 I1 I1 I1 M S3 S6 S3"),
    (5184, 4783, "S1 I3 I3 M M S5 I1 I4 I4 I2 M S1 S3 S1 S2 S1 S3 S1 S4 S1 I3 I3 I2 I2 I1 I2 I1 M S2 S8 I2 I2 I1 M S2 S2 S5 I1 I1 I4 I2 M S1 S3 S1 S3 I1 I2 I1 M M S1 S3 I1 I2 I2 I1 I1 I3 I1 I2 M S1 S2 S5 S5 I3 I2 I1 I2 I2 I3 M M S6 S6"),
    (5184, 4795, "I6 I3 M M S5 S1 S1 S1 S7 I1 I1 M M S1 I5 I3 I2 I1 I1 I1 I2 I2 M S1 S5 S1 S4 I2 I2 I1 I2 I1 M S2 S11"),
    (5184, 4975, "S1 S1 I3 M S1 S1 S4 I2 I2 I1 I2 I5 I2 I1 M S2 S2 S1 S1 S1 S4 I2 I2 I1 I1 M S11"),
    (6912, 871, "S1 I5 M M S3 I1 I1 I2 I3 M M S7 S1 S4 I2 I2 I3 I1 I2 M S1 S2 S4 S2 S5"),
    (6912, 3835, "S1 S2 S1 S2 I4 M M S3 I1 I1 I2 I1 I1 I1 I2 M S1 S2 S1 S3 S5"),
    (6912, 4699, "S1 S2 I4 M M S3 I1 I1 I2 I1 I5 M M S3 S1 S2 S4 S1 I3 I1 I2 M S1 S2 S5 S3 I1 I2 I1 I2 I2 I1 I3 I2 M M S2 S1 S4 S2 S3 I1 M S3 I1 I1 I2 I1 I3 I2 I1 M M S1 S9 I1 I2 M M M S1 S3 I1 I4 I1 I1 I1 I1 I1 I2 M M S2 S5 S5"),
    (6912, 6247, "S1 I3 I1 M S2 S1 S2 I4 M M S3 I1 I3 I1 I1 I1 I2 M S1 S2 S1 S5 S7"),
    (7776, 2203, "S1 I3 I3 I1 I2 M S1 S2 S4 S1 S5"),
    (10368, 3943, "I2 I6 M M S3 S1 S1 S2 S4 S2 S2 I8 I2 I1 I2 I1 M S2 S6 I2 I1 I1 I2 I4 I1 I2 M S1 S2 S3 S5 S3 I1 I2 I2 I3 M M S6 S7"),
    (10368, 7399, "I4 I1 M S2 S1 S1 S3 S1 S1 S3 I1 I2 I1 I3 I2 M S1 S3 I1 I2 I2 I3 M M S6 S7"),
    (10368, 9319, "S1 S1 S2 S1 S1 S1 I5 I2 M S1 S3 I1 I2 I2 I1 I3 I1 I2 M S1 S2 S9 S1 S1 I7 I1 I2 I1 I1 M S5 I3 I1 I2 I3 M S1 S1 S2 S2 S3 I1 M S3 I1 I1 I2 I1 M M S1 S3 I1 I2 I2 I1 I1 I1 I2 I1 M S2 S3 S1 S5 S3 S1 I5 I2 I2 I1 I2 I1 M S2 S8 S6"),
    (20736, 5371, "S1 S2 S1 I3 I1 I5 I1 I2 M S1 S2 S3 S1 S6 S3"),
    (20736, 10855, "S1 S1 I3 M M S7 I5 I1 I2 I1 I1 I2 M M S2 S3 S1 S4 I2 I2 I1 I2 M M S2 S2 S2 S3 I1 M S3 I1 I1 I2 I1 I3 I2 M S1 S3 I1 I2 I2 I3 M M S6 S7"),
    (62208, 38491, "I4 I2 I1 M S2 S2 S1 S1 S4 S1 S3 I1 I2 M M M S1 S3 I1 I2 I2 I1 I1 I1 I3 I2 I1 I2 M S1 S2 S2 S5 S1 S5"),
    (62208, 59227, "S1 S2 S1 S1 I3 M M S6 I4 I1 I2 I1 I1 I1 I2 I1 I1 M S5"),
)


def main():
    period = lcm(*(modulus for modulus, _, _ in CERTIFICATES))
    covered = set()
    total_moves = total_triplings = maximum_moves = 0
    for modulus, residue, word in CERTIFICATES:
        if modulus % 6 or gcd(residue, 6) != 1 or not 0 < residue < modulus:
            raise AssertionError(("invalid unit class", modulus, residue))
        moves, triplings = replay(modulus, residue, word, tripling_divisor=9,
                                  contraction=(24, 25), require_unit_target=True)
        covered.update(range(residue, period, modulus))
        total_moves += moves
        total_triplings += triplings
        maximum_moves = max(maximum_moves, moves)
    if covered != {r for r in range(period) if gcd(r, 6) == 1}:
        raise AssertionError("missing input class")
    if (len(CERTIFICATES), period, total_moves, total_triplings, maximum_moves) != (71, 62208, 3974, 284, 198):
        raise AssertionError("certificate totals changed")
    print(f"{len(CERTIFICATES)} paths cover all {len(covered)} unit residues modulo {period}")
    print(f"{total_moves} expanded moves, {total_triplings} eligible forward triplings, "
          f"maximum path length {maximum_moves}; contraction at most 24/25")


if __name__ == "__main__":
    main()
