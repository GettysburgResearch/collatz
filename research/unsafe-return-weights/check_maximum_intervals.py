"""Certify first-hit maximizers via directed dyadic rounding on the doubling orbit."""

import argparse
from array import array
from fractions import Fraction

from check_first_hit_maximum import first_return

SCALE = 2**44


def advance(lower, error, depth):
    """Each input value belongs to [lower/SCALE, (lower+error)/SCALE]."""
    modulus = 3 * len(lower)
    period = 2 * len(lower)
    output = array('Q', [0]) * modulus
    # Start below the true value and burn enough steps to suppress that error.
    # In each step a previous-level error E contributes at most 3E/2.
    burn = SCALE.bit_length() + depth + 2
    target = pow(2, period + burn, modulus)
    value = 0
    for remaining in range(period + burn, 0, -1):
        parent = target
        target = (target + (modulus if target % 2 else 0)) // 2
        injection = 3 * lower[(parent - 1) // 3] if parent % 3 == 1 else 0
        value = (value + injection) // 2
        if remaining <= period:
            output[target] = value
    return output, 3 * error + 3


def mass_interval(levels, q, t, cycle):
    values, error = levels[q]
    low = values[t % len(values)]
    high = low + error
    if cycle and cycle[0] <= q:
        d, jac = cycle
        previous, previous_error = levels[q - d]
        old = previous[t % len(previous)]
        low -= jac * (old + previous_error)
        high -= jac * old
    return low, high


def run(horizon):
    levels = [([SCALE], 0)]
    for q in range(horizon + 1):
        levels.append(advance(*levels[-1], q + 1))
        best, winner, second, winner_high = 0, 0, 0, 0
        for t in range(1, len(levels[-1][0]) + 1, 2):
            if t % 3 == 0:
                continue
            # g*_q in [0,2^q], so all subsequent targets are smaller.
            if best * t > SCALE * 2 ** (q + 1):
                break
            cycle = first_return(t, q + 1)
            lo, hi = mass_interval(levels, q + 1, t, cycle)
            old_lo, old_hi = mass_interval(levels, q, t, cycle)
            left, right = lo - old_hi, hi - old_lo
            low = Fraction(max(left, -right, 0), t)
            high = Fraction(max(-left, right), t)
            if low > best:
                second = max(second, winner_high)
                best, winner, winner_high = low, t, high
            else:
                second = max(second, high)
        assert best > second, (q, winner, best, second)
        print(q, winner, float(best / SCALE), float(winner_high / SCALE), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("depth", type=int, default=11, nargs="?")
    run(parser.parse_args().depth)
