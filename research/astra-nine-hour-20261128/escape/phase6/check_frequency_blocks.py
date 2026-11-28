"""Independent finite orbit, fusion-cylinder, first-hit, and midpoint controls."""

from fractions import Fraction
from functools import lru_cache


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


@lru_cache(maxsize=None)
def marked(n, t):
    if not t:
        return n, 0
    endpoint, odds = marked(step(n), t - 1)
    return endpoint, odds + n % 2


@lru_cache(maxsize=None)
def until_one(n):
    if n == 1:
        return 0, 0
    ticks, odds = until_one(step(n))
    return 1 + ticks, n % 2 + odds


def constant_block(n, d, t):
    root = marked(n, t)
    return all(marked(n + offset, t) == root for offset in range(1, d))


def check_blocks():
    cylinders = 0
    marks = 0
    for t in range(1, 10):
        modulus = 2 ** t
        for d in (2, 3, 5, 8):
            for n in range(1, modulus + 1):
                first = constant_block(n, d, t)
                for lift in (1, 3, 7):
                    m = n + modulus * lift
                    require(first == constant_block(m, d, t), "fusion cylinder")
                    cylinders += 1
                    if not first:
                        continue
                    # The members all exceed one through t when m > 2**t.
                    times = [until_one(m + j) for j in range(d)]
                    require(all(value == times[0] for value in times), "first-one marks")
                    ticks, odds = times[0]
                    corrected = Fraction(2 ** ticks, 3 ** odds)
                    for j in range(d):
                        x = m + j
                        running = Fraction(x)
                        while x != 1:
                            if x % 2:
                                running *= Fraction(3 * x + 1, 3 * x)
                            x = step(x)
                        require(running == corrected, "constant corrected height")
                        marks += 1
    return cylinders, marks


def check_early():
    tests = 0
    for t in range(1, 10):
        # Each true depth-i fibre has no more than 2**i points over all positives.
        parents = lambda y: [2 * y] + ([(2 * y - 1) // 3] if y % 3 == 2 else [])
        for target in range(1, 65):
            layer = {target}
            seen = {target}
            for i in range(1, t):
                layer = {x for y in layer for x in parents(y)}
                require(len(layer) <= 2 ** i, "depth fibre bound")
                seen |= layer
            require(len(seen) < 2 ** t, "early hitting bound")
            for x in seen:
                require(any(marked(x, k)[0] == target for k in range(t)), "literal hit")
                tests += 1
    return tests


def odd_core(n):
    while n % 2 == 0:
        n //= 2
    return n


def check_midpoint():
    comparisons = 0
    for f in (lambda n: odd_core(n) % 3 == 1, lambda n: odd_core(n).bit_count() % 2 == 1):
        for a in range(1, 30):
            for length in range(65):
                fine = sum(f(k) != f(k // 2) for k in range(2 * a, 2 * (a + length)))
                coarse = sum(f(2 * k + 1) != f(2 * k) for k in range(a, a + length))
                require(fine == coarse, "dyadic midpoint")
                comparisons += 1
    return comparisons


if __name__ == "__main__":
    cylinders, marks = check_blocks()
    print("PASS", cylinders, "lifted fusion cylinders,", marks, "first-hit marks,",
          check_early(), "literal early hits,", check_midpoint(), "dyadic midpoint identities")
