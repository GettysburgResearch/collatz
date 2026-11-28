"""Finite exact controls for the critical tower endpoints and marked families."""

from collections import Counter
from fractions import Fraction
from math import comb
import json


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def shortcut(value):
    return (3*value + 1)/2 if value.numerator % 2 else value/2


def word(x, horizon):
    g, carry = 0, 0
    for date in range(horizon):
        if x%2:
            g += 1
            carry = 3*carry + (1<<date)
            x=(3*x+1)//2
        else:
            x//=2
    return g, carry


def grade_history(x,t):
    g=0
    out=[0]
    for _ in range(t):
        g+=x%2
        x=(3*x+1)//2 if x%2 else x//2
        out.append(g)
    return out


def reflection(report):
    for initial in range(1,10):
        for horizon in range(1,23):
            counts={initial:1}
            for _ in range(horizon):
                nxt=Counter()
                for h,mass in counts.items():
                    nxt[h+1]+=mass
                    if h>1:
                        nxt[h-1]+=mass
                counts=nxt
            reflected=sum(comb(horizon,i) for i in range(horizon+1)
                          if -initial < 2*i-horizon <= initial)
            require(reflected==sum(counts.values()),"walk reflection survival")
            report["exact_reflection_laws"]+=1


def critical_fibres(report):
    for t in (8,11,14,16):
        modulus=2**t
        base=2*t+5
        n_count=modulus//2+37
        for direction in (-1,1):
            for c,m in ((0,1),(1,2),(-2,3)):
                labels=[]
                for n in range(base,base+n_count):
                    x=(c+m*pow(3,direction*n,modulus))%modulus
                    g,carry=word(x,t)
                    labels.append((direction*n+g,3**g*c+carry))
                fibres=Counter(labels)
                n2=sum(mass**2 for mass in fibres.values())
                collisions=sum(sum(a==b for a,b in zip(labels,labels[k:]))
                               for k in range(1,t+1))
                require(n2==n_count+2*collisions,"all-lag fibre sum")
                require(max(fibres.values())<=t+1,"coincident high exponents")
                report["visited_high_exponents"]+=n_count
                report["equal_ordered_pairs"]+=n2
                for k in (1,2,4,6):
                    found=0
                    for n in range(n_count-k):
                        if labels[n]==labels[n+k]:
                            missing=sum(x!=labels[n] for x in labels[n+1:n+k])
                            found+=1
                            report["missing_interiors_on_outer_agreement"]+=missing
                    report["outer_agreements"]+=found
                for n in range(base,base+12):
                    x=c+m*Fraction(3)**(direction*n)
                    for _ in range(t):
                        x=shortcut(x)
                    level,offset=labels[n-base]
                    predicted=(m*Fraction(3)**level+offset)/modulus
                    require(x==predicted,"actual numerical endpoint label")
                    report["exact_rational_label_checks"]+=1


def ordered_crossings(report):
    t=14
    for c in (-2,0,1,4):
        for x in range(800):
            for k in (2,4,7):
                histories=[grade_history((c+3**i*(x-c))%(2**t),t)
                           for i in range(k+1)]
                meets=[j for j in range(t+1) if histories[0][j]==k+histories[k][j]]
                if meets:
                    u=meets[0]
                    for i in range(1,k):
                        touched=any(histories[0][j]==i+histories[i][j] or
                                    i+histories[i][j]==k+histories[k][j]
                                    for j in range(u+1))
                        require(touched,"intermediate adjusted grade crossed an endpoint")
                        report["verified_interior_rank_crossings"]+=1
    actual=[Fraction(3**i) for i in range(19,24)]
    for _ in range(16):
        actual=[shortcut(x) for x in actual]
    expected=[116357384,116357384,349072151,3141649355,116357384]
    require([int(x) for x in actual]==expected,"explicit failed whole block")
    report["explicit_actual_block"]=expected


def capped_hold_bias(report):
    def valuation(x):
        x=abs(x)
        return (x & -x).bit_length()-1
    def eta(e,x):
        return e+1 if x==0 or valuation(x)>=e else valuation(x)
    for cap in range(3,9):
        for s in range(3,48,2):
            total=0
            for d in range(1,2**(cap+2),2):
                plus=(3*d+1)//2
                minus=(d-3**(s-1))//2
                total+=eta(min(cap,valuation(3**(s+1)-1)),plus)
                total+=eta(min(cap,valuation(3**(s-1)-1)),minus)
            require(total==2**(cap+2), "zero mean clipped holding bias")
            report["verified_capped_holding_means"]+=1


def main():
    report=Counter()
    reflection(report)
    capped_hold_bias(report)
    critical_fibres(report)
    ordered_crossings(report)
    print(json.dumps(dict(report),sort_keys=True,indent=2))


if __name__=="__main__":
    main()
