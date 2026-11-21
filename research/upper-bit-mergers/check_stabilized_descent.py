"""Verify a finite affine descent for an invariant label stabilized on high powers of 3."""

from collections import Counter
from heapq import heappop, heappush
from math import gcd

from check import walk


def normalize(a, b):
    for prime in (2, 3):
        while a % prime == b % prime == 0:
            a //= prime
            b //= prime
    return a, b


def moves(a, b, level):
    """Each pair represents the positive form a*t+b for every integer t >= 0."""
    if a % 2 == 0 and b % 2 == 1:
        for exponent in (1, *range(level, level + 5)):
            if exponent == 1 and (a % 3 != 0 or b % 3 == 0):
                continue
            power = 3**exponent
            yield normalize(power * a, power * b + 1)
    for exponent in range(1, 13):
        power = 2**exponent
        offset = power * b - 1
        exact_one = a % 9 == 0 and offset % 3 == 0 and offset % 9 != 0
        high = a % 3**level == 0 and offset % 3**level == 0
        if exact_one or high:
            yield normalize(power * a, offset)


def descent(modulus, residue, level):
    queue = [(modulus, residue)]
    seen = set(queue)
    for _ in range(2000):
        if not queue:
            break
        a, b = heappop(queue)
        for form in moves(a, b, level):
            slope, intercept = form
            if not (slope > 0 and intercept > 0):
                raise AssertionError((a, b, form))
            if slope < modulus:
                return form
            if slope <= 10000 * modulus and form not in seen:
                seen.add(form)
                heappush(queue, form)
    return None


def reaches_one(n):
    for _ in range(2000):
        if n == 1:
            return True
        n = walk(n, 1)[0]
    return False


def verify(level, ternary_modulus, max_binary):
    base_modulus = 2 * ternary_modulus
    active = [(base_modulus, r) for r in range(base_modulus) if gcd(r, 6) == 1]
    covered = Counter()
    exceptions = set()
    while active:
        modulus, residue = active.pop()
        result = descent(modulus, residue, level)
        if result is None:
            if modulus >= 2**max_binary * ternary_modulus:
                raise AssertionError(("uncovered class", modulus, residue))
            active.extend(((2 * modulus, residue), (2 * modulus, residue + modulus)))
            continue
        slope, intercept = result
        covered[modulus] += 1
        # Strict decrease holds once (modulus-slope)*t > intercept-residue.
        for t in range((intercept - residue) // (modulus - slope) + 1):
            exceptions.add(modulus * t + residue)
    if not all(reaches_one(n) for n in exceptions):
        raise AssertionError("a finite boundary input did not reach 1")
    print(f"level {level}: {sum(covered.values())} classes, largest modulus {max(covered)}, "
          f"{len(exceptions)} boundary inputs (largest {max(exceptions, default=0)}) reach 1")


if __name__ == "__main__":
    verify(level=6, ternary_modulus=81, max_binary=14)
