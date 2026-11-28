#!/usr/bin/env python3
"""Finite-field controls on the native layered carry pencil and reachable ports."""

from collections import defaultdict
import json


PRIME = 101


def reduce_vector(vector, pivots):
    v = {i: a % PRIME for i, a in vector.items() if a % PRIME}
    while v:
        i = min(v)
        if i not in pivots:
            inv = pow(v[i], -1, PRIME)
            return {j: (x * inv) % PRIME for j, x in v.items()}
        factor = v[i]
        for j, coefficient in pivots[i].items():
            x = (v.get(j, 0) - factor * coefficient) % PRIME
            if x:
                v[j] = x
            elif j in v:
                del v[j]
    return {}


def pencil_columns(width):
    m = 3 ** (width - 1)
    for tag in (0, 1):
        for w in range(6 * m):
            start = {2 * m * tag + w // 3: 1}
            end = defaultdict(int, {2 * m * tag + w % (2 * m): 1})
            end[4 * m + w % (3 * m)] += 1
            if tag:
                start[4 * m + w // 2] = 1
            else:
                end[4 * m + w // 2] -= 1
            yield {j:x for j,x in start.items() if x}, {j:x for j,x in end.items() if x}


def pencil_rank(width, value):
    pivots = {}
    for start, end in pencil_columns(width):
        col = defaultdict(int, end)
        for j, x in start.items():
            col[j] -= value * x
        reduced = reduce_vector(col, pivots)
        if reduced:
            pivots[min(reduced)] = reduced
    return len(pivots)


def next_reachable(width, current, reverse=False):
    # Eliminate the start part of (start,end), modulo previously reachable starts.
    # Columns with zero start then supply exactly the next reachable end space.
    port_size = 7 * 3 ** (width - 1)
    pivots = {min(v): v for v in current}
    for start, end in pencil_columns(width):
        if reverse:
            start, end = end, start
        combined = dict(start)
        combined.update({port_size+j: x for j,x in end.items()})
        reduced = reduce_vector(combined, pivots)
        if reduced:
            pivots[min(reduced)] = reduced
    return [{j-port_size:x for j,x in v.items()}
            for i,v in pivots.items() if i >= port_size]


def main():
    cases = []
    for width in (1, 2, 3, 4, 5):
        m = 3 ** (width-1)
        ranks = {str(x):pencil_rank(width,x) for x in (0,1,2,100)}
        expected = {str(x):6*m - (2 if x == 1 else 0) for x in (0,1,2,100)}
        if ranks != expected:
            raise ArithmeticError((width,ranks,expected))
        case = {'window': width, 'rows': 7*m, 'columns': 12*m,
                'ranks_mod_101_at_0_1_2_minus1': list(ranks.values())}
        if width <= 3:
            sizes = []
            for reverse in (False,True):
                current = []
                dimensions = [0]
                while True:
                    current = next_reachable(width,current,reverse)
                    dimensions.append(len(current))
                    if dimensions[-1] == dimensions[-2]: break
                sizes.append(dimensions)
            case['reach_from_zero_forward_backward'] = sizes
        cases.append(case)
    print(json.dumps({'finite_pencils': cases},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
