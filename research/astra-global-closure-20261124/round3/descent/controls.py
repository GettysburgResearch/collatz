"""Independent finite ordinary tests of the new reset, cone and non-reset proofs."""
from fractions import Fraction as Q
from itertools import product


def check(condition, label):
    if not condition:
        raise ArithmeticError(label)


def t(x):
    return (3*x+1)//2 if x%2 else x//2


def trace(x, length):
    bits = []
    for _ in range(length):
        bits.append(x%2)
        x = t(x)
    return x, bits


def data(word):
    A = C = 0
    for l in word:
        a, c = (3, 7) if l == "L" else (5, 5)
        C = 9*C+(c << A)
        A += a
    return A, 2*len(word), C


def source(word):
    A, p, C = data(word)
    modulus = 2 << A
    q = ((1 << A)-C)*pow(3**p, -1, modulus) % modulus
    return q, modulus


def path(q, word):
    for l in word:
        A, p, C = data(l)
        zz, bits = trace(q, A)
        check(q%2 == zz%2 == 1 and sum(bits) == p and (zz<<A) == 3**p*q+C, "ordinary edge")
        q = zz
    return q


def carry(bits):
    c = p = 0
    for j, b in enumerate(bits):
        if b:
            c = 3*c+(1 << j)
            p += 1
    return p, c


F = lambda q: (183*q+1)//128
CATALOG = ("L","LLP","LLPP","LLPLPP","LLPPPLPLPP","LLPPPPLLLLP")
PORTALS = ("LLPPLLLPLPLLLLLPL","LLPLLPPLPLLLLLPL","LLPLLPLPLLLLLPL",
           "LLPLLPLLLPLPLLLLLPL")


def reset_word(word):
    A, p, C = data(word)
    K, r = divmod(183*C+(1<<A)-3**p, 128)
    if r:
        return None
    b = -K*pow(3**p, -1, 1<<A) % (1<<A)
    _, bits = trace(b, A)
    return bits if carry(bits) == (p,K) else None


def run():
    for w in CATALOG:
        b = reset_word(w)
        check(b is not None, w)
        print("reset",w,"".join(map(str,b)))
    mix = 0
    for tiles in product(CATALOG,repeat=3):
        w = "".join(tiles)
        q, mod = source("L"+w+"LLL")
        for x in (q,q+mod):
            z = path(x,"L")
            y = F(z)
            for tile in tiles:
                z = path(z,tile)
                y, _ = trace(y,data(tile)[0])
                check(128*y==183*z+1,"same ordinary source")
            mix += 1
    print("ordinary three-tile concatenations",mix)
    cones = 0
    for s in (0,1,2,4,8,14,21):
        for r in range(3,9*s+12):
            if 5*9**r*729**s > 13*8**r*2048**s:
                continue
            w = "L"*r+"PLL"*s+"P"
            x,_ = source(w)
            y = path(x,w)
            check(0<y<min(x,(3*x+1)//4),"cone floor")
            cones += 1
    print("ordinary cone sources",cones)
    for w in PORTALS:
        A,p,C = data(w)
        K, rem = divmod(61*C+1195*(1<<A)-3*3**(p-2),384)
        check(not rem,"portal integral carry")
        z = -K*pow(3**(p-2),-1,1<<A) % (1<<A)
        _, bits = trace(z,A)
        check(carry(bits)==(p-2,K),"portal carry")
        x, mod = source(w+"LLL")
        for src in (x,x+mod):
            q = path(src,w)
            dest, bs = trace(F(src),A)
            check(384*dest==61*(q+7)+768 and bs==bits,"ordinary portal")
        print("positive-offset seed",w,A,p,K)
    r = 12*Q(9,8)**37
    for _ in range(3):
        r=(9*r-166)/32
    check(r>12,"surviving normalization")
    print("normalized reserve after worst burst",str(r))
    check(9**8*729<8**8*2048 and 5*9**8<13*8**8,"linear subcone")
    print("all controls passed")


if __name__ == "__main__":
    run()
