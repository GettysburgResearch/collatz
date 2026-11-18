"""Exact bounded replay for two-power parity restrictions."""
from fractions import Fraction
from itertools import product


def require(condition):
    if not condition:
        raise AssertionError("exact replay failed")


def affine(word):
    a = b = 1
    c = 0
    for bit in word:
        if bit:
            a *= 3
            c = 3 * c + b
        b *= 2
    return a, b, c


def trajectory(start, word):
    states = [start]
    for bit in word:
        state = states[-1]
        require(state % 2 == bit)
        states.append((3 * state + 1 if bit else state) // 2)
    return states


def check_local_powers():
    cases = rising = falling = fixed = 0
    for width in range(1, 8):
        for word in product(range(2), repeat=width):
            a, b, c = affine(word)
            odds = sum(word)
            require(c <= 2**(width-odds)*(3**odds-2**odds) < 3**width)
            for exponent in range(2, 5):
                itinerary = word * exponent
                aa, bb, cc = affine(itinerary)
                residue = (-cc * pow(aa, -1, bb)) % bb
                for start in (residue or bb, (residue or bb) + bb):
                    states = trajectory(start, itinerary)
                    end = states[-1]
                    dx = (b-a)*start - c
                    dz = (b-a)*end - c
                    require(bb*dz == aa*dx)
                    require(dx % bb == dz % aa == 0)
                    cases += 1
                    if end == start:
                        require(dx == dz == 0 and states[width] == start)
                        fixed += 1
                        continue
                    minimum = min(states[:-1])
                    if end > start:
                        require(a > b and dx < 0)
                        require(min(states[:width]) == minimum)
                        require(start <= 2**(width-odds)*minimum)
                        rising += 1
                    else:
                        require(a < b and dz > 0)
                        require(min(states[-width-1:-1]) == minimum)
                        # Exact forward trace from the minimum to the end.
                        require(2**odds*(end+1) <= 3**odds*(minimum+1))
                        falling += 1
    require(rising and falling and fixed)
    return cases, rising, falling, fixed


def check_two_power_words():
    words = [word for width in range(1, 5)
             for word in product(range(2), repeat=width)]
    cases = ordinary = 0
    for u, v, a, b in product(words, words, (2, 3), (2, 3)):
        word = u*a+v*b
        aa, bb, cc = affine(word)
        cases += 1
        if aa >= bb or cc == 0 or cc % (bb-aa):
            continue
        start = cc//(bb-aa)
        states = trajectory(start, word)
        require(states[-1] == start and set(states) == {1, 2})
        require(states.index(start, 1) == 2)
        ordinary += 1
    require(ordinary > 0)
    return cases, ordinary


def log_bounds(x, terms):
    y = Fraction(x-1, x+1)
    lo = 2*sum((y**(2*j+1)/(2*j+1) for j in range(terms)), Fraction())
    tail = 2*y**(2*terms+1)/((2*terms+1)*(1-y*y))
    return lo, lo+tail


def check_sources_and_constants():
    # Independent of Eliahou's cycle-length conclusion, assuming Barina's
    # published ordinary verification through 2^68 stated in the packet.
    l2, u2 = log_bounds(2, 80)
    l3, u3 = log_bounds(3, 80)
    left = Fraction(16785921, 10590737)
    right = Fraction(17087915, 10781274)
    require(l2 > Fraction(1, 2))
    require(left < l3/u2 < u3/l2 + Fraction(1, 2**68) < right)
    require(right.numerator*left.denominator-left.numerator*right.denominator == 1)
    require(right.denominator+left.denominator > 2**24)

    c = Fraction(8, 5)
    gamma = c-1
    require(3**5 < 2**8)
    require(1-(c+gamma**2)/2 == Fraction(1, 50))
    require((1+gamma+c*gamma)*80 + 2*c == 208)
    require((1+gamma+c*gamma)*15 + 1+c == 41)
    require(208*16+2*41 == 3410)
    require(3410*16 < 65536)
    require(Fraction(3410*24, 2**24) < 1-Fraction(250, 252))
    return right.denominator+left.denominator


if __name__ == "__main__":
    print("local powers, increasing, decreasing, fixed:", *check_local_powers())
    print("two-power words, ordinary repeated trivial words:", *check_two_power_words())
    print("Farey denominator lower bound:", check_sources_and_constants())
