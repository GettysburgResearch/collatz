"""Finite controls for the nested-power torus calculation, with exact slope signs."""

from fractions import Fraction
from itertools import product
from math import gcd, log


def need(condition, message):
    if not condition:
        raise ValueError(message)


def leaf(bit):
    return (1,bit,bit)


def concat(a,b):
    n,u,c = a
    m,v,d = b
    return (n+m,u+v,3**v*c + 2**n*d)


def power(a,k):
    n,u,c = a
    lo,hi = 3**u,2**n
    return (n*k,u*k,c*((hi**k-lo**k)//(hi-lo)))


def nodes(k,h,l,b):
    zero,one=leaf(0),leaf(1)
    a=concat(zero,one)
    c=concat(concat(one,one),zero)
    e=concat(one,c)
    ak,ch=power(a,k),power(c,h)
    cell=concat(ak,ch)
    outer,tail=power(cell,l),power(e,b)
    root=concat(outer,tail)
    return [zero,one,a,c,e,ak,ch,cell,outer,tail,root]


def rational_sign(twos,threes):
    positive = 2**max(twos,0)*3**max(threes,0)
    negative = 2**max(-twos,0)*3**max(-threes,0)
    return (positive>negative)-(positive<negative)


def check():
    base=nodes(3,2,3,2)
    n0,u0,_=base[-1]
    tested=0
    for k,h,l in product(range(2,18),range(2,11),range(2,18)):
        length=(2*k+3*h)*l
        count=(k+2*h)*l
        b=int((length*log(2)-count*log(3))/(3*log(3)-4*log(2)))
        if b<2:
            continue
        xs=nodes(k,h,l,b)
        n,u,carry=xs[-1]
        # Floating logarithms only select a candidate tail; the accepted gap
        # is certified here by 1 < 2^n/3^u < 101/100, hence 0 < gap < 0.01.
        if n<=5*n0 or gcd(n,u)!=1 or not (3**u < 2**n and 100*2**n < 101*3**u):
            continue
        # Compare all deformed real multipliers by integer exponentiation.
        signs=[]
        for (m,v,_),(m0,_,_) in zip(xs,base):
            d=n*v-u*m
            got=rational_sign(n0*m-n*m0, (n-n0)*v-u*(m-m0))
            need(got==(d>0)-(d<0),'unexpected deformed determinant sign')
            signs.append(got)
        for child,parent in [(2,5),(3,6),(7,8),(4,9)]:
            need(signs[child]==signs[parent]!=0,'geometric factor lost positivity')
        word=(((0,1)*k+(1,1,0)*h)*l+(1,1,1,0)*b)
        literal=(0,0,0)
        for letter in word:
            literal=concat(literal,leaf(letter))
        need(literal==xs[-1],'compressed carry disagrees with word')
        d=2**n-3**u
        need(Fraction(carry,d).denominator==d//gcd(d,carry),'denominator mismatch')
        tested+=1
    need(tested>=3,'too few nested-power controls')
    print(f'{tested} coprime nearcritical nested-power expressions verified')


if __name__=='__main__':
    check()
