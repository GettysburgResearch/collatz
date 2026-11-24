#!/usr/bin/env python3
"""Exact finite checks of selector outputs and ordinary delayed merges.

The synthetic scale 2^(j*j) controls source size only. This script does not
instantiate the widely separated cutoffs, decide global wrapped membership,
or prove the infinite counterexample.
"""
from bisect import bisect_right
from math import isqrt


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def step(x: int) -> int:
    return (3*x+1)//2 if x % 2 else x//2


def original_selector(x: int) -> tuple[int, int, int]:
    depth = x.bit_length()-1
    horizon = min(isqrt(depth), depth//2)
    powers = [1]
    while powers[-1] <= (x+1) << horizon:
        powers.append(3*powers[-1])
    best_depth = -1
    output, clock, state = x, 0, x
    for j in range(horizon+1):
        m = bisect_right(powers, state//7)-1
        if m >= 0:
            offset = state-7*powers[m]
            if offset == 0:
                t = depth
            else:
                t = min(depth, bisect_right(powers, (powers[m]-1)//offset)-1)
            if t > best_depth:
                output, clock, best_depth = state, j, t
        state = step(state)
    return output, clock, best_depth


def run(j: int) -> None:
    size = 1 << (j*j)
    anchor = 7
    while anchor < size:
        anchor *= 3
    d = next(i for i in range(2*j, 2*j+6) if (i-j+1) % 6 == 1)
    modulus = 18*(1 << d)
    offset = (13*(1 << d)-anchor-1) % modulus + 1
    s = anchor+offset
    other = 3*s+(1 << d)
    u = s >> d
    require(s == (1 << d)*u and u % 18 == 13, f'CRT mismatch at {j}')
    require(other == (1 << d)*(3*u+1), f'other branch mismatch at {j}')
    require(0 < offset and (3*offset+(1 << d))**2 <= size,
            f'offset not within tested square-root bound at {j}')
    selector_depths = []
    first, second = s, other
    for root in (s, other):
        value, clock, selected_depth = original_selector(root)
        require(value == root and clock == 0 and selected_depth > 0,
                f'ordinary selector failed at {j}')
        selector_depths.append(selected_depth)
    for i in range(d):
        require(first != second and first % 2 == second % 2 == 0,
                f'halving or distinctness failed at {j}, {i}')
        if i in (j-1, j+5):
            for x in (first, second):
                m = (4*x-5)//9
                require(x % 18 == 8 and step(step(m)) == x and m+2 <= x//2,
                        f'ancestor edge failed at {j}, {i}')
                require((2*step(x)-1) % 3 != 0, f'nonunique parent at {j}, {i}')
        first, second = step(first), step(second)
    require(first == u and second == 3*u+1 and first != second and
            step(first) == step(second), f'delayed collision failed at {j}')
    print(f'PASS j={j} bits={s.bit_length()},{other.bit_length()} '
          f'd={d} selector_depths={selector_depths[0]},{selector_depths[1]}')


if __name__ == '__main__':
    for scale in (8, 12, 16, 24, 32, 64):
        run(scale)
    print('PASS ordinary selector, congruences, cheaper ancestors and delayed merges; '
          'no finite test of wrapped global membership')
