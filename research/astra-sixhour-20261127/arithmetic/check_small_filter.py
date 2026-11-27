"""Exact signed and positive binary-division filters on actual cyclic rank arrays."""
from fractions import Fraction
from math import gcd
import json


def require(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def lowbit(q):
    require(q > 0 and q.denominator % 2 == 1, "positive integral 2-adic rational")
    return q.numerator & -q.numerator


def rank_array(word):
    p, h = len(word), sum(word)
    require(gcd(p, h) == 1, "this rank fixture requires coprime clocks")
    c0, pos = 0, 0
    for e in word:
        c0, pos = 3*c0 + (1 << pos), pos + e
    x = Fraction(c0, (1 << h) - 3**p)
    s = x
    values = [None]*p
    for j, e in enumerate(word):
        require(x >= s, "fixture must be rooted at minimum")
        k = 0
        while x >= (2 << k)*s:
            k += 1
        require(k <= 2, "fixture height")
        values[j*h % p] = (4 >> k)*x
        x = (3*x+1)/(1 << e)
    require(x == s and values == sorted(values), "physical rank order")
    return values


def extend(values, index):
    shift, r = divmod(index, len(values))
    return values[r]*(1 << shift)


def filter_digits(p, h, length, positive):
    ms = [j*h//p for j in range(length+1)]
    numerator = 1
    coeff = []
    for j in range(length):
        power = 1 << (ms[-1] - ms[j])
        residue = numerator * pow(power, -1, 3) % 3
        # Choose in the required class at or below g, or nearest to g.
        ceilshift = 0 if positive else 3*power//2
        b = residue + 3*((numerator-residue*power+ceilshift)//(3*power))
        coeff.append(b)
        numerator = (numerator - b*power)//3
    coeff.append(numerator)
    bits = sum(b*(1 << (ms[-1]-m))*3**j for j, (b,m) in enumerate(zip(coeff,ms)))
    require(bits == 1, "unit coefficient identity")
    require(max(map(abs,coeff)) <= (6 if positive else 3), "digit magnitude")
    return [j*h-m*p for j,m in enumerate(ms)], coeff, ms[-1]


def audit(word, length, positive):
    p, h = len(word), sum(word)
    values = rank_array(word)
    digits = list(map(lowbit, values))
    for r, u in enumerate(values):
        require(extend(values,r+h) == 3*u + digits[r], "true edge")
    shifts, coeff, m = filter_digits(p, h, length, positive)
    w = [sum(b*extend(values,r+t) for b,t in zip(coeff,shifts)) for r in range(p)]
    c = [sum(b*extend(digits,r+t) for b,t in zip(coeff,shifts)) for r in range(p)]
    for r in range(p):
        require(((1 << m)*w[r]-values[r]).denominator == 1, "integer residual")
        require(w[r].denominator == values[r].denominator, "entire odd denominator")
        e = w[r]-values[r]/(1 << m)
        require((0 <= e <= 8*length) if positive else abs(e) <= 4*length, "linear height")
        require(extend(w,r+h) == 3*w[r]+c[r], "virtual recurrence")
    locked = [w[r] > 0 and c[r] == lowbit(w[r]) for r in range(p)]
    return {
        "period": p, "dyadic_clock":h, "denominator":values[0].denominator,
        "length":length, "positive_filter":positive, "m":m, "coefficients":coeff,
        "strictly_ordered":all(x<y for x,y in zip(w,w[1:])),
        "locked_ranks":sum(locked), "range":[str(min(w)),str(max(w))],
        "integer_correction_range":[min(c),max(c)], "first_failed_lock":next((
            {"rank":r, "filtered_state":str(w[r]),"filtered_correction":c[r]}
            for r in range(p) if not locked[r]),None)
    }


if __name__ == '__main__':
    words = [[2], [1,1,2,2,2], [1,1,1,2,2,2,2,2],
             list(map(int,"12112121212211222212212121221122212211222"))]
    print(json.dumps([audit(word, length, positive) for word in words
                     for length in [1,4,12,32] for positive in [False,True]], indent=2))
