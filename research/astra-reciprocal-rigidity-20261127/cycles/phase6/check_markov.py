"""Exact rational certificates for the signed-word transfers and dimension margins."""

from fractions import Fraction as F
from itertools import product
from math import comb


def check(ok, msg):
    if not ok:
        raise AssertionError(msg)


DIMER = {
    (0,0):1000, (0,1):300, (0,2):396, (0,3):303, (0,4):539,
    (1,0):404, (1,1):128, (1,2):126, (1,3):187,
    (2,0):434, (2,1):130, (2,2):319, (3,0):255, (3,1):297, (4,0):734
}
TWO_GAP = (1000,468,469,443,558)


def row(b, parity, yes, no, next_weight):
    return sum(comb(b,j)*yes**j*no**(b-j)*next_weight(j) for j in range(parity,b+1,2))


def certificates():
    worst = F()
    for (a,b), v in DIMER.items():
        for e in (0,1):
            ratio = F(row(b,e,72,30,lambda j:DIMER[4-a-j,a]), 100**b * v)
            worst = max(worst, ratio)
            check(ratio <= F(37,50), "dimer transfer inequality")
    print("30 dimer parity rows, largest weighted ratio", worst)
    worst = F()
    for b, v in enumerate(TWO_GAP):
        for e in (0,1):
            ratio = F(row(b,e,59,42,lambda j:TWO_GAP[4-j]), 100**b * v)
            worst = max(worst, ratio)
            check(ratio <= F(14,25), "two-gap transfer inequality")
    print("10 two-gap parity rows, largest weighted ratio", worst)
    check(2**21 * 37**50 < 50**50, "dimer signed rate >.42")
    check(2**4 * 14**5 < 25**5, "two-gap signed rate >.80")


def cross_entropy_checks():
    check(2**158496 < 3**100000 < 2**158497, "alpha enclosure")
    al, ah = F(158496,100000), F(158497,100000)
    bdlo, bdhi = (2-ah)/(ah-1), (2-al)/(al-1)
    check(F(709,1000)<bdlo<bdhi<F(710,1000), "dimer critical bias")
    check(F(584,1000)<al-1<ah-1<F(586,1000), "two-gap critical bias")

    def log_bound(num, den, bound):
        check(den**bound.denominator < 2**bound.numerator * num**bound.denominator,
              "rational log upper bound")
    log_bound(71,100,F(495,1000))
    log_bound(29,100,F(1787,1000))
    log_bound(585,1000,F(775,1000))
    log_bound(415,1000,F(1270,1000))
    hd = (F(709,1000)*F(495,1000)+F(291,1000)*F(1787,1000))/(2+F(709,1000))
    h5 = (F(584,1000)*F(775,1000)+F(416,1000)*F(1270,1000))/al
    check(hd < F(322,1000) and h5 < F(619,1000), "cross-entropy ceilings")
    e, eta, gamma = F(1,10**9),F(1,10**13),F(1,10**12)
    check((F(35,100)-hd)*e-100*eta*(1+e) > 5*gamma, "forward high margin")
    check(al*(F(67,100)-h5)*e-100*eta*(1+e) > 5*ah*gamma, "reverse high margin")
    check(8000010*F(1,20000100) < F(1,2), "central chunk capacity")
    print("entropy ceilings", hd, h5, "common declared saving", gamma)


def affine(w):
    c = 0
    for i,ch in enumerate(w):
        if ch=="1":
            c=3*c+2**i
    return c


def canonical_chunks():
    tests = 0
    for blocks in (("10","110"),("1","10")):
        for inds in product(range(2),repeat=8):
            aa = [blocks[i] for i in inds]
            full = "".join(aa)
            t, u = len(full), full.count("1")
            source = (-pow(3,-u,2**t)*affine(full))%(2**t)
            end = (pow(2,-t,3**u)*affine(full))%(3**u)
            for cuts in ((0,2,6,8),(0,1,3,7,8)):
                x = y = F()
                for left,right in zip(cuts,cuts[1:]):
                    before,local = "".join(aa[:left]),"".join(aa[left:right])
                    m,a = t-len(before), before.count("1")+local.count("1")
                    b=affine(local)
                    z=(-pow(3,-a,2**m)*b)%(2**m)
                    v=(pow(2,-m,3**a)*b)%(3**a)
                    x+=F(z,2**m)
                    y+=F(v,3**a)
                check(x%1==F(source,2**t) and y%1==F(end,3**u),
                      "canonical source/end circle with actual factors")
                tests+=1
    print("independent exact canonical-chunk reconstructions",tests)


if __name__ == "__main__":
    certificates()
    cross_entropy_checks()
    canonical_chunks()
