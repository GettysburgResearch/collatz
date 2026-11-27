"""Exact examples for O1's clock lift and O5/O7's ordinary path arithmetic."""
from collections import deque
from fractions import Fraction
from math import prod
import json


def require(test, message):
    if not test:
        raise ValueError(message)


def shortcut(n):
    return (3*n+1)//2 if n%2 else n//2


def moves(n):
    if n%2:
        yield "O", (3*n+1)//2, 1, Fraction(3,2), Fraction(1,2)
    else:
        yield "E", n//2, 1, Fraction(1,2), 0
    yield "e", 2*n, -1, 2, 0
    if n%3==2:
        yield "o", (2*n-1)//3, -1, Fraction(2,3), Fraction(-1,3)


def copied_patch(root,radius,period):
    centers={(root,0):(Fraction(1),Fraction(0),0)}
    queue=deque([(root,0)])
    while queue:
        n,clock=queue.popleft()
        slope,offset,depth=centers[n,clock]
        if depth==radius:
            continue
        for label,nxt,step,scale,shift in moves(n):
            key=nxt,clock+step
            germ=(scale*slope, scale*offset+shift)
            if key in centers:
                require(centers[key][:2] == germ, "inconsistent germ")
            else:
                centers[key]=(*germ,depth+1)
                queue.append(key)
    require(len({v[:2] for v in centers.values()})==len(centers),"distinct germs")
    b=root+period*6**(radius+1)
    while True:
        points={node:s*b+t for node,(s,t,_) in centers.items()}
        if len(set(points.values()))==len(points):
            break
        b+=period*6**(radius+1)
    for (n,j),w in points.items():
        require(w.denominator==1 and w>0 and (int(w)-n)%(period*6)==0,"integral copy")
        if centers[n,j][2]==radius:
            continue
        first={label:(nxt,j+step) for label,nxt,step,*_ in moves(n)}
        second={label:nxt for label,nxt,*_ in moves(int(w))}
        require(first.keys()==second.keys(),"extra or missing edge")
        require(all(second[label]==points[vertex] for label,vertex in first.items()),"endpoint")
    return len(points)


def ternary_log(unit,depth):
    exponent=0 if unit%3==1 else 1
    period=2
    modulus=3
    for _ in range(1,depth):
        modulus*=3
        exponent=next(exponent+period*j for j in range(3)
                      if pow(2,exponent+period*j,modulus)==unit%modulus)
        period*=3
    return exponent,period


def source_target(residue,k,e,d,r,modulus):
    z=(pow(2,r,modulus)*(residue+1)*pow(3,-r,modulus)-1)%modulus
    y=((pow(2,d,modulus)*z+1)*pow(3,-k,modulus))%modulus
    n=(pow(2,k,modulus)*y-1)%modulus
    x=((pow(2,e,modulus)*n-1)*pow(3,-1,modulus))%modulus
    return x,z


def test_mixed_funnel(k,e,d,r,primes):
    depth=2*k+r
    modulus=3**depth
    desired=(-1+(2**d-1)*3**r*pow(2,-(d+r),modulus))%modulus
    L0,period=ternary_log(desired,depth)
    stride=period*prod(q-1 for q in primes)
    bad=(0,-1,-2)
    # For each prime test two high-precision residues against its exceptional balls.
    def allowed(L):
        for prime in primes:
            local=prime**3
            values=source_target(pow(2,L,local),k,e,d,r,local)
            if any((value-root)%local==0 for value in values for root in bad):
                return False
        return True

    for t in range(50):
        L=L0+t*stride
        if L>r+2 and allowed(L):
            break
    else:
        raise ValueError("no test exponent found")
    z,rem=divmod(2**r*(2**L+1),3**r)
    require(rem==0,"terminal integer")
    z-=1
    y,rem=divmod(2**d*z+1,3**k)
    require(rem==0 and y%3**k==0,"source ternary precision")
    n=2**k*y-1
    x,rem=divmod(2**e*n-1,3)
    require(rem==0 and x>0 and x%2==1 and z%2==1,"source integer")
    state=x
    for _ in range(e):
        state=shortcut(state)
    require(state==n,"setup shortcut path")
    for _ in range(k):
        require(state%2==1,"initial odd run")
        state=shortcut(state)
    require(state==2**d*z,"first peak")
    for _ in range(d):
        require(state%2==0,"prescribed even segment")
        state=shortcut(state)
    require(state==z,"isolated ordinary target")
    for _ in range(r):
        require(state%2==1,"terminal odd run")
        state=shortcut(state)
    require(state==(1<<L),"certified power of two")
    for prime in primes:
        local=prime**3
        require((x%local,z%local)==source_target(pow(2,L,local),k,e,d,r,local),"residue formula")
    return {"k":k,"e":e,"d":d,"r":r,"L":L,"height_bits":z.bit_length(),
            "exact_shortcut_edges":e+k+d+r}


if __name__=="__main__":
    charts=[copied_patch(a,r,7) for a in (1,2,3,5,27,121) for r in (2,4,7)]
    rows=[test_mixed_funnel(k,3,2,2,(5,7)) for k in range(1,7)]
    print(json.dumps({"lifted_charts":len(charts),"lifted_vertices":sum(charts),
          "ordinary_funnels":rows},indent=2))
