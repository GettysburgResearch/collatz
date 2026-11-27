"""Exact regulator-sign enclosures, rational rotation phases and the surviving
seven-adic coordinate on the ordinary one-cycle. Standard-library arithmetic.
"""

from fractions import Fraction as F
from math import gcd


def require(condition):
    if not condition:
        raise ArithmeticError("regulator-control mismatch")


def taylor_interval(t, power, steps=48):
    """Interval for sum_{n>=1} t^n / n^power with exact geometric tail bound."""
    terms = sum((t**n / n**power for n in range(1, steps + 1)), F(0))
    tail = t**(steps + 1) / ((steps + 1)**power * (1 - t))
    return terms, terms + tail


def rogers_interval(t):
    li_lo, li_hi = taylor_interval(t, 2)
    a_lo, a_hi = taylor_interval(t, 1)
    b_lo, b_hi = taylor_interval(1 - t, 1)
    return li_lo + a_lo*b_lo/2, li_hi + a_hi*b_hi/2


def clocks_signs():
    c0, c1 = (2 * t for t in rogers_interval(F(1, 2)))
    g0, g1 = rogers_interval(F(4, 9))
    s0, s1 = rogers_interval(F(9, 16))
    f1 = g0 - c1, g1 - c0
    f2 = c0 - s1, c1 - s0
    require(F(-901, 1000) < f1[0] <= f1[1] < F(-898, 1000))
    require(F(734, 1000) < f2[0] <= f2[1] < F(737, 1000))
    require(c1 < F(165, 100))
    require(2**158 < 3**100 < 2**159)
    require(F(42,100)*f1[0]+F(58,100)*f2[0] > 0)
    require(F(705,1000)*f1[1]+F(295,1000)*c1 < 0)


def rotation(B, b, m):
    A = m + (B - 1) * b
    D = 2**A - 3**m
    require(gcd(b, m) == 1 and m % 2 == 1 and D > 0 and D % 8 == 5)
    numerators = [
        sum(3**(m-1-j) * 2**(j+(B-1)*((j*b+r)//m)) for j in range(m))
        for r in range(m)
    ]
    for r, n in enumerate(numerators):
        a = 1 + (B-1)*((r+b)//m)
        next_r = (r+b) % m
        third = numerators[(r+2*b) % m]
        require(gcd(n, D) == 1)
        require(2**a*numerators[next_r] == 3*n+D)
        if a == 1:
            require(n % 4 == 3 and 5 % gcd(n, third) == 0)
        if a == 2:
            require(n % 8 == 5 and 7 % gcd(n, third) == 0)
    return m


def p7(n):
    if not n:
        return 1000000
    count = 0
    while n % 7 == 0:
        n //= 7
        count += 1
    return count


class Quadratic(tuple):
    """An exact rational linear combination of 1 and sqrt(3)."""
    def __new__(cls, a=0, b=0):
        return super().__new__(cls, (F(a), F(b)))

    @staticmethod
    def scalar(x):
        return x if isinstance(x, Quadratic) else Quadratic(x)

    def __add__(self, other):
        a, b = self.scalar(other)
        return Quadratic(self[0]+a, self[1]+b)

    __radd__ = __add__

    def __neg__(self):
        return Quadratic(-self[0], -self[1])

    def __sub__(self, other):
        return self + -self.scalar(other)

    def __rsub__(self, other):
        return self.scalar(other) + -self

    def __mul__(self, other):
        a, b = self.scalar(other)
        return Quadratic(self[0]*a+3*self[1]*b, self[0]*b+self[1]*a)

    __rmul__ = __mul__

    def inverse(self):
        norm = self[0]**2 - 3*self[1]**2
        return Quadratic(self[0]/norm, -self[1]/norm)

    def __truediv__(self, other):
        return self * self.scalar(other).inverse()

    def __pow__(self, k):
        if k < 0:
            return self.inverse() ** (-k)
        x, res = self, Quadratic(1)
        while k:
            if k % 2:
                res = res*x
            x = x*x
            k //= 2
        return res

    def valuation7(self):
        # Seven is unramified inert and 1,sqrt(3) is an integral basis.
        return min(p7(t.numerator)-p7(t.denominator) for t in self)


def surviving_seven():
    X = Quadratic(7, -4)
    q = Quadratic(F(3, 4))
    s2 = X**2 / q
    R = X / (q-X**2)
    S = ((1-s2)/X)**2
    H = 1+R**6+R**12
    z = (S*H**2)**-1
    J = 1+z**24
    result = tuple(x.valuation7() for x in (R,S,H,z,J))
    require(result == (-1,2,-12,22,0))
    # The displayed contraction is a non-one local unit.
    T = q * X**2 * R**12 / (H * J**22)
    require(T.valuation7() == 0 and T != Quadratic(1))
    return result


def main():
    clocks_signs()
    sizes = rotation(2, 3, 5), rotation(2, 24, 41), rotation(3, 5, 17), rotation(3, 12, 41)
    print("certified_clock_sign_intervals=2; opposite_centered_mean_signs=2")
    print("exact_rotated_odd_periods=" + ",".join(map(str, sizes)))
    print("surviving_prime_7_valuations=" + ",".join(map(str, surviving_seven())))


if __name__ == "__main__":
    main()
