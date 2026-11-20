#!/usr/bin/env python3
"""Exact checks of a conditional affine cover and specified physical carry resets."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path

class VerificationError(ValueError):
    pass

def require(p: bool, text: str) -> None:
    if not p:
        raise VerificationError(text)

def isint(n: object) -> bool:
    return isinstance(n, int) and not isinstance(n, bool)

def T(n: int) -> int:
    require(isint(n) and n > 0, "positive ordinary source required")
    return (3 * n + 1) // 2 if n & 1 else n // 2

def U(n: int) -> tuple[int, int]:
    require(isint(n) and n > 0 and n & 1, "positive odd source required")
    z = 3 * n + 1; g = 0
    while not z & 1:
        z //= 2; g += 1
    return z, g

def first_hit(n: int, limit: int = 10000) -> tuple[int, int]:
    d = h = 0
    while n != 1:
        require(d < limit, "explicit control did not finish within its replay limit")
        h += n & 1
        n = T(n); d += 1
    return d, h

@dataclass(frozen=True)
class Row:
    modulus: int
    residue: int
    word: str
    a: int
    b: int

ROWS = (
    Row(12,11,"I",8,7),
    Row(16,3,"OOEE",9,2),
    Row(24,7,"MOOEVI",18,5),
    Row(32,11,"OOEOE",27,10),
    Row(16,15,"OMOOEVII",12,11),
    Row(32,23,"OOOEE",27,20),
    Row(96,91,"MOOVOEE",81,77),
    Row(20,3,"OV",6,1),
    Row(20,15,"OOV",9,7),
    Row(60,51,"ODDIV",48,41),
    Row(60,27,"OODMIIVV",24,11),
    Row(160,39,"OMOOVOEV",81,20),
    Row(160,59,"OOEMOODDVDIVIII",128,47),
)

def affine_step(a: int, b: int, letter: str) -> tuple[int, int]:
    require(isint(a) and isint(b) and a > 0 and b > 0, "positive affine form required")
    if letter == "D":
        return 2*a, 2*b
    if letter == "E":
        require(a % 2 == b % 2 == 0, "illegal even step")
        return a//2, b//2
    if letter == "O":
        require(a % 2 == 0 and b % 2 == 1, "illegal odd step")
        return 3*a//2, (3*b+1)//2
    if letter == "I":
        require(a % 3 == 0 and b % 3 == 2, "illegal odd inverse")
        return 2*a//3, (2*b-1)//3
    if letter == "M":
        require(a % 3 == 0 and b % 3 != 0, "multiplier at a nonunit or variable unit domain")
        return 5*a, 5*b
    if letter == "V":
        require(a % 3 == 0 and b % 3 != 0 and a % 5 == b % 5 == 0, "illegal unit-five division")
        return a//5, b//5
    raise VerificationError("unknown letter")

def verify_row(row: Row) -> list[tuple[int,int]]:
    require(all(isint(v) for v in (row.modulus,row.residue,row.a,row.b)), "noninteger row")
    require(row.modulus > 0 and 0 < row.residue < row.modulus, "bad source class")
    require(isinstance(row.word,str) and bool(row.word), "nonempty word required")
    a,b = row.modulus,row.residue
    trace=[(a,b)]
    for l in row.word:
        a,b=affine_step(a,b,l);trace.append((a,b))
    require((a,b)==(row.a,row.b), "false endpoint")
    require(0<a<row.modulus and 0<b<row.residue, "not strict for every nonnegative lift")
    require(11*a<=10*row.modulus and 11*b<=10*row.residue, "false contraction bound")
    return trace

def numeric_letter(x: int, l: str) -> int:
    if l=="D":return 2*x
    if l=="E":
        require(x%2==0,"numeric E parity");return x//2
    if l=="O":
        require(x%2==1,"numeric O parity");return (3*x+1)//2
    if l=="I":
        require(x%3==2,"numeric I domain")
        y=(2*x-1)//3
        require(T(y)==x,"inverse is not an ordinary predecessor")
        return y
    if l=="M":
        require(x%3!=0,"numeric M domain");return 5*x
    if l=="V":
        require(x%3!=0 and x%5==0,"numeric V domain");return x//5
    raise VerificationError("numeric unknown letter")

def run() -> dict:
    traces=[verify_row(row) for row in ROWS]
    covered={r for r in range(3,480,4) if any(r%row.modulus==row.residue for row in ROWS)}
    require(covered==set(range(3,480,4)),"uncovered residue class")
    augmented_edges=0
    for row,trace in zip(ROWS,traces):
        for u in (0,1,7,257,2**64+1):
            x=row.modulus*u+row.residue
            for l,(a,b) in zip(row.word,trace[1:]):
                x=numeric_letter(x,l)
                require(x==a*u+b,"numeric affine disagreement")
                augmented_edges+=1
    require(max(map(lambda r:len(r.word),ROWS))==15,"wrong graph step maximum")
    bad_controls=(
        ("wrong endpoint",Row(12,11,"I",8,8)),
        ("wrong parity class",Row(16,4,"OOEE",9,2)),
        ("nonunit multiplier",Row(12,3,"M",60,15)),
        ("empty word",Row(12,11,"",8,7)),
        ("nonintegral inverse",Row(16,3,"I",9,2)),
        ("nondecreasing path",Row(12,11,"D",24,22)),
    )
    rejected=[]
    for name,row in bad_controls:
        try:verify_row(row)
        except VerificationError:rejected.append(name)
        else:raise VerificationError("accepted corruption: "+name)
    # Symbolic self/larger demand control, not a failed convergence assertion.
    for u in range(32):
        n=31+48*u;y=(9*n+1)//8
        require(y==35+54*u and y>n and y%2==1 and y%3!=0,"demand-order control failed")
    physical_edges=odd_edges=family_cases=unit_cases=nondecreasing_prefix_cases=0
    for r in range(97):
        k=6*r+3;ell=2*r+1
        x=(2**(k+2)-5)//9;u=(2**(k+1)-1)//3
        M=2**k-1;z=(9**ell-1)//8
        require(x%4==3 and x%3==(2*r)%3,"antecedent residue formula")
        require(T(x)==u and T(u)==2**k,"supplied spine identities")
        require(first_hit(x)==(k+2,2),"supplied first-hit clocks")
        require(z>0 and z%2==1 and z%3==1,"reset unit domain")
        v=T(T(5*x));physical_edges+=2
        require(v==5*M and T(T(x))==M+1,"gap-one carry reset")
        for j in range(ell+1):
            require(v==5*9**j*2**(3*(ell-j))-5,"signed-cycle block formula")
            if j<ell:
                for expected_parity in (1,1,0):
                    require(v%2==expected_parity,"block parity mismatch")
                    v=T(v);physical_edges+=1
        for _ in range(3):
            require(v%2==0,"terminal halving parity")
            v=T(v);physical_edges+=1
        require(v==5*z,"full-spine reset failed")
        # Mersenne lower bound, without assuming its convergence.
        w=M
        for j in range(k):
            require(w==3**j*2**(k-j)-1,"Mersenne odd prefix formula")
            w,g=U(w);odd_edges+=1
            require(g==(2 if j==k-1 else 1),"Mersenne exponent word")
        require(w==(3**k-1)//2 and w>1,"Mersenne terminal lower bound")
        require(M>x,"first reset did not increase height")
        if r>=5:
            require(z>x,"full reset height comparison")
            w=5*x
            for _ in range(6*r+8):
                w=T(w);physical_edges+=1
                require(w>5*x,"displayed target path dropped below source")
            require(w==5*z,"second literal reset replay")
            nondecreasing_prefix_cases+=1
        if r>=15:
            require(z>2**(6*r+5),"new shortcut-depth lower bound")
        if r%4==3:
            require(z%8==7,"new odd-depth residue lower bound")
        family_cases+=1
        unit_cases+=(r%3!=0)
    controls=[]
    for name,x,y,expected_x,expected_y,clock in (
        ("first_reset",227,511,(11,2),(41,20),2),
        ("full_spine_reset",15637498706147,25736391511831,(47,2),(254,132),50),
    ):
        dx,hx=first_hit(x);dy,hy=first_hit(y)
        require((dx,hx)==expected_x and (dy,hy)==expected_y,"convergent control clocks")
        require(y>x and dy>dx and hy>hx,"positive-resource rank did not increase")
        w=5*x
        for _ in range(clock):w=T(w)
        require(w==5*y,"control target reset")
        d5x,h5x=first_hit(5*x);d5y,h5y=first_hit(5*y)
        require(d5x==clock+d5y,"target first-hit clocks did not compose")
        controls.append(dict(name=name,x=x,y=y,x_first_hit=[dx,hx],y_first_hit=[dy,hy],reset_clock=clock,five_x_first_hit=[d5x,h5x],five_y_first_hit=[d5y,h5y]))
    return dict(status="PASS",scope="Conditional all-lift affine cover plus exact specified carry resets and finite convergent rank controls. No proof of forward-five closure or Collatz.",affine_rows=len(ROWS),covered_residues_mod480=len(covered),max_augmented_word_length=15,conditional_graph_edges_replayed=augmented_edges,rejected_corruptions=rejected,carry_r_min=0,carry_r_max=96,carry_family_cases=family_cases,eligible_unit_antecedent_cases=unit_cases,physical_carry_edges=physical_edges,odd_mersenne_edges=odd_edges,strict_above_source_prefix_cases=nondecreasing_prefix_cases,convergent_rank_controls=controls)

def main() -> None:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--output",type=Path);args=p.parse_args()
    text=json.dumps(run(),indent=2,sort_keys=True)+"\n"
    if args.output:args.output.write_text(text,encoding="utf-8")
    print(text,end="")

if __name__=="__main__":main()
