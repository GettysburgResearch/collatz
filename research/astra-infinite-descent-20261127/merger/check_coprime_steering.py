"""Finite ordinary controls for the written coprime steering construction."""

from math import gcd, lcm


def check(condition, label):
    if not condition:
        raise ValueError(label)


def order_of_two(modulus):
    exponent, residue = 1, 2 % modulus
    while residue != 1:
        exponent += 1
        residue = 2 * residue % modulus
    return exponent


def ternary_exponent(target, precision):
    """Lift a solution of 2**e = target one ternary digit at a time."""
    check(precision >= 1 and target % 3 != 0, "target is not a ternary unit")
    exponent = int(target % 3 == 2)
    period = 2
    for digit in range(1, precision):
        modulus = 3 ** (digit + 1)
        exponent = next(
            value for value in (exponent + k * period for k in range(3))
            if pow(2, value, modulus) == target % modulus
        )
        period *= 3
    return exponent


def steering_word(source, goal, modulus, suffix):
    """Reconstruct a successful sequence of two-clock slots and its odd suffix."""
    inverse_two = pow(2, -1, modulus)
    # The suffix sends z+1 to (3/2)**suffix * (z+1).
    desired = (pow(2 * pow(3, -1, modulus), suffix, modulus) * (goal + 1) - 1) % modulus
    paths = {source % modulus: ()}
    for _ in range(modulus - 1):
        next_paths = {}
        for current, word in paths.items():
            for bits, offset in [((1, 0), 1), ((0, 1), 2)]:
                final = (3 * current + offset) * inverse_two**2 % modulus
                next_paths.setdefault(final, word + bits)
        check(len(next_paths) >= min(modulus, len(paths) + 1), "reachable residue growth")
        paths = next_paths
    return paths[desired] + (1,) * suffix


def simultaneous_exponent(first, period, second, order):
    common = gcd(period, order)
    check((second - first) % common == 0, "incompatible exponent classes")
    reduced = order // common
    shift = 0
    if reduced > 1:
        shift = ((second - first) // common * pow(period // common, -1, reduced)) % reduced
    return (first + period * shift) % lcm(period, order)


def step(value):
    return value // 2 if value % 2 == 0 else (3 * value + 1) // 2


def parameters(modulus, precision, initial_grade):
    check(modulus > 1 and gcd(modulus, 6) == 1, "coprime modulus")
    order = order_of_two(modulus)
    remaining = order
    suffix = 1
    while remaining % 3 == 0:
        remaining //= 3
        suffix += 1
    final_grade = initial_grade + modulus - 1 + suffix
    period = 2 * 3 ** (final_grade + precision + 1)
    return order, suffix, period


def verify_route(target, source_class, modulus, precision, final_clock, profile):
    """Check all reconstructed words, source residues and ordinary valuation gaps."""
    prefix_clock, prefix_base, prefix_grade, endpoint_base = profile
    order, suffix, period = parameters(modulus, precision, prefix_grade)
    check(final_clock > lcm(period, order) and target % 3 != 0, "router inputs")
    low_modulus = 3 ** (suffix + 2)
    common_address = (pow(2, final_clock, low_modulus) * target + 6) % low_modulus
    common_exponent = ternary_exponent(common_address, suffix + 2)
    final_residue = (
        (pow(2, final_clock, modulus) * target - 3 - pow(2, common_exponent, modulus))
        * pow(9, -1, modulus)
    ) % modulus
    parameter_residue = (source_class - prefix_base) * pow(pow(2, prefix_clock, modulus), -1, modulus)
    initial_residue = pow(3, prefix_grade, modulus) * parameter_residue + endpoint_base
    word = steering_word(initial_residue, final_residue, modulus, suffix)

    extra_grade, binary_prefix, state = 0, 0, endpoint_base
    for index, odd in enumerate(word):
        if state % 2 != odd:
            binary_prefix += 2**index
            state += 3 ** (prefix_grade + extra_grade)
        check(state % 2 == odd, "refined cylinder parity")
        extra_grade += odd
        state = step(state)
    clock = prefix_clock + len(word)
    base = prefix_base + 2**prefix_clock * binary_prefix
    grade = prefix_grade + extra_grade
    source_modulus = 3**precision
    trits = (source_class - base) * pow(pow(2, clock, source_modulus), -1, source_modulus) % source_modulus
    terminal_trits = 3**grade * trits + state
    full_precision = grade + precision + 2
    full_modulus = 3**full_precision
    address = (pow(2, final_clock, full_modulus) * target - 3 - 9 * terminal_trits) % full_modulus
    exponent = simultaneous_exponent(ternary_exponent(address, full_precision), period, common_exponent, order)
    exponent = exponent or lcm(period, order)
    check(0 < exponent < final_clock, "positive two-gap clock split")
    numerator = 2**final_clock * target - 3 - 2**exponent
    check(numerator % 9 == 0, "two-gap integrality")
    waypoint = numerator // 9
    check((waypoint - terminal_trits) % 3 ** (full_precision - 2) == 0, "terminal ternary class")
    check(waypoint > state and (waypoint - state) % 3**grade == 0, "positive profile decoding")
    source = base + 2**clock * ((waypoint - state) // 3**grade)
    check(source % modulus == source_class % modulus, "prime-to-six source class")
    check(source % source_modulus == source_class % source_modulus, "ternary source class")
    check((source - prefix_base) % 2**prefix_clock == 0, "binary source cylinder")

    physical = source
    observed_grade = 0
    for _ in range(prefix_clock):
        observed_grade += physical % 2
        physical = step(physical)
    parameter = (source - prefix_base) // 2**prefix_clock
    check(physical == 3**prefix_grade * parameter + endpoint_base, "supplied prefix profile")
    check(observed_grade == prefix_grade, "supplied prefix grade")
    for odd in word:
        check(physical % 2 == odd, "literal steering replay parity")
        physical = step(physical)
    check(physical == waypoint and waypoint % 2 == 1, "literal steering endpoint")
    check(waypoint % modulus == final_residue, "terminal prime-to-six residue")
    middle = (3 * waypoint + 1) >> exponent
    check((middle << exponent) == 3 * waypoint + 1 and middle % 2 == 1, "first ordinary gap")
    check(3 * middle + 1 == 2 ** (final_clock - exponent) * target, "second ordinary gap")


def main():
    checked = 0
    for modulus in [5, 7]:
        for precision in [0, 1]:
            for profile in [(0, 0, 0, 0), (2, 1, 1, 1)]:
                order, _, period = parameters(modulus, precision, profile[2])
                for target in [1, 2, 5, 7]:
                    for source_class in range(modulus * 3**precision):
                        for extra in [1, 4]:
                            clock = lcm(order, period) + extra
                            verify_route(target, source_class, modulus, precision, clock, profile)
                            checked += 1
    print(f"PASS {checked} ordinary coprime-steering routes")


if __name__ == "__main__":
    main()
