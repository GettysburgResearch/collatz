#!/usr/bin/env python3
"""Exact finite interfaces for the moving-ghost packet. Not a Collatz proof."""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path

SCHEMA = 'X-ASTRA3-004/v1'
SCOPE = 'finite interfaces and stated analytic tails; no global Collatz certificate'
LIMIT = 16384
FAN_CAP = 8192

def require(ok: bool, msg: str) -> None:
    if not ok:
        raise AssertionError(msg)

def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def valuation(n: int, p: int) -> int:
    if n == 0:
        raise ValueError('valuation at zero must be handled as a separate case')
    n = abs(n)
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k

def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def z(a: int, n: int) -> int:
    return 3**a * (n + 1) - 2**a * (2 * n + 1)

def rank_at(a: int, n: int) -> int:
    v = z(a, n)
    return v * v // 3**valuation(v, 3) if v else 0

@lru_cache(maxsize=None)
def rank(n: int) -> int:
    if n < 1:
        raise ValueError('positive source required')
    h = valuation(2 * n + 1, 3)
    return min(rank_at(a, n) for a in ({0, 1, 2, h} if h >= 3 else {0, 1, 2}))

def active(n: int) -> int:
    return 0 if n % 2 == 0 else valuation(n + 1, 2)

def accelerate(n: int) -> tuple[int, int, int]:
    if n == 1:
        return 1, 0, 0
    a = active(n)
    j = a + 1
    q, p = 3**a, 2**j
    d, c = q - p, q - 2**a
    zn = z(a, n)
    k = valuation(zn, 2) // j
    require(k >= 1, 'nonempty block')
    zy = q**k * (zn // p**k)
    require((zy - c) % d == 0, 'ordinary endpoint')
    return (zy - c) // d, a, k

def inverse(y: int, cap: int) -> list[list[int]]:
    """All A predecessors 2<=n<=cap. The even ray is cut only by cap."""
    if y <= 1:
        raise ValueError('the absorbing endpoint has different inverse semantics')
    rows: list[list[int]] = []
    if y % 2:
        n, k = 2 * y, 1
        while n <= cap:
            rows.append([n, 0, k])
            n *= 2
            k += 1
    h = valuation(2 * y + 1, 3)
    for a in range(1, h + 1):
        zy, j = z(a, y), a + 1
        if valuation(zy, 2) >= j:
            continue
        d, c = 3**a - 2**j, 3**a - 2**a
        for k in range(1, valuation(zy, 3) // a + 1):
            zn = 2**(j*k) * (zy // 3**(a*k))
            require((zn - c) % d == 0, 'inverse divisibility')
            n = (zn - c) // d
            if 2 <= n <= cap:
                rows.append([n, a, k])
    rows.sort()
    require(len(rows) == len({r[0] for r in rows}), 'duplicate inverse source')
    return rows

def fiber(m: int) -> list[int]:
    if m == 0:
        return [1]
    e = valuation(m, 3)
    Z = isqrt(m * 3**e)
    if Z * Z != m * 3**e:
        return []
    candidates = {Z, Z + 1, Z - 5}
    for a in range(3, e + 1):
        d, c = 3**a - 2**(a+1), 3**a - 2**a
        if (Z - c) % d == 0:
            candidates.add((Z - c) // d)
    return sorted(n for n in candidates if n >= 2 and rank(n) == m)

def family_source(a: int, k: int, t: int) -> int:
    """Exact v2(z_a)=(a+1)k and v3(z_a)=t, using ordinary CRT."""
    d, c = 3**a - 2**(a+1), 3**a - 2**a
    M, N = 2**((a+1)*k+1), 3**(t+1)
    r = ((M//2 - c) * pow(d, -1, M)) % M
    s = ((N//3 - c) * pow(d, -1, N)) % N
    r += M * (((s - r) * pow(M, -1, N)) % N)
    return r + M * N

def serialize_fraction(x: Fraction) -> list[int]:
    return [x.numerator, x.denominator]

def renewal_report() -> dict:
    # Exact a=2 identity: weighted occupation is zeta(2)/(64-lambda).
    H = 4096
    partial = sum((Fraction(1, m*m) for m in range(1, H+1)), Fraction())
    low = partial + Fraction(1, H+1)
    high = partial + Fraction(1, H)
    # Do not serialize huge common denominators: outward 10^-12 rationals.
    scale = 10**12
    rows = []
    for lam in (1, 2, 16, 32):
        lo, hi = low/(64-lam), high/(64-lam)
        rows.append([lam, lo.numerator*scale//lo.denominator,
                     (hi.numerator*scale + hi.denominator-1)//hi.denominator])
    progressions = []
    for k in range(1, 10):
        for m in range(1, 65):
            n = 8**k * m - 5
            y, a, kk = accelerate(n)
            require(a == 2 and kk >= k, 'corridor congruence')
            require(9**k * m - 5 > n, 'uphill shadow')
            require(Fraction(1, (n+5)**2) == Fraction(1, 64**k*m*m), 'exact source mass')
            progressions.append([k, m, n, kk])
    return dict(scale=scale, zeta_cutoff=H, occupation_intervals=rows,
                progression_cases=len(progressions), progression_digest=digest(progressions),
                lambda64_diverges=True, dictionary_upper=[8,189])

def arithmetic_report() -> dict:
    rows, aligned, uphill, raw_steps = [], 0, 0, 0
    labels = Counter()
    fibers_seen = set()
    for n in range(2, LIMIT+1):
        y, a, k = accelerate(n)
        x = n
        for bit in ([1]*a+[0])*k:
            require(x % 2 == bit, 'physical parity')
            x = shortcut(x)
        require(x == y and (y == 1 or active(y) != a), 'maximal exit')
        require(valuation(z(a, y), 2) < a+1, 'exit precision')
        require(rank_at(a,y)*2**(2*(a+1)*k) == rank_at(a,n)*3**(a*k), 'rank transport')
        require(rank(n) == min(rank_at(b,n) for b in range(21)), 'finite collapse comparison')
        require(n-1 <= rank(n) <= n*n, 'proper rank')
        require(y+5 <= (n+5)**3, 'height clock')
        require((a+1)*k <= 3*(n+4).bit_length(), 'integer time bound')
        is_aligned = rank_at(a,n) == rank(n)
        if is_aligned:
            aligned += 1
            require(4*rank(y) <= rank(n), 'common quarter contraction')
        uphill += int(y > n)
        raw_steps += (a+1)*k
        labels[a] += 1
        fibers_seen.add(rank(n))
        rows.append([n,y,a,k,rank(n),rank(y),is_aligned])
    fiber_rows = [[m,fiber(m)] for m in sorted(fibers_seen)]
    for n in range(2,LIMIT+1):
        require(n in fiber(rank(n)), 'fiber omission')
    for m,F in fiber_rows:
        require(len(F) <= max(3,valuation(m,3)+1), 'fiber size')
    return dict(limit=LIMIT,sources=LIMIT-1,raw_steps=raw_steps,aligned=aligned,
                uphill=uphill,labels=dict(sorted(labels.items())),digest=digest(rows),
                fibers=len(fiber_rows),fiber_digest=digest(fiber_rows))

def family_report() -> dict:
    rows = []
    for a in range(2,13):
        for k in (1,2,4,8):
            for extra in (4,7):
                t = 2*a+extra
                n = family_source(a,k,t)
                y,aa,kk = accelerate(n)
                require((aa,kk)==(a,k), 'CRT mode and length')
                require(valuation(z(a,n),3)==t and valuation(2*n+1,3)==a, 'CRT ternary depths')
                require(rank(n)==rank_at(a,n), 'aligned family')
                require(y>n and 4*rank(y)<rank(n), 'uphill common rank drop')
                require(all(rank_at(b,n)>rank(n) for b in range(a+9) if b!=a), 'unique sampled minimizer')
                rows.append([a,k,t,str(n),str(y),str(rank(n)),str(rank(y))])
    backward=[]
    for e in range(4,125,8):
        x=3**e;y=(9*x+7)//16
        require(accelerate(x)==(y,1,2),'power-family ordinary diagram')
        require(rank(x)==x and rank(y)==9*(x-1)**2//256,'power-family exact ranks')
        require(25*rank(x)<=9*rank(y),'uniform backward gain')
        backward.append([e,str(x),str(y),str(rank(x)),str(rank(y))])
    return dict(cases=len(rows),rows=rows,backward_cases=len(backward),backward_rows=backward)

def fan_report() -> dict:
    rows = []
    for y in range(2,129):
        got = inverse(y,FAN_CAP)
        expected = sorted([[n,*accelerate(n)[1:]] for n in range(2,FAN_CAP+1) if accelerate(n)[0]==y])
        require(got==expected, 'complete capped fan')
        for n,a,k in got:
            if a and a<valuation(2*y+1,3): require(k==1,'unique resonance column')
        rows.append([y,got])
    counts=Counter(); residual=[]; witnesses=[]
    for n in range(2,LIMIT+1):
        y,a,k=accelerate(n)
        if rank(y)<rank(n):
            counts['forward']+=1
        else:
            choices=[r for r in inverse(n,rank(n)) if rank(r[0])<rank(n)]
            if choices:
                counts['inverse_only']+=1
                r=min(choices,key=lambda r:(rank(r[0]),r[0]))
                witnesses.append([n,r[0],rank(n),rank(r[0]),r[1],r[2]])
            else:
                counts['residual']+=1;residual.append(n)
    return dict(cap=FAN_CAP,endpoints=127,edges=sum(len(r[1]) for r in rows),
                digest=digest(rows),local_limit=LIMIT,classification=dict(counts),
                residual_digest=digest(residual),first_residuals=residual[:32],
                inverse_digest=digest(witnesses),first_inverse=witnesses[:16])

def escape_report() -> dict:
    rows=[];resolved=0;residual=0;maxsteps=0;safe_inputs=0
    for start in range(2,LIMIT+1):
        n=start;rr=rank(n);bound=(rr.bit_length()-1)//2+1
        count=0;steps=0
        safe_inputs += int(4*rank(accelerate(n)[0]) <= rank(n))
        while n>1:
            y,a,k=accelerate(n)
            if 4*rank(y)>rank(n):
                break
            n=y;count+=1;steps+=(a+1)*k
            require(count<=bound,'quarter-drop termination bound')
        require(steps<=3*bound*(rr+5).bit_length(),'quarter-drop shortcut clock')
        if n==1:resolved+=1
        else:residual+=1
        maxsteps=max(maxsteps,steps)
        rows.append([start,n,count,steps])
    # Counterexamples are physical: the envelope is NOT a global rank.
    controls=[]
    for n in (3,7,9,15,27):
        y,a,k=accelerate(n)
        require(rank(y)>=rank(n),'failed global monotonicity')
        controls.append([n,y,rank(n),rank(y),a,k])
    return dict(sources=LIMIT-1,safe_inputs=safe_inputs,core=resolved,unsafe=residual,max_shortcut_steps=maxsteps,
                digest=digest(rows),controls=controls,tail_s2='2^(1-r), r>=1')

def build() -> dict:
    return dict(schema=SCHEMA,scope=SCOPE,renewal=renewal_report(),arithmetic=arithmetic_report(),
                families=family_report(),fans=fan_report(),escape=escape_report())

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    # JSON normalization makes in-memory and serialized key types identical.
    payload=json.loads(json.dumps(build()))
    result=dict(payload=payload,sha256=digest(payload))
    if args.check:
        require(json.loads(args.check.read_text())==result,'canonical mismatch')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
    print(result['sha256'])
    print('exact finite moving-ghost interfaces passed')

if __name__=='__main__':
    main()
