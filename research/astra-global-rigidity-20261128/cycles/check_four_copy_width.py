"""Finite exact controls for the moment calculation and source orientation."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product
from math import factorial
import json


def check(value, message):
    if not value:
        raise AssertionError(message)


def octave(z):
    while z < 1:
        z *= 2
    while z >= 2:
        z /= 2
    return z


def numerator(word):
    n, e = 0, 0
    for v in word:
        n = 3*n + (1 << e)
        e += v
    return n


def energy_case(phase, width, n):
    phases = [octave(phase*Q(3,2)**i) for i in range(n)]
    active = {i for i,z in enumerate(phases) if 2*z < width}
    edges = [(i,i+1) for i,z in enumerate(phases[:-1])
             if i+1 in active and 3*z < 4]
    check(all(i in active for i,_ in edges), "edge begins at active site")
    check(2*len(edges) == len(set(j for pair in edges for j in pair)), "matching")
    weights, elapsed = [], 0
    for i,z in enumerate(phases):
        weights.append(3**(n-1-i) * (1 << elapsed))
        elapsed += 1 + (3*z >= 4)
    vals = []
    for bits in product((0,1),repeat=len(active)):
        grades = dict(zip(sorted(active),bits))
        if any(grades[i] < grades[j] for i,j in edges):
            continue
        vals.append(sum(w*(2-grades.get(i,0)) for i,w in enumerate(weights)))
    count = Counter(x+y for x in vals for y in vals)
    exact = sum(c*c for c in count.values())
    free = len(active) - 2*len(edges)
    check(exact == 6**free * 15**len(edges), "direct integer pair energy")
    return len(vals), exact


def verify_segments(word):
    b, k = len(word), sum(word)
    mod = 1 << k
    carry = numerator(word)
    if mod <= 3**b:
        return 0
    y = Q(carry,mod-3**b)
    source = (-carry*pow(3**b,-1,mod)) % mod
    check((y.numerator-y.denominator*source) % mod == 0, "whole-source congruence")
    count = 0
    for cuts in combinations_with_replacement(range(b+1),3):
        endpoints = (0,*cuts,b)
        residue_sum = Q(0)
        for j,v in zip(endpoints,endpoints[1:]):
            rem = 1 << (k-sum(word[:j]))
            signed = (-numerator(word[j:v])*pow(3**v,-1,rem)) % rem
            residue_sum += Q(signed,rem)
        check((residue_sum-Q(source,mod)).denominator == 1, "local sum orientation")
        count += 1
    check((y/mod - Q(source,mod))*y.denominator % 1 == 0, "arithmetic-lift arcs")
    return count


def lnbounds(x):
    """Atanh series, exact enclosure for x >= 1."""
    x = Q(x)
    t = (x-1)/(x+1)
    n = 105
    partial = 2*sum((t**(2*i+1)/(2*i+1) for i in range(n)),Q(0))
    tail = 2*t**(2*n+1)/((2*n+1)*(1-t*t))
    return partial, partial+tail


def chibounds(width):
    lo2,hi2 = lnbounds(2)
    l3,u3 = lnbounds(3)
    l6,u6 = lnbounds(6)
    l15,u15 = lnbounds(15)
    lw,uw = lnbounds(Q(width)/2)
    la,ua = lnbounds(Q(3,2))
    eta = lw/hi2,uw/lo2
    a = la/hi2,ua/lo2
    f = max(0,eta[0]-a[1]),max(0,eta[1]-a[0])
    return ((eta[0]-2*f[1])*l6+f[0]*l15)/(3*u3), ((eta[1]-2*f[0])*u6+f[1]*u15)/(3*l3)


def main():
    cases = arrays = sums = rows = 0
    for n in range(1,9):
        for phase in map(Q,("1","10/9","4/3","3/2","17/10","19/10")):
            for width in map(Q,(2,"9/4","12/5",3,"27/8","7/2",4)):
                size,cost = energy_case(phase,width,n)
                cases += 1
                arrays += size
                sums += cost
    for word in product((1,2,3),repeat=5):
        rows += verify_segments(word)
    weights = [27,18,24,16]
    left, right = [(1,1,1,0),(1,0,1,0),(0,0,0,0)], [(0,0,1,1)]*3
    check(all(g[0]>=g[1] and g[2]>=g[3] for g in left+right), "six-copy admissibility")
    delta = [sum(g[i] for g in left)-sum(g[i] for g in right) for i in range(4)]
    check(any(delta) and sum(x*y for x,y in zip(weights,delta))==0, "six-copy collision")
    carry,carries = 0,[0]
    for d,b in zip(delta,(1,2,1,2)):
        carry,rem = divmod(3*carry+d,1 << b)
        check(rem == 0,"integral higher carry")
        carries.append(carry)
    check(carries == [0,1,1,1,0],"six-copy carry trace")
    for d in (2,3):
        values = []
        for k in (1,2,3):
            multiplicities=Counter(tuple(row.count(j) for j in range(d)) for row in product(range(d),repeat=k))
            values.append(sum(v*v for v in multiplicities.values()))
        check(values == ([2,6,20] if d==2 else [3,15,93]), "diagonal counts")
        check(values[2]**3>values[1]**5 and values[0]**3>=values[1], "higher-moment obstruction")
    check(chibounds(3)[1] < Q(100,314), "clock exponent at width 3")
    check(chibounds(4)[1] < Q(10,23), "clock exponent at width 4")
    check(chibounds(Q(3116,1000))[1]<Q(1,3)<chibounds(Q(3117,1000))[0], "width threshold")
    print(json.dumps({"finite_energy_models":cases,"admissible_grade_arrays":arrays,
                      "integer_four_collisions":sums,"rational_source_decompositions":rows,
                      "six_copy_integral_trace":carries},sort_keys=True))


if __name__ == "__main__":
    main()
