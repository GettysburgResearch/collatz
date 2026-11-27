"""Certified enclosures of the full original Q*_j from a single ternary period."""
import argparse
import json
from array import array
from fractions import Fraction
from pathlib import Path

PRECISION = 40
EXTRA = 24
SCALE = 1 << PRECISION


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def lower_row(previous, depth):
    # PR193 check_linear_trace uses this geometric doubling sweep.
    small = len(previous)
    modulus = 3*small
    row = array("Q",[0])*modulus
    residue, val = 1, 0
    for _ in range(2*small+PRECISION+depth+2):
        residue = (residue+modulus*(residue % 2))//2
        if residue % 3 == 2:
            val += 3*previous[((2*residue-1)//3) % small]
        val //= 2
        row[residue]=val
    return row


def exact_row(previous):
    small = len(previous)
    mod = 3*small
    clock = 2*small
    denominator = 2**clock-1
    row = [Fraction(0)]*mod
    for n, weight in enumerate(previous):
        residue = 3*n+1
        for e in range(1,clock+1):
            residue=(residue+mod*(residue%2))//2
            row[residue] += Fraction(3*2**(clock-e),denominator)*weight
    return row


def enclosure(level, old, new):
    d = level-2
    q = len(new)
    olderr = 3*(2**(level-1)-1)
    newerr = 3*(2**level-1)
    bottom = top = sites = 0
    for y in range(3,2*q,2):
        diff = new[y%q]-old[y%len(old)]
        den = y*(3*y+1)
        lo = max(0,diff-olderr)
        hi = max(0,diff+newerr)
        sites += lo > 0
        bottom += (lo << EXTRA)//den
        top += ((hi << EXTRA)+den-1)//den
    low = Fraction(bottom,SCALE << EXTRA)
    tail = Fraction(1,6*q)
    upper = Fraction(top,SCALE << EXTRA)+tail
    return {"grade":d,"ternary_period":q,"strict_positive_sites_in_first_odd_period":sites,
            "lower":str(low),"upper":str(upper),"remaining_target_upper":str(tail),
            "lower_scaled_1e9":(low*10**9).__floor__(),"upper_scaled_1e9":(upper*10**9).__ceil__()}


def main():
    parse=argparse.ArgumentParser(description=__doc__)
    parse.add_argument("--grade",type=int,default=11)
    parse.add_argument("--output",type=Path)
    args=parse.parse_args()
    if not 1 <= args.grade <= 16:
        parse.error("--grade must lie between 1 and 16")
    for n in range(1,9):
        x=n
        for _ in range(100):
            if x == 1:
                break
            x = (3*x+1)//2 if x%2 else x//2
        require(x==1,"finite prefix for all-target marked emptiness")
    require(args.grade+1<=3*8,"verified narrow-band transfer range")
    old=array("Q",[SCALE])
    exact=[Fraction(1)]
    rows=[]
    for level in range(1,args.grade+3):
        new=lower_row(old,level)
        if level <= 5:
            exact=exact_row(exact)
            err=3*(2**level-1)
            require(sum(exact)==len(exact),"ternary full-period mass")
            require(all(v <= SCALE*w <= v+err for v,w in zip(new,exact)),"full exact row enclosure")
        if level >= 3:
            rows.append(enclosure(level,old,new))
        old=new
    data=json.dumps({"scope":"full infinite original statistic at each listed grade, using verified marked emptiness",
                     "fixed_point_bits":PRECISION,"summation_extra_bits":EXTRA,
                     "exactly_rechecked_full_levels":min(args.grade+2,5),
                     "all_target_marked_empty_via_inclusive_verified_prefix":8,"rows":rows},indent=2)+"\n"
    if args.output:
        args.output.write_text(data)
    else:
        print(data,end="")


if __name__=="__main__":
    main()
