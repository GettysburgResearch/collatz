"""Exact independent finite controls for the two-word staircase Padé calculation."""

from fractions import Fraction
from itertools import product
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def binary_valuation(value):
    require(value != 0, "binary valuation requires a nonzero rational")
    numerator = abs(value.numerator)
    denominator = value.denominator
    return (numerator & -numerator).bit_length() - (denominator & -denominator).bit_length()


def affine(word):
    odds = offset = 0
    for index, bit in enumerate(word):
        if bit:
            odds += 1
            offset = 3*offset + (1 << index)
    return odds, offset


def repeated_orbit(word, separator, runs):
    prescribed = []
    boundaries = []
    for count in runs:
        prescribed.extend(word*count)
        prescribed.extend(separator)
        boundaries.append(len(prescribed))
    odds, offset = affine(prescribed)
    modulus = 1 << len(prescribed)
    x = (-offset * pow(3, -odds, modulus)) % modulus + modulus
    state = x
    after = []
    boundary_set = set(boundaries)
    for index, bit in enumerate(prescribed, start=1):
        require(state % 2 == bit, "positive integer does not realize prescribed cylinder")
        state = (3*state+1)//2 if bit else state//2
        if index in boundary_set:
            after.append(state)
    return x, after


def choose_two(j):
    return j*(j-1)//2


def height(value):
    return max(abs(value.numerator), value.denominator)


def parameters(word, separator):
    p, v = len(word), len(separator)
    sigma, offset = affine(word)
    eta, sep_offset = affine(separator)
    rho = Fraction(offset, (1 << p)-3**sigma)
    lam = Fraction(3**sigma, 1 << p)
    kap = Fraction(3**eta, 1 << v)
    delta = (kap-1)*rho + Fraction(sep_offset, 1 << v)
    return p, v, rho, lam, kap, delta


def finite_family(word, separator, a, b, slope, s):
    p, v, rho, lam, kap, delta = parameters(word, separator)
    require(delta != 0 and slope != 0, "nondegenerate family required")
    n, m = 2*s, s
    last_separator = 5*s+14
    runs = [a] + [b+j*slope for j in range(last_separator-1)]
    require(min(runs) >= 0, "invalid decreasing truncation")
    x, after = repeated_orbit(word, separator, runs)
    q = lam**slope
    z = 1/(kap*lam**b)
    alpha = p*abs(slope)
    spacing = v+p*b
    loss = v+binary_valuation(delta)
    require(q > 0 and z > 0, "positive Padé parameters")
    require(binary_valuation(q) == (-alpha if slope > 0 else alpha)
            and binary_valuation(z) == spacing, "macro clock valuations")
    y = -kap*lam**a*(x-rho)/delta
    terms = [z**j/q**choose_two(j) for j in range(last_separator)]
    partial = [Fraction(0)]
    for entry in terms:
        partial.append(partial[-1]+entry)
    for j in range(1, last_separator):
        diff = y-partial[j]
        require(diff == -terms[j-1]*(after[j-1]-rho)/delta, "finite affine remainder identity")
        if diff:
            require(binary_valuation(diff) >= binary_valuation(terms[j])-loss, "boundary digit loss")
    coefficients = [Fraction(1)]
    for j in range(1, n+1):
        coefficients = [u - q**j*vterm for u, vterm in
                        zip(coefficients+[0], [0]+coefficients)]
    scale = (z.numerator**n * z.denominator**m * q.numerator**choose_two(m)
             * q.denominator**(n*(m+n)))
    weights = [scale*c*q**(choose_two(k)+k*m)/z**k for k, c in enumerate(coefficients)]
    require(all(entry.denominator == 1 for entry in weights), "integer macro weights")
    B = sum(weights)
    A = sum(entry*partial[k+m+1] for k, entry in enumerate(weights))
    require(A.denominator == B.denominator == 1, "integer macro forms")
    require(max(abs(A), abs(B)) <= (3*s+1)*2**(2*s)*height(z)**(3*s)*
            height(q)**(choose_two(m)+n*(n+m)), "macro archimedean budget")
    central = []
    for t in range(1, n+13):
        evaluated = sum(c/q**(t*k) for k,c in enumerate(coefficients))
        val = scale*evaluated*terms[t+m]
        if t <= n:
            require(val == 0, "vanishing Taylor row")
        else:
            central.append(val)
    tails = [weight*(y-partial[n+m+k+13]) for k,weight in enumerate(weights)]
    require(B*y-A == sum(central)+sum(tails), "twelve-row finite Padé identity")
    expected = (5*s+1)*spacing
    if slope > 0:
        expected += alpha*(21*s*s+3*s)//2
        common = 0
    else:
        require(spacing >= 256*alpha*s, "decreasing digit budget")
        expected -= alpha*(25*s*s+5*s)//2
        common = alpha*(choose_two(m)+n*(n+m))
        require(binary_valuation(B) == common and A.numerator % (1 << common) == 0,
                "common dyadic cancellation in decreasing form")
    raw_depth = common+expected
    require(binary_valuation(central[0]) == raw_depth and binary_valuation(B*y-A) == raw_depth,
            "first survivor and physical form depth")
    for rest in central[1:]+tails:
        require(rest == 0 or binary_valuation(rest) > raw_depth, "strict remaining macro depth")
    return {"families": 1, "actual_sources": 1, "checked_remainders": last_separator-1,
            "strict_survivors_and_tails": 11+len(tails), "q_lt_one": int(q<1),
            "positive_slope": int(slope>0), "negative_slope": int(slope<0),
            "nonintegral_dyadic_separator": int(binary_valuation(delta)<0),
            "positive_boundary_valuation": int(binary_valuation(delta)>0)}


def run():
    word_pairs = [("0", "1"), ("1", "0"), ("100", "1101"), ("1110", "011"),
                  ("011", "00000"), ("001", "101"), ("10", "1"),
                  ("00001", "0"), ("11110", "1")]
    counts = {}
    for index, (w,v) in enumerate(word_pairs):
        word = tuple(map(int,w))
        separator = tuple(map(int,v))
        for slope in (1+index%2, -(1+index%2)):
            s = 2 if (slope>0 or index<2) and index%2==0 else 1
            b = 256*s*abs(slope) if slope<0 else index%4
            results = finite_family(word, separator, index%3, b, slope, s)
            for key, number in results.items():
                counts[key] = counts.get(key,0)+number
    zero = 0
    for length in range(1,5):
        for word in product((0,1), repeat=length):
            for copies in (1,2,3):
                *_,delta = parameters(word, word*copies)
                require(delta == 0, "shared periodic phases")
                zero += 1
    counts["shared_phase_pairs"] = zero
    return counts


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True))
