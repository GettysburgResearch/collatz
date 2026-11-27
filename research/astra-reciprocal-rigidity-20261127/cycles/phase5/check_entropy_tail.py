"""Exhaustive checks for canonical-cut divisor list bounds."""

from collections import Counter
from itertools import combinations
from math import comb, isqrt


def check(correct, message):
    if not correct:
        raise AssertionError(message)


def divisors(d):
    low = [a for a in range(1, isqrt(d)+1) if d % a == 0]
    return sorted(set(low + [d//a for a in low]))


def numerator(word):
    c = 0
    for i, bit in enumerate(word):
        if bit == "1":
            c = 3*c + 2**i
    return c


def canonical(word):
    n, u = len(word), word.count("1")
    h = [0]
    for bit in word:
        h.append(h[-1] + (n if bit == "1" else 0) - u)
    j = h.index(min(h))
    return word[j:] + word[:j]


def type_words(n, u):
    for positions in combinations(range(n), u):
        bits = ["0"] * n
        for pos in positions:
            bits[pos] = "1"
        yield "".join(bits)


def check_slice(n, u, macro):
    physical_n = 2*n+u if macro else n
    physical_u = n+u if macro else u
    d = abs(2**physical_n-3**physical_u)
    base_power = max(2**physical_n, 3**physical_u)
    moduli = divisors(d)
    counts = {g: Counter() for g in moduli}
    factor = 81 if macro else 1
    def physical(w):
        return "".join("110" if bit == "1" else "10" for bit in w) if macro else w
    for w in type_words(n, u):
        c = numerator(physical(w))
        z = canonical(w)
        for s in range(1, n+1):
            tz = z[-s:]
            check(n*tz.count("1") <= u*s, "incorrect canonical suffix sign")
            cz = numerator(physical(tz))
            check(cz**n < (factor*s)**n * base_power**s, "canonical numerator bound")
        for g in moduli:
            counts[g][c % g] += 1
    for g in moduli:
        s = max(t for t in range(n+1) if (factor*t)**n * base_power**t < g**n)
        k = n-s
        limit = n * sum(comb(k, b) for b in range((u*k+n-1)//n, k+1))
        check(counts[g][0] <= limit, "zero-residue list too large")
        if not macro:
            check(max(counts[g].values()) <= (u+1)*limit, "arbitrary residue list too large")
    return comb(n, u), len(moduli)


def main():
    binary = [check_slice(n, u, False)
              for n in range(2, 15) for u in range((n+1)//2, n)]
    dimer = [check_slice(n, u, True)
             for n in range(2, 12) for u in range((n+1)//2, n)]
    for name, values in (("binary", binary), ("dimer", dimer)):
        print(name, "canonical words", sum(v[0] for v in values),
              "divisor lists", sum(v[1] for v in values), "strata", len(values))


if __name__ == "__main__":
    main()
