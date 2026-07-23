#!/usr/bin/env python3
"""Separate verifier for X-8203; does not import run.py."""
from __future__ import annotations
import hashlib,json,sys
from fractions import Fraction
from pathlib import Path
sys.set_int_max_str_digits(0)

def main():
    if len(sys.argv)!=2:raise SystemExit("usage: verify.py canonical.json")
    p=json.loads(Path(sys.argv[1]).read_text())
    d=p.pop("semantic_digest")
    got=hashlib.sha256(json.dumps(p,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    assert got==d
    p["semantic_digest"]=d
    c=p["canonical_absorption"]
    assert 3**665>2**1054
    assert c["canonical_471_certificate"]==124585
    assert c["canonical_234_certificate"]==593
    assert c["absorption_height"]==5632 and c["q_at_absorption"]==2
    assert Fraction(c["stack_288_margin"])==Fraction(84263,63840)
    assert Fraction(c["stack_233_margin"])==Fraction(27453,36102185)
    assert c["nine53_minus_two168"]==9**53-2**168
    a=p["affine_run_tschakaloff"]
    assert a["schedules"]==45 and a["coefficient_checks"]==1755
    assert a["backward_identity_checks"]==225
    assert a["functional_coefficient_checks"]==900
    checks=0
    for R,d in ((0,1),(1,2),(7,3),(8,5)):
        q=Fraction(8,9)**d
        z=Fraction(2**(3*R+3*d+4),9**(R+d+1))
        A=B=0
        for j in range(12):
            b=R+d*j+1
            assert Fraction(2**A,9**(B+b))==Fraction(1,9**(R+1))*z**j*q**(j*(j-1)//2)
            A+=3*d*j+3*R+3*d+4
            B+=b
            checks+=1
    assert checks==48
    assert 30**2*2086-1369**2==3239 and 2**8-3**5==13
    assert not p["counterexample_claimed"]
    print("all independent X-8203 absorption/value checks passed")
if __name__=="__main__":main()
