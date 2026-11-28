"""Exact small affine traces, checked by independent state and carry counts."""

from collections import Counter
from fractions import Fraction
from math import comb, gcd


def demand(condition):
    if not condition:
        raise ValueError("affine trace control failed")


def carry_words(steps):
    words = [(0, 0)]
    for index in range(steps):
        next_words = []
        for ones, carry in words:
            next_words.append((ones, carry))
            next_words.append((ones + 1, 3 * carry + 2**index))
        words = next_words
    return words


def trace_by_carry(modulus, steps, rho):
    contributions = Counter()
    for weight, carry in carry_words(steps):
        divisor = gcd(modulus, abs(2**steps - 3**weight))
        if carry % divisor == 0:
            contributions[weight] += divisor * rho**weight * (1 - rho)**(steps - weight)
    return contributions


def trace_by_states(modulus, steps, rho):
    # Entries store integer path weights; normalize only at the end.
    a, b = rho.numerator, rho.denominator - rho.numerator
    half = pow(2, -1, modulus)
    even = [(x * half) % modulus for x in range(modulus)]
    odd = [((3 * x + 1) * half) % modulus for x in range(modulus)]
    result = 0
    for root in range(modulus):
        counts = {root: 1}
        for _ in range(steps):
            new = Counter()
            for x, count in counts.items():
                new[even[x]] += b * count
                new[odd[x]] += a * count
            counts = new
        result += counts.get(root, 0)
    return Fraction(result, rho.denominator**steps)


def rooted_positive_count(steps, weight):
    determinant = 2**steps - 3**weight
    outcomes = []
    for v, carry in carry_words(steps):
        if v == weight and carry % determinant == 0:
            x = carry // determinant
            origin = x
            observed_weight = 0
            for _ in range(steps):
                observed_weight += x % 2
                x = (3 * x + 1) // 2 if x % 2 else x // 2
            demand(x == origin and observed_weight == weight)
            outcomes.append(origin)
    demand(len(set(outcomes)) == len(outcomes))
    return len(outcomes)


def check():
    rho = Fraction(3, 5)
    positive = set()
    for n in range(2, 13):
        for u in range(1, n + 1):
            d = 2**n - 3**u
            if d <= 0:
                continue
            count = rooted_positive_count(n, u)
            if count:
                positive.add((n, u, count))
            for e in (1, 2):
                modulus = d**e
                by_type = trace_by_carry(modulus, n, rho)
                signal = d * rho**u * (1 - rho)**(n - u) * count
                demand(by_type[u] == signal)
                if modulus <= 125:
                    demand(sum(by_type.values()) == trace_by_states(modulus, n, rho))
            for t in range(1, 8):
                for v in range(t + 1):
                    gap = abs(2**t - 3**v)
                    if n * v == u * t:
                        continue
                    divisor = gcd(d, gap)
                    demand(gcd(d**2, gap) <= divisor**2)
                    k, r = divmod(t, n)
                    w = v - k * u
                    numerator = 2**r * 3**max(0, -w) - 3**max(0, w)
                    demand(gcd(d, abs(numerator)) == divisor)
    demand(positive == {(j, j // 2, 2) for j in range(2, 13, 2)})
    d = 2**6 - 3**3
    by_type = trace_by_carry(d, 6, rho)
    demand(by_type[3] == 2 * d * rho**3 * (1 - rho)**3)
    # A genuine nonunit off-slope gcd on a composite determinant.
    d = 2**6 - 3**2  # 55
    demand(gcd(d, 2**4 - 1) == 5 and d > 5)
    demand(trace_by_carry(d, 4, rho)[0] == 5 * (1 - rho)**4)
    print("all exact traces, square covers, resonant word counts, and competing clocks agree")


if __name__ == "__main__":
    check()
