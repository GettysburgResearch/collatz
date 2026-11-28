"""Exact arithmetic controls for the one-run higher additive order theorem."""

import hashlib
import json
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb, factorial, prod
from pathlib import Path

from check_native_return_curvature import (
    binary_floor, dates_and_lift, mechanical_numerator, require, two_power,
)


def natural_log_interval(x):
    """Decimal ln is correctly rounded. The adjoining representable numbers bracket it."""
    with localcontext() as ctx:
        ctx.prec = 58
        def bounds(n):
            if n == 1:
                return Fraction(0), Fraction(0)
            value = Decimal(n).ln()
            return Fraction(value.next_minus()), Fraction(value.next_plus())
        num_lo, num_hi = bounds(x.numerator)
        den_lo, den_hi = bounds(x.denominator)
        return num_lo - den_hi, num_hi - den_lo


def exact_gap(r):
    # The strict active gap uses the *first* j for which min(2^{jγ−p},2^{p−jγ}) conflicts.
    # Use the multiplicative distance to the nearest power of two, avoiding a logarithm.
    for j in range(1, 1000):
        y = 3**j
        b = y.bit_length() - 1
        distance = min(Fraction(y, 1 << b), Fraction(1 << (b+1), y))
        if distance <= r/2:
            return j
    raise ArithmeticError('expand gap search')


def certified_rate(r, mu, h, upper):
    gap = exact_gap(r)
    require(h < 3**gap, 'full strict ternary bound')
    eta_gamma = natural_log_interval(r/2)[1] / natural_log_interval(Fraction(3))[0]
    log2_low = natural_log_interval(Fraction(2))[0]
    kappa = mu - 1
    maxima = []
    for j in range(2, min(h, 65)+1):
        order = j-1
        i_upper = natural_log_interval(Fraction(4**order, comb(2*order, order)))[1] / log2_low
        maxima.append((1+j*kappa)*eta_gamma*i_upper/order)
    i_h_upper = 1 + natural_log_interval(Fraction(h))[1]/(2*log2_low)
    if h > 65:
        # For n>=1, binom(2n,n)>=4^n/(2 sqrt n). Its induction step squared:
        # (2n+1)^2 >= 4n(n+1), with exact difference one.
        maxima.append((kappa+(1+kappa)/64)*eta_gamma*i_h_upper)
    require(max(maxima) < 1, 'every bootstrap inequality strict')
    require(eta_gamma*i_h_upper/h < upper, 'certified final residence exponent')
    return {'width': str(r), 'mu_upper': str(mu), 'h': h, 'L': gap,
            'r_h_strict_upper': str(upper), 'bootstrap_upper_rounded_up_6dp':
            (max(maxima)*10**6).__ceil__() / 10**6}


def determinant(entries):
    a = [[Fraction(x) for x in row] for row in entries]
    answer = Fraction(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            answer = -answer
        lead = a[i][i]
        answer *= lead
        for j in range(i+1, len(a)):
            scale = a[j][i]/lead
            for k in range(i+1, len(a)):
                a[j][k] -= scale*a[i][k]
    return answer


def power_coordinate_control():
    primes = [17,19,23,29,31,37,41,43,47,53]
    for d in range(1,len(primes)+1):
        exponents = primes[:d]
        a = [[(-1)**(k-1)*k*comb(l,k) for k in range(1,d+1)] for l in exponents]
        expected = (Fraction((-1)**(d*(d-1)//2)*factorial(d)*prod(exponents),
                             prod(factorial(k) for k in range(1,d+1)))
                    *prod(exponents[j]-exponents[i] for i in range(d) for j in range(i+1,d)))
        require(determinant(a) == expected != 0, 'confluent symmetric-coordinate determinant')
    # These unequal lists have equal first two ordinary moments; one power comparison is insufficient.
    x, y = [0,3,3], [1,1,4]
    require(all(sum(t**j for t in x) == sum(t**j for t in y) for j in (1,2)),
            'adversarial moment-matching multisets')
    a = [1+Fraction(t,1024) for t in x]
    b = [1+Fraction(t,1024) for t in y]
    require(all(sum(t**j for t in a) != sum(t**j for t in b) for j in primes[:3]),
            'three dilated exponents distinguish this repeated-root test')
    # Explicitly cancel common multiplicities before evaluating a left root.
    left, right = Counter([0,0,1,2]), Counter([0,1,1,2])
    common = left & right
    require(left-common == {0:1} and right-common == {1:1}, 'full multiset cancellation')
    return {'jacobian_dimensions_verified':list(range(1,len(primes)+1)),
            'unequal_repeated_root_lists_with_equal_first_two_moments':[x,y]}


def native_fixture(q):
    # Rational mechanical calendar has exactly period 53; long dyadic source cylinder realizes it.
    p,h,length = 53,84,2700
    tolls = [((j+1)*h)//p - (j*h)//p for j in range(length-1)]
    y,_ = mechanical_numerator(tolls,q)
    nums,E = dates_and_lift(y,q,length)
    require(all(E[j] == (j*h)//p for j in range(length)), 'true prescribed calendar')
    require(len(set(nums)) == length, 'distinct actual rational states')
    m = min(nums)
    require(max(nums)*2 < m*5, 'true entire band below 5/2')
    # All comparisons are in numerator units, q kept even when it shares factors with a prime dilation.
    anchor, offsets, primes = 300, [0,53,106], [5,7,11,13,17]
    native = [num << e for num,e in zip(nums,E)]
    U = [1 << e for e in E]
    floor = binary_floor(Fraction(4*native[anchor], 7*m))
    tags = [two_power(E[anchor+s]-s*h//p-floor) for s in offsets]
    require(set(tags) <= {1,2}, 'common binary chart')
    w = [Fraction(3**s,1 << (s*h//p)) for s in offsets]
    require(len(set(w)) == len(w), 'native homogeneous factors distinct on same reduced rank')
    labels = [two_power(-s*h//p-floor)*native[anchor+s] for s in offsets]
    for j in (2,3,4,5):
        sums = [sum(labels[t] for t in entries)
                for entries in combinations_with_replacement(range(len(labels)),j)]
        require(len(sums) == len(set(sums)), 'actual physical B_j fixture')
    # P=I−2D+D² tests a signed repeated-middle comparison.
    # Its actual forcing vanishes for all true dates here, although its label value is nonzero.
    for i in (anchor,anchor+13,anchor+71):
        for l in primes:
            force = U[i] - 2*two_power(-l*h)*U[i+l*p] + two_power(-2*l*h)*U[i+2*l*p]
            require(force == 0, 'exact dilated native forcing')
            signed = (native[i] - 2*two_power(-l*h)*native[i+l*p]
                      + two_power(-2*l*h)*native[i+2*l*p])
            digs = binary_floor(Fraction(4*native[i], 7*m))
            signed *= two_power(-digs)
            require(signed != 0 and signed.denominator == 1,
                    'inhomogeneous actual comparison remains nonzero before coded deadline')
            nb = 25
            end_floor = binary_floor(Fraction(4*native[i+nb],7*m))
            require(int(signed) % (1 << (end_floor-digs)) == 0, 'full Q native divisor')
            # Freshman's dream in the actual shift ring; test intermediate coefficients too.
            require(all(comb(2*l,k) % l ==
                        ({0:1,l:-2,2*l:1}.get(k,0)*(-1)**k) % l for k in range(2*l+1)),
                    'all signed Frobenius coefficients in one-variable shift operator')
    require(3**25 < max(labels), 'finite example deliberately below global decoder horizon')
    return {'Q':q,'odd_states':length,'reduced_stride':p,'dilations':primes,
            'repeated_middle_full_Q_nonzero_comparisons':3*len(primes),
            'B_orders_on_actual_three_distinct_sampled_labels':[2,3,4,5],
            'tested_25_edge_divisor_before_size_cutoff':True}


if __name__ == '__main__':
    paper = Path(__file__).with_name('HIGH_ORDER_NATIVE_RESIDENCE.md')
    out={'source_sha256':hashlib.sha256(paper.read_bytes()).hexdigest(),
         'interval_certified_rates':[
             certified_rate(Fraction(41,20), Fraction(5116201,1000000), 3**12-1, Fraction(445,10**9)),
             certified_rate(Fraction(21,10),Fraction(3),3**12-1,Fraction(879,10**9)),
             certified_rate(Fraction(12,5),Fraction(3),8,Fraction(52,1000))],
         'symmetric_coordinates':power_coordinate_control(),
         'finite_native_controls':[native_fixture(q) for q in (1,35)]}
    print(json.dumps(out,sort_keys=True,indent=2))
