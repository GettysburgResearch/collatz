"""Replay contraction or exact convergence on every supplied exponent class."""
from fractions import Fraction
from pathlib import Path
import json


def require(ok, context):
    if not ok:
        raise ValueError(context)


def prefix(center, targets):
    odds = 0
    for clock in range(700):
        if center in targets:
            return clock, odds, center
        odd = center.numerator % 2
        odds += odd
        center = ((3 * center + 1) if odd else center) / 2
    raise ValueError("No indicated terminal center")


def verify(row):
    d, t, e, m = (row[k] for k in ("depth", "index", "evens", "numerator"))
    den, p = 3**d, e + d
    period = 3**(d-4)
    j = 97 + 162*t
    require(d >= 5 and 0 <= t < period and m > 0, row)
    require((pow(2, j+p, 48*den)-m) % (48*den) == 17*den, row)
    require(j+p >= 4 and pow(2, 162*period, 3*den) == 1, row)
    require(j >= 97 and 2**97 > m, row)
    require(81*2**p < 1024*den and 2**97 > 527*den, row)
    lower = Fraction(-m, den)
    h, o, _ = prefix(lower, {-1})
    require(o >= d and h-o == e and j+p >= h, row)
    require(j >= o-d, row)
    # w ends at 3^(o-d) 2^(j-(o-d)) - 1, an actual early iterate of M_j.
    H, O, center = prefix(3*lower, {0, 1})
    require(O+1 >= d and j+p >= H, row)
    a = 3**(O+1-d)
    if center == 0:
        require(a == 1, row)
        return "power"
    slope = a * Fraction(2)**(p-H)
    pairs = 0
    while 2**40*81*slope >= 512:
        slope *= Fraction(3, 4)
        pairs += 1
    # Repeating 4x+1 -> 3x+1 consumes two powers of two on each pair.
    require(j+p-H >= 2*pairs and 512*2**97 > 2**40*81+527, row)
    return "contraction"


if __name__ == "__main__":
    rows = json.loads(Path(__file__).with_name("OppositeArmQueries.json").read_text())
    classes = {"power": set(), "contraction": set()}
    total = 3**10
    for row in rows:
        kind = verify(row)
        successors = set(range(row['index'], total, 3**(row['depth']-4)))
        require(all(not (s & successors) for s in classes.values()), "Overlapping exponent classes")
        classes[kind].update(successors)
    require(len(rows) == 214 and sum(map(len,classes.values()))==1000, "Incorrect census")
    print(f"{len(rows)} disjoint symbolic certificates; exponent classes modulo {total}:")
    print(f"{len(classes['power'])} power, {len(classes['contraction'])} positive-cycle contraction")
    print(f"{total-sum(map(len,classes.values()))} classes still outside this certificate")
