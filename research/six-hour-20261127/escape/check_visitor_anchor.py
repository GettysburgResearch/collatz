"""Exact finite positive-trajectory input to the all-visitor protection bound."""
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    last = 4095
    depth = 128
    max_stop = 0
    worst = []
    max_odd = 1
    for start in range(1, last + 1, 2):
        x = start
        stop = 0
        while x != 1 and stop < 88:
            numerator = 3 * x + 1
            exponent = (numerator & -numerator).bit_length() - 1
            x = numerator >> exponent
            max_odd = max(max_odd, x)
            stop += 1
        require(x == 1 and stop <= 87, "odd positive source exceeded verified horizon")
        if stop > max_stop:
            max_stop = stop
            worst = []
        if stop == max_stop:
            worst.append(start)

    failure = Fraction(2, 3) * Fraction(3, 4) ** (2 * (depth - max_stop))
    failure += Fraction(100, 3 * last)
    require(failure < Fraction(1, 100), "exact failure budget exceeded")
    print(json.dumps({
        "scope": "finite ordinary paths and final rational inequality only",
        "largest_odd_start": last,
        "number_of_starts": (last + 1) // 2,
        "maximum_odd_steps_to_one": max_stop,
        "maximizing_starts": worst,
        "largest_odd_vertex_after_a_step": max_odd,
        "ternary_depth": depth,
        "failure_bound": str(failure),
        "strictly_below_one_percent": True,
    }, indent=2))


if __name__ == "__main__":
    main()
