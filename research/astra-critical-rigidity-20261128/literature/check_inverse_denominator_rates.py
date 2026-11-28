"""Test synchronized integer Fourier profiles, physical word APs, and the totient intervals."""

from collections import Counter
from fractions import Fraction
from math import gcd
import sys
from sympy import Poly, Symbol, ZZ, divisors, mobius, totient

sys.dont_write_bytecode=True
from check_prime_power_spectra import cycle,verify


def profiles(g,orders):
    return [sum(sum(int(e*mobius(d//e)) for e in divisors(gcd(d,i)))
                for d in orders if d>1) for i in range(g)]


def motif_words():
    bycarry={}
    for source in range(2987,3001):
        state=source
        word=[]
        for t in range(34):
            if state%2:
                word.append(t)
                state=(3*state+1)//2
            else:
                state//=2
        verify(state==1 and len(word)==14,"explicit equal clocks, grade and target")
        bycarry[2**34-3**14*source]=word
    items=sorted(bycarry.items())
    verify(all(y[0]-x[0]==3**14 for x,y in zip(items,items[1:])),"literal AP")
    return items


def main():
    stats=Counter()
    X=Symbol("X")
    motifs=motif_words()
    for g in (2,3,4,5,6,8,9,10,12):
        ds=list(divisors(g))
        for mask in range(2**(len(ds)-2)):
            orders=[1,g]+[d for j,d in enumerate(ds[1:-1]) if mask>>j&1]
            k=sum(int(totient(d)) for d in orders)
            profile=profiles(g,orders)
            low=min(profile)
            verify(max(profile)-low<len(motifs) and sum(profile)==0,"available AP range")
            for extension in (0,2):
                r=14+extension
                n=42
                B=0
                pos=[]
                for i,value in enumerate(profile):
                    carry,word=motifs[value-low]
                    for t in range(34,34+extension):
                        carry=3*carry+2**t
                    B+=carry*3**(r*(g-1-i))*X**i
                    pos.extend(i*n+t for t in (*word,*range(34,34+extension)))
                F=Poly(X**g-3**(r*g),X,domain=ZZ)
                G=F.gcd(Poly(B,X,domain=ZZ))
                verify(F.degree()-G.degree()==k,"integer Fourier-root degree")
                cycle(pos,g*n,stats)
                stats["physical_fourier_profiles"]+=1
    for N in range(3,100,2):
        a=max(1,(int(totient(N))-1).bit_length())
        g=(2**a)*N
        weights=1<<1
        for d in divisors(g):
            if d not in (1,g):
                weights|=weights<<int(totient(d))
        weights<<=int(totient(g))
        lower=1+int(totient(g))
        verify(weights==((1<<(g+1))-(1<<lower)),"full mandatory divisor interval")
        stats["complete_totient_intervals"]+=1
        stats["integer_numerators_in_intervals"]+=g-lower+1
    for name in sorted(stats):
        print(f"{name}={stats[name]}")


if __name__=="__main__":
    main()
