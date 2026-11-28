"""Construct and replay one complete cylinder of six consecutive hard-parent rows."""

from check_finite_patterns import advance, check, refinement, trace


def main():
    gaps = [162 * i for i in range(6)]
    clock = 3
    residue = 2  # 3^(11+162j)-1 modulo eight
    profiles = [advance((gap, 3**gap - 1), clock, residue) for gap in gaps]
    clocks = []
    for index in range(1, len(profiles)):
        while profiles[index] != profiles[0]:
            length, new_bits = refinement(profiles[0], profiles[index])
            residue += (1 << clock) * new_bits
            clock += length
            profiles = [advance(profile, length, new_bits) for profile in profiles]
        clocks.append(clock)

    modulus = 1 << clock
    current = pow(3, 11, modulus)
    increment = pow(3, 162, modulus)
    target = residue + 1
    row = 0
    for bit in range(clock - 3):
        if (current - target) & (1 << (bit + 3)):
            row += 1 << bit
            current = current * increment % modulus
        increment = increment * increment % modulus
    exponent = 11 + 162 * row
    base = pow(3, exponent, modulus)
    check(base == target and pow(3, 162 * (1 << (clock - 3)), modulus) == 1,
          "complete exponent progression")
    shared, grade = trace(base - 1, clock)
    for gap in gaps:
        endpoint, extra = trace(3**gap * base - 1, clock)
        check((endpoint, gap + extra) == (shared, grade), "ordinary peak and grade")
    check(clocks == [468, 1171, 2021, 3220, 4471], "extension lengths")
    check((grade, row.bit_length(), exponent.bit_length()) == (2809, 4466, 4473),
          "canonical chain certificate")
    print("six hard rows, clock", clock, "earliest-exponent grade", grade,
          "row-index bits", row.bit_length(), "power-of-two period exponent", clock - 3)


if __name__ == "__main__":
    main()
