"""Exact finite controls for the discrepancy-mask and Fourier-divisor formulas."""
from functools import cache
from itertools import product
from math import gcd


def require(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def poly_remainder(coefficients, divisor):
    work = list(coefficients)
    while work and work[-1] == 0:
        work.pop()
    while len(work) >= len(divisor):
        shift = len(work) - len(divisor)
        scale = work[-1]
        for j, entry in enumerate(divisor):
            work[j + shift] -= scale * entry
        while work and work[-1] == 0:
            work.pop()
    return work


@cache
def cyclotomic(m):
    # Divide X^m - 1 by the previously constructed monic factors.
    coeffs = [-1] + [0] * (m-1) + [1]
    for h in range(1, m):
        if m % h:
            continue
        factor = cyclotomic(h)
        quotient = [0] * (len(coeffs) - len(factor) + 1)
        for shift in reversed(range(len(quotient))):
            scale = coeffs[shift + len(factor) - 1]
            quotient[shift] = scale
            for j, c in enumerate(factor):
                coeffs[shift+j] -= scale * c
        require(not any(coeffs), (m, h))
        coeffs = quotient
    return tuple(coeffs)


def mask_controls(gaps):
    p, A = len(gaps), sum(gaps)
    if gcd(p, A) != 1:
        return 0
    D = abs(2**A - 3**p)
    if D == 1:
        return 0
    E = 0
    C = 0
    levels = []
    for i, e in enumerate(gaps):
        levels.append(p*E - A*i)
        C = 3*C + 2**E
        E += e
    K = -min(levels)
    v = pow(A, -1, p) if p > 1 else 0
    u = (1 - A*v)//p
    z = pow(2, u, D) * pow(3, v, D) % D
    require(pow(z, p, D) == 2 % D and pow(z, A, D) == 3 % D, gaps)
    mz = sum(pow(z, K+s, D) for s in levels) % D
    require((3**(p-1)*mz - pow(z, K, D)*C) % D == 0, gaps)
    require(gcd(mz, D) == gcd(C, D), gaps)
    # Test the unoptimized resultant bound (2a) on the entire quotient Q.
    degree = max(levels) + K - p + 1
    if degree:
        for f in range(1, p+1):
            e = -((A*f + p//2)//p)
            signed = p*e+A*f
            a, b = 3**f, 2**(-e)
            upper_square = (2*max(a, b))**(2*degree) * p**abs(signed)
            require(gcd(D, C)**2 <= upper_square, (gaps, f))
    return 1


def gaps_from_levels(levels, p, A):
    table = {s % p: s for s in levels}
    require(len(table) == p, (p, A, len(table)))
    placed = [table[-i*A % p] for i in range(p+1)]
    gaps = [(A+t-s)//p for s, t in zip(placed, placed[1:])]
    require(min(gaps) >= 1 and sum(gaps) == A, (p,A,gaps))
    return gaps


def cancelled(gaps):
    E = C = 0
    for e in gaps:
        C = 3*C + 2**E
        E += e
    return gcd(C, 2**E - 3**len(gaps))


def active_component_controls(g, u, v, c, delta):
    checked = partial = 0
    H = (u**g - v**g)//(u-v)
    for js in product((0, 1), repeat=g):
        K = sum(js)
        if K in (0, g):
            continue
        n, active = 0, 1
        for m in range(2, g+1):
            if g % m:
                continue
            phi = cyclotomic(m)
            if not poly_remainder(js, phi):
                continue
            degree = len(phi)-1
            n += degree
            active *= sum(a*u**j*v**(degree-j) for j, a in enumerate(phi))
        C = sum((c+delta*j)*u**i*v**(g-1-i) for i, j in enumerate(js))
        d = (u**g-v**g)//gcd(u**g-v**g, C)
        require(n > 0 and H % active == 0 and active*2**n >= u**n, (js, n))
        require((d*gcd(active, delta))**2*(K*(g-K))**n >= active**2*n**n, js)
        primitive = all(any(js[i] != js[(i+h) % g] for i in range(g))
                        for h in range(1, g) if g % h == 0)
        require(not primitive or g <= 2**(n+1), js)
        partial += int(n < g-1)
        checked += 1
    return checked, partial


def main():
    masks = sum(mask_controls(word) for p in range(1, 8)
                for word in product(range(1, 4), repeat=p))
    families = 0
    for p in range(3, 56, 2):
        for A in range(p+2, 2*p, 2):
            if gcd(p, A) == 1:
                gaps = gaps_from_levels(range(0, 2*p, 2), p, A)
                require(set(gaps) == {1, 3} and cancelled(gaps) == 1, (p, A))
                families += 1
    for j in range(3, 9):
        p = 2**j
        A = 3*p//2 + 1
        for small in product((1, 3), repeat=j-2):
            levels = [0]
            for h, coefficient in enumerate(small+(1, 1)):
                levels += [s + coefficient*2**h for s in levels]
            gaps = gaps_from_levels(levels, p, A)
            require(7 % cancelled(gaps) == 0, (j, small))
            families += 1
    total = partial = 0
    # Same-clock legal odd words (1,4),(4,1) give u=32,v=9,c=5,delta=14.
    for g in range(2, 11):
        n, m = active_component_controls(g, 32, 9, 5, 14)
        total += n
        partial += m
    print(f"coprime composite-modulus controls: {masks}; torsion masks: {families}")
    print(f"block selectors: {total}; with inactive nontrivial frequencies: {partial}")


if __name__ == "__main__":
    main()
