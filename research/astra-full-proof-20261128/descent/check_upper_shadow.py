"""Exact scalar replay of the fixed-source shadow and all upper-lap recurrences."""

from collections import Counter
from fractions import Fraction


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    if isinstance(x, Fraction):
        return (3 * x + 1) / 2 if x.numerator % 2 else x / 2
    return (3 * x + 1) // 2 if x % 2 else x // 2


def v2(n):
    return (n & -n).bit_length() - 1


def first_upper_hit(z):
    n = 3 * z
    odds = clock = 0
    while n != 1:
        require(clock < 1000, "upper control exceeded clock budget")
        odds += n % 2
        n = step(n)
        clock += 1
    return clock, odds


def release(z, h, r):
    c = 2**h - 3 ** (r + 1) * z
    signed = Fraction(-c, 3 ** (r + 1))
    t = 0
    require(signed.denominator == 3 ** (r + 1), "unexpected initial denominator")
    while signed.denominator != 1:
        signed = step(signed)
        t += 1
        require(t < 2000, "signed control exceeded clock budget")
    return t, int(signed)


def replay(z, h, r):
    t, s = release(z, h, r)
    if h < t:
        return None
    m = h - t
    x = z
    for _ in range(t):
        x = step(x)
    require(x == 2**m + s, "incorrect release")
    signed = s
    p = 0
    for i in range(m + 1):
        require(x == (2 ** (m - i)) * 3**p + signed, "incorrect lifted integer")
        if s < 0:
            require((-s) * x >= 2**m + s, "negative floor failed")
        p += signed % 2
        x = step(x)
        signed = step(signed)
    if s >= 0:
        return (s > 0) - (s < 0)
    for lap in range(1, 13):
        a = -s
        j = v2(a)
        b = 2**m - a
        require(v2(b) == j < m, "valuation mismatch")
        next_a = ((2**m + 3 * a) // 2**j - 1) // 2
        t = t + j + 1
        m = m + 1 - j
        s = -next_a
        require(release(z, h + 2 * lap, r + lap) == (t, s), "new center disagrees")
        require(0 < -s < 2**m, "negative sign did not persist")
        require(2**m + s == (3 * (b >> j) + 1) // 2, "lower physical step disagrees")
    return -1


def main():
    counts = Counter()
    for z in range(17, 20000, 48):
        h, r = first_upper_hit(z)
        counts[replay(z, h, r)] += 1
    print("417 fixed canonical sources, first native upper certificate:", dict(counts))
    families = [(17, 17, 7, 19, 1), (1313, 20, 5, 17, 0), (3233, 18, 3, 6, -2)]
    for z, h, r, t, s in families:
        c = 2**h - 3 ** (r + 1) * z
        require(release(z, h, r) == (t, s), "row anchor disagrees")
        # Multiply the root power by 1 modulo 48*3^(r+1), after extracting 16.
        spacing = 2 * 3 ** (r + 1)
        big_h = h + spacing
        big_z, rem = divmod(2**big_h - c, 3 ** (r + 1))
        require(rem == 0 and big_z % 48 == 17, "row height is inadmissible")
        upper = 3 * big_z
        odd = 0
        for _ in range(big_h):
            odd += upper % 2
            upper = step(upper)
        require((upper, odd) == (1, r), "pumped upper certificate disagrees")
        require(replay(big_z, big_h, r) == (s > 0) - (s < 0), "pump sign changed")
        print(f"r={r}, C={c}, t={t}, s={s}, checked H={big_h}")


if __name__ == "__main__":
    main()
