"""Literal positive ordinary lifts for both synchronous rank sign-reversal words."""

from math import comb
import json


GADGETS = {
    3: ("2222 2244 1224 2424 2224 1122 2242 2222", (0, 0, -1, 0, 2, 2, 2, 0)),
    4: ("22222 24442 22221 42422 42222 22122 22222", (0, 0, -1, -2, 2, 2, 0)),
}


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def floor_clock(j):
    # 6*(1/6 + j*log_2(3)): compare exact powers for negative j as well.
    if j >= 0:
        return ((2 * 3**(6*j)).bit_length() - 1) // 6
    den = 3**(-6*j)
    s = den.bit_length() - 1
    # For j != 0, log_2(3^(-6*j)) is strictly between s and s+1.
    return -((-1 + s) // 6 + 1)


def forward_diffs(values):
    rows = [tuple(values)]
    while len(rows[-1]) > 1:
        row = rows[-1]
        rows.append(tuple(b - a for a, b in zip(row, row[1:])))
    return rows


def replay_ordinary(words, starts):
    rows = [tuple(starts)]
    for edge in words:
        moved = []
        for x, a in zip(rows[-1], edge):
            require(x > 0 and x % 2 == 1 and x % 3 != 0, "positive odd unit departure")
            numerator = 3*x + 1
            y, remainder = divmod(numerator, 1 << a)
            require(remainder == 0 and y % 2 == 1, "wrong native exponent")
            moved.append(y)
        rows.append(tuple(moved))
    return rows


def certificate(order, past, future):
    text, values = GADGETS[order]
    central = [tuple(map(int, row)) for row in text.split()]
    neutral = (2,) * (order+1)
    tags = [neutral] * past + central + [neutral] * future
    expected = [0] * past + list(values) + [0] * future
    dates = list(range(-past, len(values)+future))
    clocks = [floor_clock(j+1) - floor_clock(j) for j in dates]
    require(clocks[past:past+7] == [1,2,1,2,2,1,2][:len(clocks[past:past+7])], "calendar")
    for c,b in zip(tags, clocks):
        require(b in (1,2) and (b == 1 or 1 not in c), "grade cap")
    weights = [(-1)**(order-i)*comb(order,i) for i in range(order+1)]
    words = []
    for j, (c,d) in enumerate(zip(tags,tags[1:])):
        numerator = 3*expected[j] + sum(w*x for w,x in zip(weights,c))
        require(numerator == (1 << clocks[j])*expected[j+1], "signed carry")
        word = []
        for x,y in zip(c,d):
            scale, rem = divmod((1 << clocks[j])*y, x)
            require(rem == 0 and scale in (2,4), "native clock")
            word.append(scale.bit_length()-1)
        words.append(tuple(word))

    B = sum(clocks[:-1])
    raw = []
    for column in zip(*words):
        elapsed = C = 0
        for a in column:
            C = 3*C + 2**elapsed
            elapsed += a
        require(elapsed == B, "same column clock")
        raw.append(C)
    require(sum(w*x for w,x in zip(weights,raw)) == 0, "whole column carry")
    q2 = 2**(B+1)
    period = 3*q2
    inv3 = pow(3**len(words), -1, q2)
    rs = [inv3*(2**B - c) % q2 for c in raw]
    rs = [r + q2 * (((1-r) * pow(q2, -1, 3)) % 3) for r in rs]
    total = sum(w*x for w,x in zip(weights,rs))
    require(total % period == 0, "weighted source residues")
    rs[-1] -= total

    curvature = 1
    while True:
        # A large common intercept makes signed representatives positive and
        # influences none of the nonconstant spatial differences.
        intercept = 1 + abs(min(rs))
        starts = [r + period*(intercept + curvature*(1+i)**(order-1)) for i,r in enumerate(rs)]
        paths = replay_ordinary(words, starts)
        diffs = [forward_diffs([x*c for x,c in zip(row,cs)]) for row,cs in zip(paths,tags)]
        if all(all(x>0 for x in diff) for ds in diffs for diff in ds[1:order]):
            break
        curvature *= 2
    while True:
        starts = [r + period*(intercept + curvature*(1+i)**(order-1)) for i,r in enumerate(rs)]
        paths = replay_ordinary(words, starts)
        odd = [x for row in paths for x in row]
        if 3*max(odd) < 16*min(odd) and len(set(odd)) == len(odd):
            break
        intercept *= 2
    ds = [forward_diffs([x*c for x,c in zip(row,cs)]) for row,cs in zip(paths,tags)]
    require([d[-1][0] for d in ds] == expected, "literal difference sequence")
    require(all(all(x>0 for x in dd) for d in ds for dd in d[1:order]), "strict lower differences")
    require(all(x % 6 in (1,5) for x in odd), "all odd phases are ordinary units")
    out = {"order":order,"past_padding":past,"future_padding":future,
           "literal_odd_edges":len(words)*(order+1),"distinct_odd_states":len(set(odd)),
           "minimum_bits":min(odd).bit_length(),"maximum_bits":max(odd).bit_length(),
           "central_signed_differences":expected[past:past+len(values)],"all_lower_differences_positive":True,
           "strict_ratio_16_over_3":True}
    if past==future==0:
        out["source_tuple"] = starts
    return out


def main():
    return [certificate(order,past,future) for order in GADGETS
            for past,future in ((0,0),(4,9),(31,23),(128,128),(511,257))]


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
