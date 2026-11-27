"""Exact primitive rational cycle and residue-order controls, no external packages."""
from collections import Counter
from itertools import product
from math import gcd
import json


def necklaces(length, alphabet):
    # Classical direct generation of lexicographically least primitive rotations.
    word = [0] * (length + 1)
    def walk(i, period):
        if i > length:
            if period == length:
                yield tuple(x + 1 for x in word[1:])
            return
        word[i] = word[i - period]
        yield from walk(i + 1, period)
        for symbol in range(word[i - period] + 1, alphabet):
            word[i] = symbol
            yield from walk(i + 1, i)
    yield from walk(1, 1)


def make_cycle(word):
    p, a = len(word), sum(word)
    determinant = (1 << a) - 3 ** p
    if determinant <= 0:
        return
    b, height = 0, 0
    for e in word:
        b = 3 * b + (1 << height)
        height += e
    divisor = gcd(determinant, b)
    numerator, denominator = b // divisor, determinant // divisor
    ns = []
    x = numerator
    for e in word:
        ns.append(x)
        u = 3 * x + denominator
        assert (u & -u) == 1 << e
        x = u >> e
    assert x == numerator and len(set(ns)) == p
    return denominator, ns


def analyze(word, d, ns):
    p, a = len(word), sum(word)
    common = gcd(p, a)
    q, block_sum = p // common, a // common
    order = 1
    if d > 1:
        unit = (pow(3, q, d) * pow(2, -block_sum, d)) % d
        factor = unit
        while factor != 1:
            factor = factor * unit % d
            order += 1
            assert order <= common
    assert common % order == 0
    discrepancies = []
    e_total = 0
    for i, exp in enumerate(word):
        discrepancies.append(p * e_total - i * a)
        e_total += exp
    root = discrepancies.index(max(discrepancies))
    es = word[root:] + word[:root]
    xs = ns[root:] + ns[:root]
    total = 0
    grades = []
    for j, e in enumerate(es):
        grades.append(j * a // p - total)
        total += e
    assert min(grades) == 0
    h = max(grades)
    ls = [x << (h - z) for x,z in zip(xs, grades)]
    low = [x & -x for x in ls]
    if d != 1:
        assert all((ls[(j+q)%p] - unit * ls[j]) % d == 0 for j in range(p))
    fibre_size = common // order
    inversions = []
    for start in range(q * order):
        fibre = sorted(range(start, p, q * order), key=ls.__getitem__)
        for i, j in ((i,j) for ix,i in enumerate(fibre) for j in fibre[ix+1:]):
            assert (ls[i] - ls[j]) % d == 0
            if ls[(i+1)%p] <= ls[(j+1)%p]:
                assert ls[(i+1)%p] < ls[(j+1)%p]
                continue
            assert low[i] > low[j]
            t = (low[i] // low[j]).bit_length() - 1
            jump, rem = divmod(xs[j] - (1 << t) * xs[i], d)
            assert rem == 0 and jump % 2 == 1 and jump > 0 and 3*jump < (1 << t)-1
            assert t >= 3
            inversions.append((xs[i],xs[j],t,jump))
    assert len(inversions) >= fibre_size-1
    assert common == order or (h >= 3 and max(xs) > 8*min(xs))
    return h,common,order,inversions


def check():
    counts = Counter()
    examples = {}
    for alph, maxlen, minlen in ((2,18,1),(3,11,1),(4,8,1)):
        for p in range(minlen,maxlen+1):
            for w in necklaces(p,alph):
                if alph > 2 and max(w)<alph:
                    continue
                physical = make_cycle(w)
                if physical is None:
                    continue
                d, ns=physical
                h,g,k,inv=analyze(w,d,ns)
                counts['positive primitive necklaces'] += 1
                counts['height at most two'] += h <= 2
                counts['physical band at most eight'] += max(ns)<=8*min(ns)
                counts['nontrivial exact order'] += g==k and k>1
                counts['proper order divisor'] += g>k
                counts['inverted pairs'] += len(inv)
                for name,cond in [('nontrivial exact order',k>1 and h<=2),('physical band above height two',h>2 and max(ns)<=8*min(ns)),('proper order divisor',g>k),('height three proper order',g>k and h==3)]:
                    if cond and (name not in examples or (d,p)<(examples[name]['denominator'],len(examples[name]['word']))):
                        examples[name]={'word':w,'denominator':d,'odd_numerators':ns,'canonical_height':h,'gcd':g,'order':k,'inversions':inv}
    return {'census':counts,'examples':examples,'domains':{'binary_max_period':18,'ternary_max_period':11,'quaternary_max_period':8}}

if __name__ == '__main__':
    print(json.dumps(check(),indent=2,sort_keys=True))
