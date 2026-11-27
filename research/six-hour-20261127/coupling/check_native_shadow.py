"""Complete finite positive and reflected lookups for the near-native rank theorem."""
import json
from collections import defaultdict
from fractions import Fraction


def require(ok, label):
    if not ok:
        raise ArithmeticError(label)


def v2(x):
    return (x & -x).bit_length()-1


def v3(x):
    d = 0
    while x % 3 == 0:
        x //= 3
        d += 1
    return d


def step(x):
    u = 3*x+1
    e = v2(u)
    return u >> e, e


def profile(w, n):
    total = 0
    for _ in range(n):
        w, e = step(w)
        total += e
    return w, total


def lookup():
    reach = defaultdict(list)
    for w in range(1, 933, 2):
        x, q, d = w, 0, 0
        seen = set()
        while x not in seen:
            seen.add(x)
            reach[x].append((w, q, d))
            x, e = step(x)
            q += 1
            d += e
            require(q <= 250, "finite forward horizon")
        require(x == 1, "full odd orbit at a repeat")
    high = max(reach)
    bands = []
    for l in range(1, 8):
        hits = sorted(x for x in reach if (589 << l) <= x < (590 << l))
        bands.append({"ell": l, "hits": hits})
    require(high == 83501 and (589 << 8) > high, "all higher bands excluded")
    require([b["hits"] for b in bands] == [[], [], [], [], [18863], [], []],
            "only positive off-center intersection")
    a = (590 << 5)-18863
    cycle = []
    x = a
    while x not in cycle:
        cycle.append(x)
        u = 3*x-1
        x = u >> v2(u)
        require(len(cycle) <= 10, "reflected finite period")
    require(a == 17 and x == a and 1 not in cycle, "off-center point excluded")
    forms = []
    for w, q, d in sorted(reach[589]):
        slope = Fraction(2**d, 3**q)
        offset = 590*slope-w
        require(slope <= Fraction(128, 81) and w <= 929, "height for every lift")
        residue = (-offset.numerator*pow(offset.denominator, -1, 16)) % 16
        forms.append({"anchor_start": w, "odd_rank": q, "divisions": d,
                      "slope": [slope.numerator, slope.denominator],
                      "subtracted": [offset.numerator, offset.denominator], "mod_16": residue})
    require([item["anchor_start"] for item in forms] == [523, 589, 619, 697, 785, 825, 929],
            "complete fixed-anchor visitors")
    require([item["anchor_start"] for item in forms if item["mod_16"] == 1] == [929],
            "only original parent can be canonical")
    return high, bands, cycle, forms


def control(m, forms, exhaustive=False):
    N = 2**m
    M = N-1
    H = v2(3**(m+1)-1)
    U = (3**(m+1)-1) >> H
    R = v3(N-590)
    z = (128*N-271)//81
    require(81*z+271 == 128*N and H == 2+v2(m+1), "ordinary normalization")
    rows = [(3*(N//2)-1, m, m+H-1)]
    for item in forms:
        w, q, d = (item[key] for key in ("anchor_start", "odd_rank", "divisions"))
        if q > R:
            continue
        y = w+2**d*((N-590)//3**q)
        require(profile(y, q) == (M, d), "ordinary lifted anchor start")
        rows.append((y, m+1+q, m+H+d))
    for y, q, d in rows:
        require(0 < y <= z and profile(y, q) == (U, d), "all full odds to original U")
        require(2*y > z and (y == z or y % 48 != 17), "height and residue")
    if exhaustive:
        hits = []
        for y in range(1, z+1):
            x = y
            while x % 2 == 0:
                x //= 2
            for q in range(m+2+R):
                if x == U:
                    hits.append((y, q))
                x, _ = step(x)
        require(sorted(hits) == sorted((y, q) for y, q, _ in rows), "every ordinary source and clock")
    return {"m": m, "H": H, "R": R, "visitors": len(rows), "maximum_odd_rank": m+1+R,
            "exhaustive_starts": z if exhaustive else 0,
            "small_start_grade_pairs": sorted([y, q] for y, q, _ in rows) if exhaustive else []}


def main():
    high, bands, cycle, forms = lookup()
    require(15**7 > 8*11**7 and 3**5 < 2**8 and 3**2 > 2**3, "spectral integer comparisons")
    small = [control(m, forms, m == 11) for m in [11, 173, 335, 497, 659]]
    # All m>=659 satisfy m>=50*(2+floor(log2(m+1)))+35.
    # On 659..1022 test the left endpoint; at the next binary thresholds
    # the left side increases by at least 1024 while the right increases by 50.
    require(659 >= 50*(2+9)+35 and 1023 >= 50*(2+10)+35, "large progression threshold")
    for row in small[1:]:
        m, H, R = (row[key] for key in ("m", "H", "R"))
        require(m >= 50*H+35 or (5*3*(m-H) >= 7*(5*H+5+3*R)),
                "long-tail exclusion at small hard exponents")
        require(3*(m-3*H) >= 7*H and m >= H+2, "native exclusion at small hard exponents")
    print(json.dumps({"positive_start_cutoff": 932, "maximum_odd_visited": high,
                      "higher_bands": bands, "reflected_cycle": cycle,
                      "positive_589_forms": forms, "ordinary_controls": small}, indent=2))


if __name__ == "__main__":
    main()
