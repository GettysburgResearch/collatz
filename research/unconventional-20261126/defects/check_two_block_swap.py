#!/usr/bin/env python3
"""Exhaust the proven two-block parameter cut and replay the physical counterexample."""
import json
from itertools import product


def block(x):
    t = ((x+1) & -(x+1)).bit_length()-1
    v = 3**t * ((x+1) >> t)-1
    b = (v & -v).bit_length()-1
    return t, b, v >> b


def main():
    total = comparable = 0
    for t, u, b, c in product(range(1,3),range(1,11),range(1,13),range(1,13)):
        total += 1
        if (t,b) == (u,c) or b+c > 12 or 2**(t+u+b+c) > 12*3**(t+u):
            continue
        comparable += 1
        left = (2**b-1)*2**t*3**u + 2**(c+t+u)
        right = (2**c-1)*2**u*3**t + 2**(b+t+u)
        if (left-right) % 3**(t+u) == 0:
            raise ArithmeticError((t,b,u,c))
    left, right = (block(1893), block(355)), (block(1891), block(133))
    if left != ((1,3,355),(2,5,25)) or right != ((2,5,133),(1,3,25)):
        raise ArithmeticError("physical swap outside the floor")
    print(json.dumps({"tuples":total,"eligible_distinct_gain_and_cap":comparable,
                      "integral_swaps":0,"outside_floor_paths":[left,right]},indent=2))


if __name__ == "__main__":
    main()
