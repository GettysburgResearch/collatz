"""Finite parity and small-source certificates for the rank-three restriction."""

from fractions import Fraction


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def shadow_prefix(exponent):
    x = Fraction(-15 - 2 ** (exponent + 2), 81)
    odds = 0
    for length in range(1, 344):
        require(x.denominator % 2 == 1, "Shadow denominator must be odd")
        bit = x.numerator % 2
        odds += bit
        x = ((3 * x + 1) if bit else x) / 2
        if 2**40 * 3**odds < 2**length:
            return length, odds
    raise ValueError(f"No contracting prefix at exponent {exponent}")


def check():
    exponents = [2, 3, 4, 5, *range(49, 201)]
    prefixes = [shadow_prefix(e) for e in exponents]
    require(len(prefixes) == 156 and max(h for h, _ in prefixes) == 343,
            "Unexpected prefix census")
    require(2**703 - 15 - 2**202 > 81 * 2**40 * 3**343,
            "Large-tail size bound failed")
    checked = 0
    longest = 0
    for e in exponents:
        for b in range(700):
            numerator = 2 ** (e + b + 3) - 15 - 2 ** (e + 2)
            if numerator <= 0 or numerator % 3888 != 81 * 17:
                continue
            z = numerator // 81
            y = z
            for steps in range(6_000):
                if y == 1:
                    break
                y = shortcut(y)
            require(y == 1, f"No lower first hit for e={e}, b={b}")
            checked += 1
            longest = max(longest, steps)
    require((checked, longest) == (675, 5619), "Small-case census changed")
    shadow = Fraction(-271, 81)
    slopes = [Fraction(1)]
    for _ in range(7):
        bit = shadow.numerator % 2
        slopes.append(slopes[-1] * Fraction(3 if bit else 1, 2))
        shadow = ((3 * shadow + 1) if bit else shadow) / 2
    require(shadow == -1 and min(slopes) == Fraction(9, 16)
            and slopes[-1] == Fraction(81, 128), "Mersenne barrier changed")
    print("156 contracting shadow prefixes; maximum length 343")
    print("675 positive small-tail sources reach 1; maximum first-hit time 5619")


if __name__ == "__main__":
    check()
