#!/usr/bin/env python3
"""Exact scoped controls; no universal candidate construction."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def require(test, message):
    if not test:
        raise RuntimeError(message)


def step(x):
    return x//2 if x % 2 == 0 else (3*x+1)//2


def rational_parity(y):
    require(y.denominator % 2 == 1, 'odd denominator required')
    return y.numerator % 2


def rational_step(y):
    return y/2 if rational_parity(y) == 0 else (3*y+1)/2


def own_horizon(n, y):
    a, d = y.numerator, y.denominator
    r=0
    while d % 3 == 0:
        d//=3
        r+=1
    require(d == 1, 'not triadic')
    weight=1
    for j in range(r):
        weight*=1+3**j
    return 9*(n*max(1,abs(a))*weight).bit_length()+1


def complement_integer(n, length):
    d=b=0
    x=n
    for i in range(length):
        e=x % 2
        d=3**(1-e)*d+(1-e)*2**i
        b+=1-e
        x=step(x)
    modulus=2**length
    u=(-d*pow(3**b,-1,modulus)) % modulus if length else 0
    return u if u else modulus


def lifting_control(n, length):
    u=complement_integer(n,length)
    r=1
    while 2**r*(u+1) >= 3**r:
        r+=1
    initial_n=2**r*n
    y0=Fraction(2**r*(u+1)-3**r,3**r)
    require(r>=2 and Fraction(-1,3)<y0<0,'initial interval')
    x=initial_n
    y=y0
    for j in range(r):
        require(x == 2**(r-j)*n,'literal original state')
        require(y == Fraction(2,3)**(r-j)*(u+1)-1,'literal dual state')
        require(x % 2 == 0 and rational_parity(y) == 1,'lift parity')
        x=step(x);y=rational_step(y)
        if j==0:
            require(0<y<Fraction(1,2),'first sign crossing')
    require(x==n and y==u,'unchanged target')
    for _ in range(length):
        require(x % 2 != rational_parity(y),'continuation parity')
        x=step(x);y=rational_step(y)
    return dict(target=n,extra_prefix=length,terminal_integer=str(u),
                lift_steps=r,initial_n=str(initial_n),initial_dual=str(y0),
                passed_prefix=r+length,own_horizon=own_horizon(initial_n,y0))


def true_dual_control(n):
    xs=[n]
    while xs[-1] != 1:
        require(len(xs)<10000,'control orbit bound exceeded')
        xs.append(step(xs[-1]))
    ys=[Fraction(2)]
    for x in reversed(xs[:-1]):
        y=ys[-1]
        ys.append(2*y if x % 2 else (2*y-1)/3)
    ys.reverse()
    tau=len(xs)-1
    b=sum(x % 2 == 0 for x in xs[:-1])
    y=ys[0];a=y.numerator;den=y.denominator;r=0
    while den % 3 == 0:
        den//=3;r+=1
    require(den==1,'true dual localization')
    for x,y_at,next_y in zip(xs,ys,ys[1:]):
        require(x % 2 != rational_parity(y_at),'true parity')
        require(rational_step(y_at)==next_y,'true trajectory')
    if n>2:
        require(r==b-1,'denominator clock')
        require(tau-r-1>=0,'odd count')
        left=n*3**(tau-r-1)
        right=2**tau
        require(left<=right,'affine clock')
        require((left==right)==(n==2**tau),'zero carry endpoint')
    if n not in (1,2,4):
        require(a<0 and r>=2,'true sign')
        require(xs[tau-3]==8 and ys[tau-3]==Fraction(-1,9),'negative terminal')
        require(all(z<0 for z in ys[:tau-2]),'negative sector')
        require(8*3**r*6**(tau-3)<=9*n*abs(a)*5**(tau-3),'negative budget')
    return dict(n=n,first_hit=tau,even_count=b,reduced_exponent=r,
                numerator=str(a),dual=str(ys[0]))


def reset_control(a,r):
    require(a>0 and a%3!=0 and r>=1,'reduced positive reset source')
    w=a
    initial_halves=0
    while w%2==0:
        w//=2;initial_halves+=1
    original_w=w
    factors=Fraction(1)
    clock=0
    blocks=[]
    for j in range(r,0,-1):
        require(w%2==1,'odd level numerator')
        value=w+3**(j-1)
        k=(value & -value).bit_length()-1
        next_w=value//2**k
        require(k>=1 and 2**k*next_w==w+3**(j-1),'block identity')
        if w==1:
            require(k==(1 if (j-1)%2==0 else 2),'linked small reset')
        factors*=Fraction(w+3**(j-1),w)
        blocks.append(dict(exponent=j,numerator=str(w),steps=k,next_numerator=str(next_w)))
        w=next_w
        clock+=k
    require(Fraction(2**clock)==Fraction(original_w,w)*factors,'global product')
    return dict(a=a,r=r,initial_halves=initial_halves,compressed_clock=clock,
                terminal_odd_integer=str(w),blocks=blocks)


def main():
    targets=[1,2,3,4,7,8,27,97,871]
    lifts=[lifting_control(n,L) for n in targets for L in (0,1,2,5,13,64)]
    duals=[true_dual_control(n) for n in (1,2,3,4,5,7,8,16,27,97,871,6171)]
    resets=[reset_control(a,r) for a in (1,2,5,8,17,64) for r in (1,2,5,10,20)]
    x,y=16,Fraction(-1,9)
    control=[]
    for _ in range(3):
        require(x % 2 != rational_parity(y),'short control parity')
        control.append([x,str(y)])
        x=step(x);y=rational_step(y)
    require((x,y)==(2,Fraction(2)) and x%2==rational_parity(y),'short failure')
    control.append([x,str(y)])
    note=Path(__file__).with_name('CARRY_CONSTRUCTION_ATTACK.md')
    print(json.dumps(dict(schema='collatz-carry-construction-controls/v1',
        scope='Selected exact finite controls for symbolic scope results; no universal certificate search.',
        note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),
        lifts=lifts,true_duals=duals,positive_resets=resets,short_control=control,
        counts=dict(lifts=len(lifts),true_duals=len(duals),positive_resets=len(resets))),indent=2,sort_keys=True))


if __name__=='__main__':
    main()
