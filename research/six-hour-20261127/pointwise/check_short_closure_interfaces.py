"""Independent finite modular and source controls for the final three interfaces."""
from collections import deque
from fractions import Fraction
from itertools import product
from math import gcd
import json


def group(Q):
    u = pow(2,-1,Q)
    todo=deque([(1,0)])
    seen={(1,0)}
    while todo:
        s,b=todo.popleft()
        for ss,bb in ((u*s,u*b),(3*u*s,(3*b+1)*u)):
            item=ss%Q,bb%Q
            if item not in seen:
                seen.add(item)
                todo.append(item)
    for start in range(Q):
        assert (u,start*u%Q) in seen
        assert (1,start) in seen
    return len(seen)


def ternary(h):
    modulus=3**h
    tests=0
    for r in range(1,modulus):
        if r%3==0:
            continue
        y=r if r%2 else r+modulus
        blocks=[]
        for _ in range(h):
            e=next(e for e in range(1,7) if (y*2**e)%3==1 and (y*2**e)%9!=1)
            y=(y*2**e-1)//3
            assert y%2 and y%3
            blocks.append(e)
        for seed in range(modulus):
            x=seed
            for e in reversed(blocks):
                x=(3*x+1)*pow(2**e,-1,modulus)%modulus
            assert x==r
            tests+=1
    return tests


def chunks():
    total=0
    for n in range(1,11):
        found=set()
        for bits in product((0,1),repeat=n):
            q,A=0,0
            for j,b in enumerate(bits):
                if b:
                    q+=1
                    A=3*A+2**j
            cls=(-A*pow(3**q,-1,2**n))%2**n
            assert cls not in found
            found.add(cls)
            assert 0<=A<=3**n-2**n
            total+=1
    return total


def layer():
    tests=0
    for n in range(2,9):
        for m in range(1,2**(7*n//4+1),2):
            x,A,G=m,0,Fraction(0)
            for j in range(n):
                G+=Fraction(2**A,3**(j+1))
                h=3*x+1
                e=(h&-h).bit_length()-1
                x=h>>e
                A+=e
                if 4*A>7*(j+1):
                    break
            else:
                if m>=2**(A+1):
                    continue
                for t in (0,1,n-1):
                    for z in (0,Fraction(1,n)):
                        v=m+z*G
                        Z=Fraction(2**A,v)
                        assert Z**(n-t)/2**(A*n)==Fraction(1,2**(t*A)*v**(n-t))
                        tests+=1
    return tests


if __name__=="__main__":
    print(json.dumps({"groups":{q:group(q) for q in (5,7,11,25,35,49,65)},
                      "ternary_seed_checks":[ternary(h) for h in range(1,5)],
                      "affine_word_checks":chunks(),"boundary_word_tests":layer()},indent=2,sort_keys=True))
