#!/usr/bin/env python3
"""Exact finite interfaces for the third PR #92 pass; never a global proof."""
import argparse
from fractions import Fraction as F
from hashlib import sha256
from math import gcd, isqrt, lcm
from pathlib import Path
import json

SCALE = 1 << 80
SCHEMA = 'X-ASTRA3-003/v1'
SCOPE = 'finite exact interfaces and all-source finite-time enclosures; no Collatz proof'


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()


def digest(obj):
    return sha256(canonical(obj)).hexdigest()


def T(n):
    return (3*n+1)//2 if n & 1 else n//2


def valuation(n, p):
    if n == 0:
        raise ValueError('zero valuation is not a finite feature')
    n = abs(n); k = 0
    while n % p == 0:
        n //= p; k += 1
    return k


def wt(n):
    v = isqrt(SCALE*SCALE//(n*n*n))
    return v, v+1


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def sub(x, y):
    return x[0]-y[1], x[1]-y[0]


def ap_mass(a, step, terms=64):
    lo = hi = 0
    for j in range(terms):
        l, h = wt(a+step*j); lo += l; hi += h
    z = a+step*terms
    v = isqrt(4*SCALE*SCALE//(step*step*z))
    lo += v; hi += v+1+wt(z)[1]
    return lo, hi


def defect3(a, step, color, terms=16):
    """Enclose THREE times the signed infinite residue defect."""
    f = [wt(a+step*j) for j in range(3*terms+2)]
    d = [sub(f[j], f[j+1]) for j in range(3*terms+1)]
    out = f[0] if color == 0 else (sub((0, 0), f[0]) if color == 2 else (0, 0))
    for j in range(terms):
        v = sub(d[3*j], d[3*j+2]) if color == 0 else (
            sub(d[3*j], d[3*j+1]) if color == 1 else sub(d[3*j+1], d[3*j+2]))
        out = add(out, v) if color == 0 else sub(out, v)
    tail = max(0, d[3*terms][1])
    out = add(out, (0, tail) if color == 0 else (-tail, 0))
    return out


def cylinders(k, H):
    # (canonical residue, odd multiplier, affine constant, strict source floor)
    rows = [(0, 1, 0, F(H))]
    for depth in range(k):
        P = 1 << depth; new = []
        for r, Q, A, low in rows:
            endpoint = (Q*r+A)//P
            for bit in (0, 1):
                rr = r+((bit-endpoint) % 2)*P
                qq = 3*Q if bit else Q
                aa = 3*A+P if bit else A
                bound = max(low, F(2*P*H-aa, qq))
                new.append((rr, qq, aa, bound))
        rows = new
    mod = 1 << k
    return sorted((r, r+mod*((low-r)//mod+1)) for r, Q, A, low in rows)


def boundary_report():
    out = []; root_data = []; cases = 0; checks = 0
    for H in (64, 4096):
        for k in range(13):
            mod = 1 << k; rows = cylinders(k, H)
            mass = (0, 0); qmass = (0, 0); delta = (0, 0); guard = (0, 0)
            B = [(0, 0)]*3; V = (0, 0); counts = [0]*3
            for r, a in rows:
                root_data.append([H, k, r, a]); cases += 1
                j = ((2-a)*pow(mod, -1, 3)) % 3
                counts[j] += 1; B[j] = add(B[j], wt(a))
                if j == 0:
                    V = add(V, sub(wt(a), wt(a+mod)))
                mass = add(mass, ap_mass(a, mod))
                delta = add(delta, defect3(a, mod, j))
                b = a+j*mod
                while (2*b-1)//3 <= H:
                    guard = add(guard, wt(b)); b += 3*mod
                qmass = add(qmass, ap_mass(b, 3*mod))
                # Root and three successors are physically surviving; preceding
                # positive lift is not. Finite checks, separate from the proof.
                for n in [a, a+mod, a+2*mod, a+3*mod]:
                    y = n
                    for _ in range(k):
                        assert y > H; y = T(y)
                    assert y > H; checks += 1
                if a-mod > 0:
                    y = a-mod; survives = y > H
                    for _ in range(k):
                        y = T(y); survives &= y > H
                    assert not survives
            root_majorant = sub(add(sub(B[0], B[2]), V), (3*guard[0], 3*guard[1]))
            # Independent direct AP enclosures overlap the exact signed identity.
            signed_q3 = add(mass, sub(delta, (3*guard[0], 3*guard[1])))
            assert max(signed_q3[0], 3*qmass[0]) <= min(signed_q3[1], 3*qmass[1])
            out.append(dict(H=H, k=k, colors=counts, M=list(mass), Q=list(qmass),
                defect3=list(delta), guard=list(guard), B0=list(B[0]),
                signed_majorant3=list(root_majorant),
                positive_certificate=400*B[0][1] <= 7*mass[0],
                root_certificate=200*root_majorant[1] <= 7*mass[0],
                signed_certificate=200*delta[1]-600*guard[0] <= 7*mass[0],
                direct_certificate=200*qmass[1] <= 69*mass[0]))
    return dict(scale=SCALE, ap_terms=64, curvature_terms=16, rows=out,
                cylinders=cases, physical_lifts=checks, root_digest=digest(root_data))


def simple_path(n, limit):
    seq = []; seen = set()
    while n not in seen and len(seq) <= limit:
        seq.append(n); seen.add(n); n = T(n)
    return seq


def record_report():
    logs = []; paths = []; positions = 0
    starts = list(range(1, 513))+[(1 << a)-1 for a in range(3, 16)]
    for n in starts:
        path = simple_path(n, 160)
        odd = sorted(x for x in path if x & 1)
        # Exact integer test of the uniform 5 X^(39/40) count at every jump.
        for count, x in enumerate(odd, 1):
            assert count**40 <= 5**40*x**39
        paths.append([n, path])
        # No-descent subsegments starting at a running tail minimum.
        for start in range(min(len(path), 12)):
            x0 = path[start]; seg = []
            for x in path[start:]:
                if x < x0:
                    break
                seg.append(x)
            C = F(1); P = F(1); minimum = C; rec = [0]
            for i, x in enumerate(seg[:-1]):
                if x & 1:
                    C *= F(3, 2); P *= F(3*x+1, 3*x)
                else:
                    C /= 2
                assert F(seg[i+1]) == x0*C*P
                if C < minimum:
                    minimum = C; rec.append(i+1)
                positions += 1
            cap = (x0*P).numerator//(x0*P).denominator
            assert all(x0 <= seg[t] <= cap for t in rec)
            assert len(rec) <= cap-x0+1
            gaps = [b-a for a, b in zip(rec, rec[1:])]+[len(seg)-1-rec[-1]]
            L = len(seg)-1
            R = cap-x0+1
            assert max(gaps, default=0) >= (L+R-1)//R
            for a, b in zip(rec, rec[1:]):
                c = F(1)
                for j in range(a, b):
                    c *= F(3 if seg[j] & 1 else 1, 2)
                    assert (c >= 1) if j+1 < b else (c < 1)
            logs.append([n, start, len(seg), cap, rec, P.numerator, P.denominator])
    # Exact finite core certificate; no external range imported.
    core = []
    for n in range(1, 65):
        y = n; steps = 0
        while y != 1:
            y = T(y); steps += 1
            assert steps < 1000
        core.append(steps)
    return dict(source_count=len(starts), path_digest=digest(paths),
                records_digest=digest(logs), segments=len(logs), positions=positions,
                core=core, integer_inequalities=[8*3125**24 < 3456**24,
                    200*11 < 69*32, 200*65 < 69*192, 3**200 < 2**317,
                    317**6340 < 2**6023*117**2340*200**4000,
                    8*177**2 > 500**2, 463**2*65**3 > 250**2*98**3, 49647 < 49650])


# Coefficients are low-degree first. Polynomial roots from earlier negative
# shadows are included deliberately in the third dictionary.
DICTIONARIES = [
    dict(mod=8, features=[(2,[0,1]),(2,[1,1]),(3,[0,1]),(3,[1,1])]),
    dict(mod=35, features=[(2,[1,0,1]),(3,[0,1,1]),(5,[1,3]),(7,[-1,0,1])]),
    dict(mod=105, features=[(p,[-(3**a-2**a), 2**(a+1)-3**a])
        for a in range(2,9) for p in (2,3,5,7)]+[(2,[1,1]),(3,[1,2])])]


def poly(c, x):
    ans = 0
    for a in reversed(c):
        ans = ans*x+a
    return ans


def factors(n):
    out = []; p = 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def setup(dictionary):
    primes = sorted(set([2,3]+factors(dictionary['mod'])+[p for p,c in dictionary['features']]))
    period = lcm(*(p-1 for p in primes if p > 3)) if any(p>3 for p in primes) else 1
    a = ((2+period-1)//period)*period
    while True:
        alpha = F(3**a-2**a, 2**(a+1)-3**a)
        if all(poly(c,alpha) != 0 for p,c in dictionary['features']):
            break
        a += period
    powers = {p:max(1, valuation(dictionary['mod'],p)) for p in primes}
    for p,c in dictionary['features']:
        z = poly(c,alpha)
        assert z.denominator % p
        powers[p] = max(powers[p], valuation(z.numerator,p)+1)
    return a, alpha, powers


def feature(n, dictionary):
    return [valuation(poly(c,n),p) for p,c in dictionary['features']]+[n%dictionary['mod']]


def shadow_report():
    rows = []; total_packets = 0; adaptive_blocks = 0
    for d, dictionary in enumerate(DICTIONARIES):
        a, alpha, powers = setup(dictionary)
        for K in (1,2,4,8,16,32):
            modulus = 1
            for p,e in powers.items():
                modulus *= p**(e+((a+1)*K if p == 2 else 0))
            r = (alpha.numerator*pow(alpha.denominator,-1,modulus))%modulus
            n = modulus+r; x = n; observed = feature(n,dictionary); endpoints = [n]
            for _ in range(K):
                assert valuation(x+1,2) == a
                u = (x+1)//(1<<a)
                assert valuation(3**a*u-1,2) == 1
                x = (3**a*u-1)//2
                assert feature(x,dictionary) == observed
                endpoints.append(x); total_packets += 1
            assert F(x) == alpha+F(3**a,1<<(a+1))**K*(n-alpha)
            assert x*(1<<((a+1)*K)) > n*3**(a*K)
            # An arbitrary nonlinear JOINT score cancels, not just each profile.
            score = lambda z: (sum((j+1)*v for j,v in enumerate(z))**3
                                  + sum(z[i]*z[j] for i in range(len(z)) for j in range(i)))
            assert score(feature(x,dictionary)) == score(observed)
            # Bounded total selectors: inspect full integer, not only features.
            for B in (1,2,3):
                index = 0
                while index < max(0, K-3):
                    step = 1+(endpoints[index]//17)%B
                    index += step; adaptive_blocks += 1
                    assert feature(endpoints[index],dictionary) == observed
            rows.append(dict(dictionary=d,a=a,K=K,source=str(n),endpoint=str(x),
                             feature=observed,modulus=str(modulus)))
    return dict(dictionaries=DICTIONARIES,rows=rows,packets=total_packets,
                adaptive_blocks=adaptive_blocks,sha256=digest(rows))


def build():
    return dict(schema=SCHEMA,scope=SCOPE,boundary=boundary_report(),
                records=record_report(),shadows=shadow_report())


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--output',type=Path)
    ap.add_argument('--check',type=Path); args = ap.parse_args()
    payload = build(); report = dict(payload=payload,sha256=digest(payload))
    if args.check:
        assert json.loads(args.check.read_text()) == report, 'canonical mismatch'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n')
    print(report['sha256']); print('three finite interfaces passed')

if __name__ == '__main__':
    main()
