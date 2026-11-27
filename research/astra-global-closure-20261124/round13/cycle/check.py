"""Exact switch, decoding, transfer-count and large-factor controls."""
from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd
import json

import sympy as sp


def require(ok, why):
    if not ok:
        raise ValueError(why)


def setup(p, h):
    ranks = [j*h % p for j in range(p+1)]
    edges = [(j+1)*h//p-j*h//p for j in range(p)]
    weights = [3**(p-1-j)*2**(j*h//p) for j in range(p)]
    cap = [1 if r >= 2*p-h else 2 for r in ranks]
    return ranks, edges, weights, cap


def paths(edges, cap, start, stop, state):
    def walk(i, k, word):
        if i == stop:
            yield k, word
            return
        for t in range(cap[i+1]+1):
            if edges[i]+k-t in (1, 2):
                yield from walk(i+1, t, word+(t,))
    return walk(start, state, ())


def carry(word):
    v, w = 0, 1
    for a in word:
        v, w = 3*v+w, w*2**a
    return v


def decode(value, m, total):
    exps = []
    for i in range(m-1):
        rest = value-3**(m-1-i)
        require(rest > 0, 'positive residual')
        a = (rest & -rest).bit_length()-1
        require(a in (1, 2), 'binary valuation decoding')
        exps.append(a)
        value = rest >> a
    require(value == 1 and total-sum(exps) in (1, 2), 'last exponent')
    return (*exps, total-sum(exps))


def transfer(p, h, modulus):
    _, edges, weights, cap = setup(p, h)
    data = {(0, 0): 1}
    for j in range(p):
        nxt = Counter()
        for (k, rem), count in data.items():
            residue = (rem+weights[j]*(4 >> k)) % modulus
            for t in range(cap[j+1]+1):
                if edges[j]+k-t in (1, 2):
                    nxt[t, residue] += count
        data = nxt
    return [data[0, v] for v in range(modulus)]


def inverse_windows(a, s):
    d, S, p = s.denominator, s.numerator, len(a)
    numerators = [S]
    for e in a:
        numerators.append((3*numerators[-1]+d) >> e)
    require(numerators[-1] == S and (2*S+d) % 3 == 0, 'closed rational cycle and partner')
    merger_depth = ((S+d) & -(S+d)).bit_length()
    visits = 0

    def rivals(y, k, budget):
        nonlocal visits
        visits += 1
        if k == 0:
            yield y, 0
            return
        if y % 3 == 0:
            return
        first = 1 if (2*y-d) % 3 == 0 else 2
        for e in range(first, budget-k+2, 2):
            z = ((y << e)-d)//3
            if z > 0:
                for n, cost in rivals(z, k-1, budget-e):
                    yield n, e+cost

    central, attained = 0, 0
    for k in range(1, p+1):
        for i in range(p):
            A = sum((a+a)[i:i+k])
            budget = A+1 if i == 0 else A-2
            found_native = found_partner = False
            for n, cost in rivals(numerators[(i+k) % p], k, budget):
                if i == 0:
                    require(cost >= A and (n % 3 or cost >= A+1), 'minimum optimal clocks')
                    found_native |= (cost == A and n == S)
                    found_partner |= (cost == A+1 and n == 2*S+d)
                else:
                    require(cost >= A-2 and (n % 3 or cost >= A-1), 'every window saving bound')
            if i == 0:
                require(found_native, 'native minimum attained')
                central += 1
                if k >= merger_depth:
                    require(found_partner, 'specific central multiple attains minimum')
                    attained += 1
    return {'windows': p*p, 'central_minima': central, 'merger_depth': merger_depth,
            'central_pairs_attained': attained, 'inverse_recursion_nodes': visits}


def joint_control():
    p, h = 41, 65
    ranks, edges, weights, cap = setup(p, h)
    det = 2**h-3**p
    target = 19*29*17021
    split = 20
    half = defaultdict(list)
    for end, tail in paths(edges, cap, 0, split, 0):
        vals = (0,)+tail
        rem = sum(w*(4 >> k) for w,k in zip(weights, vals[:-1])) % target
        half[end, rem].append(vals[:-1])
    nmatch = 0
    chosen = None
    X = sp.Symbol('X')
    for start in range(3):
        for end, tail in paths(edges, cap, split, p, start):
            if end:
                continue
            word2 = ((start,)+tail)[:-1]
            rem = sum(w*(4 >> k) for w,k in zip(weights[split:], word2)) % target
            for word1 in half[start, (-rem) % target]:
                nmatch += 1
                if chosen is not None:
                    continue
                band = word1+word2
                a = tuple(edges[i]+band[i]-band[(i+1)%p] for i in range(p))
                red = carry(a)
                require(decode(red, p, h) == a, 'whole-lap decoder')
                g = gcd(red, det)
                require(g % target == 0, 'absorbed three prime factors')
                rank_band = [0]*p
                for j,r in enumerate(ranks[:-1]):
                    rank_band[r] = band[j]
                poly = sp.Poly.from_list([4 >> k for k in rank_band], X)
                if not poly.primitive()[1].is_irreducible:
                    continue
                s = Fraction(red, det)
                x = s
                z = [None]*p
                for j in range(p):
                    z[ranks[j]] = x / 2**band[j]
                    require(x.numerator % 2 and x.denominator == s.denominator and
                            s <= x <= (16*s+7)/3, 'physical rational strip')
                    x = (3*x+1)/2**a[j]
                require(x == s and z == sorted(z) and len(set(z)) == p and z[-1] < 2*s,
                        'closed and actually sorted')
                back = ''.join(map(str, reversed(a)))
                if '12212122221212121211' in back*2:
                    continue
                chosen = {'rank_bands': ''.join(map(str,rank_band)), 'exponents': ''.join(map(str,a)),
                          'minimum': str(s), 'gcd': g, 'degree_of_primitive_irreducible': poly.degree(),
                          'forbidden_inverse_window_absent': True, 'inverse_checks': inverse_windows(a, s)}
    require(chosen and nmatch > 0, 'physical irreducible control')
    return {'total': sum(transfer(p,h,1)), 'target': target, 'exact_multiples': nmatch, 'witness': chosen}


def reflection_test():
    X = sp.Symbol('X')
    counts = Counter()
    for p, h in [(5,8), (8,13), (13,21)]:
        ranks, edges, _, cap = setup(p, h)
        for end, tail in paths(edges, cap, 0, p, 0):
            if end:
                continue
            bands = (0,)+tail[:-1]
            coeff = [0]*p
            for j, r in enumerate(ranks[:-1]):
                coeff[r] = 4 >> bands[j]
            changes = sum(k != bands[(i+1)%p] for i,k in enumerate(bands))
            require(changes <= 2*sum(a != b for a,b in zip(coeff, reversed(coeff))),
                    'pointwise reflection bound')
            c = sp.Poly.from_list(coeff, X, domain=sp.QQ)
            rev = sp.Poly.from_list(coeff[::-1], X, domain=sp.QQ)
            common = c.gcd(rev)
            q = c.exquo(common)
            qr = rev.exquo(common)
            mult = sp.Poly(1, X, domain=sp.QQ)
            for _ in range(200):
                A, B = qr*mult, q*mult
                if min(A.all_coeffs()+B.all_coeffs()) >= 0:
                    break
                mult *= sp.Poly(X+1, X, domain=sp.QQ)
            else:
                raise ValueError('positive multiplier test exceeded control range')
            require(A*c == B*rev and changes <= 2*A.degree(), 'positive convolution bound')
            counts['words'] += 1
            counts['nonconstant_with_common_factor'] += int(changes > 0 and common.degree() > 0)
            counts['needed_positive_multiplier'] += int(mult.degree() > 0)
    return dict(counts)


def main():
    # All starts and both ends are retained in the binary carry uniqueness test.
    from itertools import product
    decoded = 0
    for length in range(1,10):
        for word in product((1,2), repeat=length):
            require(decode(carry(word),length,sum(word)) == word, 'local decoder')
            decoded += 1
    rows = []
    for p,h,m in [(5,8,13),(41,65,19),(41,65,29),(306,485,1)]:
        counts = transfer(p,h,m)
        require((2**h-3**p) % m == 0,'actual determinant divisor')
        rows.append({'p':p,'h':h,'modulus':m,'min':min(counts),'max':max(counts),'total':sum(counts)})
    return {'decoded':decoded,'transfer_censuses':rows,'reflection':reflection_test(),
            'high_degree_control':joint_control()}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2))
