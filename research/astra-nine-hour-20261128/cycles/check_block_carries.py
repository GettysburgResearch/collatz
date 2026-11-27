"""Exact bounded comparisons and literal rational-cycle checks for the two notes."""
from fractions import Fraction
from itertools import product
from math import gcd


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


def finite_carry_bound():
    checked = 0
    equalities = []
    for length in range(1, 256):
        base = 2**length
        for ones in range(length):
            slope = 3**ones
            if 3 * slope >= base:
                break
            largest = 2**(length-ones+1) * slope - slope - base
            target = (base-slope) * (base-3*slope)
            check(largest <= target, (length, ones, largest, target))
            if largest == target:
                equalities.append((length, ones))
            checked += 1
    check(equalities == [(2, 0)], equalities)
    return checked, equalities


def native_cycle(word):
    """Return distinct positive cleared numerators, denominator and minimum index."""
    length = len(word)
    determinant = 2**length - 3**sum(word)
    if determinant <= 0 or not any(word):
        return None
    intercept = sum(2**i * 3**sum(word[i+1:])
                    for i, bit in enumerate(word) if bit)
    root = Fraction(intercept, determinant)
    numerator, denominator = root.as_integer_ratio()
    phases = []
    for bit in word:
        if numerator in phases:
            return None
        phases.append(numerator)
        check(numerator % 2 == bit, ("branch", word, numerator))
        numerator = (3*numerator+denominator if bit else numerator) // 2
    check(numerator == phases[0], ("open trace", word))
    return phases, denominator


def check_calendars():
    counts = dict(primitive=0, contracting=0, straddling=0, packing=0, compatible=0)
    for s in range(1, 7):
        base = 2**s
        for tail in product(range(2), repeat=s-1):
            slope = 3**sum(tail)
            carry = sum(2**i * 3**sum(tail[i:]) for i in range(s))
            largest = 2**(s-sum(tail)+1) * slope - slope - base
            check(carry <= largest, ("carry", tail))
            for copies in range(2, 6):
                for free in product(range(2), repeat=copies):
                    if len(set(free)) == 1:
                        continue
                    word = tuple(t for bit in free for t in (bit, *tail))
                    cycle = native_cycle(word)
                    if cycle is None:
                        continue
                    phases, den = cycle
                    counts["primitive"] += 1
                    boundary = [2*a + den for a in phases[::s]]
                    for j, bit in enumerate(free):
                        check(base*boundary[(j+1) % copies] ==
                              slope*3**bit*boundary[j] + den*carry, ("block", word))
                    if 3*slope < base:
                        check(den*carry > (copies-1)*(base-slope)*(base-3*slope),
                              ("contracting", word))
                        counts["contracting"] += 1
                    else:
                        origin = boundary.index(min(boundary))
                        run = 0
                        while free[(origin-run-1) % copies] == 0:
                            run += 1
                        residual = (base-slope)*min(boundary) - den*carry
                        check(3*slope**(run+1) < base**(run+1) and
                              residual > 0 and residual % slope**run == 0,
                              ("terminal run", word))
                        counts["straddling"] += 1
                    minimum = min(phases)
                    for k in range(1, copies):
                        h = 2**k
                        if h >= copies:
                            break
                        check(2**(k*s) < 3**((h+1)//2)*(minimum+den), ("packing", word))
                        counts["packing"] += 1
                    for modulus in range(3, 40, 2):
                        image = {}
                        for i, value in enumerate(phases):
                            key = value % modulus
                            out = phases[(i+1) % len(phases)] % modulus
                            if key in image and image[key] != out:
                                break
                            image[key] = out
                        else:
                            if len(image) < len(word):
                                q = len(image)
                                changed = [c for c in range(q) if len(set(word[c::q])) > 1]
                                check(len(word) % q == 0 and len(changed) == 1,
                                      ("image word", word, modulus))
                                block = (word+word)[changed[0]:changed[0]+q]
                                K = sum(2**j * 3**sum(block[j+1:]) for j in range(q))
                                check(gcd(den, modulus) == 1 and K % modulus == 0,
                                      ("image return", word, modulus))
                                counts["compatible"] += 1
    return counts


if __name__ == "__main__":
    compared, ties = finite_carry_bound()
    print(f"Admissible (s,v) pairs at 1 <= s < 256: {compared}")
    print(f"Equalities: {ties}")
    for name, count in check_calendars().items():
        print(f"{name}: {count}")
