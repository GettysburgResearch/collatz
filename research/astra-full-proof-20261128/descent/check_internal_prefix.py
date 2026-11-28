"""Check every admissible prefix in a fixed positive range and all-future controls."""

from collections import Counter
from fractions import Fraction

from check_upper_shadow import first_upper_hit, require, step, v2


def prefix_replay(z):
    h, r = first_upper_hit(z)
    lower, upper = [z], [3 * z]
    positions = []
    counts = [0]
    for i in range(h + 4 * (r + 1)):
        counts.append(counts[-1] + lower[-1] % 2)
        if i < h and upper[-1] % 2:
            positions.append(i)
        lower.append(step(lower[-1]))
        upper.append(step(upper[-1]))
    require(len(positions) == r, "upper odd count changed")
    states = []
    outcomes = Counter()
    c = 0
    for j, u in enumerate(positions, start=1):
        c = 3 * c + 2**u
        q = 3 ** (j + 1)
        center = Fraction(-c, q)
        t = 0
        while center.denominator != 1:
            center = step(center)
            t += 1
        s = int(center)
        if states:
            old_t, old_s = states[-1]
            if old_t <= u:
                shift = u - old_t
                value = 3 * old_s - 2**shift
                even = v2(abs(value))
                expected = ((value // 2**even) + 1) // 2
                require((t, s) == (old_t + even + 1, expected), "prefix transition")
                outcomes["updated"] += 1
        states.append((t, s))
        stop = positions[j] if j < r else h
        if t > stop:
            outcomes["short"] += 1
            continue
        require(2**stop * upper[stop] == q * z + c, "cut carry")
        gap = stop - t
        require(lower[t] == 2**gap * upper[stop] + s, "release lift")
        signed = s
        odds = 0
        for _ in range(gap):
            odds += signed % 2
            signed = step(signed)
        require(lower[stop] == 3**odds * upper[stop] + signed, "end lift")
        outcomes["in range"] += 1
    cutoff = h + 4 * (r + 1)
    upper_odds = 0
    counted = False
    for i in range(cutoff + 1):
        if lower[i] == upper[i] and counts[i] == 1 + upper_odds:
            counted = True
        upper_odds += upper[i] % 2
    t, s = states[-1]
    if t <= h and s < 0:
        require(not counted, "negative center counted merger")
    elif t <= h and s == 0:
        require(counted, "zero center missing counted merger")
    outcomes["counted"] += counted
    return outcomes


def main():
    total = Counter()
    for z in range(17, 20000, 48):
        total.update(prefix_replay(z))
    print("417 fixed canonical starts:", dict(total))
    for m, expected in [(1, 1), (2, 1), (3, 2)]:
        x = 3**m - 1
        t = p = 0
        while x != 1:
            p += x % 2
            x = step(x)
            t += 1
        require(2 * p - t + 2 * m == expected, "Mersenne charge")
    print("Mersenne postpeak conserved charges at exponents 1, 2, 3: 1, 1, 2")


if __name__ == "__main__":
    main()
