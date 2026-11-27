"""Finite tests for octave transport, the signed target and all-height cutoffs."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
import json


def require(test, detail):
    if not test:
        raise ArithmeticError(detail)


def v3(a):
    v = 0
    while a % 3 == 0:
        a //= 3
        v += 1
    return v


def odd_step(x):
    w = 3*x+1
    e = (w & -w).bit_length()-1
    return w >> e, e


def native(x):
    return x//2 if x%2==0 else (3*x+1)//2


def script_probabilities(max_d):
    # Independent forward update of the finite residue law. Powers of two
    # have period 2*3^(d-1), so the entire infinite exponent law is included.
    rows = [[Fraction(1)]]
    for d in range(1,max_d+1):
        mod = 3**d
        period = 2*3**(d-1)
        numerators = [Fraction(0) for _ in range(mod)]
        for e in range(1,period+1):
            inv = pow(pow(2,e,mod),-1,mod)
            factor = Fraction(1 << (period-e),(1<<period)-1)
            for r,v in enumerate(rows[-1]):
                numerators[(3*r+1)*inv % mod] += v*factor
        require(sum(numerators)==1,"total depth mass")
        require(max(numerators)<=Fraction(2,3)**d,"basic residue envelope")
        require(numerators[-1] <= Fraction(10*(d+1)**2,1<<d),"signed residue envelope")
        rows.append(numerators)
    return rows


def check_transport(rows):
    counts = Counter()
    for k in range(5,11):
        source_count = 1 << (k-1)
        seeds = range((1<<k)+1,1<<(k+1),2)
        parity_blocks = Counter()
        for start in seeds:
            x=start
            bits=[]
            for _ in range(k):
                bits.append(x % 2)
                x=native(x)
            parity_blocks[tuple(bits)]+=1
        require(len(parity_blocks)==source_count and set(parity_blocks.values())=={1},
                "all native words equiprobable")
        counts["uniform_octaves"]+=1
        for j in range(4):
            cutoff=k-2
            mass=Counter()
            words={}
            for n in seeds:
                y=n
                gaps=[]
                for _ in range(j):
                    y,e=odd_step(y)
                    gaps.append(e)
                if sum(gaps)>cutoff:
                    continue
                words.setdefault(tuple(gaps),[]).append((n,y))
                for d in range(5):
                    mass[d,y%3**d]+=1
            total = 0
            for w,values in words.items():
                E=sum(w)
                total+=Fraction(1,1<<E)
                require(len(values)==1<<(k-E-1),"word count in octave")
                require(all(n2-n1==1<<(E+1) and y2-y1==2*3**j
                            for (n1,y1),(n2,y2) in zip(values,values[1:])),
                        "paired source and target strides")
                counts["exact_word_progressions"]+=1
            require(total==Fraction(mass[0,0],source_count),"truncation mass")
            for d in range(5):
                for r in range(3**d):
                    p=Fraction(mass[d,r],source_count)
                    bound=rows[d][r] if d<=j else (
                        rows[j][r%3**j]/3**(d-j)+Fraction(1,1<<(k-cutoff-1)))
                    require(p<=bound,"finite two-depth ordinary subprobability")
                    counts["ordinary_residue_comparisons"]+=1
    return counts


def check_signed():
    counts=Counter()
    for d in range(1,7):
        # Enumerate only legal reverse steps and check the exact word telescope.
        queue=[(1,0,Fraction(1),())]
        for _ in range(d):
            following=[]
            for y,E,w,history in queue:
                for e in range(1,6*d-E+1):
                    a=(1<<e)*y+1
                    if a%3:
                        continue
                    x=a//3
                    require(x%2==1 and ((3*x-1)>>e)==y and ((3*x-1)>>e)%2==1,"actual signed gap")
                    following.append((x,E+e,w*Fraction(3*x,3*x-1),history+(x,)))
            queue=following
        starts=set()
        for x,E,W,history in queue:
            require(x not in starts,"ambiguous signed source")
            starts.add(x)
            nonones=[u for u in history if u>1]
            require(len(set(nonones))==len(nonones),"repeated offcycle source")
            require(W/x==Fraction(3**d,1<<E),"negative telescoping identity")
            require(W <= (d+1)*Fraction(3,2)**d and x<=1<<E,"negative real bound")
        counts["distinct_small_division_signed_sources"]+=len(starts)
    return counts


def check_height_cutoff():
    # Use entirely integral threshold 3^v > (2h)^m, then compare the
    # archimedean height-cut count with direct enumeration up to 128.
    count=Counter()
    for n in range(1,256,2):
        for m in (2,3,4):
            full=set()
            restricted=set()
            for h in range(1,129):
                for p,q in [(h,j) for j in range(1,h+1)]+[(j,h) for j in range(1,h)]:
                    if q%3==0 or gcd(p,q)>1:
                        continue
                    if 3**v3(q*n+p) <= (2*h)**m:
                        continue
                    full.add((p,q))
                    if (2*h)**m<h*(n+1):
                        restricted.add((p,q))
            require(full==restricted,"all-height cutoff")
            count["exact_height_cutoff_tests"]+=1
            count["above_threshold_rationals"]+=len(full)
    for k in range(1,41):
        s=k.bit_length()**2+1
        n=(1<<(k+1))*3**s-1
        x=n
        for j in range(k+1):
            require(x+1==(1<<(k+1-j))*3**(s+j),"pointwise time obstruction")
            count["finite_pointwise_obstruction_states"]+=1
            if j<k:
                x,e=odd_step(x)
                require(e==1,"long initial one string")
    return count


if __name__ == "__main__":
    rows=script_probabilities(5)
    result=Counter({"exact_geometric_residue_masses":sum(map(len,rows))})
    result.update(check_transport(rows))
    result.update(check_signed())
    result.update(check_height_cutoff())
    print(json.dumps(dict(sorted(result.items())),sort_keys=True,indent=2))
