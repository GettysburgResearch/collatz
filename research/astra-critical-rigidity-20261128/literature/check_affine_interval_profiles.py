"""Exact finite controls for canonical, numerical and offset-averaged comparisons."""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb
import json


def require(value, label):
    if not value:
        raise ArithmeticError(label)


@lru_cache(maxsize=None)
def word(r,t):
    x=r
    grade=0
    carry=0
    grades=[0]
    for date in range(t):
        if x%2:
            x=(3*x+1)//2
            grade+=1
            carry=3*carry+(1<<date)
        else:
            x//=2
        grades.append(grade)
    require(carry<=3**grade*2**(t-grade), "late-odds carry bound")
    return grade,carry,grades


def endpoints(report):
    for t in (5, 9, 13):
        period=1<<t
        for s in (1, 3, 6):
            factor=3**s
            for offset in (0,1,-7,factor*period,11**(t+1),-11**(t+1)):
                for start in (1,29,3*period+1):
                    lo=max(start,1-offset//factor)
                    count=2*period//3+19
                    for x in range(lo,lo+count):
                        a,c1,_=word(x%period,t)
                        y=factor*x+offset
                        b,c2,_=word(y%period,t)
                        lhs=3**a*x+c1
                        rhs=3**b*y+c2
                        if lhs==rhs:
                            if a==b+s:
                                require(c1-c2==3**b*offset,"balanced offset identity")
                                report["balanced_numerical_mergers"]+=1
                            else:
                                radius=Fraction(3,2)*(Fraction(c1,3**a)+Fraction(c2,3**b))
                                center=Fraction(3**b*offset,3**a-3**(s+b))
                                require(abs(x-center)<=radius,"grade-center interval")
                                report["accidental_numerical_mergers"]+=1
                        report["tested_numerical_pairs"]+=1


def signed_window(report):
    for t,h in ((7,3),(9,4),(12,5)):
        modulus=2**t
        s=max(1,h//2)
        aggregate=Counter()
        for offset in range(2**h,2**(h+1)):
            full=Counter()
            early=Counter()
            for x in range(modulus):
                g1=word(x,t)[2]
                g2=word((3**s*x+offset)%modulus,t)[2]
                signed=[s+b-a for a,b in zip(g1,g2)]
                aggregate[(g1[h],g2[h])]+=1
                good=all(z!=0 for z in signed[h:])
                ge=all(z!=0 for z in signed[h:-2])
                require(not good or ge,"nested first-future-zero certificates")
                full[x]=int(good)
                early[x]=int(ge)
                report["negative_signed_ranks"]+=signed[h]<0
                report["protected_continuations"]+=good
            require(all(early[x]==early[(x+(1<<(t-2)))%modulus] for x in range(modulus)),
                    "coarse exact certificate period")
            for origin in (0,17,4*modulus+13):
                length=modulus+31
                empirical=sum(full[(origin+i)%modulus] for i in range(length))
                delta=sum(early.values())-sum(full.values())
                lower=(length*Fraction(sum(early.values()),modulus)
                       -(1<<(t-2))-(length//modulus+1)*delta)
                require(empirical>=lower,"arbitrary-origin survivor transfer")
                report["fine_coarse_interval_checks"]+=1
        for a in range(h+1):
            for b in range(h+1):
                expected=(1<<(t-h))*comb(h,a)*comb(h,b)
                require(aggregate[a,b]==expected,"independent initial binary grade census")
                report["independent_grade_cells"]+=1


def main():
    report=Counter()
    endpoints(report)
    signed_window(report)
    require(report["accidental_numerical_mergers"]>0,"exercise unequal slopes")
    require(report["negative_signed_ranks"]>0,"exercise slope reversals")
    print(json.dumps(dict(report),sort_keys=True,indent=2))


if __name__=="__main__":
    main()
