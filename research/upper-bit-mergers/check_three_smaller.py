"""Exact affine induction certificates for 7 mod 8 and bounded clock checks."""

from math import lcm


# Each expression starts at r + modulus*u or three times that, for every u >= 0.
ROWS = (
    (7, 72, "DIVOOE", "OEEIIVOD"),
    (23, 24, "IMO", "OEEIDD"),
    (23, 32, "OOOE", "OEEEOD"),
    (31, 72, "DIIMOE", "OEEIDDI"),
    (15, 48, "VOEEIMO", "OEEIIMOEEI"),
    (39, 96, "VOEEIM", "OEEEEIDI"),
    (55, 72, "ODDIIVOEO", "OEEIIVODD"),
)


def divide(a, b, divisor):
    """Both coefficients must divide, including the constant at u=0."""
    if a % divisor or b % divisor:
        raise AssertionError(("nonintegral affine function", a, b, divisor))
    return a // divisor, b // divisor


def require_smaller(a, b, modulus, r):
    if not (0 < a <= modulus and 0 < b < r):
        raise AssertionError(("tripling input too large", a, b, modulus, r))


def replay(r, modulus, start_factor, word):
    a, b = start_factor * modulus, start_factor * r
    for letter in word:
        if letter == "D":
            a, b = 2 * a, 2 * b
        elif letter == "I":
            a, b = divide(2 * a, 2 * b - 1, 3)
            if a % 2 or b % 2 != 1:
                raise AssertionError(("odd preimage", a, b))
        elif letter == "E":
            a, b = divide(a, b, 2)
        elif letter == "O":
            if a % 2 or b % 2 != 1:
                raise AssertionError(("odd input", a, b))
            a, b = divide(3 * a, 3 * b + 1, 2)
        elif letter == "M":
            require_smaller(a, b, modulus, r)
            a, b = 3 * a, 3 * b
        elif letter == "V":
            a, b = divide(a, b, 3)
            require_smaller(a, b, modulus, r)
        else:
            raise ValueError(letter)
        if min(a, b) <= 0:
            raise AssertionError(("nonpositive affine value", a, b))
    return a, b


def check_rows():
    period = lcm(*(m for _, m, _, _ in ROWS))
    for n in range(7, period, 8):
        if not any(n % m == r for r, m, _, _ in ROWS):
            raise AssertionError(("uncovered residue", n))
    for r, m, left, right in ROWS:
        if replay(r, m, 1, left) != replay(r, m, 3, right):
            raise AssertionError(("different affine endpoints", r, m))
    return period


def walk(x, clock):
    odds = 0
    for _ in range(clock):
        odd = x % 2
        odds += odd
        x = (3 * x + 1) // 2 if odd else x // 2
    return x, odds


def check_adjacent():
    good = set()
    for r in range(1, 16, 2):
        if walk(r - 1, 4) == walk(r, 4):
            good.add(r)
    if good != {3, 5, 13}:
        raise AssertionError(good)
    exponents = (5, 4, 2, 3, 3, 2, 2, 3)
    for r, j in zip(range(1, 16, 2), exponents, strict=True):
        if pow(3, j, 16) * r % 16 not in good:
            raise AssertionError(("missed adjacent pair", r, j))


def check_clock_obstruction():
    checked = 0
    for h in range(1, 13):
        three = 3**h
        two = 2**h
        least = three * (-pow(3 * three, -1, two) % two)
        for n in (least, least + two * three):
            start = 3 * n
            if n % three or (start + 1) % two:
                raise AssertionError(("CRT class", h, n))
            for i in range(h + 1):
                endpoint, count = walk(start, i)
                if count != i:
                    raise AssertionError(("prescribed odd run", start, i))
                ancestors = {endpoint}
                for _ in range(h + 1):
                    if min(ancestors) < start:
                        raise AssertionError(("early smaller ancestor", h, n, i))
                    next_ancestors = {2 * x for x in ancestors}
                    next_ancestors.update((2 * x - 1) // 3 for x in ancestors if x % 3 == 2)
                    checked += len(ancestors)
                    ancestors = next_ancestors
    return checked


if __name__ == "__main__":
    print(f"{len(ROWS)} symbolic rows cover every 7 mod 8 residue modulo {check_rows()}")
    check_adjacent()
    print("8 odd residue classes reach a synchronized adjacent pair with 2 <= j <= 5")
    print(f"{check_clock_obstruction()} inverse states in the bounded clock replay")
