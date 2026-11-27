"""Check all signed-center obstructions and three ordinary positive refinements."""

from collections import Counter

from check_finite_patterns import advance, check, refinement, trace


def signed_certificates(limit=192):
    """A grade-complete integer test, with no forward tail-length cutoff."""
    max_clock = 18 * limit + 4
    powers = [1]
    for _ in range(max_clock + 1):
        powers.append(3 * powers[-1])

    tested = 0
    reduced = 0
    terminal_cases = Counter()
    for gap in range(1, max_clock):
        numerator = 1 - powers[gap + 1]
        odds = 0
        for clock in range(1, max_clock + 1):
            if numerator % 2:
                if odds <= gap:
                    numerator = (numerator + powers[gap - odds]) // 2
                else:
                    numerator = (3 * numerator + 1) // 2
                odds += 1
            else:
                numerator //= 2
            if clock < 22 or clock % 18 != 4 or gap >= clock:
                continue
            tested += 1
            if powers[gap + 1] > (1 << clock) - 1 or odds < gap + 1:
                continue
            reduced += 1
            credit = odds - gap - 1
            signed_value = numerator - powers[credit]
            if -(1 << credit) <= signed_value <= -1:
                terminal_cases[credit, signed_value] += 1

    check(tested == 334080 and reduced == 166182, "incomplete valuation coverage")
    check(terminal_cases == {(1, -1): 44, (3, -1): 14}, "unresolved signed tail")
    return tested, reduced, sorted(terminal_cases.items())


def delayed_return(index, extra_bits):
    """Construct a positive ordinary cofactor in the shield and a paid dyadic refinement."""
    valuation = 18 * index + 4
    gap = 162
    protected_clock = valuation + extra_bits
    modulus = 1 << protected_clock
    earlier_power = ((1 - (1 << valuation)) * pow(3, -(gap + 1), modulus)) % modulus
    residue = (earlier_power - 1) % modulus
    earlier = advance((0, 0), protected_clock, residue)
    later = advance((gap, 3**gap - 1), protected_clock, residue)
    clock = protected_clock
    while earlier != later:
        length, next_bits = refinement(earlier, later)
        residue += (1 << clock) * next_bits
        clock += length
        earlier = advance(earlier, length, next_bits)
        later = advance(later, length, next_bits)

    scale = 12 << (18 * index)
    modulus = 1 << clock
    target = 3 ** (gap + 1) * (residue + 1) % modulus
    next_power = pow(3, scale, modulus)
    current = 1
    cofactor = 0
    for bit in range(clock - valuation):
        if (current - target) & (1 << (valuation + bit)):
            cofactor += 1 << bit
            current = current * next_power % modulus
        next_power = next_power * next_power % modulus
    period = 1 << (clock - valuation)
    cofactor += period * ((1 - cofactor) * pow(period, -1, 27) % 27)
    exponent = scale * cofactor - 1
    check(cofactor % 54 == 1 and exponent % 162 == 11, "canonical cofactor class")
    check(exponent >= 4 * protected_clock + 4, "independent-clock size guard")
    check(pow(3, exponent + 1, 1 << protected_clock) ==
          (1 - (1 << valuation)) % (1 << protected_clock), "signed-center congruence")
    base = pow(3, exponent - gap, modulus)
    check(base - 1 == residue, "ordinary exponent does not realize the refinement")
    left, left_grade = trace(base - 1, clock)
    right, right_grade = trace(3**gap * base - 1, clock)
    check(left == right and left_grade == right_grade + gap, "ordinary counted merger")
    return index, valuation, protected_clock, clock, left_grade, cofactor.bit_length()


def main():
    print("valuation census", signed_certificates())
    expected = [(1, 22, 62, 528, 322, 510), (80, 1444, 1504, 3089, 1200, 1647),
                (192, 3460, 3560, 7958, 3000, 4502)]
    rows = [delayed_return(k, bits) for k, bits in [(1, 40), (80, 60), (192, 100)]]
    check(rows == expected, "ordinary regression fixture")
    for row in rows:
        print("positive cofactor", *row)


if __name__ == "__main__":
    main()
