"""Replay directed Collatz paths on a complete affine partition of the odd starts."""

from math import lcm


# S_h follows h ordinary steps, first odd and then even.
# I_h traverses such a path backwards. M triples an odd multiple of three.
CERTIFICATES = (
    (4, 1, "S2"),
    (12, 11, "I1"),
    (24, 15, "M S3 I1"),
    (36, 31, "I2 I1"),
    (48, 3, "S1 S3"),
    (72, 7, "S1 I3 I5 M M S3 S1 S3 I1 I2 I1 I1 M S5 I1 I2 M M M S1 S4 I2 I2 I2 I1 I1 I1 M S3 S7 I1"),
    (96, 27, "M S2 S3"),
    (96, 75, "S1 S2 S2"),
    (108, 19, "I2 I2 M S1 S5"),
    (144, 115, "S1 S3"),
    (288, 43, "S1 S2 S2"),
    (288, 187, "S1 I5 M M S3 S1 S4 I2 I2 I1 I1 M S7"),
    (324, 55, "I2 I2 I2 M S1 S4 S3"),
    (324, 91, "I2 I2 I1 I1"),
    (324, 199, "S1 S1 I5 I2 I2 I1 I1 M S8"),
    (324, 271, "I2 I2 I4 M M S3 S2 S3 I1 M S3 I1 I3 I3 I2 I1 I1 M S6 S2 S3"),
    (324, 307, "I2 I2 I1 M S2 S2 S3"),
    (972, 163, "I2 I2 I2 I2 M S1 S4 S2 S3"),
    (972, 811, "S1 I3 I3 I2 I1 I1 M S6"),
    (3888, 1459, "S1 S3"),
    (3888, 3403, "S1 S2 I4 M M S3 I5 I2 I2 I2 I2 I1 I1 I1 M S3 S10"),
    (7776, 2431, "I4 I1 M S2 S1 S1 S3 I1 I2 I1 M S2 S5"),
    (7776, 4375, "S1 S1 S3"),
    (7776, 6319, "S1 S1 I3 M M S4 I2 I1 I2 I3 M M S10"),
    (15552, 487, "S1 S1 I3 M M S7 I1"),
    (15552, 8263, "S1 S1 I3 M M S6 I8 I2 I2 I2 I2 I1 I1 I1 M S3 S10"),
)


def replay(modulus, residue, word, *, tripling_divisor=3, contraction=(9, 10),
           require_unit_target=False):
    slope, offset = modulus, residue
    steps = triplings = 0
    for token in word.split():
        if token == "M":
            if slope % (2 * tripling_divisor) or offset % (2 * tripling_divisor) != tripling_divisor:
                raise AssertionError(("ineligible tripling", modulus, residue, slope, offset))
            slope, offset = 3 * slope, 3 * offset
            steps += 1
            triplings += 1
        else:
            shift = int(token[1:])
            if shift < 1:
                raise AssertionError(("nonpositive clock", token))
            scale = 2**shift
            if token[0] == "S":
                if slope % 2 or offset % 2 != 1:
                    raise AssertionError(("ineligible odd input", slope, offset))
                numerator_slope, numerator_offset, denominator = 3 * slope, 3 * offset + 1, scale
            elif token[0] == "I":
                numerator_slope, numerator_offset, denominator = scale * slope, scale * offset - 1, 3
            else:
                raise AssertionError(("unknown move", token))
            slope, slope_rem = divmod(numerator_slope, denominator)
            offset, offset_rem = divmod(numerator_offset, denominator)
            if slope_rem or offset_rem:
                raise AssertionError(("nonintegral affine move", modulus, residue, token))
            if token[0] == "I" and (slope % 2 or offset % 2 != 1):
                raise AssertionError(("inverse fails to be odd", slope, offset))
            steps += shift
        if min(slope, offset) <= 0:
            raise AssertionError(("nonpositive affine output", modulus, residue, token))

    # Include all positive starts except the base vertex 1.
    start_index = int(residue == 1)
    initial = modulus * start_index + residue
    terminal = slope * start_index + offset
    if require_unit_target and (slope % 3 or not offset % 3):
        raise AssertionError(("target may be divisible by three", modulus, residue, slope, offset))
    numerator, denominator = contraction
    if denominator * terminal > numerator * initial or denominator * slope > numerator * modulus:
        raise AssertionError(("insufficient contraction", modulus, residue, slope, offset))
    return steps, triplings


def main():
    period = lcm(*(modulus for modulus, _, _ in CERTIFICATES))
    covered = set()
    total_steps = total_triplings = longest = 0
    for modulus, residue, word in CERTIFICATES:
        if modulus % 2 or residue % 2 != 1 or not 0 < residue < modulus:
            raise AssertionError(("invalid input class", modulus, residue))
        lifts = set(range(residue, period, modulus))
        if covered.intersection(lifts):
            raise AssertionError(("overlapping class", modulus, residue))
        covered.update(lifts)
        steps, triplings = replay(modulus, residue, word)
        longest = max(longest, steps)
        total_steps += steps
        total_triplings += triplings
    if covered != set(range(1, period, 2)):
        raise AssertionError("missing odd residue")
    if (len(CERTIFICATES), period, total_steps, total_triplings, longest) != (26, 15552, 444, 36, 61):
        raise AssertionError("certificate totals changed")
    print(f"{len(CERTIFICATES)} progressions partition all {len(covered)} odd residues modulo {period}")
    print(f"{total_steps} expanded moves include {total_triplings} eligible forward triplings; "
          f"longest path {longest}")
    print("Every start greater than 1 reaches a positive value at most nine tenths of its size")


if __name__ == "__main__":
    main()
