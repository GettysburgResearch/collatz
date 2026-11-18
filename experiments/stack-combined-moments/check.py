"""Exact component checks for the combined-moment argument, including a finite kernel."""
from fractions import Fraction as F
from math import gcd


def exponents(word, m, count):
    out = [0]
    for i in range(count):
        m += word[i % len(word)]
        out.append(out[-1] + 9*m + 1)
    return out


def determinant(matrix):
    """Bareiss elimination on a small square integer matrix."""
    m = [row[:] for row in matrix]
    sign = old = 1
    for i in range(len(m)-1):
        if not m[i][i]:
            for k in range(i+1, len(m)):
                if m[k][i]:
                    m[k], m[i] = m[i], m[k]
                    sign = -sign
                    break
            else:
                return 0
        pivot = m[i][i]
        for j in range(i+1, len(m)):
            for k in range(i+1, len(m)):
                m[j][k] = (m[j][k]*pivot-m[j][i]*m[i][k]) // old
        old = pivot
    return sign*m[-1][-1]


def finite_kernel(word, m):
    n, D, M = 5, 6, 6
    mu, a = M+F(n, 2), F(9*sum(word), len(word))
    g = [(a*(mu*k-F(k*k, 2)))//1 for k in range(D+1)]
    E = exponents(word, m, M+n+1)
    rows = []
    for j in range(M, M+n):
        powers = [g[k]+E[j-k] for k in range(D+1)]
        lo, hi = min(powers), max(powers)
        rows.append([64**(e-lo)*81**(hi-e) for e in powers])
    # Cofactors on the first n+1 columns, independent of the pigeonhole proof.
    v = [(-1)**i * determinant([row[:i]+row[i+1:n+1] for row in rows])
         for i in range(n+1)] + [0]
    common = gcd(*v)
    assert common
    v = [x//common for x in v]
    assert all(sum(x*y for x, y in zip(v, row)) == 0 for row in rows)
    # Test the two prime minimizer paths on the literal integer kernel.
    for prime, factor, order in ((2, 6, range(M, M+n)), (3, -4, reversed(range(M, M+n)))):
        valuations = {}
        for k, coefficient in enumerate(v):
            if coefficient:
                value, multiplicity = abs(coefficient), 0
                while value % prime == 0:
                    multiplicity += 1
                    value //= prime
                valuations[k] = multiplicity
        previous = min(valuations)
        for j in order:
            costs = {k: val + factor*(g[k]+E[j-k]) for k, val in valuations.items()}
            low = min(costs.values())
            winners = sorted(k for k, val in costs.items() if val == low)
            assert len(winners) >= 2 and winners[0] >= previous
            previous = winners[-1]


def main():
    d, u = F(6, 5), F(3, 2)
    assert 64**93 > 81**88 and 64**19 < 81**18
    endpoints = (F(46, 5), F(156, 5))
    p_margins = [F(88, 93)*((s+d+1)**2/2-d/2) -
                 ((s+d)**2/2+d/2+u) for s in endpoints]
    s = endpoints[0]
    assert p_margins == [F(1469, 310), F(227, 930)]
    assert (s*s/2 - (d+F(1, 2)+s)*d + d*d/2)/19-u == F(73, 950)
    assert (endpoints[1]-endpoints[0])/18 > d
    assert 81**94639 < 64**100000 < 81**94640
    rho, delta, d = F(94639, 100000), F(536, 10000), F(5)
    u = d/(4*(d-1))
    v = u-(1+rho)/8
    lo, hi = F(1), F(243,10)
    for s in lo, hi:
        assert rho*((s+d+1)**2/2-d/2) > (s+d)**2/2+d/2+u
    assert delta*(lo+1)**2/2 > v
    assert delta*(hi-lo)*((hi+lo)/2+F(1,2))/v > F(23731,100)
    for r in range(1, 19):
        word = [1 + ((j*j+3*j+1) % 5) for j in range(r)]
        E = exponents(word, 2, 4*r+51)
        a = F(9*sum(word), r)
        for s in (r, 2*r, 3*r, 4*r):
            assert all(E[s+j] == E[s]+a*s*j+E[j] for j in range(51))
        if r in (1, 10, 18):
            finite_kernel(word, 2)
    print("3672 exact shift identities, three integer kernels, six prime minimizer paths and period-237 margins checked")


if __name__ == "__main__":
    main()
