#!/usr/bin/env python3
"""Finite dual enumeration of original-law rare gate words and actual principal seeds."""
from collections import Counter
from fractions import Fraction
from math import comb
import hashlib
import json


def edge(v):
    x = 3*v + 1
    e = (x & -x).bit_length()-1
    return x >> e, e


def cap(name, n):
    if name == "3/2":
        return 3*n//2
    if name == "7/4":
        return 7*n//4
    return (3**n).bit_length()-1


def add(row, depth, total, cap_final, m, terminal, floor_height):
    mass = 2**(cap_final-total)
    row[0] += 1
    row[1] += mass
    row[2][cap_final-total] += mass
    row[3][cap_final-(m.bit_length()-1)] += mass
    row[4][(3**depth).bit_length()-terminal.bit_length()] += mass
    row[5][floor_height.bit_length()-1] += mass
    row[6] = max(row[6], m)
    row[7] = max(row[7], terminal)


def empty():
    return [0,0,Counter(),Counter(),Counter(),Counter(),0,0]


def direct(name, n):
    D=cap(name,n)
    row=empty()
    for m in range(1, 2**(D+1), 2):
        x, A, floor_height = m, 0, m
        for i in range(1,n+1):
            x,e=edge(x)
            A+=e
            if A>cap(name,i):
                break
            floor_height=min(floor_height,x)
        else:
            if m < 2**(A+1):
                add(row,n,A,D,m,x,floor_height)
    return row


def cases(name, nmax):
    rows=[empty() for _ in range(nmax+1)]
    seed_count=[set() for _ in range(nmax+1)]
    def visit(m,A,i,x,ternary):
        if i>=1:
            D=cap(name,i)
            h,clock,floor_height=m,0,m
            for t in range(1,i+1):
                h,e=edge(h)
                clock+=e
                assert clock<=cap(name,t)
                assert h*(2**clock)>=3**t*m
                floor_height=min(floor_height,h)
            assert h==x and clock==A and m < 2**(A+1) and x<2*ternary
            assert m not in seed_count[i]
            seed_count[i].add(m)
            add(rows[i],i,A,D,m,x,floor_height)
        if i==nmax:
            return
        for e in range(1,cap(name,i+1)-A+1):
            modulus=2**e
            lift=((2**(e-1) -(3*x+1)//2)*pow(3*ternary,-1,modulus))%modulus
            m1=m+2**(A+1)*lift
            old=x+2*ternary*lift
            x1,e1=edge(old)
            assert e1==e
            visit(m1,A+e,i+1,x1,3*ternary)
    visit(1,0,0,1,1)
    for i in range(1, min(8,nmax)+1):
        assert rows[i]==direct(name,i)
    result=[]
    for i in range(1,nmax+1):
        D=cap(name,i)
        row=rows[i]
        prob=Fraction(row[1],2**D)
        assert prob>=Fraction(comb(D-1,i-1),i*2**D)
        result.append({
            "n":i,"words":row[0],"gate_probability":str(prob),
            "mean_total_gap_deficit":str(Fraction(sum(k*v for k,v in row[2].items()),row[1])),
            "mean_seed_bit_deficit":str(Fraction(sum(k*v for k,v in row[3].items()),row[1])),
            "mean_terminal_bit_deficit":str(Fraction(sum(k*v for k,v in row[4].items()),row[1])),
            "max_seed":row[6],"max_terminal":row[7],
            "minimum_height_histogram_bit_bins":sorted(row[5].items()),
        })
    return result


if __name__ == "__main__":
    print(json.dumps({name:cases(name,11) for name in ("3/2","log2(3)","7/4")},sort_keys=True,indent=2))
