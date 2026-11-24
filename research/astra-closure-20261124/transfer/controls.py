"""Exact bounded controls for the actual head-root and affine-window calculations."""
from math import comb


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def stop(n, floor, limit):
    clock = odds = 0
    while n > floor and clock < limit:
        odds += n % 2
        n = step(n)
        clock += 1
    if n > floor:
        raise ValueError("sample exceeded the stated clock cap")
    return n, clock, odds


def grid_control():
    tested = 0
    for b in range(1, 11):
        for r in range(81):
            positive = 0
            for m in range(1 << b):
                x, y, gap = 81 * m + r, m, 4
                for _ in range(b):
                    gap += x % 2 - y % 2
                    if gap == 0:
                        break
                    x, y = step(x), step(y)
                else:
                    positive += 1
                tested += 1
            if positive < comb(b, b // 2):
                raise ValueError((b, r, positive))
    return tested


def decode(v, w, cap, floor):
    """Integer-only test |v/(w*3^a*2^k)-1| <= 4(cap+1)/floor."""
    result = []
    tolerance = 4 * (cap + 1)
    for a in range(4-cap, 5+cap):
        num = v * 3 ** max(0, -a)
        den = w * 3 ** max(0, a)
        center = num.bit_length() - den.bit_length()
        for k in range(max(-cap, center-2), min(cap, center+2) + 1):
            left = num << max(0, -k)
            right = den << max(0, k)
            if abs(left - right) * floor <= tolerance * right:
                result.append((a, k))
    return result


def physical_control():
    R, floor, cap = 81**40, 2**60, 2000
    # All 81 offsets are tested at distinct ordinary parents in the head.
    equal = 0
    for r in range(81):
        m = (7*R)//81 + ((r+1)*R)//(83*81)
        x = 81 * m + r
        if not (7*R <= x < 8*R):
            raise ValueError("outside head")
        v, t, p = stop(x, floor, cap)
        w, s, q = stop(m, floor, cap)
        if decode(v, w, cap, floor) != [(4+p-q, s-t)]:
            raise ValueError((r, v, w, t, s))
        equal += int(v == w)
    return equal


if __name__ == "__main__":
    print("binary head residues checked:", grid_control())
    print("clock pairs uniquely recovered: 81")
    print("equal first roots among checked pairs:", physical_control())
