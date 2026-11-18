"""Exact odd-shell replay for the finite distortion cutoff.

Columns are power k (X = 2**k), s, fixed odd-step clock q, number of odd
sources, count that reach 1 by q, and mean V in outward-rounded millionths.
The integer clocks are part of the finite experiment. They were obtained
by evaluating max(0, floor(h/d + s*sqrt(2*log(2)**2*h/d**3))) with
60-decimal precision, h = k*log(2), d = log(4/3).
"""
import argparse


CLOCKS = {
    10: (0, 7, 24, 40, 57),
    14: (0, 13, 33, 53, 73),
    18: (0, 20, 43, 65, 88),
    22: (3, 28, 53, 77, 102),
}
INTERNAL_SCALE = 10**12
MILLION = 10**6


def replay(power):
    clocks = CLOCKS[power]
    scaled_powers = [INTERNAL_SCALE * 3**q for q in clocks]
    sums = [0] * len(clocks)
    inexact = [0] * len(clocks)
    hits = [0] * len(clocks)
    limit = 1 << power
    count = limit // 4

    for source in range(limit // 2 + 1, limit, 2):
        state = source
        valuation = 0
        depth = 0
        for index, q in enumerate(clocks):
            while depth < q and state != 1:
                value = 3 * state + 1
                shift = (value & -value).bit_length() - 1
                state = value >> shift
                valuation += shift
                depth += 1
            if state == 1:
                # U(1) = 1 with valuation 2 at every subsequent step.
                valuation += 2 * (q - depth)
                depth = q
                hits[index] += 1

            truncated, remainder = divmod(source * scaled_powers[index], state << valuation)
            sums[index] += truncated
            inexact[index] += bool(remainder)

    divisor = count * (INTERNAL_SCALE // MILLION)
    for index, q in enumerate(clocks):
        # Each discarded remainder contributes strictly less than one internal unit.
        lower = sums[index] // divisor
        upper = (sums[index] + inexact[index] + divisor - 1) // divisor
        assert 0 <= lower <= upper <= MILLION
        yield power, index - 2, q, count, hits[index], lower, upper


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("powers", nargs="*", type=int, metavar="k",
                        help="one or more of 10, 14, 18, 22 (default: 10 14 18)")
    args = parser.parse_args()
    print("k s q sources reached_1 lower_ppm upper_ppm")
    for power in args.powers or (10, 14, 18):
        if power not in CLOCKS:
            parser.error(f"unsupported k={power}; use one of {tuple(CLOCKS)}")
        for row in replay(power):
            print(*row)
