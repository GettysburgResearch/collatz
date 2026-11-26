"""Independent finite checks of the fixed-tower clock and reflection bounds."""
from collections import defaultdict
import json
from math import gcd


def check(ok, message):
    if not ok:
        raise ValueError(message)


def orbit(start, horizon):
    x, p = start, 0
    rows = []
    for _ in range(horizon + 1):
        rows.append((x, p))
        if x % 2:
            p += 1
            x = (3*x + 1) // 2
        else:
            x //= 2
    return rows


def reflection():
    comparisons = meetings = 0
    for H in range(3, 8):
        period = 2**(H - 2)
        r = period
        while 3**r <= 1 + 3*4**H:
            r += period
        for z in range(1, 97):
            lower, upper = orbit(z, H), orbit(3*z, H)
            high_l, high_u = orbit(3**r*z, H), orbit(3**(r+1)*z, H)
            for i, (x, p) in enumerate(lower):
                for j, (y, q) in enumerate(upper):
                    met = high_l[i][0] == high_u[j][0]
                    reflected = i == j and x == y and p == q+1
                    check(met == reflected, ("reflection", H, r, z, i, j))
                    comparisons += 1
                    meetings += int(met)
    check(meetings > 0, "no reflected meetings exercised")
    return dict(clock_pairs=comparisons, meetings=meetings)


def cone():
    earlier = defaultdict(list)
    matches = high_grade = 0
    for z in range(1, 130):
        if gcd(z, 6) == 1:
            for r in range(17):
                for i, (y, p) in enumerate(orbit(3**r*z, 21)):
                    for w, s, j, q in earlier[y]:
                        H = max(i, j)
                        matches += 1
                        check(3**(r+p) < 6**H, ("cone", z, w, r, s, i, j))
                        if H <= r+p:
                            check(3**(r+p+1) < 6**H, "stronger high bound")
                            high_grade += 1
                            check(q+s < H and j < i and 3**(r+p) < 2**(i-j)*3**(s+q),
                                  ("orientation", z, w, r, s, i, j))
        for s in range(17):
            for j, (y, q) in enumerate(orbit(3**s*z, 21)):
                earlier[y].append((z, s, j, q))
    check(high_grade > 0, "orientation was vacuous")
    x, p = orbit(3**3*257, 13)[13]
    y, q = orbit(3**8*244, 5)[5]
    check(x == y == 150083 and 3+p == 14 and 8+q == 9, "asynchronous control")
    return dict(matches=matches, high_grade=high_grade, asynchronous_control_endpoint=x)


def delayed(H):
    period = 2**(H-2)
    modulus = 2**H
    v = (pow(3, period, 32*modulus)-1)//modulus
    (x, p), (y, q) = orbit(17, H)[-1], orbit(51, H)[-1]
    check(x == y == 1 and p == q, "control phase")
    b = 17*pow(3, p, 32)*v % 32
    u = 5*pow(b, -1, 32) % 32
    r = period*u
    lift = 3**r
    check(lift > 1+3*modulus**2 and (lift-1) % modulus == 0, "reflection hypotheses")
    check((17*3**p*((lift-1)//modulus))%32 == 5, "suffix digit")
    lower, upper = orbit(17*lift, H+5), orbit(51*lift, H+5)
    first = min(max(i, j) for i,(a,_) in enumerate(lower)
                for j,(b,_) in enumerate(upper) if a == b)
    check(first == H+5 and lower[-1][0] == upper[-1][0], "delayed meeting")
    return dict(horizon=H, rank=r, first_asynchronous_deadline=first,
                verified_common_clock=H+5)


def main():
    check(3**2252 < 6**1381 <= 3**2253, "block threshold")
    report = dict(reflection=reflection(), lower_cone=cone(),
                  late_mergers=[delayed(17), delayed(19)], threshold_grade=2253)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
