"""Independently exercise the finite lifted-tree transplantation used in O1."""
from collections import deque
from fractions import Fraction
from hashlib import sha256
import json


def neighbors(x):
    if x % 2:
        yield "O", (3*x+1)//2, 1, (Fraction(3,2), Fraction(1,2))
    else:
        yield "E", x//2, 1, (Fraction(1,2), 0)
    yield "e", 2*x, -1, (2, 0)
    if x % 3 == 2:
        yield "o", (2*x-1)//3, -1, (Fraction(2,3), Fraction(-1,3))


def lifted_ball(source, radius):
    seen = {(source,0): (Fraction(1), Fraction(0), 0)}
    queue = deque(seen)
    while queue:
        node=queue.popleft()
        x,j=node
        alpha,beta,dist=seen[node]
        if dist == radius:
            continue
        for _,y,d,(s,t) in neighbors(x):
            new=(y,j+d)
            form=(s*alpha,s*beta+t)
            if new not in seen:
                seen[new]=(*form,dist+1)
                queue.append(new)
            elif seen[new][:2] != form:
                raise RuntimeError("incompatible affine forms at a lifted vertex")
    return seen


def certify_patch(a, r, period, multiple):
    nodes=lifted_ball(a,r)
    forms={v[:2] for v in nodes.values()}
    if len(forms)!=len(nodes):
        raise RuntimeError("distinct vertices have the same affine law")
    roots=[(s2-s1)/(r1-r2) for r1,s1 in forms for r2,s2 in forms if r1!=r2]
    h=max(roots+[0,a])
    modulus=period*6**(r+1)
    b=a+modulus*(int(h//modulus)+multiple)
    if b <= h:
        raise RuntimeError("collision threshold was not cleared")
    copied={}
    for node,(alpha,beta,_) in nodes.items():
        y=alpha*b+beta
        if y.denominator!=1 or y<=0 or (int(y)-node[0])%(6*period):
            raise RuntimeError("coordinate or label mismatch")
        copied[node]=int(y)
    if len(set(copied.values()))!=len(nodes):
        raise RuntimeError("copied coordinates collide")
    count=0
    for (x,j),(_,_,d) in nodes.items():
        if d==r:
            continue
        expected={l:copied[z,j+dt] for l,z,dt,_ in neighbors(x)}
        actual={l:z for l,z,_,_ in neighbors(copied[x,j])}
        if expected!=actual:
            raise RuntimeError("branch or inverse-domain discrepancy")
        count+=len(expected)
    return len(nodes),count


totals=dict(patches=0,vertices=0,oriented_edges_from_interiors=0)
for a in (1,2,3,5,7,17,27,121):
    for r in range(1,7):
        for p in (1,5,6):
            for m in (1,3):
                n,e=certify_patch(a,r,p,m)
                totals["patches"]+=1
                totals["vertices"]+=n
                totals["oriented_edges_from_interiors"]+=e
print(json.dumps(totals,sort_keys=True))
