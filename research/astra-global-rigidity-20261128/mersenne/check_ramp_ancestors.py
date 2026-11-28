"""Check the short ordinary-source obstruction at ALL sites of an unbounded ramp."""
import json


def next_step(x):
    return (3*x+1)//2 if x%2 else x//2


def slow_odd(x,K):
    for _ in range(K):
        if x==1:
            return False
        y=3*x+1
        x=y//(y & -y)
    return x!=1


def ordinary_obstructions(K,m):
    s=K+m
    # A full inverse visiting from below has 2**e < (3/2)**s.
    even_max=((3**s-1)//2**s).bit_length()-1
    # Referring along i+K odds ends at positive odd w; w+1 < 2*(3/2)**m.
    w_max=(2*3**m-1)//2**m-1
    active=[]
    checked_slows=0
    for w in range(1,w_max+1,2):
        if not slow_odd(w,K):
            continue
        checked_slows+=1
        z=w
        odds=0
        prior=None
        for t in range(K+even_max+2):
            e=t-K-1
            d=odds-K-1
            if z==1:
                break
            if e>=0 and d>=0 and (w+1)*3**K <= 2**(e+K+1):
                if 3**(d+1)-2**d<=z<=3**(d+1)-1:
                    # d=0,z=2,prior=1 forces original backtracking.
                    if d or z!=2 or prior!=1:
                        active.append([w,t,d,z])
            odds+=z%2
            prior,z=z,next_step(z)
    return dict(K=K,extra_budget=m,small_odd_upper=w_max,
                maximum_inverse_evens=even_max,slow_supplied_odds=checked_slows,
                virtual_boundary_candidates=active)


if __name__=='__main__':
    print(json.dumps([ordinary_obstructions(K,m) for K,m in [(41,8),(41,9),(141,29),(141,30)]],indent=2))
