"""Exact odd-grid rounding, one-node surgeries and the winding comparison."""
from bisect import bisect_left
from collections import Counter
from fractions import Fraction
from math import gcd
import json


def require(ok,reason):
    if not ok:
        raise ArithmeticError(reason)


def oddpart(x):
    return x//(x&-x)


def raw(n,N):
    if 3*n<=N:
        return 3*n
    y=3*n+1
    return y if oddpart(y)<=N else y+2


def graph(N):
    successor={x:oddpart(raw(x,N)) for x in range(1,N+1,2)}
    visited=set(); cycles=[]
    for start in successor:
        if start in visited:
            continue
        trail=[];marks={}
        x=start
        while x not in visited and x not in marks:
            marks[x]=len(trail);trail.append(x);x=successor[x]
        if x in marks:
            cyc=trail[marks[x]:]
            A=sum((raw(u,N)&-raw(u,N)).bit_length()-1 for u in cyc)
            require(gcd(A,len(cyc))==1,"monotone orbit primitive clock")
            cycles.append((cyc,A))
        visited.update(trail)
    rotations={Fraction(A,len(c)) for c,A in cycles}
    require(len(rotations)==1,"all components carry one clock")
    return cycles,rotations.pop()


def ceil_log_ratio(x,y):
    k=x.bit_length()-y.bit_length()
    if k>=0:
        return k+int(x>(y<<k))
    return k+int((x<<(-k))>y)


def winding(c,a,fn,d,b,gn):
    total=positive=negative=0
    for x in c:
        for y in d:
            step=ceil_log_ratio(fn(x),gn(y))-ceil_log_ratio(x,y)
            total+=step;positive+=max(0,step);negative+=max(0,-step)
    require(total==len(d)*a-len(c)*b,"exact signed winding")
    return positive,negative


def ceil_reference_grid(n,N):
    grid=sorted(x*(1<<k) for x in range(1,N+1,2) for k in range((4*N).bit_length()+1))
    z=3*n
    # z<=N is a grid point. If z>N, no noninteger dyadic lift can enter
    # at this magnitude. Hence this independent positive-power list suffices.
    return grid[bisect_left(grid,z)]


def main():
    merges=Counter(); changes=Counter(); finite_upper=[]
    base,old=graph(1); drops=[]; count=0; largest=3001
    for n in range(3,largest+1,2):
        components,new=graph(n)
        require(new<=old,"nested homogeneous upper rotations decrease")
        for x in range(1,n,2):
            before=raw(x,n-2);after=raw(x,n)
            if before!=after:
                zeros=n//3 if n%3==0 else (2*n-1)//3
                require(n%3 in (0,2) and zeros==x and oddpart(after)==n,"one changed source")
                merges[n%12]+=1
        if n>=17:
            required=int(n%3!=1)
            changed=sum(raw(x,n-2)!=raw(x,n) for x in range(1,n,2))
            require(changed==required,"source exists in precisely the two residue classes")
            if n%4==3:
                require(raw(n,n)==3*(n+1) and raw(oddpart(n+1),n-2)==3*oddpart(n+1),"two-step coalescence")
            else:
                require(raw(n,n)==3*n+1 and 2*raw((n+1)//2,n-2)==3*n+5,"adjacent two-step images")
        if new<old:
            require(old.numerator*new.denominator-new.numerator*old.denominator==1,"Farey-neighbor switch")
            require(len(base)==len(components)==1 and n in components[0][0],"unique switching components")
            if n>=17:require(n%12 in (5,9),"eligible switch residue")
            drops.append([n,str(old),str(new)])
            changes[n%12]+=1
        if n<=101:
            for x in range(1,n+1,2):
                require(raw(x,n)==ceil_reference_grid(x,n),"literal homogeneous ceiling")
            for c,a in base:
                for d,b in components:
                    q,r=winding(c,a,lambda x:raw(x,n-2),d,b,lambda x:raw(x,n))
                    require(0<=q-r and q<=int(n in d),"one-deletion winding signed control")
                    count+=1
        base,old=components,new
    # Test the exact ordinary winding formula on the genuine positive cycle 1
    # at every grid cutoff compatible with the factor-eight geometry.
    actual_cases=0
    for n in (1,3,5,7):
        cs,_=graph(n)
        for cyc,A in cs:
            q,r=winding([1],2,lambda x:3*x+1,cyc,A,lambda x:raw(x,n))
            require(q==int(1 in cyc and 3<=n) and r==0,"physical exact coincidence identity")
            actual_cases+=1
    # Local affine controls use literal dyadic grids, all crossings of a
    # complete reference component, and arbitrary actual ordinary odd steps.
    # This exercises exceptional valuations and both negative-tail charges
    # without assuming the existence of a nontrivial positive closed cycle.
    local_steps=eligible_cases=negative_child=negative_parent=wide_positive=0
    unit_cycle=0
    for N in range(1,128,2):
        cs,rho=graph(N)
        base=Fraction(1,256)
        grid=sorted(n*base*(1<<j) for n in range(1,N+1,2) for j in range(21))
        gridset=set(grid)
        lifts=[(V,n,raw(n,N)*V/n) for c,A in cs for n in c
               for j in range(18) for V in (n*base*(1<<j),)]
        common={n for c,A in cs for n in c}
        for x in range(1,2*N+1,2):
            Y=3*x+1;child=oddpart(Y)
            pos=[V for V,n,Z in lifts if x<=V and Z<Y]
            neg=[V for V,n,Z in lifts if V<x and Y<=Z]
            require(len(neg)<=1,"all components have one incoming target lift")
            local_steps+=1
            if child<=N:
                h=ceil_log_ratio(Y,N+1)
                delta=Fraction(2)**h
                predecessor=grid[bisect_left(grid,Y)-1]
                require(Y in gridset and Y-predecessor==delta,"literal strict predecessor at seams")
                require(pos==[V for V,n,Z in lifts if x<=V and 3*V<=predecessor],"universal crossing interval")
                eligible_cases+=1
            if neg:
                if child>N:
                    negative_child+=1
                else:
                    require(3*x>4*N and (Y&-Y)>=8,"negative charge is a high-valuation high parent")
                    negative_parent+=1
            if N<8*x:
                require(len(pos)==int(x in common and 3*x<=N),"factor-eight positive simplification")
            wide_positive+=sum(V>x for V in pos)
        for c,A in cs:
            q,r=winding([1],2,lambda x:4,c,A,lambda n:raw(n,N))
            require(r==0 and q==2*len(c)-A,"all-cut positive genuine cycle")
            unit_cycle+=1
    require(min(negative_child,negative_parent,wide_positive)>0,"all crossing mechanisms exercised")
    slopes={row[1] for row in drops}|{str(old)}
    for c in ('2','8/5','65/41'):
        require(c in slopes,"upper convergent attained")
        finite_upper.append(c)
    return {"odd_grid_maximum":largest,"cutoff_insertions":(largest-1)//2,
            "rotation_drops":len(drops),"drop_residues":dict(sorted(changes.items())),
            "changed_edge_residues":dict(sorted(merges.items())),"paired_winding_controls":count,
            "genuine_native_winding_controls":actual_cases,"upper_convergents_seen":finite_upper,
            "all_cut_unit_cycle_controls":unit_cycle,"ordinary_local_step_controls":local_steps,
            "eligible_output_controls":eligible_cases,"negative_high_child_controls":negative_child,
            "negative_high_parent_controls":negative_parent,"strict_input_positive_controls":wide_positive,
            "first_drops":drops[:8],"last_drops":drops[-3:]}


if __name__=="__main__":
    print(json.dumps(main(),indent=2,sort_keys=True))
