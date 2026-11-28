"""Native rational cycle and signed chronological sampling controls."""

import json
from fractions import Fraction
from itertools import combinations_with_replacement
from math import gcd


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def floor_log2(a, b):
    """Exact floor(log2(a/b)) for positive integers."""
    k = a.bit_length() - b.bit_length()
    if (a << max(-k, 0)) < (b << max(k, 0)):
        k -= 1
    return k


def native_cycle(exponents):
    p, A = len(exponents), sum(exponents)
    D = (1 << A) - 3**p
    require(D > 0, "positive closure")
    C = 0
    E = [0]
    for e in exponents:
        C = 3*C + (1 << E[-1])
        E.append(E[-1]+e)
    g = gcd(C, D)
    q, y0 = D//g, C//g
    y = [y0]
    for e in exponents:
        v, rem = divmod(3*y[-1] + q, 1 << e)
        require(rem == 0 and v % 2 and gcd(v, q) == 1, "true reduced odd update")
        y.append(v)
    require(y.pop() == y0 and len(set(y)) == p, "primitive physical period")
    return E, q, y


def clock_word(P, B, sheets, seed):
    """Create genuine rational words on a clock having the requested gcd."""
    p = P*sheets
    grades = []
    for t in range(p):
        r = (t*B) % P
        if 10*r < P:
            g = 0
        elif 20*r > 9*P:
            g = 1
        else:
            g = int((19*t + (t*t)//5 + 13*seed) % 23 < 10)
        grades.append(g)
    result = [(t+1)*B//P - t*B//P + grades[(t+1) % p] - grades[t]
              for t in range(p)]
    require(min(result) >= 1 and gcd(sum(result), p) == sheets, "native clock gcd")
    return result


def signed_step(tau):
    Q = abs(tau)
    numer, denom = (3**Q, 1) if tau > 0 else (1, 3**Q)
    k = floor_log2(numer, denom)
    a = Fraction(numer << max(-k, 0), denom << max(k, 0))
    lo, hi = 1, 2
    while a**hi <= 2:
        lo, hi = hi, 2*hi
    while hi-lo > 1:
        mid = (lo+hi)//2
        if a**mid <= 2:
            lo = mid
        else:
            hi = mid
    require(1 < a and a**lo < 2 < a**(lo+1), "exact signed grid step")
    return k, lo


def run(P, B, sheets, seed, tau, width):
    E, q, y = native_cycle(clock_word(P, B, sheets, seed))
    p, A, m0 = len(y), E[-1], min(y)
    require(3*m0 > max(y) and gcd(6, q) == 1, "complete sub-three cycle")
    k, N = signed_step(tau)
    def exponent(t):
        laps, i = divmod(t, p)
        return A*laps+E[i]
    def F(t):
        return exponent(t) + floor_log2(4*y[t % p], 7*m0)
    def tag(t, j):
        shift = exponent(t+j*tau)-F(t)-k*j
        require(shift in (0, 1), "exact synchronized tag")
        return 1 << shift
    def column(t, j):
        return tag(t,j)*y[(t+j*tau) % p]
    def phase_label(t):
        # qL = 7*m0/4; sorting the exact rational phases needs no logarithm.
        return column(t,0)
    anchor = min(range(p), key=phase_label)
    for t in range(-p, 2*p):
        require(F(t+p) == F(t)+A and 1 <= F(t+1)-F(t) <= 2, "winding")
        for j in range(width+1):
            lhs = (1 << (F(t+1)-F(t)))*column(t+1,j)
            require(lhs == 3*column(t,j)+q*tag(t,j), "linear column update")
            require(column(t,j) == column(t+p,j), "periodic column")
    def Y(r):
        pos = anchor+r*tau
        shift = exponent(pos)-F(anchor)-k*r
        return Fraction(y[pos % p] << max(shift,0), 1 << max(-shift,0))
    spatial = [Y(r) for r in range(N)]
    aligned = 0
    for r in range(N-width):
        t = anchor+r*tau
        if F(t) == F(anchor)+k*r:
            require(all(column(t,j) == spatial[r+j] for j in range(width+1)),
                    "matched interior equals the original integer sequence")
            aligned += 1
    tuples = list(combinations_with_replacement(range(width+1),6))
    signatures = [tuple(sorted(sum(column(t,j) for j in u) for u in tuples))
                  for t in range(p)]
    distinct_dates = sum(len(set(row)) == len(row) for row in signatures)
    require(distinct_dates == p, "finite genuine six-sum separation")
    # Witness an actual zero modulo the entire q and test propagation through
    # both the 2-adic and rational parts, regardless of coefficient mass.
    d01 = column(anchor,0)-column(anchor,1)
    d12 = column(anchor,1)-column(anchor,2)
    div = gcd(d01,d12)
    coeff = (d12//div, -(d12+d01)//div, d01//div)
    values = [sum(a*column(t,j) for j,a in enumerate(coeff)) for t in range(p)]
    require(values[anchor] == 0 and all(z % q == 0 for z in values),
            "genuine collision gives integers all around the actual circuit")
    require(any(values), "nontrivial colliding circuit")
    forced = 0
    for t,z in enumerate(values):
        if all(tag(t,j) == 2 for j in range(3)):
            require(z % (4*q) == 0, "forced-row four times complete denominator")
            forced += 1
    # Six binary sums agreeing on the selected windings imply physical
    # equality. The horizon is selected by exact integer doubling.
    horizon = 0
    while (1 << (F(anchor+horizon)-F(anchor))) <= 16*max(y):
        horizon += 1
    words = [tuple(tag(anchor+t,j)-1 for t in range(horizon)) for j in range(width+1)]
    codes = {tuple(sum(words[j][t] for j in u) for t in range(horizon)) for u in tuples}
    require(len(codes) == len(tuples), "sixfold code separation")
    return dict(primitive_odd_period=p, clock_gcd=gcd(A,p), division_sum=A,
                minimum_integer_part=m0//q,
                odd_width_millionths=(10**6*max(y))//m0, denominator_bits=q.bit_length(),
                signed_native_stride=tau, stride_mod_period=tau % p, grid_length=N,
                tested_offsets=width+1, exact_grid_matches=aligned,
                six_multisets=len(tuples), six_sum_distinct_dates=distinct_dates,
                source_code_edges=horizon, variable_code_rows=sum(len(set(row))>1
                for row in zip(*words)), collision_forced_divisibility_dates=forced)


if __name__ == "__main__":
    cases = [(41,65,1,0,-5,2), (41,65,2,1,-5,2), (41,65,3,2,-5,2),
             (306,485,1,0,12,3), (306,485,2,1,12,3),
             (306,485,3,2,-41,3)]
    print(json.dumps([run(*case) for case in cases], indent=2))
