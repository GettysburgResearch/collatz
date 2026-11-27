"""Exact finite checks for first-passage enclosures, selected pairs, and charge."""
from collections import defaultdict
from fractions import Fraction
from json import dumps


def require(test, message):
    if not test:
        raise ValueError(message)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def prefix(x, h):
    p = 0
    for _ in range(h):
        p += x % 2
        x = step(x)
    return x, p


def first_hit(n, limit=20000):
    x = n
    for h in range(limit + 1):
        if x == 1:
            _, p = prefix(n, h)
            return h, p, h - 2 * p
        x = step(x)
    raise ValueError(("first hit not found in the stated finite budget", n, limit))


def passage(n, cut, deadline):
    x, grade, l, best = n, 0, Fraction(1), Fraction(1)
    for h in range(deadline + 1):
        if l <= best:
            residual = x - l * n
            require(0 <= residual <= Fraction(h, 2), ("record residual", n, h))
            best = l
        if l <= cut:
            require(cut / 2 < l and l == best, ("first overshoot", n, cut))
            return x, h, grade, l
        odd = x % 2
        x = step(x)
        grade += odd
        l *= Fraction(3**odd, 2)
    return None


def check_interval(lo, width, deadline, denominator):
    cut = Fraction(1, denominator)
    lower_miss = upper_miss = stopped = replayed = 0
    starts = range(lo + (17 - lo) % 48, lo + width, 48)
    fibers = defaultdict(list)
    for z in starts:
        low, high = passage(z, cut, deadline), passage(3 * z, cut, deadline)
        lower_miss += low is None
        upper_miss += high is None
        if low is None or high is None:
            continue
        u, h, p, l = low
        v, k, q, m = high
        stopped += 1
        require(abs(l * v - 3 * m * u) <= (l * k + 3 * m * h) / 2,
                ("joint strip", z, h, k))
        key = (u, h, p, v, k, q)
        if fibers[key]:
            y = fibers[key][0]
            require(y < z and y % 48 == 17, ("smaller canonical parent", y, z))
            require(z - y <= Fraction(h, 2) / l, ("partner distance", y, z))
            require(prefix(y, deadline) == prefix(z, deadline), ("lower meeting", y, z))
            require(prefix(3 * y, deadline) == prefix(3 * z, deadline),
                    ("upper meeting", y, z))
            replayed += 1
        fibers[key].append(z)
    require(stopped == len(fibers) + replayed, "partition")
    return {"start": str(lo), "width": width, "canonical_sources": len(starts),
            "deadline": deadline, "coefficient_cut_denominator": denominator,
            "lower_missed_cut": lower_miss, "upper_missed_cut": upper_miss,
            "both_stopped": stopped, "distinct_stopped_signatures": len(fibers),
            "replayed_smaller_partners": replayed,
            "largest_stopped_fiber": max(map(len, fibers.values()), default=0)}


def check_strip(lo, slope, intercept, width, deadline, denominator):
    """Use nonintegral slopes/intercepts, including multiple pairs per coordinate."""
    cut = Fraction(1, denominator)
    groups = defaultdict(list)
    total = stopped = 0
    for x in range(lo, lo + width):
        center = slope * x + intercept
        for y in range(max(1, center.__floor__() - 1), center.__floor__() + 2):
            if abs(y - center) > 1:
                continue
            total += 1
            first = passage(x, cut, deadline)
            second = passage(y, cut / slope, deadline)
            if first is None or second is None:
                continue
            u, h, p, l = first
            v, k, q, m = second
            a = slope * m / l
            delta = v - a * u - m * intercept
            require(Fraction(1, 2) < a < 2, ("normalized slope", slope, a))
            require(abs(delta) <= 2 + Fraction(3 * deadline, 2), "recursive thickness")
            t = delta.__floor__()
            key = (h, p, k, q, t)
            groups[key].append((u, v))
            require(abs(v - a * u - (m * intercept + t)) <= 1, "unit strip")
            stopped += 1
    for (h, p, k, q, t), group in groups.items():
        xcoords = [u for u, _ in group]
        require(max(xcoords) - min(xcoords) <= cut * width + Fraction(deadline, 2),
                ("image interval", h, p, k, q, t))
    return {"source_pairs": total, "both_stopped": stopped, "output_pieces": len(groups)}


def main():
    charges = {str(x): first_hit(x) for x in (17, 51, 65, 195)}
    require(charges == {"17": (9, 3, 3), "51": (17, 7, 3),
                        "65": (19, 8, 3), "195": (76, 43, -10)}, "charge control")
    examples = [check_interval(lo, 1 << 16, 150, 8192)
                for lo in (1, 10**6 + 11, 2**120 + 37, 3**130 + 81)]
    require(all(row["replayed_smaller_partners"] > 0 for row in examples), "empty replay row")
    strip_rows = [check_strip(2**100 + 5, a, b, 600, 28, 5)
                  for a, b in ((Fraction(1, 2), Fraction(5, 7)),
                               (Fraction(18, 13), Fraction(-53, 4)),
                               (Fraction(3), Fraction(35, 9)))]
    print(dumps({"ordinary_charge_controls": charges, "translated_intervals": examples,
                 "recursive_strip_controls": strip_rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
