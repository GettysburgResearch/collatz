#!/usr/bin/env python3
"""Check all cyclically parity-admissible primitive wall necklaces up to a bound.

Each emitted nonzero periodic orbit is a literal repeated signed numerator,
so this test makes no assumption about rational Collatz trajectories outside
the finite starts it actually follows.
"""
import argparse
import json
from collections import Counter
from fractions import Fraction


def step(n, d):
    return (3*n+d)//2 if n%2 else n//2


def representatives(length):
    # A nonconstant cyclic trace with a zero has even length, and a rotation
    # has all odd-position digits equal to 1.
    modulus=(1<<length)-1
    seen=set()
    for free in range(1<<(length//2)):
        value=0
        for i in range(length//2):
            value=4*value+2+(free>>i&1)
        if value==modulus or value in seen:
            continue
        orbit=set()
        r=value
        while r not in orbit:
            orbit.add(r)
            r=2*r%modulus
        seen.update(orbit)
        if len(orbit)==length:
            yield min(orbit)


class NumeratorOrbits:
    def __init__(self, d):
        self.d=d
        self.cache={0:0}
        self.largest_steps=0
        self.rates={0:Fraction(0)}

    def cycle(self, n):
        if len(self.cache)>300_000:
            self.cache={0:0}
        positions={}
        path=[]
        while n not in self.cache and n not in positions:
            if len(path)>=100_000 or n.bit_length()>8192:
                raise ValueError(f"unresolved trajectory at denominator {self.d}")
            positions[n]=len(path)
            path.append(n)
            n=step(n,self.d)
        self.largest_steps=max(self.largest_steps,len(path))
        if n in self.cache:
            label=self.cache[n]
        else:
            cycle=path[positions[n]:]
            label=min(cycle)
            rate=Fraction(sum(x%2 for x in cycle),len(cycle))
            if self.rates.setdefault(label,rate)!=rate:
                raise ValueError("inconsistent cycle density")
            if step(cycle[-1],self.d)!=cycle[0]:
                raise ValueError("invalid cycle")
        for v in path:
            self.cache[v]=label
        return label


def check(length):
    d=(1<<length)-1
    calculator=NumeratorOrbits(d)
    counts=Counter()
    genuine=[]
    rate_cases=Counter()
    for p in representatives(length):
        r=p
        left=set()
        right=set()
        aligned=False
        for _ in range(length):
            a=calculator.cycle(-r)
            b=calculator.cycle(d-r)
            left.add(a)
            right.add(b)
            if calculator.rates[a]==calculator.rates[b]>0:
                aligned=True
            r=2*r%d
        if 0 in left|right:
            kind="zero_shadow"
        elif left & right:
            kind="nonzero_cycles_with_cross_color_overlap"
        else:
            kind="signed_rational_wall"
            genuine.append(f"{p:0{length}b}")
        if aligned:
            rate_cases["equal_density_at_same_phase"]+=1
        elif {calculator.rates[x] for x in left if x} & {calculator.rates[x] for x in right if x}:
            rate_cases["equal_density_only_at_distinct_phases"]+=1
        else:
            rate_cases["no_positive_equal_density"]+=1
        counts[kind]+=1
    return {"primitive_necklaces":sum(counts.values()),**dict(sorted(counts.items())),
            "signed_wall_representatives":genuine,
            "phase_density_cases":dict(sorted(rate_cases.items())),
            "largest_uncached_path":calculator.largest_steps}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through",type=int,default=26)
    args=parser.parse_args()
    if args.through<2 or args.through%2:
        parser.error("--through requires an even integer at least two")
    data={k:check(k) for k in range(2,args.through+1,2)}
    if data[2].get("zero_shadow")!=1:
        raise ValueError("the alternating boundary should have a zero shadow")
    if any(v.get("zero_shadow",0) for k,v in data.items() if k>2):
        raise ValueError("unexpected zero shadow above period two")
    out={"schema":2,"through":args.through,"lengths":data}
    print(json.dumps(out,indent=2))


if __name__=="__main__":
    main()
