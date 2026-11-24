"""Exact finite checks for primitive companion cycles and cyclic suffix marks."""

from fractions import Fraction
from itertools import product
from math import comb, gcd, isqrt
import json


def need(condition):
    if not condition:
        raise AssertionError('companion packing control failed')


def rotations(word):
    return [word[i:] + word[:i] for i in range(len(word))]


def closed(word):
    scale = 1
    carry = 0
    for bit in word:
        carry = 3 * carry + bit * scale
        scale *= 2 ** (1 + bit)
    return Fraction(carry, scale - 3 ** len(word))


def past(word, i, k):
    return tuple(word[(i-k+j) % len(word)] for j in range(k))


def examine(word, slope, upper_ratio, per_family):
    L = len(word)
    p = sum(word)
    if Fraction(p, L) <= slope:
        return
    per_family['instances'] += 1
    # upper_ratio is an exact rational upper bound for 2^(beta-slope).
    denominator = slope.denominator
    need((Fraction(3, 2) ** denominator) / 2**slope.numerator <= upper_ratio**denominator)
    bound = Fraction(1, 4) / (1 - upper_ratio)
    ws = [closed(v) for v in rotations(word)]
    q = ws[0].denominator
    need(gcd(q, 6) == 1 and all(w.denominator == q for w in ws))
    for i, bit in enumerate(word):
        need(2**(1+bit)*ws[(i+1) % L] == 3*ws[i]+bit)
    need(len(set(ws)) == L)
    marks = []
    for i in range(L):
        count = 0
        for j in range(1, L+1):
            count += word[(i-j) % L]
            if count*denominator < j*slope.numerator:
                break
        else:
            marks.append(i)
    need(len(marks)*(1-slope) >= p-L*slope)
    k = 0
    while 3**k <= bound*q:
        k += 1
    words = set()
    for i in marks:
        w = ws[i]
        need(0 < w <= bound)
        v = past(word, i, k)
        words.add(v)
        u = sum(v)
        need(u >= k*slope)
        t = (w*q).numerator
        start = (ws[(i-k) % L]*q).numerator
        carry = 0
        scale = 1
        for bit in v:
            carry = 3*carry+bit*scale
            scale *= 2**(1+bit)
        need(2**(k+u)*t == 3**k*start+q*carry)
        need(t < 3**k)
        per_family['marked_pasts'] += 1
    need(len(words) == len(marks))
    need(len(words) <= sum(comb(k, u) for u in range(k+1) if u >= slope*k))


def main():
    stats = {'primitive_words_up_to_rotation': 0, 'instances': 0, 'marked_pasts': 0}
    parameters = [(Fraction(3, 5), Fraction(99, 100)),
                  (Fraction(5, 8), Fraction(39, 40)),
                  (Fraction(2, 3), Fraction(19, 20))]
    for L in range(1, 15):
        for word in product((0, 1), repeat=L):
            rots = rotations(word)
            if word != min(rots) or len(set(rots)) != L:
                continue
            stats['primitive_words_up_to_rotation'] += 1
            for slope, ratio in parameters:
                examine(word, slope, ratio, stats)
    example = (1, 1, 1, 0, 0)
    for m in range(1, 11):
        need(closed(example*m) == Fraction(333, 13))
    stats['repeated_word_checks'] = 10
    for L in (1024, 1600, 2304, 3136):
        p = 0
        # floor(alpha L) minus the exact square root for these square clocks.
        while 3**(p+1) <= 2**L:
            p += 1
        p -= isqrt(L)
        word = (1,)*p + (0,)*(L-p)
        m = Fraction(3**p-2**p, 2**L-3**p)
        need(0 < m < 1 and closed(word)>0)
    stats['near_critical_rational_controls'] = 4
    print(json.dumps(stats, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
