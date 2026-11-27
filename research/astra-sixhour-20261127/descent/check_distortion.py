"""Exact finite part of the explicit reciprocal bound for a simple Collatz segment."""
from fractions import Fraction
from json import dumps


def require(test, reason):
    if not test:
        raise ArithmeticError(reason)


def unit_count(length):
    q, r = divmod(length, 3)
    return 2*q+min(2, r)


def next_occupancies(previous, previous_odd, last):
    full_bounds, odd_bounds = [2], [2]
    for clock in range(1, last+1):
        previous_word_count = 1
        power_three = 1
        carry_bound = (3**clock >> clock)+2
        full = odd = clock
        for grade in range(clock+1):
            # Mixed even and odd words have C(clock,grade) possibilities; fixing
            # the first departure odd retains exactly grade/clock of them.
            words = previous_word_count
            output_length = 3*power_three+carry_bound
            output_index = ((output_length-1)//3).bit_length()
            require(output_length <= 3 << output_index, "interval rounding")
            capacity = unit_count(output_length)
            if output_index <= last:
                capacity = min(capacity, previous[output_index])
            full += min(capacity, 2*words)
            odd += min(capacity, 2*(words*grade//clock))
            previous_word_count = words*(clock-grade)//(grade+1)
            power_three *= 3
        full_bounds.append(min(previous[clock], full))
        odd_bounds.append(min(previous_odd[clock], odd))
    return full_bounds, odd_bounds


def certificate():
    maximum = 959
    full = [2 << h for h in range(maximum+1)]
    odd = full[:]
    weight = sum((Fraction(1, x) for x in range(8, 16)), Fraction(0))
    stages = []
    for iteration in range(1, 5):
        full, odd = next_occupancies(full, odd, maximum)
        # A three-times-dyadic octave splits into eight native blocks.
        partial = weight*sum((Fraction(odd[h-3], 3 << (h-3))
                              for h in range(69, maximum+1)), Fraction(0))
        stages.append({"round": iteration, "scaled_ceiling_millionths":
                       -(-partial.numerator*10**6//partial.denominator)})
    require(partial < Fraction(13, 25), "four-round finite bound")
    # Each group of forty high octaves contributes at most 240*2^-floor(h/40).
    require(2*5**40*2**24 < 4**40*3**24, "heavy-word decay per forty clocks")
    require(2*3**24 < 2**40, "light-endpoint decay per forty clocks")
    tail = Fraction(480, 2**24)
    whole = partial+tail+Fraction(1, 2**71)
    require(whole < Fraction(53, 100) and Fraction(53, 300) < Fraction(9, 50),
            "ordinary distortion budget")
    return {"first_ternary_octave": 69, "last_finitely_counted_octave": maximum,
            "native_subintervals_per_octave": 8, "passes": stages,
            "high_octave_tail": str(tail), "possible_initial_odd_multiple_of_three":
            str(Fraction(1, 2**71)), "harmonic_bound": "53/100", "distortion_bound": "6/5"}


if __name__ == "__main__":
    print(dumps(certificate(), indent=2, sort_keys=True))
