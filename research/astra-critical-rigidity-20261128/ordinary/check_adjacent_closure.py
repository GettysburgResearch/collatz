"""Close actual unmerged prefixes and replay the adjacent rational and ordinary loops."""

from collections import Counter
import json


def need(condition, message):
    if not condition:
        raise ValueError(message)


def step(x, q=1):
    return (3*x+q)//2 if x % 2 else x//2


def itinerary(s, steps):
    a, b = s, 3*s
    path = []
    for _ in range(steps):
        path.append((a % 2, b % 2))
        a, b = step(a), step(b)
    return a, b, path


def flip_path():
    end_a, end_b, full = itinerary(7, 11)
    need((end_a, end_b) == (1, 2), "wrong signed seed")
    tail = full[2:]
    need(tuple(map(sum, zip(*tail))) == (3, 3), "incorrect sign-flip grades")
    return [(v, u) for u, v in tail]


FLIP = flip_path()


def close_prefix(a, b, path):
    g, h = tuple(map(sum, zip(*path)))
    budget = g+h
    signed_j = h+1-g
    swapped = signed_j < 0
    if swapped:
        a, b = b, a
    j = abs(signed_j)
    d = 3**j*a-b
    need(abs(d) <= 3**(budget+1) and j <= budget+1, "endpoint determinant estimate")
    need(d != 0 and (j == 0 or d % 3), "inadmissible endpoint translation")
    loop = [(0, 1)] + path[1:]
    descent = []
    events = Counter()
    events["swapped"] = int(swapped)
    while j:
        while d % 2 == 0:
            descent.append((0, 0))
            events["level_common_evens"] += 1
            d //= 2
        if (j, d) == (1, -1):
            descent.extend(((0, 1), (0, 0), (1, 0), (1, 0)))
            j, d = 0, 1
            events["exceptional_detours"] += 1
        else:
            descent.append((1, 0))
            d = (d+3**(j-1))//2
            j -= 1
        need(d != 0, "return fell into diagonal")
    if swapped:
        loop.extend((v, u) for u, v in descent)
        d = -d
    else:
        loop.extend(descent)
    while abs(d) > 1:
        before = abs(d)
        if d % 2 == 0:
            loop.append((0, 0))
            d //= 2
        else:
            # Lower odd/even has offset 1, lower even/odd has offset 2.
            delta = 1 if (3*d+1) % 4 == 0 else -1
            loop.extend(((0, 1), (1, 0)) if delta == 1 else ((1, 0), (0, 1)))
            d = (3*d+delta)//4
        need(d != 0 and 8*abs(d) <= 7*before, "equal-slope return did not contract")
    if d == -1:
        loop.extend(FLIP)
        events["sign_flips"] += 1
    l, r = tuple(map(sum, zip(*loop)))
    need(l == r and 0 < l <= 16*(budget+1), "incorrect loop grade")
    need(len(loop) >= len(path), "closure shortened native time")
    return loop, events


def carry(word):
    c = p = 0
    for i, b in enumerate(word):
        if b:
            c, p = 3*c+(1 << i), p+1
    return c, p


def replay(loop):
    u, v = tuple(zip(*loop))
    c, p = carry(u)
    d, p2 = carry(v)
    length = len(loop)
    denominator = (1 << length)-3**p
    need(p == p2 and c-d == denominator, "static ordered equation failed")
    # A native integer on OO/OE with the prescribed next lower calendar.
    modulus = 1 << (length+2)
    lower_residue = (-c*pow(3**p, -1, 1 << length)) % (1 << length)
    s = ((4*lower_residue-5)*pow(9, -1, modulus)) % modulus
    need(s % 4 == 3 and s > 0, "incorrect ordinary lift cylinder")
    aa, bb = s, 3*s
    rx, ry, q = c, d, denominator
    if q < 0:
        rx, ry, q = -rx, -ry, -q
    x0, y0 = rx, ry
    need(x0-y0 == q, "rational phases are not adjacent")
    for t, letter in enumerate([(1, 1), (1, 0)]+loop):
        need(aa != bb and (aa % 2, bb % 2) == letter, "physical loop parity or separation failed")
        aa, bb = step(aa), step(bb)
        if t >= 2:
            need(rx != ry and (rx % 2, ry % 2) == letter, "rational loop parity or separation failed")
            rx, ry = step(rx, q), step(ry, q)
    need(aa-bb == 1 and (rx, ry) == (x0, y0), "ordinary or rational endpoints failed")
    return int(denominator > 0)


def main():
    counts = Counter()
    longest = {}
    for s in range(1, 2048, 2):
        a, b = s, 3*s
        path = []
        for k in range(1, 41):
            path.append((a % 2, b % 2))
            a, b = step(a), step(b)
            if a == b:
                break
            if k not in (1, 2, 3, 5, 8, 13, 21, 34, 40):
                continue
            loop, event = close_prefix(a, b, path)
            positive = replay(loop)
            counts["prefixes"] += 1
            counts["positive_adjacent_loops" if positive else "negative_adjacent_loops"] += 1
            counts.update(event)
            if len(loop) > longest.get("closed_clock", 0):
                longest = {"source": s, "prefix_clock": k, "closed_clock": len(loop),
                           "joint_odd_grade": 2*sum(x for x, y in loop)}
    need(min(counts[k] for k in ("positive_adjacent_loops", "swapped",
                                "level_common_evens", "exceptional_detours", "sign_flips")) > 0,
         "a return branch lacked independent physical replay")
    # Route translation 1 to 2, insert an expanding negative-cycle block,
    # then return to 1. The two rational centers of each inner block are -5,-7.
    letters = {"U": (0, 1), "D": (1, 0), "E": (0, 0), "O": (1, 1)}
    to_two = [letters[ch] for ch in "UUDOODE"]
    expanding = [(1, 1), (1, 0), (0, 1)]
    negative = to_two + expanding*10 + [letters["E"]]
    need(replay(negative) == 0, "negative adjacent-cycle control failed")
    print(json.dumps({"counts": dict(sorted(counts.items())), "longest": longest,
                      "negative_adjacent_control": {"clock": len(negative),
                          "grades": list(map(sum, zip(*negative)))}}, indent=2))


if __name__ == "__main__":
    main()
