"""Exact adaptive-core and local signed-cut checks. Run with --cap 4 by default."""
import argparse
import json
from collections import deque
from math import comb


def odd_step(n):
    value = 3 * n + 1
    return value // (value & -value)


def runs(n):
    return (n & ~(n >> 1)).bit_count()


def inverse_basin(cap):
    seen = {1}
    queue = deque([1])
    while queue:
        n = queue.popleft()
        if n % 3 == 0:
            continue
        exponent = 1 if n % 3 == 2 else 2
        predecessor = ((n << exponent) - 1) // 3
        while runs(predecessor) <= cap:
            if predecessor not in seen:
                seen.add(predecessor)
                queue.append(predecessor)
            predecessor = 4 * predecessor + 1
    return seen


def check_core(cap):
    success = set()
    sources = 0
    max_exit = 0
    max_gap_clock = 0
    witness = 1

    def walk(prefix, depth):
        nonlocal sources, max_exit, max_gap_clock, witness
        if depth % 2 == 0:
            sources += 1
            assert runs(prefix) == depth // 2
            n = prefix
            seen = set()
            while n != 1 and runs(n) <= cap:
                if n in seen:
                    raise AssertionError(f"capped cycle reached from {prefix}: {n}")
                seen.add(n)
                n = odd_step(n)
            if n == 1:
                success.add(prefix)
            if len(seen) > max_exit:
                max_exit = len(seen)
                witness = prefix
        if depth == 2 * cap:
            return
        upper = prefix
        clock = 0
        while runs(upper >> 1) <= cap:
            upper *= 3
            clock += 1
        max_gap_clock = max(max_gap_clock, clock)
        sign = -1 if depth % 2 else 1
        for gap in range(1, 2 * clock + 1):
            walk((prefix << gap) + sign, depth + 1)

    walk(1, 1)
    assert success == inverse_basin(cap)
    return dict(cap=cap, core=sources, basin=len(success), max_core_clock=max_exit,
                max_outside_clock_bound=max_gap_clock, max_core_witness=witness)


def check_windows():
    count = 0
    for m in range(3, 12):
        length = 1 << (m - 2)
        gap = 2 * length + 1
        for upper in (1, 3, 7, 13, 55):
            for lower in (-15, -7, -3, -1, 1, 3, 9, 15):
                shift = gap + abs(lower).bit_length()
                source = (upper << shift) + lower
                n, v, high = source, lower, upper
                counts = [0, 0, 0]
                for _ in range(length):
                    assert n == (high << shift) + v
                    assert (n >> (shift + 1)) == high >> 1
                    marked = runs(n)
                    for cap in (1, 2, 3):
                        counts[cap - 1] += marked <= cap
                    valuation = ((3 * v + 1) & -(3 * v + 1)).bit_length() - 1
                    n, v, high = odd_step(n), odd_step(v), high * 3
                    shift -= valuation
                for cap in (1, 2, 3):
                    assert counts[cap - 1] <= sum(comb(m, 2*t) for t in range(cap + 1))
                count += 1
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cap", type=int, default=4)
    args = parser.parse_args()
    if args.cap < 1:
        parser.error("cap must be positive")
    print(json.dumps({"signed_windows": check_windows(),
                      "cores": [check_core(cap) for cap in range(1, args.cap + 1)]},
                     indent=2))
