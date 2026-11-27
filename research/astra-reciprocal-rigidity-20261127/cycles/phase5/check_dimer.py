"""Exact finite controls for dimer harmonic mass and ordinary survivor packing."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import comb


def check(condition, description):
    if not condition:
        raise AssertionError(description)


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


def factor_words(max_ones):
    # Every odd-start factor with q ones has length at most 2q.
    todo = ["1"]
    while todo:
        w = todo.pop()
        if w.count("1") > max_ones:
            continue
        yield w
        if w[-1] == "1":
            todo.append(w + "0")
        if not w.endswith("11"):
            todo.append(w + "1")


def tail(k):
    return Fraction(4, 2 ** k) + Fraction(4 * (-1) ** k, 5 * 4 ** k)


def threshold(m):
    k = 0
    while 2 * (3*m + 1) ** k <= m ** (k+1):
        k += 1
    return k


def grammar():
    max_ones = 16
    all_by_ones = Counter()
    total = 0
    by_count = Counter()
    for w in factor_words(max_ones):
        q = w.count("1")
        by_count[len(w), q] += 1
        all_by_ones[q] += Fraction(1, 2 ** len(w))
        total += 1
    for q in range(1, max_ones+1):
        check(all_by_ones[q] == Fraction(2, 2**q) + Fraction((-1)**q, 4**q),
              "unsigned word weight")
        check(all_by_ones[q] == tail(q)-tail(q+1), "tail difference")
    for t in range(1, max_ones+1):
        for q in range(1, t+1):
            blocks = t-q
            combined = 0
            for trailing in (0, 1, 2):
                extra = t-2*blocks-trailing
                if 0 <= extra <= blocks:
                    combined += comb(blocks, extra)
            check(by_count[t, q] == combined, "odd-count binomial formula")
    print("factor grammar", total, "words up to", max_ones, "ones")


def odd_start_back(y, t):
    if y % 2 == 0:
        if (2*y-1) % 3 or t == 0:
            return None
        y = (2*y-1)//3
        t -= 1
    while t:
        if y % 3 == 0:
            return None
        a = 2 if y % 3 == 1 else 1
        if a > t:
            return None
        y = ((2 ** a)*y-1)//3
        t -= a
    return y


def shell_and_inversion():
    floors = (2, 3, 7, 20, 64, 100, 256, 1000, 4096)
    keys = {m: threshold(m) for m in floors}
    mass = Counter()
    seen = defaultdict(set)
    count = 0
    for x in range(1, 2**16, 2):
        y = x
        word = ""
        least = x
        tmax = x.bit_length()-1
        for t in range(tmax+1):
            # Include the endpoint bit for the no-consecutive-even inversion.
            extended = word + str(y % 2)
            if "00" not in extended:
                check(odd_start_back(y, t) == x, "fixed physical lag inversion")
                check(y not in seen[t], "duplicate fixed-time endpoint")
                seen[t].add(y)
                count += 1
            if t == tmax and "00" not in word and "111" not in word:
                for m in floors:
                    if least >= m:
                        check(word.count("1") >= keys[m], "dyadic floor threshold")
                        mass[m] += Fraction(1, x)
            word += str(y % 2)
            y = step(y)
            least = min(least, y)
    for m in floors:
        check(mass[m] <= tail(keys[m]), "finite simultaneous reciprocal bound")
    print("fixed physical lag inversions", count, "floor controls", len(floors))
    check(threshold(2**71) == 45, "reported dyadic cutoff")
    check(301**44 < 2**70 * 100**44, "integer cutoff certificate")
    check(tail(45)/3 < Fraction(1, 2**44), "defect epsilon")
    print("verified floor 2^71, odd threshold 45, rational log upper bound", tail(45)/3)


def inverse_histories():
    tests = 0
    for b in range(1, 11):
        mod = 3**b
        for a in product((1, 2), repeat=b):
            pos = c = 0
            for gap in a:
                c = 3*c + 2**pos
                pos += gap
            residue = c * pow(2, -pos, mod) % mod
            shell = [z for z in (residue+mod, residue+2*mod) if z % 2]
            check(len(shell) == 1, "one odd target in two full residue classes")
            for endpoint in shell:
                x = (2**pos * endpoint-c)//mod
                if x <= 0:
                    continue
                for gap in a:
                    check((3*x+1) % 2**gap == 0, "inverse affine divisibility")
                    x = (3*x+1)//2**gap
                    check(x % 2 == 1, "inverse gap was exact")
                check(x == endpoint, "past word replay")
                tests += 1
    print("reverse ternary word replays", tests)


def four_budgets():
    k = threshold(2**71)
    fib = [0, 1]
    for _ in range(k):
        fib.append(fib[-1]+fib[-2])
    avoid1 = 4 * Fraction(3, 4)**(k-1) / 3
    avoid7 = (6-sum(2*Fraction(fib[q+1], 2**q) for q in range(1,k)))/3
    reverse = [Fraction(1), Fraction(1,3)]
    for _ in range(2, 70):
        reverse.append((reverse[-1]+reverse[-2])/3)
    avoid5 = (3-sum(reverse))/3
    cases = ((avoid1,17), (avoid5,26), (avoid7,12), (tail(k)/3,44))
    for val, shift in cases:
        check(0 < val < Fraction(1, 2**shift), "published strict budget")
    check(avoid7 == Fraction(25039203,137438953472), "avoid-7 certificate")
    check(avoid5 == Fraction(20869941361188745555087058,
                              2503155504993241601315571986085849), "avoid-5 certificate")
    for q in range(1, 10):
        # Sum exactly over all *internal* run compositions for no111;
        # the geometric zero gaps have total weight one when nonempty.
        direct = sum(1 for j in range(1,q+1) for v in product((1,2),repeat=j) if sum(v)==q)
        check(direct == fib[q+1], "avoid-7 zero-gap aggregation")
    print("four positive-entropy all-period budget powers", [i for _,i in cases])


def moving_intervals():
    forward_count = reverse_count = 0
    for t in range(1, 11):
        span = 2**t
        for low in (1, 5*span+7, 10**30+25):
            targets = set()
            for x in range(low, low+span):
                if x % 2 == 0:
                    continue
                y, q, bits = x, 0, ""
                for _ in range(t):
                    q += y % 2
                    bits += str(y % 2)
                    y = step(y)
                if "00" in bits+str(y % 2):
                    continue
                check(y not in targets, "interval source inverse collision")
                targets.add(y)
                check(3**q*low <= span*y < 3**q*(low+span)+3**t,
                      "translated forward endpoint escaped")
                forward_count += 1
    for b in range(1, 8):
        mod = 3**b
        for low in (1, 7*mod+3, 10**30+131):
            for a in product((1, 2), repeat=b):
                s = c = 0
                for gap in a:
                    c = 3*c + 2**s
                    s += gap
                r = c*pow(2,-s,mod) % mod
                y = low+(r-low)%mod
                z = (2**s*y-c)//mod
                check(c <= 4**b-3**b, "reverse intercept")
                check(2**s*low-4**b <= mod*z < 2**s*(low+mod),
                      "translated backward predecessor escaped")
                reverse_count += 1
    print("moving-interval images", forward_count, "and inverse cylinders", reverse_count)


if __name__ == "__main__":
    grammar()
    shell_and_inversion()
    inverse_histories()
    four_budgets()
    moving_intervals()
