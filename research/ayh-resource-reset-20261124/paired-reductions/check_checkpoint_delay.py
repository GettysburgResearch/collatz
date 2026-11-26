"""Exact finite replays of the symbolic obstruction, descent, and binary lifts."""
from fractions import Fraction
from math import inf


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valuation(n):
    return (abs(n) & -abs(n)).bit_length() - 1 if n else inf


def shortcut(n):
    return (3 * n + 1 if n % 2 else n) // 2


def signed_step(n):
    return (3 * n + 1 if n.numerator % 2 else n) / 2


def transition(s, gap, bit):
    if gap % 2 == 0:
        return s, (3 * gap + 1 - 3**s) // 2 if bit else gap // 2
    if not bit:
        return s + 1, (3 * gap + 1) // 2
    if s:
        return s - 1, (gap - 3**(s - 1)) // 2
    return 1, (1 - 3 * gap) // 2


def word(s, gap):
    result = []

    def append(bit):
        nonlocal s, gap
        result.append(bit)
        s, gap = transition(s, gap, bit)

    while s:
        if gap % 2:
            append(1)
        else:
            append(min((0, 1), key=lambda b: valuation(transition(s, gap, b)[1])))
    while abs(gap) > 1:
        if gap % 2:
            append(int(gap % 4 == 1))
            append(1)
        else:
            append(0)
    if gap:
        for bit in (int(gap == -1), 0, 1):
            append(bit)
    require((s, gap) == (0, 0), "word failed")
    return result


def attach(d, bits):
    # The complete physical affine arms as functions of the fresh quotient k.
    base, arm = (1, 0), (3**d, -1)
    u = 0
    for h, bit in enumerate(bits):
        digit = (bit - base[1]) % 2
        u += digit << h
        paths = []
        for slope, const in (base, arm):
            value = const + digit * slope
            odd = value % 2
            paths.append((slope * 3**odd, (3**odd * value + odd) // 2))
        base, arm = sorted(paths, key=lambda path: path[0])
    require(base == arm, "unequal ordinary affine endpoints")
    return u


def normalized_unit(c, d, h):
    return (pow(3, (44*c) << d, 1 << (h+d+4)) - 1) >> (d+4)


def recover_cofactor(u, d, h):
    c = 0
    for i in range(h):
        if (normalized_unit(c, d, i+1) ^ u) >> i & 1:
            c += 1 << i
    require(normalized_unit(c, d, h) == u, "isometric lift failed")
    return c


def main():
    for start, terminal, cycles in [
        (Fraction(-14, 3), [Fraction(-7, 3), -3, -4, -2, -1], [-1]),
        (Fraction(-1345, 81), [Fraction(-659, 27), Fraction(-325, 9),
         Fraction(-161, 3), -80, -40, -20, -10, -5], [-7, -10, -5])
    ]:
        for entry in terminal + cycles:
            start = signed_step(start)
            require(start == entry, "signed trace failed")
    total = 0
    longest = 0
    for d in list(range(1, 129)) + [256, 511]:
        bits = word(d, -1)
        h = len(bits)
        require(h <= 52*d + 19, "length")
        u = attach(d, bits)
        require(u % 2 == 1, "parity")
        c = recover_cofactor(u, d, h)
        ternary = 3**13
        target_m = 12345
        desired = (17 + 27*target_m)*pow(11 << d, -1, ternary) % ternary
        c += ((desired - c)*pow(1 << h, -1, ternary) % ternary) << h
        v = c << d
        m, rem = divmod(11*v - 17, 27)
        require(rem == 0 and m % (3**10) == target_m, "ternary source")
        require(normalized_unit(c, d, h) == u and valuation(v) == d, "source attachment")
        total += h
        longest = max(h, longest)
    # Direct integer tests independent of symbolic word lifting.
    for v in range(4, 2000, 27):
        d = valuation(v)
        if d == 0:
            continue
        u = (3**(44*v)-1) >> (d+4)
        w = (3**(42*v)-1) >> (d+3)
        for n, steps, expected in [
                (3**(44*v-1)-5, d+4, 3**d*u-1),
                (32*3**(42*v-4)-17, 8+3*(d//3), 2**(d%3)*3**(2*(d//3))*w-5)]:
            for _ in range(steps):
                n = shortcut(n)
            require(n == expected, "ordinary normalized endpoint")
    # These three sources have the PREASSIGNED odd cofactor 1.
    for d, target in [(20, 1442), (38, 746), (56, 2904)]:
        low = normalized_unit(1, d, target)
        high = 3**d*low-1
        grade = d
        for step in range(target):
            require(low != high or grade != 0, "first merger occurred earlier")
            grade += (high % 2) - (low % 2)
            low, high = shortcut(low), shortcut(high)
        require(low == high and grade == 0, "preassigned cofactor merger")
    print(f"Signed traces, ordinary starts, and 130 binary/ternary rescues passed; "
          f"{total} affine steps, largest word {longest}.")


if __name__ == "__main__":
    main()
