#!/usr/bin/env python3
"""X-8203: exact absorption arithmetic and affine-run Tschakaloff normalization."""
from __future__ import annotations
import argparse, hashlib, json, sys
from fractions import Fraction
from pathlib import Path
sys.set_int_max_str_digits(0)

P49=(5,30,20,56)
BETA49=(2,3,2,1)

def pr49_state(t,g,i):
    G=7*(t+1)+g-BETA49[i]
    D=11*(t+17)-i
    A=3**G
    Q=1<<D
    a=(-pow(A,-1,Q))%Q
    h=(A*a+1)//Q
    rows={}
    for j in range(4):
        ks=[k for k in range(64) if (3**BETA49[i]*(h+A*k))%64==P49[j]]
        assert len(ks)==1
        k=ks[0]
        r=a+Q*k
        s=(h+A*k)//(1<<j)
        for nu in range(3):
            rh=r+(1<<(D+6))*nu
            if rh%3:
                rows[j,nu]=(rh,s+(1<<(6-j))*A*nu)
    assert len(rows)==8
    return G,D,A,rows

def pr49_transition(t,g,i,j,nu,k):
    G,D,A,rows=pr49_state(t,g,i)
    sh=rows[j,nu][1]
    _,D2,_,rows2=pr49_state(t+16,BETA49[i],j)
    candidates=[(n,r) for (jj,n),(r,s) in rows2.items() if jj==k and r%3==sh%3]
    assert len(candidates)==1
    n,r2=candidates[0]
    delta=(r2-sh)//(3*(1<<(6-j)))
    H=11*(t+33)
    M=1<<H
    rho=pow(A,-1,M)*delta%M
    sigma=(A*rho-delta)//M
    assert sigma>=0
    return n,rho,sigma,H,A

def mixed_radix_crosswalk_counterexample():
    t,g,i=3744,1,0
    j,nu,k,l=0,1,0,0
    n,rho,sigma,H,A=pr49_transition(t,g,i,j,nu,k)
    n2,rho_next,sigma2,H_next,A2=pr49_transition(t+16,BETA49[i],j,k,n,l)
    M_next=1<<H_next
    ell_residue=pow(A,-1,M_next)*(rho_next-sigma)%M_next
    assert (sigma+A*ell_residue-rho_next)%M_next==0
    assert ell_residue%64==45
    assert rho_next%64==16
    assert ell_residue!=rho_next
    return {
        "state":[t,g,i],
        "current_block":[j,nu],
        "next_target":k,
        "chosen_next_lift":n,
        "following_target":l,
        "mixed_radix_second_digit_mod64":ell_residue%64,
        "actual_next_residue_mod64":rho_next%64,
        "equal":False,
    }

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
        "t8512_future_stack_crosswalk":mixed_radix_crosswalk_counterexample(),
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
