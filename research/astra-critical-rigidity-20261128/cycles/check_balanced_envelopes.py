"""Native low-envelope windows, balanced reference and exact reciprocal bounds."""
from fractions import Fraction
from itertools import product
from math import gcd
import json

from check_rotation_occupation import primitive_necklace, require, lifted, blocks


def displayed_states(word):
    """Allows repeated displayed phases, as the balanced reference may repeat."""
    p=len(word)
    D=2**sum(word)-3**p
    E=C=0
    for i,a in enumerate(word):
        C += 2**E*3**(p-1-i)
        E += a
    x=Fraction(C,D)
    out=[]
    for a in word:
        out.append(x)
        x=(3*x+1)/2**a
    require(x==out[0],"displayed closing rational")
    return out


def native(word, counts):
    source=lifted(word)
    if source is None:
        return
    q,ys=source
    p=len(word)
    A=sum(word)
    bal=tuple(((i+1)*A)//p-(i*A)//p for i in range(p))
    ref=displayed_states(bal)
    require(ref[0]==min(ref) and max(ref)<2*ref[0],"least balanced floor root and exact octave")
    counts["balanced_clocks"]+=1
    counts["imprimitive_balanced_displays"]+=len(set(ref))<p
    floor=min(ys)
    for ell in range(1,p):
        d=gcd(ell,p)
        M=p//d
        z=[min(ys[r::d]) for r in range(d)]
        orig=[ys.index(h) for h in z]
        changes=[r for r in range(d) if len(set(word[r::d]))>1]
        K=len(changes)
        actual_join=set()
        for r in range(d):
            dest=(3*z[r]+q)//2**word[orig[r]]
            if dest!=z[(r+1)%d]:
                actual_join.add(r)
                require(r in changes,"possible joins only on variable columns")
        for n in range(1,min(p,5)+2):
            excluded=0
            for r in range(d):
                if any((r+j)%d in actual_join for j in range(n-1)):
                    excluded+=1
                else:
                    require(all(z[(r+j)%d]==ys[(orig[r]+j)%p] for j in range(n)),
                            "full window matches at every observed ordinary phase")
                    counts["physical_envelope_windows"]+=1
            require(excluded<=K*(n-1),"cyclic boundary loss, including wraps")
        mass=sum(Fraction(floor,x) for x in ys)-sum(Fraction(floor,x) for x in z)
        for cap in sorted({floor,max(ys),q*p**7,2*q,ys[p//2]}):
            T=cap.bit_length()-1
            good=set()
            for start,L in blocks(changes,d):
                if L>T:
                    good.update((start+j)%d for j in range(L))
            require(all(sum(h<=cap for h in ys[r::d])<=1 for r in good),
                    "no second low track on a good column")
            require(0<=mass<= (M-1)*K*T+(p-d)*Fraction(floor,cap),
                    "exact total reciprocal loss")
            counts["reciprocal_mass_caps"]+=1
        counts["envelope_rotations"]+=1
        counts["physical_join_switches"]+=len(actual_join)


def main():
    counts={k:0 for k in ("balanced_clocks","imprimitive_balanced_displays","envelope_rotations",
                          "physical_envelope_windows","reciprocal_mass_caps","physical_join_switches")}
    for p in range(2,7):
        for w in product((1,2,3),repeat=p):
            if primitive_necklace(w):
                native(w,counts)
    for w in [(1,2,1,3,1,2,1,12),(2,1,3,2,1,3,2,1,29),(1,1,2,2,1,2,1,1,2,2,1,51)]:
        native(w,counts)
    require(all(counts.values()),"all reported native regimes reached")
    return counts


if __name__=="__main__":
    print(json.dumps(main(),indent=2,sort_keys=True))
