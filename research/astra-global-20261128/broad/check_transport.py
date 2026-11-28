"""Exact controls for parity transport, cofactor collisions and quadratic-clock forms."""
from fractions import Fraction
from itertools import combinations
from math import lcm
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valuation(value, prime):
    value = abs(value)
    require(value != 0, "valuation of zero")
    power = 0
    while value % prime == 0:
        value //= prime
        power += 1
    return power


def bits(value):
    return value.numerator % 2


def step(value):
    bit = bits(value)
    return (3**bit * value + bit) / 2


def affine(word):
    offset = 0
    odds = 0
    for i, bit in enumerate(word):
        offset = 3**bit * offset + bit * 2**i
        odds += bit
    return odds, offset


def match_controls():
    families = gaps = subsums = 0
    for x in range(1, 65):
        path = [Fraction(x)]
        for _ in range(72):
            path.append(step(path[-1]))
        parity = list(map(bits, path))
        for style in range(6):
            starts = [style % 3]
            lengths = []
            refs = []
            terminals = []
            for j in range(5):
                a = starts[-1]
                length = 1 + (x + 2*j + style) % 5
                denominator = (3, 5, 7, 11)[(style+j) % 4]
                sign = (-1)**(j+style)
                ref = path[a] + sign*Fraction(2**length, denominator)
                terminal = ref
                for t in range(a, a+length):
                    require(bits(terminal) == parity[t], "rational matching phase")
                    terminal = step(terminal)
                require(bits(terminal) != parity[a+length], "maximal rational match")
                lengths.append(length)
                refs.append(ref)
                terminals.append(terminal)
                if j < 4:
                    starts.append(a+length+(style+j) % 4)
            common = lcm(*(rho.denominator for rho in refs))
            total_odds = sum(parity[starts[0]:starts[-1]])
            terms = [3**total_odds * common*(path[starts[0]]-refs[0])]
            for i in range(4):
                left = starts[i]+lengths[i]
                right = starts[i+1]
                word = parity[left:right]
                odds, offset = affine(word)
                carry = 3**odds*terminals[i]+offset-2**len(word)*refs[i+1]
                scaled = common*carry
                require(scaled.denominator == 1 and scaled.numerator % 2 == 1,
                        ("odd signed gap", x, style, i))
                tail_multiplier = max(
                    Fraction(3**sum(word[k:]), 2**(len(word)-k))
                    for k in range(len(word)+1))
                multiplier_bound = (len(word)+2)*(1+abs(terminals[i]))*(1+abs(refs[i+1]))*tail_multiplier
                require(abs(carry)/2**len(word) <= multiplier_bound, "suffix carry bound")
                terms.append(2**(left-starts[0])*3**sum(parity[right:starts[-1]])*scaled)
                gaps += 1
            expected = 2**(starts[-1]-starts[0])*common*(path[starts[-1]]-refs[-1])
            require(sum(terms) == expected, "signed multilinear transport")
            for size in range(1, len(terms)+1):
                for subset in combinations(terms, size):
                    require(sum(subset) != 0, "nonvanishing subsum")
                    subsums += 1
            families += 1
    return {"families": families, "gaps": gaps, "nonzero_subsums": subsums}


def positive_step(x):
    return (3*x+1)//2 if x % 2 else x//2


def cofactor(x):
    z = 2*x+1
    return z // 3**valuation(z, 3)


def collision_controls():
    path = edge_count = single = two_arm = degenerate = 0
    endpoints = {}
    for x in range(1, 513):
        state = x
        odds = 0
        correction = Fraction(1)
        for length in range(13):
            if length and cofactor(state) == cofactor(x):
                d = valuation(2*state+1, 3)-valuation(2*x+1, 3)
                grade = odds-d
                require(0 < grade < length, "nonzero single-path grade")
                require(Fraction(2**length, 3**grade) == correction, "collision product")
                single += 1
            endpoints.setdefault((state, cofactor(x)), []).append((x,length,odds,correction))
            bit = state % 2
            next_state = positive_step(state)
            require(2*(2*next_state+1) == 3**bit*(2*state+1)+1, "shifted branch")
            correction *= 1+Fraction(1, 3**bit*(2*state+1))
            odds += bit
            state = next_state
            edge_count += 1
        path += 1
    for group in endpoints.values():
        for (x,r1,s1,p1),(z,r2,s2,p2) in combinations(group, 2):
            d = valuation(2*z+1,3)-valuation(2*x+1,3)
            grade = s1-s2-d
            require(Fraction(2)**(r1-r2)/Fraction(3)**grade == p1/p2, "two-arm transport")
            require((p1 == p2) == (r1 == r2 and grade == 0), "two-arm alternatives")
            if p1 == p2:
                degenerate += 1
            two_arm += 1
    require(cofactor(1) == cofactor(4) == 1 and positive_step(1) == positive_step(4),
            "necessary sibling cofactor collision")
    return {"paths": path, "edges": edge_count, "single_collisions": single,
            "two_arm_comparisons": two_arm, "zero_forms": degenerate}


def choose2(j):
    return j*(j-1)//2


def pade_forms(s,h,b):
    n,m = 2*s,s
    q = Fraction(3**h,2**h)
    z = Fraction(2**(b+1),3**b)
    coeffs = [Fraction(1)]
    for j in range(1,n+1):
        coeffs = [u-q**j*v for u,v in zip(coeffs+[0], [0]+coeffs)]
    scale = z.numerator**n*z.denominator**m*q.numerator**choose2(m)*q.denominator**(n*(m+n))
    a = bcoef = 0
    for k,c in enumerate(coeffs):
        term = scale*c*z**(-k)*q**(choose2(k)+k*m)
        bcoef += term
        a += term*sum(z**l*q**(-choose2(l)) for l in range(k+m+1))
    require(a.denominator == bcoef.denominator == 1, "integer approximant")
    return a.numerator,bcoef.numerator


def pade_controls():
    cases = prefixes = 0
    for s in range(1,5):
        for h in range(1,5):
            for b in (0,1,3,7,15):
                a,coef = pade_forms(s,h,b)
                require(coef % 2 == 1, "unit Pade coefficient")
                w = h*(21*s*s+3*s)//2+(5*s+1)*(b+1)
                modulus = 2**(w+1)
                value = 0
                j = 0
                while j*(b+1)+h*choose2(j) <= w:
                    power = j*(b+1)+h*choose2(j)
                    denominator = 3**(b*j+h*choose2(j))
                    value += 2**power*pow(denominator,-1,modulus)
                    j += 1
                require((coef*value-a) % modulus == 2**w, "exact valuation of Pade form")
                bound = (3*s+1)*2**(2*s)*(2*3**b)**(3*s)*3**(h*(13*s*s-s)//2)
                require(max(abs(a),abs(coef)) <= bound, "archimedean height of Pade form")
                # Exact exponential version of the two lower margins.
                require(2**(2*w)*3**(13*h*s*s+6*b*s)
                        >= bound**2*2**(21*h*s*s+10*b*s), "simultaneous positive margins")
                cases += 1
                for initial in (0,2,6):
                    length = w+initial+1
                    pinmod = 2**length
                    rho = -1-2**initial*pow(3**initial,-1,pinmod)*value
                    state = rho % pinmod or pinmod
                    zeros = 0
                    next_zero = initial
                    for k in range(length):
                        require((state % 2 == 0) == (k == next_zero), "quadratic prefix cylinder")
                        if k == next_zero:
                            next_zero += 1+b+h*zeros
                            zeros += 1
                        state = positive_step(state)
                    prefixes += 1
    return {"pade_forms": cases, "quadratic_prefixes": prefixes}


def declining_controls():
    cases = 0
    tails = 0
    for s in (1, 2, 3):
        for h in (1, 2):
            for b in (200*h*s, 200*h*s+3):
                n, m = 2*s, s
                modulus_index = 5*s+2
                initial = (s+h) % 3
                z = Fraction(2**(b+1), 3**b)
                q = Fraction(2**h, 3**h)
                coeffs = [Fraction(1)]
                for j in range(1,n+1):
                    coeffs = [u-q**j*v for u,v in zip(coeffs+[0], [0]+coeffs)]
                scale = (z.numerator**n*z.denominator**m*q.numerator**choose2(m)
                         *q.denominator**(n*(m+n)))
                weights = [scale*c*z**(-k)*q**(choose2(k)+k*m) for k,c in enumerate(coeffs)]
                require(all(w.denominator == 1 for w in weights), "integral descending weights")
                terms = [z**j*q**(-choose2(j)) for j in range(modulus_index+1)]
                partial = [Fraction(0)]
                for term in terms:
                    partial.append(partial[-1]+term)
                acoef = sum(weight*partial[k+m+1] for k,weight in enumerate(weights))
                bcoef = sum(weights)
                require(acoef.denominator == bcoef.denominator == 1, "integral descending forms")
                d0 = h*(choose2(m)+n*(n+m))
                require(valuation(bcoef.numerator,2) == d0 and acoef.numerator % 2**d0 == 0,
                        "common descending two-power")
                length = initial+modulus_index*(b+1)-h*choose2(modulus_index)+1
                modulus = 2**length
                rational_pin = -1-Fraction(2**initial,3**initial)*partial[-1]
                x = (rational_pin.numerator*pow(rational_pin.denominator,-1,modulus)) % modulus
                if x == 0:
                    x = modulus
                y = -(x+1)*Fraction(3,2)**initial
                require(y.denominator == 1, "integral descending pin target")
                w = (5*s+1)*(b+1)-h*(2*s+1)*3*s
                raw = bcoef*y-acoef
                require(raw.denominator == 1 and valuation(raw.numerator,2) == w,
                        "exact descending valuation")
                for k,weight in enumerate(weights):
                    j = n+m+k+2
                    tail = y-partial[j]
                    require(valuation(tail.numerator,2)-valuation(tail.denominator,2)
                            == j*(b+1)-h*choose2(j), "native descending tail depth")
                    require(valuation((weight*tail).numerator,2)-valuation((weight*tail).denominator,2)
                            > w, "strict descending remainder")
                    tails += 1
                reduced_height = max(abs(acoef.numerator), abs(bcoef.numerator))//2**d0
                require(2**(8*(w-d0)) >= reduced_height**8*2**(b*s),
                        "uniform descending slope margin")
                cases += 1
    return {"finite_forms": cases, "strict_physical_tails": tails}


if __name__ == "__main__":
    print(json.dumps({"signed_transport": match_controls(), "cofactors": collision_controls(),
                      "quadratic_clocks": pade_controls(), "descending_clocks": declining_controls()}, sort_keys=True))

