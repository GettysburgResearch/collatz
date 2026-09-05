#!/usr/bin/env python3
"""Exact finite support for the unbounded-run renewal packet.

No all-time conclusion is inferred. All-source bounds use the analytic tail
in RUN_RENEWAL.md. Only the standard library is needed.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path

SCHEMA = "astra-run-renewal-v1"
H = 1 << 18
J = 24
BITS = 96
LAMBDA = Q(9, 8)
PRESSURE_UPPER = Q(173, 200)
TAIL = Q(1, 1 << 120)


def ceil_q(x: Q) -> int:
    return -(-x.numerator // x.denominator)


def packet(n: int) -> tuple[int, int, int]:
    if n < 1 or n % 2 != 1:
        raise ValueError("packet domain is positive odd integers")
    a = ((n + 1) & -(n + 1)).bit_length() - 1
    m = (n + 1) >> a
    z = 3**a * m - 1
    b = (z & -z).bit_length() - 1
    return z >> b, a, b


def pressure_certificate() -> dict:
    # Rational enclosures, checked by squaring, not floating point.
    s2lo, s2hi = Q(1414213562373, 10**12), Q(1414213562374, 10**12)
    s3lo, s3hi = Q(1732050807568, 10**12), Q(1732050807569, 10**12)
    assert s2lo*s2lo < 2 < s2hi*s2hi
    assert s3lo*s3lo < 3 < s3hi*s3hi
    upper = s3hi / ((2*s2lo-s3hi)*(2*s2lo-1))
    assert upper < PRESSURE_UPPER
    return {"sqrt2": [str(s2lo), str(s2hi)],
            "sqrt3": [str(s3lo), str(s3hi)],
            "pressure_upper": str(upper), "simple_upper": str(PRESSURE_UPPER)}


def drift_bound(m: int, r: int) -> Q:
    X = 1 << m
    A = [ceil_q(Q(8, 5)**i * (m+2)) for i in range(r)]
    B = [ceil_q(Q(8, 5)**(i+1) * (m+2)) for i in range(r)]
    Ds, pref = [], 1
    for i in range(r+1):
        if i:
            pref *= A[i-1]*B[i-1]
        Ds.append(Q(pref)*Q(25, 2)**(r-i)*Q(5, 4)**sum(A[i:]))
    err = Q(2)*Ds[0]/X + Q(1, 1 << (m//2))*(
        sum(PRESSURE_UPPER**(r-i) for i in range(1, r+1))
        + Q(2)*sum(Ds[1:])/X)
    return LAMBDA**r*(PRESSURE_UPPER**r + err)


def cofinal_certificate() -> dict:
    rows = []
    for r, start, bound in [(1, 18, Q(99, 100)), (2, 128, Q(19, 20))]:
        for m in range(start, start+25):
            v = drift_bound(m, r)
            assert v < bound
            rows.append({"packets": r, "m": m, "upper": str(v), "target": str(bound)})
    # Twenty-five-step monotonicity of each nonnegative error term.
    factors = {
        "one_D0": Q(5, 4)**25 / 2**25,
        "one_D1": Q(9, 4)**2 / 2**37,
        "two_D0": Q(5, 4)**65 / 2**25,
        "two_D1": Q(6, 5)**2 * Q(5, 4)**40 / 2**37,
        "two_D2": Q(6, 5)**4 / 2**37,
    }
    assert all(v < 1 for v in factors.values())
    return {"rows": rows, "shift_25_error_ratios": {k: str(v) for k,v in factors.items()}}


def compile_word(pairs: tuple[tuple[int,int], ...]) -> tuple[int,int]:
    word = [bit for a,b in pairs for bit in ([1]*a+[0]*b)]
    A, q = 0, 0
    for i, bit in enumerate(word):
        if bit:
            A = 3*A + (1 << i)
            q += 1
    modulus = 1 << (len(word)+1)
    residue = ((1 << len(word))-A)*pow(3**q, -1, modulus) % modulus
    return residue, modulus


def cylinder_certificate() -> list[dict]:
    rows = []
    choices = list(itertools.product(range(1,5), repeat=2))
    for r in (1,2):
        for pairs in itertools.product(choices, repeat=r):
            if sum(a+b for a,b in pairs) > 12:
                continue
            residue, modulus = compile_word(pairs)
            for lift in range(3):
                n = residue + lift*modulus
                x = n
                for a,b in pairs:
                    x, aa, bb = packet(x)
                    assert (aa,bb) == (a,b)
            rows.append({"pairs": [list(t) for t in pairs],
                         "residue": residue, "modulus": modulus})
    return rows


def inverse_certificate() -> list[dict]:
    rows = []
    B = 6
    for y in range(3,128,2):
        terms=[]
        for b in range(1,B+1):
            z=(1 << b)*y+1
            a=0
            while z % 3 == 0:
                a+=1;z//=3
                n=(1 << a)*z-1
                assert packet(n) == (y,a,b)
                terms.append([n,a,b])
        terms.sort()
        rows.append({"endpoint":y,"max_even_run":B,"terms":terms})
    return rows


def kernel_bounds() -> list[dict]:
    # Exact partial inverse kernel applied to f(n)=(n+1)^(-2).
    rows=[]
    for y in [3,5,7,11,13,19,31,43,85,127]:
        for B in [4,8,12,16]:
            low=Q(0)
            for b in range(1,B):
                z=(1<<b)*y+1
                v=0;t=z
                while t%3==0:v+=1;t//=3
                low += Q(9,5)*(Q(9,4)**v-1)/(z*z)
            fourth = math.isqrt(math.isqrt(y))
            assert fourth**4 <= y < (fourth+1)**4
            tail = Q(18,5) / (2**(5*B//4)*y*fourth)
            rows.append({"endpoint":y,"first_omitted_b":B,
                         "lower":str(low),"upper":str(low+tail),"tail":str(tail)})
    return rows


def core_certificate() -> dict:
    # Memoization stores only paths explicitly followed to an already solved state.
    solved={1:(0,0)}
    max_packet=(0,1); max_micro=(0,1)
    for n in range(3,H+1,2):
        x=n;path=[];seen=set()
        while x not in solved:
            if x in seen or len(path)>10000:
                raise AssertionError("cycle or run cap in finite core")
            seen.add(x)
            y,a,b=packet(x);path.append((x,a+b));x=y
        r,t=solved[x]
        for x,cost in reversed(path):
            r+=1;t+=cost;solved[x]=(r,t)
        r,t=solved[n]
        if r>max_packet[0]:max_packet=(r,n)
    max_micro=(0,1)
    for n in range(1,H+1):
        b=(n&-n).bit_length()-1
        odd=n>>b
        r,t=solved[odd]
        t+=b
        if t>max_micro[0]:max_micro=(t,n)
    return {"bound":H,"odd_sources":H//2-1,"all_converged":True,
            "maximum_packets_odd":list(max_packet),
            "maximum_shortcut_steps_all":list(max_micro)}


def profile_certificate() -> dict:
    accum=[0]*(J+1);counts=[0]*(J+1);max_heights=[0]*(J+1)
    for n in range(H+1,2*H+1,2):
        x=n
        for j in range(J+1):
            if x<=H:break
            scaled=math.isqrt(((x+1)<<(2*BITS))//(n+1))
            accum[j]+=scaled;counts[j]+=1
            max_heights[j]=max(max_heights[j],x)
            if j<J:x,_,_=packet(x)
    p=ceil_q((Q(8,5)**J-1)/2)
    tail_exp=-4*H+21*p+J+1
    assert -4*(1<<19)+p <= -1
    assert tail_exp <= -120
    intervals=[]
    for j in range(J+1):
        factor=LAMBDA**j*Q(2,H)*Q(1,1<<BITS)
        lo=factor*accum[j];hi=factor*(accum[j]+counts[j])+TAIL
        intervals.append({"j":j,"finite_survivors":counts[j],"floor_sum":accum[j],
                          "finite_max_endpoint":max_heights[j],
                          "lower":str(lo),"upper":str(hi)})
    # The true entire infinite-source process grows on three successive steps.
    increases=[]
    for j in [21,22,23]:
        lo=Q(intervals[j+1]["lower"])-Q(intervals[j]["upper"])
        assert lo>0
        increases.append({"from":j,"to":j+1,"growth_lower":str(lo)})
    return {"source_first_shell":[H,2*H],"j_max":J,"rounding_bits":BITS,
            "seed":"h0(n)=2^(1-m-4*(2^m-H)) on odd 2^m<n<=2^(m+1), m>=18",
            "all_source_tail_upper":str(TAIL),"coarse_p":p,
            "tail_log2_upper":tail_exp,"intervals":intervals,"certified_increases":increases}


def control_certificate() -> dict:
    # A generalized-map nontrivial cycle must NOT be killed by the packet logic.
    n=13;path=[n]
    while True:
        n=(5*n+1)//2 if n%2 else n//2
        path.append(n)
        if n==13:break
        assert len(path)<50
    assert path==[13,33,83,208,104,52,26,13]
    return {"map":"even n/2; odd (5n+1)/2", "cycle":path,
            "packet_returns_to":13,"status":"nonterminating control, not standard Collatz"}


def build() -> dict:
    return {"schema":SCHEMA,"scope":"finite exact checks; cofinal drift certified by the written induction; no Collatz proof",
            "pressure":pressure_certificate(),"cofinal":cofinal_certificate(),
            "cylinders":cylinder_certificate(),"inverse":inverse_certificate(),
            "kernel":kernel_bounds(),"core":core_certificate(),
            "profile":profile_certificate(),"control":control_certificate()}


def seal(data: dict) -> dict:
    raw=json.dumps(data,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()
    return {"payload":data,"sha256":hashlib.sha256(raw).hexdigest()}


def compact(data: dict) -> dict:
    scale=1<<64
    intervals=[]
    for row in data["profile"]["intervals"]:
        lo=Q(row["lower"])*scale; hi=Q(row["upper"])*scale
        intervals.append({"j":row["j"],"lower_units":lo.numerator//lo.denominator,
                          "upper_units":ceil_q(hi),"finite_survivors":row["finite_survivors"]})
    cofinal=[]
    for r,start,target in [(1,18,Q(99,100)),(2,128,Q(19,20))]:
        maximum=max(Q(row["upper"]) for row in data["cofinal"]["rows"] if row["packets"]==r)
        cofinal.append({"packets":r,"first_m":start,"last_m":start+24,
                        "maximum_upper_units":ceil_q(maximum*scale),"target":str(target)})
    return {"schema":"astra-run-renewal-certificate-v1","scope":data["scope"],
            "full_replay_sha256":seal(data)["sha256"],"interval_denominator":scale,
            "coverage":{"cylinders":len(data["cylinders"]),"inverse_endpoints":len(data["inverse"]),
                        "inverse_sources":sum(len(r["terms"]) for r in data["inverse"]),
                        "kernel_intervals":len(data["kernel"]),"cofinal_rows":len(data["cofinal"]["rows"]),
                        "profile_intervals":len(intervals)},
            "pressure_upper":data["pressure"]["simple_upper"],"cofinal":cofinal,
            "shift_25_error_ratios":data["cofinal"]["shift_25_error_ratios"],
            "core":data["core"],"seed":data["profile"]["seed"],
            "tail_log2_upper":data["profile"]["tail_log2_upper"],
            "all_source_tail_upper":data["profile"]["all_source_tail_upper"],
            "coarse_p":data["profile"]["coarse_p"],"profile":intervals,
            "certified_increase_from":[21,22,23],"control":data["control"]}


def main() -> None:
    ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path);ap.add_argument("--check",type=Path)
    ap.add_argument("--full-output",type=Path,help="write every reconstructed row, not only the compact certificate")
    args=ap.parse_args();data=build();result=seal(compact(data))
    if args.check:
        expected=json.loads(args.check.read_text())
        if result!=expected:raise SystemExit("FAIL: replay differs")
    if args.output:args.output.write_text(json.dumps(result,sort_keys=True,separators=(",",":"))+"\n")
    if args.full_output:args.full_output.write_text(json.dumps(seal(data),sort_keys=True,separators=(",",":"))+"\n")
    print("PASS",result["sha256"])
    print("full replay",result["payload"]["full_replay_sha256"])
    print("coverage",result["payload"]["coverage"])
    print("core",result["payload"]["core"])

if __name__=="__main__":main()
