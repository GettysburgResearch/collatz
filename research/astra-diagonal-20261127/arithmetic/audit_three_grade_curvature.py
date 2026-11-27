"""Check the high-rank curvature cone by backward propagation of unsafe states."""

from functools import cache
from itertools import product
import json

DANGER = {(1,1,1), (1,2,1), (2,2,1), (3,1,2), (3,2,2), (4,2,2)}
NEGATIVE_DANGER = {(2,1,2), (4,2,2)}


def normal_step(n, letter):
    # Compute the two original 3x+1 transitions directly by following
    # the physical odd part and agreeing with the mechanical calendar.
    leading = n & -n
    if leading not in (1,2):
        return None
    x = n // leading
    folded = 2*n
    lowbit = 2*leading
    for m in ((2,) if letter == "S" else (2,1)):
        y = 3*x+1
        valuation = (y & -y).bit_length()-1
        if valuation not in (1,2):
            return None
        x = y >> valuation
        value = 3*folded + lowbit
        if value % (1 << m):
            return None
        folded = value >> m
        lowbit = folded & -folded
        if lowbit not in (1,2,4) or folded != lowbit*x:
            return None
    if lowbit == 1:
        return None
    return folded//2


@cache
def rows(word):
    scale = {"S": 4, "D": 8, "SD": 32, "DS": 32}[word]
    numer = {"S": 3, "D": 9, "SD": 27, "DS": 27}[word]
    row = set()
    for n in range(4*scale,8*scale):
        value = n
        midcarry = None
        for i, step in enumerate(word):
            value = normal_step(value,step)
            if value is None:
                break
            if i == 0 and len(word) == 2:
                mid = value if step == "D" else (3*value+(value&-value))//2
                midcarry = 8*mid-9*n
        if value is not None:
            row.add((n%4,value%4,scale*value-numer*n,midcarry))
    return tuple(sorted(row))


def delta(x):
    return x[0]-2*x[1]+x[2]


@cache
def run_step(state, words, sign):
    signed_height, a, b = state
    h = sign*signed_height
    ins = (a,b,(2*b-a+h)%4)
    scale = {"S":4,"D":8,"SD":32,"DS":32}[words[0]]
    numer = {"S":3,"D":9,"SD":27,"DS":27}[words[0]]
    options = [tuple(v for v in rows(w) if v[0]==r) for r,w in zip(ins,words)]
    out = set()
    for t in product(*options):
        w = numer*h+delta(tuple(v[2] for v in t))
        if w % scale:
            continue
        h2 = w//scale
        final = tuple(v[1] for v in t)
        if (delta(final)-h2)%4:
            continue
        if len(words[0])==2:
            mw = 9*h+delta(tuple(v[3] for v in t))
            assert mw%8==0
            if sign*mw<=0:
                out.add(None)
                continue
        out.add((sign*h2,final[0],final[1]) if sign*h2>0 else None)
    return frozenset(out)


def backwards(words, sign=1):
    # At the terminal single-return boundary only the supplied small
    # signed states are unsafe. Losing the strict sign is always unsafe.
    danger = DANGER if sign==1 else NEGATIVE_DANGER
    unsafe = set(danger)
    sizes = []
    for spec in reversed(words):
        max_bad = max((h for h,_,_ in unsafe),default=0)
        # H_out >= 3H/4-4, including the seam midpoint. To reach
        # H_out<=max_bad or a nonpositive midpoint requires this bound.
        search_max = 4*(max_bad+4)//3
        source = set()
        for h in range(1,search_max+1):
            for a,b in product((1,2,3),repeat=2):
                if (2*b-a+sign*h)%4==0:
                    continue
                candidate = (h,a,b)
                possible = run_step(candidate,spec,sign)
                if None in possible or not unsafe.isdisjoint(possible):
                    source.add(candidate)
        unsafe = source
        sizes.append(dict(count=len(unsafe),max_h=max((s[0] for s in unsafe),default=0)))
    assert unsafe <= danger, (words,unsafe-danger)
    return dict(reverse_steps=sizes, initial_unsafe=sorted(unsafe))


def main():
    S,D=("S",)*3,("D",)*3
    branches = {"SDD": (S,D,D), "SDDD": (S,D,D,D),
                "left": (S,D,D,("DS","DS","SD"),D,D),
                "right": (S,D,D,("DS","SD","SD"),D,D)}
    result = {k: backwards(v) for k,v in branches.items()}
    negative = {k: backwards(v,-1) for k,v in branches.items()}
    print(json.dumps(dict(row_tables={w:rows(w) for w in ("S","D","SD","DS")},
                          blocks=result,negative_blocks=negative),indent=2))


if __name__=="__main__":
    main()
