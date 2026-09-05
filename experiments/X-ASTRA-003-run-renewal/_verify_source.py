#!/usr/bin/env python3
"""Separate replay of X-ASTRA-003; does not import its generator.

The mathematical all-scale induction is in RUN_RENEWAL.md. This program
checks its finite arithmetic inputs and the complete declared finite corpus.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

LIMIT=262144
STAGES=24
PRECISION=96
RATE=F(9,8)
QBOUND=F(173,200)
SCOPE="finite exact checks; cofinal drift certified by the written induction; no Collatz proof"


def step(x: int) -> int:
    return (3*x+1)//2 if x&1 else x//2


def full_run(x: int) -> tuple[int,int,int]:
    assert x>0 and x&1
    odd=even=0
    while x&1:
        x=step(x);odd+=1
    while not x&1:
        x=step(x);even+=1
    return x,odd,even


def upper_integer(q: F) -> int:
    a,b=divmod(q.numerator,q.denominator)
    return a+(b!=0)


def make_pressure() -> dict:
    lo2,hi2=F(1414213562373,10**12),F(1414213562374,10**12)
    lo3,hi3=F(1732050807568,10**12),F(1732050807569,10**12)
    for v,lo,hi in [(2,lo2,hi2),(3,lo3,hi3)]:
        assert lo.numerator**2 < v*lo.denominator**2
        assert hi.numerator**2 > v*hi.denominator**2
    den=(2*lo2-hi3)*(2*lo2-1)
    assert den>0
    upper=hi3/den
    assert upper<QBOUND
    return {"sqrt2":[str(lo2),str(hi2)],"sqrt3":[str(lo3),str(hi3)],
            "pressure_upper":str(upper),"simple_upper":str(QBOUND)}


def scale_upper(m: int, r: int) -> F:
    odds=[upper_integer(F(8**i*(m+2),5**i)) for i in range(r)]
    evens=[upper_integer(F(8**(i+1)*(m+2),5**(i+1))) for i in range(r)]
    errors=[]
    for cut in range(r+1):
        num=math.prod(odds[i]*evens[i] for i in range(cut))
        suffix=math.prod(F(25,2)*F(5,4)**odds[i] for i in range(cut,r))
        errors.append(num*suffix)
    value=QBOUND**r
    value+=2*errors[0]/F(2**m)
    for cut in range(1,r+1):
        value+=F(1,2**(m//2))*(QBOUND**(r-cut)+2*errors[cut]/F(2**m))
    return RATE**r*value


def make_cofinal() -> dict:
    rows=[]
    for r,first,target in [(1,18,F(99,100)),(2,128,F(19,20))]:
        for m in range(first,first+25):
            upper=scale_upper(m,r)
            assert upper<target
            rows.append({"packets":r,"m":m,"upper":str(upper),"target":str(target)})
    factors={"one_D0":F(5**25,4**25*2**25),
             "one_D1":F(9**2,4**2*2**37),
             "two_D0":F(5**65,4**65*2**25),
             "two_D1":F(6**2*5**40,5**2*4**40*2**37),
             "two_D2":F(6**4,5**4*2**37)}
    assert all(0<x<1 for x in factors.values())
    assert 3**5<2**8 and 3**5<4**4
    return {"rows":rows,"shift_25_error_ratios":{k:str(v) for k,v in factors.items()}}


def lift_parities(bits: list[int]) -> tuple[int,int]:
    root=0;mod=1
    for bit in bits:
        # Exactly one of the two ordinary lifts must have the required prefix.
        passed=[]
        for candidate in (root,root+mod):
            x=candidate;ok=True
            for expected in bits[:mod.bit_length()]:
                if x%2!=expected:ok=False;break
                x=step(x)
            if ok:passed.append(candidate)
        assert len(passed)==1
        root=passed[0];mod*=2
    return root,mod


def make_cylinders() -> list[dict]:
    rows=[]
    pairs=list(itertools.product(range(1,5),repeat=2))
    for count in (1,2):
        for seq in itertools.product(pairs,repeat=count):
            if sum(sum(t) for t in seq)>12:continue
            bits=[]
            for a,b in seq:bits.extend([1]*a+[0]*b)
            root,mod=lift_parities(bits+[1])
            for t in range(3):
                x=root+t*mod
                for a,b in seq:
                    x,actual_a,actual_b=full_run(x)
                    assert (a,b)==(actual_a,actual_b)
            rows.append({"pairs":[list(t) for t in seq],"residue":root,"modulus":mod})
    assert len(rows)==237
    return rows


def make_inverse() -> list[dict]:
    rows=[]
    # Every source with even run <=6 satisfies n<2^6*y. No source is missed.
    for y in range(3,128,2):
        terms=[]
        for n in range(3,64*y+1,2):
            image,a,b=full_run(n)
            if image==y and b<=6:terms.append([n,a,b])
        rows.append({"endpoint":y,"max_even_run":6,"terms":terms})
    return rows


def make_kernel() -> list[dict]:
    rows=[]
    for y in [3,5,7,11,13,19,31,43,85,127]:
        for first_omitted in (4,8,12,16):
            partial=F(0)
            for b in range(1,first_omitted):
                raw=2**b*y+1;m=raw;a=0
                while m%3==0:
                    m//=3;a+=1
                    source=2**a*m-1
                    assert full_run(source)==(y,a,b)
                    partial+=F(1,(source+1)**2)
            lower_root=1
            while (lower_root+1)**4<=y:lower_root+=1
            tail=F(18,5*2**(5*first_omitted//4)*y*lower_root)
            rows.append({"endpoint":y,"first_omitted_b":first_omitted,
                         "lower":str(partial),"upper":str(partial+tail),"tail":str(tail)})
    return rows


def make_core() -> dict:
    # Direct shortcut iteration verifies the physical clock, independently of powers.
    times={1:0}
    max_steps=(0,1)
    for n in range(1,LIMIT+1):
        x=n;path=[];seen=set()
        while x not in times:
            assert x not in seen and len(path)<100000
            seen.add(x);path.append(x);x=step(x)
        t=times[x]
        for old in reversed(path):t+=1;times[old]=t
        if times[n]>max_steps[0]:max_steps=(times[n],n)
    packets={1:0};max_packets=(0,1)
    for n in range(3,LIMIT+1,2):
        x=n;trail=[];seen=set()
        while x not in packets:
            assert x not in seen and len(trail)<10000
            seen.add(x);trail.append(x);x=full_run(x)[0]
        r=packets[x]
        for old in reversed(trail):r+=1;packets[old]=r
        if packets[n]>max_packets[0]:max_packets=(packets[n],n)
    return {"bound":LIMIT,"odd_sources":LIMIT//2-1,"all_converged":True,
            "maximum_packets_odd":list(max_packets),"maximum_shortcut_steps_all":list(max_steps)}


def make_profile() -> dict:
    totals=[0]*(STAGES+1);numbers=[0]*(STAGES+1);peaks=[0]*(STAGES+1)
    for n in range(LIMIT+1,2*LIMIT+1,2):
        x=n
        for stage in range(STAGES+1):
            if x<=LIMIT:break
            # floor(floor(sqrt(A*B*2^(2p)))/B)=floor(2^p sqrt(A/B)).
            floor_value=math.isqrt(((x+1)*(n+1))<<(2*PRECISION))//(n+1)
            totals[stage]+=floor_value;numbers[stage]+=1
            peaks[stage]=max(peaks[stage],x)
            if stage<STAGES:x=full_run(x)[0]
    p=upper_integer(F(8**STAGES-5**STAGES,2*5**STAGES))
    E=-4*LIMIT+21*p+STAGES+1
    assert p==39614 and E==-216657 and -4*2**19+p<=-1
    tail=F(1,2**120)
    rows=[]
    for stage in range(STAGES+1):
        multiplier=F(9**stage,8**stage)*F(2,LIMIT*2**PRECISION)
        lo=multiplier*totals[stage]
        hi=multiplier*(totals[stage]+numbers[stage])+tail
        rows.append({"j":stage,"finite_survivors":numbers[stage],"floor_sum":totals[stage],
                     "finite_max_endpoint":peaks[stage],"lower":str(lo),"upper":str(hi)})
    growth=[]
    for j in (21,22,23):
        difference=F(rows[j+1]["lower"])-F(rows[j]["upper"])
        assert difference>0
        growth.append({"from":j,"to":j+1,"growth_lower":str(difference)})
    return {"source_first_shell":[LIMIT,2*LIMIT],"j_max":STAGES,"rounding_bits":PRECISION,
            "seed":"h0(n)=2^(1-m-4*(2^m-H)) on odd 2^m<n<=2^(m+1), m>=18",
            "all_source_tail_upper":str(tail),"coarse_p":p,"tail_log2_upper":E,
            "intervals":rows,"certified_increases":growth}


def make_control() -> dict:
    values=[13];x=13
    for _ in range(20):
        x=(5*x+1)//2 if x&1 else x//2;values.append(x)
        if x==13:break
    assert values==[13,33,83,208,104,52,26,13] and 1 not in values
    return {"map":"even n/2; odd (5n+1)/2","cycle":values,
            "packet_returns_to":13,"status":"nonterminating control, not standard Collatz"}


def expected_payload() -> dict:
    return {"schema":"astra-run-renewal-v1","scope":SCOPE,"pressure":make_pressure(),
            "cofinal":make_cofinal(),"cylinders":make_cylinders(),"inverse":make_inverse(),
            "kernel":make_kernel(),"core":make_core(),"profile":make_profile(),"control":make_control()}


def digest(payload: dict) -> str:
    return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()


def compact_expected(data: dict) -> dict:
    scale=2**64
    interval_rows=[]
    for row in data["profile"]["intervals"]:
        low=F(row["lower"]); high=F(row["upper"])
        interval_rows.append({"j":row["j"],
            "lower_units":low.numerator*scale//low.denominator,
            "upper_units":upper_integer(high*scale),"finite_survivors":row["finite_survivors"]})
    cofinal=[]
    for count,first,target in [(1,18,"99/100"),(2,128,"19/20")]:
        bounds=[F(row["upper"]) for row in data["cofinal"]["rows"] if row["packets"]==count]
        cofinal.append({"packets":count,"first_m":first,"last_m":first+24,
                        "maximum_upper_units":upper_integer(max(bounds)*scale),"target":target})
    return {"schema":"astra-run-renewal-certificate-v1","scope":SCOPE,
            "full_replay_sha256":digest(data),"interval_denominator":scale,
            "coverage":{"cylinders":len(data["cylinders"]),"inverse_endpoints":len(data["inverse"]),
                        "inverse_sources":sum(map(lambda r:len(r["terms"]),data["inverse"])),
                        "kernel_intervals":len(data["kernel"]),"cofinal_rows":len(data["cofinal"]["rows"]),
                        "profile_intervals":len(interval_rows)},
            "pressure_upper":"173/200","cofinal":cofinal,
            "shift_25_error_ratios":data["cofinal"]["shift_25_error_ratios"],
            "core":data["core"],"seed":data["profile"]["seed"],
            "tail_log2_upper":data["profile"]["tail_log2_upper"],
            "all_source_tail_upper":data["profile"]["all_source_tail_upper"],
            "coarse_p":data["profile"]["coarse_p"],"profile":interval_rows,
            "certified_increase_from":[21,22,23],"control":data["control"]}


def validate(report: dict, expected: dict) -> None:
    assert set(report)=={"payload","sha256"},"report fields"
    assert digest(report["payload"])==report["sha256"],"digest"
    assert set(report["payload"])==set(expected),"payload coverage"
    for section in expected:
        assert report["payload"][section]==expected[section],f"incorrect {section} mathematics, scope, or coverage"


def tamper_tests(report: dict, expected: dict) -> None:
    corrupt=[]
    r=copy.deepcopy(report);r["payload"]["coverage"]["cylinders"]-=1;corrupt.append(r)
    r=copy.deepcopy(report);r["payload"]["all_source_tail_upper"]="0";corrupt.append(r)
    r=copy.deepcopy(report);r["payload"]["cofinal"][0]["first_m"]+=1;corrupt.append(r)
    r=copy.deepcopy(report);r["payload"]["scope"]="all-time Collatz proof";corrupt.append(r)
    r=copy.deepcopy(report);r["payload"]["coverage"]["inverse_sources"]+=1;corrupt.append(r)
    r=copy.deepcopy(report);r["payload"]["control"]["status"]="converged";corrupt.append(r)
    for i,r in enumerate(corrupt):
        r["sha256"]=digest(r["payload"])
        try:validate(r,expected)
        except AssertionError:continue
        raise AssertionError(f"resealed tampering {i} accepted")
    print("RESEALED TAMPERING REJECTED",len(corrupt))


def main() -> None:
    parser=argparse.ArgumentParser();parser.add_argument("report",type=Path);parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args();report=json.loads(args.report.read_text())
    expected=compact_expected(expected_payload())
    validate(report,expected)
    if args.self_test:tamper_tests(report,expected)
    print("SEPARATE REPLAY PASS",report["sha256"])

if __name__=="__main__":main()
