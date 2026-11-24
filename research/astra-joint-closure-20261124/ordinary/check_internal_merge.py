"""Ordinary controls for the written single-block success and obstruction."""


def iterate(value, odd_steps, halvings):
    for _ in range(odd_steps):
        if value % 2 != 1:
            raise ValueError("the required odd edge is absent")
        value = (3 * value + 1) // 2
    for _ in range(halvings):
        if value % 2 != 0:
            raise ValueError("the required even edge is absent")
        value //= 2
    return value


def check_example():
    source = 293654367
    competitor = 96567295
    endpoint = 660722327
    if (source + 1) % 64 != 32 or source % 3 or 3 * competitor >= source:
        raise ValueError("wrong example source or insufficient descent")
    if iterate(source, 2, 0) != endpoint or iterate(competitor, 15, 6) != endpoint:
        raise ValueError("arms do not meet")


def check_obstruction(run_length):
    modulus = 2 ** (run_length + 1)
    power = 3 ** (2 * (run_length + 1))
    cofactor = ((2**run_length - 1) * pow(power, -1, modulus)) % modulus
    source = power * cofactor
    if (source + 1) % modulus != 2**run_length or source % 3:
        raise ValueError("incorrect first-run length or nonmultiple of three")

    # Any smaller one-block competitor satisfies 2^k <= source,
    # and 2^e < (3/2)^k, so checking e and k through this limit is enough.
    bound = source.bit_length() - 1
    endpoint = source
    for position in range(1, run_length + 1):
        endpoint = iterate(endpoint, 1, 0)
        for halvings in range(1, bound + 1):
            odd_factor = 2**halvings * endpoint + 1
            for odd_steps in range(1, bound + 1):
                odd_factor, remainder = divmod(odd_factor, 3)
                if remainder:
                    break
                competitor = 2**odd_steps * odd_factor - 1
                if 0 < competitor < source:
                    raise ValueError((source, position, competitor, odd_steps, halvings))
    return source


if __name__ == "__main__":
    check_example()
    for length in (1, 2, 5, 8, 12):
        print(f"m={length}, n={check_obstruction(length)}: no smaller one-block source")
    print("Two positive example arms meet at 660722327.")
