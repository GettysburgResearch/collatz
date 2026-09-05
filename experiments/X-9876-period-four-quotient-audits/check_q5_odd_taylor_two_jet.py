#!/usr/bin/env python3
"""Independent finite audit for q5_odd_taylor_two_jet_theorem.md.

Standard library only.  The exact normalized-jet engine is imported from the
companion scanner; all theorem-specific formulas and comparisons are repeated
here rather than trusted from the note.
"""

from fractions import Fraction as Fr

from scan_q5_normalized_jets import V, f_jet, primes, q5_normalized_jet


def unitfac_table(n, p):
    z = [1] * (n + 1)
    for i in range(1, n + 1):
        a = i
        while a % p == 0:
            a //= p
        z[i] = z[i-1] * (a % p) % p
    return z


def leading(u, b, p, uf):
    z = (-1 if b & 1 else 1) * pow(2, u-b, p)
    z = z * uf[2*u+1] * uf[b] * uf[b] % p
    den = uf[u] * uf[u-b] * uf[2*b+1] % p
    return z * pow(den, -1, p) % p


def alpha(n, p):
    return sum((i-1) * pow(2, -1, p) for i in range(1, n+1) if i % p) % p


def beta(N, b, p):
    return (16*b*b + 16*b + 8*b*N + 5*N + 3*N*N) * pow(8, -1, p) % p


def theta(N, b, p):
    half = pow(2, -1, p)
    d = (2*b + 1 + N*half) % p
    e = 2*b*(b+1) % p
    num = N*(8*N*N - 9*N - 17 + 24*d*d + 24*d*N - 48*d) - 96*e
    return num * pow(192, -1, p) % p


def check_tropical():
    count = 0
    for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        cap = 500
        h1 = (p-1)//2
        h2 = (p*p-1)//2
        for u in range(cap + 1):
            vals = [V(u, b, p) for b in range(u + 1)]
            m = min(vals)
            bs = [b for b, z in enumerate(vals) if z == m]
            allowed = {0}
            if h1 <= u:
                allowed.add(h1)
            if h2 <= u:
                allowed.add(h2)
            assert all(b in allowed for b in bs), (p, u, bs)
            assert len(bs) <= 2, (p, u, bs)
            if len(bs) == 2:
                assert bs == [0, h2], (p, u, bs)
            if h2 <= u:
                R, s = (u // p) % p, u % p
                tied = vals[0] == vals[h2] == m
                assert tied == (R >= (p+1)//2 and s < (p-1)//2), (p, u, R, s, bs)
            count += u + 1
    print("PASS three-central minimizers/tie digits in", count, "block states")


def check_leading_ratio():
    count = 0
    for p in primes(61):
        a = (p-1)//2
        h = (p*p-1)//2
        cap = min(2*p*p, 8000)
        uf = unitfac_table(2*cap+1, p)
        for R in range(a+1, p):
            for s in range(a):
                u = p*R+s
                if u > cap:
                    continue
                t = R-a-1
                got = leading(u, h, p, uf) * pow(leading(u, 0, p, uf), -1, p) % p
                num = (-1 if (a+1) & 1 else 1)
                num *= pow(1, 1, p)
                # (t+a+1)! s! / (t! (s+a+1)!)
                facts = [1]
                for i in range(1, p):
                    facts.append(facts[-1]*i % p)
                want = num * facts[t+a+1] * facts[s] % p
                want = want * pow(facts[t]*facts[s+a+1] % p, -1, p) % p
                assert got == want, (p, u, got, want)
                count += 1
    print("PASS exact tied leading-unit ratio in", count, "digit states")


def check_f_jets():
    count = 0
    for p in [11, 13, 17, 29]:
        inv2 = pow(2, -1, p)
        for N in range(p):
            for b in range(p):
                z = f_jet(N, b, p, 2)
                z0i = pow(z[0], -1, p)
                first = z[1] * z0i % p
                log2 = (z[2]*z0i - first*first*inv2) % p
                assert first == beta(N, b, p), (p, N, b, first, beta(N,b,p))
                assert log2 == theta(N, b, p), (p, N, b, log2, theta(N,b,p))
                count += 1
    print("PASS beta/theta against exact Rogers--Szego jets in", count, "states")


def check_rational_ledger():
    # Polynomials are coefficient lists, low degree first.
    def add(a, b):
        z = [Fr(0)] * max(len(a), len(b))
        for i, q in enumerate(a): z[i] += q
        for i, q in enumerate(b): z[i] += q
        return z
    def mul(a, b):
        z = [Fr(0)] * (len(a)+len(b)-1)
        for i, q in enumerate(a):
            for j, r in enumerate(b): z[i+j] += q*r
        return z
    def scale(a, c): return [c*q for q in a]

    G = [Fr(5,32), Fr(12,32)]
    r1 = [0, Fr(-1,12)]
    rp1 = [Fr(1,32), Fr(2,32)]
    d0 = [Fr(3,4), Fr(3,4)]
    dh = [Fr(1,8), Fr(6,8)]
    r2 = [0, Fr(-1,120), Fr(1,120)]
    rp2 = [Fr(3,2048), 0, Fr(-12,2048)]
    Lam = [Fr(-45,384), Fr(-57,384), Fr(26,384)]
    c1 = add(add(G, r1), rp1)
    assert c1 == [Fr(9,48), Fr(17,48)]
    c2 = Lam
    for z in [scale(mul(G,G), Fr(-1,2)), scale(mul(rp1,G), -1),
              mul(r1,d0), mul(rp1,dh), r2, rp2]:
        c2 = add(c2, z)
    assert c2 == [Fr(-990,7680), Fr(-2059,7680), Fr(-301,7680)]
    s = Fr(-9,17)
    value = c2[0] + c2[1]*s + c2[2]*s*s
    assert value == Fr(189, 320*17*17), value
    print("PASS exact first/second-jet rational ledger")


def check_exact_witnesses():
    # Includes no cancellation, one-jet cancellation, and every known
    # two-jet prime family <=101 (one representative digit state each).
    jobs = [
        (6, 3, 0),       # p=3 tied tropical state, leaders survive
        (15, 5, 1),      # leaders cancel, first jet survives
        (105, 13, 2),
        (675, 29, 2),
        (931, 37, 2),
        (2949, 61, 2),
        (4456, 79, 2),
        (7497, 97, 2),
        (9945, 101, 2),
    ]
    for u, p, expected in jobs:
        m, first, coeffs, relevant, vals = q5_normalized_jet(u, p, 3)
        assert first == expected, (u, p, m, first, coeffs, relevant)
        assert m <= V(u, 0, p)
        assert m + first <= 2*V(u, 0, p) + 1
    print("PASS exact normalized block jets in", len(jobs), "targeted witnesses")


def poly_add(a, b):
    z = [0] * max(len(a), len(b))
    for i, c in enumerate(a): z[i] += c
    for i, c in enumerate(b): z[i] += c
    while len(z) > 1 and z[-1] == 0: z.pop()
    return z


def poly_mul(a, b):
    z = [0] * (len(a)+len(b)-1)
    for i, c in enumerate(a):
        for j, d in enumerate(b): z[i+j] += c*d
    while len(z) > 1 and z[-1] == 0: z.pop()
    return z


def poly_shift_scale(a, n, c):
    return [0]*n + [c*z for z in a]


def poly_exact_div(a, b):
    a = a[:]
    while len(a) > 1 and a[-1] == 0: a.pop()
    q = [0] * max(1, len(a)-len(b)+1)
    while len(a) >= len(b) and not (len(a) == 1 and a[0] == 0):
        d = len(a)-len(b)
        assert a[-1] % b[-1] == 0
        c = a[-1] // b[-1]
        q[d] += c
        for i, z in enumerate(b): a[d+i] -= c*z
        while len(a) > 1 and a[-1] == 0: a.pop()
    assert all(z == 0 for z in a)
    while len(q) > 1 and q[-1] == 0: q.pop()
    return q


def qbin_row(n):
    row = [[1]]
    for m in range(1, n+1):
        nxt = [[1]] + [None]*(m-1) + [[1]]
        for k in range(1, m):
            nxt[k] = poly_add(row[k], poly_shift_scale(row[k-1], m-k, 1))
        row = nxt
    return row


def poch(n):
    z = [1]
    for i in range(1, n+1): z = poly_mul(z, [1] + [0]*(i-1) + [-1])
    return z


def full_q5(u):
    row = qbin_row(2*u+1)
    z = [0]
    for j in range(u+1):
        c = (2*j+1) * (-1 if j & 1 else 1)
        z = poly_add(z, poly_shift_scale(row[u-j], 5*j*(j+1)//2, c))
    return poly_exact_div(z, poch(u))


def full_taylor_order(poly, p):
    # Horner substitution q=1+x over F_p.
    z = [0]
    for c in reversed(poly):
        nxt = [0] * (len(z)+1)
        for i, a in enumerate(z):
            nxt[i] = (nxt[i] + a) % p
            nxt[i+1] = (nxt[i+1] + a) % p
        nxt[0] = (nxt[0] + c) % p
        z = nxt
    return next((i for i, c in enumerate(z) if c % p), None)


def check_full_q_small():
    count = 0
    for u in range(13):
        q = full_q5(u)
        assert len(q)-1 == 2*u*(u+1)
        for p in primes(31):
            got = full_taylor_order(q, p)
            vals = [V(u, b, p) for b in range(u+1)]
            assert got is not None and got <= min(vals)+2, (u, p, got, min(vals))
            assert got <= 2*V(u, 0, p)+1, (u, p, got, V(u,0,p))
            count += 1
    print("PASS independent full-Q Taylor audit in", count, "(u,p) states")


if __name__ == "__main__":
    check_tropical()
    check_leading_ratio()
    check_f_jets()
    check_rational_ledger()
    check_exact_witnesses()
    check_full_q_small()
    print("PASS odd-prime Taylor two-jet theorem audit")


