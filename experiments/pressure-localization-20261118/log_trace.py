"""All-source finite-clock enclosures for signed log slopes and energy."""
import argparse
import json
from fractions import Fraction


def lower_units(value, scale):
    return scale * value.numerator // value.denominator


def upper_units(value, scale):
    return -lower_units(-value, scale)


def compute(clocks, cutoff, bits):
    if cutoff < 3 or cutoff % 2 == 0 or bits < 1:
        raise ValueError("cutoff must be odd and at least 3, bits positive")
    if not clocks or min(clocks) < 1 or len(set(clocks)) != len(clocks):
        raise ValueError("clocks must be distinct positive integers")
    clocks = sorted(clocks)
    maximum = max(clocks)
    scale = 1 << bits
    numerators = [(9 ** j) << bits for j in range(maximum)]
    height = [(3 ** j).bit_length() - 1 for j in range(maximum)]
    energy = [0] * maximum
    slope = [0] * maximum
    for x in range(1, cutoff + 1, 2):
        state = x
        raw = 0
        for j in range(maximum):
            denominator = (state * state) << (2 * raw)
            numerator = numerators[j]
            energy[j] += numerator // denominator
            slope[j] += (numerator * (height[j] - raw)) // denominator
            number = 3 * state + 1
            removed = (number & -number).bit_length() - 1
            state = number >> removed
            raw += removed
    count = (cutoff + 1) // 2
    results = []
    for q in clocks:
        energy_floor = sum(energy[:q])
        slope_floor = sum(slope[:q])
        rounds = q * count
        log_tail_lower = -Fraction(q * ((cutoff - 1).bit_length() + 4), cutoff)
        log_tail_upper = Fraction(q * (q - 1), 4 * (cutoff + 1))
        results.append({
            "clock_count": q,
            "energy_sum_lower": energy_floor,
            "energy_sum_upper": energy_floor + rounds
                                + upper_units(Fraction(q, 2 * (cutoff + 1)), scale),
            "slope_sum_lower": slope_floor + lower_units(log_tail_lower, scale),
            "slope_sum_upper": slope_floor + rounds + upper_units(log_tail_upper, scale),
        })
    return {"cutoff": cutoff, "fraction_bits": bits, "rows": results}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--clocks", type=int, nargs="+", required=True)
    parser.add_argument("--cutoff", type=int, required=True)
    parser.add_argument("--bits", type=int, default=96)
    args = parser.parse_args()
    print(json.dumps(compute(args.clocks, args.cutoff, args.bits), indent=2))
