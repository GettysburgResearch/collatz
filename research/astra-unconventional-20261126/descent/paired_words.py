"""Exact binary-word witnesses for chart repair and the long internal cycle."""
from fractions import Fraction


def transition(d, c, lower):
    upper = (c + lower) % 2
    left = max(0, -d)
    right = max(0, d)
    peeled = min(left + lower, right + upper)
    twice = (3 ** (lower + upper - peeled) * c
             + 3 ** (left + lower - peeled) * upper
             - 3 ** (right + upper - peeled) * lower)
    if twice % 2:
        raise ArithmeticError("nonintegral normalized carry")
    return d + upper - lower, twice // 2, upper


def walk(state, lower):
    d, c = state
    upper = []
    for bit in lower:
        d, c, other = transition(d, c, int(bit))
        upper.append(str(other))
    return (d, c), "".join(upper)


def halves_then(events):
    """One (length, lower bit) ends a block of common initial halvings."""
    return "".join("0" * (clock - 1) + str(bit) for clock, bit in events)


PREFIX = halves_then([(1, 0)] * 7 + [(1, 1), (2, 0), (3, 0), (1, 0), (3, 1)])
LAP = halves_then([(1, 0), (10, 1), (8, 0), (1, 1)])
EXIT = halves_then([(1, 0), (10, 1), (8, 1), (1, 1), (1, 1), (1, 1),
                    (6, 1), (4, 1), (1, 1), (1, 1)]) + "000"


def offset(word):
    c = 0
    for h, bit in enumerate(word):
        if bit == "1":
            c = 3*c + 2**h
    return c


def check():
    root = (1, -1)
    hub = (9, -9899)
    for start, bits, end, grades in ((root, PREFIX, hub, (2, 10)),
                                      (hub, LAP, hub, (2, 2)),
                                      (hub, EXIT, root, (9, 1))):
        state, upper = walk(start, bits)
        if state != end or (bits.count("1"), upper.count("1")) != grades:
            raise ValueError("incorrect carry trace or grades")
    repairs = [((1, 1), "001"), ((-1, -1), "100000001")]
    for state, lower in repairs:
        if walk(state, lower)[0] != root:
            raise ValueError("incorrect repair")
    for n in range(6):
        word = PREFIX + LAP*n + EXIT
        state, upper = walk(root, word)
        p = 11 + 2*n
        if (state, len(word), word.count("1"), upper.count("1")) != (root, 54+20*n, p, p):
            raise ValueError("incorrect total")
        if offset(upper)-3*offset(word) != 3**p-2**len(word):
            raise ValueError("affine constants do not return")
    _, upper = walk(hub, LAP)
    den = 2**len(LAP)-3**LAP.count("1")
    centers = (Fraction(offset(LAP), den), Fraction(offset(upper), den))
    if centers[1] != 3**9*centers[0]-9899:
        raise ValueError("incorrect rational fixed points")
    return {"prefix": PREFIX, "lap": LAP, "exit": EXIT,
            "center": [str(q) for q in centers]}


if __name__ == "__main__":
    import json
    print(json.dumps(check(), sort_keys=True))
