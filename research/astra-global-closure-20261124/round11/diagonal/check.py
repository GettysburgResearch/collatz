"""Exact integer certificate for the occupancy recurrence in README.md."""

import argparse
from fractions import Fraction
from functools import lru_cache
import json


FLOOR_BITS = 71
TAIL_BITS = 640


@lru_cache(maxsize=16)
def binomial_tails(n):
    """Entry i is the number of binary words of length n with at least i ones."""
    row = [1]
    for i in range(n):
        row.append(row[-1] * (n - i) // (i + 1))
    row.append(0)
    for i in range(n, -1, -1):
        row[i] += row[i + 1]
    return row


def count_bound(j, odd, known, powers):
    """Bound either all states below 2^j, or odd states in [2^j,2^(j+1))."""
    best = 2**j
    for removed in range(5):
        k = j - removed
        periods = 2**removed
        unit_copies = periods - periods // 3
        tails = binomial_tails(k - odd)
        for p in range(odd, k + 1):
            image_bound = powers[p] * (3 * (2**odd) * periods + 1) // 3
            image_bits = image_bound.bit_length()
            if image_bits >= len(known):
                break
            high_words = tails[p + 1 - odd]
            best = min(best, known[image_bits] + k + unit_copies * high_words)
    return best


def check_reported_record():
    """Replay the record-holder only. Global coverage is external."""
    state = 2358909599867980429759
    peak = state
    for steps in range(10000):
        if state == 1:
            if peak != 494114680693632162318569565806744468898092:
                raise ArithmeticError("The observed peak differs from the published entry")
            return {"shortcut_steps_to_one": steps, "maximum": str(peak)}
        state = state // 2 if state % 2 == 0 else (3 * state + 1) // 2
        peak = max(peak, state)
    raise ArithmeticError("The record path exceeded its replay budget")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--floor-bits", type=int, default=FLOOR_BITS)
    parser.add_argument("--tail-bits", type=int, default=TAIL_BITS)
    args = parser.parse_args()
    floor, cutoff = args.floor_bits, args.tail_bits
    if not 6 <= floor < cutoff or cutoff % 40:
        parser.error("need floor bits >= 6 and a larger tail cutoff divisible by 40")
    known = [0] * (floor + 1)
    powers = [3**p for p in range(cutoff + 1)]
    finite = Fraction(0)
    for j in range(floor, cutoff):
        if j > floor:
            known.append(count_bound(j, 0, known, powers))
        finite += Fraction(count_bound(j, 1, known, powers), 2**j)
    # Partial summation of the resident 5 X^(39/40) bound above 2^640.
    tail = Fraction(200, 2**(cutoff // 40))
    upper = finite + tail
    if (floor, cutoff) == (71, 640) and upper >= Fraction(593690, 10**6):
        raise ArithmeticError("The finite sum and its rigorous tail exceed the claim")
    print(json.dumps({
        "first_octave_bits": floor, "first_tail_bits": cutoff,
        "finite_sum_millionths_rounded_up": -(-finite.numerator * 10**6 // finite.denominator),
        "tail_bound": str(tail), "total_millionths_rounded_up":
            -(-upper.numerator * 10**6 // upper.denominator),
        "below_three_fifths": upper < Fraction(3, 5),
        "single_record_replay": check_reported_record(),
    }, indent=2))


if __name__ == "__main__":
    main()
