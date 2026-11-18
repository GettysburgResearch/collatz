"""Certified all-source diagonal moments from a Fibonacci-cost source bank."""
import argparse
import json
from fractions import Fraction


def fibonacci(index):
    a, b = 0, 1
    for _ in range(index):
        a, b = b, a + b
    return a


def sources(budget):
    # The first bit of an odd source is odd.  r is the representative
    # modulo h, state = T^k(r), multiplier = 3^p, h = 2^k.
    yield 1
    stack = [(1, 2, 1, 2, 3)]
    while stack:
        cost, h, r, state, multiplier = stack.pop()
        if cost > budget:
            continue
        yield h + r
        for bit, step_cost in ((0, 2), (1, 1)):
            if cost + step_cost > budget:
                continue
            lift = (state ^ bit) & 1
            number = state + lift * multiplier
            next_state = (3 * number + 1) // 2 if bit else number // 2
            stack.append((cost + step_cost, 2 * h, r + lift * h,
                          next_state, multiplier * (3 if bit else 1)))


def tail(clock, budget):
    unfinished = (Fraction(9, 4) ** clock
                  * Fraction(4 * fibonacci(budget + 1) + fibonacci(budget),
                             11 * 4 ** budget))
    minimum_shell = max(clock + 1, (budget + 1) // 2 + 1)
    finished = min(Fraction(1, 2) * Fraction(3, 5) ** clock,
                   Fraction(9, 7) ** clock / 2 ** minimum_shell)
    return finished + unfinished


def ceil_fraction(number):
    return -(-number.numerator // number.denominator)


def compute(clocks, budget, bits):
    if not clocks or min(clocks) < 1 or budget < 1 or bits < 1:
        raise ValueError("positive clocks, budget, and precision required")
    if len(set(clocks)) != len(clocks):
        raise ValueError("clocks must be distinct")
    clocks = sorted(clocks)
    maximum = clocks[-1]
    scale = 1 << bits
    terms = {q: (81 ** q << bits) for q in clocks}
    lower = dict.fromkeys(clocks, 0)
    count = 0
    for x in sources(budget):
        count += 1
        state = x
        exponent = 0
        for q in range(1, maximum + 1):
            number = 3 * state + 1
            removed = (number & -number).bit_length() - 1
            state = number >> removed
            exponent += removed
            if q in terms:
                lower[q] += (terms[q] >> (4 * exponent)) // (state * state)
    if count != fibonacci(budget + 2):
        raise ArithmeticError("wrong Fibonacci source count")
    return {
        "budget": budget,
        "fraction_bits": bits,
        "source_count": count,
        "rows": [{"clock": q, "lower_units": lower[q],
                  "upper_units": lower[q] + count + ceil_fraction(scale * tail(q, budget))}
                 for q in clocks],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--budget", type=int, required=True)
    parser.add_argument("--clocks", type=int, nargs="+", required=True)
    parser.add_argument("--bits", type=int, default=96)
    args = parser.parse_args()
    print(json.dumps(compute(args.clocks, args.budget, args.bits), indent=2))
