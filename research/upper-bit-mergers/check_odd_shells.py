"""Certify the affine path and fixed binary words in ODD_TRIPLING_SHELLS."""

from check import walk


SLOPE = 2304
OFFSETS = (
    1152, 1536, 1440, 1472, 1470, 1467, 1468, 1476, 1488, 1584, 1632,
    1664, 1656, 1680, 1696, 1692, 1764, 1776, 1792, 1728, 1920, 2048,
    2016, 2112, 2176, 2160, 2448, 2496, 2560, 2544, 2576, 2574, 2610,
    2616, 2624, 2592, 2688, 2816, 2808, 2832, 2848, 2844, 2916, 2928,
    2944, 2880, 3072, 3024, 3120, 3136, 3132, 3144, 3152, 3150, 3186,
    3192, 3200, 3168, 3264, 3328, 3312, 3360, 3392, 3384, 3528, 3552,
    3584, 3456,
)
CROSSINGS = {6, 8, 15, 25, 29, 31, 41, 47, 53, 63}


def valuation(value, prime):
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def verify_chain():
    if (OFFSETS[0], OFFSETS[-1]) != (SLOPE // 2, 3 * SLOPE // 2):
        raise AssertionError("The chain must connect the two consecutive odd inputs.")
    scales = [SLOPE // 2]
    for index, (left, right) in enumerate(zip(OFFSETS, OFFSETS[1:])):
        lower, upper = sorted((left, right))
        distance = upper - lower
        if index in CROSSINGS:
            if distance % 2:
                raise AssertionError(("unequal half gaps", index))
            scale = distance // 2
            if SLOPE % (16 * scale) or (lower + scale) % (16 * scale):
                raise AssertionError(("crossing center", index))
        else:
            scale = distance
            if SLOPE % (6 * scale) or lower % (6 * scale) != 3 * scale:
                raise AssertionError(("odd tripling row", index))
        if SLOPE % scale:
            raise AssertionError(("scale does not divide smooth slope", index))
        scales.append(scale)
    scales.append(SLOPE // 2)
    for index, (offset, left_scale, right_scale) in enumerate(
        zip(OFFSETS, scales, scales[1:])
    ):
        if valuation(offset, 2) >= valuation(SLOPE, 2):
            if valuation(left_scale, 3) != valuation(right_scale, 3):
                raise AssertionError(("unbounded binary valuation at junction", index))
    return len(scales) - 2


def verify_words():
    for residue, clock, endpoint, odds in ((49, 12, 47, 5), (197, 13, 281, 6)):
        center = 16 * residue
        if walk(center - 1, clock) != (endpoint, odds):
            raise AssertionError(("lower word", center))
        if walk(center + 1, clock) != (endpoint, odds):
            raise AssertionError(("upper word", center))
    for odd in range(1, 512, 2):
        if not any((pow(3, j, 512) * odd) % 256 == 49
                   or (pow(3, j, 512) * odd) % 512 == 197 for j in range(128)):
            raise AssertionError(("missing synchronized class", odd))


if __name__ == "__main__":
    verify_words()
    print(f"{verify_chain()} localized affine edges and all junctions verified")
    print("2 synchronized words and all 256 odd classes modulo 512 verified")
