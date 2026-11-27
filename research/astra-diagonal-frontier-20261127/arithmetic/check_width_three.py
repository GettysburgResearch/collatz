"""Exact convolution, residue, calendar, and finite native stress controls."""

from fractions import Fraction
from itertools import product
from math import comb
import json


def require(ok, detail):
    if not ok:
        raise ArithmeticError(detail)


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def conv(seq,poly,r):
    return sum(c*seq[r+i] for i,c in enumerate(poly))


def polynomial_controls():
    factors=(1,1,2,3,4,5)
    p=[1];q=[1];r=[1]
    for d in factors:
        p=mul(p,[-1]+[0]*(d-1)+[1])
        q=mul(q,[1]*d)
        r=mul(r,[int(i%d==0) for i in range(61-d)])
    require([c for c in p if c]==[1,-2,1,1,-2,1,1,-2,1],"stencil coefficients")
    require([i for i,c in enumerate(p) if c]==[0,1,3,5,8,11,13,15,16],"stencil locations")
    require(mul(q,[(-1)**i*comb(6,i) for i in range(7)])==p,"order six")
    z=mul(p,r)
    require(all(c==((-1)**(i//60)*comb(6,i//60) if i%60==0 else 0)
                for i,c in enumerate(z)) and len(z)==361,"stride-sixty divisibility")
    labels=[((i*i*881+17*i+3)%113)-56 for i in range(150)]
    for t in range(1,19):
        sums=[1]
        for _ in range(6):sums=mul(sums,[1]*t)
        for k in range(3):
            left=sum((-1)**i*comb(6,i)*conv(labels,q,k+i*t) for i in range(7))
            require(left==sum(v*conv(labels,p,k+j) for j,v in enumerate(sums)),"literal stride convolution")
    coefs=[c for c in p if c]
    ds={sum(a*b for a,b in zip(coefs,row)) for row in product((1,2),repeat=len(coefs))}
    require(min(ds)==-6 and max(ds)==6,"all two-grade tags")
    return p,{"stencil":p,"positive_mass":6,"quotient_coefficient_norm":sum(abs(c) for c in q),
              "stride_sixty_quotient_degree":len(r)-1,"binary_masks":2**len(coefs)}


def calendar_controls():
    words=set();births=short=long=0
    for n in range(7,75):
        for h in range(n//2+1,(2*n-1)//3+1):
            for r in range(n):
                b=tuple(1+(r+(j+1)*h)//n-(r+j*h)//n for j in range(7))
                words.add(b)
                require(all(x!=(1,1) for x in zip(b,b[1:])),"isolated ones")
                require(all(x!=(2,2,2) for x in zip(b,b[1:],b[2:])),"at most two twos")
                require((r<h)==(r//n-(r-h)//n==1),"previous-two strip")
                if b[0]==1:require((r+h)%n>=h,"date after one is forced below critical width")
    for h in range(-6,1):
        for d in range(-6,7):
            if (3*h+d)%2==0:
                v=(3*h+d)//2
                require(v<=0 or v%4!=0,"no birth at a one")
            if (3*h+d)%4==0 and (v:=(3*h+d)//4)>0:
                require(h==0 and v==1,"second two birth")
                births+=1
    for h in range(1,4):
        for d in range(-6,7):
            if (3*h+d)%8:continue
            v=(3*h+d)//2
            if v<=0:continue
            require(v==4 and 3*v//4==3,"positive short return")
            short+=1
            for e in range(-6,7):
                if (9+e)%4==0 and (9+e)//4>0:
                    require((9+e)//4 in (1,2,3),"long return state")
                    long+=1
    return {"distinct_seven_letter_calendars":len(words),"positive_birth_scalar_pairs":births,
            "positive_short_return_choices":short,"positive_long_return_choices":long}


def stress():
    # This ordinary finite fragment shows why a pure fourth-difference
    # two-step sign argument would be insufficient.
    K=96*100
    row=[K+x for x in (1,46,97,238,553)]
    cur=[row]
    for b in (1,2):
        vec=cur[-1];c=[x&-x for x in vec]
        require(all(v in (1,2) for v in c),"two-grade finite stress input")
        for x,fac in zip(vec,c):
            require((x//fac)%6 in (1,5),"ordinary unit")
        moved=[(3*x+fac)//2**b for x,fac in zip(vec,c)]
        require(all(2**b*y==3*x+fac for x,y,fac in zip(vec,moved,c)),"literal raw relation")
        cur.append(moved)
    for before,after in zip(cur,cur[1:]):
        for x,y in zip(before,after):
            x//=x&-x;y//=y&-y
            raw=3*x+1
            require(y==raw//(raw&-raw),"actual ordinary transition")
    polys=[1,-4,6,-4,1]
    vals=[conv(z,polys,0) for z in cur]
    require(vals==[0,-4,-3],"local pure fourth stress")
    return {"finite_ordinary_edges":10,"pure_fourth_heights":vals}


if __name__=="__main__":
    _,p=polynomial_controls()
    print(json.dumps({"polynomial":p,"scalar":calendar_controls(),"finite_stress":stress()},indent=2,sort_keys=True))
