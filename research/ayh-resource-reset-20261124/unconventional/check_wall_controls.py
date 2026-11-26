#!/usr/bin/env python3
"""Replay finite signed, ordinary and symbolic controls for adjacent Collatz walls."""
import json
from functools import cache


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n, d=1):
    return (3*n+d)//2 if n%2 else n//2


def profile(n, h, d=1):
    odds = 0
    for _ in range(h):
        odds += n%2
        n = step(n, d)
    return n, odds


def cycle(n, d):
    seen = {}
    path = []
    while n not in seen:
        require(len(path) < 10_000, 'len(path) < 10_000')
        seen[n] = len(path)
        path.append(n)
        n = step(n, d)
    return tuple(path[seen[n]:])


def rational_control():
    left, right = -11, 4
    pairs = []
    for bit in (1, 0, 1, 1):
        ca, cb = cycle(left, 15), cycle(right, 15)
        require(set(ca) == {3, 12, 6}, 'set(ca) == {3, 12, 6}')
        require(set(cb) == {57, 93, 147, 228, 114}, 'set(cb) == {57, 93, 147, 228, 114}')
        pairs.append((left, right))
        left = 2*left + 15*bit
        right = left + 15
    require((left, right) == (-11, 4), '(left, right) == (-11, 4)')
    return {"denominator": 15, "phase_numerators": pairs,
            "left_cycle": [3, 12, 6], "right_cycle": [57, 93, 147, 228, 114]}


def first_cut(j, r):
    for h in range(1, j+1):
        prefix = r >> (j-h)
        if profile(prefix, h) == profile(prefix+1, h):
            return h, prefix
    raise ValueError("retained by every tested prefix")


def midpoint_child(color, n):
    require(color(n) != color(n+1), 'color(n) != color(n+1)')
    m = 2*n + int(color(2*n+1) == color(n))
    require((color(m), color(m+1)) == (color(n), color(n+1)), '(color(m), color(m+1)) == (color(n), color(n+1))')
    return m


def path(n, h):
    values = [n]
    for _ in range(h):
        values.append(step(values[-1]))
    return values


def transverse_case(a, b, j, target):
    @cache
    def color(n):
        seen = set()
        while n != target and n not in seen:
            seen.add(n)
            n = step(n)
            require(len(seen) < 10_000, 'len(seen) < 10_000')
        return n == target

    def transport(x, y):
        require(x%4 == 1 and y == (3*x+1)//4, 'x%4 == 1 and y == (3*x+1)//4')
        require(path(x, 2)[-1] == y, 'path(x, 2)[-1] == y')
        require(path(x+1, 2)[-1] == y+1, 'path(x+1, 2)[-1] == y+1')
        require((color(x),color(x+1)) == (color(y),color(y+1)), '(color(x),color(x+1)) == (color(y),color(y+1))')
        if target == 5:
            require(5 not in path(x,2)[:-1] + path(x+1,2)[:-1], '5 not in path(x,2)[:-1] + path(x+1,2)[:-1]')

    transport(a, b)
    x, z = a, b
    for _ in range(j):
        if target == 5:
            # All child and parent starts used to inherit signed colors
            # avoid the only exceptional edge 5 -> 8.
            require(min(x,z) > 5, 'min(x,z) > 5')
        x, z = midpoint_child(color,x), midpoint_child(color,z)
    y = (3*x+1)//4
    transport(x, y)
    require(y != z, 'y != z')
    h, r = first_cut(j, y - (1<<j)*b)
    parent = (1<<h)*b + r
    require(profile(parent,h) == profile(parent+1,h), 'profile(parent,h) == profile(parent+1,h)')
    if target == 5:
        require(5 not in path(parent,h)[:-1] + path(parent+1,h)[:-1], '5 not in path(parent,h)[:-1] + path(parent+1,h)[:-1]')
    return {"roots": [a,b], "depth": j, "source_index": x,
            "transported_index": y, "destination_index": z,
            "transported_offset": y-(1<<j)*b, "removed_prefix": [h,r],
            "oriented_colors": [color(a), color(a+1)]}


def forbidden(depth):
    live = {0: (0,0,1,0)}
    words = []
    for h in range(1, depth+1):
        mask = (1<<(h-1))-1
        new = {}
        for parent in live:
            for bit in (0,1):
                w = 2*parent+bit
                low = w & mask
                if low not in live:
                    continue
                x,p,y,q = live[low]
                top = w>>(h-1)
                x += top*3**p
                y += top*3**q
                x,p = step(x),p+x%2
                y,q = step(y),q+y%2
                if (x,p) == (y,q):
                    words.append(f"{w:0{h}b}")
                else:
                    new[w]=(x,p,y,q)
        live=new
    return words


def first_sqrt_bound(words):
    prefixes = {""}
    for w in words:
        prefixes.update(w[:i] for i in range(1,len(w)))
    prefixes = sorted(prefixes)
    ids = {p:i for i,p in enumerate(prefixes)}
    edges = []
    for p in prefixes:
        row = []
        for b in "01":
            t = p+b
            if any(t.endswith(w) for w in words):
                continue
            while t not in ids:
                t=t[1:]
            row.append(ids[t])
        edges.append(row)
    v = [0]*len(prefixes)
    v[ids[""]]=1
    for j in range(1,601):
        nxt=[0]*len(v)
        for multiplicity, row in zip(v,edges):
            for t in row:
                nxt[t]+=multiplicity
        v=nxt
        if sum(v)**2 < 2**j:
            return j,sum(v)
    raise ValueError("test horizon exhausted")


def main():
    capacity = {}
    for h in (13,22):
        f = forbidden(h)
        j,b = first_sqrt_bound(f)
        capacity[h] = {"minimal_forbidden_words":len(f), "block_length":j,
                       "admissible_blocks":b, "strict_square_comparison":b*b < 2**j}
    signed = transverse_case(-7,-5,9,-1)
    ordinary = transverse_case(113,85,5,5)
    require((signed["transported_index"],signed["removed_prefix"]) == (-2330,[6,28]), '(signed["transported_index"],signed["removed_prefix"]) == (-2330,[6,28])')
    require((ordinary["transported_index"],ordinary["removed_prefix"]) == (2728,[4,4]), '(ordinary["transported_index"],ordinary["removed_prefix"]) == (2728,[4,4])')
    out = {"signed_rational_periodic_wall": rational_control(),
           "negative_integer_global_basin": signed,
           "ordinary_visit_to_5_local_control": ordinary,
           "single_edge_language_capacity": capacity}
    print(json.dumps(out,indent=2))


if __name__ == "__main__":
    main()
