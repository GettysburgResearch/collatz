"""Exact native height envelopes and finite vector-space identities for the two-basis proof."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod
from random import Random
import json

from check_rotation_occupation import lifted, primitive_necklace, require
from check_separated_rotations import order


def native_case(w, stats):
    realizer=lifted(w)
    if realizer is None:
        return
    q,y=realizer
    p=len(w)
    stats["primitive_rational_cycles"] += 1
    stats["proper_denominator_cancellations"] += 1<q<2**sum(w)-3**p
    for lag in range(1,p):
        for root in sorted({y.index(min(y)),y.index(max(y))}):
            first=[y[(root+t)%p] for t in range(p+1)]
            second=[y[(root+lag+t)%p] for t in range(p+1)]
            exp=[[w[(root+a+t)%p] for t in range(p)] for a in (0,lag)]
            envelope=[max(a,b)+q for a,b in zip(first,second)]
            down=[max(Fraction(1),Fraction(a,b)) for a,b in zip(envelope,envelope[1:])]
            require(prod(down)<=Fraction(3,2)**p, "single synced envelope downward variation")
            marks={t+1 for t in range(p) if exp[0][t]!=exp[1][t]}
            for extra in (set(),set(range(1,p,2)),{p//2}):
                cuts=sorted({0,p}|marks|extra)
                product_of_carries=1
                costs=Fraction(1)
                for a,b in zip(cuts,cuts[1:]):
                    high=int(second[a]>first[a])
                    track=(first,second)[high]
                    qh=track[a]
                    B=sum(exp[0][a:b-1])+min(exp[0][b-1],exp[1][b-1])
                    require(qh>=2**B, "true high mixed-divisor scale")
                    prefix=0
                    carry0=0
                    raw=Fraction(0)
                    for h in range(b-a):
                        t=a+h
                        require(envelope[t]==track[t]+q, "same high direction before final mismatch")
                        lhs=Fraction(2**prefix*(track[t]+q),3**h)
                        rhs=qh+q*(raw+Fraction(2**prefix,3**h))
                        require(lhs==rhs and lhs<=qh*(1+q), "sharpened shifted height identity")
                        require(Fraction(2**prefix,3**h)<=Fraction(envelope[a],envelope[t])*(1+q),
                                "shifted drawdown control")
                        carry0=3*carry0+2**prefix
                        raw+=Fraction(2**prefix,3**(h+1))
                        prefix+=exp[high][t]
                        stats["physical_prefixes"] += 1
                    # Charge one actual drawdown in the block, even when the high track changes at b.
                    block_drop=prod(down[a:b])
                    bound=(b-a)*3**(b-a)*block_drop*(1+q)
                    require(carry0<=bound, "complete actual carry envelope")
                    product_of_carries *= q*carry0
                    costs *= q*(b-a)*(1+q)*3**(b-a)
                    stats["block_carries"] += 1
                    stats["blocks_ending_in_a_high_switch"] += (first[a]>second[a])!=(first[b]>second[b])
                require(product_of_carries<=costs*Fraction(3,2)**p,
                        "whole-lap one-envelope carry-height bound")
                stats["physical_mesh_partitions"] += 1


def rank(rows):
    basis={}
    for row in rows:
        v=list(map(Fraction,row))
        for j,b in sorted(basis.items()):
            c=v[j]
            if c:
                v=[x-c*y for x,y in zip(v,b)]
        pivot=next((j for j,x in enumerate(v) if x),None)
        if pivot is not None:
            scale=v[pivot]
            basis[pivot]=[x/scale for x in v]
    return len(basis)


def add(x,y,scale=1):
    return tuple(a+scale*b for a,b in zip(x,y))


def selected(roots,carries,order):
    basis=list(roots)
    indices=set()
    for i in order:
        if rank(basis+[carries[i]])>len(basis):
            basis.append(carries[i])
            indices.add(i)
    return indices


def vector_case(roots,carries,weights,cuts,stats):
    """Formal physical interface; ranks here are exact finite rational ranks."""
    k=len(carries)
    states=[roots]
    for i,z in enumerate(carries):
        states.append((add(states[-1][0],z),add(states[-1][1],z,weights[i])))
    terminal=states[-1]
    if min(rank(roots),rank(terminal))<2:
        return
    dim=rank(list(roots)+carries)
    early=selected(roots,carries,range(k))
    late=selected(terminal,carries,reversed(range(k)))
    require(len(early)==len(late)==dim-2, "two bases attain global rank")
    loss=0
    for j in range(k):
        pre=list(roots)+carries[:j]
        post=list(terminal)+carries[j:]
        l,r=rank(pre),rank(post)
        meet=l+r-dim
        require(rank(pre+list(states[j]))==l and rank(post+list(states[j]))==r,
                "both actual partial directions belong to both spans")
        require(meet>=rank(states[j]), "intersection lower rank")
        require(sum(i<j for i in early)-sum(i<j for i in late)==meet-2,
                "greedy multiplicity difference")
        loss+=(cuts[j+1]-cuts[j])*(2-meet)
        stats["finite_rank_cuts"] += 1
        stats["positive_loss_cuts"] += meet<2
        stats["negative_loss_cuts"] += meet>2
    require(loss==sum(cuts[i+1] for i in early)-sum(cuts[i+1] for i in late),
            "signed summation-by-parts identity")
    stats["finite_vector_systems"] += 1
    stats["different_selected_bases"] += early!=late


def mixed_basis_products(stats):
    # Prefix vectors (B0+T B1)/(1+T), (T B0+B1)/(1+T) over Q(T).
    # The denominator is assessed only at three. The tail forms are completed from coordinates.
    for D in (1,2,4):
        side=D+1
        size=2*side
        units=[[int(i==j) for j in range(size)] for i in range(size)]
        core=[]
        for u in range(D):
            core.append(add(units[u],units[side+u+1]))
            core.append(add(units[u+1],units[side+u]))
        require(rank(core)==2*D,"independent three-adic interior forms")
        rows=core.copy()
        tail=[]
        for i,vec in enumerate(units):
            if rank(rows+[vec])>len(rows):
                rows.append(vec)
                tail.append(i)
        require(len(rows)==size and len(tail)==2,"exact boundary completion rank")
        for j in (1,3,5,8):
            T=2**j
            Q=1+T
            for p in (2,7):
                basis=(Fraction(5*2**(p+1),3**p),Fraction(7,3**(p//2)))
                coords=[b*T**u for b in basis for u in range(side)]
                vals=[sum(a*x for a,x in zip(row,coords)) for row in rows]
                prefix=((basis[0]+T*basis[1])/Q,(T*basis[0]+basis[1])/Q)
                arch2=prod(abs(x)*Fraction(2)**-order(x,2) for x in coords)
                at3=prod(Fraction(3)**-order(x,3) for x in vals)
                joint=prod(abs(b)*Fraction(2)**-order(b,2) for b in basis)**side
                inner=(Fraction(3)**(-2*order(Q,3)-sum(order(b,3) for b in prefix)))**D
                outer=prod(Fraction(3)**-order(coords[i],3) for i in tail)
                require(arch2*at3==joint*inner*outer,
                        "unequal bases, full exponent-box product with boundary")
                stats["mixed_basis_products"]+=1
                stats["nonunit_clearing_polynomial_at_three"]+=order(Q,3)>0


def main():
    out=Counter()
    for p in range(2,7):
        for w in product((1,2,3),repeat=p):
            if primitive_necklace(w):
                native_case(w,out)
    for w in ((1,2,1,3,1,2,1,12),(2,1,3,2,1,3,2,1,29),
              (1,1,2,2,1,2,1,1,2,2,1,51),(1,2,1,3,2,61,1,3,1,2)):
        native_case(w,out)
    rng=Random(19097)
    for _ in range(180):
        n=rng.randint(2,5)
        k=rng.randint(2,8)
        roots=tuple(tuple(int(i==j) for i in range(n)) for j in range(2))
        carries=[tuple(rng.randrange(-2,3) for _ in range(n)) for _ in range(k)]
        weights=[2**rng.randrange(4) for _ in range(k)]
        dates=[0]
        for _ in carries:
            dates.append(dates[-1]+rng.randint(1,15))
        vector_case(roots,carries,weights,dates,out)
    # Both middle states are e1, with different incoming and outgoing two-planes.
    vector_case(((1,1,0),(1,2,0)),[(0,-1,0),(0,0,1)],[2,2],[0,7,20],out)
    require(3**5<2**8 and Fraction(8,5)<Fraction(69,43), "exact >1/43 at six")
    mixed_basis_products(out)
    require(all(out.values()) and len(out)==13, "all native and rank regimes covered")
    return dict(out)


if __name__=="__main__":
    print(json.dumps(main(),indent=2,sort_keys=True))
