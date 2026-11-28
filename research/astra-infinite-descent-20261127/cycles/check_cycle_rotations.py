"""Exact finite controls for native shortcut and valuation-word rotations."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd
import json


def require(cond, detail):
    if not cond:
        raise ValueError(detail)


def ceiling_log2(n):
    return (n - 1).bit_length()


def numerical():
    u = Fraction(485, 306)
    require((1 << u.numerator) > 3 ** u.denominator, 'rational slope upper bound')
    out = []
    for lower, s in ((217_000_000_000, 40), (2**100, 132)):
        H = sum((u**j for j in range(s+1)), Fraction(0))
        intercept = 11 + 15 * (ceiling_log2(lower) + 1) + u*s/2
        require(H * intercept < lower and 15 <= intercept, 'dyadic band base and induction')
        out.append({'lower_h': str(lower), 'max_excluded_even_distance': s,
                    'ceiling_period_bound': -(-(H*intercept).numerator // (H*intercept).denominator)})
    return out


def necklaces(n):
    for mask in range(1, 1 << n):
        word = tuple((mask >> k) & 1 for k in range(n))
        if any(word[k:] + word[:k] <= word for k in range(1, n)):
            continue
        yield word


def rational_labels(word):
    h = len(word)
    p = sum(word)
    D = 2**h - 3**p
    if D <= 0:
        return None
    C = date = 0
    for w in word:
        C = 3**w*C + (w << date)
        date += 1
    common = gcd(D, C)
    q = D // common
    z = C // common
    labels = []
    for w in word:
        require(z > 0 and z % 2 == w and gcd(z, q) == 1, 'true branch and reduced numerator')
        labels.append(z)
        z = (3**w*z + w*q) // 2
    require(z == labels[0] and len(set(labels)) == h, 'primitive physical closure')
    return labels, q, D


def shortcut_control(word, labels, q, D):
    h = len(word)
    cases = nonunit = pairs = 0
    for root in range(h):
        U = 2 * labels[root] + q
        rotated = word[root:] + word[:root]
        carry = 0
        for j, bit in enumerate(rotated):
            carry = 3**bit * carry + (1 << j)
        require(D*U == q*carry, 'constant-force full numerator')
    for shift in range(1, h):
        bad = [word[j] != word[(j+shift) % h] for j in range(h)]
        s = sum(bad)
        require(s >= 2 and s % 2 == 0, 'two directional mismatch counts agree')
        for j, x in enumerate(labels):
            y = labels[(j+shift) % h]
            require(2*y+q <= 3**(s//2)*(2*x+q), 'all-phase positive-force comparison')
            n = 0
            while not bad[(j+n) % h]:
                n += 1
            require((y-x) % (1 << n) == 0 and 1 << n < max(x+q, y+q), 'genuine nonzero shared-word spacing')
            pairs += 1
        cases += 1
        nonunit += gcd(shift, h) > 1
    return cases, nonunit, pairs


def tower(e, lag, check_levels):
    p, h = len(e), sum(e)
    d = gcd(p, lag)
    M = p // d
    step = lag // d
    s = sum(e[i] != e[(i+lag) % p] for i in range(p))
    # k follows the lag direction, so the original quotient j is k*step mod M.
    rectangles = []
    for r in range(d):
        circle = [r+d*((k*step) % M) for k in range(M)]
        runs = []
        for i in circle:
            if not runs or e[runs[-1][-1]] != e[i]:
                runs.append([])
            runs[-1].append(i)
        rectangles.extend(runs)
    require(len(rectangles) <= d+s, 'number of base roof intervals')
    positions = [(i, level) for row in rectangles for level in range(e[row[0]]) for i in row]
    require(len(positions) == h and len(set(positions)) == h, 'tower parametrizes every physical date')
    index = {x:j for j,x in enumerate(positions)}
    forward = [index[(i, level+1) if level+1 < e[i] else ((i+1) % p, 0)] for i, level in positions]
    require(set(forward) == set(range(h)), 'exact time permutation')
    pieces = 1+sum(y != x+1 for x,y in zip(forward, forward[1:]))
    require(pieces <= 3*len(rectangles)+1, 'number of translation pieces')
    bits = [int(v == 0) for _,v in positions]
    require(sum(x != y for x,y in zip(bits, bits[1:])) <= 2*len(rectangles), 'base layer boundaries')
    prev = [0]*h
    previous_d = 0
    for n in range(1, check_levels+1):
        types = {}
        labels = []
        for i in range(h):
            pair = (bits[i], prev[forward[i]])
            labels.append(types.setdefault(pair, len(types)))
        cuts = sum(u!=v for u,v in zip(labels,labels[1:]))
        require(cuts <= previous_d + 5*len(rectangles), 'reconstructed adjacent-word cut recursion')
        require(len(types) <= 1+5*len(rectangles)*n, 'all cyclic factors, including repeated wraps')
        prev, previous_d = labels, cuts
    return pieces


def capped_tracks(e, lag, n):
    p, h = len(e), sum(e)
    d = gcd(p, lag)
    order = p//d
    s = sum(e[i] != e[(i+lag) % p] for i in range(p))
    b = tuple(min(gap, n+1) for gap in e)
    def expanded(spans):
        return tuple(int(offset==0) for span in spans for offset in range(span))
    def cyclic_factors(bits):
        return [tuple(bits[(i+j)%len(bits)] for j in range(n)) for i in range(len(bits))]
    original = set(cyclic_factors(expanded(e)))
    actual = cyclic_factors(expanded(b))
    require(original == set(actual), 'precisely the same factors after truncating all long zero runs')
    lookup = {}
    t=0
    for i,span in enumerate(b):
        for u in range(span):
            lookup[i,u]=actual[t]
            t+=1
    full = opens = bad_source = bad_later = 0
    for r in range(d):
        track = [(r + j*lag) % p for j in range(order)]
        for u in range(max(b[i] for i in track)):
            full += int(all(u<b[i] for i in track))
            for i in track:
                j=(i+lag) % p
                if u>=b[i] and u<b[j]:
                    opens += 1
                elif u<b[i] and u<b[j] and lookup[i,u] != lookup[j,u]:
                    if b[i] != b[j]:
                        bad_source += 1
                    else:
                        bad_later += 1
    require(order*full <= h, 'additive complete-track cost')
    require(opens <= s*(n+1) and bad_source <= s*(n+1) and bad_later <= s*n,
            'separate additive charges independent of the original roof heights')
    require(len(original) <= full+opens+bad_source+bad_later, 'component count controls every factor')
    require(order*len(original) <= h + order*3*s*(n+1), 'sharper additive complexity bound')
    return [full,opens,bad_source,bad_later,len(original)]


def windows(e, oddlabels, q, D):
    p, h = len(e), sum(e)
    E = [0]
    for k in e+e:
        E.append(E[-1]+k)
    checked = proportional = beyond_nearest = 0
    for lag in range(1,p):
        t = [E[i+lag]-E[i] for i in range(p)]
        targets = {min(t),max(t), (lag*h)//p, (lag*h)//p+1}
        for K in targets:
            psi = [((1 << t[i])*oddlabels[(i+lag) % p]-(1 << K)*oddlabels[i]) for i in range(p)]
            support = [i for i in range(p) if t[i] != K]
            require(0 not in psi and support, 'nonvanishing at all physical cuts')
            Q = q//gcd(q, abs(2**K-3**lag))
            require(all(q//gcd(abs(value),q)==Q for value in psi), 'full exact signed denominator')
            R = sum(3**(p-1-i) * ((1 << (E[i]+t[i]))-(1 << (E[i]+K))) for i in support)
            require(q*R == D*psi[0], 'native unrolled sparse signed numerator')
            for i in range(p):
                require((1 << e[i])*psi[(i+1) % p] == 3*psi[i]+q*((1<<t[i])-(1<<K)), 'window transport')
            checked += 1
            proportional += K*p == h*lag
            beyond_nearest += abs(K*p - h*lag) >= p
    return checked, proportional, beyond_nearest


def main():
    totals = Counter()
    for h in range(2,15):
        for word in necklaces(h):
            model = rational_labels(word)
            if model is None:
                continue
            labels,q,D = model
            ss,ns,pairs=shortcut_control(word,labels,q,D)
            totals.update(necklaces=1, shortcut_shifts=ss, nonunit_shifts=ns, physical_comparisons=pairs)
            odd = [i for i,w in enumerate(word) if w]
            e = tuple(j-i for i,j in zip(odd,odd[1:]+[odd[0]+h]))
            n,p,b = windows(e,[labels[i] for i in odd],q,D)
            totals.update(window_pairs=n, exact_proportional_windows=p, nonnearest_targets=b)
            for lag in range(1,len(e)):
                tower(e,lag,min(5,h+1))
                totals['native_towers'] += 1
                for n in (2,5):
                    capped_tracks(e,lag,n)
                    totals['capped_track_checks'] += 1
    cases = [(16, 6, {0: 401, 3: 103, 7: 89}), (21, 7, {0: 121, 6: 64}),
             (35, 8, {4: 731, 11: 257, 19: 381}), (8, 4, {0: 1501})]
    tall = []
    for p,lag,values in cases:
        e = tuple(values.get(i, 1+i % gcd(p,lag)) for i in range(p))
        tall.append({'p':p,'lag':lag,'h':sum(e),'max_valuation':max(e),'pieces':tower(e,lag,25),
                     'cap_at_11':capped_tracks(e,lag,11),'cap_at_22':capped_tracks(e,lag,22)})
    print(json.dumps({'exact_numerical_bounds': numerical(),'exhaustive_native':dict(totals),'tall_towers':tall},indent=2))


if __name__ == '__main__':
    main()
