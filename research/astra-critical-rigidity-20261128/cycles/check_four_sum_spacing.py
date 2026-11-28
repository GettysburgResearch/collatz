"""Exact backward fourth-sum register and finite cube controls."""

import json
from itertools import combinations_with_replacement, product
from math import comb, factorial, gcd


def require(ok, label):
    if not ok:
        raise ArithmeticError(label)


def cap(r, p, A, u):
    e = p-A
    if r < 2*e-A:
        return 12
    if r < e:
        return 14
    if r <= u:
        return 17
    if r < 2*e:
        return 16
    return 20


def calendar(p, a, u):
    require(gcd(p,a) == 1 and p < 2*a and a < u < 3*p-4*a, "calendar scope")
    rows = [0]*5
    legal = [0]*5
    found = [0]*5
    endpoints = [2*p-3*a,p-a,u+1,2*p-2*a,p]
    for r in range(p):
        g = (r+a) % p
        B = 2 if r+a < p else 4
        m, following = cap(r,p,a,u), cap(g,p,a,u)
        ix = next(i for i,end in enumerate(endpoints) if r < end)
        rows[ix] += 1
        ds = range(-4,5) if r <= u else (0,)
        for z in range(-following,following+1):
            for d in ds:
                x, rem = divmod(B*z-d, 3)
                if rem:
                    continue
                legal[ix] += 1
                require(abs(x) <= m, "backward envelope integer predecessor")
                found[ix] = max(found[ix], abs(x))
    require(all(rows), "covers every endpoint type")
    return dict(moment=4, period=p, one_step_offset=a, high_threshold=u,
                rows_by_region=rows, checked_predecessors=legal,
                largest_attained_predecessor_by_region=found)


def multi_counts(state, k):
    counts = {}
    for ids in combinations_with_replacement(range(len(state)), k):
        mult = factorial(k)
        for i in set(ids):
            mult //= factorial(ids.count(i))
        target = tuple(sum(state[i][j] for i in ids) for j in range(len(state[0])))
        counts[target] = counts.get(target,0)+mult
    return counts


def cube(k):
    points = list(product((0,1),repeat=k))
    count = 0
    for mask in range(1,(1 << len(points))):
        S=[pt for i,pt in enumerate(points) if mask & (1 << i)]
        C=multi_counts(S,4)
        c=sum(v*v for v in C.values())
        require(c*256**k >= len(S)**8*70**k, "eightfold torus bound")
        if len(S) == len(points):
            require(c*256**k == len(S)**8*70**k,"cube equality")
        count+=1
    return dict(length=k, nonempty_uniform_sets=count)


def repeated_edges():
    # A small genuine B3 integer set with nontrivial four-sum collisions,
    # including one using eight distinct entries. Build it with a prescribed
    # four-equals-four identity and exact base separation.
    first=[31**i for i in range(7)]
    last=sum(first[:4])-sum(first[4:])
    off=1-last
    S=[i+off for i in first+[last]]
    require(len(set(sum(S[i] for i in c) for c in
                    combinations_with_replacement(range(8),3))) == comb(10,3),
            "true B3")
    groups={}
    for u in combinations_with_replacement(range(8),4):
        groups.setdefault(sum(S[i] for i in u),[]).append(u)
    disjoint=0
    for group in groups.values():
        require(len(group) <= len(S), "one member fixes other three")
        for i,x in enumerate(group):
            for z in group[i+1:]:
                require(set(x).isdisjoint(z),"no shared member in nondiagonal match")
                disjoint+=int(len(set(x+z))==8)
    require(disjoint>=1, "genuine eight-distinct collision")
    return dict(source_size=8, true_distinct_triples=comb(10,3),
                eight_distinct_unordered_pairs=disjoint)


if __name__=="__main__":
    calendars=[]
    for p,a in [(41,24),(306,179),(665,389),(15601,9126)]:
        for num,den in [(3,5),(13,20)]:
            calendars.append(calendar(p,a,max(a+1,p*num//den)))
    print(json.dumps(dict(calendar=calendars,cube=[cube(i) for i in (1,2,3)],
                          collision_fiber=repeated_edges()),indent=2))
