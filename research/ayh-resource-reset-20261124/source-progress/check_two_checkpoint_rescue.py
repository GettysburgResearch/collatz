"""Replay the bounded second-arm mergers on the first-arm obstruction cylinder."""
from fractions import Fraction

PRECISION = 288
# (first clock from 2^r 3^s - 17, exponent offset from s)
ROWS = [(87,-4), (43,3), (43,-2), (285,-15), (75,6), (37,1),
        (33,6), (40,9), (53,14), (77,5), (24,6)]


def require(test, context):
    if not test:
        raise ValueError(context)


def progression(precision):
    m = 0
    for b in range(4, precision):
        modulus = 2**(b+1)
        if pow(3, 67+108*m, modulus) != -53 % modulus:
            m += 2**(b-4)
        require(pow(3, 67+108*m, modulus) == -53 % modulus, ("lift", b, m))
    return m, 2**(precision-4)


def affine_word(a, b, x, length):
    """Propagate the actual word on the given 2-adic cylinder exactly."""
    for _ in range(length):
        y = a*x+b
        require(y.denominator % 2, ("lost binary digit", y.denominator))
        if y.numerator % 2:
            a, b = 3*a/2, (3*b+1)/2
        else:
            a, b = a/2, b/2
    return a, b


def signed_first_phase(c):
    odds = 0
    for i in range(80):
        if c in (-17,-5,-1,0,1):
            return c, i-odds
        odd = c.numerator % 2
        c = ((3*c+1) if odd else c)/2
        odds += odd
    raise ValueError(("unclassified deadline center", c))


if __name__ == "__main__":
    require(signed_first_phase(Fraction(-58)) == (-1,7), "first shadow")
    for d in range(-7,3):
        c, e = signed_first_phase(-53*Fraction(3)**d-1)
        require(c != -1 or e != 7+d, ("possible equal slopes", d, c, e))
    m0, period = progression(PRECISION)
    require((pow(3, 108, 32)-1) % 32 == 16, "exact exponent period at 16")
    for r,(h,d) in enumerate(ROWS):
        m = m0 + period*((r-96-162*m0)*pow(162*period,-1,11) % 11)
        j = 97+162*m
        k, rem = divmod(j-1,11)
        require(rem == r, ("wrong remainder",r,rem))
        s = 3+7*k
        require(0 < s+d < j and h-r >= 0, (r,s,d))
        modulus = 2**(PRECISION-1)
        x = pow(3,s,modulus)
        require(pow(3,1134*period,modulus) == 1 and h <= PRECISION-1,
                ("failed progression lift",r))
        lo = affine_word(Fraction(2)**r, Fraction(-17), x, h)
        other = affine_word(Fraction(3)**d, Fraction(-1), x, h-r)
        require(lo == other, ("affine forms differ",r,h,d,lo,other))
        print(f"r={r:2}  clocks={h:3},{h-r:3}  earlier exponent=s{d:+}")
    print(f"All {len(ROWS)} second-arm branches on the 2^{PRECISION} obstruction cylinder meet earlier Mersenne orbits.")
