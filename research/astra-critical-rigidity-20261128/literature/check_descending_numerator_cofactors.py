"""Test signed rational landing and the exact local ingredients of the cofactor proof."""

from collections import Counter
from fractions import Fraction
from math import gcd


def require(test, detail):
    if not test:
        raise ArithmeticError(detail)


def v(n, prime):
    n=abs(n)
    require(n!=0,"nonzero valuation")
    out=0
    while n%prime==0:
        n//=prime
        out+=1
    return out


def shortcut(x):
    return (3*x+1)/2 if x.numerator%2 else x/2


def path(b,q,n,stats):
    x=Fraction(b,q*3**n)
    native_time=0
    marks=[]
    while x.denominator!=q:
        if x.numerator%2:
            h=v(x.denominator,3)
            require(h==n-len(marks) and x.denominator==q*3**h,"physical reduced level")
            require(gcd(abs(x.numerator),6*q)==1,"unit odd numerator")
            marks.append((h,native_time,x.numerator))
        x=shortcut(x)
        native_time+=1
        require(native_time<100000,"finite control domain")
    require(len(marks)==n,"all levels observed")
    stats["negative_to_nonnegative_landing"]+=int(b<0 and x>=0)
    stats["zero_landings"]+=int(x==0)
    for start,(h,s,u) in enumerate(marks):
        for end in range(start+1,min(len(marks),start+8)):
            k=end-start
            hh,e,uu=marks[end]
            d=e-s
            V=sum(2**(time-s)*3**(k-1-i) for i,(_,time,_) in enumerate(marks[start:end]))
            require(hh==h-k and 2**d*uu-u==q*3**hh*V,"collapsed all-positive carry")
            require(0<V<=k*2**d*3**k,"native time and coefficient bound")
            if u>0:
                require(2**d*uu>=q*3**(h-1),"real lower bound")
            if u<0 and abs(u)<q*3**(h-1):
                require(uu>0,"negative real-small input flips once")
                stats["signed_flip_intervals"]+=1
            for prime in (5,7,11,13):
                exponent=min(v(u,prime),v(uu,prime))
                if exponent:
                    require(q%prime and V%prime**exponent==0,"common valuation lies in V")
                    stats["nontrivial_fixed_prime_intervals"]+=1
            stats["signed_intervals_checked"]+=1
    stats["signed_sources"]+=1
    stats["actual_odd_departures"]+=len(marks)
    stats["max_denominator_bits"]=max(stats["max_denominator_bits"],(q*3**n).bit_length())


def main():
    stats=Counter()
    for q in (1,5,7,25,35,5**12*7**5,5**83,7**110):
        for n in (1,2,5,9,17,31):
            bvalues=range(-45,46) if n<=9 else (-37,-23,-1,1,17,23,37)
            for b in bvalues:
                if gcd(b,q*3)==1:
                    path(b,q,n,stats)
            for exp in (2,7):
                for shift in (-1,1):
                    b=2**(n*exp)*q+shift
                    if gcd(b,3*q)==1:
                        path(b,q,n,stats)
                        path(-b,q,n,stats)
    for key,count in sorted(stats.items()):
        require(count>0,key)
        print(f"{key}={count}")


if __name__=="__main__":
    main()
