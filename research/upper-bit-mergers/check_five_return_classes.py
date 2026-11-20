"""Construct ratio-five returns on binary cells and replay simultaneous prescribed landings."""

from collections import deque
from dataclasses import dataclass
from math import gcd

from check import step, walk
from check_affine_rays import construct, lift_step, v2


def state_step(level, offset, bit):
    other = (bit + offset) % 2
    new_level = level + other - bit
    old_left = max(0, -level)
    left, right = max(0, -new_level), max(0, new_level)
    numerator = 3**(left + other - old_left) * offset + 3**left * other - 5 * 3**right * bit
    if numerator % 2:
        raise AssertionError("nonintegral transition")
    return new_level, numerator // 2


def return_word(level, offset):
    """Bits here specify the shortcut parity of the first arm."""
    bits = []

    def take(bit):
        nonlocal level, offset
        level, offset = state_step(level, offset, bit)
        bits.append(bit)

    while level:
        constant = 3**max(-level, 0) - 5 * 3**max(level, 0)
        limit = v2(constant)
        if offset % 2 == 0 and (offset == 0 or v2(offset) > limit):
            take(1)
        while offset % 2 == 0:
            take(0)
        take(int(level > 0))

    while offset:
        if offset == -3:
            for bit in [1, 1, 0, 1, 0, 0, 0]:
                take(bit)
        elif offset % 2 == 0:
            take(0)
        else:
            zeros = 1 + v2((3 * offset - 5) // 2)
            take(1)
            for _ in range(zeros):
                take(0)
        if level != 0:
            raise AssertionError("excursion did not restore equal odd counts")
    return bits


@dataclass(frozen=True)
class Cell:
    residue: int
    length: int
    odds: int
    endpoint: int


def return_cell(residue, length):
    if length < 0 or not 0 <= residue < 2**length:
        raise ValueError("expected a canonical binary cell")
    x, p = walk(residue, length)
    y, t = walk(5 * residue, length)
    level = t - p
    offset = 3**max(0, -level) * y - 5 * 3**max(0, level) * x
    source, target = (3**p, x), (5 * 3**t, y)
    for parity in return_word(level, offset):
        bit = (parity - source[1]) % 2
        source, i = lift_step(source, bit)
        target, j = lift_step(target, bit)
        p, t = p + i, t + j
        residue += bit << length
        length += 1
    if p != t or target != (5 * source[0], 5 * source[1]):
        raise AssertionError("affine proportional return failed")
    return Cell(residue, length, p, source[1])


# Each tuple is (slope numerator, constant, clock, required input residue).
BLOCKS = [(1, 0, 1, 0), (9, 7, 6, 49), (27, 37, 8, 65)]


def modular_route(start, goal, modulus):
    """Use actual return blocks, whose induced permutations act transitively."""
    previous = {start: None}
    queue = deque([start])
    while goal not in previous and queue:
        value = queue.popleft()
        for index, (a, c, length, _) in enumerate(BLOCKS):
            new = (a * value + c) * pow(2**length, -1, modulus) % modulus
            if new not in previous:
                previous[new] = value, index
                queue.append(new)
    if goal not in previous:
        raise AssertionError("missing modular route")
    word = []
    while goal != start:
        goal, index = previous[goal]
        word.append(index)
    return word[::-1]


@dataclass(frozen=True)
class Landing:
    # The source is x0 + dx * ((2**b * q - z0) // dz).
    x0: int
    dx: int
    z0: int
    dz: int
    prefix: int
    b: int


def prescribed_landing(a, m, q, shifts=(0,)):
    """Give compact integer data even when the final power 2**b is huge."""
    if m < 1 or q < 1 or gcd(q, 6) != 1:
        raise ValueError("need a positive modulus and a positive odd target prime to three")
    bits = v2(m)
    residue = a % (1 << bits)
    for scale in [1, 5]:
        for shift in shifts:
            if shift:
                cert = construct((scale, 0), (scale, scale * shift), residue, bits)
                residue, bits = cert.residue, cert.bits
    cell = return_cell(residue, bits)
    odd_modulus = m >> v2(m)
    k = (a - cell.residue) * pow(2**cell.length, -1, odd_modulus) % odd_modulus
    x0, dx = cell.residue + (k << cell.length), odd_modulus << cell.length
    z0, dz = cell.endpoint + 3**cell.odds * k, odd_modulus * 3**cell.odds
    prefix = cell.length

    def append(index):
        nonlocal x0, dx, z0, dz, prefix
        slope, constant, length, needed = BLOCKS[index]
        bit_modulus = 2**length
        extra = (needed - z0) * pow(dz, -1, bit_modulus) % bit_modulus
        x0 += dx * extra
        dx *= bit_modulus
        z0, rem = divmod(slope * (z0 + dz * extra) + constant, bit_modulus)
        if rem:
            raise AssertionError("invalid word extension")
        dz *= slope
        prefix += length

    coprime = odd_modulus
    while coprime % 3 == 0:
        coprime //= 3
    order = 1
    while pow(2, order, coprime) != 1 % coprime:
        order += 1
    precision, temp = 1, order
    while temp % 3 == 0:
        precision += 1
        temp //= 3
    ternary = 3**precision
    e = next(i for i in range(2 * ternary // 3) if (55 * q * pow(2, i, ternary) - 7) % ternary == 0)
    tail = [1] * ((precision + 1) // 2) + [0] * e
    wanted = q % coprime
    for index in reversed(tail):
        slope, constant, length, _ = BLOCKS[index]
        wanted = ((wanted << length) - constant) * pow(slope, -1, coprime) % coprime
    for index in modular_route(z0 % coprime, wanted, coprime) + tail:
        append(index)
    if (z0 - q) % (coprime * ternary):
        raise AssertionError("terminal residue mismatch")

    exponent, period = 0, 2 * order
    while ternary < dz // coprime:
        ternary *= 3
        exponent = next(exponent + digit * period for digit in range(3)
                        if (q * pow(2, exponent + digit * period, ternary) - z0) % ternary == 0)
        period *= 3
    minimum = (z0 + dz * (1 + max([0] + [-c for c in shifts]))).bit_length()
    exponent += max(0, (minimum - exponent + period - 1) // period) * period
    if (q * pow(2, exponent, dz) - z0) % dz or x0 % m != a % m or dx % m:
        raise AssertionError("invalid simultaneous endpoint or source congruence")
    return Landing(x0, dx, z0, dz, prefix, exponent)


def hit_data(n, limit):
    p = 0
    for d in range(limit + 1):
        if n == 1:
            return d, p
        p += n % 2
        n = step(n)
    return None


def cost_within(q, source_grade, budget):
    if budget < 0:
        raise ValueError("negative budget")
    floor = source_grade + (6 - budget)//2
    target = 5*q
    deadline = max(0, 8*(target-1).bit_length() - 7*floor)
    hit = hit_data(target, deadline)
    if hit is not None:
        grade = hit[0] - 2 * hit[1]
        cost = abs(2 * (grade - source_grade) - 5)
        if cost <= budget:
            return cost
    return None


def replay_anchor_chain(q):
    """Construct every ordinary link. Multiplication is certified only at its actual anchor."""
    nodes = (1, 5, 7, 35, q, 5*q)
    hits = {n: hit_data(n, 500) for n in nodes}
    grades = {n: d - 2*p for n, (d, p) in hits.items()}
    delta = grades[5*q] - grades[q]
    net = [(1, 3-delta), (7, delta-2)]
    links = [(r, 1) for r, n in net for _ in range(max(n, 0))]
    links += [(r, -1) for r, n in net for _ in range(max(-n, 0))]
    exponent, grade = 0, grades[q]
    before = (q, 0, 0)  # (intercept, power of five in slope, power of two in slope)
    ordinary = []
    for r, sign in links:
        enter, leave = (r, 5*r) if sign == 1 else (5*r, r)
        binary = grades[enter] - grade
        ordinary.append((before, (enter, exponent, binary)))
        grade += sign * (grades[5*r] - grades[r])
        exponent += sign
        if exponent < 0:
            raise AssertionError("reversal with no factor of five")
        before = (leave, exponent, binary)
    ordinary.append((before, (5*q, 1, 0)))
    for u, v in ordinary:
        common = max(hits[u[0]][1], hits[v[0]][1])
        times = [grades[n] + 2*common for n, _, _ in (u, v)]
        depth = max(0, times[0]-u[2], times[1]-v[2])
        ends = []
        for (n, e, b), clocks in zip((u, v), times):
            start = n + 3 * 5**e * 2**(depth+b)
            endpoint, odds = walk(start, clocks)
            if odds != common:
                raise AssertionError("lost a padded first-hit prefix")
            ends.append(endpoint)
        if ends[0] != ends[1]:
            raise AssertionError("the two anchor-chain words have different endpoints")
    return len(links)


def verify():
    for level in range(-6, 7):
        for offset in range(-140, 141):
            s, d = level, offset
            for bit in return_word(s, d):
                s, d = state_step(s, d, bit)
            if (s, d) != (0, 0):
                raise AssertionError("failed signed-state replay")

    for bits in range(10):
        for residue in range(2**bits):
            cell = return_cell(residue, bits)
            if cell.residue % 2**bits != residue:
                raise AssertionError("lost the given cell")
            for free in [1, 37]:
                x = cell.residue + (free << cell.length)
                z = cell.endpoint + 3**cell.odds * free
                for multiplier in [1, 5]:
                    if walk(multiplier * x, cell.length) != (multiplier * z, cell.odds):
                        raise AssertionError("ordinary orbit disagreed with affine certificate")

    for a, c, length, residue in BLOCKS:
        for free in [0, 1, 27]:
            x = residue + 2**length * free
            z, rem = divmod(a * x + c, 2**length)
            if rem or any(walk(k*x, length)[0] != k*z for k in [1, 5]):
                raise AssertionError("invalid modular block")
    for modulus in [5, 7, 25, 35, 37, 49, 259]:
        for goal in range(modulus):
            last = 0
            for index in modular_route(0, goal, modulus):
                a, c, length, _ = BLOCKS[index]
                last = (a * last + c) * pow(2**length, -1, modulus) % modulus
            if last != goal:
                raise AssertionError("wrong terminal residue")

    for q in range(1, 54, 2):
        if q % 3 == 0:
            continue
        start = next(i for i in range(6, 12) if (2**i*q - 7) % 9 == 0)
        children = [(i, (2**i*q-7)//9) for i in range(start, start+13, 6)]
        units = [(i, x) for i, x in children if x % 3]
        if len(units) != 2:
            raise AssertionError("incorrect inverse branching")
        for clock, x in units:
            if x % 64 != 49 or any(walk(k*x, clock)[0] != k*q for k in (1, 5)):
                raise AssertionError("child failed to carry both parent endpoints")

    literal = 0
    for modulus, start, q, shifts in [
        (1, 0, 1, (0, 1)), (35, 1, 7, (0,)), (259, 17, 11, (0,)),
        (12, 0, 5, (0,)), (9, 3, 5, (0,)), (7, 3, 5, (0, 1)),
        (8, 5, 13, (-1, 0, 1)), (37, 1, 5, (0,)), (70, 10, 7, (0,)),
    ]:
        cert = prescribed_landing(start, modulus, q, shifts)
        if cert.b <= 6000:
            free = ((q << cert.b) - cert.z0) // cert.dz
            x = cert.x0 + cert.dx * free
            for shift in shifts:
                for scale in [1, 5]:
                    if walk(scale*(x+shift), cert.prefix+cert.b)[0] != scale*q:
                        raise AssertionError("wrong prescribed ordinary endpoint")
            literal += 1
    if literal < 3:
        raise AssertionError("insufficient literal target replays")

    for q, expected in [(1, 1), (7, 1), (11, 31), (41, 27)]:
        d, p = hit_data(q, 500)
        grade = d - 2*p
        if replay_anchor_chain(q) != expected:
            raise AssertionError("constructed chain length differs from the optimum")
        if cost_within(q, grade, expected) != expected or cost_within(q, grade, expected-1) is not None:
            raise AssertionError("incorrect sharp certificate budget")
    print(f"{literal} prescribed-target examples replayed as literal ordinary paths.")


if __name__ == "__main__":
    verify()
    print("Signed return states, all binary cells through 9 bits, CRT generators and a paired block passed.")
