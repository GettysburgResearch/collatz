"""Exact 19-step merger and a finite countertest against a uniform inverse cover."""
from fractions import Fraction
from functools import lru_cache
import sys


def check(test, message):
    if not test:
        raise ValueError(message)


@lru_cache(None)
def clock(i):
    x = Fraction(3)**i
    k = x.numerator.bit_length()-x.denominator.bit_length()
    return k if Fraction(2)**k <= x else k-1


def wrap(i):
    return clock(i+1)-clock(i)


def ternary_end(gaps, modulus):
    x = 0
    for a in gaps:
        x = (3*x+1)*pow(2,-a,modulus)%modulus
    return x


def merger():
    j = lambda i: int(i not in (-2,-1,0,1))
    past = [wrap(i)+j(i)-j(i+1) for i in range(-19,0)]
    modulus = 3**19
    r = ternary_end(past,modulus)
    check(r == 187605073, "joint family anchored residue")
    route = (3,3,2,1,3,4,1,1,2)+(1,)*10
    C = 0
    for i,a in enumerate(route):
        C = 2**a*C+3**i
    check(sum(route) == 30 and C == 1467890651, "reverse affine word")
    B = (C-2**29)//3
    check(B == 310339913 and r == B*pow(2,-29,modulus)%modulus, "full class")
    check(r%3**17 == 58464910, "distinct from the earlier 16-step progression")
    print(f"Joint family's 19-gap past gives s={r} modulo {modulus}, "
          f"smaller multiple (2^29 s-{B})/3^18.")


def model(depth):
    """Enumerate all inverse words that could qualify, including affine ties."""
    extra_nodes = 0
    for i in range(8):
        # x_i = ax*s + b along the forward mechanical prefix.
        ax,b = Fraction(1),Fraction(0)
        for t in range(i):
            ax,b = 3*ax/2**wrap(t),(3*b+1)/2**wrap(t)
        modulus = 3**(depth+1)
        source = ternary_end([wrap(t) for t in range(i-depth-1,i)],modulus)
        powers = [3**j for j in range(depth+1)]
        # One future cheap endpoint at depth j can spend at most this total.
        # The greatest remaining extra budget occurs at the final depth,
        # since log_2(3)-1>0.
        max_extra = int(2*powers[-1]/ax).bit_length()-1-depth
        tests = {}
        for f,offset in ((Fraction(2),1),(Fraction(3,4),Fraction(1,4))):
            ls = []
            for pj in powers:
                q = f*pj/ax
                top = int(q).bit_length()-1
                exact = q == Fraction(2)**top
                ls.append((top,exact,offset))
            tests[f] = ls
        n = [0]
        def search(y,j,A):
            n[0] += 1
            residue = y%3
            if j:
                top, exact, offset = (multiple if residue == 0 else ordinary)[j]
                if A <= top:
                    # The 3-divisible threshold dominates the ordinary one.
                    check(A == top and exact, "strictly cheaper mechanical rival")
                    carry = (source<<A)-powers[j]*y
                    check(((1<<A)*b-carry)/powers[j] >= offset,
                          "mechanical boundary intercept")
            if j == depth or residue == 0:
                return
            for a in range(2 if residue==1 else 1,max_extra-(A-j)+2,2):
                search(((y<<a)-1)//3,j+1,A+a)
        multiple = tests[Fraction(2)]
        ordinary = tests[Fraction(3,4)]
        search(source,0,0)
        extra_nodes += n[0]
    print(f"Mechanical minimum and its next seven odd sites: "
          f"all candidate ancestor depths 1 through {depth}, {extra_nodes} nodes, no cheaper rival.")


if __name__ == '__main__':
    merger()
    model(int(sys.argv[1]) if len(sys.argv)>1 else 40)
