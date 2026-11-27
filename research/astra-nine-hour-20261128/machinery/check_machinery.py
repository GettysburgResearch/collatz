"""Finite controls for the written ordinary-routing and mixed-conductor arguments."""

from collections import defaultdict, deque
from itertools import combinations
from math import gcd


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def order_two(modulus):
    value = 2 % modulus
    order = 1
    while value != 1:
        value = 2 * value % modulus
        order += 1
    return order


def route(modulus, start, stop):
    queue = deque([(start, [])])
    seen = {start}
    while queue:
        value, letters = queue.popleft()
        if value == stop:
            return letters
        for exponent in (2, 4):
            end = ((2**exponent * value - 1) * pow(3, -1, modulus)) % modulus
            if end not in seen:
                seen.add(end)
                queue.append((end, letters + [exponent]))
    raise AssertionError("residue graph disconnected")


def corrected_step(value, base, period):
    for k in range(3):
        exponent = base + 2 * k * period
        numerator = (value << exponent) - 1
        if numerator % 9 == 3:
            next_value = numerator // 3
            require(next_value > 0 and next_value % 2 == 1, "the successful inverse step must be positive and odd")
            require((3 * next_value + 1) >> exponent == value, "the actual odd map must return the incoming seed")
            return next_value, exponent
    raise AssertionError("missing ternary digit")


def check_ordinary_routes():
    paths = letters_checked = 0
    for modulus in range(5, 36):
        if gcd(modulus, 6) != 1:
            continue
        period = order_two(modulus)
        if period % 3 == 0:
            continue
        for seed in range(1, 32, 2):
            if seed % 3 == 0:
                continue
            start, first = corrected_step(seed, 1 if seed % 3 == 2 else 2, period)
            for desired in range(modulus):
                via = route(modulus, start % modulus, 1)
                out = route(modulus, 1, desired)
                pad = 2 * (modulus - 1) - len(via) - len(out)
                require(pad >= 0, "a shortest path through residue one exceeds the padding budget")
                value = start
                clock = first
                for nominal in via + [2] * pad + out:
                    value, exponent = corrected_step(value, nominal, period)
                    clock += exponent
                    letters_checked += 1
                require(value % modulus == desired, "the exact ordinary route failed its requested congruence")
                require(clock <= (4 + 4 * period) * (2 * modulus - 1), "the exact ordinary route exceeded its raw valuation bound")
                paths += 1
    return paths, letters_checked + paths


def balanced(value, modulus):
    residue = value % modulus
    return residue - modulus if residue > modulus // 2 else residue


def check_triangle_geometry():
    sites = corners_checked = 0
    for depth in range(0, 5):
        for coprime in (5, 7, 11, 25):
            modulus = 3**depth * coprime
            period = order_two(modulus)
            horizon = 7
            for frequency in (1, coprime - 1, 3**depth):
                if frequency % coprime == 0:
                    continue
                def amplitude(j, level):
                    raw = frequency * pow(9, j - 1, modulus) * pow(2, 1 - level, modulus)
                    return abs(balanced(raw, modulus))

                def black(j, level):
                    return 20 * amplitude(j, level) <= modulus

                tips = set()
                for j in range(1, horizon + 1):
                    for level in range(period):
                        sites += 1
                        if not black(j, level):
                            continue
                        top = level
                        while black(j, top + 1):
                            top += 1
                            require(top - level < period, "a full vertical period was black")
                        left = j
                        while left > 1 and black(left - 1, top):
                            left -= 1
                        value = amplitude(left, top)
                        require(value > 0, "the mixed character vanished at a triangle corner")
                        require(20 * value * 9**(j - left) * 2**(top - level) <= modulus, "a black site fell outside its constructed triangle")
                        tips.add((left, top % period))
                for left, top in tips:
                    value = amplitude(left, top)
                    right = left
                    while 20 * value * 9**(right + 1 - left) <= modulus:
                        right += 1
                    # Real right edge is <= max(H, depth/2+1)+log_9(Q).
                    require(9**(2 * right) <= 9**max(2 * horizon, depth + 2) * coprime**2, "a full triangle exceeded the denominator-based right margin")
                    require(black(right, top) and not black(right + 1, top), "a full triangle top row has an incorrect last column")
                    corners_checked += 1
    return sites, corners_checked


def check_mixed_numerators():
    words = classes = 0
    for length in range(1, 7):
        for clock in range(length, 3 * length + 1):
            numerators = []
            for cuts in combinations(range(1, clock), length - 1):
                totals = cuts + (clock,)
                numerator = sum(3**i * 2**(clock - s) for i, s in enumerate(totals))
                numerators.append(numerator)
            require(len(numerators) == len(set(numerators)), "distinct fixed-total words have a colliding numerator")
            words += len(numerators)
            for coprime in (5, 7, 25):
                modulus = 3**length * coprime
                buckets = defaultdict(list)
                for numerator in numerators:
                    buckets[numerator % modulus].append(numerator)
                for bucket in buckets.values():
                    require(modulus * len(bucket)**2 <= modulus * len(bucket) + 2 * sum(bucket), "the full-modulus numerator spacing bound failed")
                    classes += 1
    return words, classes


if __name__ == "__main__":
    paths, steps = check_ordinary_routes()
    print(f"Exact ordinary routes: {paths} paths, {steps} positive odd steps")
    sites, tips = check_triangle_geometry()
    print(f"Mixed triangle geometry: {sites} phase sites, {tips} full triangle corners")
    words, classes = check_mixed_numerators()
    print(f"Mixed numerator spacing: {words} fixed-total words, {classes} nonempty residue buckets")
