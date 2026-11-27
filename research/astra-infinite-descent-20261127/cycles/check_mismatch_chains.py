"""Native paired-quotient identities and all-subsum checks on exact rational cycles."""
from collections import Counter
from itertools import combinations
from math import gcd
import json
from check_cycle_rotations import necklaces,rational_labels


def require(ok, message):
    if not ok:
        raise ValueError(message)


def v3(n):
    j=0
    while n%3==0:
        n//=3
        j+=1
    return j


def controls(e,ys,q,lag,totals):
    p=len(e)
    end=[i for i in range(p) if e[i]!=e[(i+lag)%p]]
    s=len(end)
    if s==0:
        return
    blocks=[]
    for k,i in enumerate(end):
        prev=end[k-1]
        L=(i-prev)%p
        m=min(e[i],e[(i+lag)%p])
        A=m+sum(e[(prev+t)%p] for t in range(1,L))
        u,v=e[i]-m,e[(i+lag)%p]-m
        old=ys[(prev+1)%p]
        other=ys[(prev+1+lag)%p]
        y,z=ys[(i+1)%p],ys[(i+1+lag)%p]
        g,rem=divmod(other-old,1<<A)
        require(not rem and g%2 and g,'odd nonzero quotient')
        require(3**L*g==2**v*z-2**u*y,'complete native mismatch-block identity')
        require(gcd(y*z,6)==1,'odd- and ternary-unit endpoints')
        blocks.append((L,A,u,v,y,z,g))
        totals['actual_mismatch_blocks']+=1
    for start in range(s):
        for length in range(1,min(3,s)+1):
            for chooser in (min,max):
                for split in (False,True):
                    rhs=[]
                    pow2=1
                    Ltotal=0
                    for t in range(length):
                        i=(start+t)%s
                        L,_,u,v,y,z,_=blocks[i]
                        Ltotal+=L
                        rho=3**L
                        rhs=[rho*r for r in rhs]
                        w=chooser(y,z)
                        if t+1==length and split:
                            rhs.extend([pow2*(1<<v)*w,-pow2*(1<<u)*w])
                        else:
                            rhs.append(pow2*((1<<v)-(1<<u))*w)
                        next_a=blocks[(i+1)%s][1]
                        pow2 <<= next_a+(v if w==y else u)
                    rhs.append(pow2*blocks[(start+length)%s][-1])
                    require(sum(rhs)==3**Ltotal*blocks[start][-1],'ordered signed expansion')
                    for k in range(1,len(rhs)+1):
                        for sub in combinations(rhs,k):
                            require(sum(sub)!=0,'genuine nonzero Evertse subsum')
                            totals['nonempty_rhs_subsums']+=1
                    true_min=min(v3(abs(n)) for n in rhs)
                    require(true_min==0 if split else 3**true_min<=3*abs(v-u),
                            'ternary absolute value floor at the last cut')
                    totals['matched_chains']+=1
                    totals['split_last_chains']+=split


def main():
    totals=Counter()
    for h in range(4,13):
        for word in necklaces(h):
            result=rational_labels(word)
            if result is None:
                continue
            labels,q,_=result
            odds=[i for i,b in enumerate(word) if b]
            if len(odds)<2:
                continue
            e=[(odds[(j+1)%len(odds)]-i)%h for j,i in enumerate(odds)]
            y=[labels[i] for i in odds]
            for lag in range(1,len(e)):
                controls(e,y,q,lag,totals)
                totals['native_odd_rotation_comparisons']+=1
            totals['primitive_positive_rational_cycles']+=1
    print(json.dumps(dict(totals),indent=2))


if __name__=='__main__':
    main()
