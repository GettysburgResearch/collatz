"""Exact finite inverse-branch subeigenvector and source-payoff checks."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
import json


def check(ok,tag):
    if not ok:
        raise ArithmeticError(tag)


def lower_vector():
    # The table stores 2^(10*t) times path mass times the terminal unit weight.
    # At t remaining backward steps, the initial unit is known modulo 3^(t+1).
    # The argument need is the still-required total number of binary divisions.
    @lru_cache(maxsize=None)
    def weight(t,y,need):
        if t==0:
            return (1 if y%3==1 else 2)*int(need==0)
        mod=3**(t+1)
        result=0
        for e in range(1,11):
            v=((y<<e)-1)%mod
            if v%3 or v%9==0:
                continue
            child=v//3
            result+=weight(t-1,child,max(0,need-e))<<(10-e)
        return result
    M=3**9;minimum=None;worst=None;hist=Counter()
    for y in range(1,M):
        if y%3==0:continue
        initial_weight=1 if y%3==1 else 2
        ratio=Q(weight(8,y,13),initial_weight*(1<<80))
        if minimum is None or ratio<minimum:
            minimum=ratio;worst=y
        hist[y%3]+=1
    c=Q(2369,10000)
    check(minimum>c**8,'eight-step positive lower operator')
    check(2**13>3**8 and Q(1,1)-Q(3**8,2**13)>Q(1,8),'endpoint expansion margin')
    check(Q(3,2)**8-1<25 and Q(3,2)**8<32,'all intermediate physical floors')
    check(Q(3,2)**8-1 < (1-Q(3**8,2**13))*256,'one-block endpoint increases')
    probability=Q(comb(895,511),512*(1<<896))
    check(probability>Q(19,20)**512,'512-word-block positive gate mass')
    check(c**3*81*Q(19,20)>1,'high-floor Holder separation diverges at four-thirds')
    return dict(most_adverse_ternary_unit=worst,exact_minimum_ratio=str(minimum),
                declared_single_letter_lower='2369/10000',unit_states_by_low_digit=dict(hist),
                subeigenvector=[1,2],blocks=8,allowed_letters=list(range(1,11)),
                minimum_total=13,gate_block_length=512,gate_probability_floor='(19/20)^512',
                cubed_four_thirds_growth_floor=str(c**3*81*Q(19,20)))


def source_checks():
    counts=Counter()
    for n in range(1,7):
        # Literal actual inverse on principal ternary representatives.
        from itertools import product
        for w in product(range(1,5),repeat=n):
            A=B=0
            for e in w:
                B=3*B+(1<<A);A+=e
            mod=1<<(A+1)
            # 3^n m+B must be exactly 2^A times an odd number.
            m=((1<<A)-B)*pow(3**n,-1,mod)%mod
            y=((3**n)*m+B)>>A
            check(0<m<mod and m%2 and y%2,'actual principal representatives')
            x=m; factor=Q(1)
            for e in w:
                factor*=1+Q(1,3*x)
                v=3*x+1
                check(v&-v==1<<e,'specified actual valuation')
                x=v>>e
            Z=Q(1<<A,m)
            check(x==y and Z==Q(3**n,y)*factor and Q(1,2)<Z<=4**n,'exact ordinary source pressure interface')
            check((Z==4**n)==(w==(2,)*n),'unique extremal word')
            counts['exact_physical_words']+=1
    # True physical high terminal and arbitrary winding true original +1 binary/ternary shadows.
    examples=[]
    for n in range(1,25):
        t=3*n;A=5*n
        u=next(u for u in range(1,5) if (23+(u<<(A+1)))%5==0)
        m=(23+(u<<(A+1)))//5;expected=(23+2*u*27**n)//5
        check(0<m<1<<(A+1),'principal guarded shadow')
        x=m;floor=m;k=0
        for i in range(t):
            e=(1,2,2)[i%3]
            k+=e
            check(4*k<=7*(i+1),'true full prefix gate')
            z=3*x+1
            check(z&-z==1<<e,'unmodified +1 dynamics')
            x=z>>e;floor=min(floor,x)
        check(x==expected and floor>=2*27**n//5,'whole shadow physical floor')
        check((5*m-23)%(1<<(A+1))==0 and (5*x-23)%27**n==0,'same rational two-adic and three-adic projection')
        counts['joint_adic_high_original_windows']+=1
        if n<=4:examples.append(dict(laps=n,initial=m,terminal=x,u=u))
    return dict(counts=counts,first_joint_shadow_examples=examples)


if __name__=='__main__':
    print(json.dumps(dict(inverse_lower_table=lower_vector(),sources=source_checks()),sort_keys=True,indent=2))
