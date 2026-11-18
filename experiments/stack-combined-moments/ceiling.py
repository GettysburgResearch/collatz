"""Rational signs for the 588 single-window obstruction."""
from fractions import Fraction as F


def log_bounds(integer):
    x = F(integer-1, integer+1)
    n = 24
    low = 2*sum(x**(2*j+1)/(2*j+1) for j in range(n))
    high = low + 2*x**(2*n+1)/((2*n+1)*(1-x*x))
    return low, high


def main():
    lower, upper = F(9463946, 10**7), F(9463947, 10**7)
    l2, u2 = log_bounds(2)
    l3, u3 = log_bounds(3)
    assert lower < 3*l2/(2*u3) < 3*u2/(2*l3) < upper
    e, f = 1-upper, 1-lower
    a = 588**2 * e*e/4 - f**3/2
    b = e*(1+lower) - f**3
    c = -upper + e*(1+lower) + e/2 - f**3/2
    d = e/3
    disc = 18*a*b*c*d - 4*b**3*d + (b*c)**2 - 4*a*c**3 - 27*(a*d)**2
    assert a > 0 and d > 0 and disc < 0
    print("Certified logarithm enclosure and negative cubic discriminant at period 588")


if __name__ == "__main__":
    main()
