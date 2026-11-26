"""Independent ordinary rational replay for the paired cyclic-word construction."""

if not __debug__:
    raise SystemExit("This independent assertion-based replay requires Python without -O or -OO.")

from fractions import Fraction
from itertools import combinations
import json

blocks=(("10","01"),("010","100"),("110100000001","000001110100"))

def shortcut(x):
    assert x.denominator & 1
    return (3*x+1)/2 if x.numerator&1 else x/2

def cycle(word):
    N,q=len(word),word.count("1")
    positions=[j for j,e in enumerate(word) if e=="1"]
    carry=sum(3**(q-1-i)*2**j for i,j in enumerate(positions))
    x=Fraction(carry,2**N-3**q)
    values=[]
    y=x
    for e in word:
        assert y>0 and y.numerator%2==int(e)
        values.append(y)
        y=shortcut(y)
    assert y==x and len(set(values))==len(word)
    return x,values

def main():
    input_cycles=set()
    output_cycles=set()
    cases=phases=raw_clock_groups=shared=0
    for length in range(2,11):
        for a in range(1,length):
            dcount={}
            for a_places in combinations(range(length),a):
                ids=[int(t not in a_places) for t in range(length)]+[2]
                W,V=("".join(blocks[i][j] for i in ids) for j in range(2))
                X,src=cycle(W); Y,dst=cycle(V); q=src[-1]
                assert X<=1 and q.numerator%2==1
                assert Y==3*X-1 and shortcut(3*q)==Y
                assert 3*q not in src and 3*q not in dst
                assert not set(src).intersection(dst)
                assert len({z.denominator for z in src+dst+[3*q]})==1
                ic,oc=min(src),min(dst)
                assert ic not in input_cycles and oc not in output_cycles
                input_cycles.add(ic); output_cycles.add(oc)
                dcount[X.denominator]=dcount.get(X.denominator,0)+1
                cases+=1; phases+=2*len(W)
            shared=max(shared,max(dcount.values()))
            raw_clock_groups+=1
    assert input_cycles.isdisjoint(output_cycles)
    examples=[]
    for L,mod in ((4,5),(24,35),(240,385)):
        b=(-6)%L
        a=(-3-b)%L
        a+=20*L; b+=20*L
        N,p=2*a+3*b+12,a+b+4
        assert N%L==0 and (p-1)%L==0
        assert (pow(2,N,mod)-pow(3,p,mod))%mod==(-2)%mod
        examples.append(dict(modulus=mod,a=a,b=b,n=N,odd=p))
    print(json.dumps(dict(word_orderings=cases,all_positive_rational_phases=phases,
               input_cycles=len(input_cycles),output_cycles=len(output_cycles),
               raw_clock_groups=raw_clock_groups,largest_common_reduced_denominator_fiber=shared,
               congruence_cases=examples),indent=2))

if __name__=="__main__":
    main()
