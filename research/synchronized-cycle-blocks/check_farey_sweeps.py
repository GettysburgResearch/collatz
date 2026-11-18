"""Certify finite exponent/count exclusions using both Farey bounds."""
from fractions import Fraction
from math import ceil

from check_power_coverage import log_bounds, require


def enclose_log_ratio():
    low2, high2 = log_bounds(2, 210)
    low3, high3 = log_bounds(3, 210)
    scale = 2**400
    numerator = int(scale*low3/high2)
    lower, upper = Fraction(numerator, scale), Fraction(numerator+1, scale)
    require(lower <= low3/high2 < high3/low2 < upper)
    return lower, upper


def deficit_ratio(cap, lower, upper):
    # Walk the continued fraction to the last two Farey neighbors of
    # order cap. Their determinant and summed denominators certify them.
    p0, q0, p1, q1 = 0, 1, 1, 0
    numerator, denominator = lower.denominator, lower.numerator
    while denominator:
        quotient, remainder = divmod(numerator, denominator)
        if q0+quotient*q1 > cap:
            break
        p0, p1 = p1, p0+quotient*p1
        q0, q1 = q1, q0+quotient*q1
        numerator, denominator = denominator, remainder
    intermediate = (cap-q0)//q1
    left, right = sorted((Fraction(p0+intermediate*p1, q0+intermediate*q1),
                          Fraction(p1, q1)))
    require(left < 1/upper < 1/lower < right)
    require(left.denominator+right.denominator > cap)
    require(right.numerator*left.denominator-left.numerator*right.denominator == 1)
    return 1/(1-upper*left)


def check(exponent, rises, lower, upper):
    lo, hi = Fraction(1054, 665), Fraction(485, 306)
    require(lo < lower < upper < hi)
    amplification = (1+(hi-1)/(1-hi/exponent))**rises
    margin = 1-(hi-1)*(exponent+amplification-1)/(exponent*(exponent-1)*lo)
    require(margin > 0)
    j_z = max(1+1/(exponent-hi), 1/margin)
    j_s = (hi-1)/(exponent*(exponent-1)*lo*margin)

    def sweep(z, s):
        boundary = j_z*z+j_s*s
        increasing = ceil((amplification-1)*boundary/(lo-1))
        width = ceil(amplification*boundary/(exponent-hi))
        deficit = ceil((amplification-1)*boundary+s)
        first_length = ceil(boundary/(1-hi/exponent))
        return increasing, width, deficit, first_length

    t = 1024
    increasing, width, deficit, _ = sweep(16*t, 2*t)
    require(increasing+deficit*width**15 < 2**t)
    cap = 2**t
    for iteration in range(32):
        s = (cap+1).bit_length()
        z = 16*s if iteration == 0 else ceil(deficit_ratio(cap, lower, upper)+2).bit_length()
        increasing, width, deficit, first_length = sweep(z, s)
        if first_length < exponent:
            return "first length"
        new_cap = ceil(increasing+deficit*deficit_ratio(width, lower, upper))
        if new_cap < 114208327604:
            return "period"
        require(new_cap < cap)
        cap = new_cap
    raise AssertionError("finite certificate did not terminate")


if __name__ == "__main__":
    lo, hi = enclose_log_ratio()
    rows = ((2, 1), (3, 3), (4, 4), (5, 6), (6, 7), (8, 8),
            (9, 9), (12, 10), (16, 11), (20, 12), (32, 13),
            (64, 15), (128, 20), (256, 24), (512, 28),
            (1024, 31), (4096, 38))
    for exponent, rises in rows:
        print(exponent, rises, check(exponent, rises, lo, hi))
