#!/usr/bin/env python3
"""X-8203: exact absorption arithmetic and affine-run Tschakaloff normalization."""
from __future__ import annotations
import argparse, hashlib, json, sys
from fractions import Fraction
from pathlib import Path
sys.set_int_max_str_digits(0)

def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def canonical_absorption():
    def run_expr(r,t):
        return r*(63*t-121080)+504*r*(r-1)-665*(22*(t+16*r)+559)
    assert 3**665 > 2**1054
    assert run_expr(470,3760)==124585
    assert 63*470-665*22==14980
    assert run_expr(233,1_140_416)==593
    assert 63*233-665*22==49
    q=lambda t:(63*t-353166)//665
    assert q(5632)==2
    assert q(5616)==0
    assert 9**53>2**168
    def bracket(d,t,r):
        ct=Fraction(63,665)-Fraction(11,d)
        cr=Fraction(504,665)-Fraction(176,d)-Fraction(88,d*d)
        c=Fraction(175,1)+Fraction(-354335,665)-Fraction(363,d)
        return ct*t+cr*r+c
    b288=bracket(288,5632,288)
    b233=bracket(233,5632,100_909)
    assert b288==Fraction(84263,63840)
    assert b233==Fraction(27453,36102185)
    return {
        "three665_gt_two1054": True,
        "canonical_471_certificate":124585,
        "canonical_234_certificate":593,
        "absorption_height":5632,
        "q_at_absorption":2,
        "stack_288_margin":str(b288),
        "stack_233_margin":str(b233),
        "nine53_minus_two168":9**53-2**168,
    }

def affine_tschakaloff():
    schedules=0
    coefficient_checks=0
    backward_checks=0
    functional_checks=0
    max_depth=20
    for R in range(9):
        for d in range(1,6):
            schedules+=1
            q=Fraction(8,9)**d
            z=Fraction(2**(3*R+3*d+4),9**(R+d+1))
            A=B=0
            terms=[]
            for j in range(max_depth):
                b_j=R+d*j+1
                direct=Fraction(2**A,9**(B+b_j))
                closed=Fraction(1,9**(R+1))*z**j*q**(j*(j-1)//2)
                assert direct==closed
                terms.append(direct)
                A+=3*d*j+3*R+3*d+4
                B+=b_j
                coefficient_checks+=1
            for j in range(max_depth-1):
                assert terms[j+1]==terms[j]*z*q**j
                coefficient_checks+=1
            for N in (1,2,5,10,20):
                terminal=2*N+1
                v=Fraction(terminal)
                for n in reversed(range(N)):
                    v=(2**(4+3*(R+d*(n+1)))*v-1)/9**(R+d*n+1)
                A_N=sum(4+3*(R+d*(n+1)) for n in range(N))
                B_N=sum(R+d*n+1 for n in range(N))
                rhs=-sum(terms[:N],Fraction())+Fraction(2**A_N,9**B_N)*terminal
                assert v==rhs
                backward_checks+=1
            for n in range(max_depth):
                c=q**(n*(n-1)//2)
                if n==0:
                    assert c==1
                else:
                    assert c==q**((n-1)*(n-2)//2)*q**(n-1)
                functional_checks+=1
    assert 30**2*2086-1369**2==3239
    assert 2**8-3**5==13
    return {
        "schedules":schedules,
        "R_range":"0..8",
        "d_range":"1..5",
        "max_depth":max_depth,
        "coefficient_checks":coefficient_checks,
        "backward_identity_checks":backward_checks,
        "functional_coefficient_checks":functional_checks,
        "q_formula":"(8/9)^d",
        "z_formula":"2^(3R+3d+4)/9^(R+d+1)",
        "core_formula":"v0=-9^(-(R+1))*F_q(z)",
        "source_lambda":"-(2/3)*log_2(3)",
        "beta":"(2*sqrt(2086)-7)/79",
        "beta_gt_16_over_15_square_margin":3239,
        "sixteen_over_fifteen_gt_gamma_integer_margin":13,
        "source_conclusion":"every eventually affine positive-slope run schedule has irrational core",
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path)
    p.add_argument("--check-results",type=Path)
    a=p.parse_args()
    payload={
        "agent":"gpt56-refund-01",
        "date":"2026-07-23",
        "experiment_id":"X-8203",
        "frozen":{
            "pr49":"210b1e204aa82947bab086b020bf2bd53805d84e",
            "pr51":"c7f1c75d0a71a63b32ef3e23306c23f1d0a60bfa",
            "source":"Amou-Matala-aho-Vaananen 2007 Theorem 5.1 DOI 10.4064/aa127-4-2",
        },
        "canonical_absorption":canonical_absorption(),
        "affine_run_tschakaloff":affine_tschakaloff(),
        "counterexample_claimed":False,
    }
    payload["semantic_digest"]=digest(payload)
    data=(json.dumps(payload,indent=2,sort_keys=True)+"\n").encode()
    if a.output:a.output.write_bytes(data)
    if a.check_results and a.check_results.read_bytes()!=data:
        raise SystemExit("canonical result mismatch")
    print(data.decode(),end="")
if __name__=="__main__":
    main()
