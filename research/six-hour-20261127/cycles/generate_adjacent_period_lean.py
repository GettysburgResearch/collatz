"""Regenerate the finite Lean coefficient/window data from independent rational log endpoints."""
from pathlib import Path
import argparse
import re
import certify_adjacent_gap_exclusion_independent as C

HERE=Path(__file__).resolve().parent


def inputs():
    lo,hi=C.enclosure()
    L,U=lo,hi
    aa,a,pp,p=0,1,1,0
    above=0; rows=[]
    while above<3:
        k=L.numerator//L.denominator
        if k!=U.numerator//U.denominator:
            raise ValueError('endpoint partial quotients diverge')
        aa,a=a,k*a+aa; pp,p=p,k*p+pp
        L,U=1/(U-k),1/(L-k)
        b=0
        if 10**6<p<=C.CAP and a>p*hi and C.FLOOR*(a-p*hi)<p:
            delta=a*hi.denominator-p*hi.numerator
            y=(hi.denominator+delta-1)//delta
            h=0;pow3=1
            while pow3*3<=y:
                h+=1;pow3*=3
            def rank(n):
                w=(2*p-a)*(n-1)//p
                return (n+1)+(y+(n+1)*3**n)*7**w//9**w,n
            _,b=min(rank(n) for n in range(max(2,h-20),h+3))
        rows.append((k,b))
        above+=p>C.CAP
    return lo,hi,rows


def main():
    lo,hi,rows=inputs()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='replace the two generated sections of the local Lean source')
    options=parser.parse_args()
    target=HERE/'AdjacentPeriodCensus.lean'
    current=target.read_text()
    params='\n'.join(f'def {key} : Nat := {n}' for key,n in
        [('lowerNum',lo.numerator),('lowerDen',lo.denominator),('upperNum',hi.numerator),('upperDen',hi.denominator)])
    specs=[]
    for i in range(0,len(rows),16):
        specs.append('  '+', '.join(f'({a}, {b})' for a,b in rows[i:i+16]))
    data='def coefficientsAndWindows : List (Nat × Nat) := [\n'+',\n'.join(specs)+']'
    first,n=re.subn(r'def lowerNum : Nat := [0-9]+\ndef lowerDen : Nat := [0-9]+\ndef upperNum : Nat := [0-9]+\ndef upperDen : Nat := [0-9]+',lambda _:params,current)
    if n!=1:raise ValueError('rational endpoint section missing or duplicated')
    regenerated,n=re.subn(r'def coefficientsAndWindows : List \(Nat × Nat\) := \[.*?\](?=\n\nstructure Row)',lambda _:data,first,flags=re.S)
    if n!=1:raise ValueError('coefficient/window section missing or duplicated')
    if options.write:
        target.write_text(regenerated)
    elif regenerated!=current:
        raise ValueError('embedded integer data does not match independent generator')
    print(f'checked {len(rows)} quotient/window records and both rational endpoints')


if __name__=='__main__':
    main()
