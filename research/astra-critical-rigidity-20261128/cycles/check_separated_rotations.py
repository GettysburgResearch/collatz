"""Exact paired-lap, common-carry and translated-product controls."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, prod
import json

from check_rotation_occupation import lifted, primitive_necklace, require


def order(z, prime):
    value = Fraction(z)
    def integral(n):
        out = 0
        while n % prime == 0:
            n //= prime
            out += 1
        return out
    return integral(abs(value.numerator)) - integral(value.denominator)


def outside(z):
    return abs(z) * Fraction(2) ** -order(z, 2) * Fraction(3) ** -order(z, 3)


def verify(w, q, y, lag, start, do_translate, stats):
    p, A = len(w), sum(w)
    root = [y[start], y[(start+lag) % p]]
    exp = [[w[(start+a+i) % p] for i in range(p)] for a in (0,lag)]
    dates = sorted({0,p} | {i+1 for i in range(p) if exp[0][i] != exp[1][i]})
    X = Fraction(2**A, 3**p)
    weighted, multipliers, carries, powers = [], [], [], []
    for u,t in zip(dates, dates[1:]):
        L, clock = t-u, 0
        C = 0
        for i in range(u,t):
            C = 3*C + 2**clock
            clock += min(exp[0][i],exp[1][i])
        B = clock
        C1 = 0
        e1 = 0
        for a in exp[1][u:t]:
            C1 = 3*C1 + 2**e1
            e1 += a
        require(C1 == C and gcd(C,6) == 1, "same actual ternary-unit carry")
        require(C <= 2**(B-L)*3**L, "complete common-carry height")
        a0,a1 = sum(exp[0][:u]),sum(exp[1][:u])
        z = Fraction(q*C*2**a0,3**t)
        v = Fraction(2)**(a1-a0)
        require(order(z,3)==-t, "exact ternary endpoint")
        for j,ray in enumerate((start,start+lag)):
            departure = y[(ray+u)%p]
            arrival = y[(ray+t)%p]
            require(2**sum(exp[j][u:t])*arrival == 3**L*departure+q*C,
                    "correct terminal excess on actual endpoint")
        weighted.append(z)
        multipliers.append(v)
        powers.append(a1-a0)
        carries.append(C)
        stats["shared_blocks"] += 1
        stats["unequal_last_divisions"] += exp[0][t-1] != exp[1][t-1]
    require(root[0]+sum(weighted) == X*root[0], "first full lap")
    require(root[1]+sum(z*v for z,v in zip(weighted,multipliers)) == X*root[1],
            "second full lap")
    require(prod(carries) <= 2**(A-p)*3**p, "total common-carry height")
    require(multipliers[0]==1 and root[0]!=root[1], "root exclusion")
    stats["paired_full_laps"] += 1
    stats["interior_artificial_cuts"] += exp[0][-1]==exp[1][-1]
    if not do_translate:
        return
    # T=4 and c=1 or 2 exercise fixed rational coefficients and negative powers.
    D = 3
    T = Fraction(4)
    box = range(D)
    shifts,coeffs = zip(*(divmod(a,2) for a in powers))
    enlarged = [set(box) | {u+h for u in box} for h in shifts]
    product_of_forms = Fraction(1)
    for u in box:
        for j in (0,1):
            old = root[j]*T**u
            if j==0:
                left = old + sum(z*T**u for z in weighted)
            else:
                left = old + sum(2**c*z*T**(u+h)
                                 for z,h,c in zip(weighted,shifts,coeffs))
            require(left==X*old, "translated source form at two")
            product_of_forms *= abs(old)*Fraction(2)**-order(left,2)*Fraction(3)**-order(old,3)
    for z,rows in zip(weighted,enlarged):
        product_of_forms *= prod(outside(z*T**u) for u in rows)
    target = Fraction(1,2**(2*A*D)) * (outside(root[0])*outside(root[1]))**D
    target *= prod((q*C)**len(rows) for C,rows in zip(carries,enlarged))
    require(product_of_forms == target, "exact three-place translate product")
    stats["translated_products"] += 1
    stats["overlapping_carry_boxes"] += sum(len(a)<2*D for a in enlarged)
    stats["negative_translation_exponents"] += sum(a<0 for a in shifts)


def main():
    stats = Counter()
    def process(w):
        realizer = lifted(w)
        if realizer is None:
            return
        q,y = realizer
        p = len(w)
        stats["primitive_cycles"] += 1
        stats["nontrivial_proper_cancellations"] += 1<q<2**sum(w)-3**p
        for lag in range(1,p):
            for start in sorted({0,p//2,y.index(min(y)),y.index(max(y))}):
                verify(w,q,y,lag,start,lag==1 and start==y.index(min(y)),stats)
    for p in range(2,7):
        for w in product((1,2,3), repeat=p):
            if primitive_necklace(w):
                process(w)
    for w in ((1,2,1,3,1,2,1,12),(2,1,3,2,1,3,2,1,29),
              (1,1,2,2,1,2,1,1,2,2,1,51),(1,2,1,3,2,61,1,3,1,2)):
        process(w)
    require(all(stats.values()) and len(stats)==9, "all native and translated controls")
    return dict(stats)


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
