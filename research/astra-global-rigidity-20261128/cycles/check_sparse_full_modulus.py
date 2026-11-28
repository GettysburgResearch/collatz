"""Exact arithmetic for sparse full-modulus bounds and the sharp edit family."""
from fractions import Fraction
from itertools import combinations, product
from math import gcd, lcm, prod


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def carry(word):
    odd, value = 0, 0
    for index, bit in enumerate(word):
        if bit:
            value = 3 * value + (1 << index)
            odd += 1
    return (1 << len(word)) - 3**odd, value


def least_period(word):
    prefix = [0] * len(word)
    for i in range(1, len(word)):
        j = prefix[i - 1]
        while j and word[i] != word[j]:
            j = prefix[j - 1]
        if word[i] == word[j]:
            j += 1
        prefix[i] = j
    candidate = len(word) - prefix[-1]
    return candidate if len(word) % candidate == 0 else len(word)


def small_swaps():
    cases = 0
    for n in range(2, 11):
        for word in product((0, 1), repeat=n):
            u = sum(word)
            d, old = carry(word)
            if u == 0 or d <= 0:
                continue
            sites = [i for i in range(n - 1) if word[i] != word[i + 1]]
            for k in range(1, min(3, len(sites)) + 1):
                for chosen in combinations(sites, k):
                    if any(b == a + 1 for a, b in zip(chosen, chosen[1:])):
                        continue
                    modified = list(word)
                    terms = []
                    for i in chosen:
                        modified[i], modified[i + 1] = modified[i + 1], modified[i]
                        terms.append((1 if word[i] else -1, i, sum(word[i + 2:])))
                    d2, new = carry(modified)
                    delta = sum(sign * (1 << i) * 3**s for sign, i, s in terms)
                    require(d == d2 and new - old == delta != 0, "signed carry difference")
                    cuts = chosen[1:] + (chosen[0] + n,)
                    _, seam = max((b - a, b % n) for a, b in zip(chosen, cuts))
                    shift = (-seam) % n
                    rebased = [
                        (sign, (i + shift) % n, s + ((i + shift) // n) * u)
                        for sign, i, s in terms
                    ]
                    places = [i for _, i, _ in rebased]
                    reduced = sum(sign * (1 << i) * 3**s for sign, i, s in rebased)
                    require((max(places) - min(places)) * k <= n * (k - 1), "time gap")
                    require(reduced != 0 and (reduced - (delta << shift)) % d == 0, "wrap")
                    q, q2 = d // gcd(d, old), d // gcd(d, new)
                    require(d // lcm(q, q2) == gcd(d, old, new), "joint denominator")
                    require(gcd(d, reduced) % (d // lcm(q, q2)) == 0, "gcd bound")
                    cases += 1
    return cases


def sharp_case(k, primes):
    length, weight = 65, 41
    a, b = 1 << length, 3**weight
    base = [((i + 1) * weight) // length - (i * weight) // length for i in range(length)]
    slots = [i for i in range(length - 1) if base[i:i + 2] == [1, 0]]
    slots.sort(key=lambda i: ((i + 1) * weight) % length)
    periods = [k, *primes]
    selected = slots[:len(periods)]
    extra = slots[len(periods)]
    m = prod(primes)
    count = k * m
    words = [[], []]
    for cell in range(count):
        middle = base.copy()
        for position, period in zip(selected, periods):
            if cell % period == 0:
                middle[position:position + 2] = [0, 1]
        words[0].extend(middle)
        if cell % m == 0:
            middle[extra:extra + 2] = [0, 1]
        words[1].extend(middle)
    endpoints = []
    for word in words:
        d, c = carry(word)
        x = Fraction(c, d)
        require(least_period(word) == len(word), "primitive clock")
        require(all(word[i] or word[(i + 1) % len(word)] for i in range(len(word))), "valuation cap")
        value, q = x.numerator, x.denominator
        for bit in word:
            require(value % 2 == bit, "actual rational parity")
            value = (3 * value + q) // 2 if bit else value // 2
        require(value == x.numerator, "closed realizer")
        endpoints.append(x)
    changed = sum(a != b for a, b in zip(*words))
    require(changed == 2 * k, "exact number of swaps")
    impulse = (1 << extra) * 3**sum(base[extra + 2:])
    expected = Fraction(impulse * b**(m - 1), a**m - b**m)
    require(endpoints[1] - endpoints[0] == expected, "geometric impulse")
    require(expected.denominator == a**m - b**m, "full impulse denominator")
    q, q2 = [x.denominator for x in endpoints]
    require(lcm(q, q2) == lcm(q, expected.denominator), "exact lcm")
    return k, len(words[0]), q.bit_length(), q2.bit_length(), lcm(q, q2).bit_length()


if __name__ == "__main__":
    print("signed swap configurations", small_swaps())
    for k, primes in ((2, (5, 7)), (3, (5, 7)), (4, (5, 7)), (5, (7, 11))):
        print("k, length, base bits, edited bits, lcm bits", *sharp_case(k, primes))
