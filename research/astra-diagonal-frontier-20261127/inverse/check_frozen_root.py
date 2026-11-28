#!/usr/bin/env python3
"""Exhaust every relevant ordinary unit source at target 25 through depth 89."""


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def step(x):
    v = 3 * x + 1
    e = (v & -v).bit_length() - 1
    return v >> e, e


def main():
    root, limit = 25, 89
    # The exact affine inverse formula has a positive subtracted offset.
    caps = [(root << (7 * b // 4)) // 3**b for b in range(1, limit + 1)]
    upper = max(caps)
    returns, y = [], root
    while y != 1:
        y, _ = step(y)
        returns.append(y)
    check(root not in returns, "root could be visited twice")
    witnesses = []
    for x in range(1, upper + 1, 2):
        if x % 3 == 0:
            continue
        y, total, passing = x, 0, True
        for b in range(1, limit + 1):
            y, e = step(y)
            total += e
            passing = passing and 4 * total <= 7 * b
            if y == root and 4 * total <= 7 * b:
                check(x <= caps[b - 1], "arithmetic height cutoff")
                witnesses.append((b, x, total, passing))
            if y in (1, root):
                break
    witnesses.sort()
    check(witnesses[:2] == [(88, 586223, 154, True),
                            (88, 588103, 154, True)], "first equality witnesses")
    check(len(witnesses) == 3 and witnesses[2][0] == 89
          and 4 * witnesses[2][2] < 7 * 89 and witnesses[2][3], "first strict witness")
    print(f"All positive odd unit sources through {upper} at depths 1–{limit}: {witnesses}")


if __name__ == "__main__":
    main()
