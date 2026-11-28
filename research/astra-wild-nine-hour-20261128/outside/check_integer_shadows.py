"""Exact finite checks of transport and simultaneously steered real/profinite windows."""

from fractions import Fraction
from itertools import product
from math import ceil, gcd


A = Fraction(3, 4)
ODD_SLOPE = Fraction(3, 2)


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def step(value, odd):
    return (3 * value + 1 if odd else value) / 2


def odds(value, count):
    return ODD_SLOPE**count * (value + 1) - 1


def residue(value, modulus):
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def check_transport():
    linked = 0
    nonlinked = 0
    for length in range(1, 8):
        for word in product((0, 1), repeat=length):
            slope = Fraction(3**sum(word), 2**length)
            for numerator in range(1, 64, 2):
                start = Fraction(numerator, 8)
                end = start
                for bit in word:
                    end = step(end, bit)
                left, right = round(start), round(end)
                budget = 2**length * abs(end-right) + 3**sum(word) * abs(start-left)
                rounded = Fraction(left)
                true = True
                for bit in word:
                    true &= rounded.denominator == 1 and rounded.numerator % 2 == bit
                    rounded = step(rounded, bit)
                if rounded.denominator == 1:
                    require(true, "integral guard")
                if budget < 1:
                    require(rounded == right and true, "strict transport")
                if rounded == right:
                    require(end-right == slope * (start-left), "linear error")
                    linked += 1
                else:
                    nonlinked += 1
    return linked, nonlinked


def choose_reserved_digits(modulus, coefficients, target):
    paths = {0: ()}
    for coeff in coefficients:
        previous = paths
        paths = {value: bits+(0,) for value, bits in previous.items()}
        for value, bits in previous.items():
            paths.setdefault((value+coeff) % modulus, bits+(1,))
    require(len(paths) == modulus, ("residue coverage", modulus))
    return paths[target]


def check_modular_coverage():
    count = 0
    for modulus in range(1, 80):
        if gcd(modulus, 6) > 1:
            continue
        for offset in (0, 1, 8):
            coefficients = [residue(A**j/4, modulus)
                            for j in range(offset, offset+modulus-1)]
            target = (11*modulus//17) % modulus
            digits = choose_reserved_digits(modulus, coefficients, target)
            require(sum(c*d for c, d in zip(coefficients, digits)) % modulus == target,
                    "reserved digits")
            count += 1
    return count


def stage(start, t, trits, modulus):
    j_count = t//10
    k = modulus-1
    u_mod = 3**trits * modulus
    y = odds(start, t)
    multiplier = ODD_SLOPE**(2*j_count)
    pair_base = A**t*y + 1 - A**t
    left = multiplier*(pair_base+1)-1
    spacing = 2**j_count * u_mod
    require(multiplier >= spacing, "target interval")
    target = spacing*ceil((left+1)/spacing)-1
    residual = (target-left)/multiplier
    require(0 <= residual <= 1, "target parameter")
    digits = []
    for _ in range(t-k):
        digit = int(residual > A)
        digits.append(digit)
        residual = (residual-Fraction(digit, 4))/A
        require(0 <= residual <= 1, "interval contraction")
    inv_four = pow(4, -1, modulus)
    a_mod = 3*inv_four % modulus
    value = residue(pair_base, modulus)
    weight = inv_four
    for digit in digits:
        value = (value + weight*digit) % modulus
        weight = weight*a_mod % modulus
    coefficients = []
    for _ in range(k):
        coefficients.append(weight)
        weight = weight*a_mod % modulus
    digits.extend(choose_reserved_digits(modulus, coefficients, (-1-value) % modulus))
    real = y
    for digit in reversed(digits):
        word = (0, 1) if digit else (1, 0)
        for bit in word:
            real = step(real, bit)
    require(residue(real+1, modulus) == 0, "pair endpoint residue")
    real = odds(real, 2*j_count)
    require(abs(real-target) <= multiplier*A**(t-k), "steered accuracy")
    next_time = 4*t+3*j_count
    # Numerical inequalities here and below use only integer/rational arithmetic.
    worst = abs(real-target)*ODD_SLOPE**j_count
    require((2**next_time)*worst**25 < 1, "exponential accuracy")
    integer = target
    for j in range(j_count+1):
        require(round(real) == integer, "common nearest integer")
        require(integer > 0 and (integer+1) % (2**(j_count-j)*u_mod) == 0,
                "ordinary all-odd window")
        require(residue(real-integer, u_mod) == 0, "odd-place match")
        require(real.denominator > 1, "first error is permanent")
        if j < j_count:
            require(integer % 2 == 1, "true guard")
            integer = (3*integer+1)//2
            real = step(real, 1)
    require(real >= (Fraction(9, 8)**t)*start, "growth reserve")
    return real, next_time, j_count+1


def check_steered_windows():
    # A chronological wrong odd branch on the positive ordinary source 2.
    seed = Fraction(2)
    after_wrong = step(seed, 1)
    t = 124
    start = odds(after_wrong, t-1)
    cases = 0
    for trits, modulus in ((1, 1), (2, 5), (3, 7)):
        start, t, count = stage(start, t, trits, modulus)
        require(start.denominator == 2**t, "exact wrong-word denominator")
        cases += count
    return cases, t


if __name__ == "__main__":
    require(3**325 < 2**532, "asymptotic margin")
    print("Rounded transports and nontransports:", *check_transport())
    print("Full modular subset-sum checks:", check_modular_coverage())
    dates, horizon = check_steered_windows()
    print("Simultaneously shadowed dates:", dates, "through shortcut tick", horizon)
