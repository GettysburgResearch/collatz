"""Verify physical equal-clock affine witnesses and exact dyadic coincidences."""
from fractions import Fraction
from itertools import product


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def data(word):
    coefficient, numerator = 1, 0
    for bit in word:
        numerator = 2*numerator + bit*coefficient
        coefficient *= 3**bit
    return coefficient, numerator


def translation(h):
    if h == 0:
        return (), ()
    if abs(h) == 1:
        return ((0,0,1),(1,0,0)) if h > 0 else ((1,0,0),(0,0,1))
    if h % 2 == 0:
        u, v = translation(h//2)
        return u+(0,), v+(0,)
    delta = 1 if (3*h)%4 == 1 else -1
    u, v = translation((3*h-delta)//4)
    c, d = ((0,1),(1,0)) if delta == 1 else ((1,0),(0,1))
    return u+c, v+d


def affine(m, d):
    if m == 0:
        return translation(d)
    if d == 0:
        u,v = affine(m, (1-3**m)//2)
        return u+(1,), v+(1,)
    if d % 2 == 0:
        u,v = affine(m, d//2)
        return u+(0,), v+(0,)
    u,v = affine(m-1, (d-3**(m-1))//2)
    return u+(0,), v+(1,)


def exact_overlap(r, h, p):
    words = list(product([0,1], repeat=r))
    maps = {data(w):sum(w) for w in words}
    require(len(maps) == len(words), "binary affine collision")
    overlap = sum(p**k*(1-p)**(r-k) for (a,c),k in maps.items() if (a,c+h) in maps)
    return overlap


def main():
    cases = 0
    largest = 0
    for m in range(9):
        for h in [*range(-400,401), -(3**62+7), 2**127-3, 6**49]:
            u,v = affine(m,h)
            a,c = data(u)
            b,d = data(v)
            require(len(u) == len(v), "clock mismatch")
            require(sum(v) == sum(u)+m, "odd count mismatch")
            require(a*3**m == b and a*h+c == d, "literal affine identity")
            require((u == v) == (m == h == 0), "separation")
            if m == 0:
                require(len(u) <= 16*(1+abs(h).bit_length()), "short synchronizer")
            cases += 1
            largest = max(largest, len(u))
    p = Fraction(3,5)
    require(exact_overlap(2,1,p) == p*(1-p), "quarter translate")
    checks = 0
    for r in range(1,8):
        for h in range(-12,13):
            x = exact_overlap(r,h,p)
            require(x == exact_overlap(r+1,2*h,p), "dyadic refinement")
            require((x == 1) == (h == 0), "translated total mass")
            if h and h % (2**r) == 0:
                require(x == 0, "integer overlap")
            checks += 1
    print(f"literal signed-affine witnesses={cases}; maximum tested clock={largest}")
    print(f"dyadic refinement and overlap checks={checks}; O(1/4)=6/25 at theta=3/5")


if __name__ == "__main__":
    main()
