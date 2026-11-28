"""Bounded exact census of all median cutoffs, with scalar and affine-block replays."""
import argparse
import json
import math
from fractions import Fraction

import numpy as np


def first_cutoff(t):
    # H_X >= t exactly when 4**t <= X**2 * 3**t.
    num, den = 4**t, 3**t
    x = math.isqrt((num - 1) // den) + 1
    if not (x-1)**2 * den < num <= x*x * den:
        raise ArithmeticError("inexact cutoff")
    return x


def step(n):
    return (3*n+1)//2 if n % 2 else n//2


def scalar_one(n, cap):
    for t in range(cap):
        if n == 1:
            return t
        n = step(n)
    return cap


def block_map(width):
    residues = np.arange(1 << width, dtype=np.uint64)
    cost = np.ones_like(residues)
    image = residues.copy()
    for _ in range(width):
        odd = image % 2 != 0
        cost[odd] *= 3
        image[odd] = 3*image[odd] + 1
        image >>= 1
    return cost, image


def capped_times(lo, hi, cache, cap, width, factor, image):
    # The cache contains the exact capped first times at 1 for all starts < lo.
    values = np.arange(lo, hi+1, dtype=np.uint64)
    active = np.arange(len(values))
    result = np.full(len(values), cap, dtype=np.uint8)
    clock = 0
    mask = (1 << width) - 1
    max_high = (2**64 - 1 - int(image.max())) // int(factor.max())
    while len(active) and clock < cap:
        quot = values >> width
        danger = quot > max_high
        if danger.any():
            for idx, val in zip(active[danger], values[danger]):
                result[idx] = clock + scalar_one(int(val), cap-clock)
            active, values, quot = active[~danger], values[~danger], quot[~danger]
        rem = values & mask
        values = quot * factor[rem] + image[rem]
        clock += width
        # All starting values for a jump are >= lo > 2**width. They
        # cannot have visited 1 before or at the last date of that jump.
        resolved = values < lo
        if clock < cap and resolved.any():
            result[active[resolved]] = np.minimum(
                cap, clock + cache[values[resolved]].astype(np.uint16))
        active, values = active[~resolved], values[~resolved]
    return result


def census(limit, width=12, block=1 << 17, emit=None, min_ratio=False, gate=False):
    if not (1 <= limit <= 1 << 34 and 1 <= width <= 16 and block > 0):
        raise ValueError("invalid census parameters")
    cuts = [1]
    while cuts[-1] <= limit:
        cuts.append(first_cutoff(len(cuts)))
    hmax = len(cuts) - 2
    cap = hmax + 2
    if cap > 255:
        raise ValueError("capped first-hit time exceeds byte range")
    warm = min(limit, max(1 << width, 1 << 13))
    cache = np.empty(limit + 1, dtype=np.uint8)
    cache[0] = cap
    for n in range(1, warm+1):
        cache[n] = scalar_one(n, cap)
    factor, image = block_map(width)
    hist = np.zeros(cap+1, dtype=np.int64)
    rows = []
    h = 0
    lo = 1
    worst_x = worst_count = worst_slack = 0
    ratio_x = ratio_count = 0
    while lo <= limit:
        if lo <= warm:
            hi = warm
        else:
            hi = min(limit, lo+block-1)
            cache[lo:hi+1] = capped_times(lo, hi, cache, cap, width, factor, image)
        a = lo
        while a <= hi:
            while cuts[h+1] <= a:
                h += 1
            octave_end = 1 if a == 1 else 1 << (a-1).bit_length()
            end = min(hi, cuts[h+1]-1, octave_end)
            times = cache[a:end+1]
            # Except at n=1 (already active), first entry at 2 is one date before 1.
            old = int(hist[:h+2].sum())
            counts = old + np.cumsum(times <= h+1, dtype=np.int64)
            xs = np.arange(a, end+1, dtype=np.int64)
            slack = 5*counts-3*xs
            i = int(slack.argmin())
            if not worst_x or slack[i] < worst_slack:
                worst_x, worst_count, worst_slack = a+i, int(counts[i]), int(slack[i])
            if min_ratio:
                # First bound every ratio using its fifths slack and an extremal
                # denominator. Only a segment able to improve the record needs
                # exact comparisons. Signed int64 accommodates 2**25 * 2**34.
                peak = end if slack[i] >= 0 else a
                lower_num = 3*peak + int(slack[i])
                if not ratio_x or lower_num*ratio_x < 5*peak*ratio_count:
                    bins = (counts << 25) // xs
                    for k in np.flatnonzero(bins == bins.min()):
                        x, c = a+int(k), int(counts[k])
                        if not ratio_x or c*ratio_x < ratio_count*x:
                            ratio_x, ratio_count = x, c
            hist += np.bincount(times, minlength=cap+1)
            if end == octave_end or end == limit:
                row = dict(end=end, deadline=h, count=int(counts[-1]),
                           min_fifths=worst_slack, min_at=worst_x, min_count=worst_count)
                if gate:
                    row["gate_tie_squares"] = sum(int(c)**2 for c in hist[2:h+2])
                if min_ratio:
                    row.update(ratio_at=ratio_x, ratio_count=ratio_count)
                    ratio_x = ratio_count = 0
                rows.append(row)
                if emit:
                    emit(row)
                worst_x = 0
            a = end+1
        lo = hi+1
    if int(hist.sum()) != limit:
        raise ArithmeticError("population size mismatch")
    return rows


def direct(limit, min_ratio=False, gate=False):
    # Independent scalar first entry at {1,2} and an exact updated deadline.
    # Its histogram is rebuilt into a count at every single cutoff.
    hmax = 5*limit.bit_length()+1
    rows = []
    first_entry_counts = [0]*(hmax+2)
    h, best = 0, None
    ratio_x = ratio_count = 0
    for n in range(1, limit+1):
        while 4**(h+1) <= 3**(h+1)*n*n:
            h += 1
        y = n
        for t in range(hmax+1):
            if y in (1, 2):
                break
            y = step(y)
        else:
            t = hmax+1
        first_entry_counts[t] += 1
        count = sum(first_entry_counts[:h+1])
        candidate = (5*count-3*n, n, count)
        if best is None or candidate < best:
            best = candidate
        if min_ratio and (not ratio_x or count*ratio_x < ratio_count*n):
            ratio_x, ratio_count = n, count
        if n & (n-1) == 0 or n == limit:
            row = dict(end=n, deadline=h, count=count, min_fifths=best[0],
                       min_at=best[1], min_count=best[2])
            if min_ratio:
                row.update(ratio_at=ratio_x, ratio_count=ratio_count)
                ratio_x = ratio_count = 0
            if gate:
                row["gate_tie_squares"] = sum(c*c for c in first_entry_counts[1:h+1])
            rows.append(row)
            best = None
    return rows


def verify_receipt(path):
    with open(path, encoding="utf-8") as source:
        rows = [json.loads(line) for line in source]
    if [r["end"] for r in rows] != [1 << k for k in range(34)]:
        raise ArithmeticError("missing dyadic octave")
    for row in rows:
        e = row["end"]
        if not (e//2 < row["min_at"] <= e and
                5*row["min_count"]-3*row["min_at"] == row["min_fifths"] > 0):
            raise ArithmeticError(f"invalid fifths witness at {e}")
        if not (e//2 < row["ratio_at"] <= e and
                5*row["ratio_count"] > 3*row["ratio_at"]):
            raise ArithmeticError(f"invalid ratio witness at {e}")
        if 128 <= e <= 1 << 32:
            # On this octave F >= (3e+slack)/(5e), X > e/2.
            # At most the full octave's tie cost and two initial diagonals
            # are subtracted from F**2/2 in the first-meeting identity.
            numerator = (3*e+row["min_fifths"])**2 - 200*(2+row["gate_tie_squares"])
            if numerator <= 7*e**2:
                raise ArithmeticError(f"uncertified 7/50 gate bound at {e}")
    for x in range(1, 65):
        h = 0
        while 4**(h+1) <= 3**(h+1)*x*x:
            h += 1
        states = list(range(1, x+1))
        gates = 0
        for _ in range(h):
            gates += 2*states.count(1)*states.count(4)
            states = [step(n) for n in states]
        if (50*gates > 7*x*x) != (x >= 3):
            raise ArithmeticError(f"direct first-meeting check at {x}")
    worst = min(rows, key=lambda r: Fraction(r["ratio_count"], r["ratio_at"]))
    print(f"Verified receipt. Lowest fraction {worst['ratio_count']}/{worst['ratio_at']}. "
          "Ordered first-meeting probability exceeds 7/50 for 3 through 2^32.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1 << 20)
    parser.add_argument("--width", type=int, default=12)
    parser.add_argument("--block", type=int, default=1 << 17)
    parser.add_argument("--gate", action="store_true", help="record the gate tie square total at each octave end")
    parser.add_argument("--min-ratio", action="store_true", help="also find the exact worst fraction in each octave")
    parser.add_argument("--verify-receipt", metavar="FILE", help="check the inequalities in the saved two-run receipt")
    args = parser.parse_args()
    for n in (1, 7, 32, 287, 1024, 20_003):
        if census(n, 4, 37, min_ratio=True, gate=True) != direct(n, min_ratio=True, gate=True):
            raise ArithmeticError(f"independent direct check failed at {n}")
    if args.verify_receipt:
        verify_receipt(args.verify_receipt)
        return
    rows = census(args.limit, args.width, args.block,
                  emit=lambda row: print(json.dumps(row), flush=True), min_ratio=args.min_ratio, gate=args.gate)
    if any(row["min_fifths"] < 0 for row in rows):
        raise ArithmeticError("a finite cutoff is below three fifths")


if __name__ == "__main__":
    main()
