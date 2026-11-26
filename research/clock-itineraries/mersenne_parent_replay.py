"""Independently replay the first delayed parent with 383-step physical Collatz blocks."""
from collections import namedtuple

BLOCK = 383
MASK = (1 << BLOCK) - 1
POWERS = tuple(3**i for i in range(BLOCK + 1))
Orbit = namedtuple("Orbit", ["clock", "odd"])


def step(n):
    return (3*n + 1)//2 if n % 2 else n//2


def block(n):
    """Advance the low part by complete runs of ones or zeros, then lift the quotient."""
    low = n & MASK
    left = BLOCK
    odd = 0
    while left and low:
        bit = low & 1
        u = low + bit
        run = min(left, (u & -u).bit_length() - 1)
        if bit:
            low = (u >> run)*POWERS[run] - 1
            odd += run
        else:
            low >>= run
        left -= run
    return low + POWERS[odd]*(n >> BLOCK), odd


def first_from_peak(n, claim):
    clock = odd = 0
    # During such a block every state is at least n/2^BLOCK > 1.
    while n > 1 << BLOCK:
        n, grade = block(n)
        clock += BLOCK
        odd += grade
        if clock > claim:
            raise ValueError("The first hit exceeded the stated clock")
    while n != 1:
        odd += n % 2
        n = step(n)
        clock += 1
        if clock > claim:
            raise ValueError("The first hit exceeded the stated clock")
    return Orbit(clock, odd)


def main():
    m = 12 * 2**18 - 1
    parent, remainder = divmod(2**(m+7) - 271, 81)
    if remainder:
        raise ValueError("Nonintegral parent")
    x = parent
    for _ in range(7):
        x = step(x)
    if x != 2**m - 1:
        raise ValueError("Incorrect seven-step entry to the Mersenne ramp")
    # T^m(2^m-1)=3^m-1 by the m consecutive odd steps. Its endpoint is >2.
    peak = 3**m - 1
    result = first_from_peak(peak, 24_052_486)
    total = 7 + m + result.clock
    if result != Orbit(24_052_486, 12_029_702) or total != 27_198_220:
        raise ValueError("Trajectory disagrees with the claimed exact counts")
    print(f"m={m}, peak first hit={result.clock}, peak odd departures={result.odd}, "
          f"parent first hit={total}")


if __name__ == "__main__":
    main()
