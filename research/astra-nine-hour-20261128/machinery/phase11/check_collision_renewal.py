"""Exact finite collision tilt, unequal-clock spacing and first-split tests."""
from collections import defaultdict
from fractions import Fraction
from itertools import product


def require(flag, message):
    if not flag:
        raise ValueError(message)


def gap_path(start, count):
    out = []
    for _ in range(count):
        numerator = 3 * start + 1
        gap = (numerator & -numerator).bit_length()-1
        start = numerator >> gap
        out.append(gap)
    return tuple(out), start


def numerator(word):
    total = 0
    n = 0
    for e in word:
        n = 3*n + (1 << total)
        total += e
    return n


def check():
    cap, depth = 4, 5
    r = Fraction(2, 5)
    u = r*r
    last_u = Fraction(1)
    pair_count = positive_count = split_count = 0
    for n in range(1, depth+1):
        mod = 3**n
        rows = defaultdict(list)
        for w in product(range(1, cap+1), repeat=n):
            s = sum(w)
            num = numerator(w)
            rows[num*pow(2, -s, mod) % mod].append((w, s, num))
        masses = [sum((1-r)**n*r**(s-n) for _, s, _ in row)
                  for row in rows.values()]
        sliced = defaultdict(Fraction)
        offdiag = Fraction()
        for row in rows.values():
            for w, s, num in row:
                source_weight = (1-u)**n*u**(s-n)
                modulus = 1 << (s+1)
                x = (((1 << s)-num)*pow(mod, -1, modulus)) % modulus
                x += 3 * (1 << (cap*n+1))
                path, y = gap_path(x, n)
                require(path == w, "supplied positive word")
                for v, t, other in row:
                    d = t-s
                    pair_count += 1
                    term = r**d*source_weight
                    sliced[d] += term
                    if w[-1] != v[-1]:
                        offdiag += term
                        split_count += 1
                    if d < 0:
                        continue
                    diff = (1 << d)*num-other
                    require(diff % mod == 0, "integer offset")
                    h = diff // mod
                    require(-other < mod*h < (1 << d)*num, "opposite bounds")
                    require((mod*h+other) % (1 << d) == 0,
                            "single displacement residue from longer word")
                    x2 = (1 << d)*x+h
                    require(x2 > 0 and gap_path(x2, n) == (v, y),
                            "actual affine counted collision")
                    # Both physical streams on these cylinders have n odd steps.
                    require((1-u)**n*u**(t-n) == u**d*source_weight,
                            "finite biased image likelihood")
                    positive_count += 1
        total = sum(sliced.values())
        require(total == ((1+r)/(1-r))**n*sum(p*p for p in masses),
                "ordered pair identity")
        require(all(value == sliced[-d] for d, value in sliced.items()),
                "clock-sign symmetry")
        require(total-(1-u**cap)*last_u == offdiag,
                "truncated same-outer-letter recurrence")
        last_u = total
    print("depth, cap:", depth, cap)
    print("ordered pairs, positive affine path checks, distinct last letters:",
          pair_count, positive_count, split_count)


if __name__ == "__main__":
    check()
