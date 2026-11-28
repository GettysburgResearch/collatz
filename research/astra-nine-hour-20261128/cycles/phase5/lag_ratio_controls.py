"""Check endpoint-ratio clock rigidity and a minimal product without closure."""

from fractions import Fraction
from itertools import combinations
from math import prod
from pathlib import Path
from runpy import run_path

base = run_path(str(Path(__file__).resolve().parents[1] / 'phase2' / 'semigroup_controls.py'))
numerator, need = base['physical_numerator'], base['need']


def closer(h, gap, sides):
    """Test ||h log_2(3)|| < log_2(gap), optionally from above only."""
    a = 3**h
    j = a.bit_length()
    return Fraction(2**j, a) < gap or (sides == 2 and Fraction(a, 2**(j-1)) < gap)


def test_word(w):
    n,u = len(w), sum(w)
    s = [i for i,b in enumerate(w) if b]
    y = [numerator(w[i:]+w[:i]) for i in s]
    gap = Fraction(2**n,3**u)
    two_sided = gap < 2 and not any(closer(h,gap,2) for h in range(1,u))
    one_sided = not any(closer(h,gap,1) for h in range(1,u))
    previous = {}
    for i in range(u):
        for h in range(1,u):
            j = (i+h)%u
            r = Fraction(y[j],y[i])
            a = (s[j]-s[i])%n
            error = 2**a*r/3**h
            need(1 < error < gap, 'ratio error in positive open interval')
            for H,A in previous.get(r,set()):
                if H != h:
                    need(closer(abs(H-h),gap,2), 'spacing for a repeated reduced ratio')
                if two_sided:
                    need((h,a)==(H,A), 'both clocks of repeated ratio')
            previous.setdefault(r,set()).add((h,a))
    if one_sided:
        for size in range(1,u):
            for I in combinations(range(u),size):
                need(prod(y[i] for i in I) != prod(y[(i+1)%u] for i in I), 'record subset product')
    return int(two_sided), int(one_sided), sum(len(lags)>1 for lags in previous.values())


def main():
    words = one = two = collisions = 0
    for n in range(3,16):
        for u in range(2,n):
            if 2**n <= 3**u:
                continue
            for ones in combinations(range(n),u):
                bits = set(ones)
                w = tuple(int(i in bits) for i in range(n))
                rotations = [w[i:]+w[:i] for i in range(n)]
                if w != min(rotations) or len(set(rotations)) !=n:
                    continue
                b,a,c = test_word(w)
                two += b
                one += a
                collisions += c
                words += 1
    src = [25,19,29,43,143]
    tgt = [19,29,11,65,215]
    exp = [2,1,3,1,1]
    need(all(3*x+1==2**a*y for x,y,a in zip(src,tgt,exp)),'five native odd steps')
    need(prod(src)==prod(tgt) and set(src)!=set(tgt),'fake balanced product')
    for j in range(1,5):
        for I in combinations(range(5),j):
            need(prod(src[i] for i in I)!=prod(tgt[i] for i in I),'minimal fake product')
    print(f'{words} positive primitive necklaces through n=15 passed all-lag tests.')
    print(f'{two} two-sided best clocks; {one} one-sided best clocks passed every proper edge subset.')
    print(f'{collisions} ratio classes had multiple (lag,time) pairs across the tested necklaces.')
    print('Five exact odd edges at (8,5) form a minimal balanced product but no orbit.')


if __name__ == '__main__':
    main()
