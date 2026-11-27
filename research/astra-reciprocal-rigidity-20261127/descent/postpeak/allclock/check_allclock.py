"""Exact finite controls for the two all-clock density deductions."""
from fractions import Fraction
from itertools import product
from math import comb


def require(condition, message):
    if not condition:
        raise ValueError(message)


def intercept(word):
    numerator = 0
    odds = 0
    for i, letter in enumerate(word):
        if letter == "O":
            odds += 1
            numerator = 3*numerator + 2**i
    return odds, numerator


def offset(word):
    odds, numerator = intercept(word)
    return numerator - 3**odds


def run_word(x, word):
    for branch in word:
        require((x % 2 == 1) == (branch == "O"), ("ordinary parity", x, branch))
        x = (3*x+1)//2 if branch == "O" else x//2
    return x


def original(height, word):
    f = word.count("O")
    mod = 2**len(word)
    v = -offset(word)*pow(3**(height+f), -1, mod) % mod
    v = v or mod
    n = 2**height * v - 1
    target = run_word(3**height*v-1, word)
    require(2**len(word)*target == 3**(height+f)*v + offset(word), "target formula")
    return n, v, target


def signed_stops(word, height, even_cap):
    """Enumerate native-at-the-ternary-root stops, not all formal strings."""
    t = len(word)
    f = word.count("O")
    q = t-f
    total_odd = height+f
    n, v, target = original(height, word)
    root = Fraction(offset(word), 2**t)
    stack = [(root, 0, 0, "", root, 0)]
    stopped = set()
    checks = 0
    while stack:
        z, odds, evens, first_t, cut, cut_odds = stack.pop()
        length = odds+evens
        if odds == total_odd:
            require(length >= t and z.denominator == 1 and z.numerator % 2 != 0,
                    "stopped signed source must be odd")
            beta = first_t[::-1]
            require(cut == Fraction(offset(word)-intercept(beta)[1], 3**cut_odds),
                    "signed suffix formula")
            require(cut.denominator == 1 and abs(cut) <= 2*3**(t-cut_odds), "signed bound")
            # These controls use H >= 12(t+2) and ell <= H/12.
            require(cut == -1 and offset(beta) == offset(word), "short-even signed trap")
            delta = f-cut_odds
            residual_evens = evens-(t-cut_odds)
            require(residual_evens >= 0 and z <= -1 and -z <= 2**residual_evens,
                    "residual reflected origin")
            positive_stop = z + Fraction(2)**(evens-q)*(n+1)
            lifted = z + Fraction(2)**length/3**total_odd*(target-root)
            require(positive_stop == lifted and positive_stop.denominator == 1 and positive_stop > 0,
                    "lifted ordinary stop")
            require(evens-q == residual_evens+delta,
                    "scale shift")
            key = evens, beta, z
            require(key not in stopped, "stopped prefix encoding fails injectivity")
            stopped.add(key)
            checks += 1
            continue
        def push(branch, zz, oo, ee):
            if length < t:
                stack.append((zz, oo, ee, first_t+branch, zz, oo))
            else:
                stack.append((zz, oo, ee, first_t, cut, cut_odds))
        if evens < even_cap:
            push("E", 2*z, odds, evens+1)
        odd = (2*z-1)/3
        if odd.denominator % 3 != 0:
            push("O", odd, odds+1, evens)
    return checks


def controls():
    require(3**5 < 2**8 and 2**5 < 3**4, "logarithmic rational comparisons")
    require(5**250 < 2**245 * 3**150 * 2**100, "entropy H(3/5)")
    require(8**200 < 2**192 * 5**125 * 3**75, "entropy H(5/8)")
    require(Fraction(51,50)-Fraction(3,125) == Fraction(249,250), "arrival exponent")
    require(Fraction(51,50)*Fraction(49,50) == Fraction(2499,2500), "image exponent")
    joint, zero = Fraction(284051,829440), Fraction(1041139,4147200)
    require(joint-Fraction(1,2**16) > Fraction(1,3) and zero-Fraction(1,2**16) > Fraction(1,4),
            "postpeak protection margins")
    require(Fraction(151,150)-Fraction(1,50)-Fraction(89,90) < 0 and
            Fraction(151,150)*Fraction(49,50)-Fraction(89,90) < 0,
            "uniform relative long-arrival exponents")
    print("entropy and shell exponents checked", "249/250", "2499/2500")

    total = gains = signs = 0
    fibers = []
    for t in range(9):
        words = ["".join(v) for v in product("EO", repeat=t)]
        groups = {}
        for w in words:
            group = groups.setdefault(offset(w), {})
            grade = w.count("O")
            require(grade not in group, "two words with the same weight and signed offset")
            group[grade] = w
        require(len(groups) >= comb(t,t//2), "central binomial lower bound")
        fibers.append(len(groups))
        for w in words:
            vlist = groups[offset(w)]
            heavier = max(vlist)
            f = w.count("O")
            n, v, target = original(600,w)
            total += 1
            if heavier > f:
                p = 600+f-heavier
                m = 2**p*v-1
                require(0<m<n and run_word(3**p*v-1,vlist[heavier]) == target,
                        "explicit smaller companion")
                gains += 1
            if t <= 5:
                signs += signed_stops(w,96,5)
    print("exhaustive postwords through clock 8", total, "nonmaximal ordinary companions", gains)
    print("signed-offset fibre counts through clock 8", *fibers)
    print("signed stopped prefixes through five evens, all upper clocks at most 5, H=96", signs)
    print("complete visitor clocks in the density conclusions use the cited long-arrival proof")


if __name__ == "__main__":
    controls()
