"""Exact finite replays for marked returns, ordinary terminals and block profiles."""

from fractions import Fraction
from math import factorial

from check import step, walk
from check_affine_rays import lift_step
from check_five_return_classes import return_cell, return_word, state_step


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def root_clocks(source, horizon):
    left, right = source, 5 * source
    p = q = 0
    roots = {}
    for clock in range(horizon + 1):
        if p == q and right == 5 * left:
            roots[clock] = left
        p += left % 2
        q += right % 2
        left, right = step(left), step(right)
    return roots


def check_marked_renewal(n):
    count = 1 << n
    first = [0] * (n + 1)
    marked = [0] * (n + 1)
    missed = [0] * (n + 1)
    for x in range(1, 2 * count, 2):
        roots = root_clocks(x, n)
        marks = [t for t, y in roots.items() if y % 2]
        for t in marks:
            marked[t] += 1
        if len(marks) > 1:
            first[marks[1]] += 1
        for delay in range(marks[-1] + 1, n + 1):
            missed[delay] += 1
        # A full binary-period lift preserves every root and the endpoint parity.
        lifted = root_clocks(x + 2 * count, n)
        check(roots.keys() == lifted.keys(), "root is not periodic")
        check(marks == [t for t, y in lifted.items() if y % 2], "mark is not periodic")

    law = [Fraction(c, count) for c in first]
    mass = [Fraction(c, count) for c in marked]
    for t in range(1, n + 1):
        check(mass[t] == sum(law[k] * mass[t - k] for k in range(1, t + 1)),
              "renewal convolution")
    for delay in range(1, n + 1):
        rhs = sum(mass[t] * (1 - sum(law[:n - t + 1])) for t in range(delay))
        check(rhs == Fraction(missed[delay], count), "last-mark partition")
    return count


def first_hit(source):
    value = source
    odds = 0
    for clock in range(5000):
        if value == 1:
            return clock, odds
        odds += value % 2
        value = step(value)
    raise ArithmeticError("test fixture has no supplied finite hitting path")


def check_terminals():
    samples = list(range(1, 769))
    rank_one = [(4**a - 1) // 3 for a in range(2, 36) if a % 3]
    samples += rank_one
    for x in samples:
        d, p = first_hit(x)
        target_hit, _ = first_hit(5 * x)
        roots = root_clocks(x, max(d, target_hit) + 2)
        last = max(roots)
        terminal = roots[last]
        check(last <= d + min(2 * p, 120), "last-root deadline")
        check(terminal % 2 == 1, "even terminal")
        check(root_clocks(terminal, max(d, target_hit) + 2 - last) == {0: terminal},
              "terminal has a further root")
        if x in rank_one:
            check(last == 0, "rank-one terminal")
    return len(samples)


def check_cells():
    words = [
        (2, 8, 0xE),
        (5, 75, 0x4F542607A5CDDDDF810),
        (12, 210, 0x141595A963339B80F6E9CD0009BB816D9B27B4D718D47BEC66E3D),
        (24, 313, 0x10F133D691945657B8E7EE5CFF58F6F65D09E2CC417BB26FFAFB43C7E8BF4C80B90E1F4D4CC10BE),
    ]
    verified = []
    for size, clock, residue in words:
        groups = [{(b, b * i) for i in range(size)} for b in (1, 5)]
        for j in range(clock):
            bit = (residue >> j) & 1
            groups = [{lift_step(arm, bit)[0] for arm in group} for group in groups]
        check(all(len(group) == 1 for group in groups), "profile coalescence")
        cell = return_cell(residue, clock)
        for lift in (1, 2):
            x = cell.residue + (lift << cell.length)
            z = cell.endpoint + lift * 3**cell.odds
            for i in range(size):
                for b in (1, 5):
                    check(walk(b * (x + i), cell.length) == (b * z, cell.odds),
                          "ordinary block endpoint or total count")
        verified.append((size, clock, cell.length))
    return verified



def terminal_lift(residue, h, ternary_residue):
    """Construct an ordinary terminal with prescribed binary prefix and residue modulo 9."""
    source, p = walk(residue, h)
    target, q = walk(5 * residue, h)
    level = q - p
    offset = 3**max(0, -level) * target - 5 * 3**max(0, level) * source
    form = (3**p, source)

    def take(parity):
        nonlocal level, offset, form, residue, h, p
        bit = (parity - form[1]) % 2
        residue += bit << h
        h += 1
        form, actual = lift_step(form, bit)
        check(actual == parity, "illegal selected source parity")
        level, offset = state_step(level, offset, parity)
        check((level, offset) != (0, 0), "terminal steering touched the root")
        p += parity

    for parity in return_word(level, offset):
        if state_step(level, offset, parity) == (0, 0):
            break
        take(parity)
    if (level, offset) == (-1, -1):
        for bit in (1, 0, 0, 0, 0, 0):
            take(bit)
    else:
        check((level, offset) == (1, 5), "unexpected predecessor of the root")
        take(0)
    while level < 61:
        take(0)
    check((level, offset) == (61, 2), "universal terminal section")

    # Lift the doubling exponent one ternary digit at a time. No large
    # power of two needs to be materialized for the symbolic certificate.
    unit = 9
    t0 = (ternary_residue - residue) * pow(1 << h, -1, unit) % unit
    wanted = form[1] + form[0] * t0
    modulus, period = 3, 2
    exponent = 0 if wanted % 3 == 1 else 1
    while modulus < unit * form[0]:
        modulus *= 3
        candidates = (exponent + j * period for j in range(3))
        exponent = next(pos for pos in candidates if pow(2, pos, modulus) == wanted % modulus)
        period *= 3
    lower = max(2, form[1].bit_length() + 1)
    exponent += max(0, (lower - exponent + period - 1) // period) * period
    check(pow(2, exponent, modulus) == wanted % modulus, "power endpoint congruence")
    check(form[0] == 3**p, "incorrect source slope")
    if exponent <= 1800:
        parameter = ((1 << exponent) - form[1]) // form[0]
        x = residue + (parameter << h)
        check(x > 0 and x % 9 == ternary_residue, "ordinary ternary projection")
        check(walk(x, h) == (1 << exponent, p), "ordinary power endpoint")
        endpoint = 5 * 3**(61 + exponent // 2) + (1 if exponent % 2 else 2)
        check(walk(5 * x, h + exponent)[0] == endpoint, "exponential companion endpoint")
        check(root_clocks(x, h + exponent + 120) == {0: x}, "ordinary terminal lift")
        return 1
    return 0


def check_terminal_prefixes():
    h = 8
    survivors = literals = 0
    for residue in range(1 << h):
        if set(root_clocks(residue, h)) != {0}:
            continue
        survivors += 1
        for ternary_residue in (0, 1, 5):
            literals += terminal_lift(residue, h, ternary_residue)
    check(literals > 0, "missing literal ordinary witnesses")
    return survivors, literals


def check_martingale():
    for level in range(-4, 5):
        for offset in range(-24, 25):
            states = [(level, offset)]
            for _ in range(3):
                states = [state_step(k, d, bit) for k, d in states for bit in (0, 1)]
            jumps = [k - level for k, _ in states]
            check(sum(jumps) == 0 and sum(v * v for v in jumps) >= 2,
                  "three-step conditional moments")
    check(sum(Fraction(11, 4)**j / factorial(j) for j in range(7)) > 15,
          "logarithmic split point")
    check(Fraction(40, 3) * Fraction(11, 4) + 2 + Fraction(200, 15) == 52,
          "reciprocal bound roundoff")
    check(Fraction(2 * 52, 3) / Fraction(2, 7) < 122, "even absolute deadline")


if __name__ == "__main__":
    check_martingale()
    print("Odd binary representatives in renewal replay:", check_marked_renewal(13))
    print("Certified source fixtures:", check_terminals())
    print("Terminal construction (surviving classes, literal lifts):", check_terminal_prefixes())
    print("Block certificates (size, group clock, ratio clock):", check_cells())
