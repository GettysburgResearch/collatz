"""Replay finite ordinary rows, simultaneous lifts and the small-tail obstruction."""

import json
from collections import Counter, defaultdict
from fractions import Fraction


def require(condition, code):
    if not condition:
        raise ValueError(code)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def path(x, h):
    word = []
    for _ in range(h):
        word.append(x % 2)
        x = step(x)
    return tuple(word), x


def carry(word):
    c = 0
    for i, odd in enumerate(word):
        c = (3 * c + 2**i) if odd else c
    return c


def roots(x, h):
    a, b = x, 5 * x
    p = k = 0
    out = []
    for j in range(1, h + 1):
        p += a % 2
        k += b % 2
        a, b = step(a), step(b)
        if a * 5 == b and p == k:
            out.append((j, a))
    return out


def parse_marks(x, h):
    """Use a fresh first return and its whole even padding at each odd mark."""
    a, b = x, 5 * x
    elapsed = blocks = 0
    while elapsed < h:
        require(a % 2 == 1 and b == 5 * a, "mark start")
        p = k = 0
        while elapsed < h:
            p += a % 2
            k += b % 2
            a, b = step(a), step(b)
            elapsed += 1
            if p == k and b == 5 * a:
                break
        require(p == k and b == 5 * a, "incomplete return")
        while a % 2 == 0:
            require(elapsed < h and b % 2 == 0, "incomplete padding")
            a, b = step(a), step(b)
            elapsed += 1
        blocks += 1
    return blocks, a


def valuation2(z):
    require(z != 0, "zero valuation")
    z = abs(z)
    return (z & -z).bit_length() - 1


def advance(k, d, i):
    j = (i + d) % 2
    n = k + j - i
    sm, nm, np = max(-k, 0), max(-n, 0), max(n, 0)
    exponent = nm + j - sm
    require(exponent >= 0, "negative exponent in state")
    value = 3**exponent * d + 3**nm * j - 5 * 3**np * i
    require(value % 2 == 0, "state parity")
    return n, value // 2


def steer(k, d):
    word = []

    def push(i):
        nonlocal k, d
        k, d = advance(k, d, i)
        word.append(i)
        require(len(word) < 10000, "steering control guard")

    while k != 0:
        if d % 2:
            push(int(k > 0))
        else:
            v = valuation2(3**max(-k, 0) - 5 * 3**max(k, 0))
            if d and valuation2(d) <= v:
                push(0)
            else:
                push(1)
                for _ in range(v - 1):
                    push(0)
    while d != 0:
        if d % 2 == 0:
            push(0)
        elif d == -3:
            for i in (1, 1, 0, 1, 0, 0, 0):
                push(i)
        else:
            u = valuation2((3 * d - 5) // 2)
            push(1)
            for _ in range(u + 1):
                push(0)
    require(k == d == 0, "control root")
    return tuple(word)


def fixed_row(q, e, p):
    P, B = 3**p, 2**e
    # x=G(q-beta), with 0<=beta<=1/2. Only x=1 mod 3 is selected.
    lo = ((2 * q - 1) * B + 2 * P - 1) // (2 * P)
    hi = q * B // P
    groups = defaultdict(list)
    for x in range(lo + (1 - lo) % 6, hi + 1, 6):
        w, y = path(x, e)
        if y != q or sum(w) != p:
            continue
        require(P * x + carry(w) == B * q and 2 * carry(w) <= B, "ordinary row")
        v, z = path(5 * x, e)
        groups[(z, sum(v) - p)].append(x)
    return groups


def validate_lifts(q, e, p, Y, k, xs):
    signed_d = 3**max(-k, 0) * Y - 5 * 3**max(k, 0) * q
    control = steer(k, signed_d)
    g = len(control)
    padding = g + (q + 1).bit_length() + 2
    sigma = control + (0,) * padding
    h, a, C = len(sigma), sum(sigma), carry(sigma)
    M = 3**a * q + C
    require(0 < M < 2**h, "subunit dyadic center")
    # Prescribe the odd sentinel and choose t=0 mod 3 so all starts stay units.
    mod = 2 ** (h + 1)
    t3 = (2**h - M) * pow(3 ** (p + a + 1), -1, mod) % mod
    t = 3 * t3
    numerator = M + 3 ** (p + a) * t
    require(numerator % (2**h) == 0, "target division")
    Q = numerator // (2**h)
    require(Q % 2 == 1 and Q % 3 and (2**h) * Q >= 3 ** (p + a + 1) + M,
            "small-center lift gap")
    require(Q != q or 2**h * q >= 3**p + q, "return clock")
    marks = Counter()
    seen = set()
    for x in xs:
        tstart = x + 2**e * t
        require(tstart not in seen and tstart % 6 == 1, "distinct unit start")
        seen.add(tstart)
        w, y = path(tstart, e + h)
        v, z = path(5 * tstart, e + h)
        require(w[:e] == path(x, e)[0] and v[:e] == path(5 * x, e)[0],
                "both frozen prefixes")
        require(w[e:] == sigma and y == Q and z == 5 * Q, "physical pair")
        require(sum(w) == sum(v) == p + a, "equal total odd counts")
        require(2 * carry(w) <= 2 ** (e + h) and carry(v) == 5 * carry(w),
                "bounded real first-arm offset and exact companion carry")
        count, finish = parse_marks(tstart, e + h)
        require(finish == Q and count >= 1, "complete parsing")
        marks[count] += 1
    return {"q": q, "p": p, "e": e, "Y": Y, "k": k,
            "inputs": len(seen), "control_clock": g, "new_clock": e + h,
            "new_odd_count": p + a, "center": str(Fraction(M, 2**h)),
            "ordinary_target": Q, "completed_blocks": dict(sorted(marks.items()))}


def check_late_edits():
    comparisons = 0
    for x in range(1, 100):
        for e in range(1, 8):
            w, y = path(x, e)
            P = 3**sum(w)
            for t in (0, 1, 2):
                z = x + t * 2**e
                wz, yy = path(z, e)
                require(wz == w and yy == y + P * t, "unconditional lift")
                for h in range(4):
                    _, r = path(yy, h)
                    if y < P and 2**h * r < y + P:
                        require(z == x and path(y, h)[1] == r, "short suffix")
                    comparisons += 1
    return comparisons


def main():
    repairs = []
    total_members = 0
    for q, p in ((1, 34), (5, 35), (7, 34), (11, 35)):
        e = 2 * p
        groups = fixed_row(q, e, p)
        require(groups, "empty finite sample")
        total_members += sum(map(len, groups.values()))
        candidates = sorted(((len(xs), Y, k) for (Y, k), xs in groups.items()
                             if (Y, k) != (5 * q, 0)), reverse=True)
        for _, Y, k in candidates[:2]:
            repairs.append(validate_lifts(q, e, p, Y, k, groups[(Y, k)]))
    for q, coalescence in ((1, 3), (5, 15)):
        require(not roots(q, coalescence), "root before coalescence")
        require(path(q, coalescence)[1] == path(5*q, coalescence)[1],
                "terminal coalescence")
    require(roots(49, 6) == [(6, 7)], "first mark example")
    return {"status": "PASS", "ordinary_row_members": total_members,
            "late_edit_comparisons": check_late_edits(),
            "terminal_coalescences": {"1": 3, "5": 15},
            "simultaneous_repair_examples": repairs}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
