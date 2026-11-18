"""Exact arithmetic certificates for powered-cycle height arguments."""
from fractions import Fraction

from check_power_coverage import log_bounds, require


def certify_ratio(limit, target, lower, upper):
    # A dyadic enclosure gives inexpensive integer comparisons even
    # when the certified logarithms were initially much more precise.
    den = 2**100
    low_num = lower.numerator*den//lower.denominator
    high_num = upper.numerator*den//upper.denominator+1
    require(low_num+1 == high_num)
    for width in range(1, limit+1):
        count = width*den//high_num
        require(count == width*den//low_num)
        require(width*den < target*(width*den-high_num*count))


def main():
    log2_lo, log2_hi = log_bounds(2, 100)
    log3_lo, log3_hi = log_bounds(3, 100)
    lower, upper = log3_lo/log2_hi, log3_hi/log2_lo
    clo, cup = Fraction(19, 12), Fraction(485, 306)
    require(clo < lower < upper < cup)
    gamma = cup-1
    amp = 1+gamma/(1-cup/2)
    margin = 1-gamma*(amp+1)/(2*clo)
    require(margin > Fraction(1, 10))
    require(gamma/(2*clo*margin) < 2)
    require(820+494*1640**15 < 2**175)
    require(2**512 > 2**175 * 512**16)
    for width, cap in ((840000, 4*10**12), (98400, 5*10**9),
                       (12000, 14*10**6)):
        certify_ratio(width, cap, lower, upper)
    require(1640*512 <= 840000 and 1640*60 <= 98400)
    require((820+494*4*10**12)*512 < 2**60)
    require((820+494*5*10**9)*60 < 2**49)

    n, d = 766512153894657, 483615324366283
    require(Fraction(n, d) < lower < upper < Fraction(n, d)+Fraction(1, 2*d*2**49))
    require(2*d < 2**50)
    require(100*101+20*50 <= 12000)
    require(50*101+10*50 + 14*10**6*(30*101+7*50) < 48*10**9)

    lo = Fraction(103768467013, 65470613321)
    hi = Fraction(10439860591, 6586818670)
    require(log2_lo > Fraction(2, 3))
    require(lo < lower < upper+Fraction(1, 2**69) < hi)
    require(hi.numerator*lo.denominator-hi.denominator*lo.numerator == 1)
    require(hi.numerator+lo.numerator == 114208327604)
    print("R(W) certified at 840000, 98400, 12000")
    print("upper length below 48000000000; Farey lower length 114208327604")


if __name__ == "__main__":
    main()
