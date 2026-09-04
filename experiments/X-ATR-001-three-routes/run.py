#!/usr/bin/env python3
"""Exact, bounded interface checks for the Astra three-route packet.

Standard library only. No test here certifies unrestricted Collatz convergence.
Use --write PATH to generate the frozen report; --check PATH to reproduce it.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

SCOPE = {
    "forward_limit_inclusive": 12289,
    "fan_target_limit_inclusive": 49153,
    "deep_h_max": 32,
    "deep_k_max": 24,
    "density_h_max": 32,
    "tile_count": 32,
    "tile_search_shortcut_cap": 128,
    "parametric_h_max": 32,
    "two_parameter_a_max": 8,
    "two_parameter_h_max": 16,
    "schur_targets": [10,13,19,22,28,37],
    "schur_depths": [0,2,4,8],
    "certificate_claim": "finite exact checks plus explicitly stated symbolic inequalities; not global coverage",
}


def vp(n: int, p: int) -> int:
    if n == 0 or p < 2:
        raise ValueError("valuation requires a nonzero integer and p >= 2")
    n = abs(n)
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def step(n: int) -> int:
    if n <= 0:
        raise ValueError("positive input required")
    return (3*n+1)//2 if n & 1 else n//2


def hard(n: int) -> bool:
    return n >= 4 and n % 3 == 1


def data(n: int) -> tuple[int, int, int]:
    if not hard(n):
        raise ValueError("hard state required")
    h = vp(2*n+1, 3)
    u = (2*n+1)//3**h
    k = vp(2**(h+1)*u-1, 3)
    return h, u, k


def rank(n: int) -> int:
    return (2*n+1)**2//3**vp(2*n+1, 3)


def weight(n: int) -> F:
    return F(1, rank(n))


def charge(n: int) -> F:
    h, _, k = data(n)
    return max(F(1), F(3**(h+k), 4**h))


def jump(n: int) -> tuple[int, int]:
    """First positive-time visit to H union {1}; exact unbounded-run formula."""
    if not hard(n):
        raise ValueError("hard state required")
    if n % 4 == 0:
        return n//4, 2
    if n & 1:
        a = vp(n+1, 2)
        u = (n+1)//2**a
        return (3**a*u-1)//2, a+1
    a = vp(n//2+1, 2)
    u = (n//2+1)//2**a
    return (3**a*u-1)//2, a+2


def fan(y: int) -> list[int]:
    h, u, _ = data(y)
    ans = [2*(2**j*3**(h-j)*u-1) for j in range(h)]
    last = 2**h*u-1
    if hard(last):
        ans.append(last)
    assert len(ans) == len(set(ans))
    return ans


def word_affine(bits: str) -> tuple[int, int, int]:
    """Return q,A,j for T_w(n)=(3**q*n+A)/2**j."""
    q = A = 0
    for j, b in enumerate(bits):
        if b not in "01":
            raise ValueError("binary word required")
        if b == "1":
            A = 3*A+2**j
            q += 1
    return q, A, len(bits)


def residue(bits: str) -> int:
    r = A = q = 0
    for j, b in enumerate(bits):
        x = (3**q*r+A)//2**j
        if (x & 1) != int(b):
            r += 2**j
        if b == "1":
            A = 3*A+2**j
            q += 1
    return r


def replay(n: int, bits: str) -> int:
    for b in bits:
        assert n % 2 == int(b)
        n = step(n)
    return n


def tile(n: int, bits: str) -> dict:
    y = replay(n, bits)
    assert hard(n) and (hard(y) or y == 1) and rank(y) < rank(n)
    q, A, j = word_affine(bits)
    h0, h1 = vp(2*n+1,3), vp(2*y+1,3)
    H = max(h0+1, h1+1-q)
    M = 2**j * 3**H
    B = 2*A+2**j-3**q
    assert B > 0
    # The theorem proves every t >= 0. These are interface samples only.
    for t in (0,1,2,17):
        x = n+M*t
        z = replay(x,bits)
        assert vp(2*x+1,3) == h0 and vp(2*z+1,3) == h1
        assert rank(z)*rank(n) <= rank(y)*rank(x)
    return {"source": n, "word": bits, "endpoint": y, "h_source": h0,
            "h_endpoint": h1, "modulus": M,
            "base_rank_ratio": [rank(y),rank(n)]}


def first_rank_drop(n: int, cap: int) -> tuple[str, int] | None:
    x, bits = n, ""
    for _ in range(cap):
        bits += str(x & 1)
        x = step(x)
        if (x == 1 or hard(x)) and rank(x) < rank(n):
            return bits, x
    return None


def digest(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def rational(x: F) -> list[int]:
    return [x.numerator, x.denominator]


def generate() -> dict:
    # These exact inequalities are also used in the symbolic all-parameter proofs.
    assert F(27,605) < F(1,20)
    assert F(1,20)+F(64,147) < F(1,2)
    assert 243 < 256
    assert F(2,3)+F(6561,131072) < F(3,4)
    assert F(2,3)+F(27,512) < F(3,4)
    assert 27 < 32

    stats: Counter = Counter()
    kernel_max = F()
    safe_max = F()
    for y in range(4,SCOPE["fan_target_limit_inclusive"]+1,3):
        xs = fan(y)
        h,u,k = data(y)
        B = 2**(h+1)*u-1
        bulk = sum((F(3,(2**(j+2)*3**(h-j)*u-3)**2)
                    for j in range(h-1)), F())
        boundary = F(1,3*B*B) if k == 0 else F(4*3**k,3*B*B)
        K = sum((weight(x) for x in xs), F())
        assert K == bulk+boundary
        assert K <= charge(y)*weight(y)/2
        for x in xs:
            assert jump(x)[0] == y
            assert rank(y) <= charge(y)*rank(x)/2
        stats["fan_targets"] += 1
        stats["fan_edges"] += len(xs)
        kernel_max = max(kernel_max,K/weight(y))
        if charge(y)==1:
            stats["nonresonant_fan_targets"] += 1
            safe_max=max(safe_max,K/weight(y))
        if K > weight(y):
            stats["pointwise_weight_expansion_targets"] += 1

    deep = set()
    for h in range(1,SCOPE["deep_h_max"]+1):
        for u in range(1,32,2):
            if u%3 and (3**h*u-1)//2>=4:
                deep.add((3**h*u-1)//2)
        for k in range(1,SCOPE["deep_k_max"]+1):
            m=3**k
            u=pow(2**(h+1),-1,m)
            if u%2==0:u+=m
            if (3**h*u-1)//2<4:u+=2*m
            deep.add((3**h*u-1)//2)
    for y in sorted(deep):
        assert sum((weight(x) for x in fan(y)),F()) <= charge(y)*weight(y)/2
    stats["deep_arithmetic_targets"]=len(deep)

    entry_r=(0,0); entry_t=(0,0)
    longest_drop=(0,0); unresolved=[]; tiles=[]
    jet_fixed=jet_boundary=0
    for n in range(4,SCOPE["forward_limit_inclusive"]+1,3):
        y,ell=jump(n)
        assert hard(y) or y==1
        assert n in fan(y) if y!=1 else n==4
        assert ell <= rank(n).bit_length()+1
        stats["forward_sources"]+=1
        if y==1 or charge(y)==1:stats["one_return_absorption_or_halving"]+=1
        elif rank(y)<rank(n):stats["resonant_but_rank_decreasing"]+=1
        else:stats["one_return_rank_nondecrease"]+=1

        x=n; r=clock=0
        while hard(x) and charge(x)==1:
            x,dt=jump(x);r+=1;clock+=dt
            assert r <= rank(n).bit_length()
        assert clock <= rank(n).bit_length()*(rank(n).bit_length()+1)
        if r>entry_r[0]:entry_r=(r,n)
        if clock>entry_t[0]:entry_t=(clock,n)

        # Exact source pressure on actual no-descent return prefixes.
        x=n; prod=F(1)
        for r in range(1,33):
            x,_=jump(x)
            if x==1 or x<n:break
            prod*=charge(x)
            assert F(2**r) <= data(n)[1]*prod
            stats["no_descent_pressure_prefixes"]+=1

        found=first_rank_drop(n,SCOPE["tile_search_shortcut_cap"])
        if found is None:
            unresolved.append(n)
        else:
            bits,z=found
            if len(bits)>longest_drop[0]:longest_drop=(len(bits),n)
            if y!=1 and rank(y)>=rank(n) and len(tiles)<SCOPE["tile_count"]:
                tiles.append(tile(n,bits))

        # Parity-word determination of endpoint ternary jets before the information boundary.
        x=n; A=q=0
        for j in range(1,33):
            bit=x&1
            if bit:A=3*A+2**(j-1);q+=1
            x=step(x)
            if hard(x):
                Z=2*A+2**j
                h=vp(Z,3)
                if h<q:
                    assert h==data(x)[0]
                    W=2**(h+1)*Z-3**h*2**j
                    if W and vp(W,3)<q:
                        k=vp(W,3)-h
                        assert k==data(x)[2]
                        jet_fixed+=1
                    else:jet_boundary+=1
                else:jet_boundary+=1
            if x==1:break

    assert len(tiles)==SCOPE["tile_count"]
    stats["fixed_endpoint_jet_pairs"]=jet_fixed
    stats["unfrozen_endpoint_jet_pairs"]=jet_boundary

    params=[]
    for h in range(2,SCOPE["parametric_h_max"]+1):
        bits="10010"+"10"*(2*h)
        r=residue(bits); L=len(bits); m=3**(h+1)
        s=(3**h-1)//2
        n=r+2**L*((s-r)*pow(2**L,-1,m)%m)
        if n<=1:n+=2**L*m
        y=replay(n,bits); first,_=jump(n)
        assert vp(2*n+1,3)==h and vp(2*y+1,3)==1
        assert rank(y)*4 < 3*rank(n)
        assert F(rank(first),rank(n)) > F(3**(h+1),16)
        params.append({"h":h,"source":n,"endpoint":y,
                       "first_return":first,
                       "final_rank_ratio":rational(F(rank(y),rank(n)))})

    two_parameter=[]
    for a in range(1,SCOPE["two_parameter_a_max"]+1):
        for h in range(2,SCOPE["two_parameter_h_max"]+1):
            b=2*(h+a)+3; bits="1"*a+"0"+"10"*b
            L=len(bits); r=residue(bits); mod=3**(h+1)
            t=(((3**h-1)//2-r)*pow(2**L,-1,mod))%mod
            n=r+2**L*t
            if n<=1:n+=2**L*mod
            y=replay(n,bits); first,_=jump(n)
            assert vp(n+1,2)==a and vp(2*n+1,3)==h
            assert vp(2*y+1,3)==1 and 4*rank(y)<3*rank(n)
            assert F(rank(first),rank(n))>F(3**(h+a),4**(a+1))
            if a>=2:assert first>n
            two_parameter.append([a,h,n,y,first])

    density_rows=[]; low=F()
    for h in range(1,SCOPE["density_h_max"]+1):
        k=0
        while 3**(h+k)<=4**h:k+=1
        low+=F(1,3**(h+k))
        density_rows.append([h,k])
    high=low+F(1,3**(SCOPE["density_h_max"]+1))

    budget_failures=[]
    for n,A0 in ((31,1),(121,4)):
        x=n; prod=F(1); trace=[n]
        for r in range(1,129):
            x,_=jump(x);trace.append(x)
            assert x!=1, "expected countertest must appear before termination"
            prod*=charge(x)
            normalized=prod/F(3,2)**r
            if normalized>rank(n)**A0:
                budget_failures.append({"source":n,"power":A0,"returns":r,
                    "trace":trace,"normalized_charge":rational(normalized),
                    "rank_power":rank(n)**A0})
                break
        else:raise AssertionError("missing budget countertest")

    schur=[]
    for target in SCOPE["schur_targets"]:
        assert charge(target)>1
        safe_row=sum((weight(x) for x in fan(target) if charge(x)==1),F())
        for L in SCOPE["schur_depths"]:
            current=[(x,1) for x in fan(target) if charge(x)==1]
            roots={x for x in fan(target) if charge(x)>1}
            while current:
                x,depth=current.pop()
                if depth>L:continue
                for z in fan(x):
                    if charge(z)>1:
                        assert z not in roots
                        roots.add(z)
                    else:current.append((z,depth+1))
            low_mass=sum((weight(x) for x in roots),F())
            high_mass=low_mass+safe_row/2**L
            schur.append({"target":target,"safe_interiors":L,
                "resolved_resonant_sources":len(roots),
                "lower_mass":rational(low_mass),"upper_mass":rational(high_mass)})

    payload={"scope":SCOPE,"statistics":dict(sorted(stats.items())),
        "kernel_ratio_max":rational(kernel_max),"nonresonant_ratio_max":rational(safe_max),
        "entry_max_returns_and_source":list(entry_r),
        "entry_max_shortcut_steps_and_source":list(entry_t),
        "rank_drop_pilot":{"max_steps_and_source":list(longest_drop),
            "unresolved_at_cap":unresolved,"scope":"finite source interval only"},
        "rank_spike":{"source":13,"endpoint":10,"ranks":[27,147]},
        "density":{"cutoffs":density_rows,"lower":rational(low),"upper":rational(high)},
        "tiles":tiles,"parametric_samples":params,"budget_countertests":budget_failures,
        "schur_intervals":schur,
        "two_parameter_family":{"cases":len(two_parameter),"sha256":digest(two_parameter)}}
    return {"payload":payload,"sha256":digest(payload)}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write",type=Path)
    group.add_argument("--check",type=Path)
    args=parser.parse_args()
    result=generate()
    if args.write:
        args.write.parent.mkdir(parents=True,exist_ok=True)
        args.write.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    else:
        if json.loads(args.check.read_text())!=result:
            raise SystemExit("FAIL: frozen report differs from exact regeneration")
    print(json.dumps({"sha256":result["sha256"],"statistics":result["payload"]["statistics"],
        "entry":result["payload"]["entry_max_returns_and_source"],
        "rank_drop":result["payload"]["rank_drop_pilot"]},sort_keys=True))

if __name__=="__main__":main()
