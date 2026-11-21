"""Exact finite replays for marked returns, ordinary terminals and block profiles."""

from fractions import Fraction
from math import factorial

from check import step, walk
from check_affine_rays import lift_step
from check_five_return_classes import return_cell, state_step


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
    print("Block certificates (size, group clock, ratio clock):", check_cells())
