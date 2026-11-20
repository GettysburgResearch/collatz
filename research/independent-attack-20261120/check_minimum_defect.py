"""Exact finite checks for the minimum-location multiplier refinement.

No actual cycles are produced.  Analytic limiting arguments and the
Subspace-Theorem implication are written in MINIMUM_DEFECT.md.
"""

from fractions import Fraction as F
from itertools import product


C = F(485, 306)
GAMMA = C - 1
CEILING = F(11191, 48500)


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def threshold(c, gains):
    g1, g2, g3 = gains
    return 2 + g1 + g2 + g3 - (3 + 3*g1 + g2 + g3) / c


def charge_margin(c, gains, weighted_defect):
    g1, g2, g3 = gains
    gamma = c - 1
    u1 = 1 - (2-c)*g1/gamma
    up = g1 + g2 + g3 + 1 - c/gamma
    return 2*g1 - 2*u1 - up + c*weighted_defect/gamma


def numerator(word):
    a, b, bonus = 1, 1, 0
    for bit in word:
        bonus = (3 if bit else 1)*bonus + (b if bit else 0)
        a *= 3 if bit else 1
        b *= 2
    return a, b, bonus


def replay_minimum_splits():
    cases = 0
    for width in range(1, 8):
        for word in product((0, 1), repeat=width):
            a, b, bonus = numerator(word)
            if a >= b:
                continue
            aa, bb, cc = numerator(word*2)
            n = (-cc*pow(aa, -1, bb)) % bb + bb
            states = [n]
            for bit in word*2:
                z = states[-1]
                require(z % 2 == bit, "ordinary parity replay")
                states.append((3*z+1)//2 if bit else z//2)
            p = ((b-a)*states[0]-bonus)//b**2
            require(p > 0, "positive contracting multiplier")
            offset = min(range(width+1), key=lambda j: states[width+j])
            m = states[width+offset]
            previous = states[offset]
            suffix_width = width-offset
            prefix_ones = sum(word[:offset])
            require(previous-m == p*2**suffix_width*3**prefix_ones,
                    "corresponding minimum-phase displacement")
            correction = F(1)
            for state in states[width+offset:2*width]:
                if state % 2:
                    correction *= F(3*state+1, 3*state)
            suffix_ones = sum(word[offset:])
            ratio = F(3**suffix_ones, 2**suffix_width)*correction
            require(F(states[-1], m) == ratio, "exact suffix product")
            cases += 1
    return cases


def main():
    require(3**306 < 2**485, "upper logarithm bound")
    box = [(F(49, 100), F(51, 100)),
           (F(49, 100), F(51, 100)),
           (F(99, 100), F(101, 100))]
    vertices = list(product(*box))
    thresholds = [threshold(C, gains) for gains in vertices]
    require(max(thresholds) == CEILING, "exact maximum defect threshold")
    require(CEILING < F(1, 4), "quarter-height sufficient exclusion")
    margins = [charge_margin(C, gains, F(1, 4)) for gains in vertices]
    require(min(margins) == F(467, 8950), "uniform positive charge margin")
    require(min(margins) > F(1, 20), "strict Subspace-Theorem margin")
    # In the whole box the source error 2*g1 is the weakest of all
    # three guaranteed savings, and exceeds the secondary-term gap g1.
    require(F(102, 100) < F(197, 100), "source saving below descending gap")
    require(F(102, 100) < F(198, 100)/C, "source saving below transport gap")
    require(F(49, 100) > 0, "two retained terms have a strict height gap")
    u1_max = 1 - (2-C)*F(49, 100)/GAMMA
    divisor_min = C/GAMMA + F(197, 100)
    require(divisor_min-u1_max == F(36043, 8950),
            "divisibility contradiction remains strict")
    even_fraction = GAMMA*(CEILING/2)/(F(49, 100)+C*(CEILING/2))
    require(even_fraction == F(2003189, 19971815), "root even-density bound")
    require(even_fraction < F(101, 1000), "root even density below 10.1 percent")
    require(charge_margin(C, (F(1, 2), F(1, 2), F(1)), F(0)) < 0,
            "zero-defect abstract profile remains outside this comparison")

    print("maximum necessary weighted-defect threshold:", CEILING)
    print("quarter-height defect charge margin:", min(margins))
    print("divisibility margin:", divisor_min-u1_max)
    print("first rising root even-density ceiling:", even_fraction)
    print("ordinary minimum-split replays:", replay_minimum_splits())
    print("negative control: zero-defect abstract profile not excluded")
    print("PASS: minimum-location refinement constants and exact local identities")


if __name__ == "__main__":
    main()
