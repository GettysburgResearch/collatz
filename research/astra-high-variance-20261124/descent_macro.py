"""Exact certificates for the expanding-tail shadow and the signed pair obstruction."""

from fractions import Fraction

HEADERS = {"PPLLL": (5583, 12, -6), "PLLPL": (5583, 12, -6),
           "PLLPP": (72873, 16, -9)}
MACROS = ("L",) + tuple("L"*6 + end for end in ("P", "PP", "PLP", "PLLP"))


def check(ok, message):
    if not ok:
        raise ArithmeticError(message)


def source(word):
    time = odds = carry = 0
    for letter in word:
        check(letter in "LP", "unknown source block")
        duration, increment = (3, 7) if letter == "L" else (5, 5)
        carry = 9*carry + (increment << time)
        time += duration
        odds += 2
    return time, odds, carry


def walk(x, time):
    bits = []
    for _ in range(time):
        bit = x.numerator % 2
        bits.append(str(bit))
        if isinstance(x, Fraction):
            check(x.denominator % 2 == 1, "even denominator in signed lift")
            x = (3*x+1)/2 if bit else x/2
        else:
            x = (3*x+1)//2 if bit else x//2
    return x, "".join(bits)


def certificate(time, odds, carry):
    modulus = 1 << time
    slope = 3**odds
    b = -carry*pow(slope, -1, modulus) % modulus
    end, bits = walk(b, time)
    check(bits.count("1") == odds and modulus*end == slope*b+carry,
          f"incorrect parity carry {time}, {odds}, {carry}")
    return b, end, bits


def reset(m, d, word):
    a, p, c = source(word)
    g = m*(c-7*3**p + (7 << a))
    check(g % (1 << d) == 0, "nonintegral reset carry")
    target = (g >> d)+7*(3**p-(1 << a))
    return a, p, target, *certificate(a, p, target)


def entrance(word):
    m, d, ell = HEADERS[word]
    a, p, c = source(word)
    time, odds = a+d-1, p-ell
    target = m*((c-7*3**p + (7 << a))//2) - (7 << time) + 3**odds
    return time, odds, target, *certificate(time, odds, target)


def floor_control():
    # For an actual first paid preceded by r<=6 light blocks, its boundary
    # is smaller than both initial floors as soon as q0>=17. At r=0 just
    # compare it with the initial boundary. Smaller positive sources converge.
    for r in range(7):
        a, p, c = source("L"*r + "P")
        check(4*3**p < 3*(1 << a), "wrong leading slope")
        check(4*(3**p*17+c) < (3*17+1)*(1 << a), "floor at 17")
    for name, (m, d, ell) in HEADERS.items():
        # At r>=7 the numerator ratio relative to q0+7 is <= 0.557.
        check(8*m <= 5*(1 << (8-ell)), name)
        check(14+ell >= 1, "empty ramp")


def signed_control():
    for k in range(-9, 0):
        z = -1 - 3403*Fraction(3)**k
        seen = set()
        while z not in seen:
            check(z != -7, "exception reached the forbidden terminal point")
            seen.add(z)
            z, _ = walk(z, 1)
    coef = Fraction(63*3403, 65*512)
    check(coef*Fraction(169, 162)**2 > 7 and coef*Fraction(27, 26)**3 > 7,
          "signed growth bound")
    for s in range(2):
        for k in range(min(2, 2*s)+1):
            z, bits = walk(-1 - 3403*3**k, 3*s+9)
            check(z != -7 or bits.count("1") != 2*s-k, "exceptional pair")


def main():
    floor_control()
    signed_control()
    for m, d in sorted({(m, d) for m, d, _ in HEADERS.values()}):
        for w in MACROS:
            a, p, c, b, e, code = reset(m, d, w)
            check(2*p > a, "target cycle could alternate indefinitely")
            print(f"reset {m}/2^{d} {w} {code}")
    for w in HEADERS:
        a, p, c, b, e, code = entrance(w)
        print(f"entry {w} {a} clocks, {p} odds, {code}")


if __name__ == "__main__":
    main()
