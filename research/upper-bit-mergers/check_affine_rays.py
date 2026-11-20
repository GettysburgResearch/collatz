"""Construct and replay exact common endpoints for affine Collatz rays on binary cells."""

from dataclasses import dataclass
from itertools import product

from check import step, walk


def v2(n):
    """The 2-adic valuation of a nonzero integer."""
    if n == 0:
        raise ValueError("the valuation of zero is not finite")
    return (abs(n) & -abs(n)).bit_length() - 1


def strip_even_slope(ray, residue, bits):
    """Return the arm after the common prefix fixed by its even coefficient."""
    slope, offset = ray
    valuation = v2(slope)
    head = valuation + bits
    value, odds = walk(slope * residue + offset, head)
    return ((slope >> valuation) * 3**odds, value), head, odds


def three_level(left, right):
    """Return s for an ordered pair of slopes in ratio 3**s, or None."""
    factor, remainder = divmod(right, left)
    if remainder:
        return None
    level = 0
    while factor % 3 == 0:
        factor //= 3
        level += 1
    return level if factor == 1 else None


def prescribe(level, gap, equal_stage):
    if level and equal_stage:
        return gap % 2
    if level:
        if gap % 2:
            return 1
        limit = v2(3**level - 1)
        return int(gap == 0 or v2(gap) > limit)
    if gap % 2:
        return int((3 * gap + 1) % 4 != 0)
    return 0


def lift_step(arm, bit):
    """Replace the free parameter by 2*u+bit and take one literal step."""
    slope, offset = arm
    start = slope * bit + offset
    odd = start % 2
    return (slope * (3 if odd else 1), step(start)), odd


@dataclass(frozen=True)
class Certificate:
    residue: int
    bits: int
    clocks: tuple
    odd_counts: tuple
    endpoint: tuple


def construct(left, right, residue=0, bits=0):
    """The endpoint is affine in u on n=residue_out+2**bits_out*u."""
    if bits < 0 or not 0 <= residue < 2**bits or min(left[0], right[0]) <= 0:
        raise ValueError("require positive slopes and a canonical binary residue")
    a, left_clock, left_odds = strip_even_slope(left, residue, bits)
    b, right_clock, right_odds = strip_even_slope(right, residue, bits)
    initial_level = three_level(min(a[0], b[0]), max(a[0], b[0]))
    if initial_level is None:
        return None
    # LTE gives sum_j v2(3**j-1) = 2*s + floor(s/2) - popcount(s).
    level_budget = 3 * initial_level + initial_level // 2 - initial_level.bit_count()
    equal_stage = False
    while a != b:
        base, other = (a, b) if a[0] <= b[0] else (b, a)
        level = three_level(base[0], other[0])
        if level is None or base[0] % 2 == 0:
            raise AssertionError(("invalid normalized slopes", a, b))
        gap = other[1] - 3**level * base[1]
        if level == 0:
            equal_stage = True
        elif not equal_stage:
            level_budget -= 1
            if level_budget < 0:
                raise AssertionError(("positive-level clock exceeded", initial_level, a, b))
        parity = prescribe(level, gap, equal_stage)
        zero, one = ((base[1] + bit * base[0]) % 2 == parity for bit in (0, 1))
        if zero == one:
            raise AssertionError(("ambiguous next bit", base, parity))
        bit = int(one)
        a, odd_a = lift_step(a, bit)
        b, odd_b = lift_step(b, bit)
        residue += bit * 2**bits
        bits += 1
        left_clock += 1
        right_clock += 1
        left_odds += odd_a
        right_odds += odd_b
    return Certificate(residue, bits, (left_clock, right_clock), (left_odds, right_odds), a)


def slope_core(coefficient):
    for prime in (2, 3):
        while coefficient % prime == 0:
            coefficient //= prime
    return coefficient


def verify(left, right, residue, bits, cert):
    if cert is None or cert.residue % 2**bits != residue or cert.bits < bits:
        raise AssertionError(("wrong parameter cell", left, right, residue, bits, cert))
    step_size = 2**cert.bits
    # Each ray must be strictly positive; signed intercepts are legitimate
    # during symbolic construction, including when the representative is small.
    first = max(0, *(1 + (-c - a * cert.residue) // (a * step_size) for a, c in (left, right)))
    for free in (first, first + 1, first + 3, first + 37, first + 2**31):
        n = cert.residue + step_size * free
        endpoint = cert.endpoint[0] * free + cert.endpoint[1]
        for (a, b), clock, odds in zip((left, right), cert.clocks, cert.odd_counts, strict=True):
            if a * n + b <= 0 or walk(a * n + b, clock) != (endpoint, odds):
                raise AssertionError(("orbit mismatch", a, b, n, clock, odds, endpoint))


def replay():
    good = bad = 0
    # Include unequal 2-adic prefixes, forced orientation changes, zero gaps,
    # negative intercepts, several common prime-to-six factors and fixed cells.
    slopes = (1, 2, 3, 5, 6, 7, 9, 10, 12, 14, 18, 21, 24, 25, 45, 81)
    offsets = ((0, 0), (-37, 19), (16, -23), (-12, -75), (29, 29))
    cells = ((0, 0), (0, 1), (1, 1), (3, 3), (17, 5))
    for a, c in product(slopes, repeat=2):
        for (b, d), (residue, bits) in product(offsets, cells):
            left, right = (a, b), (c, d)
            cert = construct(left, right, residue, bits)
            if slope_core(a) != slope_core(c):
                if cert is not None:
                    raise AssertionError(("incompatible slopes", left, right, cert))
                bad += 1
            else:
                verify(left, right, residue, bits, cert)
                good += 1
    # An incompatible pair can still meet at an individual parameter.
    if walk(1, 1)[0] != walk(5, 3)[0] or construct((1, 0), (5, 0)) is not None:
        raise AssertionError("isolated root versus uniform affine certificate")
    return good, bad


if __name__ == "__main__":
    successes, incompatible = replay()
    print(f"{successes} affine certificates replayed on five positive lifts each")
    print(f"{incompatible} incompatible ray-and-cell cases rejected")
