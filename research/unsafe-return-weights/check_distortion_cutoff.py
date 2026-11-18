"""Exact odd-shell replay for the finite distortion cutoff.

Columns are power k (X = 2**k), s, fixed odd-step clock q, number of odd
sources, count that reach 1 by q, and mean V in outward-rounded millionths.
The integer clocks are part of the finite experiment. They were obtained
by evaluating max(0, floor(h/d + s*sqrt(2*log(2)**2*h/d**3))) with
60-decimal precision, h = k*log(2), d = log(4/3).
"""
import argparse
from decimal import Decimal, localcontext


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


def log_scalar(power):
    """Return rigorous millionth bounds for the normalized mean negative log."""
    limit = 1 << power
    q = 0
    while 4**(q + 1) <= limit**2 * 3**(q + 1):
        q += 1
    count = limit // 4
    bins = 4096
    scale = INTERNAL_SCALE

    # Decimal.ln is correctly rounded. All table arguments are exact dyadics;
    # one unit on either side after scaling more than covers decimal rounding.
    with localcontext() as ctx:
        ctx.prec = 50
        table = [int((Decimal(b) / bins).ln() * scale)
                 for b in range(bins, 2 * bins + 1)]
    log2_low, log2_high = table[-1] - 1, table[-1] + 1

    def log_bounds(number):
        exponent = number.bit_length() - 1
        unit = 1 << exponent
        bin_number, residual = divmod(number * bins, unit)
        denominator = bin_number * unit
        base = table[bin_number - bins]
        # For u=residual/denominator, u-u²/2 <= log(1+u) <= u.
        low = scale * residual * (2 * denominator - residual) // (2 * denominator**2)
        high = (scale * residual + denominator - 1) // denominator
        return exponent * log2_low + base - 1 + low, exponent * log2_high + base + 1 + high

    ratio_low = ratio_high = valuation_sum = hits = 0
    for source in range(limit // 2 + 1, limit, 2):
        state = source
        depth = 0
        while depth < q and state != 1:
            value = 3 * state + 1
            shift = (value & -value).bit_length() - 1
            state = value >> shift
            valuation_sum += shift
            depth += 1
        if state == 1:
            hits += 1
            valuation_sum += 2 * (q - depth)
        source_low, source_high = log_bounds(source)
        state_low, state_high = log_bounds(state)
        ratio_low += state_low - source_high
        ratio_high += state_high - source_low

    log3_low, log3_high = log_bounds(3)
    low = valuation_sum * log2_low + ratio_low - q * count * log3_high
    high = valuation_sum * log2_high + ratio_high - q * count * log3_low
    # Each individual negative log is nonnegative.
    lower_ppm = max(0, low) * MILLION // (power * count * log2_high)
    divisor = power * count * log2_low
    upper_ppm = (high * MILLION + divisor - 1) // divisor
    return power, q, count, hits, lower_ppm, upper_ppm


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("powers", nargs="*", type=int, metavar="k",
                        help="one or more of 10, 14, 18, 22 (default: 10 14 18)")
    parser.add_argument("--log-scalar", action="store_true",
                        help="report the mean normalized negative log instead (default k=22)")
    args = parser.parse_args()
    if args.log_scalar:
        print("k q sources reached_1 mean_Z_lower_ppm mean_Z_upper_ppm")
        for power in args.powers or (22,):
            if power not in CLOCKS:
                parser.error(f"unsupported k={power}; use one of {tuple(CLOCKS)}")
            print(*log_scalar(power))
        parser.exit()
    print("k s q sources reached_1 lower_ppm upper_ppm")
    for power in args.powers or (10, 14, 18):
        if power not in CLOCKS:
            parser.error(f"unsupported k={power}; use one of {tuple(CLOCKS)}")
        for row in replay(power):
            print(*row)
